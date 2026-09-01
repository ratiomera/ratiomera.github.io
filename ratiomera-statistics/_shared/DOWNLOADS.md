# Shared download architecture

The English, German, and Albanian Downloads pages are rendered from the same
registry, `ratiomera-statistics/_shared/downloads.yml`. The registry uses schema 4
and groups materials by learning sequence, so another Statistics or Mathematics
sequence can be added without creating a second download system.

## Stable IDs and visible choices

Introduction to Statistics currently registers 36 stable logical download IDs:

- 24 individual document IDs, comprising one summary, exercise sheet, and
  complete solution set for each of eight topics. Each ID retains its PDF and
  editable Word actions.
- Eight topic-package IDs. Each points to one localized ZIP containing that
  topic's six PDF and Word documents.
- Four course-bundle IDs. `intro-statistics-all-materials` is the single primary
  complete package. The summary-only, exercise-only, and solution-only ZIPs are
  secondary choices inside a restrained disclosure.

Only nine package choices display a count: the eight topic ZIPs and the one
primary complete ZIP. Individual files and secondary bundles remain directly
downloadable but do not display separate numbers. This keeps the visible metric
attached to an exact, understandable package rather than mixing unrelated
formats or suggesting that several asset totals describe one person.

## Real files and deterministic bundles

Only entries marked `available` may define files. Every file record must point
to a real localized asset in the corresponding locale's `downloads/files/`
directory. Unavailable entries must not contain placeholder links or file
records.

Run `python3 scripts/build-download-bundles.py` after any registered PDF, Word,
topic title, package, or bundle definition changes. The builder creates and
validates 36 localized ZIP files: 24 topic packages and 12 course bundles.
Archives use stable top-level names, chronological topic folders, normalized
timestamps, and deterministic member ordering. Use `--check` to verify names,
members, timestamps, sizes, and checksums without rewriting them.

## Release mapping and count semantics

Each learning sequence declares a `release_key`. The matching entry under
`download_counts.providers.github_releases.releases` in `config/counters.yml`
will later map that key to one repository and one exact release tag. An exact
tag makes the time span represented by the release asset's provider total
explicit. Switching tags starts a new release-specific total unless the future
provider deliberately supplies a cumulative value.

Every action retains a local `download` URL as its failure-safe default and
declares its stable material ID, release key, and exact release-asset filename.
When GitHub Releases is enabled outside a local host, the shared client resolves
each matching action to its public HTTPS asset URL. Link resolution is separate
from count rendering: a valid public link may be used even if its count is
missing, while a missing or ambiguous asset leaves only that action on its local
fallback.

A visible package count is read from the `download_count` field of that exact
ZIP asset. It means completed downloads reported for the release asset. It is
not a unique-person total, a page-visit total, or a local click count. Providers
remain disabled locally, so the component shows the configured nonnumeric dash
and sends no remote request. No browser click handler increments any value.

## Validation

After editing the registry or renderer, run:

```bash
python3 scripts/build-download-bundles.py --check
Rscript scripts/validate-multilingual.R
Rscript scripts/validate-counters.R
```

The counter validator requires a current rendered site. The multilingual
validator checks the source registry, stable IDs, localized paths, ZIP magic,
renderer contract, and the exact set of 27 locale-specific package-counter IDs.
