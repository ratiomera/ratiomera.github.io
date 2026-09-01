#!/usr/bin/env python3
"""Disposable regression tests for the Ratiomera topic-summary pipeline."""

from __future__ import annotations

import struct
import tempfile
import unittest
import zipfile
from dataclasses import replace
from pathlib import Path
from xml.etree import ElementTree as ET

from summary_documents import (
    NOTE_PAGE_COUNT,
    DOCX_LAYOUT_STATISTICS,
    EP_NS,
    ProjectPaths,
    SummaryDocumentError,
    TABLE_WIDTH_PROFILES,
    W_NS,
    _canonicalize_ooxml_property_children,
    _normalize_docx_app_properties,
    _set_docx_paragraph_layout,
    _validate_ooxml_property_children,
    _validate_summary_tab_output,
    build_table_width_filter,
    build_wrapper,
    normalize_docx,
    parse_source,
    validate_docx,
    validate_source_set,
)


class SummaryDocumentPipelineTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(prefix="ratiomera-summary-test-")
        self.root = Path(self.temporary.name).resolve()
        self.source_root = self.root / "ratiomera-statistics" / "_shared" / "summary-sources"
        self.topic_summary_root = (
            self.root / "ratiomera-statistics" / "_shared" / "topic-summaries"
        )
        self.asset_root = self.source_root / "assets"
        (self.source_root / "en").mkdir(parents=True)
        (self.topic_summary_root / "en").mkdir(parents=True)
        (self.asset_root / "en").mkdir(parents=True)
        (self.root / "ratiomera-statistics" / "en" / "downloads" / "files").mkdir(parents=True)
        self.paths = ProjectPaths(
            root=self.root,
            source_root=self.source_root,
            topic_summary_root=self.topic_summary_root,
            asset_root=self.asset_root,
            logo=self.asset_root / "en" / "ratiomera-summary-logo.png",
        )
        self._write_png(self.paths.logo, width=900, height=230)
        self.figure = self.asset_root / "en" / "topic-01-descriptive-statistics-summary-figure-en.png"
        self._write_png(self.figure, width=1200, height=700)
        self.write_summary_tab()

    def tearDown(self) -> None:
        self.temporary.cleanup()

    @staticmethod
    def _write_png(path: Path, *, width: int, height: int) -> None:
        # Source validation needs only the immutable PNG signature and IHDR dimensions.
        path.write_bytes(
            b"\x89PNG\r\n\x1a\n"
            + struct.pack(">I", 13)
            + b"IHDR"
            + struct.pack(">II", width, height)
            + b"\x08\x06\x00\x00\x00"
        )

    @staticmethod
    def _body(extra: str = "") -> str:
        paragraphs = " ".join(
            [
                "Evidence belongs to a defined variable, case, measurement, and research question."
                for _ in range(115)
            ]
        )
        return "\n".join(
            [
                "## Purpose and foundations",
                paragraphs,
                extra,
                "## Core ideas",
                "| Idea | Meaning | Check |",
                "|---|---|---|",
                "| Center | Typical position | Inspect context |",
                "| Spread | Observed variation | Retain units |",
                paragraphs,
                "## Formula guide",
                "$$",
                "\\bar{x}=\\frac{1}{n}\\sum_{i=1}^{n}x_i",
                "$$",
                "$$",
                "s^2=\\frac{1}{n-1}\\sum_{i=1}^{n}(x_i-\\bar{x})^2",
                "$$",
                "$$",
                "z_i=\\frac{x_i-\\bar{x}}{s}",
                "$$",
                "| Symbol | Role | Reading |",
                "|---|---|---|",
                "| $n$ | Sample size | Number of valid cases |",
                "| $s$ | Standard deviation | Spread in original units |",
                "## Reading the explanatory figure",
                "![A detailed accessible description of a distribution with a central cluster, two tails, labeled axes, frequencies, and visible unusual observations.](assets/topic-01-descriptive-statistics-summary-figure-en.png){#fig-summary-t01 width=92%}",
                paragraphs,
                "## Interpretation checklist",
                paragraphs,
                "## How this topic connects",
                paragraphs,
                "",
            ]
        )

    @staticmethod
    def _summary_tab_body(extra: str = "") -> str:
        paragraph = " ".join(
            [
                "A course-page summary keeps the main decision sequence visible and connects each statistical quantity to the research question."
                for _ in range(9)
            ]
        )
        return "\n".join(
            [
                paragraph,
                "",
                "### Shared Reasoning {.cs-heading}",
                "",
                "| Step | Question |",
                "|---|---|",
                "| Define | What is measured? |",
                "| Match | Which summary is defensible? |",
                "",
                paragraph,
                "",
                "### Shared Interpretation {.cs-heading}",
                "",
                paragraph,
                extra,
                "",
            ]
        )

    def write_summary_tab(self, *, body: str | None = None) -> Path:
        path = self.topic_summary_root / "en" / "t01.md"
        path.write_text(
            body if body is not None else self._summary_tab_body(),
            encoding="utf-8",
            newline="\n",
        )
        return path

    def write_source(self, *, body: str | None = None) -> Path:
        source = self.source_root / "en" / "topic-01-descriptive-statistics-summary-en.md"
        source.write_text(
            "\n".join(
                [
                    "---",
                    'title: "Descriptive Statistics"',
                    'subtitle: "Temporary safety fixture"',
                    'document-id: "topic-01-descriptive-statistics-summary-en"',
                    'course-id: "intro-statistics"',
                    'topic-id: "topic-01-descriptive-statistics"',
                    'topic-number: "01"',
                    'topic-slug: "descriptive-statistics"',
                    'document-type: "summary"',
                    'locale: "en"',
                    'figure-asset: "topic-01-descriptive-statistics-summary-figure-en.png"',
                    "---",
                    "",
                    body if body is not None else self._body(),
                ]
            ),
            encoding="utf-8",
            newline="\n",
        )
        return source

    def test_valid_source_has_stable_paired_output_names(self) -> None:
        document = parse_source(self.write_source(), self.paths)
        self.assertEqual(document.pdf_name, "topic-01-descriptive-statistics-summary-en.pdf")
        self.assertEqual(document.docx_name, "topic-01-descriptive-statistics-summary-en.docx")

    def test_resource_code_and_traversal_probes_are_rejected(self) -> None:
        probes = (
            "https://example.invalid/figure.png",
            "../private/source.md",
            "```{python}\nprint(1)\n```",
            "{{< include hidden.md >}}",
            "<script>unsafe</script>",
        )
        for probe in probes:
            with self.subTest(probe=probe):
                with self.assertRaises(SummaryDocumentError):
                    parse_source(self.write_source(body=self._body(probe)), self.paths)

    def test_unsafe_website_summary_tab_markdown_is_rejected(self) -> None:
        probes = (
            "https://example.invalid/source",
            "../private/source.md",
            "[remote](https://example.invalid/source)",
            "![image](local.png)",
            "{{< include hidden.md >}}",
            "```{python}\nprint(1)\n```",
            "<script>unsafe</script>",
            "## A wrapper-owned heading",
            "An em dash is prohibited — here.",
        )
        source = self.write_source()
        for probe in probes:
            with self.subTest(probe=probe):
                self.write_summary_tab(body=self._summary_tab_body(probe))
                with self.assertRaises(SummaryDocumentError):
                    parse_source(source, self.paths)

    def test_missing_website_summary_tab_source_is_rejected(self) -> None:
        source = self.write_source()
        self.write_summary_tab().unlink()
        with self.assertRaisesRegex(SummaryDocumentError, "missing trusted website"):
            parse_source(source, self.paths)

    def test_wrapper_uses_shared_summary_first_with_clean_heading_hierarchy(self) -> None:
        document = parse_source(self.write_source(), self.paths)
        wrapper = build_wrapper(document)
        course_heading = "# Course-Page Summary"
        expanded_heading = "# Expanded Reference"
        self.assertLess(wrapper.index(course_heading), wrapper.index("## Shared Reasoning"))
        self.assertLess(wrapper.index("## Shared Interpretation"), wrapper.index(expanded_heading))
        self.assertLess(wrapper.index(expanded_heading), wrapper.index("## Purpose and foundations"))
        self.assertNotIn("### Shared Reasoning", wrapper)
        promoted = document.summary_tab_body.replace(
            "### Shared Reasoning", "## Shared Reasoning"
        ).replace("### Shared Interpretation", "## Shared Interpretation")
        self.assertIn(promoted.strip(), wrapper)

    def test_output_presence_check_requires_shared_headings_and_prose(self) -> None:
        document = parse_source(self.write_source(), self.paths)
        _validate_summary_tab_output(
            document, document.summary_tab_body, self.root / "complete-output"
        )
        with self.assertRaisesRegex(SummaryDocumentError, "does not retain"):
            _validate_summary_tab_output(
                document,
                "Shared Reasoning Shared Interpretation",
                self.root / "incomplete-output",
            )

    def test_output_presence_check_tolerates_pdf_math_glyph_extraction(self) -> None:
        document = parse_source(self.write_source(), self.paths)
        math_heading_document = replace(
            document,
            summary_tab_headings=(
                "Shared Reasoning",
                "What to Check Before Interpreting $r$ Carefully",
            ),
        )
        extracted = (
            document.summary_tab_body
            + "\nWhat to Check Before Interpreting r Carefully\n"
        )
        _validate_summary_tab_output(
            math_heading_document,
            extracted,
            self.root / "math-heading-output",
        )

    def test_output_presence_check_tolerates_pdf_line_hyphenation(self) -> None:
        document = parse_source(self.write_source(), self.paths)
        extracted = document.summary_tab_body.replace(
            "statistical quantity", "statisti-\ncal quantity"
        )
        _validate_summary_tab_output(
            document,
            extracted,
            self.root / "line-hyphenated-output",
        )

    def test_wrapper_owns_exactly_three_note_pages_per_format(self) -> None:
        document = parse_source(self.write_source(), self.paths)
        wrapper = build_wrapper(document)
        self.assertEqual(wrapper.count("#pagebreak()"), NOTE_PAGE_COUNT + 2)
        self.assertEqual(wrapper.count("#pagebreak(weak: true)"), 0)
        self.assertEqual(
            wrapper.count('w:br w:type="page"'), NOTE_PAGE_COUNT + 1
        )
        for page in range(1, NOTE_PAGE_COUNT + 1):
            self.assertEqual(wrapper.count(f"Notes {page} of {NOTE_PAGE_COUNT}"), 2)

    def test_german_wrapper_localizes_central_labels(self) -> None:
        document = parse_source(self.write_source(), self.paths)
        german = replace(
            document,
            locale="de",
            metadata={**document.metadata, "title": "Deskriptive Statistik"},
        )
        wrapper = build_wrapper(german)
        self.assertIn("Einführung in die Statistik | Thema 1", wrapper)
        self.assertIn('toc-title: "Inhaltsverzeichnis"', wrapper)
        self.assertIn('fig-title: "Abbildung"', wrapper)
        self.assertIn('tbl-title: "Tabelle"', wrapper)
        self.assertIn("# Zusammenfassung der Kursseite", wrapper)
        self.assertIn("# Erweiterte Referenz", wrapper)
        self.assertIn("*Dokument-ID:", wrapper)
        for page in range(1, NOTE_PAGE_COUNT + 1):
            self.assertEqual(wrapper.count(f"Notizen {page} von {NOTE_PAGE_COUNT}"), 2)
        self.assertNotIn("Notes 1 of 3", wrapper)

    def test_albanian_wrapper_localizes_central_labels(self) -> None:
        document = parse_source(self.write_source(), self.paths)
        albanian = replace(
            document,
            locale="sq",
            metadata={**document.metadata, "title": "Statistika përshkruese"},
        )
        wrapper = build_wrapper(albanian)
        self.assertIn("Hyrje në Statistikë | Tema 1", wrapper)
        self.assertIn('toc-title: "Përmbajtja"', wrapper)
        self.assertIn('fig-title: "Figura"', wrapper)
        self.assertIn('tbl-title: "Tabela"', wrapper)
        self.assertIn("# Përmbledhja e faqes së kursit", wrapper)
        self.assertIn("# Referencë e zgjeruar", wrapper)
        self.assertIn("*ID-ja e dokumentit:", wrapper)
        for page in range(1, NOTE_PAGE_COUNT + 1):
            self.assertEqual(wrapper.count(f"Shënime {page} nga {NOTE_PAGE_COUNT}"), 2)
        self.assertNotIn("Notes 1 of 3", wrapper)

    def test_complete_validation_rejects_an_empty_locale(self) -> None:
        with self.assertRaises(SummaryDocumentError):
            validate_source_set([], require_complete=True)

    def test_docx_validator_rejects_svg_media(self) -> None:
        document = parse_source(self.write_source(), self.paths)
        path = self.root / "unsafe.docx"
        padding = b"x" * 13000
        with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_STORED) as archive:
            archive.writestr("[Content_Types].xml", b"<Types/>" + padding)
            archive.writestr("word/document.xml", b"<w:document xmlns:w='http://schemas.openxmlformats.org/wordprocessingml/2006/main'/>")
            archive.writestr("word/styles.xml", b"<w:styles xmlns:w='http://schemas.openxmlformats.org/wordprocessingml/2006/main'/>")
            archive.writestr(
                "docProps/core.xml",
                b"<cp:coreProperties xmlns:cp='http://schemas.openxmlformats.org/package/2006/metadata/core-properties'/>",
            )
            archive.writestr(
                "docProps/app.xml",
                b"<Properties xmlns='http://schemas.openxmlformats.org/officeDocument/2006/extended-properties'/>",
            )
            archive.writestr("word/media/image1.png", b"\x89PNG\r\n\x1a\n")
            archive.writestr("word/media/image2.svg", b"<svg/>")
        with self.assertRaisesRegex(SummaryDocumentError, "SVG"):
            validate_docx(document, path)

    def test_docx_app_normalizer_removes_reference_layout_statistics(self) -> None:
        app_children = "".join(
            f"<{name}>1</{name}>" for name in DOCX_LAYOUT_STATISTICS
        )
        normalized = _normalize_docx_app_properties(
            (
                "<Properties xmlns='" + EP_NS + "'>"
                "<Application>Microsoft Word 12.0.0</Application>"
                + app_children
                + "</Properties>"
            ).encode("utf-8")
        )
        root = ET.fromstring(normalized)
        self.assertEqual(
            root.find(f"{{{EP_NS}}}Application").text,
            "Ratiomera document pipeline",
        )
        for name in DOCX_LAYOUT_STATISTICS:
            self.assertIsNone(root.find(f"{{{EP_NS}}}{name}"))

    def test_all_owned_table_width_profiles_are_complete_and_safe(self) -> None:
        self.assertEqual(set(TABLE_WIDTH_PROFILES), {f"{number:02d}" for number in range(1, 9)})
        self.assertEqual(
            [len(TABLE_WIDTH_PROFILES[f"{number:02d}"]) for number in range(1, 9)],
            [10, 9, 5, 4, 4, 4, 4, 5],
        )
        for profile in TABLE_WIDTH_PROFILES.values():
            for widths in profile:
                self.assertEqual(sum(widths), 100)
                self.assertTrue(all(12 <= width <= 72 for width in widths))

    def test_lua_filter_owns_each_table_width_and_rejects_shape_drift(self) -> None:
        document = parse_source(self.write_source(), self.paths)
        lua = build_table_width_filter(document)
        self.assertEqual(
            sum(line.startswith("  {") for line in lua.splitlines()),
            len(TABLE_WIDTH_PROFILES["01"]),
        )
        self.assertIn("#tbl.colspecs", lua)
        self.assertIn("more Markdown tables", lua)
        self.assertIn("fewer Markdown tables", lua)

    def test_word_property_normalizer_orders_and_deduplicates_owned_children(self) -> None:
        root = ET.fromstring(
            (
                f"<w:root xmlns:w='{W_NS}'>"
                "<w:pPr><w:jc/><w:spacing/><w:pStyle/><w:jc/><w:keepLines/></w:pPr>"
                "<w:tblPr><w:tblLook/><w:tblW/><w:tblBorders/><w:tblLayout/></w:tblPr>"
                "<w:tcPr><w:vAlign/><w:tcW/><w:shd/></w:tcPr>"
                "</w:root>"
            )
        )
        _canonicalize_ooxml_property_children(root)
        expected = {
            "pPr": ["pStyle", "keepLines", "spacing", "jc"],
            "tblPr": ["tblW", "tblBorders", "tblLayout", "tblLook"],
            "tcPr": ["tcW", "shd", "vAlign"],
        }
        for node in root:
            local = node.tag.rsplit("}", 1)[-1]
            self.assertEqual(
                [child.tag.rsplit("}", 1)[-1] for child in node],
                expected[local],
            )
        _validate_ooxml_property_children(root, self.root / "normalized.docx")
        paragraph = root.find(f"{{{W_NS}}}pPr")
        paragraph[:] = list(reversed(list(paragraph)))
        with self.assertRaisesRegex(SummaryDocumentError, "schema order"):
            _validate_ooxml_property_children(root, self.root / "scrambled.docx")

    def test_table_header_layout_overrides_duplicate_inherited_alignment(self) -> None:
        paragraph = ET.fromstring(
            f"<w:p xmlns:w='{W_NS}'><w:pPr>"
            "<w:jc w:val='center'/><w:jc w:val='right'/>"
            "</w:pPr><w:r><w:t>Header</w:t></w:r></w:p>"
        )
        _set_docx_paragraph_layout(paragraph, header=True)
        _canonicalize_ooxml_property_children(paragraph)
        alignments = paragraph.findall(f"./{{{W_NS}}}pPr/{{{W_NS}}}jc")
        self.assertEqual(len(alignments), 1)
        self.assertEqual(alignments[0].get(f"{{{W_NS}}}val"), "left")


if __name__ == "__main__":
    unittest.main(verbosity=2)
