#!/usr/bin/env python3
"""Validate Ratiomera learner sources, pairs, and generated PDF and Word files."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from download_documents import (
    DocumentError,
    LOCALES,
    ProjectPaths,
    discover_sources,
    validate_docx_set,
    validate_pdf_set,
    validate_project_tree,
    validate_source_set,
)


def parser() -> argparse.ArgumentParser:
    command = argparse.ArgumentParser(
        description=(
            "Validate stable learner PDF and Word filenames, metadata, "
            "exercise-solution numbering, locale parity, and generated files."
        )
    )
    command.add_argument(
        "--sources-only",
        action="store_true",
        help="validate editable sources without requiring generated PDF or Word files",
    )
    command.add_argument(
        "--allow-incomplete-locales",
        action="store_true",
        help="authoring mode: require pairs but do not require an en/de/sq triplet",
    )
    command.add_argument(
        "--locale",
        choices=LOCALES,
        help=(
            "validate the progressive locale sequence through this locale: en, "
            "then en+de, then en+de+sq; complete triplet coverage is required only "
            "by the strict validator"
        ),
    )
    return command


def main() -> int:
    command = parser()
    arguments = command.parse_args()
    if arguments.locale and not arguments.sources_only:
        command.error("--locale is an authoring option and requires --sources-only")
    paths = ProjectPaths.from_script(Path(__file__))
    try:
        validate_project_tree(paths)
        documents = discover_sources(paths.source_root)
        if arguments.locale:
            locale_index = LOCALES.index(arguments.locale)
            allowed_locales = set(LOCALES[: locale_index + 1])
            documents = [
                document for document in documents if document.locale in allowed_locales
            ]
        validate_source_set(
            documents,
            require_complete_locales=(
                not arguments.allow_incomplete_locales and arguments.locale is None
            ),
        )
        from intro_stats_practice_support import validate_existing_practice_structure

        if arguments.locale:
            locales_to_check = LOCALES[: LOCALES.index(arguments.locale) + 1]
        else:
            locales_to_check = LOCALES
        for locale in locales_to_check:
            validate_existing_practice_structure(locale)
        if arguments.sources_only:
            pdf_count = 0
            docx_count = 0
        else:
            pdf_count = validate_pdf_set(paths, documents)
            docx_count = validate_docx_set(paths, documents)
        mode = "source-only" if arguments.sources_only else "source, PDF, and Word"
        locale_note = f", locale {arguments.locale}" if arguments.locale else ""
        print(
            f"Learner-document validation passed ({mode}{locale_note}): "
            f"{len(documents)} source document(s), {pdf_count} PDF(s), "
            f"{docx_count} Word document(s)."
        )
        return 0
    except DocumentError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
