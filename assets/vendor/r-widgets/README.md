# Vendored R htmlwidget browser dependencies

This directory owns the browser files required by the Introduction to
Statistics Simulated Example tabs. Quarto and the R packages still generate
the widget HTML and JSON payloads. The final page references are rewritten to
this stable source-owned resource tree because the cloud file provider can
prune selected files from Quarto's generated `docs/site_libs` directory after
an otherwise successful render.

The versioned paths are copied byte-for-byte from the matching files generated
in `.quarto/_freeze/site_libs` by the reviewed local toolchain. They comprise
HTMLWidgets, htmltools fill CSS, jQuery, DT/DataTables, Crosstalk, Plotly, and
typedarray. Do not edit minified or generated vendor files by hand. When an R
package version changes, regenerate this complete owned set, retain the
versioned directories, run `scripts/render-site.sh`, and require
`scripts/validate-rendered-widgets.py` to confirm source-to-published byte
identity and live widget initialization.

## Third-party notices

The runtime files remain third-party software under their respective
licenses. The copied notices in [`licenses/`](licenses/) travel with the
published vendor directory. Ratiomera's source ownership of this directory
means that the files are versioned and deployed reliably; it does not change
their copyright or license terms.

| Runtime path | Upstream component | Version | License notice |
|---|---|---:|---|
| `htmltools-fill-0.5.9/` | R package `htmltools` | 0.5.9 | GPL-2.0-or-later; `licenses/GPL-2.txt` |
| `htmlwidgets-1.6.4/` | R package `htmlwidgets` | 1.6.4 | MIT; `licenses/htmlwidgets-LICENSE` and `licenses/MIT-template.txt` |
| `jquery-3.6.0/` | jQuery / OpenJS Foundation | 3.6.0 | MIT; `licenses/jquery-LICENSE.txt` |
| `datatables-binding-0.34.0/`, `datatables-css-0.0.0/` | R package `DT` | 0.34.0 | MIT; `licenses/DT-LICENSE` and `licenses/MIT-template.txt` |
| `dt-core-1.13.6/` | DataTables | 1.13.6 | MIT; `licenses/DataTables-LICENSE.txt` |
| `crosstalk-1.2.2/` | R package `crosstalk` | 1.2.2 | MIT; `licenses/crosstalk-LICENSE` and `licenses/MIT-template.txt` |
| `plotly-binding-4.11.0/`, `plotly-htmlwidgets-css-2.11.1/` | R package `plotly` | 4.11.0 | MIT; `licenses/plotly-R-LICENSE` and `licenses/MIT-template.txt` |
| `plotly-main-2.11.1/` | Plotly.js | 2.11.1 | MIT; `licenses/plotlyjs-LICENSE` |
| `typedarray-0.1/` | Plotly typedarray helper | 0.1 | MIT; `licenses/typedarray-LICENSE` |

The package-specific R `LICENSE` files record the applicable copyright
holders; `MIT-template.txt` contains R's standard MIT terms referenced by
those files. The minified jQuery file also retains its upstream license
banner.
