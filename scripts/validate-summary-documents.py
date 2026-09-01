#!/usr/bin/env python3
"""Validate Ratiomera summary sources and their paired PDF/DOCX outputs."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from summary_documents import (
    ProjectPaths,
    SummaryDocumentError,
    discover_sources,
    parse_topic_arguments,
    select_documents,
    validate_output_set,
    validate_source_set,
)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--locale", choices=("en", "de", "sq"), default="en")
    parser.add_argument("--topic", type=int, action="append")
    parser.add_argument("--sources-only", action="store_true")
    arguments = parser.parse_args()
    try:
        paths = ProjectPaths.from_script(Path(__file__))
        documents = discover_sources(paths, arguments.locale)
        validate_source_set(documents, require_complete=True)
        selected = select_documents(documents, parse_topic_arguments(arguments.topic))
        if arguments.sources_only:
            print(f"Summary validation passed: {len(selected)} {arguments.locale} source(s).")
            return 0
        pdf_count, docx_count, page_counts = validate_output_set(paths, selected)
        pages = ", ".join(
            f"T{document.number}={page_counts[document.document_id]}p" for document in selected
        )
        print(
            f"Summary validation passed: {len(selected)} source(s), "
            f"{pdf_count} PDF(s), {docx_count} DOCX file(s); {pages}."
        )
        return 0
    except SummaryDocumentError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
