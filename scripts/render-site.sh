#!/usr/bin/env bash

set -euo pipefail

script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
project_dir=$(CDPATH= cd -- "$script_dir/.." && pwd)
cd "$project_dir"

case "${1:-}" in
  "")
    render_command=(quarto render --no-clean)
    ;;
  --clean)
    render_command=(quarto render)
    ;;
  *)
    echo "Usage: scripts/render-site.sh [--clean]" >&2
    exit 2
    ;;
esac

Rscript scripts/validate-multilingual.R
"${render_command[@]}"

# This second, outer-process check is intentional. In a cloud-synced workspace,
# the file provider can reconcile Quarto's output directory just after Quarto's
# internal post-render hooks finish. Rechecking after the Quarto process exits
# makes the deployable output complete before this command succeeds.
Rscript scripts/ensure-site-libs.R

# Repeat the dependency publication step across a short early-warning window.
# Durable R-htmlwidget publication does not depend on this timing: the same
# step rewrites all widget URLs to the source-owned assets/vendor/r-widgets
# namespace, and the final widget validator enforces its byte identity.
for settle_delay_seconds in 2 2; do
  sleep "$settle_delay_seconds"
  Rscript scripts/ensure-site-libs.R
done

Rscript scripts/localize-mathjax.R
Rscript scripts/validate-counters.R
PYTHONDONTWRITEBYTECODE=1 python3 scripts/validate-rendered-site.py
PYTHONDONTWRITEBYTECODE=1 python3 scripts/validate-rendered-widgets.py

echo "Ratiomera site render and final output validation completed."
