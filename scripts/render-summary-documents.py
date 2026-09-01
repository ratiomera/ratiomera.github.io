#!/usr/bin/env python3
"""Render reviewed Ratiomera summary Markdown to paired PDF and DOCX assets."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from summary_documents import (
    ProjectPaths,
    SummaryDocumentError,
    discover_sources,
    parse_topic_arguments,
    render_document,
    select_documents,
    validate_source_set,
)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--locale", choices=("en", "de", "sq"), default="en")
    parser.add_argument("--topic", type=int, action="append")
    arguments = parser.parse_args()
    try:
        paths = ProjectPaths.from_script(Path(__file__))
        documents = discover_sources(paths, arguments.locale)
        validate_source_set(documents, require_complete=True)
        selected = select_documents(documents, parse_topic_arguments(arguments.topic))
        for document in selected:
            pdf, docx = render_document(paths, document)
            print(f"Rendered {pdf.relative_to(paths.root)}")
            print(f"Rendered {docx.relative_to(paths.root)}")
        return 0
    except SummaryDocumentError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

