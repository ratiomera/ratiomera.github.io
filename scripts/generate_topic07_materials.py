#!/usr/bin/env python3
"""Generate Ratiomera's multilingual Topic 7 practice pairs.

The nine groups follow the registered Topic 7 worksheet-objective map. Every
setting, value, table, output, question, and worked solution is newly authored
teaching material. English remains canonical; German and Albanian reuse its
calculations, stable task identifiers, formulas, and table geometry.
"""

from __future__ import annotations

import argparse
import math
import re
import sys

from intro_stats_practice_support import (
    group_heading,
    number,
    student_t_two_sided_p,
    task,
    task_id,
    validate_sources_allowing_incomplete_locales,
    write_pair,
)


CONTEXTS = [
    {
        "title": "Guided practice and reasoning",
        "outcome": "reasoning score",
        "outcome_unit": "points",
        "x1": "guided-practice hours",
        "x2": "prior-preparation score",
        "x3": "reflection-session count",
    },
    {
        "title": "Archive workflow and retrieval time",
        "outcome": "retrieval time",
        "outcome_unit": "minutes",
        "x1": "checklist-practice sessions",
        "x2": "archive-experience months",
        "x3": "catalog-familiarity score",
    },
    {
        "title": "Reading routines and comprehension",
        "outcome": "comprehension score",
        "outcome_unit": "points",
        "x1": "weekly reading hours",
        "x2": "baseline-vocabulary score",
        "x3": "annotation-session count",
    },
    {
        "title": "Route rehearsal and navigation time",
        "outcome": "navigation time",
        "outcome_unit": "minutes",
        "x1": "route-rehearsal attempts",
        "x2": "route-familiarity score",
        "x3": "landmark-recall score",
    },
    {
        "title": "Search practice and catalog accuracy",
        "outcome": "catalog-accuracy score",
        "outcome_unit": "points",
        "x1": "search-practice sets",
        "x2": "prior catalog-knowledge score",
        "x3": "query-planning score",
    },
    {
        "title": "Workshop participation and confidence",
        "outcome": "confidence score",
        "outcome_unit": "points",
        "x1": "workshop sessions",
        "x2": "baseline-confidence score",
        "x3": "reflection-log count",
    },
    {
        "title": "Focus blocks and task accuracy",
        "outcome": "task-accuracy score",
        "outcome_unit": "points",
        "x1": "notification-free blocks",
        "x2": "sleep duration in hours",
        "x3": "planning-break count",
    },
    {
        "title": "Museum engagement and historical knowledge",
        "outcome": "historical-knowledge score",
        "outcome_unit": "points",
        "x1": "museum visits",
        "x2": "prior-history score",
        "x3": "exhibit-note count",
    },
    {
        "title": "Peer feedback and revision quality",
        "outcome": "revision-quality score",
        "outcome_unit": "points",
        "x1": "peer-feedback rounds",
        "x2": "baseline-writing score",
        "x3": "revision-plan score",
    },
    {
        "title": "Planning sessions and completion time",
        "outcome": "completion time",
        "outcome_unit": "minutes",
        "x1": "planning sessions",
        "x2": "task-complexity score",
        "x3": "progress-check count",
    },
]


# n, intercept, unstandardized slopes, three correlations, and residual standard
# error. Standardized slopes, R-squared, and coefficient SEs are calculated.
A01_CASES = [
    (80, 38.0, 2.40, 0.31, 0.55, 0.48, 0.45, 5.6),
    (72, 70.0, -1.75, -0.22, -0.51, -0.42, 0.40, 4.8),
    (95, 42.0, 1.85, 0.28, 0.49, 0.44, 0.35, 5.1),
    (68, 65.0, -2.10, -0.16, -0.53, -0.39, 0.38, 6.0),
    (110, 48.0, 1.55, 0.34, 0.46, 0.43, 0.42, 4.6),
    (76, 30.0, 2.20, 0.45, 0.50, 0.47, 0.30, 5.0),
    (120, 55.0, 1.30, 1.15, 0.41, 0.38, 0.28, 4.3),
    (84, 40.0, 2.65, 0.37, 0.52, 0.45, 0.36, 5.5),
    (92, 44.0, 2.10, 0.30, 0.48, 0.40, 0.33, 4.9),
    (88, 82.0, -1.90, 0.85, -0.45, 0.42, -0.05, 5.7),
]


# n, total sum of squares, and R-squared for one-, two-, and three-predictor models.
A02_CASES = [
    (70, 1840.0, 0.220, 0.370, 0.390),
    (80, 1320.0, 0.280, 0.350, 0.351),
    (60, 1560.0, 0.180, 0.310, 0.360),
    (90, 2100.0, 0.250, 0.330, 0.334),
    (100, 1750.0, 0.300, 0.410, 0.440),
    (55, 980.0, 0.160, 0.290, 0.292),
    (120, 2280.0, 0.210, 0.340, 0.370),
    (75, 1440.0, 0.240, 0.320, 0.321),
    (65, 1620.0, 0.190, 0.360, 0.420),
    (110, 1960.0, 0.270, 0.390, 0.395),
]


# n, R-squared, 5% F critical value, and three coefficient (estimate, SE) pairs.
A03_CASES = [
    (50, 0.220, 2.80684, ((1.80, 0.60), (0.22, 0.18), (0.12, 0.16))),
    (60, 0.300, 2.76943, ((-1.40, 0.45), (-0.20, 0.16), (0.30, 0.12))),
    (70, 0.100, 2.74371, ((1.10, 0.58), (0.18, 0.13), (-0.15, 0.14))),
    (80, 0.250, 2.72494, ((-1.80, 0.55), (-0.12, 0.10), (0.28, 0.11))),
    (90, 0.080, 2.71065, ((1.00, 0.57), (0.15, 0.12), (0.18, 0.14))),
    (100, 0.350, 2.69939, ((2.10, 0.50), (0.38, 0.14), (-0.10, 0.13))),
    (110, 0.200, 2.69030, ((1.30, 0.40), (0.12, 0.11), (0.25, 0.15))),
    (120, 0.280, 2.68281, ((2.00, 0.48), (0.31, 0.13), (0.08, 0.12))),
    (75, 0.160, 2.73365, ((1.20, 0.52), (0.19, 0.15), (-0.09, 0.13))),
    (65, 0.240, 2.75548, ((-1.60, 0.50), (0.42, 0.17), (0.16, 0.14))),
]


CANDIDATE_NAMES = [
    ("reflection sessions", "study-partner meetings", "planning checks"),
    ("catalog familiarity", "desk-map use", "mentor consultations"),
    ("annotation sessions", "discussion posts", "quiet-reading blocks"),
    ("landmark recall", "map checks", "route previews"),
    ("query planning", "keyword rehearsals", "catalog hints used"),
    ("reflection logs", "peer meetings", "practice demonstrations"),
    ("planning breaks", "screen-free intervals", "task previews"),
    ("exhibit notes", "guided-tour stops", "follow-up readings"),
    ("revision planning", "peer comments used", "editing passes"),
    ("progress checks", "calendar reminders", "task previews"),
]


# Current-model R-squared and correlations between each residualized candidate
# predictor and the original outcome. Their squares are incremental R-squared.
A04_CASES = [
    (0.300, (0.24, 0.10, -0.18)),
    (0.260, (-0.12, -0.27, 0.08)),
    (0.340, (0.15, 0.31, 0.20)),
    (0.290, (-0.28, -0.14, 0.19)),
    (0.370, (0.11, 0.22, 0.29)),
    (0.320, (0.26, 0.17, -0.09)),
    (0.250, (0.13, 0.21, 0.07)),
    (0.310, (0.18, 0.12, 0.25)),
    (0.360, (0.09, 0.28, 0.16)),
    (0.280, (-0.23, -0.11, 0.20)),
]


# Log likelihoods for M1 through M4. K is 3, 4, 5, and 6 respectively.
A05_CASES = [
    (-155.0, -146.0, -142.5, -141.9),
    (-142.0, -134.0, -133.4, -131.8),
    (-180.0, -170.0, -166.0, -165.5),
    (-130.0, -126.0, -125.5, -125.2),
    (-200.0, -188.0, -183.0, -180.0),
    (-165.0, -157.0, -156.4, -155.8),
    (-175.0, -166.0, -162.0, -161.2),
    (-145.0, -140.0, -138.0, -136.4),
    (-190.0, -181.0, -180.3, -179.9),
    (-158.0, -149.0, -145.0, -144.4),
]


# Setting, outcome, category labels (first is reference), intercept, and dummy effects.
A06_CASES = [
    ("Tutorial format", "reasoning score", ("Text", "Video", "Interactive"), 61.0, (3.5, 6.0)),
    ("Study location", "focus score", ("Home", "Library", "Study room", "Outdoors"), 54.0, (4.0, 2.5, -1.5)),
    ("Feedback channel", "revision score", ("Written", "Audio", "Video"), 66.0, (2.0, 4.5)),
    ("Note-taking method", "recall score", ("Paper", "Tablet", "Laptop", "Mixed"), 58.0, (-1.5, -2.5, 3.0)),
    ("Workshop schedule", "confidence score", ("Morning", "Afternoon", "Evening"), 49.0, (2.5, -3.0)),
    ("Archive guide", "retrieval score", ("Checklist", "Map", "Mentor", "Search tool"), 63.0, (1.5, 5.0, 3.0)),
    ("Revision strategy", "quality score", ("Self-review", "Peer review", "Instructor review"), 60.0, (4.0, 7.0)),
    ("Museum route", "knowledge score", ("Chronological", "Thematic", "Free choice", "Guided", "Hybrid"), 57.0, (3.0, -1.0, 5.5, 4.0)),
    ("Study plan", "retention score", ("Daily", "Twice weekly", "Weekly"), 69.0, (-2.0, -5.0)),
    ("Task interface", "completion score", ("List", "Board", "Calendar", "Timeline"), 62.0, (2.5, 4.0, 1.0)),
]


# Title, outcome, quantitative predictor, reference group, comparison group,
# intercept, common slope, group difference, and two predictor coordinates.
A07_CASES = [
    ("Tutorial support and reasoning", "reasoning score", "practice hours", "Self-guided", "Tutored", 42.0, 3.0, 5.0, 2.0, 6.0),
    ("Archive experience and retrieval", "retrieval time", "practice sessions", "New staff", "Experienced staff", 36.0, -1.8, -4.0, 1.0, 5.0),
    ("Reading format and comprehension", "comprehension score", "reading hours", "Print", "Digital", 51.0, 2.2, -2.5, 2.0, 7.0),
    ("Route aid and navigation", "navigation time", "rehearsal attempts", "Paper map", "App map", 44.0, -2.0, -3.0, 1.0, 4.0),
    ("Search guide and accuracy", "accuracy score", "practice sets", "No guide", "Checklist", 55.0, 2.5, 4.0, 0.0, 4.0),
    ("Workshop mode and confidence", "confidence score", "sessions attended", "Online", "In person", 38.0, 3.2, 3.5, 1.0, 5.0),
    ("Focus setting and accuracy", "task-accuracy score", "focus blocks", "Shared room", "Quiet room", 60.0, 1.7, 4.5, 2.0, 8.0),
    ("Museum guide and knowledge", "knowledge score", "visits", "Self-guided", "Guided", 47.0, 4.0, 6.0, 0.0, 3.0),
    ("Feedback mode and revision", "revision score", "feedback rounds", "Written", "Conversation", 52.0, 3.5, 2.0, 1.0, 4.0),
    ("Planning format and completion", "completion time", "planning sessions", "Paper", "Digital", 70.0, -2.4, -3.5, 1.0, 6.0),
]


# The same structure as A07, but each case is a separate releveling exercise.
A08_CASES = [
    ("Practice format releveling", "reasoning score", "practice hours", "Independent", "Partnered", 40.0, 2.8, 4.5, 1.0, 5.0),
    ("Archive role releveling", "retrieval time", "practice sessions", "Assistant", "Coordinator", 35.0, -1.6, -5.0, 0.0, 4.0),
    ("Reading medium releveling", "comprehension score", "reading hours", "Print", "Audio", 50.0, 2.0, -3.0, 2.0, 6.0),
    ("Navigation display releveling", "navigation time", "rehearsal attempts", "Static", "Interactive", 46.0, -2.2, -4.0, 1.0, 5.0),
    ("Catalog aid releveling", "accuracy score", "practice sets", "Index", "Search bar", 53.0, 2.6, 3.0, 0.0, 3.0),
    ("Workshop setting releveling", "confidence score", "sessions", "Remote", "Classroom", 37.0, 3.0, 5.0, 1.0, 4.0),
    ("Focus room releveling", "task-accuracy score", "focus blocks", "Open room", "Private room", 59.0, 1.8, 4.0, 2.0, 7.0),
    ("Museum route releveling", "knowledge score", "visits", "Free route", "Curated route", 45.0, 4.2, 6.5, 0.0, 3.0),
    ("Revision meeting releveling", "revision score", "feedback rounds", "Asynchronous", "Live", 51.0, 3.4, 2.5, 1.0, 5.0),
    ("Planning tool releveling", "completion time", "planning sessions", "Notebook", "Calendar", 72.0, -2.5, -4.0, 1.0, 6.0),
]


# Title, outcome, X, reference group, comparison group, b0, b1, b2, b3,
# and two X coordinates for an interaction model.
A09_CASES = [
    ("Practice hours by tutorial support", "reasoning score", "practice hours", "Self-guided", "Tutored", 40.0, 2.0, 4.0, 1.2, 1.0, 5.0),
    ("Practice sessions by archive role", "retrieval time", "practice sessions", "New staff", "Experienced staff", 38.0, -1.2, -3.0, -0.8, 0.0, 4.0),
    ("Reading hours by medium", "comprehension score", "reading hours", "Print", "Audio", 49.0, 2.6, 2.0, -1.0, 2.0, 6.0),
    ("Rehearsal by navigation display", "navigation time", "rehearsal attempts", "Static", "Interactive", 48.0, -1.5, -2.0, -0.9, 1.0, 5.0),
    ("Practice sets by catalog aid", "accuracy score", "practice sets", "Index", "Search bar", 52.0, 2.0, 3.0, 0.7, 0.0, 4.0),
    ("Sessions by workshop setting", "confidence score", "sessions", "Remote", "Classroom", 36.0, 2.4, 5.0, 0.8, 1.0, 5.0),
    ("Focus blocks by room type", "task-accuracy score", "focus blocks", "Open room", "Private room", 58.0, 2.1, 4.0, -0.6, 2.0, 7.0),
    ("Visits by museum route", "knowledge score", "visits", "Free route", "Curated route", 44.0, 3.5, 3.0, 1.5, 0.0, 3.0),
    ("Feedback rounds by meeting mode", "revision score", "feedback rounds", "Asynchronous", "Live", 50.0, 2.8, 4.0, -0.5, 1.0, 5.0),
    ("Planning by tool type", "completion time", "planning sessions", "Notebook", "Calendar", 74.0, -1.8, -2.0, -0.9, 1.0, 6.0),
]


GROUP_TITLES = (
    "Reading a Multiple-Regression Equation and Output",
    "Comparing a Prespecified Nested Model Sequence",
    "Distinguishing the Global F Test From Coefficient t Tests",
    "Semipartial Correlation and Incremental R-Squared",
    "Comparing Prespecified Candidate Models With AIC",
    "Constructing Dummy Indicators and Finding the Reference",
    "Interpreting an Additive Group Model",
    "Releveling Without Changing Fitted Relationships",
    "Interpreting a Group-by-Quantitative-Predictor Interaction",
)


def markdown_table(headers: tuple[str, ...], rows: list[tuple[object, ...]]) -> str:
    """Return a compact Markdown table with text-safe cell values."""

    if not rows or any(len(row) != len(headers) for row in rows):
        raise ValueError("a Markdown table needs nonempty rows matching its headers")
    header = "| " + " | ".join(headers) + " |"
    rule = "| " + " | ".join("---" for _ in headers) + " |"
    body = ["| " + " | ".join(str(cell) for cell in row) + " |" for row in rows]
    return "\n".join((header, rule, *body))


def adjusted_r_squared(r_squared: float, n: int, predictors: int) -> float:
    return 1.0 - (1.0 - r_squared) * (n - 1) / (n - predictors - 1)


def standardized_two_predictor_output(
    r_y1: float, r_y2: float, r_12: float
) -> tuple[float, float, float]:
    denominator = 1.0 - r_12 * r_12
    beta_1 = (r_y1 - r_y2 * r_12) / denominator
    beta_2 = (r_y2 - r_y1 * r_12) / denominator
    r_squared = beta_1 * r_y1 + beta_2 * r_y2
    return beta_1, beta_2, r_squared


def two_predictor_output(
    n: int,
    b1: float,
    b2: float,
    r_y1: float,
    r_y2: float,
    r_12: float,
) -> tuple[float, float, float, float, float]:
    """Return mutually consistent standardized slopes, fit, and raw-scale SEs."""

    beta1, beta2, r_squared = standardized_two_predictor_output(r_y1, r_y2, r_12)
    standardized_se = math.sqrt(
        (1.0 - r_squared) / ((n - 3) * (1.0 - r_12 * r_12))
    )
    if beta1 == 0 or beta2 == 0:
        raise ValueError("A01 requires nonzero standardized slopes")
    se1 = abs(b1 / beta1) * standardized_se
    se2 = abs(b2 / beta2) * standardized_se
    return beta1, beta2, r_squared, se1, se2


def global_f(r_squared: float, n: int, predictors: int) -> float:
    return (r_squared / predictors) / (
        (1.0 - r_squared) / (n - predictors - 1)
    )


def p_text(p_value: float) -> str:
    if p_value < 0.0001:
        return "< 0.0001"
    return f"= {number(p_value, 4)}"


def decision_text(p_value: float) -> str:
    return "reject the coefficient null" if p_value < 0.05 else "do not reject the coefficient null"


def fitted(b0: float, b1: float, b2: float, b3: float, x: float, group: int) -> float:
    return b0 + b1 * x + b2 * group + b3 * x * group


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def _validate_case_data() -> None:
    """Assert feasibility and exact formula relationships before rendering."""

    case_sets = (
        A01_CASES,
        A02_CASES,
        A03_CASES,
        A04_CASES,
        A05_CASES,
        A06_CASES,
        A07_CASES,
        A08_CASES,
        A09_CASES,
    )
    _require(len(CONTEXTS) == 10, "Topic 7 needs ten base contexts")
    _require(all(len(cases) == 10 for cases in case_sets), "each group needs ten cases")

    for index, case in enumerate(A01_CASES, 1):
        n, _b0, b1, b2, r_y1, r_y2, r_12, rse = case
        determinant = 1.0 + 2.0 * r_y1 * r_y2 * r_12 - r_y1**2 - r_y2**2 - r_12**2
        beta1, beta2, r2, se1, se2 = two_predictor_output(
            n, b1, b2, r_y1, r_y2, r_12
        )
        standardized_se = math.sqrt(
            (1.0 - r2) / ((n - 3) * (1.0 - r_12 * r_12))
        )
        _require(n > 3 and se1 > 0 and se2 > 0 and rse > 0, f"A01 V{index:02d} has invalid scales")
        _require(determinant > 0, f"A01 V{index:02d} has an impossible correlation matrix")
        _require(b1 * beta1 > 0 and b2 * beta2 > 0, f"A01 V{index:02d} raw and standardized signs differ")
        _require(0 < r2 < 1, f"A01 V{index:02d} has invalid R-squared")
        _require(abs(r2 - (beta1 * r_y1 + beta2 * r_y2)) < 1e-12, f"A01 V{index:02d} beta formula failed")
        _require(abs(b1 / se1 - beta1 / standardized_se) < 1e-12, f"A01 V{index:02d} first t statistic is inconsistent")
        _require(abs(b2 / se2 - beta2 / standardized_se) < 1e-12, f"A01 V{index:02d} second t statistic is inconsistent")
        _require(adjusted_r_squared(r2, n, 2) < r2, f"A01 V{index:02d} adjusted R-squared must be smaller")

    saw_adjusted_increase = False
    saw_adjusted_decrease = False
    for index, (n, sst, r1, r2, r3) in enumerate(A02_CASES, 1):
        _require(n > 4 and sst > 0, f"A02 V{index:02d} has invalid n or SST")
        _require(0 <= r1 <= r2 <= r3 < 1, f"A02 V{index:02d} violates nested R-squared monotonicity")
        adjusted = [adjusted_r_squared(r, n, p) for p, r in enumerate((r1, r2, r3), 1)]
        saw_adjusted_increase |= adjusted[2] > adjusted[1]
        saw_adjusted_decrease |= adjusted[2] < adjusted[1]
        _require(all(0 < value < 1 for value in adjusted), f"A02 V{index:02d} has invalid adjusted R-squared")
        _require(all(abs(sst * (1.0 - r)) > 0 for r in (r1, r2, r3)), f"A02 V{index:02d} has invalid SSE")
    _require(saw_adjusted_increase and saw_adjusted_decrease, "A02 must illustrate both adjusted-fit outcomes")

    saw_global_reject = False
    saw_global_retain = False
    for index, (n, r2, critical, coefficients) in enumerate(A03_CASES, 1):
        f_value = global_f(r2, n, 3)
        saw_global_reject |= f_value > critical
        saw_global_retain |= f_value <= critical
        _require(n > 4 and 0 < r2 < 1 and critical > 0, f"A03 V{index:02d} has invalid model values")
        for estimate, se in coefficients:
            t_value = estimate / se
            p_value = student_t_two_sided_p(estimate / se, n - 4)
            _require(se > 0 and 0 <= p_value <= 1, f"A03 V{index:02d} has invalid coefficient inference")
            implied_increment = t_value * t_value * (1.0 - r2) / (n - 4)
            _require(implied_increment <= r2, f"A03 V{index:02d} coefficient test exceeds total fit")
    _require(saw_global_reject and saw_global_retain, "A03 must include both global decisions")

    for index, (base_r2, semipartials) in enumerate(A04_CASES, 1):
        increments = [value * value for value in semipartials]
        _require(0 < base_r2 < 1 and max(increments) + base_r2 < 1, f"A04 V{index:02d} has infeasible R-squared")
        _require(len(set(increments)) == 3, f"A04 V{index:02d} needs a unique forward candidate")

    k_values = (3, 4, 5, 6)
    for index, log_likelihoods in enumerate(A05_CASES, 1):
        _require(all(a <= b for a, b in zip(log_likelihoods, log_likelihoods[1:])), f"A05 V{index:02d} violates nested likelihood monotonicity")
        aics = [-2.0 * log_likelihood + 2.0 * k for log_likelihood, k in zip(log_likelihoods, k_values)]
        minimum = min(aics)
        _require(sum(abs(value - minimum) < 1e-10 for value in aics) == 1, f"A05 V{index:02d} needs one lowest AIC")
        _require(all(abs(aic - (-2.0 * ll + 2.0 * k)) < 1e-12 for aic, ll, k in zip(aics, log_likelihoods, k_values)), f"A05 V{index:02d} AIC formula failed")

    for index, (_title, _outcome, categories, _b0, effects) in enumerate(A06_CASES, 1):
        _require(3 <= len(categories) <= 5, f"A06 V{index:02d} has invalid category count")
        _require(len(set(categories)) == len(categories), f"A06 V{index:02d} repeats a category")
        _require(len(effects) == len(categories) - 1, f"A06 V{index:02d} must use k-1 effects")

    for index, case in enumerate(A07_CASES, 1):
        _title, _y, _x, _ref, _comparison, b0, b1, b2, x_low, x_high = case
        reference_change = (b0 + b1 * x_high) - (b0 + b1 * x_low)
        comparison_change = (b0 + b2 + b1 * x_high) - (b0 + b2 + b1 * x_low)
        _require(x_low < x_high and abs(reference_change - comparison_change) < 1e-12, f"A07 V{index:02d} lines are not parallel")
        _require(abs(((b0 + b2 + b1 * x_low) - (b0 + b1 * x_low)) - b2) < 1e-12, f"A07 V{index:02d} group gap failed")

    for index, case in enumerate(A08_CASES, 1):
        _title, _y, _x, _ref, _comparison, b0, b1, b2, x_low, x_high = case
        new_b0, new_b1, new_b2 = b0 + b2, b1, -b2
        for x_value in (x_low, x_high):
            original_ref = b0 + b1 * x_value
            original_comparison = b0 + b1 * x_value + b2
            new_comparison = new_b0 + new_b1 * x_value
            new_ref = new_b0 + new_b1 * x_value + new_b2
            _require(abs(original_ref - new_ref) < 1e-12, f"A08 V{index:02d} reference fit changed")
            _require(abs(original_comparison - new_comparison) < 1e-12, f"A08 V{index:02d} comparison fit changed")

    for index, case in enumerate(A09_CASES, 1):
        _title, _y, _x, _ref, _comparison, b0, b1, b2, b3, x_low, x_high = case
        reference_slope = (
            fitted(b0, b1, b2, b3, x_high, 0) - fitted(b0, b1, b2, b3, x_low, 0)
        ) / (x_high - x_low)
        comparison_slope = (
            fitted(b0, b1, b2, b3, x_high, 1) - fitted(b0, b1, b2, b3, x_low, 1)
        ) / (x_high - x_low)
        _require(abs(reference_slope - b1) < 1e-12, f"A09 V{index:02d} reference slope failed")
        _require(abs(comparison_slope - (b1 + b3)) < 1e-12, f"A09 V{index:02d} conditional slope failed")


def _validate_rendered_content(exercises: list[str], solutions: list[str]) -> None:
    """Assert the 90-ID contract and direct multipart solution correspondence."""

    _require(len(exercises) == 9 and len(solutions) == 9, "nine rendered groups are required")
    expected = [
        task_id(7, group, variant)
        for group in range(1, 10)
        for variant in range(1, 11)
    ]
    heading_pattern = re.compile(r"^## (T07-A\d{2}-V\d{2}): ([^\n]+)\n\n", re.MULTILINE)
    exercise_text = "".join(exercises)
    solution_text = "".join(solutions)
    exercise_matches = list(heading_pattern.finditer(exercise_text))
    solution_matches = list(heading_pattern.finditer(solution_text))
    _require([match.group(1) for match in exercise_matches] == expected, "exercise IDs are incomplete or out of order")
    _require([match.group(1) for match in solution_matches] == expected, "solution IDs are incomplete or out of order")
    _require([match.group(2) for match in exercise_matches] == [match.group(2) for match in solution_matches], "exercise and solution titles differ")
    for label, text, matches in (
        ("exercise", exercise_text, exercise_matches),
        ("solution", solution_text, solution_matches),
    ):
        _require("\u2014" not in text, f"{label} text contains a prohibited em dash")
        _require(text.count("$") % 2 == 0, f"{label} text has unbalanced math delimiters")
        for position, match in enumerate(matches):
            end = matches[position + 1].start() if position + 1 < len(matches) else len(text)
            body = text[match.end():end]
            for letter in "abcd":
                _require(body.count(f"({letter})") == 1, f"{match.group(1)} {label} needs one ({letter}) response")
            minimum = 260 if label == "exercise" else 420
            _require(len(body.strip()) >= minimum, f"{match.group(1)} {label} is too brief")
    _require(
        all(("constructed" in section.lower() or "hypothetical" in section.lower()) for section in exercises),
        "each group must explicitly identify its fictional teaching outputs",
    )


def render_a01() -> tuple[str, str]:
    exercise_group = [group_heading(1, GROUP_TITLES[0])]
    solution_group = [group_heading(1, GROUP_TITLES[0])]
    for variant, (context, case) in enumerate(zip(CONTEXTS, A01_CASES), 1):
        n, b0, b1, b2, r_y1, r_y2, r_12, rse = case
        beta1, beta2, r2, se1, se2 = two_predictor_output(
            n, b1, b2, r_y1, r_y2, r_12
        )
        adjusted = adjusted_r_squared(r2, n, 2)
        df = n - 3
        t1, t2 = b1 / se1, b2 / se2
        p1, p2 = student_t_two_sided_p(t1, df), student_t_two_sided_p(t2, df)
        output = markdown_table(
            ("Term", "Estimate", "SE", "Standardized", "Bivariate r"),
            [
                ("$X_1$", number(b1, 3), number(se1, 3), number(beta1, 3), number(r_y1, 3)),
                ("$X_2$", number(b2, 3), number(se2, 3), number(beta2, 3), number(r_y2, 3)),
            ],
        )
        prompt = rf"""A constructed study uses {n} cases. Its outcome $Y$ is {context["outcome"]} in {context["outcome_unit"]}; $X_1$ is {context["x1"]}, and $X_2$ is {context["x2"]}. The fitted intercept is {number(b0, 3)}. The selected output is:

{output}

The model reports $R^2={number(r2, 3)}$, adjusted $R^2={number(adjusted, 3)}$, residual standard error $={number(rse, 2)}$ {context["outcome_unit"]}, and residual $df={df}$.

(a) Write the fitted equation and explain how an unstandardized estimate differs from a standardized coefficient. (b) Interpret both unstandardized slopes conditionally, using the outcome unit and the phrase "with the other predictor held fixed." (c) Calculate each $t$ statistic as estimate divided by its standard error, obtain the two-sided $p$ values, and decide at $\alpha=.05$. (d) Interpret $R^2$, adjusted $R^2$, and the residual standard error, then explain why each standardized multiple-regression coefficient can differ from its bivariate correlation."""
        solution = rf"""(a) The fitted equation is $\hat Y={number(b0, 3)}+({number(b1, 3)})X_1+({number(b2, 3)})X_2$. An unstandardized slope uses the original measurement units. A standardized coefficient instead describes the fitted change in outcome standard deviations for a one-standard-deviation increase in a predictor, conditional on the other predictor.

(b) With {context["x2"]} held fixed, a one-unit increase in {context["x1"]} is associated with a fitted change of {number(b1, 3)} {context["outcome_unit"]} in {context["outcome"]}. With {context["x1"]} held fixed, a one-unit increase in {context["x2"]} is associated with a fitted change of {number(b2, 3)} {context["outcome_unit"]}. These are conditional associations, not automatically causal effects.

(c) For $X_1$, $t={number(b1, 3)}/{number(se1, 3)}={number(t1, 3)}$ with {df} degrees of freedom, giving $p {p_text(p1)}$; therefore, {decision_text(p1)} at $\alpha=.05$. For $X_2$, $t={number(b2, 3)}/{number(se2, 3)}={number(t2, 3)}$, giving $p {p_text(p2)}$; therefore, {decision_text(p2)}. Each test concerns that one population coefficient conditional on the exact other term in this model.

(d) $R^2={number(r2, 3)}$ means the fitted two-predictor model accounts for {number(100*r2, 1)}% of the sample variation in {context["outcome"]}. Adjusted $R^2={number(adjusted, 3)}$ applies an in-sample penalty for estimating two slopes; it is not a new-data test. The residual standard error says observed outcomes typically remain spread by roughly {number(rse, 2)} {context["outcome_unit"]} around their fitted values, under the model. The standardized slopes, {number(beta1, 3)} and {number(beta2, 3)}, differ from the bivariate correlations, {number(r_y1, 3)} and {number(r_y2, 3)}, because each slope separates a predictor's conditional relationship from variation shared with the other predictor."""
        exercise_group.append(task(7, 1, variant, context["title"], prompt))
        solution_group.append(task(7, 1, variant, context["title"], solution))
    return "".join(exercise_group), "".join(solution_group)


def render_a02() -> tuple[str, str]:
    exercise_group = [group_heading(2, GROUP_TITLES[1])]
    solution_group = [group_heading(2, GROUP_TITLES[1])]
    for variant, (context, case) in enumerate(zip(CONTEXTS, A02_CASES), 1):
        n, sst, r1, r2, r3 = case
        r_values = (r1, r2, r3)
        adjusted = tuple(adjusted_r_squared(r, n, p) for p, r in enumerate(r_values, 1))
        sse = tuple(sst * (1.0 - r) for r in r_values)
        changes = (r1, r2 - r1, r3 - r2)
        change_df = 1
        error_df = n - 3 - 1
        change_f = (changes[2] / change_df) / ((1.0 - r3) / error_df)
        change_p = student_t_two_sided_p(math.sqrt(change_f), error_df)
        model_rows = [
            ("M1", context["x1"], "1", number(r1, 3)),
            ("M2", f'{context["x1"]}; {context["x2"]}', "2", number(r2, 3)),
            ("M3", f'{context["x1"]}; {context["x2"]}; {context["x3"]}', "3", number(r3, 3)),
        ]
        prompt = rf"""Three constructed ordinary least-squares models use the same $n={n}$ cases, the same {context["outcome"]} outcome, and an intercept. Each later model contains every term in the earlier model. The common total sum of squares is $SST={number(sst, 1)}$, and $p$ denotes the number of predictor coefficients.

{markdown_table(("Model", "Predictor set", "p", "R-squared"), model_rows)}

(a) Calculate the residual sum of squares $SSE=SST(1-R^2)$ for every model and the change in $R^2$ at each step after M1. (b) Calculate adjusted $R^2=1-(1-R^2)(n-1)/(n-p-1)$ for all three models. (c) Describe what ordinary and adjusted $R^2$ say about adding {context["x3"]}. (d) Treat M2 as the restricted model and M3 as the unrestricted model. Write both model equations, state the null hypothesis for the added coefficient, and calculate the incremental test $F=[(R_U^2-R_R^2)/1]/[(1-R_U^2)/(n-3-1)]$ with 1 and {error_df} degrees of freedom. Obtain its p-value and interpret the decision. (e) Explain why this is a valid nested sequence and why neither the fit table nor the incremental test establishes causality or new-data performance."""
        solution_rows = [
            ("M1", number(sse[0], 2), "not a later step", number(adjusted[0], 4)),
            ("M2", number(sse[1], 2), number(changes[1], 3), number(adjusted[1], 4)),
            ("M3", number(sse[2], 2), number(changes[2], 3), number(adjusted[2], 4)),
        ]
        direction = "increases" if adjusted[2] > adjusted[1] else "decreases"
        solution = rf"""(a) Apply $SSE={number(sst, 1)}(1-R^2)$ and subtract consecutive $R^2$ values. (b) Substitute each model's own number of predictors into the adjusted formula:

{markdown_table(("Model", "SSE", "Change in R-squared", "Adjusted R-squared"), solution_rows)}

(c) Ordinary $R^2$ rises from {number(r2, 3)} to {number(r3, 3)} when {context["x3"]} is added, an increment of {number(changes[2], 3)}, or {number(100*changes[2], 1)} percentage points of sample variation. Ordinary $R^2$ cannot fall when a predictor is added to this same-case, same-intercept model. Adjusted $R^2$ {direction} from {number(adjusted[1], 4)} to {number(adjusted[2], 4)} because it weighs the extra fit against the additional estimated slope. That adjustment is descriptive and in-sample.

(d) The restricted equation is $Y=\beta_0+\beta_1X_1+\beta_2X_2+\varepsilon$. The unrestricted equation adds {context["x3"]}: $Y=\beta_0+\beta_1X_1+\beta_2X_2+\beta_3X_3+\varepsilon$. The null hypothesis is $H_0:\beta_3=0$, conditional on the terms already in M2. The incremental statistic is $F=[({number(r3,3)}-{number(r2,3)})/1]/[(1-{number(r3,3)})/({n}-3-1)]={number(change_f,4)}$ with 1 and {error_df} degrees of freedom. Its p-value is {number(change_p,4)}, so the added term {'meets' if change_p < 0.05 else 'does not meet'} the 5% criterion.

(e) M1 is contained in M2, and M2 is contained in M3: setting each newly added coefficient to zero reproduces the preceding model. The outcome, cases, and intercept also stay the same, so the fit changes are comparable as nested steps. The sequence does not randomize predictors, exclude omitted variables, prove a mechanism, or measure prediction on new cases. Those questions require design information and separate validation."""
        exercise_group.append(task(7, 2, variant, context["title"], prompt))
        solution_group.append(task(7, 2, variant, context["title"], solution))
    return "".join(exercise_group), "".join(solution_group)


def render_a03() -> tuple[str, str]:
    exercise_group = [group_heading(3, GROUP_TITLES[2])]
    solution_group = [group_heading(3, GROUP_TITLES[2])]
    for variant, (context, case, candidate_names) in enumerate(zip(CONTEXTS, A03_CASES, CANDIDATE_NAMES), 1):
        n, r2, critical, coefficients = case
        names = (context["x1"], context["x2"], candidate_names[0])
        df2 = n - 4
        f_value = global_f(r2, n, 3)
        coefficient_rows = [
            (name, number(estimate, 3), number(se, 3))
            for name, (estimate, se) in zip(names, coefficients)
        ]
        prompt = rf"""A constructed three-predictor model for {context["outcome"]} uses $n={n}$ and reports $R^2={number(r2, 3)}$. Let $\beta_1$, $\beta_2$, and $\beta_3$ denote the three population slopes. For $\alpha=.05$, the supplied critical value is $F_{{3,{df2}}}={number(critical, 5)}$. Its coefficient table is:

{markdown_table(("Predictor", "Estimate", "SE"), coefficient_rows)}

(a) State the global null hypothesis, calculate $F=(R^2/3)/[(1-R^2)/(n-3-1)]$, and make the global decision. (b) For each predictor, calculate $t=b/SE$, its two-sided $p$ value with {df2} residual degrees of freedom, and the decision at $\alpha=.05$. (c) State the individual coefficient null and explain why a global result does not identify which slope differs from zero. (d) Reconcile this model's global and individual decisions without treating either kind of test as proof of importance, prediction, or causality."""
        details = []
        for name, (estimate, se) in zip(names, coefficients):
            t_value = estimate / se
            p_value = student_t_two_sided_p(t_value, df2)
            details.append(
                f"{name}: $t={number(estimate, 3)}/{number(se, 3)}={number(t_value, 3)}$, "
                f"$p {p_text(p_value)}$, so {decision_text(p_value)}"
            )
        global_decision = "reject" if f_value > critical else "do not reject"
        significant_count = sum(
            student_t_two_sided_p(estimate / se, df2) < 0.05
            for estimate, se in coefficients
        )
        test_verb = "rejects" if significant_count == 1 else "reject"
        solution = rf"""(a) The global null is $H_0:\beta_1=\beta_2=\beta_3=0$. The statistic is $F=({number(r2, 3)}/3)/[(1-{number(r2, 3)})/{df2}]={number(f_value, 3)}$. Because {number(f_value, 3)} is {"greater than" if f_value > critical else "not greater than"} {number(critical, 5)}, {global_decision} the global null at $\alpha=.05$.

(b) The coefficient calculations are: {"; ".join(details)}. Thus {significant_count} of the three displayed individual tests {test_verb} at the stated level.

(c) For predictor $X_j$, the individual null is $H_0:\beta_j=0$ conditional on every other term in this exact model. The global test asks one joint question about all three slopes. Rejecting it says at least one non-intercept population slope differs from zero under the model, but the global statistic does not name a predictor. Not rejecting it likewise is not proof that every population slope equals zero.

(d) The two sets of decisions can differ because the global test evaluates the predictors jointly, whereas each $t$ test isolates one conditional coefficient and its uncertainty. Shared predictor variation can make individual standard errors large even when the predictor set has joint explanatory value. Conversely, sampling variation can yield a small individual p-value in a model whose global test is not rejected. A p-value does not measure effect size, practical value, future prediction, or causality."""
        exercise_group.append(task(7, 3, variant, context["title"], prompt))
        solution_group.append(task(7, 3, variant, context["title"], solution))
    return "".join(exercise_group), "".join(solution_group)


def render_a04() -> tuple[str, str]:
    exercise_group = [group_heading(4, GROUP_TITLES[3])]
    solution_group = [group_heading(4, GROUP_TITLES[3])]
    for variant, (context, case, names) in enumerate(zip(CONTEXTS, A04_CASES, CANDIDATE_NAMES), 1):
        base_r2, semipartials = case
        candidate_rows = [
            (name, number(value, 3)) for name, value in zip(names, semipartials)
        ]
        increments = tuple(value * value for value in semipartials)
        new_r2 = tuple(base_r2 + increment for increment in increments)
        winner = max(range(3), key=lambda index: increments[index])
        prompt = rf"""A constructed current model for {context["outcome"]} already contains {context["x1"]} and {context["x2"]}, with $R^2={number(base_r2, 3)}$. Each candidate below was separately regressed on those current predictors. The residual from that regression is the candidate's part not linearly predicted by the current set. The table reports the correlation between that residualized candidate and the original, not residualized, outcome. The symbol $r_{{sp}}$ denotes this semipartial correlation:

{markdown_table(("Candidate", "Semipartial r"), candidate_rows)}

(a) Explain why this is a semipartial correlation rather than a partial correlation. (b) For each one-candidate addition, calculate $\Delta R^2=r_{{sp}}^2$ and the resulting $R^2$. (c) If a forward step uses the largest increment, identify the chosen candidate and quantify its increment. (d) Explain what this step does and does not justify, including why it neither proves that the chosen variable is true or causal nor guarantees that it will remain best after another term enters."""
        result_rows = [
            (name, number(value, 3), number(increment, 4), number(result, 4))
            for name, value, increment, result in zip(names, semipartials, increments, new_r2)
        ]
        solution = rf"""(a) Each candidate is residualized against the current predictors, but the outcome remains in its original form. That one-sided residualization defines a semipartial correlation. A partial correlation would residualize both the candidate and the outcome against the current predictor set.

(b) Squaring each semipartial correlation gives the one-predictor increment:

{markdown_table(("Candidate", "Semipartial r", "Increment in R-squared", "New R-squared"), result_rows)}

(c) The largest squared semipartial correlation is {number(increments[winner], 4)}, for {names[winner]}. A forward rule based only on the displayed candidates would add that predictor first, raising the sample $R^2$ from {number(base_r2, 3)} to {number(new_r2[winner], 4)}.

(d) The step ranks these three candidates by the additional sample variation each explains after the current predictors. Squaring removes the sign, so the sign of $r_{{sp}}$ still matters for the direction of association even though it does not affect $\Delta R^2$. The ranking is conditional on the present model, candidates, and sample. After another predictor enters, shared variation changes what remains in every other candidate. Selection does not prove truth, causal effect, substantive importance, or performance on new data."""
        exercise_group.append(task(7, 4, variant, context["title"], prompt))
        solution_group.append(task(7, 4, variant, context["title"], solution))
    return "".join(exercise_group), "".join(solution_group)


def render_a05() -> tuple[str, str]:
    exercise_group = [group_heading(5, GROUP_TITLES[4])]
    solution_group = [group_heading(5, GROUP_TITLES[4])]
    k_values = (3, 4, 5, 6)
    for variant, (context, log_likelihoods) in enumerate(zip(CONTEXTS, A05_CASES), 1):
        formulas = (
            context["x1"],
            f'{context["x1"]} + {context["x2"]}',
            f'{context["x1"]} + {context["x2"]} + {context["x3"]}',
            f'{context["x1"]} + {context["x2"]} + {context["x3"]} + a prespecified product term',
        )
        input_rows = [
            (f"M{index}", formula, k, number(ll, 1))
            for index, (formula, k, ll) in enumerate(zip(formulas, k_values, log_likelihoods), 1)
        ]
        aics = tuple(-2.0 * ll + 2.0 * k for ll, k in zip(log_likelihoods, k_values))
        minimum = min(aics)
        deltas = tuple(aic - minimum for aic in aics)
        forward_rows = [
            ("Step 1", f'add {context["x2"]}', number(aics[1], 2)),
            ("Step 1", f'add {context["x3"]}', number(aics[1] + 3.20, 2)),
            ("Step 1", "add the product term", number(aics[1] + 6.40, 2)),
            ("Step 2", "stop after M2", number(aics[1], 2)),
            ("Step 2", f'add {context["x3"]}', number(aics[2], 2)),
            ("Step 2", "add the product term", number(aics[2] + 2.80, 2)),
            ("Step 3", "stop after M3", number(aics[2], 2)),
            ("Step 3", "add the product term", number(aics[3], 2)),
        ]
        selected_models = [0, 1]
        if aics[2] < aics[1]:
            selected_models.append(2)
            if aics[3] < aics[2]:
                selected_models.append(3)
        final_index = selected_models[-1]
        path_coordinates = ", ".join(
            f"({step}, {number(aics[model],2)})"
            for step, model in enumerate(selected_models)
        )
        final_terms = formulas[final_index]
        prompt = rf"""Four constructed, prespecified candidate models use exactly the same cases and the same {context["outcome"]} outcome. Here $\log(L)$ is the maximized log likelihood reported by the fitted model. Under the stated convention, $K$ counts all estimated parameters used in the AIC calculation.

{markdown_table(("Model", "Terms", "K", "Log likelihood"), input_rows)}

(a) Calculate $AIC=-2\log(L)+2K$ for every model and calculate each $\Delta AIC=AIC-AIC_{{min}}$. (b) Starting from M1, carry out forward selection with the step-specific candidate table below. At each step choose the lowest available AIC only if it is lower than the current model; otherwise stop.

{markdown_table(("Forward step", "Candidate action", "AIC"), forward_rows)}

(c) Plot the AIC path of the models actually selected, beginning with M1 at step 0. (d) Write the final model formula and interpret what the selected terms contribute to the fitted association. (e) Explain why the path is conditional on earlier choices and why the final model is not thereby proven true, causal, or externally predictive."""
        result_rows = [
            (f"M{index}", number(aic, 2), number(delta, 2))
            for index, (aic, delta) in enumerate(zip(aics, deltas), 1)
        ]
        solution = rf"""(a) For example, M1 gives $-2({number(log_likelihoods[0], 1)})+2({k_values[0]})={number(aics[0], 2)}$. Applying the same rule to all four models gives:

{markdown_table(("Model", "AIC", "Delta AIC"), result_rows)}

(b) Step 1 selects M2 because {number(aics[1],2)} is lower than the other displayed Step 1 values and lower than M1's {number(aics[0],2)}. {'Step 2 selects M3 because its AIC is lower than the current M2 value.' if 2 in selected_models else 'Step 2 stops because neither addition has an AIC below the current M2 value.'} {'Step 3 then selects M4 because its AIC is below M3.' if 3 in selected_models else 'No later product term is selected on this forward path.'}

(c) The selected path coordinates are {path_coordinates}. Plot step on the horizontal axis and AIC on the vertical axis, connect only consecutive selected models, and stop where the rule stops. The downward movements show improvements in the relative fit-complexity balance along this particular path.

(d) The final selected formula is `{context["outcome"]} ~ {final_terms}`. Its terms describe conditional fitted associations for this outcome and these cases. They do not by themselves identify causes.

(e) A forward path recomputes the choice after each selected term, so an addition that looks useful at one stage can become redundant at another. The path can also stop before reaching the globally lowest AIC among combinations it never made reachable. AIC rewards fit but adds a complexity penalty. It does not establish that a selected model is the data-generating truth or that its predictions will generalize. New-data performance requires separate validation, and AIC values from different outcomes or case sets are not one comparable candidate family."""
        exercise_group.append(task(7, 5, variant, context["title"], prompt))
        solution_group.append(task(7, 5, variant, context["title"], solution))
    return "".join(exercise_group), "".join(solution_group)


def render_a06() -> tuple[str, str]:
    exercise_group = [group_heading(6, GROUP_TITLES[5])]
    solution_group = [group_heading(6, GROUP_TITLES[5])]
    for variant, (setting, outcome, categories, b0, effects) in enumerate(A06_CASES, 1):
        k = len(categories)
        reference = categories[0]
        formula_terms = " ".join(
            f"{'+' if effect >= 0 else '-'} {number(abs(effect), 2)}D_{index}"
            for index, effect in enumerate(effects, 1)
        )
        prompt = rf"""In a constructed model, the categorical predictor {setting.lower()} has $k={k}$ categories: {", ".join(categories)}. Use {reference} as the reference category and keep an intercept. Let $D_1$ through $D_{k-1}$ identify the nonreference categories in the order listed. The fitted model is $\hat Y={number(b0, 2)} {formula_terms}$ for {outcome}.

(a) State how many indicators are required and why. (b) Construct the complete zero-one coding table for every category. (c) Identify the reference row, calculate each category's fitted value, and interpret the coefficient on $D_1$ as a comparison with the reference. (d) Explain why adding a separate indicator for all $k$ categories while retaining the intercept creates exact redundancy, and describe what would change and stay unchanged if a different reference were chosen."""
        coding_rows = []
        fitted_rows = []
        for category_index, category in enumerate(categories):
            codes = tuple(int(category_index == indicator_index) for indicator_index in range(1, k))
            coding_rows.append((category, *codes))
            fit_value = b0 if category_index == 0 else b0 + effects[category_index - 1]
            fitted_rows.append((category, number(fit_value, 2)))
        headers = ("Category",) + tuple(
            f"$D_{index}$ ({categories[index]})" for index in range(1, k)
        )
        solution = rf"""(a) With an intercept, $k-1={k-1}$ indicators are required. The omitted category is represented by the intercept and becomes the comparison baseline.

(b) The complete coding is:

{markdown_table(headers, coding_rows)}

(c) {reference} is the reference because every indicator equals zero in its row. The fitted category values are:

{markdown_table(("Category", f"Fitted {outcome}"), fitted_rows)}

The coefficient on $D_1$ is {number(effects[0], 2)}. Therefore, the fitted {outcome} for {categories[1]} is {number(abs(effects[0]), 2)} points {"higher" if effects[0] > 0 else "lower"} than for {reference}. The intercept {number(b0, 2)} is the fitted value for {reference}.

(d) For each case, the $k$ category indicators would sum exactly to one, which is already the intercept column. Including all of them with the intercept makes one column an exact combination of the others, so the coefficients are not uniquely identified. Choosing a different reference changes the displayed intercept and category contrasts, but it does not change any category's fitted value."""
        exercise_group.append(task(7, 6, variant, setting, prompt))
        solution_group.append(task(7, 6, variant, setting, solution))
    return "".join(exercise_group), "".join(solution_group)


def render_a07() -> tuple[str, str]:
    exercise_group = [group_heading(7, GROUP_TITLES[6])]
    solution_group = [group_heading(7, GROUP_TITLES[6])]
    for variant, case in enumerate(A07_CASES, 1):
        title, outcome, x_name, reference, comparison, b0, b1, b2, x_low, x_high = case
        prompt = rf"""A constructed additive model uses $G=0$ for {reference} and $G=1$ for {comparison}: $\hat Y={number(b0, 2)}+({number(b1, 2)})X+({number(b2, 2)})G$, where $Y$ is {outcome} and $X$ is {x_name}.

(a) Write the fitted equation for each group and interpret the intercept at $X=0$, noting when zero may be only a mathematical reference. (b) Interpret the common $X$ slope and the group coefficient as conditional comparisons. (c) Calculate the fitted coordinates for both groups at $X={number(x_low, 1)}$ and $X={number(x_high, 1)}$ and organize them in a table. (d) Explain how those coordinates show parallel lines and a constant group gap, and state why the fitted gap alone does not establish a causal group effect."""
        rows = []
        for group_name, group in ((reference, 0), (comparison, 1)):
            for x_value in (x_low, x_high):
                rows.append(
                    (
                        group_name,
                        number(x_value, 1),
                        number(fitted(b0, b1, b2, 0.0, x_value, group), 2),
                    )
                )
        direction = "higher" if b2 > 0 else "lower"
        solution = rf"""(a) For {reference}, set $G=0$: $\hat Y={number(b0, 2)}+({number(b1, 2)})X$. For {comparison}, set $G=1$: $\hat Y={number(b0+b2, 2)}+({number(b1, 2)})X$. The intercept {number(b0, 2)} is the fitted {outcome} for {reference} when {x_name} equals zero. It may be mathematically necessary but substantively unhelpful if zero lies outside the meaningful range.

(b) Within either group, a one-unit increase in {x_name} is associated with a fitted change of {number(b1, 2)} units in {outcome}. At the same value of {x_name}, {comparison} is fitted {number(abs(b2), 2)} units {direction} than {reference}. "At the same value" expresses the model's conditional comparison, not an intervention.

(c) Substitution gives:

{markdown_table(("Group", "X", f"Fitted {outcome}"), rows)}

(d) Both equations have slope {number(b1, 2)}, so equal horizontal changes produce equal fitted vertical changes. Their intercepts differ by {number(b2, 2)}, and subtracting the two fitted values at either displayed $X$ gives that same constant gap. The model contains no $XG$ product term, so it imposes parallel fitted lines. The gap is an adjusted association; without suitable design and assumptions, it does not prove that changing group membership would change the outcome."""
        exercise_group.append(task(7, 7, variant, title, prompt))
        solution_group.append(task(7, 7, variant, title, solution))
    return "".join(exercise_group), "".join(solution_group)


def render_a08() -> tuple[str, str]:
    exercise_group = [group_heading(8, GROUP_TITLES[7])]
    solution_group = [group_heading(8, GROUP_TITLES[7])]
    for variant, case in enumerate(A08_CASES, 1):
        title, outcome, x_name, old_reference, new_reference, b0, b1, b2, x_low, x_high = case
        new_b0, new_b1, new_b2 = b0 + b2, b1, -b2
        prompt = rf"""A constructed additive model codes $G=0$ for {old_reference} and $G=1$ for {new_reference}: $\hat Y={number(b0, 2)}+({number(b1, 2)})X+({number(b2, 2)})G$, where $Y$ is {outcome} and $X$ is {x_name}. Recode with $H=0$ for {new_reference} and $H=1$ for {old_reference}.

(a) Derive the new intercept, $X$ slope, and coefficient on $H$. (b) Write both group equations under the new coding and interpret the new group coefficient. (c) At $X={number(x_low, 1)}$ and $X={number(x_high, 1)}$, calculate fitted values from both parameterizations for both groups and place them side by side. (d) Use the calculations to explain why releveling changes the coefficient coordinate system but cannot change fitted values, residuals, or group-specific fitted lines."""
        comparison_rows = []
        for group_name, old_g, new_h in (
            (old_reference, 0, 1),
            (new_reference, 1, 0),
        ):
            for x_value in (x_low, x_high):
                old_fit = b0 + b1 * x_value + b2 * old_g
                new_fit = new_b0 + new_b1 * x_value + new_b2 * new_h
                comparison_rows.append(
                    (
                        group_name,
                        number(x_value, 1),
                        number(old_fit, 2),
                        number(new_fit, 2),
                    )
                )
        direction = "higher" if new_b2 > 0 else "lower"
        solution = rf"""(a) The new reference is the old $G=1$ group, so its old intercept becomes the new intercept: $b'_0={number(b0, 2)}+({number(b2, 2)})={number(new_b0, 2)}$. The common slope remains $b'_1={number(new_b1, 2)}$. The contrast reverses direction, so $b'_2=-({number(b2, 2)})={number(new_b2, 2)}$.

(b) For {new_reference}, $H=0$, giving $\hat Y={number(new_b0, 2)}+({number(new_b1, 2)})X$. For {old_reference}, $H=1$, giving $\hat Y={number(new_b0, 2)}+({number(new_b1, 2)})X+({number(new_b2, 2)})={number(b0, 2)}+({number(b1, 2)})X$. At the same $X$, {old_reference} is fitted {number(abs(new_b2), 2)} units {direction} than {new_reference}.

(c) Both codings give:

{markdown_table(("Group", "X", "Fit from old coding", "Fit from new coding"), comparison_rows)}

(d) Every row has identical fitted values under the two codings. Releveling changes which group is represented by the intercept and reverses the displayed group contrast, but it describes the same two lines. Because each case keeps the same fitted value, subtracting that fit from its observed outcome also leaves every residual unchanged. Reference choice changes representation, not model fit or the underlying fitted relationships."""
        exercise_group.append(task(7, 8, variant, title, prompt))
        solution_group.append(task(7, 8, variant, title, solution))
    return "".join(exercise_group), "".join(solution_group)


def render_a09() -> tuple[str, str]:
    exercise_group = [group_heading(9, GROUP_TITLES[8])]
    solution_group = [group_heading(9, GROUP_TITLES[8])]
    for variant, case in enumerate(A09_CASES, 1):
        title, outcome, x_name, reference, comparison, b0, b1, b2, b3, x_low, x_high = case
        prompt = rf"""A constructed interaction model uses $G=0$ for {reference}, $G=1$ for {comparison}, and the product $XG$: $\hat Y={number(b0, 2)}+({number(b1, 2)})X+({number(b2, 2)})G+({number(b3, 2)})XG$. Here $Y$ is {outcome} and $X$ is {x_name}.

(a) Construct rows for both groups at $X={number(x_low, 1)}$ and $X={number(x_high, 1)}$, showing $G$ and $XG$. (b) Derive each group's conditional intercept and slope. (c) Calculate the four fitted coordinates and organize all quantities in one table. (d) Draw the two fitted lines from those coordinates in one labeled graph and mark the fitted group gap at both displayed $X$ values. (e) Interpret $b_1$, $b_2$, and $b_3$ at their proper reference conditions, explain how $b_3$ changes the group gap across $X$, and state why an interaction is not itself causal evidence."""
        rows = []
        for group_name, group in ((reference, 0), (comparison, 1)):
            for x_value in (x_low, x_high):
                rows.append(
                    (
                        group_name,
                        str(group),
                        number(x_value, 1),
                        number(x_value * group, 1),
                        number(fitted(b0, b1, b2, b3, x_value, group), 2),
                    )
                )
        gap_low = b2 + b3 * x_low
        gap_high = b2 + b3 * x_high
        solution = rf"""(a) When $G=0$, the product $XG$ is zero for every $X$. When $G=1$, $XG=X$. (b) Substitution gives {reference}: $\hat Y={number(b0, 2)}+({number(b1, 2)})X$, with slope {number(b1, 2)}. For {comparison}: $\hat Y={number(b0+b2, 2)}+({number(b1+b3, 2)})X$, with slope $b_1+b_3={number(b1, 2)}+({number(b3, 2)})={number(b1+b3, 2)}$.

(c) The product terms and fitted coordinates are:

{markdown_table(("Group", "G", "X", "XG", f"Fitted {outcome}"), rows)}

(d) Put {x_name} on the horizontal axis and fitted {outcome} on the vertical axis. For {reference}, connect its two table coordinates. For {comparison}, connect its two coordinates in a second labeled line. Draw vertical segments between the lines at $X={number(x_low,1)}$ and $X={number(x_high,1)}$ and label their lengths {number(gap_low,2)} and {number(gap_high,2)}. The nonparallel slopes make the changing gap visible.

(e) $b_1={number(b1, 2)}$ is the {x_name} slope in the reference group. $b_2={number(b2, 2)}$ is the fitted {comparison} minus {reference} difference specifically at $X=0$. It remains interpretable there, although zero may not be substantively central. $b_3={number(b3, 2)}$ is the difference between the two group slopes. Consequently, the fitted group gap is $b_2+b_3X$: it equals {number(gap_low, 2)} at $X={number(x_low, 1)}$ and {number(gap_high, 2)} at $X={number(x_high, 1)}$. The interaction describes how a conditional association differs by group. It does not establish that group or $X$ causes the outcome."""
        exercise_group.append(task(7, 9, variant, title, prompt))
        solution_group.append(task(7, 9, variant, title, solution))
    return "".join(exercise_group), "".join(solution_group)


def render_english() -> tuple[list[str], list[str]]:
    _validate_case_data()
    rendered = [
        render_a01(),
        render_a02(),
        render_a03(),
        render_a04(),
        render_a05(),
        render_a06(),
        render_a07(),
        render_a08(),
        render_a09(),
    ]
    exercises = [pair[0] for pair in rendered]
    solutions = [pair[1] for pair in rendered]
    _validate_rendered_content(exercises, solutions)
    return exercises, solutions


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--locale", choices=("en", "de", "sq"), default="en")
    args = parser.parse_args()
    if args.locale == "en":
        exercises, solutions = render_english()
    else:
        from topic07_practice_i18n import render_localized

        exercises, solutions = render_localized(args.locale, sys.modules[__name__])
    write_pair(7, args.locale, 9, exercises, solutions)
    validate_sources_allowing_incomplete_locales(args.locale, topic=7)
    print(
        "Generated and source-validated Topic 7 "
        f"{args.locale} exercise and solution sources."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
