#!/usr/bin/env python3
"""Safe authoring, rendering, and validation for Ratiomera topic summaries.

Summary documents deliberately use a pipeline separate from the practice-PDF
pipeline. Each document starts with the same reviewed Markdown fragment used
by the corresponding website Summary tab, then retains the longer six-section
reference source and exactly three note pages. The renderer reads both trusted
sources, copies only the allowlisted PNG assets into an isolated temporary
Quarto project, and renders one PDF and one DOCX without source execution or a
network connection.
"""

from __future__ import annotations

import argparse
import html
import json
import os
import re
import shutil
import struct
import subprocess
import tempfile
import unicodedata
import zipfile
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Sequence
from xml.etree import ElementTree as ET


LOCALES = ("en", "de", "sq")
LANGUAGE_TAGS = {"en": "en-US", "de": "de-CH", "sq": "sq-AL"}
NOTE_PAGE_COUNT = 3
MINIMUM_CONTENT_PAGE_COUNT = 4
MAXIMUM_CONTENT_PAGE_COUNT = 14
MINIMUM_SOURCE_WORDS = 850
MINIMUM_SUMMARY_TAB_WORDS = 120
MINIMUM_PDF_BYTES = 20_000
MINIMUM_DOCX_BYTES = 12_000
A4_WIDTH_POINTS = 595.276
A4_HEIGHT_POINTS = 841.890
DOCX_PAGE_WIDTH_TWIPS = 11906
DOCX_PAGE_HEIGHT_TWIPS = 16838
DOCX_MARGIN_TWIPS = 1191
DOCX_CONTENT_WIDTH_TWIPS = DOCX_PAGE_WIDTH_TWIPS - (2 * DOCX_MARGIN_TWIPS)
DOCX_TABLE_STYLE_ID = "RatiomeraTable"
DOCX_BODY_FONT_HALF_POINTS = "22"
DOCX_TABLE_FONT_HALF_POINTS = "20"
DOCX_TABLE_CELL_HORIZONTAL_MARGIN = "110"
DOCX_TABLE_CELL_VERTICAL_MARGIN = "70"

# Stable, content-aware percentages for every Markdown data table in a topic
# summary, in document order.  The same profile is applied to EN, de-CH, and
# SQ so equivalent tables keep the same geometry across PDF and DOCX.  Widths
# are deliberately not inferred from a localized renderer's line wrapping.
TABLE_WIDTH_PROFILES: dict[str, tuple[tuple[int, ...], ...]] = {
    "01": (
        (21, 40, 39), (16, 28, 26, 30), (32, 24, 44), (26, 32, 42),
        (28, 28, 44), (26, 41, 33), (41, 59), (26, 33, 41),
        (24, 38, 38), (30, 37, 33),
    ),
    "02": (
        (31, 35, 34), (42, 58), (31, 32, 37), (26, 39, 35),
        (32, 24, 44), (30, 26, 44), (34, 27, 39), (28, 37, 35),
        (29, 35, 36),
    ),
    "03": ((22, 37, 41), (31, 38, 31), (28, 36, 36), (32, 28, 40), (33, 32, 35)),
    "04": ((42, 58), (25, 36, 39), (31, 32, 37), (30, 36, 34)),
    "05": ((35, 65), (32, 39, 29), (33, 32, 35), (32, 35, 33)),
    "06": ((44, 56), (31, 32, 37), (33, 30, 37), (29, 35, 36)),
    "07": ((41, 59), (29, 40, 31), (32, 33, 35), (26, 42, 32)),
    "08": ((18, 28, 24, 30), (42, 58), (29, 37, 34), (34, 30, 36), (34, 33, 33)),
}
TABLE_CAPTION_COUNTS = {
    "01": 8, "02": 6, "03": 2, "04": 1,
    "05": 1, "06": 1, "07": 1, "08": 2,
}
ALLOWED_EMPTY_DATA_CELLS: dict[str, dict[int, set[tuple[int, int]]]] = {
    # The one-way ANOVA summary table has no F statistic for Error or Total,
    # and Total has no mean square. These blanks carry meaning and are the only
    # empty body cells permitted by the document contract.
    "08": {0: {(2, 3), (3, 2), (3, 3)}},
}
PDF_FORCED_SECTION_BREAKS: dict[tuple[str, str], dict[str, tuple[str, ...]]] = {
    ("en", "01"): {"summary": ("## Linear Transformations {.cs-heading}",)},
    ("sq", "01"): {"summary": ("## Ndryshueshmëria {.cs-heading}",)},
    ("de", "08"): {
        "expanded": ("## Formelleitfaden", "## Verbindung zu anderen Themen"),
    },
}

TOPICS = {
    "01": ("descriptive-statistics", "topic-01-descriptive-statistics-summary-figure-en.png"),
    "02": ("probability", "topic-02-probability-summary-figure-en.png"),
    "03": ("hypothesis-testing", "topic-03-hypothesis-testing-summary-figure-en.png"),
    "04": ("covariance-correlation", "topic-04-covariance-correlation-summary-figure-en.png"),
    "05": ("simple-linear-regression", "topic-05-simple-linear-regression-summary-figure-en.png"),
    "06": ("partial-correlation", "topic-06-partial-correlation-summary-figure-en.png"),
    "07": ("multiple-regression", "topic-07-multiple-regression-summary-figure-en.png"),
    "08": ("analysis-of-variance", "topic-08-analysis-of-variance-summary-figure-en.png"),
}

SOURCE_NAME_RE = re.compile(
    r"^topic-(?P<number>\d{2})-"
    r"(?P<slug>[a-z0-9]+(?:-[a-z0-9]+)*)-"
    r"summary-(?P<locale>en|de|sq)\.md$"
)
OUTPUT_NAME_RE = re.compile(
    r"^topic-(?P<number>\d{2})-"
    r"(?P<slug>[a-z0-9]+(?:-[a-z0-9]+)*)-"
    r"summary-(?P<locale>en|de|sq)\.(?P<format>pdf|docx)$"
)
REQUIRED_METADATA = {
    "title",
    "subtitle",
    "document-id",
    "course-id",
    "topic-id",
    "topic-number",
    "topic-slug",
    "document-type",
    "locale",
    "figure-asset",
}
ALLOWED_METADATA = REQUIRED_METADATA
DOCUMENT_LABELS = {
    "en": {
        "headings": (
            "Purpose and foundations",
            "Core ideas",
            "Formula guide",
            "Reading the explanatory figure",
            "Interpretation checklist",
            "How this topic connects",
        ),
        "course": "Introduction to Statistics",
        "topic": "Topic {number}",
        "document-id": "Document ID",
        "course-summary": "Course-Page Summary",
        "expanded-reference": "Expanded Reference",
        "toc-title": "Table of contents",
        "figure-title": "Figure",
        "table-title": "Table",
        "subject": "Ratiomera Statistics topic summary",
        "notes": "Notes {page} of {count}",
        "notes-prefix": "Notes ",
    },
    "de": {
        "headings": (
            "Zweck und Grundlagen",
            "Zentrale Ideen",
            "Formelleitfaden",
            "Die erklärende Abbildung lesen",
            "Checkliste zur Interpretation",
            "Verbindung zu anderen Themen",
        ),
        "course": "Einführung in die Statistik",
        "topic": "Thema {number}",
        "document-id": "Dokument-ID",
        "course-summary": "Zusammenfassung der Kursseite",
        "expanded-reference": "Erweiterte Referenz",
        "toc-title": "Inhaltsverzeichnis",
        "figure-title": "Abbildung",
        "table-title": "Tabelle",
        "subject": "Themenzusammenfassung von Ratiomera Statistics",
        "notes": "Notizen {page} von {count}",
        "notes-prefix": "Notizen ",
    },
    "sq": {
        "headings": (
            "Qëllimi dhe bazat",
            "Idetë kryesore",
            "Udhëzuesi i formulave",
            "Si lexohet figura shpjeguese",
            "Lista e kontrollit për interpretim",
            "Si lidhet kjo temë me të tjerat",
        ),
        "course": "Hyrje në Statistikë",
        "topic": "Tema {number}",
        "document-id": "ID-ja e dokumentit",
        "course-summary": "Përmbledhja e faqes së kursit",
        "expanded-reference": "Referencë e zgjeruar",
        "toc-title": "Përmbajtja",
        "figure-title": "Figura",
        "table-title": "Tabela",
        "subject": "Përmbledhje teme nga Ratiomera Statistics",
        "notes": "Shënime {page} nga {count}",
        "notes-prefix": "Shënime ",
    },
}
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
M_NS = "http://schemas.openxmlformats.org/officeDocument/2006/math"
WP_NS = "http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing"
CP_NS = "http://schemas.openxmlformats.org/package/2006/metadata/core-properties"
DC_NS = "http://purl.org/dc/elements/1.1/"
DCTERMS_NS = "http://purl.org/dc/terms/"
EP_NS = "http://schemas.openxmlformats.org/officeDocument/2006/extended-properties"
DOCX_LAYOUT_STATISTICS = (
    "Pages", "Words", "Characters", "CharactersWithSpaces", "Lines",
    "Paragraphs", "TotalTime",
)

# Direct-child orders for the WordprocessingML property containers that the
# pipeline owns.  Word is forgiving, but several non-Microsoft renderers and
# the Open XML schema require these sequences and reject duplicate properties.
OOXML_PROPERTY_ORDER: dict[str, tuple[str, ...]] = {
    "pPr": (
        "pStyle", "keepNext", "keepLines", "pageBreakBefore", "framePr",
        "widowControl", "numPr", "suppressLineNumbers", "pBdr", "shd",
        "tabs", "suppressAutoHyphens", "kinsoku", "wordWrap",
        "overflowPunct", "topLinePunct", "autoSpaceDE", "autoSpaceDN",
        "bidi", "adjustRightInd", "snapToGrid", "spacing", "ind",
        "contextualSpacing", "mirrorIndents", "suppressOverlap", "jc",
        "textDirection", "textAlignment", "textboxTightWrap", "outlineLvl",
        "divId", "cnfStyle", "rPr", "sectPr", "pPrChange",
    ),
    "tblPr": (
        "tblStyle", "tblpPr", "tblOverlap", "bidiVisual",
        "tblStyleRowBandSize", "tblStyleColBandSize", "tblW", "jc",
        "tblCellSpacing", "tblInd", "tblBorders", "shd", "tblLayout",
        "tblCellMar", "tblLook", "tblCaption", "tblDescription", "tblPrChange",
    ),
    "tcPr": (
        "cnfStyle", "tcW", "gridSpan", "hMerge", "vMerge", "tcBorders",
        "shd", "noWrap", "tcMar", "textDirection", "tcFitText", "vAlign",
        "hideMark", "cellIns", "cellDel", "cellMerge", "tcPrChange",
    ),
    "trPr": (
        "cnfStyle", "divId", "gridBefore", "gridAfter", "wBefore", "wAfter",
        "trHeight", "hidden", "cantSplit", "tblHeader", "tblCellSpacing", "jc",
        "ins", "del", "trPrChange",
    ),
    "rPr": (
        "rStyle", "rFonts", "b", "bCs", "i", "iCs", "caps", "smallCaps",
        "strike", "dstrike", "outline", "shadow", "emboss", "imprint",
        "noProof", "snapToGrid", "vanish", "webHidden", "color", "spacing",
        "w", "kern", "position", "sz", "szCs", "highlight", "u", "effect",
        "bdr", "shd", "fitText", "vertAlign", "rtl", "cs", "em", "lang",
        "eastAsianLayout", "specVanish", "oMath", "rPrChange",
    ),
}

ET.register_namespace("w", W_NS)
ET.register_namespace("cp", CP_NS)
ET.register_namespace("dc", DC_NS)
ET.register_namespace("dcterms", DCTERMS_NS)
ET.register_namespace("xsi", "http://www.w3.org/2001/XMLSchema-instance")


class SummaryDocumentError(RuntimeError):
    """A summary source, asset, render, or validation failure."""


@dataclass(frozen=True)
class ProjectPaths:
    root: Path
    source_root: Path
    topic_summary_root: Path
    asset_root: Path
    logo: Path

    @classmethod
    def from_script(cls, script_path: Path) -> "ProjectPaths":
        root = script_path.resolve().parents[1]
        source_root = root / "ratiomera-statistics" / "_shared" / "summary-sources"
        topic_summary_root = root / "ratiomera-statistics" / "_shared" / "topic-summaries"
        asset_root = source_root / "assets"
        return cls(
            root=root,
            source_root=source_root,
            topic_summary_root=topic_summary_root,
            asset_root=asset_root,
            logo=asset_root / "ratiomera-summary-logo.png",
        )

    def locale_source_dir(self, locale: str) -> Path:
        return self.source_root / locale

    def topic_summary_path(self, locale: str, number: str) -> Path:
        return self.topic_summary_root / locale / f"t{number}.md"

    def output_dir(self, locale: str) -> Path:
        return self.root / "ratiomera-statistics" / locale / "downloads" / "files"


@dataclass(frozen=True)
class SummarySource:
    path: Path
    metadata: dict[str, str]
    body: str
    summary_tab_path: Path
    summary_tab_body: str
    summary_tab_headings: tuple[str, ...]
    number: str
    slug: str
    locale: str
    image_alt: str

    @property
    def document_id(self) -> str:
        return self.path.stem

    @property
    def topic_id(self) -> str:
        return f"topic-{self.number}-{self.slug}"

    @property
    def figure_asset(self) -> str:
        return self.metadata["figure-asset"]

    @property
    def pdf_name(self) -> str:
        return f"{self.document_id}.pdf"

    @property
    def docx_name(self) -> str:
        return f"{self.document_id}.docx"

    @property
    def summary_tab_anchors(self) -> tuple[str, ...]:
        return _summary_tab_text_anchors(self.summary_tab_body)


def _absolute(path: Path) -> Path:
    return Path(os.path.abspath(os.fspath(path)))


def _is_within(path: Path, parent: Path) -> bool:
    try:
        _absolute(path).relative_to(_absolute(parent))
        return True
    except ValueError:
        return False


def _reject_symlink_components(path: Path, *, anchor: Path) -> None:
    absolute = _absolute(path)
    anchor = _absolute(anchor)
    if not _is_within(absolute, anchor):
        raise SummaryDocumentError(f"path escapes its canonical root: {path}")
    current = anchor
    if current.is_symlink():
        raise SummaryDocumentError(f"symlink path component is not allowed: {current}")
    for part in absolute.relative_to(anchor).parts:
        current = current / part
        if os.path.lexists(current) and current.is_symlink():
            raise SummaryDocumentError(f"symlink path component is not allowed: {current}")


def validate_project_tree(paths: ProjectPaths) -> None:
    root = _absolute(paths.root)
    expected_source = root / "ratiomera-statistics" / "_shared" / "summary-sources"
    expected_topic_summaries = (
        root / "ratiomera-statistics" / "_shared" / "topic-summaries"
    )
    if _absolute(paths.source_root) != expected_source:
        raise SummaryDocumentError(
            f"summary source root must be the canonical path: {expected_source}"
        )
    if _absolute(paths.topic_summary_root) != expected_topic_summaries:
        raise SummaryDocumentError(
            "website topic-summary root must be the canonical path: "
            f"{expected_topic_summaries}"
        )
    if not root.is_dir() or root.is_symlink():
        raise SummaryDocumentError(f"project root must be a regular directory: {root}")
    _reject_symlink_components(expected_source, anchor=root)
    if not expected_source.is_dir() or expected_source.is_symlink():
        raise SummaryDocumentError(f"missing safe summary source root: {expected_source}")
    _reject_symlink_components(expected_topic_summaries, anchor=root)
    if not expected_topic_summaries.is_dir() or expected_topic_summaries.is_symlink():
        raise SummaryDocumentError(
            f"missing safe website topic-summary root: {expected_topic_summaries}"
        )
    _reject_symlink_components(paths.asset_root, anchor=root)
    if not paths.asset_root.is_dir() or paths.asset_root.is_symlink():
        raise SummaryDocumentError(f"missing safe summary asset root: {paths.asset_root}")


def _parse_scalar(raw: str, path: Path, line_number: int) -> str:
    value = raw.strip()
    if not value:
        return ""
    if value.startswith('"'):
        try:
            parsed = json.loads(value)
        except json.JSONDecodeError as exc:
            raise SummaryDocumentError(
                f"{path}:{line_number}: invalid quoted metadata: {exc.msg}"
            ) from exc
        if not isinstance(parsed, str):
            raise SummaryDocumentError(
                f"{path}:{line_number}: metadata values must be strings"
            )
        return parsed
    if value.startswith("'"):
        if len(value) < 2 or not value.endswith("'"):
            raise SummaryDocumentError(
                f"{path}:{line_number}: unterminated single-quoted metadata"
            )
        return value[1:-1].replace("''", "'")
    if " #" in value:
        value = value.split(" #", 1)[0].rstrip()
    return value


def split_front_matter(path: Path) -> tuple[dict[str, str], str]:
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        raise SummaryDocumentError(f"{path}: source must be UTF-8") from exc
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].strip() != "---":
        raise SummaryDocumentError(f"{path}: source must begin with YAML front matter")
    closing = next(
        (index for index, line in enumerate(lines[1:], start=1) if line.strip() in {"---", "..."}),
        None,
    )
    if closing is None:
        raise SummaryDocumentError(f"{path}: YAML front matter has no closing delimiter")
    metadata: dict[str, str] = {}
    key_re = re.compile(r"^(?P<key>[a-z][a-z0-9-]*):(?P<value>.*)$")
    for index, line in enumerate(lines[1:closing], start=2):
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        match = key_re.fullmatch(line.rstrip("\r\n"))
        if not match:
            raise SummaryDocumentError(
                f"{path}:{index}: front matter must use flat key: value entries"
            )
        key = match.group("key")
        if key in metadata:
            raise SummaryDocumentError(f"{path}:{index}: duplicate metadata key {key!r}")
        metadata[key] = _parse_scalar(match.group("value"), path, index)
    unknown = set(metadata) - ALLOWED_METADATA
    missing = REQUIRED_METADATA - set(metadata)
    if unknown:
        raise SummaryDocumentError(
            f"{path}: unsupported metadata keys: {', '.join(sorted(unknown))}"
        )
    if missing:
        raise SummaryDocumentError(
            f"{path}: missing metadata keys: {', '.join(sorted(missing))}"
        )
    if any(not metadata[key].strip() for key in REQUIRED_METADATA):
        raise SummaryDocumentError(f"{path}: required metadata values must not be empty")
    return metadata, "".join(lines[closing + 1 :])


def png_dimensions(path: Path) -> tuple[int, int]:
    data = path.read_bytes()[:24]
    if len(data) != 24 or not data.startswith(PNG_SIGNATURE) or data[12:16] != b"IHDR":
        raise SummaryDocumentError(f"{path}: asset is not a valid PNG")
    return struct.unpack(">II", data[16:24])


def _strip_markdown_for_word_count(body: str) -> str:
    text = re.sub(r"\$\$.*?\$\$", " ", body, flags=re.DOTALL)
    text = re.sub(r"!\[[^]]*\]\([^)]*\)(?:\{[^}]*\})?", " ", text)
    text = re.sub(r"[`*_#|{}$]", " ", text)
    return text


def _normalized_text(value: str) -> str:
    normalized = unicodedata.normalize("NFC", value).casefold()
    return " ".join(re.findall(r"[\w]+(?:['’-][\w]+)*", normalized))


def _summary_tab_text_anchors(body: str) -> tuple[str, ...]:
    """Return stable prose anchors from the beginning and end of a fragment."""
    candidates: list[str] = []
    for block in re.split(r"\n\s*\n", body.strip()):
        stripped = block.strip()
        if (
            not stripped
            or stripped.startswith(("#", "|", ":", "- ", "* ", "$$"))
            or "$" in stripped
        ):
            continue
        normalized = _normalized_text(stripped)
        words = normalized.split()
        if len(words) >= 12:
            candidates.append(" ".join(words[:12]))
    if not candidates:
        raise SummaryDocumentError(
            "website Summary-tab Markdown needs a substantive prose paragraph "
            "without inline mathematics"
        )
    return tuple(dict.fromkeys((candidates[0], candidates[-1])))


def _promote_summary_tab_headings(body: str) -> str:
    """Place website H3 subsections under the wrapper's trusted H1 part heading."""
    return re.sub(r"(?m)^###(?=\s)", "##", body)


def validate_summary_tab_body(body: str, path: Path) -> tuple[str, ...]:
    """Validate the shared Markdown used by both the website and downloads."""
    if not body.strip():
        raise SummaryDocumentError(f"{path}: website Summary-tab source is empty")
    if "\x00" in body or any(
        ord(character) < 32 and character not in "\n\r\t" for character in body
    ):
        raise SummaryDocumentError(
            f"{path}: website Summary-tab source contains control characters"
        )
    prohibited_patterns = {
        "fenced code or executable chunks": r"(?m)^\s*(?:`{3,}|~{3,})",
        "fenced divs": r"(?m)^\s*:::",
        "Quarto shortcodes or includes": r"\{\{[<%]",
        "raw output blocks": r"\{=(?:typst|openxml|html|latex|tex)\}",
        "HTML/XML elements": r"<\s*/?\s*[A-Za-z][^>]*>",
        "absolute or parent file paths": r"(?:file:/{0,2}|(?:^|[\s(])/(?:[^\s)]+)|\.\./)",
        "remote resources": r"(?i)(?:(?:https?|ftp)://|\bwww\.)",
        "script-like calls": r"(?i)\b(?:include|input|read|write|system|shell|import)\s*\(",
        "images": r"!\[[^]]*\]",
        "inline hyperlinks": r"(?<!!)\[[^]]+\]\([^)]+\)",
        "reference hyperlinks": r"(?<!!)\[[^]]+\]\[[^]]*\]",
        "link definitions": r"(?m)^\s*\[[^]]+\]:\s*\S+",
    }
    for label, pattern in prohibited_patterns.items():
        if re.search(pattern, body):
            raise SummaryDocumentError(
                f"{path}: website Summary-tab source contains prohibited {label}"
            )
    if "—" in body:
        raise SummaryDocumentError(
            f"{path}: website Summary-tab source contains an em dash"
        )
    if re.search(r"(?m)^#{1,2}\s+", body):
        raise SummaryDocumentError(
            f"{path}: the website page and trusted document wrapper own H1 and H2 headings"
        )
    malformed_heading = re.search(
        r"(?m)^#{3,6}\s+.*$", body
    )
    headings = tuple(
        match.group("title").strip()
        for match in re.finditer(
            r"(?m)^###\s+(?P<title>.+?)\s+\{\.cs-heading\}\s*$", body
        )
    )
    heading_line_count = len(re.findall(r"(?m)^#{3,6}\s+", body))
    if malformed_heading and len(headings) != heading_line_count:
        raise SummaryDocumentError(
            f"{path}: Summary-tab subsections must be H3 headings with .cs-heading"
        )
    if len(headings) < 2 or len(headings) != len(set(headings)):
        raise SummaryDocumentError(
            f"{path}: Summary-tab source needs at least two unique H3 subsections"
        )
    word_count = len(
        re.findall(r"\b[\w'-]+\b", _strip_markdown_for_word_count(body))
    )
    if word_count < MINIMUM_SUMMARY_TAB_WORDS:
        raise SummaryDocumentError(
            f"{path}: Summary-tab source has {word_count} words; at least "
            f"{MINIMUM_SUMMARY_TAB_WORDS} are required"
        )
    _summary_tab_text_anchors(body)
    return headings


def _document_labels(locale: str) -> dict[str, object]:
    labels = DOCUMENT_LABELS.get(locale)
    if labels is None:
        raise SummaryDocumentError(
            f"summary document labels have not been reviewed for locale: {locale}"
        )
    return labels


def validate_source_body(body: str, path: Path, figure_asset: str, locale: str) -> str:
    prohibited_patterns = {
        "fenced code or executable chunks": r"(?m)^\s*(?:`{3,}|~{3,})",
        "Quarto shortcodes or includes": r"\{\{[<%]",
        "raw output blocks": r"\{=(?:typst|openxml|html|latex|tex)\}",
        "HTML/XML elements": r"<\s*/?\s*[A-Za-z][^>]*>",
        "absolute or parent file paths": r"(?:file:/{0,2}|(?:^|[\s(])/(?:[^\s)]+)|\.\./)",
        "remote resources": r"(?:https?|ftp)://",
        "script-like calls": r"(?i)\b(?:include|input|read|write|system|shell|import)\s*\(",
    }
    for label, pattern in prohibited_patterns.items():
        if re.search(pattern, body):
            raise SummaryDocumentError(f"{path}: source contains prohibited {label}")
    if "—" in body:
        raise SummaryDocumentError(f"{path}: source contains an em dash")
    if re.search(r"(?i)\b(?:simply|just|obviously|clearly)\b", body):
        raise SummaryDocumentError(f"{path}: source contains a discouraged minimizing word")

    images = list(
        re.finditer(
            r"!\[(?P<alt>[^]]+)\]\((?P<target>[^)\s]+)\)(?:\{(?P<attrs>[^}]*)\})?",
            body,
        )
    )
    if len(images) != 1:
        raise SummaryDocumentError(
            f"{path}: source must contain exactly one registered explanatory figure"
        )
    image = images[0]
    expected_target = f"assets/{figure_asset}"
    if image.group("target") != expected_target:
        raise SummaryDocumentError(
            f"{path}: figure target must be {expected_target!r}"
        )
    image_alt = image.group("alt").strip()
    if len(image_alt.split()) < 18:
        raise SummaryDocumentError(f"{path}: figure alt text is too short")
    attrs = image.group("attrs") or ""
    expected_id = f"fig-summary-t{path.name[6:8]}"
    if f"#{expected_id}" not in attrs:
        raise SummaryDocumentError(f"{path}: figure must use stable ID {expected_id}")

    non_image_links = re.sub(
        r"!\[[^]]+\]\([^)]+\)(?:\{[^}]*\})?", "", body
    )
    if re.search(r"(?<!!)\[[^]]+\]\([^)]+\)", non_image_links):
        raise SummaryDocumentError(f"{path}: hyperlinks are not supported in summary sources")

    level_two = tuple(
        match.group(1).strip()
        for match in re.finditer(r"(?m)^##\s+(.+?)\s*$", body)
    )
    required_headings = _document_labels(locale)["headings"]
    if level_two != required_headings:
        raise SummaryDocumentError(
            f"{path}: level-two headings must be exactly: {' | '.join(required_headings)}"
        )
    if re.search(r"(?m)^#\s+", body):
        raise SummaryDocumentError(f"{path}: the trusted wrapper owns the document title")
    if re.search(r"(?m)^##\s+(?:Notes|Notizen|Shënime)\b", body):
        raise SummaryDocumentError(f"{path}: note pages are appended centrally")

    display_delimiters = len(re.findall(r"(?m)^\$\$\s*$", body))
    if display_delimiters < 6 or display_delimiters % 2:
        raise SummaryDocumentError(f"{path}: at least three complete display formulas are required")
    table_separators = len(
        re.findall(r"(?m)^\|(?:\s*:?-{3,}:?\s*\|){2,}\s*$", body)
    )
    if table_separators < 2:
        raise SummaryDocumentError(f"{path}: at least two Markdown tables are required")
    word_count = len(re.findall(r"\b[\w'-]+\b", _strip_markdown_for_word_count(body)))
    if word_count < MINIMUM_SOURCE_WORDS:
        raise SummaryDocumentError(
            f"{path}: source has {word_count} words; at least {MINIMUM_SOURCE_WORDS} are required"
        )
    return image_alt


def parse_source(path: Path, paths: ProjectPaths) -> SummarySource:
    path = _absolute(path)
    if path.is_symlink() or not path.is_file():
        raise SummaryDocumentError(f"{path}: source must be a regular, non-symlink file")
    match = SOURCE_NAME_RE.fullmatch(path.name)
    if not match:
        raise SummaryDocumentError(f"{path}: filename does not follow the summary contract")
    metadata, body = split_front_matter(path)
    number, slug, locale = match.group("number"), match.group("slug"), match.group("locale")
    if number not in TOPICS or TOPICS[number][0] != slug:
        raise SummaryDocumentError(f"{path}: topic number and slug are not registered")
    document = SummarySource(
        path=path.resolve(), metadata=metadata, body=body,
        summary_tab_path=Path(), summary_tab_body="", summary_tab_headings=(),
        number=number, slug=slug, locale=locale, image_alt="",
    )
    expected = {
        "document-id": document.document_id,
        "course-id": "intro-statistics",
        "topic-id": document.topic_id,
        "topic-number": number,
        "topic-slug": slug,
        "document-type": "summary",
        "locale": locale,
        "figure-asset": TOPICS[number][1].replace("-en.png", f"-{locale}.png"),
    }
    errors = [
        f"{key} must be {value!r}, found {metadata[key]!r}"
        for key, value in expected.items() if metadata[key] != value
    ]
    if errors:
        raise SummaryDocumentError(f"{path}: " + "; ".join(errors))
    if path.parent != paths.locale_source_dir(locale):
        raise SummaryDocumentError(f"{path}: source must be in the canonical {locale} directory")

    summary_tab_path = paths.topic_summary_path(locale, number)
    _reject_symlink_components(summary_tab_path, anchor=paths.root)
    if summary_tab_path.is_symlink() or not summary_tab_path.is_file():
        raise SummaryDocumentError(
            f"{path}: missing trusted website Summary-tab source {summary_tab_path}"
        )
    try:
        summary_tab_body = summary_tab_path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        raise SummaryDocumentError(
            f"{summary_tab_path}: website Summary-tab source must be UTF-8"
        ) from exc
    summary_tab_headings = validate_summary_tab_body(
        summary_tab_body, summary_tab_path
    )

    figure = paths.asset_root / locale / document.figure_asset
    _reject_symlink_components(figure, anchor=paths.root)
    if figure.is_symlink() or not figure.is_file():
        raise SummaryDocumentError(f"{path}: missing registered PNG figure {figure}")
    width, height = png_dimensions(figure)
    if width < 900 or height < 500:
        raise SummaryDocumentError(
            f"{figure}: explanatory figure is too small ({width} x {height})"
        )
    image_alt = validate_source_body(body, path, document.figure_asset, locale)
    return SummarySource(
        path=document.path, metadata=metadata, body=body,
        summary_tab_path=summary_tab_path.resolve(),
        summary_tab_body=summary_tab_body,
        summary_tab_headings=summary_tab_headings,
        number=number, slug=slug, locale=locale, image_alt=image_alt,
    )


def discover_sources(paths: ProjectPaths, locale: str) -> list[SummarySource]:
    validate_project_tree(paths)
    if locale not in LOCALES:
        raise SummaryDocumentError(f"unsupported summary locale: {locale}")
    locale_dir = paths.locale_source_dir(locale)
    _reject_symlink_components(locale_dir, anchor=paths.root)
    if not locale_dir.is_dir() or locale_dir.is_symlink():
        raise SummaryDocumentError(f"missing safe summary source locale directory: {locale_dir}")
    documents: list[SummarySource] = []
    for path in sorted(locale_dir.iterdir(), key=lambda item: item.name.casefold()):
        if path.is_symlink() or path.is_dir():
            raise SummaryDocumentError(f"nested or symlinked summary source is not allowed: {path}")
        if path.name in {".DS_Store", ".gitkeep"} or path.name.startswith("_"):
            continue
        if path.suffix.lower() != ".md" or not SOURCE_NAME_RE.fullmatch(path.name):
            raise SummaryDocumentError(f"unsupported file in summary source directory: {path}")
        documents.append(parse_source(path, paths))
    return documents


def validate_source_set(documents: Sequence[SummarySource], *, require_complete: bool) -> None:
    if require_complete and not documents:
        raise SummaryDocumentError("the requested locale has no summary sources")
    ids = [document.document_id for document in documents]
    if len(ids) != len(set(ids)):
        raise SummaryDocumentError("summary document IDs must be unique")
    by_locale: dict[str, dict[str, SummarySource]] = {}
    for document in documents:
        locale_topics = by_locale.setdefault(document.locale, {})
        if document.number in locale_topics:
            raise SummaryDocumentError(
                f"duplicate Topic {document.number} summary for {document.locale}"
            )
        locale_topics[document.number] = document
    if require_complete:
        for locale, topics in by_locale.items():
            missing = sorted(set(TOPICS) - set(topics))
            if missing:
                raise SummaryDocumentError(
                    f"{locale}: missing topic summary sources: {', '.join(missing)}"
                )


def select_documents(
    documents: Sequence[SummarySource], topic_numbers: Iterable[int] | None
) -> list[SummarySource]:
    if not topic_numbers:
        return list(documents)
    wanted = {f"{number:02d}" for number in topic_numbers}
    selected = [document for document in documents if document.number in wanted]
    missing = sorted(wanted - {document.number for document in selected})
    if missing:
        raise SummaryDocumentError(f"missing selected summary topics: {', '.join(missing)}")
    return selected


def _yaml_quote(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def _table_width_profile(document: SummarySource) -> tuple[tuple[int, ...], ...]:
    try:
        profile = TABLE_WIDTH_PROFILES[document.number]
    except KeyError as exc:
        raise SummaryDocumentError(
            f"no table-width profile is registered for topic {document.number}"
        ) from exc
    if not profile or any(
        len(widths) < 2
        or sum(widths) != 100
        or any(width < 12 or width > 72 for width in widths)
        for widths in profile
    ):
        raise SummaryDocumentError(
            f"topic {document.number} has an invalid table-width profile"
        )
    return profile


def build_table_width_filter(document: SummarySource) -> str:
    """Create the trusted Pandoc Lua filter used by both output formats."""
    rows = []
    for widths in _table_width_profile(document):
        rows.append("  {" + ", ".join(f"{width / 100:.2f}" for width in widths) + "}")
    profiles = ",\n".join(rows)
    return (
        "local profiles = {\n"
        + profiles
        + "\n}\n"
        "local table_index = 0\n\n"
        "function Table(tbl)\n"
        "  table_index = table_index + 1\n"
        "  local widths = profiles[table_index]\n"
        "  if widths == nil then\n"
        "    error('summary contains more Markdown tables than its owned profile')\n"
        "  end\n"
        "  if #widths ~= #tbl.colspecs then\n"
        "    error('summary table column count does not match its owned profile')\n"
        "  end\n"
        "  for index, colspec in ipairs(tbl.colspecs) do\n"
        "    local alignment = colspec[1]\n"
        "    if alignment == pandoc.AlignDefault then\n"
        "      alignment = pandoc.AlignLeft\n"
        "    end\n"
        "    tbl.colspecs[index] = {alignment, widths[index]}\n"
        "  end\n"
        "  return tbl\n"
        "end\n\n"
        "function Pandoc(doc)\n"
        "  if table_index ~= #profiles then\n"
        "    error('summary contains fewer Markdown tables than its owned profile')\n"
        "  end\n"
        "  return doc\n"
        "end\n"
    )


def _openxml_note_page(document: SummarySource, page_number: int) -> str:
    labels = _document_labels(document.locale)
    label = labels["notes"].format(page=page_number, count=NOTE_PAGE_COUNT)
    context = (
        f"{document.metadata['title']} | "
        f"{labels['topic'].format(number=int(document.number))}"
    )
    line_paragraphs = []
    for _ in range(20):
        line_paragraphs.append(
            '<w:p><w:pPr><w:spacing w:before="0" w:after="210"/>'
            '<w:pBdr><w:bottom w:val="single" w:sz="3" w:space="1" '
            'w:color="B8C6CF"/></w:pBdr></w:pPr><w:r><w:t xml:space="preserve"> </w:t></w:r></w:p>'
        )
    return "\n".join([
        '<w:p><w:r><w:br w:type="page"/></w:r></w:p>',
        '<w:p><w:pPr><w:pStyle w:val="Heading1"/></w:pPr><w:r><w:t>'
        + html.escape(label) + '</w:t></w:r></w:p>',
        '<w:p><w:r><w:rPr><w:color w:val="526A79"/><w:sz w:val="18"/>'
        '<w:szCs w:val="18"/></w:rPr><w:t>' + html.escape(context)
        + '</w:t></w:r></w:p>',
        *line_paragraphs,
    ])


def _typst_note_page(document: SummarySource, page_number: int) -> str:
    labels = _document_labels(document.locale)
    label = labels["notes"].format(page=page_number, count=NOTE_PAGE_COUNT)
    context = (
        f"{document.metadata['title']} | "
        f"{labels['topic'].format(number=int(document.number))}"
    )
    return "\n".join([
        "#pagebreak()",
        f'#text(size: 19pt, weight: "bold", fill: rgb("#183B56"))[{label}]',
        "#v(4pt)",
        f'#text(size: 9pt, fill: rgb("#526A79"))[{context}]',
        "#v(14pt)",
        '#for _ in range(20) [',
        '  #line(length: 100%, stroke: 0.45pt + rgb("#B8C6CF"))',
        "  #v(16pt)",
        "]",
    ])


def _insert_pdf_section_breaks(
    document: SummarySource, text: str, *, part: str
) -> str:
    headings = PDF_FORCED_SECTION_BREAKS.get(
        (document.locale, document.number), {}
    ).get(part, ())
    for heading in headings:
        count = text.count(heading)
        if count == 0:
            continue
        if count != 1:
            raise SummaryDocumentError(
                f"owned PDF page-break heading {heading!r} must occur exactly once"
            )
        text = text.replace(
            heading,
            "```{=typst}\n#pagebreak(weak: true)\n```\n\n" + heading,
            1,
        )
    return text


def build_wrapper(document: SummarySource) -> str:
    title = document.metadata["title"]
    subtitle = document.metadata["subtitle"]
    labels = _document_labels(document.locale)
    body_font_size = "11pt"
    note_blocks: list[str] = []
    for page_number in range(1, NOTE_PAGE_COUNT + 1):
        note_blocks.extend([
            "```{=typst}",
            _typst_note_page(document, page_number),
            "```",
            "",
            "```{=openxml}",
            _openxml_note_page(document, page_number),
            "```",
            "",
        ])
    front_matter = [
        "---",
        f"title: {_yaml_quote(title)}",
        f"subtitle: {_yaml_quote(subtitle)}",
        'author: "Ratiomera Statistics"',
        f"lang: {LANGUAGE_TAGS[document.locale]}",
        'mainfont: "Arial"',
        "number-sections: false",
        f"toc-title: {_yaml_quote(labels['toc-title'])}",
        "crossref:",
        f"  fig-title: {_yaml_quote(labels['figure-title'])}",
        f"  tbl-title: {_yaml_quote(labels['table-title'])}",
        "filters:",
        "  - _table-widths.lua",
        "format:",
        "  typst:",
        f"    fontsize: {body_font_size}",
        "    toc: true",
        "    toc-depth: 2",
        "    papersize: a4",
        "    margin:",
        "      x: 21mm",
        "      y: 19mm",
        "    include-in-header:",
        "      - text: |",
        "          #set par(justify: false)",
        "          #set text(hyphenate: false)",
        "          #set table(",
        '            inset: (x: 5pt, y: 4pt),',
        '            stroke: 0.45pt + rgb("#B8C6CF"),',
        '            fill: (x, y) => if y == 0 { rgb("#EAF2F6") } else { none },',
        "          )",
        "          #show table.cell: set par(justify: false)",
        '          #show table.cell.where(y: 0): set text(weight: "bold", fill: rgb("#183B56"))',
        "          #show heading: set block(sticky: true)",
        "  docx:",
        "    toc: false",
        "    reference-doc: _reference.docx",
        "execute:",
        "  enabled: false",
        "---",
        "",
    ]
    summary_body = _insert_pdf_section_breaks(
        document,
        _promote_summary_tab_headings(document.summary_tab_body).rstrip(),
        part="summary",
    )
    expanded_body = _insert_pdf_section_breaks(
        document, document.body.rstrip(), part="expanded"
    )
    brand_block = [
        "```{=typst}\n#pagebreak()\n```",
        "",
        "```{=openxml}\n<w:p><w:r><w:br w:type=\"page\"/></w:r></w:p>\n```",
        "",
        f"![Ratiomera logo](assets/{document.locale}/ratiomera-summary-logo.png){{width=1.25in}}  \n"
        f"**{labels['course']} | {labels['topic'].format(number=int(document.number))}**",
        "",
        f"# {labels['course-summary']}",
        "",
        summary_body,
        "",
        "```{=typst}\n#pagebreak()\n```",
        "",
        f"# {labels['expanded-reference']}",
        "",
        expanded_body,
        "",
        "---",
        "",
        f"*{labels['document-id']}: `{document.document_id}`*",
        "",
    ]
    return "\n".join(front_matter + brand_block + note_blocks).rstrip() + "\n"


def _safe_environment(workspace: Path) -> dict[str, str]:
    keep = (
        "PATH", "HOME", "USER", "LOGNAME", "LANG", "LC_ALL", "SHELL",
        "QUARTO_PANDOC", "QUARTO_DENO", "QUARTO_SHARE_PATH",
    )
    environment = {key: os.environ[key] for key in keep if key in os.environ}
    environment.update({
        "TMPDIR": str(workspace / "tmp"),
        "SOURCE_DATE_EPOCH": "0",
        "HTTP_PROXY": "http://127.0.0.1:9",
        "HTTPS_PROXY": "http://127.0.0.1:9",
        "ALL_PROXY": "http://127.0.0.1:9",
        "NO_PROXY": "localhost,127.0.0.1,::1",
    })
    return environment


def _run(command: Sequence[str], *, cwd: Path, environment: dict[str, str]) -> None:
    try:
        process = subprocess.run(
            list(command), cwd=cwd, env=environment,
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
            text=True, encoding="utf-8", errors="replace", timeout=180,
            check=False,
        )
    except subprocess.TimeoutExpired as exc:
        raise SummaryDocumentError(f"render command timed out: {' '.join(command)}") from exc
    if process.returncode:
        raise SummaryDocumentError(
            f"render command failed ({process.returncode}): {' '.join(command)}\n{process.stdout}"
        )


def _replace_child(parent: ET.Element, name: str) -> ET.Element:
    """Replace one direct WML child, retaining its earliest original position."""
    tag = f"{{{W_NS}}}{name}"
    children = list(parent)
    matches = [index for index, child in enumerate(children) if child.tag == tag]
    insertion_index = matches[0] if matches else len(children)
    for child in [child for child in list(parent) if child.tag == tag]:
        parent.remove(child)
    child = ET.Element(tag)
    parent.insert(min(insertion_index, len(parent)), child)
    return child


def _set_word_value(node: ET.Element, value: str) -> None:
    node.set(f"{{{W_NS}}}val", value)


def _wml_local_name(node: ET.Element) -> str:
    return node.tag.rsplit("}", 1)[-1]


def _canonicalize_ooxml_property_children(root: ET.Element) -> None:
    """Remove duplicate WML properties and sort owned containers by schema."""
    for parent in root.iter():
        parent_name = _wml_local_name(parent)
        order = OOXML_PROPERTY_ORDER.get(parent_name)
        if order is None:
            continue
        rank = {name: index for index, name in enumerate(order)}
        children = list(parent)
        # Keep the last occurrence because pipeline-owned properties are added
        # after Pandoc's defaults and therefore express the intended value.
        last_by_tag: dict[str, ET.Element] = {}
        for child in children:
            if child.tag.startswith(f"{{{W_NS}}}"):
                last_by_tag[child.tag] = child
        retained = [
            child
            for child in children
            if not child.tag.startswith(f"{{{W_NS}}}")
            or last_by_tag.get(child.tag) is child
        ]
        original_index = {id(child): index for index, child in enumerate(retained)}
        retained.sort(
            key=lambda child: (
                rank.get(_wml_local_name(child), len(rank) + original_index[id(child)]),
                original_index[id(child)],
            )
        )
        parent[:] = retained


def _validate_ooxml_property_children(root: ET.Element, path: Path) -> None:
    for parent in root.iter():
        parent_name = _wml_local_name(parent)
        order = OOXML_PROPERTY_ORDER.get(parent_name)
        if order is None:
            continue
        rank = {name: index for index, name in enumerate(order)}
        known = [
            _wml_local_name(child)
            for child in parent
            if child.tag.startswith(f"{{{W_NS}}}")
            and _wml_local_name(child) in rank
        ]
        if len(known) != len(set(known)):
            raise SummaryDocumentError(
                f"{path}: DOCX {parent_name} contains duplicate properties"
            )
        if [rank[name] for name in known] != sorted(rank[name] for name in known):
            raise SummaryDocumentError(
                f"{path}: DOCX {parent_name} properties are outside schema order: "
                + ", ".join(known)
            )


def _ensure_ratiomera_table_style(styles: ET.Element) -> None:
    """Install an owned, readable table style in the DOCX reference package."""
    existing = styles.find(
        f".//{{{W_NS}}}style[@{{{W_NS}}}styleId='{DOCX_TABLE_STYLE_ID}']"
    )
    if existing is not None:
        styles.remove(existing)

    style = ET.SubElement(styles, f"{{{W_NS}}}style")
    style.set(f"{{{W_NS}}}type", "table")
    style.set(f"{{{W_NS}}}customStyle", "1")
    style.set(f"{{{W_NS}}}styleId", DOCX_TABLE_STYLE_ID)
    name = ET.SubElement(style, f"{{{W_NS}}}name")
    _set_word_value(name, "Ratiomera data table")
    based_on = ET.SubElement(style, f"{{{W_NS}}}basedOn")
    _set_word_value(based_on, "Table")
    priority = ET.SubElement(style, f"{{{W_NS}}}uiPriority")
    _set_word_value(priority, "35")
    ET.SubElement(style, f"{{{W_NS}}}qFormat")

    paragraph_properties = ET.SubElement(style, f"{{{W_NS}}}pPr")
    spacing = ET.SubElement(paragraph_properties, f"{{{W_NS}}}spacing")
    spacing.set(f"{{{W_NS}}}before", "0")
    spacing.set(f"{{{W_NS}}}after", "40")
    spacing.set(f"{{{W_NS}}}line", "240")
    spacing.set(f"{{{W_NS}}}lineRule", "auto")
    ET.SubElement(paragraph_properties, f"{{{W_NS}}}widowControl")

    run_properties = ET.SubElement(style, f"{{{W_NS}}}rPr")
    fonts = ET.SubElement(run_properties, f"{{{W_NS}}}rFonts")
    for attribute in ("ascii", "hAnsi", "cs"):
        fonts.set(f"{{{W_NS}}}{attribute}", "Arial")
    for size_name in ("sz", "szCs"):
        size = ET.SubElement(run_properties, f"{{{W_NS}}}{size_name}")
        _set_word_value(size, DOCX_TABLE_FONT_HALF_POINTS)

    table_properties = ET.SubElement(style, f"{{{W_NS}}}tblPr")
    indent = ET.SubElement(table_properties, f"{{{W_NS}}}tblInd")
    indent.set(f"{{{W_NS}}}type", "dxa")
    indent.set(f"{{{W_NS}}}w", "0")

    header = ET.SubElement(style, f"{{{W_NS}}}tblStylePr")
    header.set(f"{{{W_NS}}}type", "firstRow")
    header_run = ET.SubElement(header, f"{{{W_NS}}}rPr")
    header_fonts = ET.SubElement(header_run, f"{{{W_NS}}}rFonts")
    for attribute in ("ascii", "hAnsi", "cs"):
        header_fonts.set(f"{{{W_NS}}}{attribute}", "Arial")
    ET.SubElement(header_run, f"{{{W_NS}}}b")
    color = ET.SubElement(header_run, f"{{{W_NS}}}color")
    _set_word_value(color, "183B56")
    for size_name in ("sz", "szCs"):
        size = ET.SubElement(header_run, f"{{{W_NS}}}{size_name}")
        _set_word_value(size, DOCX_TABLE_FONT_HALF_POINTS)
    header_cell = ET.SubElement(header, f"{{{W_NS}}}tcPr")
    shading = ET.SubElement(header_cell, f"{{{W_NS}}}shd")
    shading.set(f"{{{W_NS}}}fill", "EAF2F6")
    vertical = ET.SubElement(header_cell, f"{{{W_NS}}}vAlign")
    _set_word_value(vertical, "center")

    band = ET.SubElement(style, f"{{{W_NS}}}tblStylePr")
    band.set(f"{{{W_NS}}}type", "band1Horz")
    band_cell = ET.SubElement(band, f"{{{W_NS}}}tcPr")
    band_shading = ET.SubElement(band_cell, f"{{{W_NS}}}shd")
    band_shading.set(f"{{{W_NS}}}fill", "F3F7F9")


def _patch_reference_docx(path: Path, document: SummarySource) -> None:
    replacement = path.with_name(f".{path.name}.patched")
    with zipfile.ZipFile(path, "r") as source, zipfile.ZipFile(
        replacement, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9
    ) as target:
        for info in sorted(source.infolist(), key=lambda item: item.filename):
            data = source.read(info.filename)
            if info.filename == "word/document.xml":
                root = ET.fromstring(data)
                section = root.find(f".//{{{W_NS}}}sectPr")
                if section is None:
                    raise SummaryDocumentError(
                        "the default DOCX reference has no section properties"
                    )
                pg_size = section.find(f"{{{W_NS}}}pgSz")
                if pg_size is None:
                    pg_size = ET.SubElement(section, f"{{{W_NS}}}pgSz")
                pg_size.set(f"{{{W_NS}}}w", str(DOCX_PAGE_WIDTH_TWIPS))
                pg_size.set(f"{{{W_NS}}}h", str(DOCX_PAGE_HEIGHT_TWIPS))
                pg_margin = section.find(f"{{{W_NS}}}pgMar")
                if pg_margin is None:
                    pg_margin = ET.SubElement(section, f"{{{W_NS}}}pgMar")
                pg_margin.set(f"{{{W_NS}}}top", "1077")
                pg_margin.set(f"{{{W_NS}}}bottom", "1077")
                pg_margin.set(f"{{{W_NS}}}left", str(DOCX_MARGIN_TWIPS))
                pg_margin.set(f"{{{W_NS}}}right", str(DOCX_MARGIN_TWIPS))
                pg_margin.set(f"{{{W_NS}}}header", "720")
                pg_margin.set(f"{{{W_NS}}}footer", "720")
                pg_margin.set(f"{{{W_NS}}}gutter", "0")
                data = ET.tostring(root, encoding="utf-8", xml_declaration=True)
            elif info.filename == "word/styles.xml":
                root = ET.fromstring(data)
                for lang in root.findall(f".//{{{W_NS}}}lang"):
                    lang.set(f"{{{W_NS}}}val", LANGUAGE_TAGS[document.locale])
                normal = root.find(
                    f".//{{{W_NS}}}style[@{{{W_NS}}}styleId='Normal']"
                )
                if normal is None:
                    raise SummaryDocumentError(
                        "the default DOCX reference has no Normal style"
                    )
                run_properties = normal.find(f"{{{W_NS}}}rPr")
                if run_properties is None:
                    run_properties = ET.SubElement(normal, f"{{{W_NS}}}rPr")
                for name in ("sz", "szCs"):
                    size = run_properties.find(f"{{{W_NS}}}{name}")
                    if size is None:
                        size = ET.SubElement(run_properties, f"{{{W_NS}}}{name}")
                    size.set(f"{{{W_NS}}}val", DOCX_BODY_FONT_HALF_POINTS)
                normal_fonts = run_properties.find(f"{{{W_NS}}}rFonts")
                if normal_fonts is None:
                    normal_fonts = ET.SubElement(
                        run_properties, f"{{{W_NS}}}rFonts"
                    )
                for attribute in ("ascii", "hAnsi", "cs"):
                    normal_fonts.set(f"{{{W_NS}}}{attribute}", "Arial")
                for style_id in ("Caption", "TableCaption", "ImageCaption"):
                    caption_style = root.find(
                        f".//{{{W_NS}}}style[@{{{W_NS}}}styleId='{style_id}']"
                    )
                    if caption_style is None:
                        continue
                    caption_run = caption_style.find(f"{{{W_NS}}}rPr")
                    if caption_run is None:
                        caption_run = ET.SubElement(
                            caption_style, f"{{{W_NS}}}rPr"
                        )
                    caption_color = caption_run.find(f"{{{W_NS}}}color")
                    if caption_color is None:
                        caption_color = ET.SubElement(
                            caption_run, f"{{{W_NS}}}color"
                        )
                    _set_word_value(caption_color, "526A79")
                    caption_fonts = caption_run.find(f"{{{W_NS}}}rFonts")
                    if caption_fonts is None:
                        caption_fonts = ET.SubElement(
                            caption_run, f"{{{W_NS}}}rFonts"
                        )
                    for attribute in ("ascii", "hAnsi", "cs"):
                        caption_fonts.set(
                            f"{{{W_NS}}}{attribute}", "Arial"
                        )
                    for name in ("sz", "szCs"):
                        size = caption_run.find(f"{{{W_NS}}}{name}")
                        if size is None:
                            size = ET.SubElement(
                                caption_run, f"{{{W_NS}}}{name}"
                            )
                        _set_word_value(size, "18")
                for style_id in ("Heading1", "Heading2", "Heading3"):
                    heading_style = root.find(
                        f".//{{{W_NS}}}style[@{{{W_NS}}}styleId='{style_id}']"
                    )
                    if heading_style is None:
                        continue
                    heading_paragraph = heading_style.find(f"{{{W_NS}}}pPr")
                    if heading_paragraph is None:
                        heading_paragraph = ET.SubElement(
                            heading_style, f"{{{W_NS}}}pPr"
                        )
                    for property_name in ("keepNext", "keepLines", "widowControl"):
                        if heading_paragraph.find(
                            f"{{{W_NS}}}{property_name}"
                        ) is None:
                            ET.SubElement(
                                heading_paragraph, f"{{{W_NS}}}{property_name}"
                            )
                _ensure_ratiomera_table_style(root)
                _canonicalize_ooxml_property_children(root)
                data = ET.tostring(root, encoding="utf-8", xml_declaration=True)
            target.writestr(_normalized_zip_info(info.filename), data)
    os.replace(replacement, path)


def _normalized_zip_info(filename: str) -> zipfile.ZipInfo:
    info = zipfile.ZipInfo(filename=filename, date_time=(1980, 1, 1, 0, 0, 0))
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = 0o100644 << 16
    info.create_system = 3
    return info


def _docx_cell_text(cell: ET.Element) -> str:
    text = "".join(
        node.text or ""
        for node in cell.iter()
        if node.tag in {f"{{{W_NS}}}t", f"{{{M_NS}}}t"}
    )
    return " ".join(text.split())


def _profile_widths_twips(percentages: Sequence[int]) -> list[int]:
    widths = [round(DOCX_CONTENT_WIDTH_TWIPS * value / 100) for value in percentages]
    widths[-1] += DOCX_CONTENT_WIDTH_TWIPS - sum(widths)
    return widths


def _parent_chain(
    node: ET.Element, parent_map: dict[ET.Element, ET.Element]
) -> Iterable[ET.Element]:
    parent = parent_map.get(node)
    while parent is not None:
        yield parent
        parent = parent_map.get(parent)


def _set_docx_cell_margins(
    table_properties: ET.Element, *, horizontal: str, vertical: str
) -> None:
    margins = _replace_child(table_properties, "tblCellMar")
    for side, width in (
        ("top", vertical),
        ("left", horizontal),
        ("bottom", vertical),
        ("right", horizontal),
    ):
        margin = ET.SubElement(margins, f"{{{W_NS}}}{side}")
        margin.set(f"{{{W_NS}}}w", width)
        margin.set(f"{{{W_NS}}}type", "dxa")


def _set_docx_table_grid(table: ET.Element, widths: Sequence[int]) -> None:
    old_grid = table.find(f"{{{W_NS}}}tblGrid")
    if old_grid is not None:
        table.remove(old_grid)
    grid = ET.Element(f"{{{W_NS}}}tblGrid")
    for width in widths:
        column = ET.SubElement(grid, f"{{{W_NS}}}gridCol")
        column.set(f"{{{W_NS}}}w", str(width))
    properties = table.find(f"{{{W_NS}}}tblPr")
    insertion_index = list(table).index(properties) + 1 if properties is not None else 0
    table.insert(insertion_index, grid)


def _set_docx_borders(table_properties: ET.Element) -> None:
    borders = _replace_child(table_properties, "tblBorders")
    for side, size, color in (
        ("top", "6", "9FB2BF"),
        ("left", "4", "D4DEE4"),
        ("bottom", "6", "9FB2BF"),
        ("right", "4", "D4DEE4"),
        ("insideH", "4", "D4DEE4"),
        ("insideV", "4", "D4DEE4"),
    ):
        border = ET.SubElement(borders, f"{{{W_NS}}}{side}")
        border.set(f"{{{W_NS}}}val", "single")
        border.set(f"{{{W_NS}}}sz", size)
        border.set(f"{{{W_NS}}}space", "0")
        border.set(f"{{{W_NS}}}color", color)


def _set_docx_paragraph_layout(paragraph: ET.Element, *, header: bool) -> None:
    properties = paragraph.find(f"{{{W_NS}}}pPr")
    if properties is None:
        properties = ET.Element(f"{{{W_NS}}}pPr")
        paragraph.insert(0, properties)
    spacing = properties.find(f"{{{W_NS}}}spacing")
    if spacing is None:
        spacing = ET.SubElement(properties, f"{{{W_NS}}}spacing")
    spacing.set(f"{{{W_NS}}}before", "0")
    spacing.set(f"{{{W_NS}}}after", "40")
    spacing.set(f"{{{W_NS}}}line", "240")
    spacing.set(f"{{{W_NS}}}lineRule", "auto")
    for name in ("keepLines", "widowControl"):
        if properties.find(f"{{{W_NS}}}{name}") is None:
            ET.SubElement(properties, f"{{{W_NS}}}{name}")
    if header:
        alignment = _replace_child(properties, "jc")
        _set_word_value(alignment, "left")


def _set_docx_run_layout(run: ET.Element, *, header: bool) -> None:
    properties = run.find(f"{{{W_NS}}}rPr")
    if properties is None:
        properties = ET.Element(f"{{{W_NS}}}rPr")
        run.insert(0, properties)
    for name in ("sz", "szCs"):
        size = properties.find(f"{{{W_NS}}}{name}")
        if size is None:
            size = ET.SubElement(properties, f"{{{W_NS}}}{name}")
        _set_word_value(size, DOCX_TABLE_FONT_HALF_POINTS)
    if header:
        if properties.find(f"{{{W_NS}}}b") is None:
            ET.SubElement(properties, f"{{{W_NS}}}b")
        color = properties.find(f"{{{W_NS}}}color")
        if color is None:
            color = ET.SubElement(properties, f"{{{W_NS}}}color")
        _set_word_value(color, "183B56")


def _normalize_docx_data_table(
    table: ET.Element, percentages: Sequence[int]
) -> None:
    widths = _profile_widths_twips(percentages)
    rows = table.findall(f"{{{W_NS}}}tr")
    column_count = max(
        (len(row.findall(f"{{{W_NS}}}tc")) for row in rows), default=0
    )
    if column_count != len(widths):
        raise SummaryDocumentError(
            "DOCX table column count does not match its owned width profile"
        )
    properties = table.find(f"{{{W_NS}}}tblPr")
    if properties is None:
        properties = ET.Element(f"{{{W_NS}}}tblPr")
        table.insert(0, properties)
    style = _replace_child(properties, "tblStyle")
    _set_word_value(style, DOCX_TABLE_STYLE_ID)
    table_width = _replace_child(properties, "tblW")
    table_width.set(f"{{{W_NS}}}w", str(DOCX_CONTENT_WIDTH_TWIPS))
    table_width.set(f"{{{W_NS}}}type", "dxa")
    layout = _replace_child(properties, "tblLayout")
    _set_word_value(layout, "fixed")
    look = _replace_child(properties, "tblLook")
    look.set(f"{{{W_NS}}}firstRow", "1")
    look.set(f"{{{W_NS}}}lastRow", "0")
    look.set(f"{{{W_NS}}}firstColumn", "0")
    look.set(f"{{{W_NS}}}lastColumn", "0")
    look.set(f"{{{W_NS}}}noHBand", "0")
    look.set(f"{{{W_NS}}}noVBand", "1")
    look.set(f"{{{W_NS}}}val", "0220")
    _set_docx_cell_margins(
        properties,
        horizontal=DOCX_TABLE_CELL_HORIZONTAL_MARGIN,
        vertical=DOCX_TABLE_CELL_VERTICAL_MARGIN,
    )
    _set_docx_borders(properties)
    _set_docx_table_grid(table, widths)

    for row_index, row in enumerate(rows):
        row_properties = row.find(f"{{{W_NS}}}trPr")
        if row_properties is None:
            row_properties = ET.Element(f"{{{W_NS}}}trPr")
            row.insert(0, row_properties)
        if row_properties.find(f"{{{W_NS}}}cantSplit") is None:
            ET.SubElement(row_properties, f"{{{W_NS}}}cantSplit")
        if row_index == 0 and row_properties.find(f"{{{W_NS}}}tblHeader") is None:
            header = ET.SubElement(row_properties, f"{{{W_NS}}}tblHeader")
            _set_word_value(header, "on")
        for column, cell in enumerate(row.findall(f"{{{W_NS}}}tc")):
            cell_properties = cell.find(f"{{{W_NS}}}tcPr")
            if cell_properties is None:
                cell_properties = ET.Element(f"{{{W_NS}}}tcPr")
                cell.insert(0, cell_properties)
            cell_width = _replace_child(cell_properties, "tcW")
            cell_width.set(f"{{{W_NS}}}w", str(widths[column]))
            cell_width.set(f"{{{W_NS}}}type", "dxa")
            vertical = _replace_child(cell_properties, "vAlign")
            _set_word_value(vertical, "center" if row_index == 0 else "top")
            shading = _replace_child(cell_properties, "shd")
            shading.set(
                f"{{{W_NS}}}fill",
                "EAF2F6" if row_index == 0 else (
                    "F3F7F9" if row_index % 2 == 1 else "FFFFFF"
                ),
            )
            no_wrap = cell_properties.find(f"{{{W_NS}}}noWrap")
            if no_wrap is not None:
                cell_properties.remove(no_wrap)
            for paragraph in cell.iter(f"{{{W_NS}}}p"):
                _set_docx_paragraph_layout(paragraph, header=row_index == 0)
            for run in cell.iter(f"{{{W_NS}}}r"):
                _set_docx_run_layout(run, header=row_index == 0)


def _normalize_docx_container_table(table: ET.Element) -> None:
    """Make Quarto's one-cell figure/table float wrapper match the page width."""
    properties = table.find(f"{{{W_NS}}}tblPr")
    if properties is None:
        properties = ET.Element(f"{{{W_NS}}}tblPr")
        table.insert(0, properties)
    table_width = _replace_child(properties, "tblW")
    table_width.set(f"{{{W_NS}}}w", str(DOCX_CONTENT_WIDTH_TWIPS))
    table_width.set(f"{{{W_NS}}}type", "dxa")
    layout = _replace_child(properties, "tblLayout")
    _set_word_value(layout, "fixed")
    _set_docx_cell_margins(properties, horizontal="0", vertical="0")
    old_borders = properties.find(f"{{{W_NS}}}tblBorders")
    if old_borders is not None:
        properties.remove(old_borders)
    _set_docx_table_grid(table, [DOCX_CONTENT_WIDTH_TWIPS])
    rows = table.findall(f"{{{W_NS}}}tr")
    if rows:
        row_properties = rows[0].find(f"{{{W_NS}}}trPr")
        if row_properties is None:
            row_properties = ET.Element(f"{{{W_NS}}}trPr")
            rows[0].insert(0, row_properties)
        if row_properties.find(f"{{{W_NS}}}cantSplit") is None:
            ET.SubElement(row_properties, f"{{{W_NS}}}cantSplit")
        cells = rows[0].findall(f"{{{W_NS}}}tc")
        if cells:
            cell_properties = cells[0].find(f"{{{W_NS}}}tcPr")
            if cell_properties is None:
                cell_properties = ET.Element(f"{{{W_NS}}}tcPr")
                cells[0].insert(0, cell_properties)
            width = _replace_child(cell_properties, "tcW")
            width.set(f"{{{W_NS}}}w", str(DOCX_CONTENT_WIDTH_TWIPS))
            width.set(f"{{{W_NS}}}type", "dxa")
            for paragraph in cells[0].iter(f"{{{W_NS}}}p"):
                has_drawing = paragraph.find(f".//{{{W_NS}}}drawing") is not None
                text = "".join(
                    node.text or "" for node in paragraph.iter(f"{{{W_NS}}}t")
                ).strip()
                if has_drawing:
                    properties = paragraph.find(f"{{{W_NS}}}pPr")
                    if properties is None:
                        properties = ET.Element(f"{{{W_NS}}}pPr")
                        paragraph.insert(0, properties)
                    if properties.find(f"{{{W_NS}}}keepNext") is None:
                        ET.SubElement(properties, f"{{{W_NS}}}keepNext")
                elif text:
                    _set_docx_caption_style(paragraph, "ImageCaption")


def _merge_docx_paragraph_properties(root: ET.Element) -> None:
    """Collapse invalid duplicate pPr blocks emitted around cross-reference captions."""
    for paragraph in root.iter(f"{{{W_NS}}}p"):
        blocks = paragraph.findall(f"{{{W_NS}}}pPr")
        if len(blocks) <= 1:
            continue
        primary = blocks[0]
        for extra in blocks[1:]:
            for child in list(extra):
                previous = primary.find(child.tag)
                if previous is not None:
                    primary.remove(previous)
                primary.append(child)
            paragraph.remove(extra)
        if list(paragraph)[0] is not primary:
            paragraph.remove(primary)
            paragraph.insert(0, primary)


def _set_docx_caption_style(paragraph: ET.Element, style_id: str) -> None:
    properties = paragraph.find(f"{{{W_NS}}}pPr")
    if properties is None:
        properties = ET.Element(f"{{{W_NS}}}pPr")
        paragraph.insert(0, properties)
    style = properties.find(f"{{{W_NS}}}pStyle")
    if style is None:
        style = ET.SubElement(properties, f"{{{W_NS}}}pStyle")
    _set_word_value(style, style_id)
    for name in ("keepNext", "keepLines", "widowControl"):
        if properties.find(f"{{{W_NS}}}{name}") is None:
            ET.SubElement(properties, f"{{{W_NS}}}{name}")
    spacing = properties.find(f"{{{W_NS}}}spacing")
    if spacing is None:
        spacing = ET.SubElement(properties, f"{{{W_NS}}}spacing")
    spacing.set(f"{{{W_NS}}}before", "120")
    spacing.set(f"{{{W_NS}}}after", "80")


def _denest_docx_table_floats(root: ET.Element) -> int:
    """Replace Quarto's one-cell table floats with caption + body-level table."""
    parent_map = {child: parent for parent in root.iter() for child in parent}
    changed = 0
    for outer in list(root.iter(f"{{{W_NS}}}tbl")):
        rows = outer.findall(f"{{{W_NS}}}tr")
        if len(rows) != 1:
            continue
        cells = rows[0].findall(f"{{{W_NS}}}tc")
        if len(cells) != 1:
            continue
        nested = cells[0].find(f"{{{W_NS}}}tbl")
        if nested is None:
            continue
        parent = parent_map.get(outer)
        if parent is None:
            raise SummaryDocumentError("captioned DOCX table has no parent")
        insertion_index = list(parent).index(outer)
        retained: list[ET.Element] = []
        for child in list(cells[0]):
            if child.tag == f"{{{W_NS}}}tcPr":
                continue
            if child.tag == f"{{{W_NS}}}p":
                text = "".join(
                    node.text or "" for node in child.iter(f"{{{W_NS}}}t")
                ).strip()
                if text:
                    _set_docx_caption_style(child, "TableCaption")
                    retained.append(child)
                elif child is list(cells[0])[-1]:
                    retained.append(child)
            else:
                retained.append(child)
        if nested not in retained:
            raise SummaryDocumentError("captioned DOCX table lost its nested data table")
        parent.remove(outer)
        for offset, child in enumerate(retained):
            parent.insert(insertion_index + offset, child)
        changed += 1
    return changed


def _normalize_docx_horizontal_rules(root: ET.Element) -> int:
    """Replace legacy zero-width VML rules with stable paragraph borders."""
    changed = 0
    for paragraph in root.iter(f"{{{W_NS}}}p"):
        runs = [
            run for run in paragraph.findall(f"{{{W_NS}}}r")
            if run.find(f".//{{{W_NS}}}pict") is not None
        ]
        if not runs:
            continue
        for run in runs:
            paragraph.remove(run)
        properties = paragraph.find(f"{{{W_NS}}}pPr")
        if properties is None:
            properties = ET.Element(f"{{{W_NS}}}pPr")
            paragraph.insert(0, properties)
        borders = properties.find(f"{{{W_NS}}}pBdr")
        if borders is None:
            borders = ET.SubElement(properties, f"{{{W_NS}}}pBdr")
        bottom = borders.find(f"{{{W_NS}}}bottom")
        if bottom is None:
            bottom = ET.SubElement(borders, f"{{{W_NS}}}bottom")
        bottom.set(f"{{{W_NS}}}val", "single")
        bottom.set(f"{{{W_NS}}}sz", "4")
        bottom.set(f"{{{W_NS}}}space", "6")
        bottom.set(f"{{{W_NS}}}color", "B8C6CF")
        spacing = properties.find(f"{{{W_NS}}}spacing")
        if spacing is None:
            spacing = ET.SubElement(properties, f"{{{W_NS}}}spacing")
        spacing.set(f"{{{W_NS}}}before", "60")
        spacing.set(f"{{{W_NS}}}after", "100")
        changed += 1
    return changed


def _normalize_docx_drawing_accessibility(
    root: ET.Element, document: SummarySource
) -> None:
    drawing_properties = list(root.iter(f"{{{WP_NS}}}docPr"))
    if len(drawing_properties) != 2:
        raise SummaryDocumentError(
            "summary DOCX must contain one logo and one explanatory figure"
        )
    alternatives = (
        ("Ratiomera logo", "Ratiomera logo"),
        (
            f"{_document_labels(document.locale)['figure-title']} 1",
            document.image_alt,
        ),
    )
    for properties, (title, description) in zip(drawing_properties, alternatives):
        properties.set("title", title)
        properties.set("descr", description)


def _normalize_docx_part_break(root: ET.Element, document: SummarySource) -> None:
    label = str(_document_labels(document.locale)["expanded-reference"])
    matches = []
    for paragraph in root.iter(f"{{{W_NS}}}p"):
        text = "".join(node.text or "" for node in paragraph.iter(f"{{{W_NS}}}t"))
        if text.strip() == label:
            matches.append(paragraph)
    if len(matches) != 1:
        raise SummaryDocumentError(
            "the DOCX expanded-reference heading must occur exactly once"
        )
    paragraph = matches[0]
    properties = paragraph.find(f"{{{W_NS}}}pPr")
    if properties is None:
        properties = ET.Element(f"{{{W_NS}}}pPr")
        paragraph.insert(0, properties)
    if properties.find(f"{{{W_NS}}}pageBreakBefore") is None:
        ET.SubElement(properties, f"{{{W_NS}}}pageBreakBefore")


def _normalize_docx_app_properties(data: bytes) -> bytes:
    root = ET.fromstring(data)
    # Pandoc copies one-page placeholder statistics from its reference
    # document. They are false for generated summaries and cannot be
    # calculated without a specific Word layout engine, so omit them.
    for name in DOCX_LAYOUT_STATISTICS:
        node = root.find(f"{{{EP_NS}}}{name}")
        if node is not None:
            root.remove(node)
    application = root.find(f"{{{EP_NS}}}Application")
    if application is None:
        application = ET.SubElement(root, f"{{{EP_NS}}}Application")
    application.text = "Ratiomera document pipeline"
    return ET.tostring(root, encoding="utf-8", xml_declaration=True)


def normalize_docx(path: Path, document: SummarySource) -> None:
    replacement = path.with_name(f".{path.name}.normalized")
    with zipfile.ZipFile(path, "r") as source, zipfile.ZipFile(
        replacement, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9
    ) as target:
        for info in sorted(source.infolist(), key=lambda item: item.filename):
            data = source.read(info.filename)
            if info.filename == "docProps/core.xml":
                root = ET.fromstring(data)
                title_node = root.find(f"{{{DC_NS}}}title")
                if title_node is None:
                    title_node = ET.SubElement(root, f"{{{DC_NS}}}title")
                title_node.text = document.metadata["title"]
                subject_node = root.find(f"{{{DC_NS}}}subject")
                if subject_node is None:
                    subject_node = ET.SubElement(root, f"{{{DC_NS}}}subject")
                subject_node.text = str(
                    _document_labels(document.locale)["subject"]
                )
                for name in ("created", "modified"):
                    node = root.find(f"{{{DCTERMS_NS}}}{name}")
                    if node is not None:
                        node.text = "1970-01-01T00:00:00Z"
                data = ET.tostring(root, encoding="utf-8", xml_declaration=True)
            elif info.filename == "docProps/app.xml":
                data = _normalize_docx_app_properties(data)
            elif info.filename == "word/document.xml":
                root = ET.fromstring(data)
                _merge_docx_paragraph_properties(root)
                _denest_docx_table_floats(root)
                _normalize_docx_horizontal_rules(root)
                width_profiles = _table_width_profile(document)
                data_table_index = 0
                for table in list(root.iter(f"{{{W_NS}}}tbl")):
                    rows = table.findall(f"{{{W_NS}}}tr")
                    column_count = max(
                        (
                            len(row.findall(f"{{{W_NS}}}tc"))
                            for row in rows
                        ),
                        default=0,
                    )
                    if len(rows) >= 2 and column_count >= 2:
                        if data_table_index >= len(width_profiles):
                            raise SummaryDocumentError(
                                "DOCX contains more data tables than its owned profile"
                            )
                        _normalize_docx_data_table(
                            table, width_profiles[data_table_index]
                        )
                        data_table_index += 1
                    elif len(rows) == 1 and column_count == 1:
                        _normalize_docx_container_table(table)
                    else:
                        raise SummaryDocumentError(
                            "summary DOCX contains an unsupported table shape"
                        )
                if data_table_index != len(width_profiles):
                    raise SummaryDocumentError(
                        "DOCX contains fewer data tables than its owned profile"
                    )
                _normalize_docx_part_break(root, document)
                _normalize_docx_drawing_accessibility(root, document)
                _canonicalize_ooxml_property_children(root)
                data = ET.tostring(root, encoding="utf-8", xml_declaration=True)
            elif info.filename == "word/settings.xml":
                root = ET.fromstring(data)
                language = root.find(f"{{{W_NS}}}themeFontLang")
                if language is None:
                    language = ET.SubElement(root, f"{{{W_NS}}}themeFontLang")
                language.set(f"{{{W_NS}}}val", LANGUAGE_TAGS[document.locale])
                language.set(f"{{{W_NS}}}eastAsia", LANGUAGE_TAGS[document.locale])
                language.set(f"{{{W_NS}}}bidi", LANGUAGE_TAGS[document.locale])
                embedded = root.find(f"{{{W_NS}}}embedSystemFonts")
                if embedded is not None:
                    root.remove(embedded)
                data = ET.tostring(root, encoding="utf-8", xml_declaration=True)
            elif info.filename == "word/styles.xml":
                root = ET.fromstring(data)
                _canonicalize_ooxml_property_children(root)
                data = ET.tostring(root, encoding="utf-8", xml_declaration=True)
            elif info.filename == "word/numbering.xml":
                root = ET.fromstring(data)
                for level in root.iter(f"{{{W_NS}}}lvl"):
                    number_format = level.find(f"{{{W_NS}}}numFmt")
                    if (
                        number_format is None
                        or number_format.get(f"{{{W_NS}}}val") != "bullet"
                    ):
                        continue
                    level_text = level.find(f"{{{W_NS}}}lvlText")
                    if level_text is None:
                        level_text = ET.SubElement(level, f"{{{W_NS}}}lvlText")
                    _set_word_value(level_text, "•")
                    run_properties = level.find(f"{{{W_NS}}}rPr")
                    if run_properties is None:
                        run_properties = ET.SubElement(level, f"{{{W_NS}}}rPr")
                    fonts = run_properties.find(f"{{{W_NS}}}rFonts")
                    if fonts is None:
                        fonts = ET.SubElement(run_properties, f"{{{W_NS}}}rFonts")
                    for attribute in ("ascii", "hAnsi", "cs"):
                        fonts.set(f"{{{W_NS}}}{attribute}", "Arial")
                _canonicalize_ooxml_property_children(root)
                data = ET.tostring(root, encoding="utf-8", xml_declaration=True)
            target.writestr(_normalized_zip_info(info.filename), data)
    os.replace(replacement, path)


def _atomic_copy(source: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.exists() and destination.read_bytes() == source.read_bytes():
        return
    with tempfile.NamedTemporaryFile(
        mode="wb", dir=destination.parent, prefix=f".{destination.name}.",
        suffix=".tmp", delete=False,
    ) as handle:
        temporary = Path(handle.name)
        handle.write(source.read_bytes())
        handle.flush()
        os.fsync(handle.fileno())
    try:
        os.replace(temporary, destination)
        destination.chmod(0o644)
    finally:
        temporary.unlink(missing_ok=True)


def render_document(paths: ProjectPaths, document: SummarySource) -> tuple[Path, Path]:
    validate_project_tree(paths)
    output_dir = paths.output_dir(document.locale)
    _reject_symlink_components(output_dir, anchor=paths.root)
    if not output_dir.is_dir() or output_dir.is_symlink():
        raise SummaryDocumentError(f"missing safe output directory: {output_dir}")
    if not shutil.which("quarto") or not shutil.which("pandoc"):
        raise SummaryDocumentError("summary rendering requires local quarto and pandoc executables")
    logo = paths.asset_root / document.locale / "ratiomera-summary-logo.png"
    figure = paths.asset_root / document.locale / document.figure_asset
    for asset in (logo, figure):
        if asset.is_symlink() or not asset.is_file():
            raise SummaryDocumentError(f"missing safe registered asset: {asset}")
        png_dimensions(asset)

    with tempfile.TemporaryDirectory(prefix="ratiomera-summary-") as temporary_base:
        workspace = Path(temporary_base)
        (workspace / "tmp").mkdir()
        (workspace / "assets" / document.locale).mkdir(parents=True)
        shutil.copyfile(logo, workspace / "assets" / document.locale / logo.name)
        shutil.copyfile(figure, workspace / "assets" / figure.name)
        wrapper = workspace / "summary.qmd"
        wrapper.write_text(build_wrapper(document), encoding="utf-8", newline="\n")
        (workspace / "_table-widths.lua").write_text(
            build_table_width_filter(document), encoding="utf-8", newline="\n"
        )
        (workspace / "_quarto.yml").write_text(
            "project:\n  type: default\n  output-dir: _output\n  render:\n    - summary.qmd\n"
            "execute:\n  enabled: false\n",
            encoding="utf-8", newline="\n",
        )
        environment = _safe_environment(workspace)
        reference = workspace / "_reference.docx"
        with reference.open("wb") as handle:
            process = subprocess.run(
                ["pandoc", "--print-default-data-file", "reference.docx"],
                cwd=workspace, env=environment, stdout=handle, stderr=subprocess.PIPE,
                timeout=60, check=False,
            )
        if process.returncode:
            raise SummaryDocumentError(
                "could not create the owned DOCX reference document: "
                + process.stderr.decode("utf-8", errors="replace")
            )
        _patch_reference_docx(reference, document)
        _run(
            ["quarto", "render", "summary.qmd", "--to", "typst", "--output", document.pdf_name],
            cwd=workspace, environment=environment,
        )
        _run(
            ["quarto", "render", "summary.qmd", "--to", "docx", "--output", document.docx_name],
            cwd=workspace, environment=environment,
        )
        rendered_pdf = workspace / "_output" / document.pdf_name
        rendered_docx = workspace / "_output" / document.docx_name
        if not rendered_pdf.is_file() or not rendered_docx.is_file():
            raise SummaryDocumentError("Quarto did not create both expected summary formats")
        normalize_pdf_metadata(rendered_pdf, document)
        normalize_docx(rendered_docx, document)
        validate_pdf(document, rendered_pdf)
        validate_docx(document, rendered_docx)
        destination_pdf = output_dir / document.pdf_name
        destination_docx = output_dir / document.docx_name
        _atomic_copy(rendered_pdf, destination_pdf)
        _atomic_copy(rendered_docx, destination_docx)
    return destination_pdf, destination_docx


def extract_pdf_text(path: Path) -> tuple[list[str], int]:
    try:
        from pypdf import PdfReader
    except ImportError as exc:
        raise SummaryDocumentError("PDF validation requires the installed pypdf package") from exc
    try:
        reader = PdfReader(path)
        pages = [(page.extract_text() or "") for page in reader.pages]
        for page_number, page in enumerate(reader.pages, start=1):
            width = float(page.mediabox.width)
            height = float(page.mediabox.height)
            if (
                abs(width - A4_WIDTH_POINTS) > 1.0
                or abs(height - A4_HEIGHT_POINTS) > 1.0
            ):
                raise SummaryDocumentError(
                    f"{path}: PDF page {page_number} is not A4 portrait "
                    f"({width:.1f} x {height:.1f} points)"
                )
    except SummaryDocumentError:
        raise
    except Exception as exc:
        raise SummaryDocumentError(f"{path}: could not read PDF: {exc}") from exc
    return pages, len(pages)


def _expected_pdf_metadata(document: SummarySource) -> dict[str, str]:
    return {
        "/Title": document.metadata["title"],
        "/Author": "Ratiomera Statistics",
        "/Subject": str(_document_labels(document.locale)["subject"]),
        "/Creator": "Ratiomera document pipeline",
        "/Producer": "Ratiomera document pipeline",
        "/Keywords": document.document_id,
        "/CreationDate": "D:19700101000000Z",
        "/ModDate": "D:19700101000000Z",
    }


def normalize_pdf_metadata(path: Path, document: SummarySource) -> None:
    """Write deterministic, branded PDF metadata without altering page content."""
    try:
        from pypdf import PdfReader, PdfWriter
        from pypdf.generic import NameObject, TextStringObject
    except ImportError as exc:
        raise SummaryDocumentError(
            "PDF metadata normalization requires the installed pypdf package"
        ) from exc
    replacement = path.with_name(f".{path.name}.metadata")
    try:
        reader = PdfReader(path)
        if reader.is_encrypted:
            raise SummaryDocumentError(f"{path}: summary PDF must not be encrypted")
        writer = PdfWriter(clone_from=reader)
        writer.add_metadata(_expected_pdf_metadata(document))
        writer.root_object[NameObject("/Lang")] = TextStringObject(
            LANGUAGE_TAGS[document.locale]
        )
        with replacement.open("wb") as handle:
            writer.write(handle)
        os.replace(replacement, path)
    except SummaryDocumentError:
        replacement.unlink(missing_ok=True)
        raise
    except Exception as exc:
        replacement.unlink(missing_ok=True)
        raise SummaryDocumentError(
            f"{path}: could not normalize PDF metadata: {exc}"
        ) from exc


def validate_pdf_metadata(document: SummarySource, path: Path) -> None:
    try:
        from pypdf import PdfReader
    except ImportError as exc:
        raise SummaryDocumentError(
            "PDF metadata validation requires the installed pypdf package"
        ) from exc
    try:
        reader = PdfReader(path)
        metadata = reader.metadata or {}
        language = reader.trailer["/Root"].get("/Lang")
    except Exception as exc:
        raise SummaryDocumentError(
            f"{path}: could not read PDF metadata: {exc}"
        ) from exc
    expected = _expected_pdf_metadata(document)
    mismatches = [
        f"{key}={metadata.get(key)!r}, expected {value!r}"
        for key, value in expected.items()
        if metadata.get(key) != value
    ]
    if mismatches:
        raise SummaryDocumentError(
            f"{path}: PDF metadata mismatch: {'; '.join(mismatches)}"
        )
    if str(language) != LANGUAGE_TAGS[document.locale]:
        raise SummaryDocumentError(
            f"{path}: PDF language is {language!r}, expected "
            f"{LANGUAGE_TAGS[document.locale]!r}"
        )


def _validate_summary_tab_output(
    document: SummarySource, extracted_text: str, path: Path
) -> None:
    normalized_output = _normalized_text(extracted_text)
    # PDF text extractors do not represent inline mathematical glyphs
    # consistently (for example, heading `$r$` may become an italic Unicode
    # character or disappear from the heading text).  Verify the stable prose
    # portion of each heading here; formulas are preserved separately by the
    # source contract and the representative fragment anchors below.
    heading_anchors = tuple(
        anchor
        for heading in document.summary_tab_headings
        for segment in re.split(r"\$[^$]*\$", heading)
        if (anchor := _normalized_text(segment))
    )
    required_fragments = (
        *document.summary_tab_anchors,
        *(anchor for anchor in heading_anchors if anchor),
    )
    # Long German and Albanian words may be line-hyphenated or split into two
    # extractor tokens in PDF text. Comparing a whitespace/punctuation-free
    # form keeps the required multiword anchors strict while making the check
    # independent of renderer line breaks.
    compact_output = re.sub(r"[-'’\s]+", "", normalized_output)
    missing = [
        fragment
        for fragment in required_fragments
        if re.sub(r"[-'’\s]+", "", fragment) not in compact_output
    ]
    if missing:
        raise SummaryDocumentError(
            f"{path}: output does not retain the shared website Summary-tab "
            f"content; missing normalized text: {', '.join(missing)}"
        )


def validate_pdf(document: SummarySource, path: Path) -> tuple[int, int]:
    if path.is_symlink() or not path.is_file():
        raise SummaryDocumentError(f"{path}: PDF must be a regular file")
    data = path.read_bytes()
    if len(data) < MINIMUM_PDF_BYTES or not data.startswith(b"%PDF-"):
        raise SummaryDocumentError(f"{path}: PDF is missing its header or substantive content")
    if b"%%EOF" not in data[-2048:]:
        raise SummaryDocumentError(f"{path}: PDF lacks a final EOF marker")
    if b"<svg" in data.lower() or b"image/svg+xml" in data.lower():
        raise SummaryDocumentError(f"{path}: PDF contains prohibited SVG data")
    validate_pdf_metadata(document, path)
    pages, page_count = extract_pdf_text(path)
    content_page_count = page_count - NOTE_PAGE_COUNT
    if not MINIMUM_CONTENT_PAGE_COUNT <= content_page_count <= MAXIMUM_CONTENT_PAGE_COUNT:
        raise SummaryDocumentError(
            f"{path}: summary PDF must have {MINIMUM_CONTENT_PAGE_COUNT} to "
            f"{MAXIMUM_CONTENT_PAGE_COUNT} content pages followed by exactly "
            f"{NOTE_PAGE_COUNT} note pages; found {content_page_count} content pages "
            f"and {page_count} pages in total"
        )
    text = "\n".join(pages)
    control_characters = sorted({
        character
        for character in text
        if unicodedata.category(character) == "Cc"
        and character not in {"\n", "\r", "\t"}
    })
    if control_characters:
        codes = ", ".join(f"U+{ord(character):04X}" for character in control_characters)
        examples = []
        for index, character in enumerate(text):
            if character in control_characters:
                examples.append(repr(text[max(0, index - 24):index + 25]))
            if len(examples) == 4:
                break
        raise SummaryDocumentError(
            f"{path}: PDF text layer contains control characters: {codes}; "
            f"contexts: {'; '.join(examples)}"
        )
    labels = _document_labels(document.locale)
    required_text = (
        document.metadata["title"], document.document_id,
        labels["document-id"], labels["course-summary"],
        labels["expanded-reference"], labels["toc-title"], labels["figure-title"],
        *labels["headings"],
    )
    missing = [item for item in required_text if item not in text]
    if missing:
        raise SummaryDocumentError(f"{path}: PDF text lacks: {', '.join(missing)}")
    compact_table_label = re.sub(r"\s+", "", str(labels["table-title"]))
    table_caption_count = sum(
        bool(
            re.match(
                rf"^{re.escape(compact_table_label)}\d+:",
                re.sub(r"\s+", "", line),
            )
        )
        for line in text.splitlines()
    )
    if table_caption_count != TABLE_CAPTION_COUNTS[document.number]:
        caption_candidates = [
            repr(line)
            for line in text.splitlines()
            if str(labels["table-title"]) in line
        ][:8]
        raise SummaryDocumentError(
            f"{path}: expected {TABLE_CAPTION_COUNTS[document.number]} localized "
            f"table captions, found {table_caption_count}; candidates: "
            + "; ".join(caption_candidates)
        )
    _validate_summary_tab_output(document, text, path)
    expected_note_labels = [
        labels["notes"].format(page=page, count=NOTE_PAGE_COUNT)
        for page in range(1, NOTE_PAGE_COUNT + 1)
    ]
    last_pages = pages[-NOTE_PAGE_COUNT:]
    for label, page_text in zip(expected_note_labels, last_pages):
        if label not in page_text:
            raise SummaryDocumentError(
                f"{path}: final note pages are not exactly ordered; missing {label!r}"
            )
    if any(labels["notes-prefix"] in page for page in pages[:-NOTE_PAGE_COUNT]):
        raise SummaryDocumentError(f"{path}: note content appears before the final three pages")
    return page_count, len(text)


def _docx_text(document_xml: bytes) -> str:
    root = ET.fromstring(document_xml)
    return "\n".join(
        node.text or ""
        for node in root.iter()
        if node.tag in {f"{{{W_NS}}}t", f"{{{M_NS}}}t"}
    )


def validate_docx(document: SummarySource, path: Path) -> tuple[int, int]:
    if path.is_symlink() or not path.is_file():
        raise SummaryDocumentError(f"{path}: DOCX must be a regular file")
    if path.stat().st_size < MINIMUM_DOCX_BYTES:
        raise SummaryDocumentError(f"{path}: DOCX is unexpectedly small")
    try:
        with zipfile.ZipFile(path, "r") as archive:
            names = archive.namelist()
            if len(names) != len(set(names)):
                raise SummaryDocumentError(f"{path}: DOCX contains duplicate ZIP entries")
            required = {
                "[Content_Types].xml", "word/document.xml", "word/styles.xml",
                "word/settings.xml", "word/numbering.xml",
                "docProps/core.xml", "docProps/app.xml",
            }
            for name in names:
                pure = Path(name)
                if pure.is_absolute() or ".." in pure.parts:
                    raise SummaryDocumentError(f"{path}: unsafe DOCX ZIP member {name!r}")
                lowered = name.lower()
                if lowered.endswith(".svg"):
                    raise SummaryDocumentError(f"{path}: DOCX contains prohibited SVG media")
            if not required.issubset(names):
                raise SummaryDocumentError(f"{path}: DOCX lacks required package parts")
            xml_parts = [
                (name, archive.read(name)) for name in names
                if name.endswith((".xml", ".rels"))
            ]
            for name, data in xml_parts:
                try:
                    ET.fromstring(data)
                except ET.ParseError as exc:
                    raise SummaryDocumentError(
                        f"{path}: malformed XML package part {name}: {exc}"
                    ) from exc
            all_xml = b"\n".join(data for _name, data in xml_parts)
            if b"<svg" in all_xml.lower() or b"image/svg+xml" in all_xml.lower():
                raise SummaryDocumentError(f"{path}: DOCX embeds prohibited SVG data")
            if re.search(br'TargetMode=["\']External["\']', all_xml, flags=re.IGNORECASE):
                raise SummaryDocumentError(f"{path}: DOCX contains an external relationship")
            media_names = [name for name in names if name.startswith("word/media/")]
            if len(media_names) < 2 or any(not name.lower().endswith(".png") for name in media_names):
                raise SummaryDocumentError(
                    f"{path}: DOCX must embed the raster logo and explanatory PNG figure"
                )
            for name in media_names:
                if not archive.read(name).startswith(PNG_SIGNATURE):
                    raise SummaryDocumentError(f"{path}: non-PNG media found in {name}")
            document_xml = archive.read("word/document.xml")
            styles_xml = archive.read("word/styles.xml")
            settings_xml = archive.read("word/settings.xml")
            numbering_xml = archive.read("word/numbering.xml")
            core_xml = archive.read("docProps/core.xml")
            app_xml = archive.read("docProps/app.xml")
    except zipfile.BadZipFile as exc:
        raise SummaryDocumentError(f"{path}: DOCX is not a valid ZIP package") from exc
    text = _docx_text(document_xml)
    core_root = ET.fromstring(core_xml)
    core_expected = {
        (DC_NS, "title"): document.metadata["title"],
        (DC_NS, "creator"): "Ratiomera Statistics",
        (DC_NS, "language"): LANGUAGE_TAGS[document.locale],
        (DC_NS, "subject"): str(
            _document_labels(document.locale)["subject"]
        ),
        (DCTERMS_NS, "created"): "1970-01-01T00:00:00Z",
        (DCTERMS_NS, "modified"): "1970-01-01T00:00:00Z",
    }
    core_mismatches = []
    for (namespace, name), expected_value in core_expected.items():
        node = core_root.find(f"{{{namespace}}}{name}")
        if node is None or node.text != expected_value:
            core_mismatches.append(f"{name}={None if node is None else node.text!r}")
    if core_mismatches:
        raise SummaryDocumentError(
            f"{path}: DOCX core metadata mismatch: {'; '.join(core_mismatches)}"
        )
    app_root = ET.fromstring(app_xml)
    application = app_root.find(f"{{{EP_NS}}}Application")
    if application is None or application.text != "Ratiomera document pipeline":
        raise SummaryDocumentError(f"{path}: DOCX application metadata is not owned")
    stale_statistics = [
        name for name in DOCX_LAYOUT_STATISTICS
        if app_root.find(f"{{{EP_NS}}}{name}") is not None
    ]
    if stale_statistics:
        raise SummaryDocumentError(
            f"{path}: DOCX contains stale layout statistics: "
            f"{', '.join(stale_statistics)}"
        )
    labels = _document_labels(document.locale)
    expected_note_labels = {
        labels["notes"].format(page=page, count=NOTE_PAGE_COUNT)
        for page in range(1, NOTE_PAGE_COUNT + 1)
    }
    required_text = (
        document.metadata["title"], document.document_id,
        labels["document-id"], labels["course-summary"],
        labels["expanded-reference"], labels["figure-title"], labels["table-title"],
        *labels["headings"],
        *sorted(expected_note_labels),
    )
    missing = [item for item in required_text if item not in text]
    if missing:
        raise SummaryDocumentError(f"{path}: DOCX text lacks: {', '.join(missing)}")
    _validate_summary_tab_output(document, text, path)
    root = ET.fromstring(document_xml)
    styles_root = ET.fromstring(styles_xml)
    numbering_root = ET.fromstring(numbering_xml)
    _validate_ooxml_property_children(root, path)
    _validate_ooxml_property_children(styles_root, path)
    _validate_ooxml_property_children(numbering_root, path)
    owned_style = styles_root.find(
        f".//{{{W_NS}}}style[@{{{W_NS}}}styleId='{DOCX_TABLE_STYLE_ID}']"
    )
    if owned_style is None:
        raise SummaryDocumentError(f"{path}: DOCX lacks the owned table style")
    normal_style = styles_root.find(
        f".//{{{W_NS}}}style[@{{{W_NS}}}styleId='Normal']"
    )
    normal_run = normal_style.find(f"{{{W_NS}}}rPr") if normal_style is not None else None
    normal_size = normal_run.find(f"{{{W_NS}}}sz") if normal_run is not None else None
    normal_fonts = normal_run.find(f"{{{W_NS}}}rFonts") if normal_run is not None else None
    if (
        normal_size is None
        or normal_size.get(f"{{{W_NS}}}val") != DOCX_BODY_FONT_HALF_POINTS
        or normal_fonts is None
        or any(
            normal_fonts.get(f"{{{W_NS}}}{attribute}") != "Arial"
            for attribute in ("ascii", "hAnsi", "cs")
        )
    ):
        raise SummaryDocumentError(f"{path}: DOCX body typography is not owned")
    for style_id in ("Heading1", "Heading2", "Heading3"):
        heading_style = styles_root.find(
            f".//{{{W_NS}}}style[@{{{W_NS}}}styleId='{style_id}']"
        )
        heading_properties = (
            heading_style.find(f"{{{W_NS}}}pPr")
            if heading_style is not None else None
        )
        if heading_properties is None or any(
            heading_properties.find(f"{{{W_NS}}}{name}") is None
            for name in ("keepNext", "keepLines", "widowControl")
        ):
            raise SummaryDocumentError(
                f"{path}: DOCX {style_id} does not keep headings with their content"
            )

    settings_root = ET.fromstring(settings_xml)
    theme_language = settings_root.find(f"{{{W_NS}}}themeFontLang")
    if theme_language is None or any(
        theme_language.get(f"{{{W_NS}}}{attribute}")
        != LANGUAGE_TAGS[document.locale]
        for attribute in ("val", "eastAsia", "bidi")
    ):
        raise SummaryDocumentError(f"{path}: DOCX theme language is not localized")
    if settings_root.find(f"{{{W_NS}}}embedSystemFonts") is not None:
        raise SummaryDocumentError(f"{path}: DOCX falsely requests system-font embedding")

    bullet_levels = []
    for level in numbering_root.iter(f"{{{W_NS}}}lvl"):
        number_format = level.find(f"{{{W_NS}}}numFmt")
        if number_format is not None and number_format.get(f"{{{W_NS}}}val") == "bullet":
            bullet_levels.append(level)
    if not bullet_levels or any(
        (level.find(f"{{{W_NS}}}lvlText") is None)
        or level.find(f"{{{W_NS}}}lvlText").get(f"{{{W_NS}}}val") != "•"
        for level in bullet_levels
    ):
        raise SummaryDocumentError(f"{path}: DOCX bullets are not portable Unicode")

    if any(
        len(paragraph.findall(f"{{{W_NS}}}pPr")) > 1
        for paragraph in root.iter(f"{{{W_NS}}}p")
    ):
        raise SummaryDocumentError(f"{path}: DOCX contains duplicate paragraph properties")
    if any(root.iter(f"{{{W_NS}}}pict")):
        raise SummaryDocumentError(f"{path}: DOCX contains legacy VML separators")
    drawing_properties = list(root.iter(f"{{{WP_NS}}}docPr"))
    if len(drawing_properties) != 2 or any(
        not node.get("title", "").strip() or not node.get("descr", "").strip()
        for node in drawing_properties
    ):
        raise SummaryDocumentError(f"{path}: DOCX drawing alternatives are incomplete")

    parent_map = {child: parent for parent in root.iter() for child in parent}
    tables = list(root.iter(f"{{{W_NS}}}tbl"))
    if any(
        any(ancestor.tag == f"{{{W_NS}}}tbl" for ancestor in _parent_chain(table, parent_map))
        for table in tables
    ):
        raise SummaryDocumentError(f"{path}: DOCX still contains nested table floats")
    width_profiles = _table_width_profile(document)
    data_table_count = 0
    container_table_count = 0
    for table in tables:
        rows = table.findall(f"{{{W_NS}}}tr")
        column_count = max(
            (len(row.findall(f"{{{W_NS}}}tc")) for row in rows),
            default=0,
        )
        table_properties = table.find(f"{{{W_NS}}}tblPr")
        if table_properties is None:
            raise SummaryDocumentError(f"{path}: DOCX table lacks properties")
        table_width = table_properties.find(f"{{{W_NS}}}tblW")
        layout = table_properties.find(f"{{{W_NS}}}tblLayout")
        grid = table.find(f"{{{W_NS}}}tblGrid")
        grid_widths = [
            int(column.get(f"{{{W_NS}}}w", "0"))
            for column in (grid.findall(f"{{{W_NS}}}gridCol") if grid is not None else [])
        ]
        if (
            table_width is None
            or table_width.get(f"{{{W_NS}}}type") != "dxa"
            or table_width.get(f"{{{W_NS}}}w") != str(DOCX_CONTENT_WIDTH_TWIPS)
            or layout is None
            or layout.get(f"{{{W_NS}}}val") != "fixed"
            or len(grid_widths) != column_count
            or sum(grid_widths) != DOCX_CONTENT_WIDTH_TWIPS
        ):
            raise SummaryDocumentError(f"{path}: DOCX table width is not stable")
        margins = (
            table_properties.find(f"{{{W_NS}}}tblCellMar")
        )
        is_data_table = len(rows) >= 2 and column_count >= 2
        is_container = len(rows) == 1 and column_count == 1
        if not is_data_table and not is_container:
            raise SummaryDocumentError(f"{path}: unsupported DOCX table shape")
        expected_cell_margins = (
            {
                "top": DOCX_TABLE_CELL_VERTICAL_MARGIN,
                "left": DOCX_TABLE_CELL_HORIZONTAL_MARGIN,
                "bottom": DOCX_TABLE_CELL_VERTICAL_MARGIN,
                "right": DOCX_TABLE_CELL_HORIZONTAL_MARGIN,
            }
            if is_data_table
            else {"top": "0", "left": "0", "bottom": "0", "right": "0"}
        )
        if margins is None or any(
            (node := margins.find(f"{{{W_NS}}}{side}")) is None
            or node.get(f"{{{W_NS}}}w") != width
            or node.get(f"{{{W_NS}}}type") != "dxa"
            for side, width in expected_cell_margins.items()
        ):
            raise SummaryDocumentError(
                f"{path}: DOCX table cell margins are not owned"
            )
        if is_data_table:
            if data_table_count >= len(width_profiles):
                raise SummaryDocumentError(
                    f"{path}: DOCX has more data tables than its owned profile"
                )
            expected_grid = _profile_widths_twips(width_profiles[data_table_count])
            if grid_widths != expected_grid:
                raise SummaryDocumentError(
                    f"{path}: DOCX table {data_table_count + 1} does not use "
                    "its owned column-width profile"
                )
            data_table_count += 1
            style = table_properties.find(f"{{{W_NS}}}tblStyle")
            if style is None or style.get(f"{{{W_NS}}}val") != DOCX_TABLE_STYLE_ID:
                raise SummaryDocumentError(f"{path}: data table style is not owned")
            if table_properties.find(f"{{{W_NS}}}tblBorders") is None:
                raise SummaryDocumentError(f"{path}: data table borders are missing")
        else:
            container_table_count += 1
        for row_index, row in enumerate(rows):
            row_properties = row.find(f"{{{W_NS}}}trPr")
            if row_properties is None or row_properties.find(f"{{{W_NS}}}cantSplit") is None:
                raise SummaryDocumentError(f"{path}: DOCX table row may split across pages")
            if is_data_table and row_index == 0 and row_properties.find(f"{{{W_NS}}}tblHeader") is None:
                raise SummaryDocumentError(f"{path}: DOCX table header does not repeat")
            cells = row.findall(f"{{{W_NS}}}tc")
            for column, cell in enumerate(cells):
                cell_properties = cell.find(f"{{{W_NS}}}tcPr")
                cell_width = (
                    cell_properties.find(f"{{{W_NS}}}tcW")
                    if cell_properties is not None else None
                )
                if (
                    cell_width is None
                    or cell_width.get(f"{{{W_NS}}}type") != "dxa"
                    or cell_width.get(f"{{{W_NS}}}w") != str(grid_widths[column])
                ):
                    raise SummaryDocumentError(f"{path}: DOCX cell width is unstable")
                if not is_data_table:
                    continue
                allowed_empty = ALLOWED_EMPTY_DATA_CELLS.get(
                    document.number, {}
                ).get(data_table_count - 1, set())
                if (
                    row_index > 0
                    and not _docx_cell_text(cell)
                    and (row_index, column) not in allowed_empty
                ):
                    raise SummaryDocumentError(
                        f"{path}: DOCX data table {data_table_count} contains an "
                        f"empty body cell at row {row_index + 1}, column {column + 1}"
                    )
                expected_vertical = "center" if row_index == 0 else "top"
                vertical = cell_properties.find(f"{{{W_NS}}}vAlign")
                shading = cell_properties.find(f"{{{W_NS}}}shd")
                expected_fill = (
                    "EAF2F6" if row_index == 0
                    else ("F3F7F9" if row_index % 2 == 1 else "FFFFFF")
                )
                if (
                    vertical is None
                    or vertical.get(f"{{{W_NS}}}val") != expected_vertical
                    or shading is None
                    or shading.get(f"{{{W_NS}}}fill") != expected_fill
                ):
                    raise SummaryDocumentError(f"{path}: DOCX cell styling is incomplete")
                for paragraph in cell.iter(f"{{{W_NS}}}p"):
                    paragraph_properties = paragraph.find(f"{{{W_NS}}}pPr")
                    if row_index == 0:
                        alignment = (
                            paragraph_properties.find(f"{{{W_NS}}}jc")
                            if paragraph_properties is not None else None
                        )
                        if (
                            alignment is None
                            or alignment.get(f"{{{W_NS}}}val") != "left"
                        ):
                            raise SummaryDocumentError(
                                f"{path}: DOCX table header is not left-aligned"
                            )
                    indent = (
                        paragraph_properties.find(f"{{{W_NS}}}ind")
                        if paragraph_properties is not None
                        else None
                    )
                    if indent is not None and any(
                        int(indent.get(f"{{{W_NS}}}{side}", "0") or "0") > 0
                        for side in ("left", "right", "start", "end")
                    ):
                        raise SummaryDocumentError(
                            f"{path}: DOCX table paragraph contains extra indentation"
                        )
    if data_table_count != len(width_profiles) or container_table_count != 1:
        raise SummaryDocumentError(
            f"{path}: expected {len(width_profiles)} data tables plus one figure "
            "container; found "
            f"{data_table_count} data and {container_table_count} container tables"
        )
    table_captions = [
        paragraph
        for paragraph in root.iter(f"{{{W_NS}}}p")
        if (
            (properties := paragraph.find(f"{{{W_NS}}}pPr")) is not None
            and (style := properties.find(f"{{{W_NS}}}pStyle")) is not None
            and style.get(f"{{{W_NS}}}val") == "TableCaption"
        )
    ]
    table_caption_count = len(table_captions)
    if table_caption_count != TABLE_CAPTION_COUNTS[document.number]:
        raise SummaryDocumentError(
            f"{path}: expected {TABLE_CAPTION_COUNTS[document.number]} stable "
            f"table captions, found {table_caption_count}"
        )
    for caption in table_captions:
        parent = parent_map.get(caption)
        if parent is None:
            raise SummaryDocumentError(f"{path}: DOCX table caption has no parent")
        siblings = list(parent)
        position = siblings.index(caption)
        if position + 1 >= len(siblings) or siblings[position + 1].tag != f"{{{W_NS}}}tbl":
            raise SummaryDocumentError(
                f"{path}: DOCX table caption is not directly attached to its table"
            )
    image_caption_count = sum(
        1
        for paragraph in root.iter(f"{{{W_NS}}}p")
        if (
            (properties := paragraph.find(f"{{{W_NS}}}pPr")) is not None
            and (style := properties.find(f"{{{W_NS}}}pStyle")) is not None
            and style.get(f"{{{W_NS}}}val") == "ImageCaption"
        )
    )
    if image_caption_count != 1:
        raise SummaryDocumentError(
            f"{path}: expected one stable image caption, found {image_caption_count}"
        )

    expanded_headings = [
        paragraph
        for paragraph in root.iter(f"{{{W_NS}}}p")
        if "".join(
            node.text or "" for node in paragraph.iter(f"{{{W_NS}}}t")
        ).strip() == labels["expanded-reference"]
    ]
    if len(expanded_headings) != 1 or (
        (properties := expanded_headings[0].find(f"{{{W_NS}}}pPr")) is None
        or properties.find(f"{{{W_NS}}}pageBreakBefore") is None
    ):
        raise SummaryDocumentError(f"{path}: expanded reference lacks a page break")
    sections = list(root.iter(f"{{{W_NS}}}sectPr"))
    if not sections:
        raise SummaryDocumentError(f"{path}: DOCX has no section properties")
    for section in sections:
        pg_size = section.find(f"{{{W_NS}}}pgSz")
        pg_margin = section.find(f"{{{W_NS}}}pgMar")
        if pg_size is None or (
            pg_size.get(f"{{{W_NS}}}w"), pg_size.get(f"{{{W_NS}}}h")
        ) != (str(DOCX_PAGE_WIDTH_TWIPS), str(DOCX_PAGE_HEIGHT_TWIPS)):
            raise SummaryDocumentError(f"{path}: DOCX section is not explicit A4 portrait")
        expected_margins = {
            "top": "1077", "bottom": "1077",
            "left": str(DOCX_MARGIN_TWIPS), "right": str(DOCX_MARGIN_TWIPS)
        }
        if pg_margin is None or any(
            pg_margin.get(f"{{{W_NS}}}{name}") != value
            for name, value in expected_margins.items()
        ):
            raise SummaryDocumentError(f"{path}: DOCX section margins are not owned")
    body = root.find(f"{{{W_NS}}}body")
    if body is None:
        raise SummaryDocumentError(f"{path}: DOCX has no document body")
    body_children = list(body)

    def child_text(node: ET.Element) -> str:
        return "".join(
            child.text or "" for child in node.iter(f"{{{W_NS}}}t")
        ).strip()

    def child_page_breaks(node: ET.Element) -> int:
        return sum(
            1
            for child in node.iter(f"{{{W_NS}}}br")
            if child.get(f"{{{W_NS}}}type") == "page"
        )

    note_positions: list[int] = []
    for expected_label in sorted(
        expected_note_labels,
        key=lambda value: int(re.search(r"\d+", value).group()),
    ):
        matches = [
            index
            for index, child in enumerate(body_children)
            if child_text(child) == expected_label
        ]
        if len(matches) != 1:
            raise SummaryDocumentError(
                f"{path}: note label {expected_label!r} must occur exactly once"
            )
        position = matches[0]
        if (
            position == 0
            or child_text(body_children[position - 1])
            or child_page_breaks(body_children[position - 1]) != 1
        ):
            raise SummaryDocumentError(
                f"{path}: note page {expected_label!r} lacks its own preceding page break"
            )
        note_positions.append(position)
    if note_positions != sorted(note_positions):
        raise SummaryDocumentError(f"{path}: DOCX note pages are out of order")

    note_break_positions = {position - 1 for position in note_positions}
    body_break_positions = [
        index
        for index, child in enumerate(body_children)
        if child_page_breaks(child)
        and index not in note_break_positions
    ]
    course_positions = [
        index
        for index, child in enumerate(body_children)
        if child_text(child) == labels["course-summary"]
    ]
    if (
        len(body_break_positions) != 1
        or len(course_positions) != 1
        or body_break_positions[0] >= course_positions[0]
    ):
        raise SummaryDocumentError(
            f"{path}: DOCX must contain one title-to-summary page break"
        )
    return len(media_names), len(text)


def validate_output_set(
    paths: ProjectPaths, documents: Sequence[SummarySource]
) -> tuple[int, int, dict[str, int]]:
    expected: dict[Path, tuple[SummarySource, str]] = {}
    page_counts: dict[str, int] = {}
    for document in documents:
        output_dir = paths.output_dir(document.locale)
        expected[output_dir / document.pdf_name] = (document, "pdf")
        expected[output_dir / document.docx_name] = (document, "docx")
    pdf_count = docx_count = 0
    for path, (document, file_format) in sorted(expected.items(), key=lambda item: str(item[0])):
        if file_format == "pdf":
            pages, _ = validate_pdf(document, path)
            page_counts[document.document_id] = pages
            pdf_count += 1
        else:
            validate_docx(document, path)
            docx_count += 1
    return pdf_count, docx_count, page_counts


def parse_topic_arguments(values: Sequence[int] | None) -> list[int] | None:
    if not values:
        return None
    invalid = sorted({value for value in values if value not in range(1, 9)})
    if invalid:
        raise SummaryDocumentError(
            f"topic numbers must be 1 through 8: {', '.join(map(str, invalid))}"
        )
    return sorted(set(values))
