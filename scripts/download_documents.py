#!/usr/bin/env python3
"""Shared authoring, rendering, and validation logic for learner documents.

The public entry points are ``render-download-documents.py`` and
``validate-download-documents.py``. This module intentionally uses only the
Python standard library at render time. PDF text validation uses either the
locally installed ``pypdf`` module or the local ``pdftotext`` executable.
"""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import tempfile
import unicodedata
import zipfile
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from itertools import zip_longest
from pathlib import Path
from typing import Iterable, Sequence


LOCALES = ("en", "de", "sq")
DOCUMENT_TYPES = ("exercises", "solutions")
LANGUAGE_TAGS = {"en": "en-US", "de": "de-CH", "sq": "sq-AL"}
MINIMUM_PDF_BYTES = 1024

# Preserve the shared page geometry unless a reviewed document would otherwise
# strand only a few closing lines on a separate page. These small, documented
# exceptions keep the common type size and line spacing unchanged.
BOTTOM_MARGIN_OVERRIDES = {
    "topic-02-probability-solutions-sq": "16mm",
    "topic-06-partial-correlation-solutions-en": "18mm",
    "topic-06-partial-correlation-exercises-sq": "14mm",
}

SOURCE_NAME_RE = re.compile(
    r"^topic-(?P<number>\d{2})-"
    r"(?P<slug>[a-z0-9]+(?:-[a-z0-9]+)*)-"
    r"(?P<document_type>exercises|solutions)-"
    r"(?P<locale>en|de|sq)\.md$"
)
PDF_NAME_RE = re.compile(
    r"^topic-(?P<number>\d{2})-"
    r"(?P<slug>[a-z0-9]+(?:-[a-z0-9]+)*)-"
    r"(?P<document_type>exercises|solutions)-"
    r"(?P<locale>en|de|sq)\.pdf$"
)
DOCX_NAME_RE = re.compile(
    r"^topic-(?P<number>\d{2})-"
    r"(?P<slug>[a-z0-9]+(?:-[a-z0-9]+)*)-"
    r"(?P<document_type>exercises|solutions)-"
    r"(?P<locale>en|de|sq)\.docx$"
)
TASK_ID_RE = re.compile(
    r"^T(?P<topic>\d{2})-A(?P<archetype>\d{2})-V(?P<variant>\d{2})$"
)
TASK_LIKE_RE = re.compile(r"\bT\d{1,3}-A\d{1,3}-V\d{1,3}\b", re.IGNORECASE)
STRICT_TASK_HEADING_RE = re.compile(
    r"^#{2,4} (?P<task_id>T\d{2}-A\d{2}-V\d{2}): "
    r"(?P<title>\S(?:.*\S)?)$"
)
ATX_HEADING_RE = re.compile(r"^(?P<indent> {0,3})(?P<marks>#{1,6})(?:[ \t]+|$)")
FENCE_RE = re.compile(r"^(?P<indent> {0,3})(?P<fence>`{3,}|~{3,})(?P<rest>.*)$")
NUMERIC_TOKEN_RE = re.compile(
    # A hyphen attached to a word, as in "width-5", is punctuation rather
    # than a numeric sign. Starting a signed token after a letter would make
    # harmless localization differences look like changed data. If the
    # signed match is blocked, the engine still starts at the digit and
    # records the unsigned value 5. Genuine negatives after whitespace,
    # commas, parentheses, or operators retain their sign.
    r"(?<![\dA-Za-z])"
    r"[+\-−]?"
    r"(?:\d{1,3}(?:,\d{3})+(?:\.\d+)?|\d+(?:\.\d+)?|\.\d+)"
    r"(?:[eE][+\-]?\d+)?"
    r"(?:[ \t\u00a0]*%)?"
)

RESOURCE_RULES = (
    (re.compile(r"!\s*\[", re.IGNORECASE), "Markdown image"),
    (
        re.compile(
            r"<\s*(?:img|object|embed|iframe|script|link|audio|video|source)\b",
            re.IGNORECASE,
        ),
        "HTML resource element",
    ),
    (
        re.compile(
            r"<\s*/?\s*[A-Za-z][A-Za-z0-9-]*(?:\s+[^<>]*|/?)>",
            re.IGNORECASE,
        ),
        "raw HTML element",
    ),
    (re.compile(r"\{\{\s*[<%]", re.IGNORECASE), "Quarto shortcode"),
    (
        re.compile(
            r"^ {0,3}(?:`{3,}|~{3,}).*(?:\{=\s*typst\s*\}|\btypst\b)",
            re.MULTILINE | re.IGNORECASE,
        ),
        "raw Typst block",
    ),
    (re.compile(r"\{=\s*typst\s*\}", re.IGNORECASE), "raw Typst span"),
    (
        re.compile(
            r"#\s*(?:read|image|import|include|bibliography|csv|json|yaml|xml|plugin)\b",
            re.IGNORECASE,
        ),
        "Typst resource operation",
    ),
    (
        re.compile(r"@(?:preview|local)/|https?://[^\s\"']+\.typ", re.IGNORECASE),
        "Typst package or network resource",
    ),
    (re.compile(r"\bfile\s*:", re.IGNORECASE), "file URI"),
    (
        re.compile(
            r"(?<!!)\[[^\]\r\n]*\]\(\s*<?"
            r"(?:/|~/|\.\.?/|[A-Za-z]:[\\/])",
            re.IGNORECASE,
        ),
        "absolute or local-file Markdown link",
    ),
    (
        re.compile(
            r"^ {0,3}\[[^\]\r\n]+\]:\s*<?"
            r"(?:/|~/|\.\.?/|[A-Za-z]:[\\/]|file:)",
            re.MULTILINE | re.IGNORECASE,
        ),
        "absolute or local-file reference",
    ),
    (
        re.compile(r"\\(?:includegraphics|input|include)\s*\{", re.IGNORECASE),
        "raw TeX resource operation",
    ),
)
MARKDOWN_LINK_RE = re.compile(
    r"(?<!!)\[[^\]\r\n]*\]\(\s*<?(?P<target>[^\s)>]+)",
    re.IGNORECASE,
)
REFERENCE_LINK_RE = re.compile(
    r"^ {0,3}\[[^\]\r\n]+\]:\s*<?(?P<target>[^\s>]+)",
    re.MULTILINE | re.IGNORECASE,
)
LEGACY_MATH_DELIMITER_RE = re.compile(r"\\(?:\(|\)|\[|\])")

REQUIRED_METADATA = {
    "title",
    "document-id",
    "topic-id",
    "topic-number",
    "topic-slug",
    "document-type",
    "locale",
    "paired-document-id",
}
ALLOWED_METADATA = REQUIRED_METADATA | {"subtitle"}


class DocumentError(RuntimeError):
    """A source, render, or PDF validation error."""


@dataclass(frozen=True)
class ProjectPaths:
    root: Path
    source_root: Path
    brand_logo: Path
    is_self_test: bool = False

    @classmethod
    def from_script(cls, script_path: Path) -> "ProjectPaths":
        root = script_path.resolve().parents[1]
        return cls(
            root=root,
            source_root=root
            / "ratiomera-statistics"
            / "_shared"
            / "download-sources",
            brand_logo=root / "assets" / "brand" / "ratiomera-logo-primary.svg",
        )

    def output_dir(self, locale: str) -> Path:
        return (
            self.root
            / "ratiomera-statistics"
            / locale
            / "downloads"
            / "files"
        )


def _absolute(path: Path) -> Path:
    """Return an absolute normalized path without resolving symlinks."""
    return Path(os.path.abspath(os.fspath(path)))


def _is_within(path: Path, parent: Path) -> bool:
    try:
        _absolute(path).relative_to(_absolute(parent))
        return True
    except ValueError:
        return False


def _reject_symlink_components(path: Path, *, anchor: Path | None = None) -> None:
    absolute = _absolute(path)
    if anchor is None:
        current = Path(absolute.anchor)
        parts = absolute.parts[1:]
    else:
        anchor = _absolute(anchor)
        if not _is_within(absolute, anchor):
            raise DocumentError(f"path escapes its canonical root: {path}")
        current = anchor
        parts = absolute.relative_to(anchor).parts
        if current.is_symlink():
            raise DocumentError(f"symlink path component is not allowed: {current}")
    for part in parts:
        current = current / part
        if os.path.lexists(current) and current.is_symlink():
            raise DocumentError(f"symlink path component is not allowed: {current}")


def validate_project_tree(paths: ProjectPaths) -> None:
    root = _absolute(paths.root)
    expected_source = (
        root / "ratiomera-statistics" / "_shared" / "download-sources"
    )
    if _absolute(paths.source_root) != expected_source:
        raise DocumentError(
            f"source root must be the canonical learner source path: {expected_source}"
        )
    if not root.is_dir() or root.is_symlink():
        raise DocumentError(f"project root must be a regular directory: {root}")
    _reject_symlink_components(expected_source, anchor=root)
    if not expected_source.is_dir():
        raise DocumentError(f"missing learner source root: {expected_source}")


@dataclass(frozen=True)
class SourceDocument:
    path: Path
    metadata: dict[str, str]
    body: str
    number: str
    slug: str
    document_type: str
    locale: str
    task_ids: tuple[str, ...]
    task_numeric_tokens: tuple[tuple[str, tuple[str, ...]], ...]

    @property
    def document_id(self) -> str:
        return self.path.stem

    @property
    def topic_id(self) -> str:
        return f"topic-{self.number}-{self.slug}"

    @property
    def pair_type(self) -> str:
        return "solutions" if self.document_type == "exercises" else "exercises"

    @property
    def pair_id(self) -> str:
        return f"{self.topic_id}-{self.pair_type}-{self.locale}"

    @property
    def pdf_name(self) -> str:
        return f"{self.document_id}.pdf"

    @property
    def docx_name(self) -> str:
        return f"{self.document_id}.docx"

    @property
    def grouping_key(self) -> tuple[str, str, str]:
        return (self.number, self.slug, self.locale)

    @property
    def numeric_tokens_by_task(self) -> dict[str, tuple[str, ...]]:
        return dict(self.task_numeric_tokens)


def _parse_scalar(raw: str, path: Path, line_number: int) -> str:
    value = raw.strip()
    if not value:
        return ""
    if value.startswith('"'):
        try:
            parsed = json.loads(value)
        except json.JSONDecodeError as exc:
            raise DocumentError(
                f"{path}:{line_number}: invalid double-quoted metadata value: {exc.msg}"
            ) from exc
        if not isinstance(parsed, str):
            raise DocumentError(
                f"{path}:{line_number}: metadata values must be strings"
            )
        return parsed
    if value.startswith("'"):
        if len(value) < 2 or not value.endswith("'"):
            raise DocumentError(
                f"{path}:{line_number}: unterminated single-quoted metadata value"
            )
        return value[1:-1].replace("''", "'")
    if " #" in value:
        value = value.split(" #", 1)[0].rstrip()
    return value


def split_front_matter(path: Path) -> tuple[dict[str, str], str]:
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        raise DocumentError(f"{path}: source must be UTF-8") from exc
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].strip() != "---":
        raise DocumentError(f"{path}: source must begin with YAML front matter")

    closing = None
    for index in range(1, len(lines)):
        if lines[index].strip() in {"---", "..."}:
            closing = index
            break
    if closing is None:
        raise DocumentError(f"{path}: YAML front matter has no closing delimiter")

    metadata: dict[str, str] = {}
    key_re = re.compile(r"^(?P<key>[a-z][a-z0-9-]*):(?P<value>.*)$")
    for index, line in enumerate(lines[1:closing], start=2):
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        match = key_re.fullmatch(line.rstrip("\r\n"))
        if not match:
            raise DocumentError(
                f"{path}:{index}: front matter must use flat key: value entries"
            )
        key = match.group("key")
        if key in metadata:
            raise DocumentError(f"{path}:{index}: duplicate metadata key {key!r}")
        metadata[key] = _parse_scalar(match.group("value"), path, index)

    unknown = set(metadata) - ALLOWED_METADATA
    if unknown:
        raise DocumentError(
            f"{path}: unsupported metadata keys: {', '.join(sorted(unknown))}"
        )
    missing = REQUIRED_METADATA - set(metadata)
    if missing:
        raise DocumentError(
            f"{path}: missing metadata keys: {', '.join(sorted(missing))}"
        )
    empty = sorted(key for key in REQUIRED_METADATA if not metadata[key].strip())
    if empty:
        raise DocumentError(
            f"{path}: empty metadata values: {', '.join(empty)}"
        )
    if not metadata["title"].strip():
        raise DocumentError(f"{path}: title must not be empty")

    return metadata, "".join(lines[closing + 1 :])


def _mask_html_comments(text: str) -> str:
    """Blank HTML comments while preserving newlines and line positions."""
    output: list[str] = []
    position = 0
    in_comment = False
    while position < len(text):
        if in_comment:
            end = text.find("-->", position)
            if end == -1:
                hidden = text[position:]
                output.append("".join("\n" if char == "\n" else " " for char in hidden))
                break
            hidden = text[position : end + 3]
            output.append("".join("\n" if char == "\n" else " " for char in hidden))
            position = end + 3
            in_comment = False
            continue
        start = text.find("<!--", position)
        if start == -1:
            output.append(text[position:])
            break
        output.append(text[position:start])
        hidden = text[start : start + 4]
        output.append(" " * len(hidden))
        position = start + 4
        in_comment = True
    return "".join(output)


def validate_body_resources(body: str, path: Path) -> None:
    visible = _mask_html_comments(body)
    legacy_math = LEGACY_MATH_DELIMITER_RE.search(visible)
    if legacy_math:
        line = visible.count("\n", 0, legacy_math.start()) + 1
        raise DocumentError(
            f"{path}:{line}: legacy \\( ... \\) and \\[ ... \\] math "
            "delimiters are not supported; use Pandoc $...$ for inline math "
            "and $$...$$ for display math"
        )
    for pattern, label in RESOURCE_RULES:
        match = pattern.search(visible)
        if match:
            line = visible.count("\n", 0, match.start()) + 1
            raise DocumentError(f"{path}:{line}: {label} is not allowed")
    for pattern in (MARKDOWN_LINK_RE, REFERENCE_LINK_RE):
        for match in pattern.finditer(visible):
            target = match.group("target").strip().rstrip(">")
            if target.startswith("#") or re.match(
                r"^(?:https?://|mailto:)", target, re.IGNORECASE
            ):
                continue
            line = visible.count("\n", 0, match.start()) + 1
            raise DocumentError(
                f"{path}:{line}: local or unsupported link target is not allowed"
            )


def _numeric_tokens(text: str) -> tuple[str, ...]:
    without_comments = _mask_html_comments(text)
    without_ids = re.sub(
        r"\bT\d{2}-A\d{2}-V\d{2}\b", "", without_comments
    )
    tokens: list[str] = []
    for match in NUMERIC_TOKEN_RE.finditer(without_ids):
        token = unicodedata.normalize("NFKC", match.group(0))
        token = token.replace("−", "-").replace(" ", "").replace("\u00a0", "")
        tokens.append(token)
    return tuple(tokens)


def parse_task_structure(
    body: str, path: Path
) -> tuple[tuple[str, ...], tuple[tuple[str, tuple[str, ...]], ...]]:
    masked = _mask_html_comments(body)
    raw_lines = body.splitlines(keepends=True)
    masked_lines = masked.splitlines(keepends=True)
    if len(raw_lines) != len(masked_lines):
        raise DocumentError(f"{path}: internal line-preservation failure")

    fence_character: str | None = None
    fence_length = 0
    task_starts: list[tuple[str, int]] = []
    ignored_lines: set[int] = set()
    for index, line_with_ending in enumerate(masked_lines):
        line = line_with_ending.rstrip("\r\n")
        fence_match = FENCE_RE.match(line)
        if fence_character is not None:
            ignored_lines.add(index)
            if fence_match:
                candidate = fence_match.group("fence")
                if (
                    candidate[0] == fence_character
                    and len(candidate) >= fence_length
                    and not fence_match.group("rest").strip()
                ):
                    fence_character = None
                    fence_length = 0
            continue
        if fence_match:
            candidate = fence_match.group("fence")
            if candidate[0] == "`" and "`" in fence_match.group("rest"):
                continue
            ignored_lines.add(index)
            fence_character = candidate[0]
            fence_length = len(candidate)
            continue
        if line.startswith("    ") or line.startswith("\t"):
            ignored_lines.add(index)
            continue

        exact = STRICT_TASK_HEADING_RE.fullmatch(line)
        if exact:
            task_starts.append((exact.group("task_id"), index))
            continue

        task_like = TASK_LIKE_RE.search(line)
        if task_like and (
            ATX_HEADING_RE.match(line)
            or re.search(r"#{1,6}[ \t]+", line)
            or re.search(r"<\s*h[1-6]\b", line, re.IGNORECASE)
            or line.lstrip().startswith(task_like.group(0))
        ):
            raise DocumentError(
                f"{path}:{index + 1}: malformed task heading; expected "
                "an unindented level-two through level-four heading in the form "
                "'TNN-ANN-VNN: nonempty localized title'"
            )

    if fence_character is not None:
        raise DocumentError(
            f"{path}: unclosed fenced code block; closing fence must use the "
            "same character and be at least as long as its opening fence"
        )

    for index in range(len(masked_lines) - 1):
        if index in ignored_lines or index + 1 in ignored_lines:
            continue
        line = masked_lines[index].rstrip("\r\n")
        following = masked_lines[index + 1].rstrip("\r\n")
        if TASK_LIKE_RE.search(line) and re.fullmatch(r" {0,3}(?:=+|-+)\s*", following):
            raise DocumentError(
                f"{path}:{index + 1}: setext task headings are not allowed"
            )

    task_ids = tuple(task_id for task_id, _line in task_starts)
    numeric: list[tuple[str, tuple[str, ...]]] = []
    for position, (task_id, start) in enumerate(task_starts):
        stop = (
            task_starts[position + 1][1]
            if position + 1 < len(task_starts)
            else len(raw_lines)
        )
        numeric.append((task_id, _numeric_tokens("".join(raw_lines[start:stop]))))
    return task_ids, tuple(numeric)


def parse_source(path: Path) -> SourceDocument:
    path = _absolute(path)
    if path.parent.is_symlink() or not path.is_file() or path.is_symlink():
        raise DocumentError(f"{path}: source must be a regular, non-symlink file")
    match = SOURCE_NAME_RE.fullmatch(path.name)
    if not match:
        raise DocumentError(f"{path}: filename does not follow the learner-PDF contract")

    metadata, body = split_front_matter(path)
    validate_body_resources(body, path)
    task_ids, task_numeric_tokens = parse_task_structure(body, path)
    document = SourceDocument(
        path=path.resolve(),
        metadata=metadata,
        body=body,
        number=match.group("number"),
        slug=match.group("slug"),
        document_type=match.group("document_type"),
        locale=match.group("locale"),
        task_ids=task_ids,
        task_numeric_tokens=task_numeric_tokens,
    )
    expected = {
        "document-id": document.document_id,
        "topic-id": document.topic_id,
        "topic-number": document.number,
        "topic-slug": document.slug,
        "document-type": document.document_type,
        "locale": document.locale,
        "paired-document-id": document.pair_id,
    }
    errors = [
        f"{key} must be {value!r}, found {metadata[key]!r}"
        for key, value in expected.items()
        if metadata[key] != value
    ]
    if errors:
        raise DocumentError(f"{path}: " + "; ".join(errors))
    if path.parent.name != document.locale:
        raise DocumentError(
            f"{path}: locale folder must be {document.locale!r}"
        )
    if not document.task_ids:
        raise DocumentError(
            f"{path}: no visible TNN-ANN-VNN task headings were found"
        )
    if len(set(document.task_ids)) != len(document.task_ids):
        raise DocumentError(f"{path}: task IDs must be unique")
    parsed_ids = [TASK_ID_RE.fullmatch(task_id) for task_id in document.task_ids]
    if any(match is None for match in parsed_ids):
        raise DocumentError(f"{path}: malformed task ID")
    expected_topic = document.number
    if any(match.group("topic") != expected_topic for match in parsed_ids if match):
        raise DocumentError(
            f"{path}: every task ID must start with 'T{expected_topic}-'"
        )
    coordinates = [
        (int(match.group("archetype")), int(match.group("variant")))
        for match in parsed_ids
        if match
    ]
    archetypes = sorted({archetype for archetype, _variant in coordinates})
    if archetypes != list(range(1, max(archetypes) + 1)):
        raise DocumentError(
            f"{path}: archetype IDs must be contiguous from A01"
        )
    encountered_archetypes: list[int] = []
    previous_archetype: int | None = None
    for archetype, _variant in coordinates:
        if archetype != previous_archetype:
            if archetype in encountered_archetypes:
                raise DocumentError(
                    f"{path}: every archetype must remain in one contiguous block"
                )
            encountered_archetypes.append(archetype)
            previous_archetype = archetype
    for archetype in archetypes:
        variants = [
            variant
            for item_archetype, variant in coordinates
            if item_archetype == archetype
        ]
        if variants != list(range(1, 11)):
            raise DocumentError(
                f"{path}: A{archetype:02d} must contain exactly V01 through V10"
            )
    if any(
        reserved in {"expanded", "exercises", "solutions"}
        for reserved in document.slug.split("-")
    ):
        raise DocumentError(
            f"{path}: topic slug contains a reserved learner-document word"
        )
    return document


def discover_sources(source_root: Path) -> list[SourceDocument]:
    source_root = _absolute(source_root)
    if not source_root.is_dir() or source_root.is_symlink():
        raise DocumentError(f"invalid learner source root: {source_root}")
    documents: list[SourceDocument] = []
    for locale in LOCALES:
        locale_dir = source_root / locale
        _reject_symlink_components(locale_dir, anchor=source_root)
        if not locale_dir.is_dir() or locale_dir.is_symlink():
            raise DocumentError(f"missing locale source directory: {locale_dir}")
        for path in sorted(locale_dir.iterdir(), key=lambda item: item.name):
            if path.is_symlink():
                raise DocumentError(f"symlinks are not allowed in {locale_dir}: {path}")
            if path.is_dir():
                raise DocumentError(
                    f"nested learner source directories are not allowed: {path}"
                )
            if path.name in {".gitkeep", ".DS_Store"} or path.name.startswith("_"):
                continue
            if path.name.lower() == "readme.md":
                continue
            if path.suffix.lower() == ".md":
                if not SOURCE_NAME_RE.fullmatch(path.name):
                    raise DocumentError(
                        f"{path}: learner source has an unstable or unsupported filename"
                    )
                documents.append(parse_source(path))
            elif not path.name.startswith("."):
                raise DocumentError(
                    f"unsupported file in text-only learner source directory: {path}"
                )
    return sorted(documents, key=lambda item: item.document_id)


def validate_source_set(
    documents: Sequence[SourceDocument], *, require_complete_locales: bool
) -> None:
    by_group: dict[tuple[str, str, str], dict[str, SourceDocument]] = {}
    seen_ids: set[str] = set()
    number_to_slug: dict[str, str] = {}
    slug_to_number: dict[str, str] = {}
    task_to_topic: dict[str, tuple[str, str]] = {}
    for document in documents:
        if document.document_id in seen_ids:
            raise DocumentError(f"duplicate document ID: {document.document_id}")
        seen_ids.add(document.document_id)
        kinds = by_group.setdefault(document.grouping_key, {})
        if document.document_type in kinds:
            raise DocumentError(
                f"duplicate {document.document_type} source for {document.grouping_key}"
            )
        kinds[document.document_type] = document
        existing_slug = number_to_slug.setdefault(document.number, document.slug)
        if existing_slug != document.slug:
            raise DocumentError(
                f"topic number {document.number} maps to both {existing_slug!r} "
                f"and {document.slug!r}"
            )
        existing_number = slug_to_number.setdefault(document.slug, document.number)
        if existing_number != document.number:
            raise DocumentError(
                f"topic slug {document.slug!r} maps to both {existing_number} "
                f"and {document.number}"
            )
        topic = (document.number, document.slug)
        for task_id in document.task_ids:
            existing_topic = task_to_topic.setdefault(task_id, topic)
            if existing_topic != topic:
                raise DocumentError(
                    f"task ID {task_id} maps to both {existing_topic} and {topic}"
                )

    for group, kinds in sorted(by_group.items()):
        missing = set(DOCUMENT_TYPES) - set(kinds)
        if missing:
            raise DocumentError(
                f"{group}: missing paired source type(s): {', '.join(sorted(missing))}"
            )
        exercises = kinds["exercises"]
        solutions = kinds["solutions"]
        if exercises.task_ids != solutions.task_ids:
            raise DocumentError(
                f"{group}: exercise and solution task IDs differ or are ordered differently"
            )

    topics: dict[tuple[str, str], dict[str, tuple[str, ...]]] = {}
    for (number, slug, locale), kinds in by_group.items():
        topics.setdefault((number, slug), {})[locale] = kinds["exercises"].task_ids
    for topic, locale_ids in sorted(topics.items()):
        if require_complete_locales:
            missing = set(LOCALES) - set(locale_ids)
            if missing:
                raise DocumentError(
                    f"{topic}: missing locale source pair(s): {', '.join(sorted(missing))}"
                )
        if "en" in locale_ids:
            canonical = locale_ids["en"]
            for locale in ("de", "sq"):
                if locale in locale_ids and locale_ids[locale] != canonical:
                    raise DocumentError(
                        f"{topic}: {locale} task IDs do not match canonical English"
                    )

    by_topic_type: dict[
        tuple[str, str, str], dict[str, SourceDocument]
    ] = {}
    for document in documents:
        key = (document.number, document.slug, document.document_type)
        by_topic_type.setdefault(key, {})[document.locale] = document
    for topic_type, locale_documents in sorted(by_topic_type.items()):
        canonical = locale_documents.get("en")
        if canonical is None:
            continue
        canonical_tokens = canonical.numeric_tokens_by_task
        for locale in ("de", "sq"):
            localized = locale_documents.get(locale)
            if localized is None:
                continue
            localized_tokens = localized.numeric_tokens_by_task
            for task_id in canonical.task_ids:
                expected = canonical_tokens[task_id]
                actual = localized_tokens[task_id]
                if actual != expected:
                    mismatch = next(
                        (
                            index,
                            left,
                            right,
                        )
                        for index, (left, right) in enumerate(
                            zip_longest(expected, actual, fillvalue="<missing>"),
                            start=1,
                        )
                        if left != right
                    )
                    index, left, right = mismatch
                    raise DocumentError(
                        f"{topic_type}: {locale} numeric-token mismatch in "
                        f"{task_id} at token {index}: expected {left!r}, "
                        f"found {right!r}"
                    )


def _front_matter_for_render(document: SourceDocument) -> str:
    quote = lambda value: json.dumps(value, ensure_ascii=False)
    subtitle = document.metadata.get("subtitle", "").strip()
    # Albanian learner prose is consistently a little longer than its English
    # and German counterparts, so its shared footer margin is 18 mm. A small
    # reviewed override may prevent a final two-line fragment without changing
    # the common type size, line spacing, or horizontal page geometry.
    default_bottom_margin = "18mm" if document.locale == "sq" else "22mm"
    bottom_margin = BOTTOM_MARGIN_OVERRIDES.get(
        document.document_id, default_bottom_margin
    )
    lines = [
        "---",
        f"title: {quote(document.metadata['title'])}",
    ]
    if subtitle:
        lines.append(f"subtitle: {quote(subtitle)}")
    lines.extend(
        [
            'author: "Ratiomera Statistics"',
            f"lang: {quote(LANGUAGE_TAGS[document.locale])}",
            'brand: "_ratiomera-brand.yml"',
            "format:",
            "  typst:",
            '    papersize: "a4"',
            "    margin:",
            "      top: 32mm",
            f"      bottom: {bottom_margin}",
            "      left: 22mm",
            "      right: 22mm",
            '    page-numbering: "1"',
            "    toc: false",
            "    logo:",
            '      path: "_ratiomera-logo-primary.svg"',
            '      alt: "Ratiomera"',
            "      location: top + left",
            "      inset: 9mm",
            "      width: 42mm",
            "execute:",
            "  enabled: false",
            "---",
            "",
        ]
    )
    return "\n".join(lines)


def _front_matter_for_word(document: SourceDocument) -> str:
    """Create a restrained, editable Word wrapper for the canonical source."""
    quote = lambda value: json.dumps(value, ensure_ascii=False)
    subtitle = document.metadata.get("subtitle", "").strip()
    lines = [
        "---",
        f"title: {quote(document.metadata['title'])}",
    ]
    if subtitle:
        lines.append(f"subtitle: {quote(subtitle)}")
    lines.extend(
        [
            'author: "Ratiomera Statistics"',
            f"lang: {quote(LANGUAGE_TAGS[document.locale])}",
            "format:",
            "  docx:",
            "    toc: false",
            "execute:",
            "  enabled: false",
            "---",
            "",
        ]
    )
    return "\n".join(lines)


BRAND_YAML = """\
meta:
  name: "Ratiomera Statistics"
color:
  palette:
    ratiomera-navy: "#183B56"
    statistics-blue: "#2F6F9F"
  foreground: "#183B56"
  background: "#FFFFFF"
  primary: ratiomera-navy
  secondary: statistics-blue
  link: statistics-blue
typography:
  base:
    family: "Libertinus Serif"
    size: "10.5pt"
    line-height: 1.35
  headings:
    family: "Libertinus Serif"
    weight: 700
    color: ratiomera-navy
  link:
    color: statistics-blue
    decoration: underline
"""


def _minimal_project_yaml(wrapper_name: str) -> str:
    return "\n".join(
        [
            "project:",
            "  type: default",
            "  render:",
            f"    - {json.dumps(wrapper_name)}",
            "",
        ]
    )


def _body_for_render(document: SourceDocument) -> str:
    """Keep every visible task ID together without changing its source heading.

    Typst can give ordinary hyphens in a heading incomplete text mappings for
    some language and line-breaking combinations. The PDF then looks correct,
    but assistive technology and text extraction see a spaced or separatorless
    ID. Rendering only the stable ID token as inline code keeps its ASCII
    hyphens visible, searchable, and unbroken. Source Markdown remains the
    canonical plain-heading format validated above.
    """
    raw_lines = document.body.splitlines(keepends=True)
    masked_lines = _mask_html_comments(document.body).splitlines(keepends=True)
    if len(raw_lines) != len(masked_lines):
        raise DocumentError(
            f"{document.path}: internal render line-preservation failure"
        )

    rendered_ids: list[str] = []
    fence_character: str | None = None
    fence_length = 0
    output = list(raw_lines)
    for index, masked_with_ending in enumerate(masked_lines):
        masked_line = masked_with_ending.rstrip("\r\n")
        fence_match = FENCE_RE.match(masked_line)
        if fence_character is not None:
            if fence_match:
                candidate = fence_match.group("fence")
                if (
                    candidate[0] == fence_character
                    and len(candidate) >= fence_length
                    and not fence_match.group("rest").strip()
                ):
                    fence_character = None
                    fence_length = 0
            continue
        if fence_match:
            candidate = fence_match.group("fence")
            if candidate[0] == "`" and "`" in fence_match.group("rest"):
                continue
            fence_character = candidate[0]
            fence_length = len(candidate)
            continue

        exact = STRICT_TASK_HEADING_RE.fullmatch(masked_line)
        if exact is None:
            continue
        task_id = exact.group("task_id")
        raw_with_ending = raw_lines[index]
        raw_line = raw_with_ending.rstrip("\r\n")
        ending = raw_with_ending[len(raw_line) :]
        marker = f" {task_id}: "
        if marker not in raw_line:
            raise DocumentError(
                f"{document.path}: task heading changed during render preparation"
            )
        marks, title = raw_line.split(marker, maxsplit=1)
        output[index] = f"{marks} `{task_id}`: {title}{ending}"
        rendered_ids.append(task_id)

    if tuple(rendered_ids) != document.task_ids:
        raise DocumentError(
            f"{document.path}: render preparation did not preserve every task ID"
        )
    return "".join(output)


def _safe_temp_base(project_root: Path) -> Path:
    candidates: list[Path] = []
    configured = os.environ.get("TMPDIR") or os.environ.get("TEMP")
    if configured:
        candidates.append(Path(configured))
    candidates.extend([Path(tempfile.gettempdir()), Path("/tmp"), Path("/var/tmp")])
    checked: set[Path] = set()
    for candidate in candidates:
        try:
            resolved = candidate.expanduser().resolve(strict=True)
        except (FileNotFoundError, OSError):
            continue
        if resolved in checked or not resolved.is_dir():
            continue
        checked.add(resolved)
        if _is_within(resolved, project_root):
            continue
        if os.access(resolved, os.W_OK | os.X_OK):
            return resolved
    raise DocumentError("no safe system temporary directory exists outside the project")


def _sanitized_render_environment(temp_base: Path) -> dict[str, str]:
    environment: dict[str, str] = {}
    for key in (
        "PATH",
        "HOME",
        "USER",
        "LOGNAME",
        "LANG",
        "LC_ALL",
        "TZ",
        "SYSTEMROOT",
        "WINDIR",
    ):
        value = os.environ.get(key)
        if value:
            environment[key] = value
    blocked_proxy = "http://127.0.0.1:9"
    environment.update(
        {
            "TMPDIR": str(temp_base),
            "TMP": str(temp_base),
            "TEMP": str(temp_base),
            "QUARTO_DISABLE_VERSION_CHECK": "1",
            "SOURCE_DATE_EPOCH": "0",
            "HTTP_PROXY": blocked_proxy,
            "HTTPS_PROXY": blocked_proxy,
            "ALL_PROXY": blocked_proxy,
            "http_proxy": blocked_proxy,
            "https_proxy": blocked_proxy,
            "all_proxy": blocked_proxy,
            "NO_PROXY": "",
            "no_proxy": "",
        }
    )
    return environment


def canonical_output_path(paths: ProjectPaths, document: SourceDocument) -> Path:
    root = _absolute(paths.root)
    directory = _absolute(paths.output_dir(document.locale))
    expected = (
        root
        / "ratiomera-statistics"
        / document.locale
        / "downloads"
        / "files"
    )
    if directory != expected:
        raise DocumentError(f"noncanonical learner-PDF output directory: {directory}")
    _reject_symlink_components(directory, anchor=root)
    if not directory.is_dir() or directory.is_symlink():
        raise DocumentError(
            f"learner-PDF output must be an existing regular directory: {directory}"
        )
    destination = directory / document.pdf_name
    if os.path.lexists(destination):
        if destination.is_symlink() or not destination.is_file():
            raise DocumentError(
                f"learner-PDF destination must be a regular non-symlink file: {destination}"
            )
    return destination


def canonical_docx_output_path(paths: ProjectPaths, document: SourceDocument) -> Path:
    root = _absolute(paths.root)
    directory = _absolute(paths.output_dir(document.locale))
    expected = (
        root
        / "ratiomera-statistics"
        / document.locale
        / "downloads"
        / "files"
    )
    if directory != expected:
        raise DocumentError(f"noncanonical learner-Word output directory: {directory}")
    _reject_symlink_components(directory, anchor=root)
    if not directory.is_dir() or directory.is_symlink():
        raise DocumentError(
            f"learner-Word output must be an existing regular directory: {directory}"
        )
    destination = directory / document.docx_name
    if os.path.lexists(destination):
        if destination.is_symlink() or not destination.is_file():
            raise DocumentError(
                f"learner-Word destination must be a regular non-symlink file: {destination}"
            )
    return destination


def _write_if_changed(path: Path, content: bytes) -> bool:
    if os.path.lexists(path):
        if path.is_symlink() or not path.is_file():
            raise DocumentError(f"unsafe learner-PDF destination: {path}")
        if path.read_bytes() == content:
            return False
    if not path.parent.is_dir() or path.parent.is_symlink():
        raise DocumentError(f"unsafe learner-PDF output directory: {path.parent}")
    handle = tempfile.NamedTemporaryFile(
        mode="wb",
        prefix=f".{path.name}.tmp-",
        dir=path.parent,
        delete=False,
    )
    temporary = Path(handle.name)
    try:
        with handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    finally:
        if temporary.exists():
            temporary.unlink()
    return True


def render_document(
    paths: ProjectPaths,
    document: SourceDocument,
) -> tuple[Path, bool]:
    if shutil.which("quarto") is None:
        raise DocumentError("quarto is required to render learner PDFs")
    if not paths.brand_logo.is_file():
        raise DocumentError(f"missing Ratiomera logo: {paths.brand_logo}")
    validate_project_tree(paths)
    if paths.is_self_test:
        if paths.brand_logo.is_symlink() or paths.brand_logo.parent.is_symlink():
            raise DocumentError(f"unsafe self-test logo path: {paths.brand_logo}")
    else:
        _reject_symlink_components(paths.brand_logo, anchor=paths.root)
    expected_source_parent = _absolute(paths.source_root / document.locale)
    if _absolute(document.path.parent) != expected_source_parent:
        raise DocumentError(
            f"document is outside its canonical locale source directory: {document.path}"
        )
    _reject_symlink_components(document.path, anchor=paths.root)
    final_path = canonical_output_path(paths, document)
    temp_base = _safe_temp_base(paths.root)

    with tempfile.TemporaryDirectory(
        prefix="ratiomera-download-render-", dir=temp_base
    ) as temp_name:
        workspace = Path(temp_name)
        wrapper = workspace / f"_{document.document_id}-render.md"
        wrapper.write_text(
            _front_matter_for_render(document) + _body_for_render(document),
            encoding="utf-8",
            newline="\n",
        )
        shutil.copyfile(paths.brand_logo, workspace / "_ratiomera-logo-primary.svg")
        (workspace / "_ratiomera-brand.yml").write_text(
            BRAND_YAML, encoding="utf-8", newline="\n"
        )
        project_file = workspace / "_quarto.yml"
        project_file.write_text(
            _minimal_project_yaml(wrapper.name), encoding="utf-8", newline="\n"
        )
        expected_inputs = {
            wrapper.name,
            "_ratiomera-logo-primary.svg",
            "_ratiomera-brand.yml",
            "_quarto.yml",
        }
        actual_inputs = {entry.name for entry in workspace.iterdir()}
        if actual_inputs != expected_inputs or any(
            entry.is_symlink() for entry in workspace.iterdir()
        ):
            raise DocumentError(
                "isolated render workspace contains an unexpected input"
            )
        rendered = workspace / f"{document.document_id}.pdf"
        command = [
            "quarto",
            "render",
            wrapper.name,
            "--to",
            "typst",
            "--output",
            rendered.name,
            "--no-execute",
            "--quiet",
        ]
        result = subprocess.run(
            command,
            cwd=workspace,
            text=True,
            capture_output=True,
            check=False,
            env=_sanitized_render_environment(temp_base),
        )
        if result.returncode != 0:
            details = (result.stderr or result.stdout).strip()
            raise DocumentError(
                f"Quarto Typst render failed for {document.path}:\n{details}"
            )
        normalize_pdf_metadata(rendered, document)
        validate_pdf(document, rendered)
        final_path = canonical_output_path(paths, document)
        changed = _write_if_changed(final_path, rendered.read_bytes())
    return final_path, changed


def render_word_document(
    paths: ProjectPaths,
    document: SourceDocument,
) -> tuple[Path, bool]:
    if shutil.which("quarto") is None:
        raise DocumentError("quarto is required to render learner Word documents")
    validate_project_tree(paths)
    expected_source_parent = _absolute(paths.source_root / document.locale)
    if _absolute(document.path.parent) != expected_source_parent:
        raise DocumentError(
            f"document is outside its canonical locale source directory: {document.path}"
        )
    _reject_symlink_components(document.path, anchor=paths.root)
    final_path = canonical_docx_output_path(paths, document)
    temp_base = _safe_temp_base(paths.root)

    with tempfile.TemporaryDirectory(
        prefix="ratiomera-download-word-render-", dir=temp_base
    ) as temp_name:
        workspace = Path(temp_name)
        wrapper = workspace / f"_{document.document_id}-word-render.md"
        wrapper.write_text(
            _front_matter_for_word(document) + _body_for_render(document),
            encoding="utf-8",
            newline="\n",
        )
        project_file = workspace / "_quarto.yml"
        project_file.write_text(
            _minimal_project_yaml(wrapper.name), encoding="utf-8", newline="\n"
        )
        expected_inputs = {wrapper.name, "_quarto.yml"}
        actual_inputs = {entry.name for entry in workspace.iterdir()}
        if actual_inputs != expected_inputs or any(
            entry.is_symlink() for entry in workspace.iterdir()
        ):
            raise DocumentError(
                "isolated Word render workspace contains an unexpected input"
            )
        rendered = workspace / document.docx_name
        command = [
            "quarto",
            "render",
            wrapper.name,
            "--to",
            "docx",
            "--output",
            rendered.name,
            "--no-execute",
            "--quiet",
        ]
        result = subprocess.run(
            command,
            cwd=workspace,
            text=True,
            capture_output=True,
            check=False,
            env=_sanitized_render_environment(temp_base),
        )
        if result.returncode != 0:
            details = (result.stderr or result.stdout).strip()
            raise DocumentError(
                f"Quarto Word render failed for {document.path}:\n{details}"
            )
        validate_docx(document, rendered)
        final_path = canonical_docx_output_path(paths, document)
        changed = _write_if_changed(final_path, rendered.read_bytes())
    return final_path, changed


def _extract_with_pypdf(path: Path) -> tuple[str, int] | None:
    try:
        from pypdf import PdfReader  # type: ignore[import-not-found]
    except ImportError:
        return None
    try:
        reader = PdfReader(str(path), strict=False)
        if reader.is_encrypted:
            raise DocumentError(f"{path}: learner PDF must not be encrypted")
        text = "\n".join((page.extract_text() or "") for page in reader.pages)
        return text, len(reader.pages)
    except DocumentError:
        raise
    except Exception as exc:
        raise DocumentError(f"{path}: pypdf could not read the PDF: {exc}") from exc


def _expected_pdf_metadata(document: SourceDocument) -> dict[str, str]:
    subject = (
        "Ratiomera Statistics exercise sheet"
        if document.document_type == "exercises"
        else "Ratiomera Statistics complete solutions"
    )
    return {
        "/Title": document.metadata["title"],
        "/Author": "Ratiomera Statistics",
        "/Subject": subject,
        "/Creator": "Ratiomera document pipeline",
        "/Producer": "Ratiomera document pipeline",
        "/Keywords": document.document_id,
        "/CreationDate": "D:19700101000000Z",
        "/ModDate": "D:19700101000000Z",
    }


def normalize_pdf_metadata(path: Path, document: SourceDocument) -> None:
    """Write deterministic, branded PDF metadata without altering page content."""
    try:
        from pypdf import PdfReader, PdfWriter  # type: ignore[import-not-found]
    except ImportError as exc:
        raise DocumentError(
            "PDF metadata normalization requires the installed pypdf package"
        ) from exc
    replacement = path.with_name(f".{path.name}.metadata")
    try:
        reader = PdfReader(str(path), strict=False)
        if reader.is_encrypted:
            raise DocumentError(f"{path}: learner PDF must not be encrypted")
        writer = PdfWriter(clone_from=reader)
        writer.add_metadata(_expected_pdf_metadata(document))
        with replacement.open("wb") as handle:
            writer.write(handle)
        os.replace(replacement, path)
    except DocumentError:
        replacement.unlink(missing_ok=True)
        raise
    except Exception as exc:
        replacement.unlink(missing_ok=True)
        raise DocumentError(f"{path}: could not normalize PDF metadata: {exc}") from exc


def validate_pdf_metadata(document: SourceDocument, path: Path) -> None:
    try:
        from pypdf import PdfReader  # type: ignore[import-not-found]
    except ImportError as exc:
        raise DocumentError(
            "PDF metadata validation requires the installed pypdf package"
        ) from exc
    try:
        metadata = PdfReader(str(path), strict=False).metadata or {}
    except Exception as exc:
        raise DocumentError(f"{path}: could not read PDF metadata: {exc}") from exc
    expected = _expected_pdf_metadata(document)
    mismatches = [
        f"{key}={metadata.get(key)!r}, expected {value!r}"
        for key, value in expected.items()
        if metadata.get(key) != value
    ]
    if mismatches:
        raise DocumentError(f"{path}: PDF metadata mismatch: {'; '.join(mismatches)}")


def _extract_with_pdftotext(path: Path) -> tuple[str, int] | None:
    executable = shutil.which("pdftotext")
    if executable is None:
        return None
    result = subprocess.run(
        [executable, "-layout", str(path), "-"],
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        raise DocumentError(
            f"{path}: pdftotext failed: {(result.stderr or result.stdout).strip()}"
        )
    page_count = max(1, result.stdout.count("\f") + 1)
    return result.stdout, page_count


def extract_pdf_text(path: Path) -> tuple[str, int]:
    for extractor in (_extract_with_pypdf, _extract_with_pdftotext):
        result = extractor(path)
        if result is not None:
            return result
    raise DocumentError(
        "PDF text validation requires a local pypdf installation or the "
        "pdftotext executable; the validator never installs dependencies"
    )


def _normalized_text(value: str) -> str:
    normalized = unicodedata.normalize("NFKC", value)
    return " ".join(normalized.split())


def validate_pdf(document: SourceDocument, path: Path) -> tuple[str, int]:
    if path.is_symlink() or not path.is_file():
        raise DocumentError(f"{path}: expected a regular PDF file")
    if path.name != document.pdf_name:
        raise DocumentError(
            f"{path}: PDF filename must be exactly {document.pdf_name!r}"
        )
    payload = path.read_bytes()
    if len(payload) < MINIMUM_PDF_BYTES:
        raise DocumentError(
            f"{path}: PDF is only {len(payload)} bytes; expected at least {MINIMUM_PDF_BYTES}"
        )
    if not payload.startswith(b"%PDF-"):
        raise DocumentError(f"{path}: missing PDF magic bytes")
    if b"%%EOF" not in payload[-4096:]:
        raise DocumentError(f"{path}: missing final PDF EOF marker")

    validate_pdf_metadata(document, path)

    text, page_count = extract_pdf_text(path)
    normalized = _normalized_text(text)
    if page_count < 1:
        raise DocumentError(f"{path}: PDF contains no pages")
    if len(normalized) < 40:
        raise DocumentError(f"{path}: PDF contains too little extractable text")
    missing_ids = [
        task_id for task_id in document.task_ids if task_id not in normalized
    ]
    if missing_ids:
        raise DocumentError(
            f"{path}: PDF text is missing task IDs: {', '.join(missing_ids)}"
        )
    return text, page_count


def extract_docx_text(path: Path) -> str:
    if path.is_symlink() or not path.is_file():
        raise DocumentError(f"{path}: expected a regular Word file")
    if not zipfile.is_zipfile(path):
        raise DocumentError(f"{path}: Word file is not a valid OOXML archive")
    try:
        with zipfile.ZipFile(path) as archive:
            names = set(archive.namelist())
            if "word/document.xml" not in names or "[Content_Types].xml" not in names:
                raise DocumentError(f"{path}: required Word document parts are missing")
            if "word/vbaProject.bin" in names:
                raise DocumentError(f"{path}: macro-enabled Word content is not allowed")
            root = ET.fromstring(archive.read("word/document.xml"))
    except DocumentError:
        raise
    except (OSError, zipfile.BadZipFile, ET.ParseError) as exc:
        raise DocumentError(f"{path}: Word document could not be read: {exc}") from exc
    return " ".join(text for text in root.itertext() if text)


def validate_docx(document: SourceDocument, path: Path) -> str:
    if path.name != document.docx_name:
        raise DocumentError(
            f"{path}: Word filename must be exactly {document.docx_name!r}"
        )
    payload_size = path.stat().st_size
    if payload_size < 2048:
        raise DocumentError(
            f"{path}: Word document is only {payload_size} bytes; expected at least 2048"
        )
    text = extract_docx_text(path)
    normalized = _normalized_text(text)
    if len(normalized) < 40:
        raise DocumentError(f"{path}: Word document contains too little extractable text")
    missing_ids = [
        task_id for task_id in document.task_ids if task_id not in normalized
    ]
    if missing_ids:
        raise DocumentError(
            f"{path}: Word text is missing task IDs: {', '.join(missing_ids)}"
        )
    return text


def validate_pdf_set(paths: ProjectPaths, documents: Sequence[SourceDocument]) -> int:
    validate_project_tree(paths)
    by_pdf = {
        canonical_output_path(paths, document).resolve(): document
        for document in documents
    }
    validated = 0
    for pdf_path, document in sorted(by_pdf.items(), key=lambda item: str(item[0])):
        validate_pdf(document, pdf_path)
        validated += 1

    for locale in LOCALES:
        directory = _absolute(paths.output_dir(locale))
        expected = (
            _absolute(paths.root)
            / "ratiomera-statistics"
            / locale
            / "downloads"
            / "files"
        )
        if directory != expected:
            raise DocumentError(f"noncanonical download output directory: {directory}")
        _reject_symlink_components(directory, anchor=paths.root)
        if not directory.is_dir() or directory.is_symlink():
            raise DocumentError(f"missing safe download output directory: {directory}")
        for path in sorted(directory.iterdir(), key=lambda item: item.name.casefold()):
            name = path.name
            lower_name = name.casefold()
            if re.search(
                r"(?:^|[-_])expanded[-_](?:exercises?|solutions?)(?:[-_.]|$)",
                lower_name,
            ):
                continue
            pdf_like = lower_name.endswith(".pdf") and bool(
                re.search(
                    r"(?:^|[-_])(?:exercises?|solutions?)(?:[-_.]|$)",
                    lower_name,
                )
            )
            if not pdf_like:
                continue
            if path.is_symlink() or not path.is_file():
                raise DocumentError(
                    f"learner-PDF-like path must be a regular file: {path}"
                )
            match = PDF_NAME_RE.fullmatch(name)
            if not match:
                raise DocumentError(f"{path}: unstable learner-PDF filename")
            if match.group("locale") != locale:
                raise DocumentError(f"{path}: filename locale does not match its folder")
            if path.resolve() not in by_pdf:
                raise DocumentError(f"{path}: learner PDF has no editable source document")
    return validated


def validate_docx_set(paths: ProjectPaths, documents: Sequence[SourceDocument]) -> int:
    validate_project_tree(paths)
    by_docx = {
        canonical_docx_output_path(paths, document).resolve(): document
        for document in documents
    }
    validated = 0
    for docx_path, document in sorted(by_docx.items(), key=lambda item: str(item[0])):
        validate_docx(document, docx_path)
        validated += 1

    for locale in LOCALES:
        directory = _absolute(paths.output_dir(locale))
        expected = (
            _absolute(paths.root)
            / "ratiomera-statistics"
            / locale
            / "downloads"
            / "files"
        )
        if directory != expected:
            raise DocumentError(f"noncanonical download output directory: {directory}")
        _reject_symlink_components(directory, anchor=paths.root)
        if not directory.is_dir() or directory.is_symlink():
            raise DocumentError(f"missing safe download output directory: {directory}")
        for path in sorted(directory.iterdir(), key=lambda item: item.name.casefold()):
            name = path.name
            lower_name = name.casefold()
            docx_like = lower_name.endswith(".docx") and bool(
                re.search(
                    r"(?:^|[-_])(?:exercises?|solutions?)(?:[-_.]|$)",
                    lower_name,
                )
            )
            if not docx_like:
                continue
            if path.is_symlink() or not path.is_file():
                raise DocumentError(
                    f"learner-Word-like path must be a regular file: {path}"
                )
            match = DOCX_NAME_RE.fullmatch(name)
            if not match:
                raise DocumentError(f"{path}: unstable learner-Word filename")
            if match.group("locale") != locale:
                raise DocumentError(f"{path}: filename locale does not match its folder")
            if path.resolve() not in by_docx:
                raise DocumentError(
                    f"{path}: learner Word document has no editable source document"
                )
    return validated


def resolve_selected_sources(
    paths: ProjectPaths,
    requested: Iterable[str],
    corpus: Sequence[SourceDocument],
) -> list[SourceDocument]:
    root = paths.root.resolve()
    source_root = paths.source_root.resolve()
    selected: list[SourceDocument] = []
    seen: set[Path] = set()
    canonical = {document.path.resolve(): document for document in corpus}
    for value in requested:
        supplied = Path(value)
        candidates = (
            [supplied]
            if supplied.is_absolute()
            else [root / supplied, source_root / supplied]
        )
        existing = next(
            (candidate for candidate in candidates if candidate.is_file()), None
        )
        if existing is None:
            raise DocumentError(f"source does not exist: {value}")
        _reject_symlink_components(existing, anchor=paths.root)
        resolved = existing.resolve()
        try:
            resolved.relative_to(source_root)
        except ValueError as exc:
            raise DocumentError(
                f"source must be inside {source_root}: {resolved}"
            ) from exc
        if resolved not in canonical:
            raise DocumentError(
                f"selected path is not an exact discovered canonical source: {resolved}"
            )
        if resolved not in seen:
            selected.append(canonical[resolved])
            seen.add(resolved)
    return sorted(selected, key=lambda item: item.document_id)


def self_test(paths: ProjectPaths) -> tuple[int, int]:
    """Render and validate one temporary pair; the temporary tree is removed."""
    safe_base = _safe_temp_base(paths.root)
    with tempfile.TemporaryDirectory(
        prefix="ratiomera-download-self-test-", dir=safe_base
    ) as temp_name:
        temp_root = Path(temp_name).resolve()
        source_root = temp_root / "ratiomera-statistics" / "_shared" / "download-sources"
        for locale in LOCALES:
            (source_root / locale).mkdir(parents=True, exist_ok=True)
        for locale in LOCALES:
            output_dir = (
                temp_root
                / "ratiomera-statistics"
                / locale
                / "downloads"
                / "files"
            )
            output_dir.mkdir(parents=True, exist_ok=True)
        fixture_paths = ProjectPaths(
            root=temp_root,
            source_root=source_root,
            brand_logo=paths.brand_logo,
            is_self_test=True,
        )
        hostile_temp = temp_root / "hostile-tmp"
        hostile_temp.mkdir()
        sentinel = temp_root / "hostile-hook-ran"
        (hostile_temp / "hook.py").write_text(
            "from pathlib import Path\n"
            f"Path({str(sentinel)!r}).write_text('unsafe', encoding='utf-8')\n",
            encoding="utf-8",
            newline="\n",
        )
        (hostile_temp / "_quarto.yml").write_text(
            "project:\n"
            "  type: default\n"
            "  post-render:\n"
            "    - python3 hook.py\n",
            encoding="utf-8",
            newline="\n",
        )
        base = "topic-99-pipeline-self-test"
        documents: list[SourceDocument] = []
        for document_type, pair_type in (
            ("exercises", "solutions"),
            ("solutions", "exercises"),
        ):
            document_id = f"{base}-{document_type}-en"
            source = source_root / "en" / f"{document_id}.md"
            task_lines: list[str] = []
            for variant in range(1, 11):
                task_lines.extend(
                    [
                        f"## T99-A01-V{variant:02d}: Temporary {document_type} pipeline check",
                        "",
                        "This temporary sentence verifies extractable PDF text "
                        "with $x = 2 + 3 = 5$ and is deleted after the self-test.",
                        "",
                    ]
                )
            source.write_text(
                "\n".join(
                    [
                        "---",
                        f'title: "Pipeline self-test {document_type}"',
                        'subtitle: "Temporary validation fixture, not learner material"',
                        f'document-id: "{document_id}"',
                        f'topic-id: "{base}"',
                        'topic-number: "99"',
                        'topic-slug: "pipeline-self-test"',
                        f'document-type: "{document_type}"',
                        'locale: "en"',
                        f'paired-document-id: "{base}-{pair_type}-en"',
                        "---",
                        "",
                        *task_lines,
                    ]
                ),
                encoding="utf-8",
                newline="\n",
            )
            documents.append(parse_source(source))
        validate_source_set(documents, require_complete_locales=False)
        previous_temp = os.environ.get("TMPDIR")
        os.environ["TMPDIR"] = str(hostile_temp)
        try:
            for document in documents:
                render_document(fixture_paths, document)
            for document in documents:
                _destination, changed = render_document(fixture_paths, document)
                if changed:
                    raise DocumentError(
                        "self-test render was not byte-stable on the second pass"
                    )
        finally:
            if previous_temp is None:
                os.environ.pop("TMPDIR", None)
            else:
                os.environ["TMPDIR"] = previous_temp
        if sentinel.exists():
            raise DocumentError("hostile ancestor Quarto hook ran during self-test")
        validated = validate_pdf_set(fixture_paths, documents)
        return len(documents), validated
