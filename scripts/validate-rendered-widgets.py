#!/usr/bin/env python3
"""Validate the rendered Simulated Example widget and table inventory.

This is deliberately a file-level publication check.  It complements the
general rendered-site link validator by asserting that every localized topic
page still contains its complete Simulated Example, that every htmlwidget has
its JSON payload, and that all browser dependencies required to turn those
placeholders into visible Plotly figures and DataTables are publishable.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path


LOCALES = ("en", "de", "sq")
TOPIC_CONTRACT = {
    "01": {"plotly": 3, "tables": 8},
    "02": {"plotly": 6, "tables": 6},
    "03": {"plotly": 6, "tables": 7},
    "04": {"plotly": 4, "tables": 5},
    "05": {"plotly": 6, "tables": 10},
    "06": {"plotly": 2, "tables": 7},
    "07": {"plotly": 7, "tables": 16},
    "08": {"plotly": 4, "tables": 9},
}

REQUIRED_WIDGET_DEPENDENCIES = (
    "htmltools-fill-0.5.9/fill.css",
    "htmlwidgets-1.6.4/htmlwidgets.js",
    "datatables-css-0.0.0/datatables-crosstalk.css",
    "datatables-binding-0.34.0/datatables.js",
    "jquery-3.6.0/jquery-3.6.0.min.js",
    "dt-core-1.13.6/css/jquery.dataTables.min.css",
    "dt-core-1.13.6/css/jquery.dataTables.extra.css",
    "dt-core-1.13.6/js/jquery.dataTables.min.js",
    "crosstalk-1.2.2/css/crosstalk.min.css",
    "crosstalk-1.2.2/js/crosstalk.min.js",
    "plotly-binding-4.11.0/plotly.js",
    "typedarray-0.1/typedarray.min.js",
    "plotly-htmlwidgets-css-2.11.1/plotly-htmlwidgets.css",
    "plotly-main-2.11.1/plotly-latest.min.js",
)

REQUIRED_VENDOR_SUPPORT_FILES = (
    "README.md",
    "licenses/DT-LICENSE",
    "licenses/DataTables-LICENSE.txt",
    "licenses/GPL-2.txt",
    "licenses/MIT-template.txt",
    "licenses/crosstalk-LICENSE",
    "licenses/htmlwidgets-LICENSE",
    "licenses/jquery-LICENSE.txt",
    "licenses/plotly-R-LICENSE",
    "licenses/plotlyjs-LICENSE",
    "licenses/typedarray-LICENSE",
)


def simulated_pane(html: str, source: Path) -> str:
    start = re.search(r'<div id="tabset-1-2"[^>]*>', html)
    if start is None:
        raise ValueError(f"{source}: Simulated Example pane is missing")
    following = html[start.end() :]
    end = re.search(r'<div id="tabset-1-3"[^>]*>', following)
    if end is None:
        raise ValueError(f"{source}: Exercises pane after Simulated Example is missing")
    return following[: end.start()]


def widget_payloads(html: str, source: Path) -> dict[str, object]:
    payloads: dict[str, object] = {}
    pattern = re.compile(
        r'<script\s+type="application/json"\s+data-for="([^"]+)"[^>]*>'
        r'(.*?)</script>',
        re.DOTALL,
    )
    for widget_id, raw_payload in pattern.findall(html):
        try:
            payloads[widget_id] = json.loads(raw_payload)
        except json.JSONDecodeError as error:
            raise ValueError(f"{source}: invalid JSON payload for {widget_id}: {error}") from error
    return payloads


def source_simulated_ids(source: Path) -> tuple[set[str], set[str]]:
    if not source.is_file():
        raise ValueError(f"canonical source is missing: {source}")
    markdown = source.read_text(encoding="utf-8", errors="strict")
    headings = list(re.finditer(r"^##\s+.+$", markdown, re.MULTILINE))
    if len(headings) < 3:
        raise ValueError(f"{source}: expected at least three level-two tab headings")
    simulated = markdown[headings[1].end() : headings[2].start()]
    identifiers = set(
        re.findall(
            r"(?:#\|\s*label:\s*|\{#)((?:fig|tbl)-[A-Za-z0-9_-]+)",
            simulated,
        )
    )
    return (
        {identifier for identifier in identifiers if identifier.startswith("fig-")},
        {identifier for identifier in identifiers if identifier.startswith("tbl-")},
    )


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def htmlwidget_ids(pane: str, widget_class: str) -> list[str]:
    """Return widget ids without depending on HTML attribute order."""
    identifiers: list[str] = []
    for tag in re.findall(r"<div\b[^>]*>", pane):
        class_match = re.search(r'\bclass="([^"]*)"', tag)
        id_match = re.search(r'\bid="([^"]+)"', tag)
        if class_match is None or id_match is None:
            continue
        classes = set(class_match.group(1).split())
        if {widget_class, "html-widget"}.issubset(classes):
            identifiers.append(id_match.group(1))
    return identifiers


def validate(site_root: Path) -> int:
    site_root = site_root.resolve()
    project_root = site_root.parent
    failures: list[str] = []
    page_count = 0
    plotly_total = 0
    table_total = 0
    datatable_total = 0

    for locale in LOCALES:
        topic_dir = site_root / "ratiomera-statistics" / locale / "intro-stats"
        files = sorted(topic_dir.glob("t0[1-8]_*.html"))
        if len(files) != len(TOPIC_CONTRACT):
            failures.append(
                f"{locale}: expected 8 rendered topic pages, found {len(files)}"
            )

        for source in files:
            topic_match = re.match(r"t(\d{2})_", source.name)
            if topic_match is None or topic_match.group(1) not in TOPIC_CONTRACT:
                failures.append(f"{source}: unrecognized topic filename")
                continue
            topic = topic_match.group(1)
            contract = TOPIC_CONTRACT[topic]
            html = source.read_text(encoding="utf-8", errors="strict")

            try:
                pane = simulated_pane(html, source)
                payloads = widget_payloads(html, source)
                source_figures, source_tables = source_simulated_ids(
                    project_root
                    / "ratiomera-statistics"
                    / locale
                    / "intro-stats"
                    / source.with_suffix(".qmd").name
                )
            except ValueError as error:
                failures.append(str(error))
                continue

            figure_ids = {
                value
                for value in re.findall(r'\bid="(fig-[^"]+)"', pane)
                if "-caption-" not in value
            }
            table_ids = {
                value
                for value in re.findall(r'\bid="(tbl-[^"]+)"', pane)
                if "-caption-" not in value
            }
            plotly_ids = htmlwidget_ids(pane, "plotly")
            datatable_ids = htmlwidget_ids(pane, "datatables")

            if len(figure_ids) != contract["plotly"]:
                failures.append(
                    f"{source}: expected {contract['plotly']} semantic figures, "
                    f"found {len(figure_ids)}"
                )
            if figure_ids != source_figures:
                failures.append(
                    f"{source}: figure IDs differ from source "
                    f"(missing={sorted(source_figures - figure_ids)}, "
                    f"extra={sorted(figure_ids - source_figures)})"
                )
            if len(plotly_ids) != contract["plotly"]:
                failures.append(
                    f"{source}: expected {contract['plotly']} Plotly widgets, "
                    f"found {len(plotly_ids)}"
                )
            if len(table_ids) != contract["tables"]:
                failures.append(
                    f"{source}: expected {contract['tables']} semantic tables, "
                    f"found {len(table_ids)}"
                )
            if table_ids != source_tables:
                failures.append(
                    f"{source}: table IDs differ from source "
                    f"(missing={sorted(source_tables - table_ids)}, "
                    f"extra={sorted(table_ids - source_tables)})"
                )
            pane_without_payloads = re.sub(
                r'<script\s+type="application/json".*?</script>',
                "",
                pane,
                flags=re.DOTALL,
            )
            if len(re.findall(r"<table\b", pane_without_payloads)) != contract["tables"] - 1:
                failures.append(
                    f"{source}: static table markup does not match the owned table inventory"
                )
            if len(datatable_ids) != 1:
                failures.append(
                    f"{source}: expected one interactive raw-data table, "
                    f"found {len(datatable_ids)}"
                )

            for semantic_id in sorted(figure_ids | table_ids):
                if f'id="{semantic_id}-caption-' not in pane:
                    failures.append(f"{source}: {semantic_id} has no rendered caption")

            for widget_id in plotly_ids + datatable_ids:
                payload = payloads.get(widget_id)
                if not isinstance(payload, dict) or not payload:
                    failures.append(f"{source}: {widget_id} has no nonempty JSON payload")
                    continue
                if widget_id in plotly_ids:
                    widget_data = payload.get("x")
                    if not isinstance(widget_data, dict) or not widget_data.get("data"):
                        failures.append(f"{source}: {widget_id} has no Plotly trace data")
                    render_hooks = payload.get("jsHooks", {}).get("render", [])
                    if not any(
                        isinstance(hook, dict)
                        and isinstance(hook.get("data"), str)
                        and hook["data"].strip()
                        for hook in render_hooks
                    ):
                        failures.append(f"{source}: {widget_id} has no localized alt-text hook")
                else:
                    widget_data = payload.get("x")
                    if not isinstance(widget_data, dict) or not widget_data.get("data"):
                        failures.append(f"{source}: {widget_id} has no DataTable row data")
                    container = widget_data.get("container", "") if isinstance(widget_data, dict) else ""
                    if not isinstance(container, str) or "<table" not in container or "<thead" not in container:
                        failures.append(f"{source}: {widget_id} has no DataTable container/header markup")

            for dependency in REQUIRED_WIDGET_DEPENDENCIES:
                stable_reference = f"assets/vendor/r-widgets/{dependency}"
                if stable_reference not in html:
                    failures.append(f"{source}: does not reference {stable_reference}")
                if f"site_libs/{dependency}" in html:
                    failures.append(
                        f"{source}: still references provider-pruned site_libs path: {dependency}"
                    )

            page_count += 1
            plotly_total += len(plotly_ids)
            table_total += len(table_ids)
            datatable_total += len(datatable_ids)

    vendor_relative = Path("assets/vendor/r-widgets")
    vendor_source_root = project_root / vendor_relative
    vendor_output_root = site_root / vendor_relative
    expected_vendor_files = set(REQUIRED_WIDGET_DEPENDENCIES) | set(
        REQUIRED_VENDOR_SUPPORT_FILES
    )
    source_vendor_files = {
        path.relative_to(vendor_source_root).as_posix()
        for path in vendor_source_root.rglob("*")
        if path.is_file()
    }
    output_vendor_files = {
        path.relative_to(vendor_output_root).as_posix()
        for path in vendor_output_root.rglob("*")
        if path.is_file()
    }
    if source_vendor_files != expected_vendor_files:
        failures.append(
            "source-owned widget vendor inventory differs from its contract "
            f"(missing={sorted(expected_vendor_files - source_vendor_files)}, "
            f"extra={sorted(source_vendor_files - expected_vendor_files)})"
        )
    if output_vendor_files != source_vendor_files:
        failures.append(
            "published widget vendor inventory differs from source "
            f"(missing={sorted(source_vendor_files - output_vendor_files)}, "
            f"extra={sorted(output_vendor_files - source_vendor_files)})"
        )
    for relative in sorted(source_vendor_files & output_vendor_files):
        source_dependency = vendor_source_root / relative
        output_dependency = vendor_output_root / relative
        if source_dependency.stat().st_size == 0:
            failures.append(f"source widget vendor file is empty: {relative}")
        elif output_dependency.stat().st_size == 0:
            failures.append(f"published widget vendor file is empty: {relative}")
        elif sha256(source_dependency) != sha256(output_dependency):
            failures.append(f"published widget vendor file differs from source: {relative}")

    if failures:
        for failure in failures:
            print(f"FAIL {failure}")
        print(
            "Rendered-widget validation FAILED: "
            f"{len(failures)} failure(s) across {page_count} parsed topic page(s)."
        )
        return 1

    print(
        "Rendered-widget validation PASS: "
        f"{page_count} localized topic page(s), {plotly_total} Plotly figure(s), "
        f"{table_total} table(s), {datatable_total} interactive raw-data table(s), "
        f"{len(source_vendor_files)} source-owned vendor file(s), all payloads, "
        "captions, dependencies, and license notices present."
    )
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site-root", default="docs", type=Path)
    args = parser.parse_args()
    return validate(args.site_root)


if __name__ == "__main__":
    raise SystemExit(main())
