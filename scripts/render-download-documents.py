#!/usr/bin/env python3
"""Render Ratiomera exercise and solution sources to PDF and editable Word."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from download_documents import (
    DocumentError,
    ProjectPaths,
    discover_sources,
    render_document,
    render_word_document,
    resolve_selected_sources,
    self_test,
    validate_project_tree,
    validate_source_set,
)


def parser() -> argparse.ArgumentParser:
    command = argparse.ArgumentParser(
        description=(
            "Render selected learner Markdown sources to stable locale PDF and Word paths. "
            "Use explicit source paths or --all."
        )
    )
    command.add_argument(
        "sources",
        nargs="*",
        metavar="SOURCE",
        help="source path relative to the project or download-sources directory",
    )
    command.add_argument(
        "--all", action="store_true", help="render every valid learner source"
    )
    command.add_argument(
        "--self-test",
        action="store_true",
        help="render and validate a temporary pair outside the project, then remove it",
    )
    return command


def main() -> int:
    arguments = parser().parse_args()
    if arguments.self_test:
        if arguments.all or arguments.sources:
            parser().error("--self-test cannot be combined with sources or --all")
    elif arguments.all == bool(arguments.sources):
        parser().error("provide explicit SOURCE paths or --all, but not both")

    paths = ProjectPaths.from_script(Path(__file__))
    try:
        if arguments.self_test:
            source_count, pdf_count = self_test(paths)
            print(
                f"Learner-PDF self-test passed: {source_count} temporary sources, "
                f"{pdf_count} temporary PDFs; fixture removed."
            )
            return 0

        validate_project_tree(paths)
        corpus = discover_sources(paths.source_root)
        validate_source_set(corpus, require_complete_locales=arguments.all)
        selected = (
            corpus
            if arguments.all
            else resolve_selected_sources(paths, arguments.sources, corpus)
        )
        if not selected:
            raise DocumentError("no learner source documents were selected")
        for document in selected:
            for render in (render_document, render_word_document):
                destination, changed = render(paths, document)
                state = "updated" if changed else "unchanged"
                print(f"{state}: {destination.relative_to(paths.root)}")
        print(
            f"Rendered and validated {len(selected)} learner PDF(s) and "
            f"{len(selected)} learner Word document(s)."
        )
        return 0
    except DocumentError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
