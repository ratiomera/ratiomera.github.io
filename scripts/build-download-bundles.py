#!/usr/bin/env python3
"""Build and verify deterministic multilingual course-material ZIP bundles."""

from __future__ import annotations

import argparse
import binascii
import re
import tempfile
import unicodedata
import zipfile
from pathlib import Path

import yaml


PROJECT_ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = PROJECT_ROOT / "ratiomera-statistics" / "_shared" / "downloads.yml"
LOCALES = ("en", "de", "sq")
CATEGORY_ORDER = ("summary", "exercises", "solutions")
FIXED_TIMESTAMP = (1980, 1, 1, 0, 0, 0)


def portable_slug(value: str) -> str:
    """Return an ASCII folder name that remains portable across ZIP clients."""
    normalized = unicodedata.normalize("NFKD", value)
    ascii_value = normalized.encode("ascii", "ignore").decode("ascii").lower()
    return re.sub(r"[^a-z0-9]+", "-", ascii_value).strip("-")


def load_registry() -> dict:
    with REGISTRY_PATH.open(encoding="utf-8") as handle:
        registry = yaml.safe_load(handle)
    if registry.get("schema_version") != 4:
        raise ValueError("The bundle builder requires Downloads schema version 4.")
    return registry


def localized_file_records(material: dict, locale: str) -> list[tuple[Path, str]]:
    records: list[tuple[Path, str]] = []
    for file_record in material.get("files", []):
        relative_path = file_record.get("paths", {}).get(locale)
        if not relative_path:
            raise ValueError(f"Material {material.get('id')} has no {locale} path.")
        source = PROJECT_ROOT / relative_path
        if not source.is_file():
            raise FileNotFoundError(f"Missing bundle source: {source}")
        records.append((source, source.name))
    return records


def validated_zip_output(package: dict, locale: str) -> tuple[Path, str]:
    output_record = package.get("files", [])
    if len(output_record) != 1 or str(output_record[0].get("format", "")).upper() != "ZIP":
        raise ValueError(f"Package {package.get('id')} must define exactly one ZIP file.")
    output_relative = output_record[0].get("paths", {}).get(locale)
    if not output_relative:
        raise ValueError(f"Package {package.get('id')} has no {locale} ZIP path.")
    return PROJECT_ROOT / output_relative, Path(output_relative).stem


def expected_course_bundle_members(
    registry: dict, course: dict, bundle: dict, locale: str
) -> list[tuple[Path, str]]:
    includes = tuple(bundle.get("includes", []))
    if not includes or any(category not in CATEGORY_ORDER for category in includes):
        raise ValueError(f"Bundle {bundle.get('id')} has invalid included categories.")
    if tuple(sorted(includes, key=CATEGORY_ORDER.index)) != includes:
        raise ValueError(f"Bundle {bundle.get('id')} categories are not in canonical order.")

    _destination, archive_root = validated_zip_output(bundle, locale)

    members: list[tuple[Path, str]] = []
    for topic in course.get("topics", []):
        number = int(topic["number"])
        topic_folder = f"{number:02d}-{portable_slug(topic['title'][locale])}"
        materials_by_category = {
            material["category"]: material for material in topic.get("materials", [])
        }
        for category in includes:
            material = materials_by_category.get(category)
            if material is None or material.get("status") != "available":
                raise ValueError(
                    f"Bundle {bundle.get('id')} requires available {category} material "
                    f"for Topic {number}."
                )
            folder_parts = [archive_root, topic_folder]
            if len(includes) > 1:
                category_number = CATEGORY_ORDER.index(category) + 1
                category_label = registry["categories"][category][locale]
                folder_parts.append(
                    f"{category_number:02d}-{portable_slug(category_label)}"
                )
            for source, basename in localized_file_records(material, locale):
                archive_name = "/".join((*folder_parts, basename))
                members.append((source, archive_name))

    names = [name for _, name in members]
    if len(names) != len(set(names)):
        raise ValueError(f"Bundle {bundle.get('id')} produces duplicate archive paths.")
    return members


def expected_topic_package_members(
    registry: dict, topic: dict, package: dict, locale: str
) -> list[tuple[Path, str]]:
    includes = tuple(package.get("includes", []))
    if includes != CATEGORY_ORDER:
        raise ValueError(
            f"Topic package {package.get('id')} must include summary, exercises, "
            "and solutions in canonical order."
        )
    _destination, archive_root = validated_zip_output(package, locale)
    materials_by_category = {
        material["category"]: material for material in topic.get("materials", [])
    }
    members: list[tuple[Path, str]] = []
    for category in CATEGORY_ORDER:
        material = materials_by_category.get(category)
        if material is None or material.get("status") != "available":
            raise ValueError(
                f"Topic package {package.get('id')} requires available {category} material."
            )
        category_number = CATEGORY_ORDER.index(category) + 1
        category_label = registry["categories"][category][locale]
        category_folder = f"{category_number:02d}-{portable_slug(category_label)}"
        for source, basename in localized_file_records(material, locale):
            members.append((source, "/".join((archive_root, category_folder, basename))))

    names = [name for _, name in members]
    if len(members) != 6 or len(names) != len(set(names)):
        raise ValueError(
            f"Topic package {package.get('id')} must produce six unique archive paths."
        )
    return members


def output_path(package: dict, locale: str) -> Path:
    destination, _archive_root = validated_zip_output(package, locale)
    return destination


def write_bundle(destination: Path, members: list[tuple[Path, str]]) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        dir=destination.parent, prefix=f".{destination.name}.", suffix=".tmp", delete=False
    ) as temporary:
        temporary_path = Path(temporary.name)
    try:
        with zipfile.ZipFile(
            temporary_path,
            mode="w",
            compression=zipfile.ZIP_DEFLATED,
            compresslevel=9,
        ) as archive:
            for source, archive_name in members:
                info = zipfile.ZipInfo(archive_name, date_time=FIXED_TIMESTAMP)
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o100644 << 16
                info.flag_bits |= 0x800
                archive.writestr(info, source.read_bytes(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
        temporary_path.replace(destination)
    finally:
        if temporary_path.exists():
            temporary_path.unlink()


def file_crc32(path: Path) -> int:
    checksum = 0
    with path.open("rb") as handle:
        while chunk := handle.read(1024 * 1024):
            checksum = binascii.crc32(chunk, checksum)
    return checksum & 0xFFFFFFFF


def verify_bundle(destination: Path, members: list[tuple[Path, str]]) -> None:
    if not destination.is_file() or not zipfile.is_zipfile(destination):
        raise ValueError(f"Bundle is missing or unreadable: {destination}")
    expected_names = [archive_name for _, archive_name in members]
    with zipfile.ZipFile(destination) as archive:
        actual_names = archive.namelist()
        if actual_names != expected_names:
            raise ValueError(f"Bundle member order or names are stale: {destination}")
        for source, archive_name in members:
            info = archive.getinfo(archive_name)
            if info.date_time != FIXED_TIMESTAMP:
                raise ValueError(f"Bundle timestamp is not deterministic: {archive_name}")
            if info.file_size != source.stat().st_size or info.CRC != file_crc32(source):
                raise ValueError(f"Bundle member does not match its source: {archive_name}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="Verify existing ZIP bundles without rebuilding them.",
    )
    args = parser.parse_args()
    registry = load_registry()
    courses = registry.get("courses", [])
    if not courses:
        raise ValueError("No download collection is registered.")

    completed = 0
    topic_packages = 0
    course_bundles = 0
    for course in courses:
        for topic in course.get("topics", []):
            package = topic.get("package")
            if not package:
                raise ValueError(f"Topic {topic.get('id')} has no registered package.")
            for locale in LOCALES:
                members = expected_topic_package_members(registry, topic, package, locale)
                destination = output_path(package, locale)
                if not args.check:
                    write_bundle(destination, members)
                verify_bundle(destination, members)
                completed += 1
                topic_packages += 1
                verb = "Verified" if args.check else "Built"
                print(f"{verb} {destination.relative_to(PROJECT_ROOT)} ({len(members)} files)")
        for bundle in course.get("bundles", []):
            for locale in LOCALES:
                members = expected_course_bundle_members(registry, course, bundle, locale)
                destination = output_path(bundle, locale)
                if not args.check:
                    write_bundle(destination, members)
                verify_bundle(destination, members)
                completed += 1
                course_bundles += 1
                verb = "Verified" if args.check else "Built"
                print(f"{verb} {destination.relative_to(PROJECT_ROOT)} ({len(members)} files)")
    print(
        "Download bundle validation PASS: "
        f"{completed} localized ZIP files "
        f"({topic_packages} topic packages, {course_bundles} course bundles)."
    )


if __name__ == "__main__":
    main()
