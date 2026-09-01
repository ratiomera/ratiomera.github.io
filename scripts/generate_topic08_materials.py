#!/usr/bin/env python3
"""Generate Ratiomera's multilingual Topic 8 practice pair.

The ten registered worksheet groups define the learning objectives only. All
settings, values, tables, questions, and worked explanations below are newly
authored teaching material. English remains canonical; the reviewed German
and Albanian adaptations reuse its identifiers, values, formulas, and results.
"""

from __future__ import annotations

import argparse
import math

from intro_stats_practice_support import (
    f_upper_p,
    group_heading,
    number,
    task,
    validate_sources_allowing_incomplete_locales,
    write_pair,
)


OMNIBUS_CASES = [
    ("Reading formats and comprehension", "comprehension score", "reading format", ("print", "tablet", "audio"), "points", True),
    ("Museum routes and visit duration", "visit duration", "route type", ("free route", "numbered route", "guided route"), "minutes", True),
    ("Study locations and concentration", "concentration score", "usual study location", ("home", "library", "shared workspace"), "points", False),
    ("Reminder schedules and response delay", "response delay", "reminder schedule", ("none", "one reminder", "three reminders"), "hours", True),
    ("Archive interfaces and retrieval accuracy", "retrieval accuracy", "interface version", ("standard", "compact", "guided"), "points", True),
    ("Travel modes and commuting time", "commuting time", "usual travel mode", ("walking", "public transport", "car"), "minutes", False),
    ("Practice routines and delayed recall", "delayed-recall score", "practice routine", ("rereading", "self-testing", "mixed practice"), "points", True),
    ("Workshop tracks and confidence", "confidence score", "chosen workshop track", ("methods", "writing", "presentation"), "points", False),
    ("Caption styles and tutorial understanding", "understanding score", "caption style", ("none", "verbatim", "edited"), "points", True),
    ("Neighborhood types and park use", "weekly park visits", "neighborhood type", ("central", "suburban", "rural"), "visits", False),
]


RAW_GROUP_CASES = [
    ("Study routines and learning score", "learning score", ("Reference", "Planning", "Retrieval"), (12, 16, 20), "points"),
    ("Reading layouts and speed", "reading speed", ("Narrow", "Standard", "Wide"), (20, 22, 24), "words per minute above baseline"),
    ("Archive prompts and correct records", "correctly retrieved records", ("None", "Checklist", "Examples"), (15, 15, 15), "records"),
    ("Museum maps and route confidence", "route-confidence score", ("Text", "Icons", "Combined"), (45, 50, 47), "points"),
    ("Reminder timing and completion", "completion score", ("Morning", "Midday", "Evening"), (30, 35, 39), "points"),
    ("Note formats and argument detection", "argument-detection score", ("Free", "Outline", "Matrix"), (52, 56, 61), "points"),
    ("Practice spacing and recall", "recall score", ("Massed", "Two sessions", "Four sessions"), (40, 43, 48), "points"),
    ("Sound settings and focus", "focus score", ("Quiet", "Ambient", "Music"), (70, 68, 63), "points"),
    ("Route instructions and errors", "navigation-error score", ("Text", "Map", "Text plus map"), (18, 14, 10), "errors"),
    ("Feedback timing and revision quality", "revision-quality score", ("Immediate", "Next day", "One week"), (64, 67, 65), "points"),
]


TABLE_CASES = [
    ("Randomized reading prompts", (8, 8, 8), 96, 144, 3.44, True),
    ("Observed commuting modes", (10, 7, 9), 45, 210, 3.42, False),
    ("Randomized archive interfaces", (6, 6, 6, 6), 180, 220, 3.10, True),
    ("Self-selected workshop tracks", (12, 12, 12), 30, 330, 3.28, False),
    ("Randomized reminder schedules", (9, 9, 9), 120, 180, 3.35, True),
    ("Observed neighborhood types", (14, 9, 7), 75, 270, 3.35, False),
    ("Randomized caption styles", (7, 7, 7, 7), 210, 252, 3.01, True),
    ("Chosen study locations", (11, 11, 8), 54, 243, 3.35, False),
    ("Randomized route maps", (10, 10, 10), 160, 240, 3.35, True),
    ("Observed employment sectors", (8, 12, 10), 40, 260, 3.35, False),
]


CONTRAST_CASES = [
    ("Four study routines", (62, 66, 70, 74), 8, 25),
    ("Four reading layouts", (48, 53, 55, 59), 8, 16),
    ("Four archive prompts", (18, 21, 24, 23), 8, 9),
    ("Four museum routes", (72, 69, 76, 80), 8, 36),
    ("Four reminder schedules", (40, 45, 47, 52), 8, 20),
    ("Four note templates", (58, 61, 67, 69), 8, 24),
    ("Four practice intervals", (63, 68, 71, 77), 8, 30),
    ("Four sound settings", (74, 70, 68, 65), 8, 18),
    ("Four navigation aids", (51, 56, 60, 64), 8, 22),
    ("Four feedback schedules", (66, 70, 73, 71), 8, 28),
]


PAIRWISE_LEVELS = [3, 4, 5, 6, 7, 8, 4, 5, 6, 7]


FAMILY_CASES = [
    ("Study routines", (0.004, 0.018, 0.041, 0.083, 0.220)),
    ("Reading layouts", (0.009, 0.011, 0.037, 0.120, 0.310)),
    ("Archive prompts", (0.002, 0.015, 0.049, 0.070, 0.440)),
    ("Museum routes", (0.006, 0.024, 0.032, 0.190, 0.270)),
    ("Reminder schedules", (0.013, 0.021, 0.028, 0.055, 0.330)),
    ("Note templates", (0.001, 0.017, 0.044, 0.099, 0.510)),
    ("Practice intervals", (0.008, 0.019, 0.026, 0.078, 0.290)),
    ("Sound settings", (0.003, 0.014, 0.039, 0.140, 0.410)),
    ("Navigation aids", (0.007, 0.016, 0.047, 0.088, 0.360)),
    ("Feedback schedules", (0.005, 0.023, 0.035, 0.110, 0.250)),
]


TREND_CASES = [
    ("Practice sessions and recall", (52, 57, 63, 69), 10, 25),
    ("Reminder intensity and response", (44, 48, 51, 55), 10, 16),
    ("Reading guidance and comprehension", (61, 64, 68, 73), 10, 20),
    ("Archive examples and accuracy", (18, 20, 24, 27), 10, 9),
    ("Route rehearsal and confidence", (50, 56, 59, 66), 10, 24),
    ("Note structure and reasoning", (58, 62, 65, 71), 10, 18),
    ("Feedback frequency and revision", (63, 66, 70, 72), 10, 22),
    ("Ambient noise and focus", (74, 71, 68, 62), 10, 16),
    ("Navigation support and errors", (20, 17, 13, 9), 10, 12),
    ("Delay before feedback and retention", (72, 69, 65, 60), 10, 20),
]


FACTORIAL_CASES = [
    ("Captioning and practice", "Captioning", "Practice", (62, 68, 70, 76), 6, 16),
    ("Map and route rehearsal", "Map", "Rehearsal", (54, 60, 58, 70), 6, 20),
    ("Quiet room and checklist", "Quiet room", "Checklist", (65, 71, 69, 75), 6, 18),
    ("Prompt and feedback", "Prompt", "Feedback", (50, 59, 56, 61), 6, 15),
    ("Icons and examples", "Icons", "Examples", (72, 74, 76, 83), 6, 24),
    ("Planning and self-testing", "Planning", "Self-testing", (60, 67, 66, 78), 6, 21),
    ("Lighting and background sound", "Bright light", "Sound", (74, 67, 70, 65), 6, 17),
    ("Orientation and signs", "Orientation", "Signs", (48, 55, 59, 68), 6, 19),
    ("Spacing and retrieval cues", "Spacing", "Retrieval cues", (64, 72, 69, 80), 6, 23),
    ("Template and peer review", "Template", "Peer review", (57, 66, 63, 74), 6, 20),
]


RANDOM_FACTOR_CASES = [
    ("Libraries sampled from a regional population", "library", "three deliberately chosen interface designs", 5, 18, 6),
    ("Schools sampled from a district", "school", "two named teaching programs", 6, 20, 5),
    ("Interviewers sampled from a trained pool", "interviewer", "three fixed questionnaire versions", 4, 15, 7),
    ("Neighborhoods sampled from a city", "neighborhood", "two selected outreach messages", 8, 24, 8),
    ("Museum guides sampled from the staff roster", "guide", "four fixed tour scripts", 5, 21, 6),
    ("Archive boxes sampled from a collection", "archive box", "three chosen scanning settings", 7, 19, 5),
    ("Tutorial groups sampled from a program", "tutorial group", "two fixed practice schedules", 6, 17, 7),
    ("Routes sampled from a transport network", "route", "three selected sign designs", 9, 27, 9),
    ("Workshops sampled from an annual series", "workshop", "two named facilitation formats", 5, 16, 4),
    ("Days sampled from a semester", "day", "three fixed reminder messages", 8, 22, 6),
]


REPEATED_CASES = [
    ("Reading at three occasions", (18, 19, 20), 84, 176, 132, 0.82),
    ("Focus under three sound settings", (12, 22, 31), 66, 154, 110, 0.74),
    ("Recall across three delays", (16, 17, 15), 72, 198, 121, 0.91),
    ("Navigation across three route trials", (10, 25, 38), 90, 165, 143, 0.68),
    ("Confidence at three course points", (20, 21, 19), 78, 187, 126, 0.88),
    ("Accuracy under three interfaces", (14, 28, 35), 81, 143, 119, 0.71),
    ("Response time across three reminders", (24, 23, 26), 63, 209, 138, 0.95),
    ("Comprehension across three formats", (11, 20, 34), 96, 176, 154, 0.65),
    ("Revision quality at three drafts", (17, 18, 16), 75, 220, 132, 0.90),
    ("Search skill at three practice points", (13, 26, 40), 87, 187, 143, 0.70),
]


def vector(values: tuple[float, ...] | list[float]) -> str:
    return ", ".join(number(value, 0) for value in values)


def markdown_table(headers: tuple[str, ...], rows: list[tuple[str, ...]] | tuple[tuple[str, ...], ...]) -> str:
    header = "| " + " | ".join(headers) + " |"
    separator = "|" + "|".join("---" for _ in headers) + "|"
    body = ["| " + " | ".join(str(cell) for cell in row) + " |" for row in rows]
    return "\n".join((header, separator, *body))


def render_english() -> tuple[list[str], list[str]]:
    exercises: list[str] = []
    solutions: list[str] = []

    ex_group = [group_heading(1, "The Question Answered by One-Way ANOVA")]
    so_group = [group_heading(1, "The Question Answered by One-Way ANOVA")]
    for i,(title,outcome,factor,levels,unit,randomized) in enumerate(OMNIBUS_CASES,1):
        labels = ", ".join(levels)
        ex_group.append(task(8,1,i,title,f"A study records {outcome} in {unit} and compares the levels {labels} of the categorical factor {factor}. {'Cases were randomly assigned to the levels.' if randomized else 'The factor was observed without random assignment.'} (a) Identify the quantitative outcome, factor, and levels. (b) State the one-way ANOVA null and alternative hypotheses in words and symbols. (c) Explain why one omnibus test is preferable to beginning with three unadjusted pairwise tests. (d) State what a significant omnibus result would and would not establish."))
        causal = "Because cases were randomly assigned, a well-conducted study can support a causal interpretation for these conditions, subject to its design and assumptions." if randomized else "Because the groups were observed rather than randomly assigned, a difference describes association and does not by itself identify a causal effect."
        so_group.append(task(8,1,i,title,f"The quantitative outcome is {outcome}, measured in {unit}. The factor is {factor}, with levels {labels}. Write the population means as $\\mu_1$, $\\mu_2$, and $\\mu_3$. The null hypothesis is $H_0:\\mu_1=\\mu_2=\\mu_3$. The alternative is that at least two means differ. It does not say that every pair differs. Beginning with three separate tests would create a family of opportunities for a Type I error, while the omnibus $F$ test asks the single global question first. A significant result would provide evidence against equality of all three population means, but it would not identify which pairs differ. {causal}"))
    exercises.append("".join(ex_group)); solutions.append("".join(so_group))

    ex_group = [group_heading(2, "Group Means, Sum-of-Squares Partition, and the One-Way F Test")]
    so_group = [group_heading(2, "Group Means, Sum-of-Squares Partition, and the One-Way F Test")]
    offsets = (-3, -1, 1, 3)
    for i,(title,outcome,labels,means,unit) in enumerate(RAW_GROUP_CASES,1):
        groups = [[mean + offset for offset in offsets] for mean in means]
        rows = "\n".join(f"| {label} | {vector(tuple(values))} |" for label,values in zip(labels,groups))
        flat = [value for values in groups for value in values]
        grand = sum(flat) / len(flat)
        ss_factor = sum(len(values) * (sum(values)/len(values)-grand)**2 for values in groups)
        ss_error = sum(sum((value-sum(values)/len(values))**2 for value in values) for values in groups)
        ss_total = sum((value-grand)**2 for value in flat)
        df_factor = 2; df_error = 9
        ms_factor = ss_factor / df_factor; ms_error = ss_error / df_error
        f_value = ms_factor / ms_error
        decision = "reject" if f_value > 4.26 else "do not reject"
        ex_group.append(task(8,2,i,title,f"A constructed study records {outcome} in {unit}.\n\n| Group | Observations |\n|---|---|\n{rows}\n\n(a) Calculate the three group means and the grand mean. (b) Calculate $SS_A$, $SS_e$, and $SS_{{total}}$. (c) Verify $SS_{{total}}=SS_A+SS_e$. (d) Complete the degrees of freedom, mean squares, and $F$ statistic. (e) At the 5% level, compare the result with the supplied critical value $F_{{2,9}}=4.26$ and interpret the decision."))
        so_group.append(task(8,2,i,title,f"The group means are {vector(means)}, and the grand mean is {number(grand,4)} {unit}. The between-group calculation gives $SS_A=\\sum_i n_i(\\bar y_i-\\bar y)^2={number(ss_factor,4)}$. Summing squared deviations inside the three groups gives $SS_e={number(ss_error,4)}$. Around the grand mean, $SS_{{total}}={number(ss_total,4)}$, and {number(ss_total,4)} = {number(ss_factor,4)} + {number(ss_error,4)}, so the partition checks. The degrees of freedom are $df_A=3-1=2$, $df_e=12-3=9$, and $df_{{total}}=11$. Thus $MS_A={number(ss_factor,4)}/2={number(ms_factor,4)}$, $MS_e={number(ss_error,4)}/9={number(ms_error,4)}$, and $F={number(ms_factor,4)}/{number(ms_error,4)}={number(f_value,4)}$. Since {number(f_value,4)} is {'greater' if f_value > 4.26 else 'not greater'} than 4.26, we {decision} the equal-means null at the 5% level. The decision concerns the global mean pattern, not every pair separately."))
    exercises.append("".join(ex_group)); solutions.append("".join(so_group))

    ex_group = [group_heading(3, "Reconstructing an ANOVA Table and Reading the Design")]
    so_group = [group_heading(3, "Reconstructing an ANOVA Table and Reading the Design")]
    for i,(title,ns,ss_factor,ss_error,critical,randomized) in enumerate(TABLE_CASES,1):
        k=len(ns); total_n=sum(ns); df_factor=k-1; df_error=total_n-k; df_total=total_n-1
        ss_total=ss_factor+ss_error; ms_factor=ss_factor/df_factor; ms_error=ss_error/df_error; f_value=ms_factor/ms_error
        balanced=len(set(ns)) == 1; decision="reject" if f_value > critical else "do not reject"
        ex_group.append(task(8,3,i,title,f"A {'randomized' if randomized else 'nonrandomized observational'} study has group sizes $n_i=({', '.join(str(n) for n in ns)})$. Its incomplete ANOVA table reports $SS_A={ss_factor}$ and $SS_e={ss_error}$. (a) State the equal-means hypotheses. (b) Complete $SS_{{total}}$ and all three degrees of freedom. (c) Calculate both mean squares and $F$. (d) Compare $F$ with the supplied 5% critical value {number(critical,2)}. (e) Identify whether the design is balanced and explain the limit on a causal conclusion."))
        design = "The equal group sizes make the design balanced." if balanced else "The unequal group sizes make the design unbalanced."
        causal = "Random assignment can support a causal interpretation for the assigned conditions if the implementation and model assumptions are credible." if randomized else "Without random assignment, the result describes group association and cannot by itself rule out preexisting group differences."
        so_group.append(task(8,3,i,title,f"For $k={k}$ groups, $H_0:\\mu_1=\\cdots=\\mu_{k}$; the alternative is that at least two means differ. The total sum of squares is {ss_factor}+{ss_error}={ss_total}. With $N={total_n}$, the degrees of freedom are $df_A={k}-1={df_factor}$, $df_e={total_n}-{k}={df_error}$, and $df_{{total}}={total_n}-1={df_total}$. Then $MS_A={ss_factor}/{df_factor}={number(ms_factor,4)}$, $MS_e={ss_error}/{df_error}={number(ms_error,4)}$, and $F={number(f_value,4)}$. Because {number(f_value,4)} is {'greater' if f_value > critical else 'not greater'} than {number(critical,2)}, we {decision} the null at the 5% level. {design} {causal}"))
    exercises.append("".join(ex_group)); solutions.append("".join(so_group))

    ex_group = [group_heading(4, "Simple Pairwise and Pooled Complex Contrasts")]
    so_group = [group_heading(4, "Simple Pairwise and Pooled Complex Contrasts")]
    simple=(-1,1,0,0); complex_weights=(-1,-1,1,1)
    for i,(title,means,n,mse) in enumerate(CONTRAST_CASES,1):
        d_simple=sum(c*m for c,m in zip(simple,means)); d_complex=sum(c*m for c,m in zip(complex_weights,means))
        se_simple=math.sqrt(mse/n*sum(c*c for c in simple)); se_complex=math.sqrt(mse/n*sum(c*c for c in complex_weights))
        t_simple=d_simple/se_simple; t_complex=d_complex/se_complex
        ex_group.append(task(8,4,i,title,f"Four balanced groups have means ({vector(means)}), $n={n}$ per group, and pooled error mean square $MS_e={mse}$. (a) Verify that $c=(-1,1,0,0)$ is a contrast and calculate its estimate, standard error, and $t$ statistic. (b) Repeat for the pooled comparison $c=(-1,-1,1,1)$. (c) Translate both weight patterns into plain-language questions. (d) Explain why the larger numerical contrast estimate is not automatically the stronger standardized result."))
        so_group.append(task(8,4,i,title,f"Both weight vectors sum to zero, so both are valid contrasts. The simple contrast compares group 2 with group 1: $D_s={number(d_simple,4)}$. Its standard error is $SE_s=\\sqrt{{({mse}/{n})[(-1)^2+1^2]}}={number(se_simple,4)}$, giving $t_s={number(d_simple,4)}/{number(se_simple,4)}={number(t_simple,4)}$. The complex contrast compares the sum of groups 3 and 4 with the sum of groups 1 and 2: $D_c={number(d_complex,4)}$. Its standard error is $SE_c=\\sqrt{{({mse}/{n})[(-1)^2+(-1)^2+1^2+1^2]}}={number(se_complex,4)}$, so $t_c={number(t_complex,4)}$. Dividing every complex weight by 2 would express the difference between the two pooled averages and would leave its $t$ statistic unchanged because its estimate and standard error scale together. Raw contrast estimates use different scales when their weights differ, so compare the stated question and standardized statistic, not magnitude alone."))
    exercises.append("".join(ex_group)); solutions.append("".join(so_group))

    ex_group = [group_heading(5, "All Pairwise Comparisons and Bonferroni Protection")]
    so_group = [group_heading(5, "All Pairwise Comparisons and Bonferroni Protection")]
    for i,k in enumerate(PAIRWISE_LEVELS,1):
        comparisons=k*(k-1)//2; threshold=.05/comparisons; independent_risk=1-(1-.05)**comparisons
        ex_group.append(task(8,5,i,f"All pairs among {k} levels",f"An analyst wants every pairwise comparison among $k={k}$ factor levels and wants the familywise Type I error rate no larger than 0.05. (a) Count the distinct pairs. (b) Calculate the Bonferroni per-test threshold. (c) Under the simplifying assumption of independent tests, calculate the familywise risk if every comparison instead used 0.05. (d) Explain why the Bonferroni guarantee does not require the pairwise tests to be independent."))
        so_group.append(task(8,5,i,f"All pairs among {k} levels",f"The number of distinct unordered pairs is $m=k(k-1)/2={k}({k}-1)/2={comparisons}$. Bonferroni uses $\\alpha_{{test}}=0.05/{comparisons}={number(threshold,4)}$. If all {comparisons} tests were independent and each used 0.05, the probability of at least one Type I error under the complete null would be $1-(1-0.05)^{{{comparisons}}}={number(independent_risk,4)}$. Actual pairwise comparisons often share groups and are therefore dependent, so that last expression is an illustration rather than their general exact familywise rate. Bonferroni relies on an upper bound for the probability of a union of errors, so it controls the family even without independence, although it can be conservative."))
    exercises.append("".join(ex_group)); solutions.append("".join(so_group))

    ex_group = [group_heading(6, "Defining a Comparison Family Before Looking at Results")]
    so_group = [group_heading(6, "Defining a Comparison Family Before Looking at Results")]
    labels=("A versus B","A versus C","A versus D","B versus C","B versus D")
    for i,(title,pvalues) in enumerate(FAMILY_CASES,1):
        pvalue_rows=[(label,number(p,3)) for label,p in zip(labels,pvalues)]
        analyst_rows=(
            ("Analyst 1", "Before seeing outcomes, plans A versus B and A versus C only"),
            ("Analyst 2", "Before seeing outcomes, plans all five displayed comparisons"),
            ("Analyst 3", "Before seeing outcomes, plans A versus D only"),
            ("Analyst 4", "Plans all five, then drops the comparison with the largest p-value after seeing outcomes"),
            ("Analyst 5", "Makes no prior choice, inspects all five, then reports only the smallest p-value"),
        )
        ex_group.append(task(8,6,i,title,f"Five analysts receive the same five unadjusted results.\n\n{markdown_table(('Comparison','Unadjusted p-value'),pvalue_rows)}\n\nTheir stated plans are:\n\n{markdown_table(('Analyst','Decision process'),analyst_rows)}\n\n(a) For each analyst, define the comparison family that must be protected and explain why its size is 1, 2, or 5. (b) Calculate the analyst's Bonferroni threshold for familywise $\\alpha=0.05$. (c) Identify which of that analyst's reported comparisons meet the threshold. (d) Explain why dropping or selecting a comparison after seeing outcomes does not make the family smaller or turn a comparison into a planned one. (e) State what each analyst would have needed to document before viewing outcomes."))
        plan_indices=((0,1),tuple(range(5)),(2,),tuple(range(5)),tuple(range(5)))
        solution_rows=[]
        for analyst_index,indices in enumerate(plan_indices,1):
            family_size=len(indices)
            threshold=.05/family_size
            passing=[labels[index] for index in indices if pvalues[index] <= threshold]
            result=", ".join(passing) if passing else "none"
            solution_rows.append((f"Analyst {analyst_index}",str(family_size),number(threshold,3),result))
        so_group.append(task(8,6,i,title,f"(a) and (b) A family contains every comparison made available by the decision process, including comparisons examined and later hidden. The resulting family sizes and thresholds are:\n\n{markdown_table(('Analyst','Family size','Bonferroni threshold','Results meeting threshold'),solution_rows)}\n\n(c) Each result in the final column is obtained by comparing only the p-values in that analyst's honest family with $0.05/m$. Analyst 1 has two prospectively named comparisons, Analyst 2 has five, and Analyst 3 has one. Analysts 4 and 5 also have five because their reduction happened after the outcomes were visible. (d) Removing the largest result or highlighting the smallest result after inspection is data-dependent selection. It cannot erase the other opportunities for a Type I error, and it cannot make the highlighted question planned retrospectively. (e) Before viewing outcomes, each analyst needed to record the scientific comparison, its direction or contrast weights where relevant, the complete family of primary and secondary comparisons, and the chosen multiplicity rule."))
    exercises.append("".join(ex_group)); solutions.append("".join(so_group))

    ex_group = [group_heading(7, "A Prespecified Trend Contrast")]
    so_group = [group_heading(7, "A Prespecified Trend Contrast")]
    weights=(-3,-1,1,3)
    for i,(title,means,n,mse) in enumerate(TREND_CASES,1):
        estimate=sum(c*m for c,m in zip(weights,means)); se=math.sqrt(mse/n*sum(c*c for c in weights)); t_value=estimate/se
        ex_group.append(task(8,7,i,title,f"Four equally spaced ordered levels have means ({vector(means)}), $n={n}$ per level, and $MS_e={mse}$. Three analysts propose $c_1=(0,1,2,3)$, $c_2=(-3,-1,1,3)$, and $c_3=(0.5,-0.5,-0.5,0.5)$. (a) Sketch each weight sequence against the four ordered levels and state the pattern it represents. (b) Check which vectors satisfy the contrast condition that their weights sum to zero. (c) Repair $c_1$ by subtracting its mean weight from every entry, and explain why the repaired vector represents the same linear direction as $c_2$. (d) Use the valid linear-trend weights $c_2$ to calculate the weighted estimate, its standard error, and its $t$ statistic. (e) Compare $|t|$ with the supplied two-sided 5% critical value 2.028 and interpret the sign as an ordered pattern rather than proof of a perfectly linear relationship."))
        so_group.append(task(8,7,i,title,f"(a) The weights $c_1$ rise by one unit at every level, so their sketch is a straight increasing sequence. The weights $c_2$ also rise by equal increments and are centered around zero. The weights $c_3$ compare the two endpoints with the two middle levels, so they represent curvature rather than a linear trend. (b) The sums are $0+1+2+3=6$, $-3-1+1+3=0$, and $0.5-0.5-0.5+0.5=0$. Thus $c_2$ and $c_3$ are contrasts, but only $c_2$ is the stated linear-trend contrast. (c) The mean of $c_1$ is $1.5$. Subtracting it gives $(-1.5,-0.5,0.5,1.5)$, which is exactly one half of $c_2$. Multiplying every contrast weight by the same positive constant changes the numerical scale of the estimate and standard error together but not the tested direction or $t$ statistic. (d) With $c_2$, the weighted estimate is $D=\\sum c_i\\bar y_i={number(estimate,4)}$. Because the groups are balanced, $SE(D)=\\sqrt{{(MS_e/n)\\sum c_i^2}}=\\sqrt{{({mse}/{n})(9+1+1+9)}}={number(se,4)}$. Thus $t={number(estimate,4)}/{number(se,4)}={number(t_value,4)}$. (e) Since $|{number(t_value,4)}|$ is {'greater' if abs(t_value)>2.028 else 'not greater'} than 2.028, the linear trend {'meets' if abs(t_value)>2.028 else 'does not meet'} the two-sided 5% criterion. The {'positive' if estimate>0 else 'negative'} sign means the weighted pattern tends to {'rise' if estimate>0 else 'fall'} across the ordered levels. It does not prove equal adjacent changes or rule out curvature."))
    exercises.append("".join(ex_group)); solutions.append("".join(so_group))

    ex_group = [group_heading(8, "Cell Means, Marginal Means, and Interaction in a Two-Factor ANOVA")]
    so_group = [group_heading(8, "Cell Means, Marginal Means, and Interaction in a Two-Factor ANOVA")]
    for i,(title,a_name,b_name,cells,n,mse) in enumerate(FACTORIAL_CASES,1):
        a0b0,a0b1,a1b0,a1b1=cells; grand=sum(cells)/4
        a_means=((a0b0+a0b1)/2,(a1b0+a1b1)/2); b_means=((a0b0+a1b0)/2,(a0b1+a1b1)/2)
        ss_a=2*n*sum((m-grand)**2 for m in a_means); ss_b=2*n*sum((m-grand)**2 for m in b_means)
        ss_ab=n*sum((cell-a_means[a]-b_means[b]+grand)**2 for a in range(2) for b,cell in enumerate(cells[2*a:2*a+2]))
        df_error=4*(n-1); ss_error=mse*df_error
        f_a=ss_a/mse; f_b=ss_b/mse; f_ab=ss_ab/mse
        interaction="The change across factor B differs between the two levels of factor A, so the cell pattern contains an interaction." if abs((a0b1-a0b0)-(a1b1-a1b0))>1e-9 else "The change across factor B is the same at both levels of factor A, so these cell means show no interaction."
        ex_group.append(task(8,8,i,title,f"A balanced $2\\times2$ study has $n={n}$ observations per cell. The cell means, ordered as $A_0B_0,A_0B_1,A_1B_0,A_1B_1$, are ({vector(cells)}). Factor A is {a_name}; factor B is {b_name}. The pooled error mean square is $MS_e={mse}$. (a) Calculate the two marginal means for each factor and the grand mean. (b) Describe both main-effect patterns and the interaction pattern. (c) State the three null hypotheses. (d) Reconstruct $SS_A$, $SS_B$, $SS_{{AB}}$, $SS_e$, their degrees of freedom, and the three $F$ ratios. (e) Draw a means plot with $B_0$ and $B_1$ on the horizontal axis and one labeled line for each level of factor A. Explain how parallel or nonparallel lines express the interaction result."))
        so_group.append(task(8,8,i,title,f"(a) The factor-A marginal means are ({number(a_means[0],4)}, {number(a_means[1],4)}); the factor-B marginal means are ({number(b_means[0],4)}, {number(b_means[1],4)}); and the grand mean is {number(grand,4)}. (b) The A main effect compares its two marginal means, and the B main effect compares its two marginal means. {interaction} (c) The three null hypotheses are no population A main effect, no population B main effect, and no population $A\\times B$ interaction. (d) Balanced-design calculations give $SS_A={number(ss_a,4)}$, $SS_B={number(ss_b,4)}$, and $SS_{{AB}}={number(ss_ab,4)}$. With $df_A=df_B=df_{{AB}}=1$ and $df_e=4({n}-1)={df_error}$, $SS_e=MS_e\\,df_e={mse}({df_error})={number(ss_error,4)}$. Therefore $F_A={number(f_a,4)}$, $F_B={number(f_b,4)}$, and $F_{{AB}}={number(f_ab,4)}$. (e) Plot the factor-A level $A_0$ through the coordinates $(B_0,{number(a0b0,4)})$ and $(B_1,{number(a0b1,4)})$. Plot $A_1$ through $(B_0,{number(a1b0,4)})$ and $(B_1,{number(a1b1,4)})$. {'The two changes differ, so the lines are nonparallel and the plot displays the interaction.' if 'contains an interaction' in interaction else 'The two changes are equal, so the lines are parallel and the plot displays no interaction.'} Main effects summarize margins, while interaction asks whether one factor's pattern changes across the other factor."))
    exercises.append("".join(ex_group)); solutions.append("".join(so_group))

    ex_group = [group_heading(9, "Fixed and Random Factors, Variance Components, and the ICC")]
    so_group = [group_heading(9, "Fixed and Random Factors, Variance Components, and the ICC")]
    for i,(title,random_level,fixed_factor,n,ms_between,ms_error) in enumerate(RANDOM_FACTOR_CASES,1):
        var_between=(ms_between-ms_error)/n; var_error=ms_error; icc=var_between/(var_between+var_error)
        ex_group.append(task(8,9,i,title,f"A study includes a random sample of {random_level} levels from a wider population and also includes {fixed_factor}. For the balanced one-way analysis of the random {random_level} factor, $n={n}$ observations occur at every sampled level, $MS_A={ms_between}$, and $MS_e={ms_error}$. (a) Explain why the {random_level} factor is random and the other factor is fixed. (b) State the population target of the random-factor analysis. (c) Estimate the between-level and error variance components. (d) Calculate and interpret the one-way ICC. (e) State why this formula should not be applied automatically to every grouped design."))
        so_group.append(task(8,9,i,title,f"The {random_level} levels were sampled to represent a wider population of possible levels, so repeating the study could draw new levels. By contrast, {fixed_factor} names the exact selected conditions of interest. The random-factor target is variation across the population of {random_level} levels, not a list of pairwise differences among only the sampled labels. In this balanced one-way setting, $\\widehat{{\\sigma}}_A^2=(MS_A-MS_e)/n=({ms_between}-{ms_error})/{n}={number(var_between,4)}$ and $\\widehat{{\\sigma}}_e^2=MS_e={number(var_error,4)}$. Hence $ICC={number(var_between,4)}/[{number(var_between,4)}+{number(var_error,4)}]={number(icc,4)}$. The model attributes about {number(100*icc,1)}% of its variance to differences among random {random_level} levels. This equation depends on a balanced one-way random-factor structure; crossed, nested, repeated, or unbalanced designs can require different components and denominators."))
    exercises.append("".join(ex_group)); solutions.append("".join(so_group))

    ex_group = [group_heading(10, "Repeated Measures, Sphericity, and Greenhouse-Geisser Correction")]
    so_group = [group_heading(10, "Repeated Measures, Sphericity, and Greenhouse-Geisser Correction")]
    for i,(title,diffvars,ss_condition,ss_person,ss_error,epsilon) in enumerate(REPEATED_CASES,1):
        df_condition=2; df_person=11; df_error=22; k=3
        ms_condition=ss_condition/df_condition; ms_person=ss_person/df_person; ms_error=ss_error/df_error; f_value=ms_condition/ms_error
        corrected_condition=epsilon*df_condition; corrected_error=epsilon*df_error
        person_var=(ms_person-ms_error)/k; icc=person_var/(person_var+ms_error)
        ratio=max(diffvars)/min(diffvars); plausible=ratio < 1.35
        marginal_variance=max(diffvars)+12
        correlations=tuple(1-difference/(2*marginal_variance) for difference in diffvars)
        moment_rows=(
            ("Variance at condition 1",number(marginal_variance,4)),
            ("Variance at condition 2",number(marginal_variance,4)),
            ("Variance at condition 3",number(marginal_variance,4)),
            ("Correlation 1 with 2",number(correlations[0],4)),
            ("Correlation 1 with 3",number(correlations[1],4)),
            ("Correlation 2 with 3",number(correlations[2],4)),
        )
        condition_p=f_upper_p(f_value,df_condition,df_error)
        person_f=ms_person/ms_error
        person_p=f_upper_p(person_f,df_person,df_error)
        corrected_p=f_upper_p(f_value,corrected_condition,corrected_error)
        ex_group.append(task(8,10,i,title,f"Twelve people are measured under three conditions. The sample variances and correlations are:\n\n{markdown_table(('Summary quantity','Value'),moment_rows)}\n\nThe repeated-measures table provides $SS_{{condition}}={ss_condition}$, $SS_{{person}}={ss_person}$, and $SS_e={ss_error}$ with degrees of freedom 2, 11, and 22. A Greenhouse-Geisser estimate is $\\widehat{{\\varepsilon}}={number(epsilon,2)}$. (a) Use $s_{{j-k}}^2=s_j^2+s_k^2-2r_{{jk}}s_js_k$ to calculate the three pairwise difference-score variances. Explain what sphericity asks and assess the pattern descriptively. (b) State the null hypotheses for the condition effect and person variation. Complete the three mean squares, calculate both $F_{{condition}}$ and $F_{{person}}$, obtain their upper-tail p-values, and interpret both decisions. (c) Estimate the person variance component and ICC. (d) Calculate the Greenhouse-Geisser-corrected condition and error degrees of freedom and the corrected p-value. (e) Explain what the correction changes, what remains unchanged, and why repeated rows do not become independent."))
        so_group.append(task(8,10,i,title,f"(a) Because all three marginal variances are {number(marginal_variance,4)}, each standard deviation is $\\sqrt{{{number(marginal_variance,4)}}}$. Substitution gives difference-score variances approximately ({vector(diffvars)}); the correlations were displayed to four decimals, so tiny reconstruction differences are rounding only. Sphericity asks whether the population variances of every pairwise condition difference are equal. The reconstructed values range from {min(diffvars)} to {max(diffvars)}, with largest-to-smallest ratio {number(ratio,4)}. This pattern is {'fairly similar and offers descriptive reassurance, although it does not prove sphericity' if plausible else 'noticeably unequal and warns that the uncorrected reference may be unreliable'}. (b) For conditions, $H_0:\\mu_1=\\mu_2=\\mu_3$; the alternative is that at least two condition means differ. For people, the random-person null is $H_0:\\sigma_{{person}}^2=0$ against positive between-person variation. The mean squares are $MS_{{condition}}={ss_condition}/2={number(ms_condition,4)}$, $MS_{{person}}={ss_person}/11={number(ms_person,4)}$, and $MS_e={ss_error}/22={number(ms_error,4)}$. Thus $F_{{condition}}={number(f_value,4)}$ with p-value {number(condition_p,4)}, and $F_{{person}}={number(ms_person,4)}/{number(ms_error,4)}={number(person_f,4)}$ with p-value {number(person_p,4)}. The condition test {'rejects' if condition_p < .05 else 'does not reject'} equal means at 5%; the person test {'supports' if person_p < .05 else 'does not provide sufficient evidence for'} between-person variation at 5%. (c) $\\widehat{{\\sigma}}_{{person}}^2=({number(ms_person,4)}-{number(ms_error,4)})/3={number(person_var,4)}$, so $ICC={number(person_var,4)}/[{number(person_var,4)}+{number(ms_error,4)}]={number(icc,4)}$. The ICC describes similarity among measurements from the same person under this model. (d) Greenhouse-Geisser gives $df_{{condition}}^*={number(epsilon,2)}(2)={number(corrected_condition,4)}$ and $df_e^*={number(epsilon,2)}(22)={number(corrected_error,4)}$. Using the observed $F={number(f_value,4)}$ with those reference degrees of freedom gives corrected p-value {number(corrected_p,4)}. (e) The correction changes the reference degrees of freedom and therefore the p-value or critical value. It does not change the observed $F$, the fitted means, or the dependence among repeated rows. Measurements from the same person remain linked."))
    exercises.append("".join(ex_group)); solutions.append("".join(so_group))

    return exercises, solutions


GROUP_TITLES = {
    "de": (
        "Die Frage der einfaktoriellen ANOVA",
        "Gruppenmittelwerte, Quadratsummenzerlegung und einfaktorieller F-Test",
        "Eine ANOVA-Tabelle rekonstruieren und das Design lesen",
        "Einfache paarweise und gepoolte komplexe Kontraste",
        "Alle paarweisen Vergleiche und Bonferroni-Schutz",
        "Eine Vergleichsfamilie vor der Ergebnissichtung festlegen",
        "Ein vorab festgelegter Trendkontrast",
        "Zellmittelwerte, Randmittelwerte und Interaktion in einer zweifaktoriellen ANOVA",
        "Feste und zufällige Faktoren, Varianzkomponenten und ICC",
        "Messwiederholung, Sphärizität und Greenhouse-Geisser-Korrektur",
    ),
    "sq": (
        "Pyetja së cilës i përgjigjet ANOVA njëfaktoriale",
        "Mesataret e grupeve, ndarja e shumave të katrorëve dhe testi F njëfaktorial",
        "Rindërtimi i tabelës ANOVA dhe leximi i dizajnit",
        "Kontrastet e thjeshta dyshe dhe kontrastet komplekse të bashkuara",
        "Të gjitha krahasimet dyshe dhe mbrojtja Bonferroni",
        "Përcaktimi i familjes së krahasimeve para shqyrtimit të rezultateve",
        "Një kontrast prirjeje i përcaktuar paraprakisht",
        "Mesataret e qelizave, mesataret margjinale dhe ndërveprimi në ANOVA dyfaktoriale",
        "Faktorët fiksë e të rastësishëm, komponentët e variancës dhe ICC-ja",
        "Matjet e përsëritura, sfericiteti dhe korrigjimi Greenhouse-Geisser",
    ),
}


OMNIBUS_LOCALIZED = {
    "de": (
        ("Leseformate und Verständnis", "Verständniswert", "Leseformat", ("Druck", "Tablet", "Audio")),
        ("Museumsrouten und Besuchsdauer", "Besuchsdauer", "Routentyp", ("freie Route", "nummerierte Route", "geführte Route")),
        ("Lernorte und Konzentration", "Konzentrationswert", "üblicher Lernort", ("zu Hause", "Bibliothek", "Gemeinschaftsarbeitsraum")),
        ("Erinnerungspläne und Antwortverzögerung", "Antwortverzögerung", "Erinnerungsplan", ("keine Erinnerung", "eine Erinnerung", "drei Erinnerungen")),
        ("Archivoberflächen und Abrufgenauigkeit", "Abrufgenauigkeit", "Oberflächenversion", ("Standard", "kompakt", "geführt")),
        ("Verkehrsmittel und Pendelzeit", "Pendelzeit", "übliches Verkehrsmittel", ("zu Fuss", "öffentlicher Verkehr", "Auto")),
        ("Übungsroutinen und verzögerte Erinnerung", "Wert der verzögerten Erinnerung", "Übungsroutine", ("wiederholtes Lesen", "Selbsttest", "gemischtes Üben")),
        ("Workshop-Schwerpunkte und Selbstvertrauen", "Selbstvertrauenswert", "gewählter Workshop-Schwerpunkt", ("Methoden", "Schreiben", "Präsentieren")),
        ("Untertitelstile und Tutorialverständnis", "Verständniswert", "Untertitelstil", ("keine", "wortgetreu", "redigiert")),
        ("Quartiertypen und Parknutzung", "wöchentliche Parkbesuche", "Quartiertyp", ("zentral", "vorstädtisch", "ländlich")),
    ),
    "sq": (
        ("Formatet e leximit dhe të kuptuarit", "rezultati i të kuptuarit", "formati i leximit", ("tekst i shtypur", "tablet", "audio")),
        ("Rrugët në muze dhe kohëzgjatja e vizitës", "kohëzgjatja e vizitës", "lloji i rrugës", ("rrugë e lirë", "rrugë e numërtuar", "rrugë me udhërrëfyes")),
        ("Vendet e studimit dhe përqendrimi", "rezultati i përqendrimit", "vendi i zakonshëm i studimit", ("shtëpi", "bibliotekë", "hapësirë e përbashkët pune")),
        ("Oraret e kujtesave dhe vonesa e përgjigjes", "vonesa e përgjigjes", "orari i kujtesave", ("pa kujtesë", "një kujtesë", "tri kujtesa")),
        ("Ndërfaqet e arkivit dhe saktësia e gjetjes", "saktësia e gjetjes", "versioni i ndërfaqes", ("standard", "i përmbledhur", "i udhëzuar")),
        ("Mënyrat e udhëtimit dhe koha e vajtje-ardhjes", "koha e vajtje-ardhjes", "mënyra e zakonshme e udhëtimit", ("ecje", "transport publik", "makinë")),
        ("Rutinat e ushtrimit dhe rikujtimi i vonuar", "rezultati i rikujtimit të vonuar", "rutina e ushtrimit", ("rilexim", "vetëtestim", "ushtrim i përzier")),
        ("Drejtimet e seminarit dhe vetëbesimi", "rezultati i vetëbesimit", "drejtimi i zgjedhur i seminarit", ("metoda", "shkrim", "prezantim")),
        ("Stilet e titrave dhe të kuptuarit e tutorialit", "rezultati i të kuptuarit", "stili i titrave", ("pa titra", "fjalë për fjalë", "të redaktuar")),
        ("Llojet e lagjeve dhe përdorimi i parkut", "numri javor i vizitave në park", "lloji i lagjes", ("qendrore", "periferike", "rurale")),
    ),
}


RAW_GROUP_LOCALIZED = {
    "de": (
        ("Lernroutinen und Lernleistung", "Lernleistung", ("Referenz", "Planung", "Abruf")),
        ("Leselayouts und Lesegeschwindigkeit", "Lesegeschwindigkeit", ("schmal", "Standard", "breit")),
        ("Archivhinweise und korrekte Datensätze", "Anzahl korrekt abgerufener Datensätze", ("keine", "Checkliste", "Beispiele")),
        ("Museumskarten und Routensicherheit", "Routensicherheitswert", ("Text", "Symbole", "kombiniert")),
        ("Zeitpunkt der Erinnerung und Abschluss", "Abschlusswert", ("Morgen", "Mittag", "Abend")),
        ("Notizformate und Erkennen von Argumenten", "Wert für das Erkennen von Argumenten", ("frei", "Gliederung", "Matrix")),
        ("Zeitliche Verteilung des Übens und Erinnerung", "Erinnerungswert", ("geballt", "zwei Sitzungen", "vier Sitzungen")),
        ("Geräuschkulisse und Konzentration", "Konzentrationswert", ("Ruhe", "Umgebungsgeräusche", "Musik")),
        ("Routenanweisungen und Fehler", "Navigationsfehlerwert", ("Text", "Karte", "Text und Karte")),
        ("Zeitpunkt der Rückmeldung und Überarbeitungsqualität", "Überarbeitungsqualitätswert", ("sofort", "nächster Tag", "eine Woche")),
    ),
    "sq": (
        ("Rutinat e studimit dhe rezultati i të nxënit", "rezultati i të nxënit", ("Referencë", "Planifikim", "Rikujtim")),
        ("Paraqitjet e tekstit dhe shpejtësia e leximit", "shpejtësia e leximit", ("i ngushtë", "standard", "i gjerë")),
        ("Udhëzimet e arkivit dhe regjistrimet e sakta", "numri i regjistrimeve të gjetura saktë", ("asnjë", "listë kontrolli", "shembuj")),
        ("Hartat e muzeut dhe siguria për rrugën", "rezultati i sigurisë për rrugën", ("tekst", "ikona", "të kombinuara")),
        ("Koha e kujtesës dhe përfundimi", "rezultati i përfundimit", ("mëngjes", "mesditë", "mbrëmje")),
        ("Formatet e shënimeve dhe dallimi i argumentit", "rezultati i dallimit të argumentit", ("i lirë", "skicë", "matricë")),
        ("Shpërndarja e ushtrimit në kohë dhe rikujtimi", "rezultati i rikujtimit", ("i përqendruar", "dy seanca", "katër seanca")),
        ("Mjediset zanore dhe përqendrimi", "rezultati i përqendrimit", ("qetësi", "zhurmë ambienti", "muzikë")),
        ("Udhëzimet e rrugës dhe gabimet", "rezultati i gabimeve të navigimit", ("tekst", "hartë", "tekst dhe hartë")),
        ("Koha e komenteve kthyese dhe cilësia e rishikimit", "rezultati i cilësisë së rishikimit", ("menjëherë", "të nesërmen", "pas një jave")),
    ),
}


CASE_TITLES = {
    "de": {
        3: ("Randomisierte Lesehinweise", "Beobachtete Verkehrsmittel beim Pendeln", "Randomisierte Archivoberflächen", "Selbst gewählte Workshop-Schwerpunkte", "Randomisierte Erinnerungspläne", "Beobachtete Quartiertypen", "Randomisierte Untertitelstile", "Gewählte Lernorte", "Randomisierte Routenkarten", "Beobachtete Beschäftigungssektoren"),
        4: ("Vier Lernroutinen", "Vier Leselayouts", "Vier Archivhinweise", "Vier Museumsrouten", "Vier Erinnerungspläne", "Vier Notizvorlagen", "Vier Übungsintervalle", "Vier Geräuschkulissen", "Vier Navigationshilfen", "Vier Rückmeldungspläne"),
        6: ("Lernroutinen", "Leselayouts", "Archivhinweise", "Museumsrouten", "Erinnerungspläne", "Notizvorlagen", "Übungsintervalle", "Geräuschkulissen", "Navigationshilfen", "Rückmeldungspläne"),
        7: ("Übungssitzungen und Erinnerung", "Intensität der Erinnerungen und Antwort", "Leseunterstützung und Verständnis", "Archivbeispiele und Genauigkeit", "Routenübung und Selbstvertrauen", "Notizstruktur und logisches Denken", "Häufigkeit der Rückmeldung und Überarbeitung", "Umgebungsgeräusche und Konzentration", "Navigationsunterstützung und Fehler", "Verzögerung der Rückmeldung und Behalten"),
        10: ("Lesen zu drei Zeitpunkten", "Konzentration unter drei Geräuschkulissen", "Erinnerung nach drei Verzögerungen", "Navigation in drei Routendurchgängen", "Selbstvertrauen zu drei Kurszeitpunkten", "Genauigkeit mit drei Oberflächen", "Antwortzeit bei drei Erinnerungen", "Verständnis mit drei Formaten", "Überarbeitungsqualität bei drei Entwürfen", "Suchkompetenz zu drei Übungszeitpunkten"),
    },
    "sq": {
        3: ("Udhëzime leximi të caktuara rastësisht", "Mënyra të vrojtuara udhëtimi", "Ndërfaqe arkivi të caktuara rastësisht", "Drejtime seminari të zgjedhura vetë", "Oraret e kujtesave të caktuara rastësisht", "Lloje lagjesh të vrojtuara", "Stile titrash të caktuara rastësisht", "Vende studimi të zgjedhura", "Harta rrugësh të caktuara rastësisht", "Sektorë punësimi të vrojtuar"),
        4: ("Katër rutina studimi", "Katër paraqitje teksti", "Katër udhëzime arkivi", "Katër rrugë muzeu", "Katër orare kujtesash", "Katër modele shënimesh", "Katër intervale ushtrimi", "Katër mjedise zanore", "Katër ndihma navigimi", "Katër orare komentesh kthyese"),
        6: ("Rutinat e studimit", "Paraqitjet e tekstit", "Udhëzimet e arkivit", "Rrugët në muze", "Oraret e kujtesave", "Modelet e shënimeve", "Intervalet e ushtrimit", "Mjediset zanore", "Ndihmat e navigimit", "Oraret e komenteve kthyese"),
        7: ("Seancat e ushtrimit dhe rikujtimi", "Intensiteti i kujtesave dhe përgjigjja", "Udhëzimi në lexim dhe të kuptuarit", "Shembujt në arkiv dhe saktësia", "Ushtrimi i rrugës dhe vetëbesimi", "Struktura e shënimeve dhe arsyetimi", "Shpeshtësia e komenteve kthyese dhe rishikimi", "Zhurma e ambientit dhe përqendrimi", "Mbështetja e navigimit dhe gabimet", "Vonesa e komenteve kthyese dhe mbajtja mend"),
        10: ("Leximi në tri kohë matjeje", "Përqendrimi në tri mjedise zanore", "Rikujtimi pas tri vonesave", "Navigimi në tri prova rruge", "Vetëbesimi në tri pika të kursit", "Saktësia me tri ndërfaqe", "Koha e përgjigjes me tri kujtesa", "Të kuptuarit me tri formate", "Cilësia e rishikimit në tri drafte", "Aftësia e kërkimit në tri pika ushtrimi"),
    },
}


FACTORIAL_LOCALIZED = {
    "de": (
        ("Untertitel und Üben", "Untertitel", "Üben"), ("Karte und Routenübung", "Karte", "Routenübung"),
        ("Ruhiger Raum und Checkliste", "ruhiger Raum", "Checkliste"), ("Hinweis und Rückmeldung", "Hinweis", "Rückmeldung"),
        ("Symbole und Beispiele", "Symbole", "Beispiele"), ("Planung und Selbsttest", "Planung", "Selbsttest"),
        ("Beleuchtung und Hintergrundgeräusche", "helle Beleuchtung", "Geräuschkulisse"), ("Orientierung und Beschilderung", "Orientierung", "Beschilderung"),
        ("Zeitliche Verteilung und Abrufhinweise", "zeitliche Verteilung", "Abrufhinweise"), ("Vorlage und Peer-Review", "Vorlage", "Peer-Review"),
    ),
    "sq": (
        ("Titrat dhe ushtrimi", "titrat", "ushtrimi"), ("Harta dhe ushtrimi i rrugës", "harta", "ushtrimi i rrugës"),
        ("Dhoma e qetë dhe lista e kontrollit", "dhoma e qetë", "lista e kontrollit"), ("Udhëzimi dhe komentet kthyese", "udhëzimi", "komentet kthyese"),
        ("Ikonat dhe shembujt", "ikonat", "shembujt"), ("Planifikimi dhe vetëtestimi", "planifikimi", "vetëtestimi"),
        ("Ndriçimi dhe zhurma e sfondit", "ndriçimi i fortë", "zhurma"), ("Orientimi dhe shenjat", "orientimi", "shenjat"),
        ("Shpërndarja në kohë dhe shenjat e rikujtimit", "shpërndarja në kohë", "shenjat e rikujtimit"), ("Modeli dhe shqyrtimi nga bashkëmoshatarët", "modeli", "shqyrtimi nga bashkëmoshatarët"),
    ),
}


RANDOM_FACTOR_LOCALIZED = {
    "de": (
        ("Bibliotheken aus einer regionalen Population", "Bibliothek", "drei bewusst ausgewählte Oberflächendesigns"),
        ("Schulen aus einem Bezirk", "Schule", "zwei benannte Unterrichtsprogramme"),
        ("Befragende Personen aus einem geschulten Pool", "befragende Person", "drei feste Fragebogenversionen"),
        ("Quartiere aus einer Stadt", "Quartier", "zwei ausgewählte Informationsbotschaften"),
        ("Museumsführende aus der Personalliste", "Führungsperson", "vier feste Führungsskripte"),
        ("Archivboxen aus einer Sammlung", "Archivbox", "drei ausgewählte Scaneinstellungen"),
        ("Tutoriumsgruppen aus einem Studienprogramm", "Tutoriumsgruppe", "zwei feste Übungspläne"),
        ("Routen aus einem Verkehrsnetz", "Route", "drei ausgewählte Beschilderungsdesigns"),
        ("Workshops aus einer jährlichen Reihe", "Workshop", "zwei benannte Moderationsformate"),
        ("Tage aus einem Semester", "Tag", "drei feste Erinnerungsnachrichten"),
    ),
    "sq": (
        ("Biblioteka të kampionuara nga një popullatë rajonale", "biblioteka", "tri dizajne të zgjedhura qëllimisht të ndërfaqes"),
        ("Shkolla të kampionuara nga një distrikt", "shkolla", "dy programe mësimore të emërtuara"),
        ("Intervistues të kampionuar nga një grup i trajnuar", "intervistuesi", "tri versione fikse të pyetësorit"),
        ("Lagje të kampionuara nga një qytet", "lagjja", "dy mesazhe të zgjedhura informuese"),
        ("Udhërrëfyes muzeu të kampionuar nga lista e stafit", "udhërrëfyesi i muzeut", "katër tekste fikse të vizitës"),
        ("Kuti arkivi të kampionuara nga një koleksion", "kutia e arkivit", "tri cilësime të zgjedhura skanimi"),
        ("Grupe tutoriali të kampionuara nga një program", "grupi i tutorialit", "dy orare fikse ushtrimi"),
        ("Rrugë të kampionuara nga një rrjet transporti", "rruga", "tri dizajne të zgjedhura shenjash"),
        ("Seminare të kampionuara nga një seri vjetore", "seminari", "dy formate të emërtuara lehtësimi"),
        ("Ditë të kampionuara nga një semestër", "dita", "tri mesazhe fikse kujtese"),
    ),
}


UNITS = {
    "de": {"points":"Punkte", "minutes":"Minuten", "hours":"Stunden", "visits":"Besuche", "words per minute above baseline":"Wörter pro Minute über dem Ausgangswert", "records":"Datensätze", "errors":"Fehler"},
    "sq": {"points":"pikë", "minutes":"minuta", "hours":"orë", "visits":"vizita", "words per minute above baseline":"fjalë në minutë mbi nivelin fillestar", "records":"regjistrime", "errors":"gabime"},
}


DE_MEASUREMENT_PHRASES = {
    "points": "in Punkten",
    "minutes": "in Minuten",
    "hours": "in Stunden",
    "visits": "als Anzahl von Besuchen",
    "words per minute above baseline": "in Wörtern pro Minute über dem Ausgangswert",
    "records": "als Anzahl von Datensätzen",
    "errors": "als Anzahl von Fehlern",
}


def render_localized(locale: str) -> tuple[list[str], list[str]]:
    """Render the reviewed de-CH or Albanian adaptation from canonical values."""

    if locale == "en":
        return render_english()
    if locale not in ("de", "sq"):
        raise ValueError(f"unsupported locale: {locale}")
    titles=GROUP_TITLES[locale];units=UNITS[locale]
    exercises: list[str]=[];solutions: list[str]=[]

    exg=[group_heading(1,titles[0])];sog=[group_heading(1,titles[0])]
    for i,(_title,_outcome,_factor,_levels,unit,randomized) in enumerate(OMNIBUS_CASES,1):
        title,outcome,factor,levels=OMNIBUS_LOCALIZED[locale][i-1];u=units[unit]
        labels=f"{', '.join(levels[:-1])} {'und' if locale == 'de' else 'dhe'} {levels[-1]}"
        if locale=="de":
            assignment="Die Fälle wurden den Faktorstufen zufällig zugewiesen." if randomized else "Der Faktor wurde ohne zufällige Zuweisung beobachtet."
            causal="Da die Fälle zufällig zugewiesen wurden, kann eine gut durchgeführte Studie für diese Bedingungen eine kausale Interpretation stützen, soweit Design und Annahmen glaubwürdig sind." if randomized else "Da die Gruppen beobachtet und nicht zufällig zugewiesen wurden, beschreibt ein Unterschied einen Zusammenhang und identifiziert für sich allein keinen kausalen Effekt."
            measurement=DE_MEASUREMENT_PHRASES[unit]
            prompt=rf"Eine Studie erfasst das quantitative Ergebnis «{outcome}». Die Werte werden {measurement} angegeben. Sie vergleicht die Stufen {labels} des kategorialen Faktors «{factor}». {assignment} (a) Bestimme das quantitative Ergebnis, den Faktor und seine Stufen. (b) Formuliere Null- und Alternativhypothese der einfaktoriellen ANOVA in Worten und Symbolen. (c) Erkläre, weshalb ein Globaltest dem Beginn mit drei unkorrigierten paarweisen Tests vorzuziehen ist. (d) Formuliere, was ein signifikanter Globaltest zeigen würde und was nicht."
            solution=rf"Das quantitative Ergebnis ist «{outcome}»; seine Werte werden {measurement} angegeben. Der Faktor ist «{factor}» mit den Stufen {labels}. Bezeichne die Populationsmittelwerte mit $\mu_1$, $\mu_2$ und $\mu_3$. Die Nullhypothese ist $H_0:\mu_1=\mu_2=\mu_3$. Die Alternative besagt, dass sich mindestens zwei Mittelwerte unterscheiden. Sie besagt nicht, dass jedes Paar verschieden ist. Drei getrennte Tests würden mehrere Gelegenheiten für einen Fehler vom Typ I schaffen, während der globale $F$-Test zuerst die eine übergeordnete Frage stellt. Ein signifikantes Ergebnis liefert Evidenz gegen die Gleichheit aller drei Populationsmittelwerte, zeigt aber nicht, welche Paare verschieden sind. {causal}"
        else:
            assignment="Rastet u caktuan rastësisht në nivelet e faktorit." if randomized else "Faktori u vrojtua pa caktim të rastësishëm."
            causal="Meqë rastet u caktuan rastësisht, një studim i zbatuar mirë mund të mbështetë interpretim shkakor për këto kushte, në varësi të dizajnit dhe supozimeve." if randomized else "Meqë grupet u vrojtuan dhe nuk u caktuan rastësisht, dallimi përshkruan lidhje dhe nuk identifikon vetvetiu efekt shkakor."
            prompt=rf"Një studim mat ndryshoren sasiore «{outcome}». Njësia matëse është {u}. Studimi krahason nivelet {labels} të faktorit kategorik «{factor}». {assignment} (a) Përcakto rezultatin sasior, faktorin dhe nivelet e tij. (b) Shkruaj me fjalë dhe simbole hipotezën zero dhe hipotezën alternative të ANOVA-s njëfaktoriale. (c) Shpjego pse një test i përgjithshëm është më i përshtatshëm se fillimi me tri teste dyshe të pakorrigjuara. (d) Thuaj çfarë do të tregonte dhe çfarë nuk mund të tregonte një rezultat domethënës i testit të përgjithshëm."
            solution=rf"Rezultati sasior është «{outcome}»; njësia matëse është {u}. Faktori është «{factor}» me nivelet {labels}. Shënoji mesataret e popullatave me $\mu_1$, $\mu_2$ dhe $\mu_3$. Hipoteza zero është $H_0:\mu_1=\mu_2=\mu_3$. Alternativa thotë se të paktën dy mesatare ndryshojnë. Nuk thotë se ndryshon çdo çift. Fillimi me tri teste të veçanta do të krijonte disa mundësi për gabim të llojit I, ndërsa testi i përgjithshëm $F$ e bën fillimisht pyetjen e vetme globale. Rezultati domethënës do të jepte evidencë kundër barazisë së të tria mesatareve të popullatave, por nuk do të tregonte cilat çifte ndryshojnë. {causal}"
        exg.append(task(8,1,i,title,prompt));sog.append(task(8,1,i,title,solution))
    exercises.append("".join(exg));solutions.append("".join(sog))

    exg=[group_heading(2,titles[1])];sog=[group_heading(2,titles[1])];offsets=(-3,-1,1,3)
    for i,(_title,_outcome,_labels,means,unit) in enumerate(RAW_GROUP_CASES,1):
        title,outcome,group_labels=RAW_GROUP_LOCALIZED[locale][i-1];u=units[unit];groups=[[mean+offset for offset in offsets] for mean in means];rows="\n".join(f"| {label} | {vector(tuple(values))} |" for label,values in zip(group_labels,groups));flat=[v for values in groups for v in values];grand=sum(flat)/len(flat);ss_factor=sum(len(values)*(sum(values)/len(values)-grand)**2 for values in groups);ss_error=sum(sum((v-sum(values)/len(values))**2 for v in values) for values in groups);ss_total=sum((v-grand)**2 for v in flat);ms_factor=ss_factor/2;ms_error=ss_error/9;f_value=ms_factor/ms_error;reject=f_value>4.26
        if locale=="de":
            measurement=DE_MEASUREMENT_PHRASES[unit]
            prompt=f"Eine konstruierte Studie erfasst das Ergebnis «{outcome}». Die Werte werden {measurement} angegeben.\n\n| Gruppe | Beobachtungen |\n|---|---|\n{rows}\n\n(a) Berechne die drei Gruppenmittelwerte und den Gesamtmittelwert. (b) Berechne $SS_A$, $SS_e$ und $SS_{{total}}$. (c) Überprüfe $SS_{{total}}=SS_A+SS_e$. (d) Vervollständige Freiheitsgrade, mittlere Quadratsummen und $F$-Statistik. (e) Vergleiche das Ergebnis auf dem 5%-Niveau mit dem angegebenen kritischen Wert $F_{{2,9}}=4.26$ und interpretiere die Entscheidung."
            solution=rf"Die Gruppenmittelwerte sind {vector(means)}, der Gesamtmittelwert ist {number(grand,4)} {u}. Die Berechnung zwischen den Gruppen ergibt $SS_A=\sum_i n_i(\bar y_i-\bar y)^2={number(ss_factor,4)}$. Die Summe quadrierter Abweichungen innerhalb der drei Gruppen ergibt $SS_e={number(ss_error,4)}$. Um den Gesamtmittelwert gilt $SS_{{total}}={number(ss_total,4)}$ und {number(ss_total,4)} = {number(ss_factor,4)} + {number(ss_error,4)}; die Zerlegung stimmt. Die Freiheitsgrade sind $df_A=3-1=2$, $df_e=12-3=9$ und $df_{{total}}=11$. Somit $MS_A={number(ss_factor,4)}/2={number(ms_factor,4)}$, $MS_e={number(ss_error,4)}/9={number(ms_error,4)}$ und $F={number(ms_factor,4)}/{number(ms_error,4)}={number(f_value,4)}$. Weil {number(f_value,4)} {'grösser' if reject else 'nicht grösser'} als 4.26 ist, {'lehnen wir' if reject else 'lehnen wir'} die Nullhypothese gleicher Mittelwerte auf dem 5%-Niveau {'ab' if reject else 'nicht ab'}. Die Entscheidung betrifft das globale Mittelwertmuster und nicht jedes einzelne Paar."
        else:
            prompt=f"Një studim i krijuar mat ndryshoren «{outcome}». Njësia matëse është {u}.\n\n| Grupi | Vrojtimet |\n|---|---|\n{rows}\n\n(a) Llogarit tri mesataret e grupeve dhe mesataren e përgjithshme. (b) Llogarit $SS_A$, $SS_e$ dhe $SS_{{total}}$. (c) Verifiko $SS_{{total}}=SS_A+SS_e$. (d) Plotëso shkallët e lirisë, katrorët mesatarë dhe statistikën $F$. (e) Në nivelin 5%, krahaso rezultatin me vlerën kritike të dhënë $F_{{2,9}}=4.26$ dhe interpreto vendimin."
            solution=rf"Mesataret e grupeve janë {vector(means)}, ndërsa mesatarja e përgjithshme është {number(grand,4)} {u}. Llogaritja mes grupeve jep $SS_A=\sum_i n_i(\bar y_i-\bar y)^2={number(ss_factor,4)}$. Mbledhja e devijimeve në katror brenda tri grupeve jep $SS_e={number(ss_error,4)}$. Rreth mesatares së përgjithshme, $SS_{{total}}={number(ss_total,4)}$ dhe {number(ss_total,4)} = {number(ss_factor,4)} + {number(ss_error,4)}, prandaj ndarja përputhet. Shkallët e lirisë janë $df_A=3-1=2$, $df_e=12-3=9$ dhe $df_{{total}}=11$. Kështu $MS_A={number(ss_factor,4)}/2={number(ms_factor,4)}$, $MS_e={number(ss_error,4)}/9={number(ms_error,4)}$ dhe $F={number(ms_factor,4)}/{number(ms_error,4)}={number(f_value,4)}$. Meqë {number(f_value,4)} {'është më e madhe' if reject else 'nuk është më e madhe'} se 4.26, {'e refuzojmë' if reject else 'nuk e refuzojmë'} hipotezën zero të mesatareve të barabarta në nivelin 5%. Vendimi lidhet me modelin global të mesatareve, jo me çdo çift veçmas."
        exg.append(task(8,2,i,title,prompt));sog.append(task(8,2,i,title,solution))
    exercises.append("".join(exg));solutions.append("".join(sog))

    exg=[group_heading(3,titles[2])];sog=[group_heading(3,titles[2])]
    for i,(_title,ns,ss_factor,ss_error,critical,randomized) in enumerate(TABLE_CASES,1):
        title=CASE_TITLES[locale][3][i-1];k=len(ns);total_n=sum(ns);df_factor=k-1;df_error=total_n-k;df_total=total_n-1;ss_total=ss_factor+ss_error;ms_factor=ss_factor/df_factor;ms_error=ss_error/df_error;f_value=ms_factor/ms_error;balanced=len(set(ns))==1;reject=f_value>critical
        if locale=="de":
            prompt=rf"Eine {'randomisierte' if randomized else 'nicht randomisierte beobachtende'} Studie hat Gruppengrössen $n_i=({', '.join(str(n) for n in ns)})$. Ihre unvollständige ANOVA-Tabelle berichtet $SS_A={ss_factor}$ und $SS_e={ss_error}$. (a) Formuliere die Hypothesen gleicher Mittelwerte. (b) Vervollständige $SS_{{total}}$ und alle drei Freiheitsgrade. (c) Berechne beide mittleren Quadratsummen und $F$. (d) Vergleiche $F$ mit dem angegebenen kritischen 5%-Wert {number(critical,2)}. (e) Bestimme, ob das Design balanciert ist, und erkläre die Grenze eines kausalen Schlusses."
            design="Die gleichen Gruppengrössen machen das Design balanciert." if balanced else "Die ungleichen Gruppengrössen machen das Design unbalanciert.";causal="Zufällige Zuweisung kann für die zugewiesenen Bedingungen eine kausale Interpretation stützen, wenn Umsetzung und Modellannahmen glaubwürdig sind." if randomized else "Ohne zufällige Zuweisung beschreibt das Ergebnis einen Gruppenzusammenhang und kann bestehende Gruppenunterschiede nicht selbst ausschliessen."
            solution=rf"Für $k={k}$ Gruppen gilt $H_0:\mu_1=\cdots=\mu_{k}$; die Alternative besagt, dass sich mindestens zwei Mittelwerte unterscheiden. Die Gesamtquadratsumme ist {ss_factor}+{ss_error}={ss_total}. Bei $N={total_n}$ sind die Freiheitsgrade $df_A={k}-1={df_factor}$, $df_e={total_n}-{k}={df_error}$ und $df_{{total}}={total_n}-1={df_total}$. Dann $MS_A={ss_factor}/{df_factor}={number(ms_factor,4)}$, $MS_e={ss_error}/{df_error}={number(ms_error,4)}$ und $F={number(f_value,4)}$. Weil {number(f_value,4)} {'grösser' if reject else 'nicht grösser'} als {number(critical,2)} ist, {'lehnen wir' if reject else 'lehnen wir'} die Nullhypothese auf dem 5%-Niveau {'ab' if reject else 'nicht ab'}. {design} {causal}"
        else:
            prompt=rf"Një studim {'i rastësuar' if randomized else 'vrojtues jo i rastësuar'} ka madhësitë e grupeve $n_i=({', '.join(str(n) for n in ns)})$. Tabela e paplotë ANOVA raporton $SS_A={ss_factor}$ dhe $SS_e={ss_error}$. (a) Shkruaj hipotezat e mesatareve të barabarta. (b) Plotëso $SS_{{total}}$ dhe të tria shkallët e lirisë. (c) Llogarit të dy katrorët mesatarë dhe $F$. (d) Krahaso $F$ me vlerën kritike 5% të dhënë {number(critical,2)}. (e) Përcakto nëse dizajni është i balancuar dhe shpjego kufirin e përfundimit shkakor."
            design="Madhësitë e barabarta të grupeve e bëjnë dizajnin të balancuar." if balanced else "Madhësitë e pabarabarta të grupeve e bëjnë dizajnin të pabalancuar.";causal="Caktimi i rastësishëm mund të mbështetë interpretim shkakor për kushtet e caktuara nëse zbatimi dhe supozimet e modelit janë të besueshme." if randomized else "Pa caktim të rastësishëm, rezultati përshkruan lidhje mes grupeve dhe nuk mund t'i përjashtojë vetë dallimet që ekzistonin më parë."
            solution=rf"Për $k={k}$ grupe, $H_0:\mu_1=\cdots=\mu_{k}$; alternativa thotë se të paktën dy mesatare ndryshojnë. Shuma totale e katrorëve është {ss_factor}+{ss_error}={ss_total}. Me $N={total_n}$, shkallët e lirisë janë $df_A={k}-1={df_factor}$, $df_e={total_n}-{k}={df_error}$ dhe $df_{{total}}={total_n}-1={df_total}$. Pastaj $MS_A={ss_factor}/{df_factor}={number(ms_factor,4)}$, $MS_e={ss_error}/{df_error}={number(ms_error,4)}$ dhe $F={number(f_value,4)}$. Meqë {number(f_value,4)} {'është më e madhe' if reject else 'nuk është më e madhe'} se {number(critical,2)}, {'e refuzojmë' if reject else 'nuk e refuzojmë'} hipotezën zero në nivelin 5%. {design} {causal}"
        exg.append(task(8,3,i,title,prompt));sog.append(task(8,3,i,title,solution))
    exercises.append("".join(exg));solutions.append("".join(sog))

    exg=[group_heading(4,titles[3])];sog=[group_heading(4,titles[3])];simple=(-1,1,0,0);complex_weights=(-1,-1,1,1)
    for i,(_title,means,n,mse) in enumerate(CONTRAST_CASES,1):
        title=CASE_TITLES[locale][4][i-1];d_simple=sum(c*m for c,m in zip(simple,means));d_complex=sum(c*m for c,m in zip(complex_weights,means));se_simple=math.sqrt(mse/n*sum(c*c for c in simple));se_complex=math.sqrt(mse/n*sum(c*c for c in complex_weights));t_simple=d_simple/se_simple;t_complex=d_complex/se_complex
        if locale=="de":
            prompt=rf"Vier balancierte Gruppen haben die Mittelwerte ({vector(means)}), je $n={n}$ Beobachtungen und die gepoolte mittlere Fehlerquadratsumme $MS_e={mse}$. (a) Überprüfe, dass $c=(-1,1,0,0)$ ein Kontrast ist, und berechne Schätzung, Standardfehler und $t$-Statistik. (b) Wiederhole dies für den gepoolten Vergleich $c=(-1,-1,1,1)$. (c) Übersetze beide Gewichtsmuster in einfache Fragen. (d) Erkläre, weshalb die grössere numerische Kontrastschätzung nicht automatisch das stärkere standardisierte Ergebnis ist."
            solution=rf"Beide Gewichtsvektoren summieren sich zu null und sind daher gültige Kontraste. Der einfache Kontrast vergleicht Gruppe 2 mit Gruppe 1: $D_s={number(d_simple,4)}$. Sein Standardfehler ist $SE_s=\sqrt{{({mse}/{n})[(-1)^2+1^2]}}={number(se_simple,4)}$; damit $t_s={number(d_simple,4)}/{number(se_simple,4)}={number(t_simple,4)}$. Der komplexe Kontrast vergleicht die Summe der Gruppen 3 und 4 mit der Summe der Gruppen 1 und 2: $D_c={number(d_complex,4)}$. Sein Standardfehler ist $SE_c=\sqrt{{({mse}/{n})[(-1)^2+(-1)^2+1^2+1^2]}}={number(se_complex,4)}$; somit $t_c={number(t_complex,4)}$. Eine Division jedes komplexen Gewichts durch 2 würde die Differenz zwischen den zwei gepoolten Mittelwerten ausdrücken und die $t$-Statistik unverändert lassen, weil Schätzung und Standardfehler gemeinsam skaliert werden. Rohe Kontrastschätzungen verwenden bei verschiedenen Gewichten verschiedene Skalen. Vergleiche deshalb die formulierte Frage und die standardisierte Statistik, nicht nur den Betrag."
        else:
            prompt=rf"Katër grupe të balancuara kanë mesataret ({vector(means)}), $n={n}$ në secilin grup dhe katrorin mesatar të përbashkët të gabimit $MS_e={mse}$. (a) Verifiko se $c=(-1,1,0,0)$ është kontrast dhe llogarit vlerësimin, gabimin standard dhe statistikën $t$. (b) Përsërite për krahasimin e bashkuar $c=(-1,-1,1,1)$. (c) Shndërroji të dy modelet e peshave në pyetje me fjalë të thjeshta. (d) Shpjego pse vlerësimi numerik më i madh i kontrastit nuk është automatikisht rezultati më i fortë i standardizuar."
            solution=rf"Shuma e secilit vektor të peshave është zero, prandaj të dy janë kontraste të vlefshme. Kontrasti i thjeshtë krahason Grupin 2 me Grupin 1: $D_s={number(d_simple,4)}$. Gabimi standard është $SE_s=\sqrt{{({mse}/{n})[(-1)^2+1^2]}}={number(se_simple,4)}$, duke dhënë $t_s={number(d_simple,4)}/{number(se_simple,4)}={number(t_simple,4)}$. Kontrasti kompleks krahason shumën e Grupeve 3 dhe 4 me shumën e Grupeve 1 dhe 2: $D_c={number(d_complex,4)}$. Gabimi standard është $SE_c=\sqrt{{({mse}/{n})[(-1)^2+(-1)^2+1^2+1^2]}}={number(se_complex,4)}$, prandaj $t_c={number(t_complex,4)}$. Pjesëtimi i çdo peshe komplekse me 2 do ta shprehte dallimin mes dy mesatareve të bashkuara dhe do ta linte statistikën $t$ të pandryshuar, sepse vlerësimi dhe gabimi standard shkallëzohen së bashku. Vlerësimet e papërpunuara të kontrasteve përdorin shkallë të ndryshme kur ndryshojnë peshat, prandaj krahaso pyetjen e deklaruar dhe statistikën e standardizuar, jo vetëm madhësinë."
        exg.append(task(8,4,i,title,prompt));sog.append(task(8,4,i,title,solution))
    exercises.append("".join(exg));solutions.append("".join(sog))

    exg=[group_heading(5,titles[4])];sog=[group_heading(5,titles[4])]
    for i,k in enumerate(PAIRWISE_LEVELS,1):
        comparisons=k*(k-1)//2;threshold=.05/comparisons;independent_risk=1-(1-.05)**comparisons;title=(f"Alle Paare zwischen {k} Stufen" if locale=="de" else f"Të gjitha çiftet mes {k} niveleve")
        if locale=="de":
            prompt=rf"Eine Analyse soll jeden paarweisen Vergleich zwischen $k={k}$ Faktorstufen durchführen und die familienweise Fehlerrate vom Typ I auf höchstens 0.05 begrenzen. (a) Zähle die verschiedenen Paare. (b) Berechne die Bonferroni-Grenze pro Test. (c) Berechne unter der vereinfachenden Annahme unabhängiger Tests das Risiko für die ganze Testfamilie, wenn jeder Vergleich stattdessen 0.05 verwendet. (d) Erkläre, weshalb die Bonferroni-Garantie keine Unabhängigkeit der paarweisen Tests verlangt."
            solution=rf"Die Anzahl verschiedener ungeordneter Paare ist $m=k(k-1)/2={k}({k}-1)/2={comparisons}$. Bonferroni verwendet $\alpha_{{test}}=0.05/{comparisons}={number(threshold,4)}$. Wären alle {comparisons} Tests unabhängig und verwendete jeder 0.05, wäre die Wahrscheinlichkeit mindestens eines Fehlers vom Typ I unter der vollständigen Nullhypothese $1-(1-0.05)^{{{comparisons}}}={number(independent_risk,4)}$. Tatsächliche paarweise Vergleiche teilen häufig Gruppen und sind deshalb abhängig. Der letzte Ausdruck ist somit eine Veranschaulichung und nicht ihre allgemein exakte familienweise Fehlerrate. Bonferroni verwendet eine obere Grenze für die Wahrscheinlichkeit einer Vereinigung von Fehlern und kontrolliert die Familie daher auch ohne Unabhängigkeit, kann aber konservativ sein."
        else:
            prompt=rf"Një analizë synon çdo krahasim dysh mes $k={k}$ niveleve të faktorit dhe kërkon që norma e gabimit të llojit I për familjen e testeve të mos kalojë 0.05. (a) Numëro çiftet e ndryshme. (b) Llogarit pragun Bonferroni për secilin test. (c) Nën supozimin thjeshtues të testeve të pavarura, llogarit rrezikun për të gjithë familjen nëse secili krahasim përdor në vend të tij 0.05. (d) Shpjego pse garancia Bonferroni nuk kërkon që testet dyshe të jenë të pavarura."
            solution=rf"Numri i çifteve të ndryshme të parenditura është $m=k(k-1)/2={k}({k}-1)/2={comparisons}$. Bonferroni përdor $\alpha_{{test}}=0.05/{comparisons}={number(threshold,4)}$. Nëse të gjitha {comparisons} testet do të ishin të pavarura dhe secili do të përdorte 0.05, probabiliteti i të paktën një gabimi të llojit I nën hipotezën zero të plotë do të ishte $1-(1-0.05)^{{{comparisons}}}={number(independent_risk,4)}$. Krahasimet dyshe të vërteta shpesh përdorin grupe të përbashkëta dhe prandaj janë të varura, kështu që shprehja e fundit është ilustrim dhe jo norma e tyre e përgjithshme e saktë e gabimit për familjen e testeve. Bonferroni mbështetet në kufirin e sipërm të probabilitetit të bashkimit të gabimeve, ndaj e kontrollon familjen edhe pa pavarësi, megjithëse mund të jetë konservativ."
        exg.append(task(8,5,i,title,prompt));sog.append(task(8,5,i,title,solution))
    exercises.append("".join(exg));solutions.append("".join(sog))

    exg=[group_heading(6,titles[5])];sog=[group_heading(6,titles[5])];pair_labels=("A-B","A-C","A-D","B-C","B-D")
    for i,(_title,pvalues) in enumerate(FAMILY_CASES,1):
        title=CASE_TITLES[locale][6][i-1];rendered=", ".join(f"{label}: {number(p,3)}" for label,p in zip(pair_labels,pvalues));threshold=.05/5;passing=[label for label,p in zip(pair_labels,pvalues) if p<=threshold]
        if locale=="de":
            comparison_labels=("A gegen B","A gegen C","A gegen D","B gegen C","B gegen D")
            pvalue_rows=[(label,number(p,3)) for label,p in zip(comparison_labels,pvalues)]
            analyst_rows=(
                ("Person 1", "Legt vor der Ergebnissichtung nur A gegen B und A gegen C fest"),
                ("Person 2", "Legt vor der Ergebnissichtung alle fünf gezeigten Vergleiche fest"),
                ("Person 3", "Legt vor der Ergebnissichtung nur A gegen D fest"),
                ("Person 4", "Legt alle fünf fest und entfernt nach der Ergebnissichtung den Vergleich mit dem grössten p-Wert"),
                ("Person 5", "Trifft vorher keine Wahl, prüft alle fünf und berichtet danach nur den kleinsten p-Wert"),
            )
            prompt=rf"""Fünf Forschende erhalten dieselben fünf unkorrigierten Ergebnisse.

{markdown_table(('Vergleich','Unkorrigierter p-Wert'),pvalue_rows)}

Ihre angegebenen Pläne lauten:

{markdown_table(('Person','Entscheidungsprozess'),analyst_rows)}

(a) Definiere für jede Person die Vergleichsfamilie, die geschützt werden muss, und erkläre, weshalb ihre Grösse 1, 2 oder 5 beträgt. (b) Berechne für jede Person die Bonferroni-Grenze bei einer familienweisen Fehlerrate von $\alpha=0.05$. (c) Bestimme, welche von dieser Person berichteten Vergleiche die Grenze erfüllen. (d) Erkläre, weshalb das Entfernen oder Auswählen eines Vergleichs nach der Ergebnissichtung die Familie nicht verkleinert und einen Vergleich nicht nachträglich geplant macht. (e) Nenne, was jede Person vor der Ergebnissichtung hätte dokumentieren müssen."""
            plan_indices=((0,1),tuple(range(5)),(2,),tuple(range(5)),tuple(range(5)))
            solution_rows=[]
            for analyst_index,indices in enumerate(plan_indices,1):
                family_size=len(indices)
                analyst_threshold=.05/family_size
                analyst_passing=[comparison_labels[index] for index in indices if pvalues[index] <= analyst_threshold]
                result=", ".join(analyst_passing) if analyst_passing else "keines"
                solution_rows.append((f"Person {analyst_index}",str(family_size),number(analyst_threshold,3),result))
            solution=rf"""(a) und (b) Eine Familie enthält jeden Vergleich, den der Entscheidungsprozess verfügbar macht. Dazu gehören auch geprüfte und später ausgeblendete Vergleiche. Daraus ergeben sich folgende Familiengrössen und Grenzen:

{markdown_table(('Person','Familiengrösse','Bonferroni-Grenze','Ergebnisse unter der Grenze'),solution_rows)}

(c) Jedes Ergebnis in der letzten Spalte entsteht, indem nur die p-Werte in der ehrlichen Familie dieser Person mit $0.05/m$ verglichen werden. Person 1 hat zwei vorausschauend festgelegte Vergleiche, Person 2 hat fünf und Person 3 hat einen. Personen 4 und 5 haben ebenfalls fünf, weil ihre Reduktion erst erfolgte, nachdem die Ergebnisse sichtbar waren. (d) Das Entfernen des grössten Ergebnisses oder das Hervorheben des kleinsten Ergebnisses nach der Prüfung ist datenabhängige Auswahl. Dadurch verschwinden die anderen Möglichkeiten für einen Fehler vom Typ I nicht, und die hervorgehobene Frage wird nicht nachträglich geplant. (e) Vor der Ergebnissichtung hätte jede Person den wissenschaftlichen Vergleich, gegebenenfalls seine Richtung oder Kontrastgewichte, die vollständige Familie primärer und sekundärer Vergleiche sowie die gewählte Korrektur für Mehrfachvergleiche festhalten müssen."""
        else:
            comparison_labels=("A kundrejt B","A kundrejt C","A kundrejt D","B kundrejt C","B kundrejt D")
            pvalue_rows=[(label,number(p,3)) for label,p in zip(comparison_labels,pvalues)]
            analyst_rows=(
                ("Personi 1", "Para se t'i shohë rezultatet, planifikon vetëm A kundrejt B dhe A kundrejt C"),
                ("Personi 2", "Para se t'i shohë rezultatet, planifikon të pesë krahasimet e paraqitura"),
                ("Personi 3", "Para se t'i shohë rezultatet, planifikon vetëm A kundrejt D"),
                ("Personi 4", "Planifikon të pesë krahasimet, pastaj heq krahasimin me vlerën p më të madhe pasi i sheh rezultatet"),
                ("Personi 5", "Nuk bën zgjedhje paraprake, shqyrton të pesë krahasimet dhe pastaj raporton vetëm vlerën p më të vogël"),
            )
            prompt=rf"""Pesë persona që analizojnë të dhënat marrin të njëjtat pesë rezultate të pakorrigjuara.

{markdown_table(('Krahasimi','Vlera p e pakorrigjuar'),pvalue_rows)}

Planet që kanë deklaruar janë:

{markdown_table(('Personi','Procesi i vendimmarrjes'),analyst_rows)}

(a) Për secilin person, përcakto familjen e krahasimeve që duhet mbrojtur dhe shpjego pse madhësia e saj është 1, 2 ose 5. (b) Llogarite pragun Bonferroni të secilit person për normën e gabimit të familjes me $\alpha=0.05$. (c) Përcakto cilat krahasime të raportuara nga ai person e plotësojnë pragun. (d) Shpjego pse heqja ose përzgjedhja e një krahasimi pasi shihen rezultatet nuk e zvogëlon familjen dhe nuk e kthen krahasimin në të planifikuar. (e) Thuaj çfarë duhej të kishte dokumentuar secili person para se t'i shihte rezultatet."""
            plan_indices=((0,1),tuple(range(5)),(2,),tuple(range(5)),tuple(range(5)))
            solution_rows=[]
            for analyst_index,indices in enumerate(plan_indices,1):
                family_size=len(indices)
                analyst_threshold=.05/family_size
                analyst_passing=[comparison_labels[index] for index in indices if pvalues[index] <= analyst_threshold]
                result=", ".join(analyst_passing) if analyst_passing else "asnjë"
                solution_rows.append((f"Personi {analyst_index}",str(family_size),number(analyst_threshold,3),result))
            solution=rf"""(a) dhe (b) Një familje përmban çdo krahasim që procesi i vendimmarrjes e bën të disponueshëm, përfshirë krahasimet që u shqyrtuan dhe u fshehën më vonë. Kjo jep madhësitë dhe pragjet e mëposhtme:

{markdown_table(('Personi','Madhësia e familjes','Pragu Bonferroni','Rezultatet nën prag'),solution_rows)}

(c) Çdo rezultat në kolonën e fundit merret duke krahasuar vetëm vlerat p në familjen e deklaruar ndershmërisht nga ai person me $0.05/m$. Personi 1 ka dy krahasime të përcaktuara paraprakisht, Personi 2 ka pesë dhe Personi 3 ka një. Edhe Personat 4 dhe 5 kanë pesë, sepse zvogëlimi i tyre ndodhi pasi rezultatet u bënë të dukshme. (d) Heqja e rezultatit më të madh ose theksimi i rezultatit më të vogël pas shqyrtimit është përzgjedhje e varur nga të dhënat. Kjo nuk i zhduk mundësitë e tjera për një gabim të llojit I dhe nuk e bën pyetjen e theksuar të planifikuar në mënyrë prapavepruese. (e) Para se t'i shihte rezultatet, secili person duhej të shënonte krahasimin shkencor, drejtimin ose peshat e kontrastit kur ishin të rëndësishme, familjen e plotë të krahasimeve kryesore dhe dytësore, si dhe rregullin e zgjedhur për krahasimet e shumëfishta."""
        exg.append(task(8,6,i,title,prompt));sog.append(task(8,6,i,title,solution))
    exercises.append("".join(exg));solutions.append("".join(sog))

    exg=[group_heading(7,titles[6])];sog=[group_heading(7,titles[6])];weights=(-3,-1,1,3)
    for i,(_title,means,n,mse) in enumerate(TREND_CASES,1):
        title=CASE_TITLES[locale][7][i-1];estimate=sum(c*m for c,m in zip(weights,means));se=math.sqrt(mse/n*sum(c*c for c in weights));t_value=estimate/se;passes=abs(t_value)>2.028
        if locale=="de":
            prompt=rf"Vier gleichabständige geordnete Stufen haben die Mittelwerte ({vector(means)}), je $n={n}$ Beobachtungen und $MS_e={mse}$. Drei Forschende schlagen $c_1=(0,1,2,3)$, $c_2=(-3,-1,1,3)$ und $c_3=(0.5,-0.5,-0.5,0.5)$ vor. (a) Skizziere jede Gewichtsfolge über den vier geordneten Stufen und nenne das Muster, das sie darstellt. (b) Prüfe, welche Vektoren die Kontrastbedingung erfüllen, nach der ihre Gewichte zusammen null ergeben. (c) Repariere $c_1$, indem du von jedem Eintrag das mittlere Gewicht abziehst. Erkläre danach, weshalb der reparierte Vektor dieselbe lineare Richtung wie $c_2$ darstellt. (d) Verwende die gültigen Gewichte des linearen Trends $c_2$, um die gewichtete Schätzung, ihren Standardfehler und ihre $t$-Statistik zu berechnen. (e) Vergleiche $|t|$ mit dem angegebenen zweiseitigen kritischen 5%-Wert 2.028 und interpretiere das Vorzeichen als geordnetes Muster statt als Beweis einer perfekt linearen Beziehung."
            solution=rf"(a) Die Gewichte $c_1$ steigen auf jeder Stufe um eine Einheit. Ihre Skizze bildet deshalb eine gerade ansteigende Folge. Auch die Gewichte $c_2$ steigen in gleichen Schritten und sind um null zentriert. Die Gewichte $c_3$ vergleichen die zwei Endpunkte mit den zwei mittleren Stufen und stellen deshalb Krümmung statt eines linearen Trends dar. (b) Die Summen lauten $0+1+2+3=6$, $-3-1+1+3=0$ und $0.5-0.5-0.5+0.5=0$. Somit sind $c_2$ und $c_3$ Kontraste, aber nur $c_2$ ist der angegebene lineare Trendkontrast. (c) Das mittlere Gewicht von $c_1$ beträgt $1.5$. Nach dem Abziehen entsteht $(-1.5,-0.5,0.5,1.5)$, genau die Hälfte von $c_2$. Werden alle Kontrastgewichte mit derselben positiven Konstante multipliziert, ändern sich die numerischen Skalen von Schätzung und Standardfehler gemeinsam. Die geprüfte Richtung und die $t$-Statistik bleiben gleich. (d) Mit $c_2$ ist die gewichtete Schätzung $D=\sum c_i\bar y_i={number(estimate,4)}$. Wegen der balancierten Gruppen gilt $SE(D)=\sqrt{{(MS_e/n)\sum c_i^2}}=\sqrt{{({mse}/{n})(9+1+1+9)}}={number(se,4)}$. Somit ist $t={number(estimate,4)}/{number(se,4)}={number(t_value,4)}$. (e) Weil $|{number(t_value,4)}|$ {'grösser' if passes else 'nicht grösser'} als 2.028 ist, {'erfüllt der lineare Trend das zweiseitige 5%-Kriterium' if passes else 'erfüllt der lineare Trend das zweiseitige 5%-Kriterium nicht'}. Das {'positive' if estimate>0 else 'negative'} Vorzeichen bedeutet, dass das gewichtete Muster über die geordneten Stufen tendenziell {'steigt' if estimate>0 else 'fällt'}. Das beweist weder gleiche benachbarte Veränderungen noch schliesst es Krümmung aus."
        else:
            prompt=rf"Katër nivele të renditura me largësi të barabartë kanë mesataret ({vector(means)}), $n={n}$ vrojtime për nivel dhe $MS_e={mse}$. Tre persona propozojnë $c_1=(0,1,2,3)$, $c_2=(-3,-1,1,3)$ dhe $c_3=(0.5,-0.5,-0.5,0.5)$. (a) Skicoje secilën renditje peshash kundrejt katër niveleve të renditura dhe thuaj çfarë modeli paraqet. (b) Kontrollo cilët vektorë e plotësojnë kushtin e kontrastit, sipas të cilit shuma e peshave është zero. (c) Riparoje $c_1$ duke zbritur peshën e tij mesatare nga çdo vlerë dhe shpjego pse vektori i riparuar paraqet të njëjtin drejtim linear si $c_2$. (d) Përdori peshat e vlefshme të prirjes lineare $c_2$ për të llogaritur vlerësimin e peshuar, gabimin e tij standard dhe statistikën $t$. (e) Krahasoje $|t|$ me vlerën kritike të dhënë për testin e dyanshëm në nivelin 5%, që është 2.028, dhe interpretoje shenjën si model të renditur, jo si provë të një marrëdhënieje plotësisht lineare."
            solution=rf"(a) Peshat $c_1$ rriten me një njësi në çdo nivel, prandaj skica e tyre formon një renditje të drejtë në rritje. Edhe peshat $c_2$ rriten me hapa të barabartë dhe janë të qendërzuara rreth zeros. Peshat $c_3$ krahasojnë dy pikat fundore me dy nivelet e mesme, prandaj paraqesin lakim dhe jo prirje lineare. (b) Shumat janë $0+1+2+3=6$, $-3-1+1+3=0$ dhe $0.5-0.5-0.5+0.5=0$. Kështu, $c_2$ dhe $c_3$ janë kontraste, por vetëm $c_2$ është kontrasti i dhënë i prirjes lineare. (c) Pesha mesatare e $c_1$ është $1.5$. Zbritja e saj jep $(-1.5,-0.5,0.5,1.5)$, që është saktësisht gjysma e $c_2$. Shumëzimi i të gjitha peshave të kontrastit me të njëjtën konstante pozitive e ndryshon së bashku shkallën numerike të vlerësimit dhe gabimit standard, por nuk e ndryshon drejtimin që testohet ose statistikën $t$. (d) Me $c_2$, vlerësimi i peshuar është $D=\sum c_i\bar y_i={number(estimate,4)}$. Meqë grupet janë të balancuara, $SE(D)=\sqrt{{(MS_e/n)\sum c_i^2}}=\sqrt{{({mse}/{n})(9+1+1+9)}}={number(se,4)}$. Prandaj $t={number(estimate,4)}/{number(se,4)}={number(t_value,4)}$. (e) Meqë $|{number(t_value,4)}|$ {'është më e madhe' if passes else 'nuk është më e madhe'} se 2.028, prirja lineare {'e plotëson' if passes else 'nuk e plotëson'} kriterin e dyanshëm 5%. Shenja {'pozitive' if estimate>0 else 'negative'} do të thotë se modeli i peshuar priret të {'rritet' if estimate>0 else 'ulet'} përgjatë niveleve të renditura. Kjo nuk provon se ndryshimet mes niveleve fqinje janë të barabarta dhe as nuk e përjashton lakimin."
        exg.append(task(8,7,i,title,prompt));sog.append(task(8,7,i,title,solution))
    exercises.append("".join(exg));solutions.append("".join(sog))

    exg=[group_heading(8,titles[7])];sog=[group_heading(8,titles[7])]
    for i,(_title,_a_name,_b_name,cells,n,mse) in enumerate(FACTORIAL_CASES,1):
        title,a_name,b_name=FACTORIAL_LOCALIZED[locale][i-1];a0b0,a0b1,a1b0,a1b1=cells;grand=sum(cells)/4;a_means=((a0b0+a0b1)/2,(a1b0+a1b1)/2);b_means=((a0b0+a1b0)/2,(a0b1+a1b1)/2);ss_a=2*n*sum((m-grand)**2 for m in a_means);ss_b=2*n*sum((m-grand)**2 for m in b_means);ss_ab=n*sum((cell-a_means[a]-b_means[b]+grand)**2 for a in range(2) for b,cell in enumerate(cells[2*a:2*a+2]));df_error=4*(n-1);ss_error=mse*df_error;f_a=ss_a/mse;f_b=ss_b/mse;f_ab=ss_ab/mse;has_interaction=abs((a0b1-a0b0)-(a1b1-a1b0))>1e-9
        if locale=="de":
            prompt=rf"Eine balancierte $2\times2$-Studie hat $n={n}$ Beobachtungen pro Zelle. Die Zellmittelwerte in der Reihenfolge $A_0B_0,A_0B_1,A_1B_0,A_1B_1$ sind ({vector(cells)}). Faktor A ist «{a_name}»; Faktor B ist «{b_name}». Die gepoolte mittlere Fehlerquadratsumme ist $MS_e={mse}$. (a) Berechne die zwei Randmittelwerte jedes Faktors und den Gesamtmittelwert. (b) Beschreibe die Muster beider Haupteffekte und der Interaktion. (c) Formuliere die drei Nullhypothesen. (d) Rekonstruiere $SS_A$, $SS_B$, $SS_{{AB}}$, $SS_e$, ihre Freiheitsgrade und die drei $F$-Quotienten. (e) Zeichne ein Mittelwertdiagramm mit $B_0$ und $B_1$ auf der horizontalen Achse und einer beschrifteten Linie für jede Stufe von Faktor A. Erkläre, wie parallele oder nicht parallele Linien das Interaktionsergebnis ausdrücken."
            interaction="Die Veränderung über Faktor B unterscheidet sich zwischen den zwei Stufen von Faktor A; das Zellmuster enthält daher eine Interaktion." if has_interaction else "Die Veränderung über Faktor B ist bei beiden Stufen von Faktor A gleich; diese Zellmittelwerte zeigen daher keine Interaktion."
            solution=rf"(a) Die Randmittelwerte von Faktor A sind ({number(a_means[0],4)}, {number(a_means[1],4)}); die Randmittelwerte von Faktor B sind ({number(b_means[0],4)}, {number(b_means[1],4)}); der Gesamtmittelwert ist {number(grand,4)}. (b) Der A-Haupteffekt vergleicht seine zwei Randmittelwerte, der B-Haupteffekt die seinen. {interaction} (c) Die drei Nullhypothesen lauten: kein A-Haupteffekt in der Population, kein B-Haupteffekt in der Population und keine $A\times B$-Interaktion in der Population. (d) Die Berechnungen des balancierten Designs ergeben $SS_A={number(ss_a,4)}$, $SS_B={number(ss_b,4)}$ und $SS_{{AB}}={number(ss_ab,4)}$. Mit $df_A=df_B=df_{{AB}}=1$ und $df_e=4({n}-1)={df_error}$ gilt $SS_e=MS_e\,df_e={mse}({df_error})={number(ss_error,4)}$. Deshalb $F_A={number(f_a,4)}$, $F_B={number(f_b,4)}$ und $F_{{AB}}={number(f_ab,4)}$. (e) Zeichne die Stufe $A_0$ von Faktor A durch die Koordinaten $(B_0,{number(a0b0,4)})$ und $(B_1,{number(a0b1,4)})$. Zeichne $A_1$ durch $(B_0,{number(a1b0,4)})$ und $(B_1,{number(a1b1,4)})$. {'Die beiden Veränderungen unterscheiden sich, daher sind die Linien nicht parallel und das Diagramm zeigt die Interaktion.' if has_interaction else 'Die beiden Veränderungen sind gleich, daher sind die Linien parallel und das Diagramm zeigt keine Interaktion.'} Haupteffekte fassen Randmittelwerte zusammen; eine Interaktion fragt, ob sich das Muster eines Faktors über den anderen verändert."
        else:
            prompt=rf"Një studim i balancuar $2\times2$ ka $n={n}$ vrojtime për qelizë. Mesataret e qelizave, sipas rendit $A_0B_0,A_0B_1,A_1B_0,A_1B_1$, janë ({vector(cells)}). Faktori A është «{a_name}»; Faktori B është «{b_name}». Katrori mesatar i përbashkët i gabimit është $MS_e={mse}$. (a) Llogariti dy mesataret margjinale për secilin faktor dhe mesataren e përgjithshme. (b) Përshkruaji modelet e të dy efekteve kryesore dhe modelin e ndërveprimit. (c) Shkruaji tri hipotezat zero. (d) Rindërtoji $SS_A$, $SS_B$, $SS_{{AB}}$, $SS_e$, shkallët e tyre të lirisë dhe tri raportet $F$. (e) Vizato një grafik të mesatareve me $B_0$ dhe $B_1$ në boshtin horizontal dhe nga një vijë të emërtuar për secilin nivel të faktorit A. Shpjego si e shprehin vijat paralele ose joparalele rezultatin e ndërveprimit."
            interaction="Ndryshimi përgjatë Faktorit B dallon mes dy niveleve të Faktorit A, prandaj modeli i qelizave përmban ndërveprim." if has_interaction else "Ndryshimi përgjatë Faktorit B është i njëjtë në të dy nivelet e Faktorit A, prandaj këto mesatare qelizash nuk tregojnë ndërveprim."
            solution=rf"(a) Mesataret margjinale të Faktorit A janë ({number(a_means[0],4)}, {number(a_means[1],4)}); mesataret margjinale të Faktorit B janë ({number(b_means[0],4)}, {number(b_means[1],4)}); mesatarja e përgjithshme është {number(grand,4)}. (b) Efekti kryesor A krahason dy mesataret margjinale të tij, ndërsa efekti kryesor B krahason dy mesataret margjinale të tij. {interaction} (c) Tri hipotezat zero janë: pa efekt kryesor A në popullatë, pa efekt kryesor B në popullatë dhe pa ndërveprim $A\times B$ në popullatë. (d) Llogaritjet e dizajnit të balancuar japin $SS_A={number(ss_a,4)}$, $SS_B={number(ss_b,4)}$ dhe $SS_{{AB}}={number(ss_ab,4)}$. Me $df_A=df_B=df_{{AB}}=1$ dhe $df_e=4({n}-1)={df_error}$, $SS_e=MS_e\,df_e={mse}({df_error})={number(ss_error,4)}$. Prandaj $F_A={number(f_a,4)}$, $F_B={number(f_b,4)}$ dhe $F_{{AB}}={number(f_ab,4)}$. (e) Vizatoje nivelin $A_0$ të faktorit A përmes koordinatave $(B_0,{number(a0b0,4)})$ dhe $(B_1,{number(a0b1,4)})$. Vizatoje $A_1$ përmes $(B_0,{number(a1b0,4)})$ dhe $(B_1,{number(a1b1,4)})$. {'Dy ndryshimet dallojnë, prandaj vijat nuk janë paralele dhe grafiku e paraqet ndërveprimin.' if has_interaction else 'Dy ndryshimet janë të barabarta, prandaj vijat janë paralele dhe grafiku nuk paraqet ndërveprim.'} Efektet kryesore përmbledhin mesataret margjinale, ndërsa ndërveprimi pyet nëse modeli i një faktori ndryshon përgjatë faktorit tjetër."
        exg.append(task(8,8,i,title,prompt));sog.append(task(8,8,i,title,solution))
    exercises.append("".join(exg));solutions.append("".join(sog))

    exg=[group_heading(9,titles[8])];sog=[group_heading(9,titles[8])]
    for i,(_title,_random_level,_fixed_factor,n,ms_between,ms_error) in enumerate(RANDOM_FACTOR_CASES,1):
        title,random_level,fixed_factor=RANDOM_FACTOR_LOCALIZED[locale][i-1];var_between=(ms_between-ms_error)/n;var_error=ms_error;icc=var_between/(var_between+var_error)
        if locale=="de":
            prompt=rf"Eine Studie zieht Stufen des Faktors «{random_level}» zufällig aus einer grösseren Population und untersucht zusätzlich den festen Faktor «{fixed_factor}». Für die balancierte einfaktorielle Analyse dieses Zufallsfaktors liegen an jeder gezogenen Stufe $n={n}$ Beobachtungen vor, $MS_A={ms_between}$ und $MS_e={ms_error}$. (a) Erkläre, weshalb «{random_level}» ein Zufallsfaktor und der andere Faktor fest ist. (b) Nenne das Populationsziel der Zufallsfaktoranalyse. (c) Schätze die Varianzkomponenten zwischen den Stufen und innerhalb der Stufen. (d) Berechne und interpretiere den einfaktoriellen ICC. (e) Begründe, weshalb diese Formel nicht automatisch auf jedes gruppierte Design angewendet werden darf."
            solution=rf"Die Stufen des Faktors «{random_level}» wurden gezogen, um eine grössere Population möglicher Stufen darzustellen; bei einer Wiederholung könnten neue Stufen gezogen werden. Dagegen bezeichnet der feste Faktor «{fixed_factor}» genau die ausgewählten interessierenden Bedingungen. Das Ziel des Zufallsfaktors ist die Variation in seiner Population von Stufen und nicht eine Liste paarweiser Unterschiede nur zwischen den gezogenen Bezeichnungen. In diesem balancierten einfaktoriellen Modell ist $\widehat{{\sigma}}_A^2=(MS_A-MS_e)/n=({ms_between}-{ms_error})/{n}={number(var_between,4)}$ und $\widehat{{\sigma}}_e^2=MS_e={number(var_error,4)}$. Somit $ICC={number(var_between,4)}/[{number(var_between,4)}+{number(var_error,4)}]={number(icc,4)}$. Das Modell ordnet ungefähr {number(100*icc,1)}% seiner Varianz Unterschieden zwischen zufällig gezogenen Stufen des Faktors «{random_level}» zu. Diese Gleichung hängt von einer balancierten einfaktoriellen Zufallsfaktorstruktur ab; gekreuzte, verschachtelte, wiederholte oder unbalancierte Designs können andere Komponenten und Nenner verlangen."
        else:
            prompt=rf"Një studim përzgjedh rastësisht nivele të faktorit «{random_level}» nga një popullatë më e gjerë dhe shqyrton gjithashtu faktorin fiks «{fixed_factor}». Për analizën e balancuar njëfaktoriale të këtij faktori të rastësishëm, në çdo nivel të kampionuar ka $n={n}$ vrojtime, $MS_A={ms_between}$ dhe $MS_e={ms_error}$. (a) Shpjego pse «{random_level}» është faktor i rastësishëm dhe faktori tjetër është fiks. (b) Jep synimin në popullatë të analizës së faktorit të rastësishëm. (c) Vlerëso komponentët e variancës mes niveleve dhe të gabimit. (d) Llogarit dhe interpreto ICC-në njëfaktoriale. (e) Thuaj pse kjo formulë nuk duhet zbatuar automatikisht në çdo dizajn të grupuar."
            solution=rf"Nivelet e faktorit «{random_level}» u kampionuan për të përfaqësuar një popullatë më të gjerë nivelesh të mundshme, prandaj përsëritja e studimit mund të zgjidhte nivele të reja. Në të kundërt, faktori fiks «{fixed_factor}» emërton pikërisht kushtet e zgjedhura me interes. Synimi i faktorit të rastësishëm është ndryshueshmëria në popullatën e niveleve të tij, jo një listë dallimesh dyshe vetëm mes emërtimeve të kampionuara. Në këtë model të balancuar njëfaktorial, $\widehat{{\sigma}}_A^2=(MS_A-MS_e)/n=({ms_between}-{ms_error})/{n}={number(var_between,4)}$ dhe $\widehat{{\sigma}}_e^2=MS_e={number(var_error,4)}$. Prandaj $ICC={number(var_between,4)}/[{number(var_between,4)}+{number(var_error,4)}]={number(icc,4)}$. Modeli ia atribuon rreth {number(100*icc,1)}% të variancës së vet dallimeve mes niveleve të kampionuara të faktorit «{random_level}». Ky ekuacion varet nga një strukturë e balancuar njëfaktoriale me faktor të rastësishëm; dizajnet e kryqëzuara, të folezuara, të përsëritura ose të pabalancuara mund të kërkojnë komponentë dhe emërues të ndryshëm."
        exg.append(task(8,9,i,title,prompt));sog.append(task(8,9,i,title,solution))
    exercises.append("".join(exg));solutions.append("".join(sog))

    exg=[group_heading(10,titles[9])];sog=[group_heading(10,titles[9])]
    for i,(_title,diffvars,ss_condition,ss_person,ss_error,epsilon) in enumerate(REPEATED_CASES,1):
        title=CASE_TITLES[locale][10][i-1];df_condition=2;df_person=11;df_error=22;k=3;ms_condition=ss_condition/df_condition;ms_person=ss_person/df_person;ms_error=ss_error/df_error;f_value=ms_condition/ms_error;corrected_condition=epsilon*df_condition;corrected_error=epsilon*df_error;person_var=(ms_person-ms_error)/k;icc=person_var/(person_var+ms_error);ratio=max(diffvars)/min(diffvars);plausible=ratio<1.35;marginal_variance=max(diffvars)+12;correlations=tuple(1-difference/(2*marginal_variance) for difference in diffvars);condition_p=f_upper_p(f_value,df_condition,df_error);person_f=ms_person/ms_error;person_p=f_upper_p(person_f,df_person,df_error);corrected_p=f_upper_p(f_value,corrected_condition,corrected_error)
        if locale=="de":
            moment_rows=(
                ("Varianz bei Bedingung 1",number(marginal_variance,4)),
                ("Varianz bei Bedingung 2",number(marginal_variance,4)),
                ("Varianz bei Bedingung 3",number(marginal_variance,4)),
                ("Korrelation 1 mit 2",number(correlations[0],4)),
                ("Korrelation 1 mit 3",number(correlations[1],4)),
                ("Korrelation 2 mit 3",number(correlations[2],4)),
            )
            prompt=rf"""Zwölf Personen werden unter drei Bedingungen gemessen. Die Stichprobenvarianzen und Korrelationen lauten:

{markdown_table(('Zusammenfassende Grösse','Wert'),moment_rows)}

Die Messwiederholungstabelle enthält $SS_{{condition}}={ss_condition}$, $SS_{{person}}={ss_person}$ und $SS_e={ss_error}$ mit den Freiheitsgraden 2, 11 und 22. Die Greenhouse-Geisser-Schätzung ist $\widehat{{\varepsilon}}={number(epsilon,2)}$. (a) Berechne mit $s_{{j-k}}^2=s_j^2+s_k^2-2r_{{jk}}s_js_k$ die drei Varianzen der paarweisen Differenzwerte. Erkläre, wonach Sphärizität fragt, und beurteile das Muster beschreibend. (b) Formuliere die Nullhypothesen für den Bedingungseffekt und die Personenvariation. Vervollständige die drei mittleren Quadratsummen, berechne sowohl $F_{{condition}}$ als auch $F_{{person}}$, bestimme ihre p-Werte im oberen Verteilungsschwanz und interpretiere beide Entscheidungen. (c) Schätze die Personenvarianzkomponente und den ICC. (d) Berechne die Greenhouse-Geisser-korrigierten Freiheitsgrade für Bedingung und Fehler sowie den korrigierten p-Wert. (e) Erkläre, was die Korrektur verändert, was unverändert bleibt und weshalb wiederholte Zeilen nicht unabhängig werden."""
            description="ziemlich ähnlich und bietet daher beschreibende Beruhigung, beweist Sphärizität aber nicht" if plausible else "deutlich ungleich und warnt daher davor, dass die unkorrigierte Referenz unzuverlässig sein kann"
            solution=rf"(a) Weil alle drei Randvarianzen {number(marginal_variance,4)} betragen, ist jede Standardabweichung $\sqrt{{{number(marginal_variance,4)}}}$. Das Einsetzen ergibt ungefähr die Varianzen der Differenzwerte ({vector(diffvars)}). Die Korrelationen wurden mit vier Dezimalstellen gezeigt, weshalb kleine Abweichungen bei der Rekonstruktion nur auf Rundung beruhen. Sphärizität fragt, ob die Populationsvarianzen aller paarweisen Bedingungsdifferenzen gleich sind. Die rekonstruierten Werte reichen von {min(diffvars)} bis {max(diffvars)}; ihr Verhältnis von grösstem zu kleinstem Wert beträgt {number(ratio,4)}. Dieses Muster ist {description}. (b) Für die Bedingungen lautet $H_0:\mu_1=\mu_2=\mu_3$; die Alternative besagt, dass sich mindestens zwei Bedingungsmittelwerte unterscheiden. Für Personen lautet die Nullhypothese des zufälligen Personeneffekts $H_0:\sigma_{{person}}^2=0$ gegen positive Variation zwischen Personen. Die mittleren Quadratsummen sind $MS_{{condition}}={ss_condition}/2={number(ms_condition,4)}$, $MS_{{person}}={ss_person}/11={number(ms_person,4)}$ und $MS_e={ss_error}/22={number(ms_error,4)}$. Somit gilt $F_{{condition}}={number(f_value,4)}$ mit p-Wert {number(condition_p,4)} und $F_{{person}}={number(ms_person,4)}/{number(ms_error,4)}={number(person_f,4)}$ mit p-Wert {number(person_p,4)}. Der Bedingungstest {'verwirft' if condition_p < .05 else 'verwirft nicht'} die Gleichheit der Mittelwerte bei 5%; der Personentest {'stützt' if person_p < .05 else 'liefert keine ausreichende Evidenz für'} Variation zwischen Personen bei 5%. (c) $\widehat{{\sigma}}_{{person}}^2=({number(ms_person,4)}-{number(ms_error,4)})/3={number(person_var,4)}$, somit $ICC={number(person_var,4)}/[{number(person_var,4)}+{number(ms_error,4)}]={number(icc,4)}$. Der ICC beschreibt unter diesem Modell die Ähnlichkeit von Messungen derselben Person. (d) Greenhouse-Geisser ergibt $df_{{condition}}^*={number(epsilon,2)}(2)={number(corrected_condition,4)}$ und $df_e^*={number(epsilon,2)}(22)={number(corrected_error,4)}$. Wird das beobachtete $F={number(f_value,4)}$ mit diesen Referenzfreiheitsgraden verwendet, ergibt sich der korrigierte p-Wert {number(corrected_p,4)}. (e) Die Korrektur verändert die Referenzfreiheitsgrade und damit den p-Wert oder den kritischen Wert. Sie verändert weder das beobachtete $F$ noch die angepassten Mittelwerte oder die Abhängigkeit zwischen wiederholten Zeilen. Messungen derselben Person bleiben miteinander verbunden."
        else:
            moment_rows=(
                ("Varianca në kushtin 1",number(marginal_variance,4)),
                ("Varianca në kushtin 2",number(marginal_variance,4)),
                ("Varianca në kushtin 3",number(marginal_variance,4)),
                ("Korrelacioni i kushtit 1 me kushtin 2",number(correlations[0],4)),
                ("Korrelacioni i kushtit 1 me kushtin 3",number(correlations[1],4)),
                ("Korrelacioni i kushtit 2 me kushtin 3",number(correlations[2],4)),
            )
            prompt=rf"""Dymbëdhjetë persona maten në tri kushte. Variancat dhe korrelacionet e kampionit janë:

{markdown_table(('Madhësia përmbledhëse','Vlera'),moment_rows)}

Tabela e matjeve të përsëritura jep $SS_{{condition}}={ss_condition}$, $SS_{{person}}={ss_person}$ dhe $SS_e={ss_error}$ me shkallët e lirisë 2, 11 dhe 22. Vlerësimi Greenhouse-Geisser është $\widehat{{\varepsilon}}={number(epsilon,2)}$. (a) Përdore $s_{{j-k}}^2=s_j^2+s_k^2-2r_{{jk}}s_js_k$ për të llogaritur tri variancat e rezultateve të diferencave dyshe. Shpjego çfarë kërkon sfericiteti dhe vlerësoje modelin në mënyrë përshkruese. (b) Formuloji hipotezat zero për efektin e kushtit dhe ndryshueshmërinë mes personave. Plotësoji tre katrorët mesatarë, llogariti si $F_{{condition}}$ ashtu edhe $F_{{person}}$, gjeji vlerat e tyre p në bishtin e sipërm dhe interpretoji të dyja vendimet. (c) Vlerësoje komponentin e variancës mes personave dhe ICC-në. (d) Llogariti shkallët e lirisë të korrigjuara me Greenhouse-Geisser për kushtin dhe gabimin, si dhe vlerën p të korrigjuar. (e) Shpjego çfarë ndryshon korrigjimi, çfarë mbetet e pandryshuar dhe pse rreshtat e përsëritur nuk bëhen të pavarur."""
            description="mjaft i ngjashëm dhe prandaj jep siguri përshkruese, megjithëse nuk e provon sfericitetin" if plausible else "dukshëm i pabarabartë dhe prandaj paralajmëron se referenca e pakorrigjuar mund të jetë e pasigurt"
            solution=rf"(a) Meqë të tria variancat margjinale janë {number(marginal_variance,4)}, secili devijim standard është $\sqrt{{{number(marginal_variance,4)}}}$. Zëvendësimi jep afërsisht variancat e rezultateve të diferencave ({vector(diffvars)}). Korrelacionet janë paraqitur me katër shifra dhjetore, prandaj ndryshimet e vogla gjatë rindërtimit vijnë vetëm nga rrumbullakimi. Sfericiteti pyet nëse variancat e popullatës të çdo diference dyshe mes kushteve janë të barabarta. Vlerat e rindërtuara shtrihen nga {min(diffvars)} deri në {max(diffvars)}; raporti i më të madhes me më të voglën është {number(ratio,4)}. Ky model është {description}. (b) Për kushtet, hipoteza zero është $H_0:\mu_1=\mu_2=\mu_3$; alternativa thotë se të paktën dy mesatare të kushteve ndryshojnë. Për personat, hipoteza zero e efektit të rastësishëm të personit është $H_0:\sigma_{{person}}^2=0$ kundrejt ndryshueshmërisë pozitive mes personave. Katrorët mesatarë janë $MS_{{condition}}={ss_condition}/2={number(ms_condition,4)}$, $MS_{{person}}={ss_person}/11={number(ms_person,4)}$ dhe $MS_e={ss_error}/22={number(ms_error,4)}$. Prandaj $F_{{condition}}={number(f_value,4)}$ me vlerë p {number(condition_p,4)}, ndërsa $F_{{person}}={number(ms_person,4)}/{number(ms_error,4)}={number(person_f,4)}$ me vlerë p {number(person_p,4)}. Testi i kushtit {'e hedh poshtë' if condition_p < .05 else 'nuk e hedh poshtë'} barazinë e mesatareve në nivelin 5%; testi i personit {'mbështet' if person_p < .05 else 'nuk jep evidencë të mjaftueshme për'} ndryshueshmëri mes personave në nivelin 5%. (c) $\widehat{{\sigma}}_{{person}}^2=({number(ms_person,4)}-{number(ms_error,4)})/3={number(person_var,4)}$, prandaj $ICC={number(person_var,4)}/[{number(person_var,4)}+{number(ms_error,4)}]={number(icc,4)}$. Sipas këtij modeli, ICC-ja përshkruan ngjashmërinë mes matjeve të të njëjtit person. (d) Greenhouse-Geisser jep $df_{{condition}}^*={number(epsilon,2)}(2)={number(corrected_condition,4)}$ dhe $df_e^*={number(epsilon,2)}(22)={number(corrected_error,4)}$. Përdorimi i $F={number(f_value,4)}$ të vëzhguar me këto shkallë lirie referuese jep vlerën p të korrigjuar {number(corrected_p,4)}. (e) Korrigjimi i ndryshon shkallët referuese të lirisë dhe, për pasojë, vlerën p ose vlerën kritike. Nuk e ndryshon $F$ të vëzhguar, mesataret e përshtatura ose varësinë mes rreshtave të përsëritur. Matjet e të njëjtit person mbeten të lidhura."
        exg.append(task(8,10,i,title,prompt));sog.append(task(8,10,i,title,solution))
    exercises.append("".join(exg));solutions.append("".join(sog));return exercises,solutions


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--locale", choices=("en", "de", "sq"), default="en")
    args = parser.parse_args()
    exercises, solutions = render_localized(args.locale)
    write_pair(8, args.locale, 10, exercises, solutions)
    validate_sources_allowing_incomplete_locales(args.locale, topic=8)
    print(f"Generated and source-validated Topic 8 {args.locale} exercise and solution sources.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
