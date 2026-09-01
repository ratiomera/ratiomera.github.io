# Contributing to Ratiomera

Ratiomera is a multilingual Quarto website. The source repository is designed so
a third person can review the learning material, regenerate the public site,
and understand which files own each part of the platform.

## Source of truth

- Edit QMD, Markdown, R, Python, JavaScript, SCSS, CSS, YAML, and brand source
  files. Never edit generated files in `docs/` by hand.
- English is canonical and uses US English. Finalize it first, then adapt the
  same structure into natural German for Switzerland, followed by natural
  standard Albanian. Albanian learner text uses informal singular address.
- Keep formulas, numerical values, table data, figure geometry, exercise IDs,
  material IDs, and counter IDs equivalent across languages.
- Use `config/terminology.yml` for recurring terminology and
  `config/content-parity.yml` for routes, status, and multilingual coverage.
- Do not add invented people, affiliations, reviews, downloads, usage totals,
  or publication claims.

## Important directories

| Path | Purpose |
|---|---|
| `en/`, `de/`, `sq/` | Project-wide localized pages |
| `ratiomera-statistics/` | Statistics branch, lessons, document sources, and downloads |
| `ratiomera-mathematics/` | Planned Mathematics branch pages |
| `ratiomera-statistics/_shared/` | Shared lesson data, figures, downloads, and document pipelines |
| `assets/` | Brand assets and pinned third-party browser dependencies |
| `config/` | Public machine-readable configuration and validation registries |
| `js/`, `styles/` | Shared browser behavior and presentation |
| `scripts/` | Rendering, document generation, and validation tools |
| `docs/` | Generated GitHub Pages output, retained until deployment is automated |

Contributions must use the tracked public sources. Never commit private teaching
materials, internal working notes, unpublished assessments, or personal data
that has not been approved for publication. Standard Python tooling can install
the exact validator dependencies with
`python3 -m pip install -r requirements.txt`.

## Required checks

After a user-facing or structural change, run:

```bash
python3 scripts/validate-download-documents.py
python3 scripts/validate-summary-documents.py --locale en
python3 scripts/validate-summary-documents.py --locale de
python3 scripts/validate-summary-documents.py --locale sq
python3 scripts/test-download-documents.py
python3 scripts/test-summary-documents.py
python3 scripts/build-download-bundles.py --check
Rscript scripts/validate-multilingual.R
scripts/render-site.sh
Rscript scripts/validate-counters.R
python3 scripts/validate-rendered-site.py
```

The complete render must finish without remote MathJax references, broken
internal links, missing localized assets, or fabricated counter values. Review
desktop and phone layouts, keyboard navigation, visible focus, figures, tables,
formulas, and download actions before publication.

## Publication boundaries

Remote counter providers are disabled. Do not enable one without documenting
the provider, transmitted information, retention, failure behavior, and
privacy consequences. Public contact addresses are centralized in
`_variables.yml`; never place mailbox passwords, recovery codes, API keys,
access tokens, or other credentials in the repository. Do not add a remote,
commit, publish, change DNS or deployment settings, or enable donations without
maintainer review.
