---
title: "<localized document title>"
subtitle: "<localized topic title>"
document-id: "topic-<NN>-<topic-slug>-<exercises-or-solutions>-<locale>"
topic-id: "topic-<NN>-<topic-slug>"
topic-number: "<NN>"
topic-slug: "<topic-slug>"
document-type: "<exercises-or-solutions>"
locale: "<en-de-or-sq>"
paired-document-id: "topic-<NN>-<topic-slug>-<paired-type>-<locale>"
---

<!--
TEMPLATE ONLY. This file is not learner content and is never rendered.

Replace every angle-bracket placeholder. Introduction to Statistics practice
uses the authoritative map in
`config/intro-stats-practice-map.tsv`. Each document has
exactly two localized top-level parts in Theory then Calculator Practice order.
Each mapped group uses a visible level-two heading. Each learner task or
solution uses a visible level-three heading whose stable ID has the form
TNN-ANN-VNN. Use exactly one space after the heading marks and `: ` before a
nonempty localized title. Number groups from A01 without gaps and give each
group exactly ten variants, V01 through V10. Keep every group contiguous and
use the same IDs, section placement, and order in the paired exercise and
solution documents. A localized heading follows each colon. Complete solutions
use visible localized step labels and never provide only a final answer.

Example shape only:

# <localized Part I: Theory heading>

## ANN: <localized group heading>

### TNN-ANN-VNN: <localized task or solution heading>

<complete localized content>

# <localized Part II: Calculator Practice heading>

Use text, Markdown tables, and math only. Do not add images, file resources,
includes, raw Typst, or local-file links.

Use Pandoc `$...$` for inline math and `$$...$$` for display math. Legacy
`\(...\)` and `\[...\]` delimiters fail validation.
-->
