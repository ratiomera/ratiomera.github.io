# Practice exercise and solution PDF and Word sources

This directory is the public, repository-maintained source area for learner-facing
exercise and solution PDFs and Word documents. It is not a second website content tree. The Quarto website
renders `.qmd` files, while this directory contains `.md` files that are rendered
only by `scripts/render-download-documents.py` in an isolated temporary project.

This directory and renderer own practice exercises and complete solutions only.
Topic summary Markdown, PDF, DOCX, raster figures, and three-page note sections
belong to the separate pipeline under `../summary-sources/` and
`scripts/render-summary-documents.py`. Neither pipeline may discover or rewrite
the other pipeline's source or generated files.

Only real, reviewed learner documents belong in the locale directories. Do not
turn the template or an incomplete draft into a published download. Publication
requires complete exercise and solution documents in all three locales.

Locale source directories:

- `en/` for canonical US English;
- `de/` for natural academic German for Switzerland;
- `sq/` for natural standard Albanian with informal singular learner address.

Copy `_document-template.md` into the appropriate locale directory, replace all
angle-bracket placeholders, and follow the metadata contract documented in the
template. Exercise and solution sources form a required pair and use identical
visible task IDs.

For Introduction to Statistics, the authoritative 81-group worksheet inventory
is `config/intro-stats-practice-map.tsv`. Do not maintain
a competing hand-written ordering in a generator. The TSV fixes each group's
raw source anchor, learning objective, stable `TNN-ANN` ID, practice part, and
reason-first status.

Every exercise and solution document has exactly two top-level parts in this
order:

```markdown
# Part I: Theory
# Part II: Calculator Practice
```

Group headings use level two and task headings use level three. A `mixed` group
belongs in Calculator Practice because it requires numerical or graphical work
as well as interpretation. A reason-first task asks the learner to state the
statistical idea before carrying out the calculation. Each matching solution
uses visible, localized step labels for reasoning, calculation where relevant,
result, checking, and contextual interpretation. A final answer by itself is
not a complete solution.

English is the canonical progressive-authoring source. Rebuild and validate it
first. German and Albanian are adapted only after that English structure is
final. PDF and Word files are rendered after all three locale pairs pass the
strict machine checks; human language and publication review remains a separate
requirement before the In Review material can be marked Published.

Learner sources are text-only Markdown: prose, headings, lists, tables, and math.
Images, file-backed resources, raw Typst, include mechanisms, and local-file
links are intentionally unsupported so the isolated renderer never reads or
publishes an undeclared file.

Write inline math with Pandoc delimiters such as `$x = 2$` and display math
with `$$...$$`. Do not use the legacy `\(...\)` or `\[...\]` forms: they are
rejected before Quarto because they do not survive this Markdown-to-Typst path
reliably.

One Markdown source produces a PDF and an editable Word document with the same
stable stem. Both formats must contain the complete task-ID sequence. The Word
file is an alternative format of the same logical material, not a separate
exercise tier or a second counter identity. Register both real paths under the
existing material ID in `../downloads.yml` only after machine validation and
human visual review.
