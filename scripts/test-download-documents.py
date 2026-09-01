#!/usr/bin/env python3
"""Disposable regression tests for the learner-PDF pipeline."""

from __future__ import annotations

import os
import shutil
import tempfile
import unittest
from pathlib import Path

from download_documents import (
    _body_for_render,
    DocumentError,
    ProjectPaths,
    canonical_output_path,
    discover_sources,
    extract_pdf_text,
    parse_source,
    render_document,
    resolve_selected_sources,
    self_test,
    validate_pdf_set,
    validate_source_set,
)


SCRIPT_PATH = Path(__file__).resolve()
REAL_PROJECT = ProjectPaths.from_script(SCRIPT_PATH)


class DownloadDocumentPipelineTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(
            prefix="ratiomera-download-regression-"
        )
        self.root = Path(self.temporary.name).resolve()
        self.source_root = (
            self.root
            / "ratiomera-statistics"
            / "_shared"
            / "download-sources"
        )
        for locale in ("en", "de", "sq"):
            (self.source_root / locale).mkdir(parents=True)
            (
                self.root
                / "ratiomera-statistics"
                / locale
                / "downloads"
                / "files"
            ).mkdir(parents=True)
        self.paths = ProjectPaths(
            root=self.root,
            source_root=self.source_root,
            brand_logo=REAL_PROJECT.brand_logo,
            is_self_test=True,
        )

    def tearDown(self) -> None:
        self.temporary.cleanup()

    @staticmethod
    def task_body(
        number: str,
        *,
        numeric_text: str = "Values: -2, 10.5, and 25%.",
        prefix: str = "",
    ) -> str:
        lines = [prefix] if prefix else []
        for variant in range(1, 11):
            lines.extend(
                [
                    f"## T{number}-A01-V{variant:02d}: Localized task title",
                    "",
                    numeric_text,
                    "",
                ]
            )
        return "\n".join(lines)

    def write_document(
        self,
        *,
        number: str = "01",
        slug: str = "test-topic",
        document_type: str = "exercises",
        locale: str = "en",
        body: str | None = None,
    ) -> Path:
        pair_type = (
            "solutions" if document_type == "exercises" else "exercises"
        )
        base = f"topic-{number}-{slug}"
        document_id = f"{base}-{document_type}-{locale}"
        source = self.source_root / locale / f"{document_id}.md"
        if body is None:
            body = self.task_body(number)
        source.write_text(
            "\n".join(
                [
                    "---",
                    f'title: "Temporary {document_type} test"',
                    f'document-id: "{document_id}"',
                    f'topic-id: "{base}"',
                    f'topic-number: "{number}"',
                    f'topic-slug: "{slug}"',
                    f'document-type: "{document_type}"',
                    f'locale: "{locale}"',
                    f'paired-document-id: "{base}-{pair_type}-{locale}"',
                    "---",
                    "",
                    body,
                    "",
                ]
            ),
            encoding="utf-8",
            newline="\n",
        )
        return source

    def write_pair(
        self,
        *,
        number: str = "01",
        slug: str = "test-topic",
        locale: str = "en",
        exercise_numbers: str = "Values: -2, 10.5, and 25%.",
        solution_numbers: str = "Values: -2, 10.5, 25%, and 8.5.",
    ) -> None:
        self.write_document(
            number=number,
            slug=slug,
            document_type="exercises",
            locale=locale,
            body=self.task_body(number, numeric_text=exercise_numbers),
        )
        self.write_document(
            number=number,
            slug=slug,
            document_type="solutions",
            locale=locale,
            body=self.task_body(number, numeric_text=solution_numbers),
        )

    def test_resource_and_include_bypasses_are_rejected(self) -> None:
        probes = (
            "![plot](plot.png)",
            "![plot][figure]\n[figure]: plot.png",
            "![plot]",
            "<IMG\n SRC='plot.png'>",
            "<span>raw HTML</span>",
            "{{< include file.md >}}",
            "{{% include file.md %}}",
            "[local file](file:///etc/passwd)",
            "[absolute file](/etc/passwd)",
            "[parent file](../secret.txt)",
            "[relative file](notes.txt)",
            "```{=typst}\n#read(\"secret\")\n```",
            "`#let f = read; f(\"secret\")`{=typst}",
            "# image(\"plot.png\")",
            '#import "@preview/package:1.0.0"',
            "\\includegraphics{plot.png}",
        )
        for index, probe in enumerate(probes):
            with self.subTest(probe=probe):
                source = self.write_document(
                    slug=f"probe-{index:02d}",
                    body=self.task_body("01", prefix=probe),
                )
                with self.assertRaises(DocumentError):
                    parse_source(source)

    def test_legacy_math_delimiters_are_rejected_before_render(self) -> None:
        for index, legacy in enumerate((r"\(x = 2\)", r"\[x = 2\]")):
            with self.subTest(legacy=legacy):
                source = self.write_document(
                    slug=f"legacy-math-{index:02d}",
                    body=self.task_body("01", prefix=legacy),
                )
                with self.assertRaisesRegex(
                    DocumentError, r"use Pandoc \$\.\.\.\$"
                ):
                    parse_source(source)

    def test_pandoc_inline_math_renders_as_extractable_formula_text(self) -> None:
        formula = "Formula check: $x = 2 + 3 = 5$."
        self.write_pair(
            exercise_numbers=formula,
            solution_numbers=formula,
        )
        document = parse_source(
            self.source_root
            / "en"
            / "topic-01-test-topic-exercises-en.md"
        )
        destination, _changed = render_document(self.paths, document)
        text, pages = extract_pdf_text(destination)
        normalized = " ".join(text.split())
        self.assertGreaterEqual(pages, 1)
        self.assertIn("x", normalized)
        self.assertRegex(normalized, r"2\s*\+\s*3\s*=\s*5")

    def test_render_body_keeps_real_task_ids_together(self) -> None:
        prefix = "\n".join(
            [
                "````text",
                "## T01-A99-V01: ignored inside fence",
                "````",
                "<!-- ## T01-A99-V02: ignored inside comment -->",
            ]
        )
        source = self.write_document(body=self.task_body("01", prefix=prefix))
        document = parse_source(source)
        rendered = _body_for_render(document)
        self.assertIn("## `T01-A01-V01`: Localized task title", rendered)
        self.assertIn("## T01-A99-V01: ignored inside fence", rendered)
        self.assertNotIn("## `T01-A99-V01`", rendered)

    def test_long_albanian_task_ids_remain_extractable(self) -> None:
        sections: list[str] = []
        long_titles = (
            "Ushtrimi dhe arsyetimi pas përshtatjes për rezultatin paraprak",
            "Koha e kërkimit dhe saktësia pas përshtatjes për përvojën në arkiv",
        )
        for archetype, title in enumerate(long_titles, start=1):
            for variant in range(1, 11):
                sections.extend(
                    [
                        f"## T01-A{archetype:02d}-V{variant:02d}: {title}",
                        "",
                        "Vlerat mësimore janë 2, 10.5 dhe 25%.",
                        "",
                    ]
                )
        source = self.write_document(
            locale="sq",
            body="\n".join(sections),
        )
        document = parse_source(source)
        destination, _changed = render_document(self.paths, document)
        text, pages = extract_pdf_text(destination)
        normalized = " ".join(text.split())
        self.assertGreaterEqual(pages, 1)
        for task_id in document.task_ids:
            self.assertIn(task_id, normalized)

    def test_shadow_source_and_noncanonical_selection_are_rejected(self) -> None:
        self.write_pair()
        shadow_dir = self.source_root / "en" / "nested-shadow"
        shadow_dir.mkdir()
        shadow = shadow_dir / "topic-01-test-topic-exercises-en.md"
        shadow.write_text("shadow", encoding="utf-8")
        with self.assertRaises(DocumentError):
            discover_sources(self.source_root)

        shutil.rmtree(shadow_dir)
        corpus = discover_sources(self.source_root)
        outside = self.root / "shadow" / corpus[0].path.name
        outside.parent.mkdir()
        outside.write_text(corpus[0].path.read_text(encoding="utf-8"), encoding="utf-8")
        with self.assertRaises(DocumentError):
            resolve_selected_sources(self.paths, [str(outside)], corpus)

    def test_duplicate_topic_number_or_slug_is_rejected(self) -> None:
        self.write_pair(slug="alpha")
        self.write_pair(slug="beta")
        with self.assertRaisesRegex(DocumentError, "maps to both"):
            validate_source_set(
                discover_sources(self.source_root),
                require_complete_locales=False,
            )

    def test_heading_parser_handles_fences_comments_and_indented_code(self) -> None:
        prefix = "\n".join(
            [
                "````text",
                "## T01-A99-V01: ignored inside fence",
                "T01-A99-V09: ignored setext text inside fence",
                "---",
                "```",
                "## T01-A99-V02: still ignored after shorter fence",
                "````",
                "<!-- ## T01-A99-V03: ignored inside comment -->",
                "    ## T01-A99-V04: ignored as indented code",
            ]
        )
        source = self.write_document(body=self.task_body("01", prefix=prefix))
        document = parse_source(source)
        self.assertEqual(len(document.task_ids), 10)

        malformed = (
            "# T01-A01-V01: wrong level",
            "##### T01-A01-V01: wrong level",
            " ## T01-A01-V01: indented heading",
            "## T01-A01-V01 missing colon",
            "## T01-A01-V01: ",
            "T01-A01-V01: setext heading\n---",
            "```text\n## T01-A01-V01: never closed",
        )
        for index, heading in enumerate(malformed):
            with self.subTest(heading=heading):
                probe = self.write_document(
                    slug=f"heading-{index:02d}", body=heading
                )
                with self.assertRaises(DocumentError):
                    parse_source(probe)

    @unittest.skipUnless(hasattr(os, "symlink"), "symlinks are unavailable")
    def test_symlink_sources_locales_and_outputs_are_rejected(self) -> None:
        target = self.root / "outside-source.md"
        target.write_text("outside", encoding="utf-8")
        linked_source = (
            self.source_root / "en" / "topic-01-test-topic-exercises-en.md"
        )
        linked_source.symlink_to(target)
        with self.assertRaises(DocumentError):
            discover_sources(self.source_root)
        linked_source.unlink()

        real_locale = self.source_root / "en-real"
        (self.source_root / "en").rename(real_locale)
        (self.source_root / "en").symlink_to(real_locale, target_is_directory=True)
        with self.assertRaises(DocumentError):
            discover_sources(self.source_root)
        (self.source_root / "en").unlink()
        real_locale.rename(self.source_root / "en")

        source = self.write_document()
        document = parse_source(source)
        output = self.paths.output_dir("en")
        outside_output = self.root / "outside-output"
        outside_output.mkdir()
        output.rmdir()
        output.symlink_to(outside_output, target_is_directory=True)
        with self.assertRaises(DocumentError):
            canonical_output_path(self.paths, document)

    def test_numeric_tokens_match_by_type_across_locales(self) -> None:
        for locale in ("en", "de", "sq"):
            self.write_pair(locale=locale)
        documents = discover_sources(self.source_root)
        validate_source_set(documents, require_complete_locales=True)

        self.write_document(
            document_type="exercises",
            locale="de",
            body=self.task_body("01", numeric_text="Values: -2, 10.6, and 25%."),
        )
        with self.assertRaisesRegex(DocumentError, "numeric-token mismatch"):
            validate_source_set(
                discover_sources(self.source_root),
                require_complete_locales=True,
            )

    def test_word_hyphen_before_number_is_not_treated_as_a_minus_sign(self) -> None:
        localized = {
            "en": "A width-5 bin contains -2 observations.",
            "de": "Eine Klasse mit Breite 5 enthält -2 Beobachtungen.",
            "sq": "Një klasë me gjerësi 5 përmban -2 vrojtime.",
        }
        for locale, numeric_text in localized.items():
            self.write_pair(
                locale=locale,
                exercise_numbers=numeric_text,
                solution_numbers=numeric_text,
            )
        validate_source_set(
            discover_sources(self.source_root),
            require_complete_locales=True,
        )

    def test_orphan_scan_catches_case_variants_but_ignores_foreign_files(self) -> None:
        output = self.paths.output_dir("en")
        foreign = output / "topic-01-test-topic-instructor-notes-en.pdf"
        foreign.write_bytes(b"not managed by this pipeline")
        self.assertEqual(validate_pdf_set(self.paths, []), 0)

        malformed = output / "Topic-01-Test-Topic-Exercises-EN.PDF"
        malformed.write_bytes(b"orphan")
        with self.assertRaisesRegex(DocumentError, "unstable learner-PDF filename"):
            validate_pdf_set(self.paths, [])

    def test_hostile_temp_project_isolated_and_render_is_byte_stable(self) -> None:
        source_count, pdf_count = self_test(REAL_PROJECT)
        self.assertEqual((source_count, pdf_count), (2, 2))


if __name__ == "__main__":
    unittest.main(verbosity=2)
