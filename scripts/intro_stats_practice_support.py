#!/usr/bin/env python3
"""Shared helpers for authored Introduction to Statistics practice documents.

Topic generators own their statistical scenarios, values, questions, and worked
solutions. This module owns only the stable document contract: metadata,
localized document labels, task identifiers, safe writes, and common numerical
helpers. Keeping that contract in one place makes it harder for the English,
German, and Albanian learner PDFs to drift apart.
"""

from __future__ import annotations

import math
import os
import re
import shutil
import tempfile
import csv
from dataclasses import dataclass
from pathlib import Path
from statistics import NormalDist


ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = ROOT / "ratiomera-statistics" / "_shared" / "download-sources"
WORKSHEET_MAP_PATH = ROOT / "config" / "intro-stats-practice-map.tsv"
RAW_MATERIAL_ROOT = ROOT / "_materials" / "intro-stats" / "raw"


@dataclass(frozen=True)
class TopicMetadata:
    number: int
    slug: str
    titles: dict[str, str]


TOPICS: dict[int, TopicMetadata] = {
    1: TopicMetadata(
        1,
        "descriptive-statistics",
        {
            "en": "Descriptive Statistics",
            "de": "Deskriptive Statistik",
            "sq": "Statistika përshkruese",
        },
    ),
    2: TopicMetadata(
        2,
        "probability",
        {
            "en": "Probability",
            "de": "Wahrscheinlichkeit",
            "sq": "Probabiliteti",
        },
    ),
    3: TopicMetadata(
        3,
        "hypothesis-testing",
        {
            "en": "Hypothesis Testing and Confidence Intervals",
            "de": "Hypothesentests und Konfidenzintervalle",
            "sq": "Testimi i hipotezave dhe intervalet e besimit",
        },
    ),
    4: TopicMetadata(
        4,
        "covariance-correlation",
        {
            "en": "Covariance and Correlation",
            "de": "Kovarianz und Korrelation",
            "sq": "Kovarianca dhe korrelacioni",
        },
    ),
    5: TopicMetadata(
        5,
        "simple-linear-regression",
        {
            "en": "Simple Linear Regression",
            "de": "Einfache lineare Regression",
            "sq": "Regresioni i thjeshtë linear",
        },
    ),
    6: TopicMetadata(
        6,
        "partial-correlation",
        {
            "en": "Partial Correlation",
            "de": "Partielle Korrelation",
            "sq": "Korrelacioni i pjesshëm",
        },
    ),
    7: TopicMetadata(
        7,
        "multiple-regression",
        {
            "en": "Multiple Regression",
            "de": "Multiple Regression",
            "sq": "Regresioni i shumëfishtë",
        },
    ),
    8: TopicMetadata(
        8,
        "analysis-of-variance",
        {
            "en": "Analysis of Variance",
            "de": "Varianzanalyse",
            "sq": "Analiza e variancës",
        },
    ),
}


@dataclass(frozen=True)
class PracticeGroup:
    """One authoritative worksheet objective and its practice classification."""

    topic: int
    group_id: str
    source_file: str
    physical_pages: str
    source_task: str
    objective: str
    classification: str
    conceptual_first: bool

    @property
    def group(self) -> int:
        return int(self.group_id[-2:])

    @property
    def section(self) -> str:
        return "theory" if self.classification == "theory" else "calculator"


EXPECTED_GROUP_COUNTS = {1: 15, 2: 16, 3: 12, 4: 7, 5: 10, 6: 2, 7: 9, 8: 10}


def _load_practice_groups() -> tuple[PracticeGroup, ...]:
    if not WORKSHEET_MAP_PATH.is_file() or WORKSHEET_MAP_PATH.is_symlink():
        raise RuntimeError(f"missing authoritative worksheet map: {WORKSHEET_MAP_PATH}")
    with WORKSHEET_MAP_PATH.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        expected_fields = (
            "topic",
            "group_id",
            "source_file",
            "physical_pages",
            "source_task",
            "objective",
            "classification",
            "conceptual_first",
        )
        if tuple(reader.fieldnames or ()) != expected_fields:
            raise RuntimeError("the worksheet map has an unexpected column contract")
        rows: list[PracticeGroup] = []
        for line_number, row in enumerate(reader, start=2):
            try:
                topic = int(row["topic"])
            except ValueError as exc:
                raise RuntimeError(
                    f"{WORKSHEET_MAP_PATH}:{line_number}: topic must be an integer"
                ) from exc
            classification = row["classification"]
            if classification not in {"theory", "calculator", "mixed"}:
                raise RuntimeError(
                    f"{WORKSHEET_MAP_PATH}:{line_number}: invalid classification"
                )
            conceptual = row["conceptual_first"]
            if conceptual not in {"true", "false"}:
                raise RuntimeError(
                    f"{WORKSHEET_MAP_PATH}:{line_number}: conceptual_first must be true or false"
                )
            item = PracticeGroup(
                topic=topic,
                group_id=row["group_id"],
                source_file=row["source_file"],
                physical_pages=row["physical_pages"],
                source_task=row["source_task"],
                objective=row["objective"],
                classification=classification,
                conceptual_first=conceptual == "true",
            )
            expected_group_id = f"T{topic:02d}-A{item.group:02d}"
            if item.group_id != expected_group_id:
                raise RuntimeError(
                    f"{WORKSHEET_MAP_PATH}:{line_number}: expected {expected_group_id}"
                )
            if not re.fullmatch(r"[1-9]\d*(?:-[1-9]\d*)?", item.physical_pages):
                raise RuntimeError(
                    f"{WORKSHEET_MAP_PATH}:{line_number}: invalid physical page range"
                )
            if not item.source_task.strip() or not item.objective.strip():
                raise RuntimeError(
                    f"{WORKSHEET_MAP_PATH}:{line_number}: source task and objective are required"
                )
            if "\u2014" in "\t".join(row.values()):
                raise RuntimeError(
                    f"{WORKSHEET_MAP_PATH}:{line_number}: prohibited em dash"
                )
            rows.append(item)

    if len(rows) != 81:
        raise RuntimeError(f"the worksheet map must contain 81 rows, found {len(rows)}")
    if len({row.group_id for row in rows}) != len(rows):
        raise RuntimeError("the worksheet map contains duplicate practice group IDs")
    for topic, expected_count in EXPECTED_GROUP_COUNTS.items():
        topic_rows = sorted(
            (row for row in rows if row.topic == topic), key=lambda row: row.group
        )
        expected_ids = [f"T{topic:02d}-A{group:02d}" for group in range(1, expected_count + 1)]
        if [row.group_id for row in topic_rows] != expected_ids:
            raise RuntimeError(
                f"the worksheet map does not contain the complete Topic {topic} group sequence"
            )
        if not any(row.section == "theory" for row in topic_rows):
            raise RuntimeError(f"Topic {topic} needs at least one Theory group")
        if not any(row.section == "calculator" for row in topic_rows):
            raise RuntimeError(f"Topic {topic} needs at least one Calculator Practice group")
    return tuple(rows)


PRACTICE_GROUPS = _load_practice_groups()
PRACTICE_GROUP_BY_ID = {group.group_id: group for group in PRACTICE_GROUPS}


def validate_registered_raw_sources() -> None:
    """Require protected worksheet files only when authoring generated practice."""

    for source_file in sorted({group.source_file for group in PRACTICE_GROUPS}):
        source_path = RAW_MATERIAL_ROOT / source_file
        if not source_path.is_file() or source_path.is_symlink():
            raise RuntimeError(f"missing registered raw worksheet source: {source_path}")


def practice_groups_for_topic(topic: int) -> tuple[PracticeGroup, ...]:
    """Return Theory first and Calculator Practice second, stable within each part."""

    topic_groups = tuple(group for group in PRACTICE_GROUPS if group.topic == topic)
    return tuple(
        group
        for section in ("theory", "calculator")
        for group in topic_groups
        if group.section == section
    )


DOCUMENT_LABELS = {
    "en": {
        "exercises": "Exercise Sheet",
        "solutions": "Complete Solutions",
        "exercise_intro": (
            "This sheet contains {tasks} exercises organized into {groups} "
            "learning-objective groups. Work through each exercise before "
            "consulting its matching complete solution. Show the relevant "
            "formula or rule, substituted values, units, and an interpretation."
        ),
        "solution_intro": (
            "These complete solutions use the same identifiers and order as "
            "the Exercise Sheet. Intermediate values are retained until the "
            "stated rounding step, so small differences caused by earlier "
            "rounding are acceptable where noted."
        ),
        "fiction_notice": (
            "All settings, values, data, and software outputs are constructed "
            "teaching material; they are not empirical findings."
        ),
    },
    "de": {
        "exercises": "Übungsblatt",
        "solutions": "Vollständige Lösungen",
        "exercise_intro": (
            "Dieses Blatt enthält {tasks} Übungen in {groups} Gruppen von "
            "Lernzielen. Bearbeite jede Übung, bevor du die passende vollständige "
            "Lösung anschaust. Zeige die relevante Formel oder Regel, die "
            "eingesetzten Werte, die Einheiten und eine Interpretation."
        ),
        "solution_intro": (
            "Diese vollständigen Lösungen verwenden dieselben Kennungen und "
            "dieselbe Reihenfolge wie das Übungsblatt. Zwischenwerte werden bis "
            "zum angegebenen Rundungsschritt beibehalten. Kleine Abweichungen "
            "durch früheres Runden sind deshalb dort zulässig, wo dies vermerkt ist."
        ),
        "fiction_notice": (
            "Alle Kontexte, Werte, Daten und Softwareausgaben sind eigens "
            "erstelltes Lehrmaterial; sie sind keine empirischen Befunde."
        ),
    },
    "sq": {
        "exercises": "Fleta e ushtrimeve",
        "solutions": "Zgjidhjet e plota",
        "exercise_intro": (
            "Kjo fletë përmban {tasks} ushtrime të organizuara në {groups} grupe "
            "objektivash mësimorë. Përpiqu ta zgjidhësh secilin ushtrim para se "
            "të shikosh zgjidhjen e plotë përkatëse. Trego formulën ose rregullin "
            "përkatës, vlerat e zëvendësuara, njësitë dhe interpretimin."
        ),
        "solution_intro": (
            "Këto zgjidhje të plota përdorin të njëjtat kode dhe të njëjtën "
            "renditje si Fleta e ushtrimeve. Vlerat ndërmjetëse ruhen deri te hapi "
            "i treguar i rrumbullakimit, prandaj aty ku shënohet pranohen dallime "
            "të vogla që vijnë nga rrumbullakimi më i hershëm."
        ),
        "fiction_notice": (
            "Të gjitha situatat, vlerat, të dhënat dhe rezultatet e programeve "
            "janë krijuar për mësim; nuk janë gjetje empirike."
        ),
    },
}


PRACTICE_STRUCTURE_LABELS = {
    "en": {
        "theory": "Part I: Theory",
        "calculator": "Part II: Calculator Practice",
        "part_label": "part",
        "reason_first": (
            "**Reason first.** Before calculating, state the relationship, rule, "
            "or expected pattern that makes the calculation appropriate."
        ),
        "theory_steps": (
            "Identify the issue",
            "Reason through the evidence",
            "State the conclusion and its limits",
        ),
        "calculator_steps": (
            "Set up the calculation",
            "Work through the calculation",
            "Interpret and check the result",
        ),
        "mixed_steps": (
            "Reason before calculating",
            "Work through the calculation",
            "Interpret and check the result",
        ),
        "single_check": (
            "Check that the conclusion answers the requested question and does not "
            "extend beyond the conditions stated in the task."
        ),
        "double_check": (
            "Read the result in context and verify that each requested part has been answered."
        ),
    },
    "de": {
        "theory": "Teil I: Theorie",
        "calculator": "Teil II: Rechnerpraxis",
        "part_label": "Teil",
        "reason_first": (
            "**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel "
            "oder das erwartete Muster, das die Berechnung begründet."
        ),
        "theory_steps": (
            "Fragestellung bestimmen",
            "Evidenz schrittweise beurteilen",
            "Schluss und Grenzen festhalten",
        ),
        "calculator_steps": (
            "Berechnung einrichten",
            "Berechnung durchführen",
            "Ergebnis interpretieren und prüfen",
        ),
        "mixed_steps": (
            "Vor dem Rechnen begründen",
            "Berechnung durchführen",
            "Ergebnis interpretieren und prüfen",
        ),
        "single_check": (
            "Prüfe, ob der Schluss die gestellte Frage beantwortet und nicht über "
            "die Bedingungen der Aufgabe hinausgeht."
        ),
        "double_check": (
            "Lies das Ergebnis im Kontext und prüfe, ob alle verlangten Teile beantwortet sind."
        ),
    },
    "sq": {
        "theory": "Pjesa I: Teoria",
        "calculator": "Pjesa II: Praktika me kalkulator",
        "part_label": "pjesa",
        "reason_first": (
            "**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose "
            "modelin e pritur që e bën llogaritjen të përshtatshme."
        ),
        "theory_steps": (
            "Përcakto çështjen",
            "Arsyeto hap pas hapi nga evidenca",
            "Jep përfundimin dhe kufijtë e tij",
        ),
        "calculator_steps": (
            "Përgatit llogaritjen",
            "Zhvillo llogaritjen",
            "Interpreto dhe kontrollo rezultatin",
        ),
        "mixed_steps": (
            "Arsyeto para llogaritjes",
            "Zhvillo llogaritjen",
            "Interpreto dhe kontrollo rezultatin",
        ),
        "single_check": (
            "Kontrollo nëse përfundimi i përgjigjet pyetjes së kërkuar dhe nuk "
            "shkon përtej kushteve të dhëna në ushtrim."
        ),
        "double_check": (
            "Lexoje rezultatin në kontekst dhe kontrollo nëse i ke dhënë përgjigje "
            "çdo pjese të kërkuar."
        ),
    },
}


def number(value: float, digits: int = 4) -> str:
    """Return the project-wide, language-independent decimal representation."""

    rounded = f"{value:.{digits}f}"
    if rounded.startswith("-0") and float(rounded) == 0:
        rounded = rounded[1:]
    return rounded


def normal_cdf(z: float) -> float:
    return NormalDist().cdf(z)


def normal_ppf(probability: float) -> float:
    if not 0 < probability < 1:
        raise ValueError("a normal quantile probability must lie strictly between 0 and 1")
    return NormalDist().inv_cdf(probability)


def _continued_beta_fraction(a: float, b: float, x: float) -> float:
    """Evaluate the continued fraction used by the incomplete beta function."""

    maximum_iterations = 240
    tolerance = 3e-14
    minimum = 1e-300
    qab = a + b
    qap = a + 1.0
    qam = a - 1.0
    c = 1.0
    d = 1.0 - qab * x / qap
    if abs(d) < minimum:
        d = minimum
    d = 1.0 / d
    value = d
    for iteration in range(1, maximum_iterations + 1):
        even_step = 2 * iteration
        coefficient = (
            iteration * (b - iteration) * x
            / ((qam + even_step) * (a + even_step))
        )
        d = 1.0 + coefficient * d
        if abs(d) < minimum:
            d = minimum
        c = 1.0 + coefficient / c
        if abs(c) < minimum:
            c = minimum
        d = 1.0 / d
        value *= d * c

        coefficient = -(
            (a + iteration) * (qab + iteration) * x
            / ((a + even_step) * (qap + even_step))
        )
        d = 1.0 + coefficient * d
        if abs(d) < minimum:
            d = minimum
        c = 1.0 + coefficient / c
        if abs(c) < minimum:
            c = minimum
        d = 1.0 / d
        change = d * c
        value *= change
        if abs(change - 1.0) <= tolerance:
            return value
    raise ArithmeticError("incomplete beta continued fraction did not converge")


def _regularized_incomplete_beta(x: float, a: float, b: float) -> float:
    if not 0.0 <= x <= 1.0 or a <= 0.0 or b <= 0.0:
        raise ValueError("invalid incomplete beta arguments")
    if x == 0.0:
        return 0.0
    if x == 1.0:
        return 1.0
    scale = math.exp(
        math.lgamma(a + b)
        - math.lgamma(a)
        - math.lgamma(b)
        + a * math.log(x)
        + b * math.log1p(-x)
    )
    if x < (a + 1.0) / (a + b + 2.0):
        return scale * _continued_beta_fraction(a, b, x) / a
    return 1.0 - scale * _continued_beta_fraction(b, a, 1.0 - x) / b


def student_t_cdf(value: float, degrees_of_freedom: int) -> float:
    """Return the cumulative probability for Student's t distribution."""

    if degrees_of_freedom < 1:
        raise ValueError("Student's t requires at least one degree of freedom")
    if not math.isfinite(value):
        return 0.0 if value < 0 else 1.0
    if value == 0.0:
        return 0.5
    beta_argument = degrees_of_freedom / (degrees_of_freedom + value * value)
    tail_area_twice = _regularized_incomplete_beta(
        beta_argument, degrees_of_freedom / 2.0, 0.5
    )
    if value > 0:
        return 1.0 - tail_area_twice / 2.0
    return tail_area_twice / 2.0


def student_t_ppf(probability: float, degrees_of_freedom: int) -> float:
    """Return a Student-t quantile using the exact CDF and bisection."""

    if not 0.0 < probability < 1.0:
        raise ValueError("a t quantile probability must lie strictly between 0 and 1")
    if degrees_of_freedom < 1:
        raise ValueError("Student's t requires at least one degree of freedom")
    if probability == 0.5:
        return 0.0
    if probability < 0.5:
        return -student_t_ppf(1.0 - probability, degrees_of_freedom)
    lower = 0.0
    upper = 1.0
    while student_t_cdf(upper, degrees_of_freedom) < probability:
        upper *= 2.0
    for _ in range(100):
        midpoint = (lower + upper) / 2.0
        if student_t_cdf(midpoint, degrees_of_freedom) < probability:
            lower = midpoint
        else:
            upper = midpoint
    return (lower + upper) / 2.0


def student_t_two_sided_p(value: float, degrees_of_freedom: int) -> float:
    """Return the exact two-sided p-value for a Student-t statistic."""

    return 2.0 * (1.0 - student_t_cdf(abs(value), degrees_of_freedom))


def f_cdf(value: float, numerator_df: float, denominator_df: float) -> float:
    """Return the cumulative probability of an F distribution."""

    if value < 0 or numerator_df <= 0 or denominator_df <= 0:
        raise ValueError("F arguments require a nonnegative value and positive degrees of freedom")
    if value == 0:
        return 0.0
    transformed = numerator_df * value / (numerator_df * value + denominator_df)
    return _regularized_incomplete_beta(
        transformed, numerator_df / 2.0, denominator_df / 2.0
    )


def f_upper_p(value: float, numerator_df: float, denominator_df: float) -> float:
    """Return the upper-tail probability of an F statistic."""

    return max(0.0, min(1.0, 1.0 - f_cdf(value, numerator_df, denominator_df)))


def sample_mean(values: list[float] | tuple[float, ...]) -> float:
    if not values:
        raise ValueError("cannot calculate a mean from an empty sequence")
    return sum(values) / len(values)


def sample_variance(values: list[float] | tuple[float, ...]) -> float:
    if len(values) < 2:
        raise ValueError("sample variance requires at least two observations")
    mean = sample_mean(values)
    return sum((value - mean) ** 2 for value in values) / (len(values) - 1)


def pearson(x: list[float] | tuple[float, ...], y: list[float] | tuple[float, ...]) -> float:
    if len(x) != len(y) or len(x) < 2:
        raise ValueError("Pearson correlation requires equal nontrivial sequences")
    x_mean = sample_mean(x)
    y_mean = sample_mean(y)
    cross = sum((a - x_mean) * (b - y_mean) for a, b in zip(x, y))
    x_ss = sum((a - x_mean) ** 2 for a in x)
    y_ss = sum((b - y_mean) ** 2 for b in y)
    if x_ss == 0 or y_ss == 0:
        raise ValueError("Pearson correlation is undefined for a constant sequence")
    return cross / math.sqrt(x_ss * y_ss)


def task_id(topic: int, group: int, variant: int) -> str:
    if topic not in TOPICS:
        raise ValueError(f"unsupported topic number: {topic}")
    if group < 1 or variant not in range(1, 11):
        raise ValueError("groups start at 1 and variants must be V01 through V10")
    return f"T{topic:02d}-A{group:02d}-V{variant:02d}"


def group_heading(group: int, title: str) -> str:
    return f"# A{group:02d}: {title}\n\n"


def task(topic: int, group: int, variant: int, title: str, body: str) -> str:
    identifier = task_id(topic, group, variant)
    return f"## {identifier}: {title}\n\n{body.strip()}\n\n"


GROUP_SECTION_RE = re.compile(
    r"(?ms)^#{1,2} A(?P<group>\d{2}): (?P<title>\S(?:[^\n]*\S)?)\n\n(?P<body>.*)\Z"
)
TASK_SECTION_RE = re.compile(
    r"(?ms)^#{2,3} (?P<task_id>T\d{2}-A\d{2}-V\d{2}): "
    r"(?P<title>\S(?:[^\n]*\S)?)\n\n(?P<body>.*?)"
    r"(?=^#{2,3} T\d{2}-A\d{2}-V\d{2}: |\Z)"
)
PART_MARKER_RE = re.compile(r"(?<!\w)\(([a-z])\)\s*")
SENTENCE_BREAK_RE = re.compile(r"(?<=[.!?])\s+(?=(?:[A-Z\"(]|\$))")


def _solution_units(body: str) -> list[str]:
    """Split prose safely enough for visible steps while keeping tables and math intact."""

    units: list[str] = []
    for block in re.split(r"\n\s*\n", body.strip()):
        block = block.strip()
        if not block:
            continue
        if block.startswith(("|", "$$", "```", "~~~")) or "\n|" in block:
            units.append(block)
            continue
        sentences = [item.strip() for item in SENTENCE_BREAK_RE.split(block) if item.strip()]
        units.extend(sentences or [block])
    return units


def _label_solution_parts(
    body: str, labels: tuple[str, str, str], part_label: str
) -> str:
    markers = list(PART_MARKER_RE.finditer(body))
    if len(markers) < 2:
        return ""
    prefix = body[: markers[0].start()].strip()
    parts: list[tuple[str, str]] = []
    for index, marker in enumerate(markers):
        stop = markers[index + 1].start() if index + 1 < len(markers) else len(body)
        parts.append((marker.group(1), body[marker.end() : stop].strip()))
    rendered: list[str] = []
    for index, (letter, content) in enumerate(parts):
        if index == 0:
            label = labels[0]
        elif index == len(parts) - 1:
            label = labels[2]
        else:
            label = labels[1]
        leading = prefix + "\n\n" if index == 0 and prefix else ""
        rendered.append(f"**{label}, {part_label} ({letter})**\n\n{leading}{content}")
    return "\n\n".join(rendered)


def _stepwise_solution_body(
    body: str, locale: str, group: PracticeGroup
) -> str:
    label_key = (
        "theory_steps"
        if group.classification == "theory"
        else "mixed_steps"
        if group.classification == "mixed"
        else "calculator_steps"
    )
    labels = PRACTICE_STRUCTURE_LABELS[locale][label_key]
    explicitly_parted = _label_solution_parts(
        body, labels, PRACTICE_STRUCTURE_LABELS[locale]["part_label"]
    )
    if explicitly_parted:
        return explicitly_parted

    units = _solution_units(body)
    if not units:
        raise ValueError(f"{group.group_id} contains an empty solution body")
    if len(units) == 1:
        return (
            f"**{labels[0]}**\n\n{units[0]}\n\n"
            f"**{labels[2]}**\n\n"
            f"{PRACTICE_STRUCTURE_LABELS[locale]['single_check']}"
        )
    if len(units) == 2:
        return (
            f"**{labels[0]}**\n\n{units[0]}\n\n"
            f"**{labels[1]}**\n\n{units[1]}\n\n"
            f"**{labels[2]}**\n\n"
            f"{PRACTICE_STRUCTURE_LABELS[locale]['double_check']}"
        )

    first_cut = max(1, len(units) // 3)
    second_cut = max(first_cut + 1, (2 * len(units)) // 3)
    second_cut = min(second_cut, len(units) - 1)
    chunks = (
        "\n\n".join(units[:first_cut]),
        "\n\n".join(units[first_cut:second_cut]),
        "\n\n".join(units[second_cut:]),
    )
    return "\n\n".join(
        f"**{label}**\n\n{chunk}" for label, chunk in zip(labels, chunks)
    )


def _format_group_section(
    raw_section: str,
    *,
    topic: int,
    locale: str,
    document_type: str,
) -> tuple[int, str]:
    match = GROUP_SECTION_RE.fullmatch(raw_section.strip() + "\n")
    if match is None:
        match = GROUP_SECTION_RE.fullmatch(raw_section.strip())
    if match is None:
        raise ValueError("a generated practice group does not follow the group contract")
    group_number = int(match.group("group"))
    group_id = f"T{topic:02d}-A{group_number:02d}"
    metadata = PRACTICE_GROUP_BY_ID.get(group_id)
    if metadata is None:
        raise ValueError(f"{group_id} is absent from the authoritative worksheet map")
    rendered_tasks: list[str] = []
    tasks = list(TASK_SECTION_RE.finditer(match.group("body")))
    if len(tasks) != 10:
        raise ValueError(f"{group_id} must contain exactly ten task variants")
    for task_match in tasks:
        body = task_match.group("body").strip()
        if document_type == "exercises" and metadata.conceptual_first:
            reason_first = PRACTICE_STRUCTURE_LABELS[locale]["reason_first"]
            if not body.startswith(reason_first):
                body = reason_first + "\n\n" + body
        elif document_type == "solutions":
            part_label = PRACTICE_STRUCTURE_LABELS[locale]["part_label"]
            if part_label != "part":
                body = body.replace(", part (", f", {part_label} (")
            first_step = PRACTICE_STRUCTURE_LABELS[locale][
                "theory_steps"
                if metadata.classification == "theory"
                else "mixed_steps"
                if metadata.classification == "mixed"
                else "calculator_steps"
            ][0]
            if not body.startswith(f"**{first_step}"):
                body = _stepwise_solution_body(body, locale, metadata)
        rendered_tasks.append(
            f"### {task_match.group('task_id')}: {task_match.group('title')}\n\n{body}\n\n"
        )
    return group_number, (
        f"## A{group_number:02d}: {match.group('title')}\n\n"
        + "".join(rendered_tasks)
    )


def _assemble_practice_body(
    topic: int,
    locale: str,
    document_type: str,
    raw_sections: list[str],
) -> str:
    by_group: dict[int, str] = {}
    for raw_section in raw_sections:
        group_number, formatted = _format_group_section(
            raw_section,
            topic=topic,
            locale=locale,
            document_type=document_type,
        )
        if group_number in by_group:
            raise ValueError(f"duplicate generated group A{group_number:02d}")
        by_group[group_number] = formatted

    metadata = practice_groups_for_topic(topic)
    expected_groups = {item.group for item in metadata}
    if set(by_group) != expected_groups:
        raise ValueError(f"Topic {topic} generated groups do not match the worksheet map")
    labels = PRACTICE_STRUCTURE_LABELS[locale]
    parts: list[str] = []
    for section in ("theory", "calculator"):
        parts.append(f"# {labels[section]}\n\n")
        parts.extend(by_group[item.group] for item in metadata if item.section == section)
    return "".join(parts)


def document_header(topic: int, locale: str, document_type: str) -> str:
    if locale not in DOCUMENT_LABELS:
        raise ValueError(f"unsupported locale: {locale}")
    if document_type not in ("exercises", "solutions"):
        raise ValueError(f"unsupported document type: {document_type}")
    metadata = TOPICS[topic]
    pair = "solutions" if document_type == "exercises" else "exercises"
    document_id = (
        f"topic-{metadata.number:02d}-{metadata.slug}-{document_type}-{locale}"
    )
    paired_id = f"topic-{metadata.number:02d}-{metadata.slug}-{pair}-{locale}"
    return f'''---
title: "{DOCUMENT_LABELS[locale][document_type]}"
subtitle: "{metadata.titles[locale]}"
document-id: "{document_id}"
topic-id: "topic-{metadata.number:02d}-{metadata.slug}"
topic-number: "{metadata.number:02d}"
topic-slug: "{metadata.slug}"
document-type: "{document_type}"
locale: "{locale}"
paired-document-id: "{paired_id}"
---

'''


def document_intro(locale: str, document_type: str, groups: int) -> str:
    if groups < 1:
        raise ValueError("a published practice document needs at least one group")
    key = "exercise_intro" if document_type == "exercises" else "solution_intro"
    introduction = DOCUMENT_LABELS[locale][key].format(
        groups=groups, tasks=groups * 10
    )
    return introduction + " " + DOCUMENT_LABELS[locale]["fiction_notice"] + "\n\n"


def source_path(topic: int, locale: str, document_type: str) -> Path:
    metadata = TOPICS[topic]
    return SOURCE_ROOT / locale / (
        f"topic-{metadata.number:02d}-{metadata.slug}-{document_type}-{locale}.md"
    )


def _absolute(path: Path) -> Path:
    return Path(os.path.abspath(os.fspath(path)))


def _reject_output_symlinks(path: Path) -> None:
    root = _absolute(ROOT)
    target = _absolute(path)
    try:
        relative = target.relative_to(root)
    except ValueError as exc:
        raise RuntimeError(f"refusing to write outside the project: {target}") from exc
    if root.is_symlink():
        raise RuntimeError(f"project root must not be a symlink: {root}")
    current = root
    for part in relative.parts:
        current = current / part
        if os.path.lexists(current) and current.is_symlink():
            raise RuntimeError(f"refusing to write through a symlink: {current}")


def _stage_text(path: Path, text: str, label: str) -> Path:
    _reject_output_symlinks(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    _reject_output_symlinks(path.parent)
    with tempfile.NamedTemporaryFile(
        mode="w",
        encoding="utf-8",
        newline="\n",
        prefix=f".{path.name}.{label}.",
        suffix=".tmp",
        dir=path.parent,
        delete=False,
    ) as handle:
        handle.write(text.rstrip() + "\n")
        handle.flush()
        os.fsync(handle.fileno())
        return Path(handle.name)


def _stage_backup(path: Path) -> Path | None:
    if not path.exists():
        return None
    _reject_output_symlinks(path)
    with tempfile.NamedTemporaryFile(
        mode="wb",
        prefix=f".{path.name}.backup.",
        suffix=".tmp",
        dir=path.parent,
        delete=False,
    ) as handle:
        backup = Path(handle.name)
        with path.open("rb") as source:
            shutil.copyfileobj(source, handle)
        handle.flush()
        os.fsync(handle.fileno())
    return backup


def _validate_assembled_pair(
    topic: int,
    locale: str,
    groups: int,
    exercise_text: str,
    solution_text: str,
) -> None:
    from download_documents import (
        ProjectPaths,
        discover_sources,
        parse_task_structure,
        validate_body_resources,
        validate_project_tree,
        validate_source_set,
    )

    mapped_groups = practice_groups_for_topic(topic)
    if len(mapped_groups) != groups:
        raise ValueError(f"Topic {topic} group count differs from the worksheet map")
    expected_ids = tuple(
        task_id(topic, metadata.group, variant)
        for metadata in mapped_groups
        for variant in range(1, 11)
    )
    expected_groups = [f"{metadata.group:02d}" for metadata in mapped_groups]
    expected_parts = [
        PRACTICE_STRUCTURE_LABELS[locale]["theory"],
        PRACTICE_STRUCTURE_LABELS[locale]["calculator"],
    ]
    prospective_numeric: dict[str, dict[str, tuple[str, ...]]] = {}
    for document_type, assembled in (
        ("exercises", exercise_text),
        ("solutions", solution_text),
    ):
        diagnostic_path = ROOT / f".{document_type}-validation.md"
        validate_body_resources(assembled, diagnostic_path)
        identifiers, numeric = parse_task_structure(assembled, diagnostic_path)
        if identifiers != expected_ids:
            raise ValueError(
                f"{document_type} must contain exactly the expected stable task IDs"
            )
        headings = re.findall(r"^## A(\d{2}):\s+\S.*$", assembled, re.MULTILINE)
        if headings != expected_groups:
            raise ValueError(
                f"{document_type} must contain exactly one ordered heading per group"
            )
        parts = re.findall(r"^# (Part .+|Teil .+|Pjesa .+)$", assembled, re.MULTILINE)
        if parts != expected_parts:
            raise ValueError(
                f"{document_type} must contain the two localized top-level practice parts"
            )
        if "\u2014" in assembled:
            raise ValueError(f"{document_type} contains a prohibited em dash")
        if locale != "en" and ", part (" in assembled:
            raise ValueError(
                f"{document_type} contains an unlocalized English part label"
            )
        if locale == "de" and "ß" in assembled:
            raise ValueError(
                f"{document_type} contains ß instead of Swiss German ss"
            )
        if document_type == "solutions":
            labels = PRACTICE_STRUCTURE_LABELS[locale]
            all_step_labels = {
                label
                for key in ("theory_steps", "calculator_steps", "mixed_steps")
                for label in labels[key]
            }
            for identifier in expected_ids:
                heading_match = re.search(
                    rf"(?ms)^### {re.escape(identifier)}: .+?\n\n(?P<body>.*?)"
                    rf"(?=^### T\d{{2}}-A\d{{2}}-V\d{{2}}: |^## A\d{{2}}: |^# |\Z)",
                    assembled,
                )
                if heading_match is None:
                    raise ValueError(f"missing solution task {identifier}")
                visible_labels = sum(
                    f"**{label}" in heading_match.group("body")
                    for label in all_step_labels
                )
                if visible_labels < 2:
                    raise ValueError(
                        f"solution task {identifier} needs at least two visible step labels"
                    )
        prospective_numeric[document_type] = dict(numeric)

    paths = ProjectPaths.from_script(Path(__file__))
    validate_project_tree(paths)
    allowed_locales = {"en"}
    if locale == "sq":
        allowed_locales.add("de")
    topic_metadata = TOPICS[topic]
    documents = [
        document
        for document in discover_sources(paths.source_root)
        if document.locale in allowed_locales
        and not (
            document.locale == locale
            and document.number == f"{topic:02d}"
            and document.slug == topic_metadata.slug
        )
    ]
    validate_source_set(documents, require_complete_locales=False)
    for document in documents:
        if (
            document.number != f"{topic:02d}"
            or document.slug != topic_metadata.slug
            or document.locale == locale
        ):
            continue
        if locale == "en":
            continue
        if document.locale != "en":
            continue
        if document.task_ids != expected_ids:
            raise ValueError(
                f"prospective {locale} IDs do not match existing "
                f"{document.locale} {document.document_type} IDs"
            )
        expected_numeric = prospective_numeric[document.document_type]
        actual_numeric = document.numeric_tokens_by_task
        for identifier in expected_ids:
            if expected_numeric[identifier] != actual_numeric[identifier]:
                raise ValueError(
                    f"prospective {locale} numeric tokens differ from existing "
                    f"{document.locale} {document.document_type} task {identifier}"
                )


def write_pair(
    topic: int,
    locale: str,
    groups: int,
    exercise_sections: list[str],
    solution_sections: list[str],
) -> tuple[Path, Path]:
    """Write one complete paired source set after basic generator checks."""

    validate_registered_raw_sources()
    if len(exercise_sections) != groups or len(solution_sections) != groups:
        raise ValueError("one exercise and solution section is required per group")
    exercise_text = (
        document_header(topic, locale, "exercises")
        + document_intro(locale, "exercises", groups)
        + _assemble_practice_body(
            topic, locale, "exercises", exercise_sections
        )
    )
    solution_text = (
        document_header(topic, locale, "solutions")
        + document_intro(locale, "solutions", groups)
        + _assemble_practice_body(
            topic, locale, "solutions", solution_sections
        )
    )
    _validate_assembled_pair(topic, locale, groups, exercise_text, solution_text)
    exercise_path = source_path(topic, locale, "exercises")
    solution_path = source_path(topic, locale, "solutions")
    paths_and_text = (
        (exercise_path, exercise_text),
        (solution_path, solution_text),
    )
    staged: dict[Path, Path] = {}
    backups: dict[Path, Path | None] = {}
    replaced: list[Path] = []
    retained_backups: set[Path] = set()
    try:
        for path, assembled in paths_and_text:
            staged[path] = _stage_text(path, assembled, "staged")
        for path, _assembled in paths_and_text:
            backups[path] = _stage_backup(path)
        for path, _assembled in paths_and_text:
            _reject_output_symlinks(path)
            os.replace(staged[path], path)
            del staged[path]
            replaced.append(path)
    except BaseException as original_error:
        rollback_errors: list[str] = []
        for path in reversed(replaced):
            backup = backups.get(path)
            try:
                if backup is None:
                    path.unlink(missing_ok=True)
                else:
                    os.replace(backup, path)
                    backups[path] = None
            except BaseException as rollback_error:
                if backup is not None:
                    retained_backups.add(backup)
                rollback_errors.append(
                    f"{path} (recovery copy {backup}): {rollback_error}"
                )
        if rollback_errors:
            raise RuntimeError(
                "paired write failed and rollback was incomplete; retained backup(s): "
                + "; ".join(rollback_errors)
            ) from original_error
        raise
    finally:
        for temporary in staged.values():
            temporary.unlink(missing_ok=True)
        for backup in backups.values():
            if backup is not None and backup not in retained_backups:
                backup.unlink(missing_ok=True)
    return exercise_path, solution_path


def validate_sources_allowing_incomplete_locales(
    locale: str, topic: int | None = None
) -> None:
    """Validate one progressive topic pass or the complete progressive corpus."""

    from download_documents import (
        ProjectPaths,
        discover_sources,
        validate_project_tree,
        validate_source_set,
    )

    paths = ProjectPaths.from_script(Path(__file__))
    validate_project_tree(paths)
    allowed_locales = {"en"}
    if locale in {"de", "sq"}:
        allowed_locales.add("de")
    if locale == "sq":
        allowed_locales.add("sq")
    documents = [
        document
        for document in discover_sources(paths.source_root)
        if document.locale in allowed_locales
        and (topic is None or document.number == f"{topic:02d}")
    ]
    validate_source_set(documents, require_complete_locales=False)


def validate_existing_practice_structure(locale: str) -> None:
    """Validate all eight existing practice pairs through one locale phase."""

    from download_documents import DocumentError

    if locale not in DOCUMENT_LABELS:
        raise DocumentError(f"unsupported locale: {locale}")
    try:
        for topic, groups in EXPECTED_GROUP_COUNTS.items():
            exercise_text = source_path(topic, locale, "exercises").read_text(
                encoding="utf-8"
            )
            solution_text = source_path(topic, locale, "solutions").read_text(
                encoding="utf-8"
            )
            _validate_assembled_pair(
                topic,
                locale,
                groups,
                exercise_text,
                solution_text,
            )
    except DocumentError:
        raise
    except (OSError, RuntimeError, ValueError) as exc:
        raise DocumentError(
            f"{locale} Introduction to Statistics practice structure failed: {exc}"
        ) from exc
