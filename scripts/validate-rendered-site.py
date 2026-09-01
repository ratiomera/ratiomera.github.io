#!/usr/bin/env python3
"""Validate local targets and loaded resources in the rendered Pages tree."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


SKIPPED_SCHEMES = {"about", "blob", "data", "javascript", "mailto", "tel"}
RESOURCE_TAGS = {"audio", "embed", "iframe", "img", "link", "object", "script", "source", "track", "video"}


@dataclass(frozen=True)
class Reference:
    source: Path
    tag: str
    attribute: str
    value: str


class PageParser(HTMLParser):
    def __init__(self, source: Path) -> None:
        super().__init__(convert_charrefs=True)
        self.source = source
        self.identifiers: set[str] = set()
        self.references: list[Reference] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if values.get("id"):
            self.identifiers.add(values["id"])
        if tag == "a" and values.get("name"):
            self.identifiers.add(values["name"])

        for attribute in ("href", "src", "data"):
            value = values.get(attribute)
            if value:
                self.references.append(Reference(self.source, tag, attribute, value))

        for attribute in ("srcset",):
            value = values.get(attribute)
            if not value:
                continue
            for candidate in value.split(","):
                url = candidate.strip().split(maxsplit=1)[0]
                if url:
                    self.references.append(Reference(self.source, tag, attribute, url))


def candidate_targets(target: Path, url_path: str) -> list[Path]:
    if target.is_dir() or url_path.endswith("/"):
        return [target / "index.html"]
    if target.suffix:
        return [target]
    return [target, target.with_suffix(".html"), target / "index.html"]


def validate(site_root: Path) -> int:
    site_root = site_root.resolve()
    html_files = sorted(site_root.rglob("*.html"))
    if not html_files:
        raise SystemExit(f"No rendered HTML files found under {site_root}")

    identifiers: dict[Path, set[str]] = {}
    references: list[Reference] = []
    for html_file in html_files:
        parser = PageParser(html_file)
        parser.feed(html_file.read_text(encoding="utf-8", errors="strict"))
        identifiers[html_file.resolve()] = parser.identifiers
        references.extend(parser.references)

    missing: list[tuple[Reference, Path]] = []
    bad_fragments: list[tuple[Reference, Path, str]] = []
    outside: list[tuple[Reference, Path]] = []
    remote_resources: list[Reference] = []

    for reference in references:
        split = urlsplit(reference.value)
        scheme = split.scheme.lower()
        if scheme in {"http", "https"} or reference.value.startswith("//"):
            if reference.tag in RESOURCE_TAGS:
                remote_resources.append(reference)
            continue
        if scheme in SKIPPED_SCHEMES:
            continue
        if scheme:
            continue

        url_path = unquote(split.path)
        if not url_path:
            target = reference.source.resolve()
        elif url_path.startswith("/"):
            target = (site_root / url_path.lstrip("/")).resolve()
        else:
            target = (reference.source.parent / url_path).resolve()

        try:
            target.relative_to(site_root)
        except ValueError:
            outside.append((reference, target))
            continue

        existing = next((path for path in candidate_targets(target, url_path) if path.exists()), None)
        if existing is None:
            missing.append((reference, target))
            continue

        fragment = unquote(split.fragment)
        if fragment and existing.suffix.lower() == ".html":
            if fragment not in identifiers.get(existing.resolve(), set()):
                bad_fragments.append((reference, existing, fragment))

    failures = len(missing) + len(bad_fragments) + len(outside) + len(remote_resources)
    if failures:
        for reference, target in missing:
            print(f"MISSING {reference.source.relative_to(site_root)}: {reference.value} -> {target}")
        for reference, target, fragment in bad_fragments:
            print(
                f"BAD FRAGMENT {reference.source.relative_to(site_root)}: "
                f"{reference.value} -> {target}#{fragment}"
            )
        for reference, target in outside:
            print(f"OUTSIDE SITE {reference.source.relative_to(site_root)}: {reference.value} -> {target}")
        for reference in remote_resources:
            print(
                f"REMOTE RESOURCE {reference.source.relative_to(site_root)}: "
                f"<{reference.tag} {reference.attribute}={reference.value!r}>"
            )
        print(
            "Rendered-site validation FAILED: "
            f"{len(missing)} missing target(s), {len(bad_fragments)} bad fragment(s), "
            f"{len(outside)} outside-site reference(s), {len(remote_resources)} remote resource(s)."
        )
        return 1

    local_count = sum(
        1
        for reference in references
        if not urlsplit(reference.value).scheme and not reference.value.startswith("//")
    )
    print(
        "Rendered-site validation PASS: "
        f"{len(html_files)} HTML file(s), {local_count} local reference(s), "
        "no missing targets, bad fragments, outside-site references, or remote resources."
    )
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site-root", default="docs", type=Path)
    args = parser.parse_args()
    return validate(args.site_root)


if __name__ == "__main__":
    raise SystemExit(main())
