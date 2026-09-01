---
title: "Exercise Sheet"
subtitle: "Analysis of Variance"
document-id: "topic-08-analysis-of-variance-exercises-en"
topic-id: "topic-08-analysis-of-variance"
topic-number: "08"
topic-slug: "analysis-of-variance"
document-type: "exercises"
locale: "en"
paired-document-id: "topic-08-analysis-of-variance-solutions-en"
---

This sheet contains 100 exercises organized into 10 learning-objective groups. Work through each exercise before consulting its matching complete solution. Show the relevant formula or rule, substituted values, units, and an interpretation. All settings, values, data, and software outputs are constructed teaching material; they are not empirical findings.

# Part I: Theory

## A01: The Question Answered by One-Way ANOVA

### T08-A01-V01: Reading formats and comprehension

A study records comprehension score in points and compares the levels print, tablet, audio of the categorical factor reading format. Cases were randomly assigned to the levels. (a) Identify the quantitative outcome, factor, and levels. (b) State the one-way ANOVA null and alternative hypotheses in words and symbols. (c) Explain why one omnibus test is preferable to beginning with three unadjusted pairwise tests. (d) State what a significant omnibus result would and would not establish.

### T08-A01-V02: Museum routes and visit duration

A study records visit duration in minutes and compares the levels free route, numbered route, guided route of the categorical factor route type. Cases were randomly assigned to the levels. (a) Identify the quantitative outcome, factor, and levels. (b) State the one-way ANOVA null and alternative hypotheses in words and symbols. (c) Explain why one omnibus test is preferable to beginning with three unadjusted pairwise tests. (d) State what a significant omnibus result would and would not establish.

### T08-A01-V03: Study locations and concentration

A study records concentration score in points and compares the levels home, library, shared workspace of the categorical factor usual study location. The factor was observed without random assignment. (a) Identify the quantitative outcome, factor, and levels. (b) State the one-way ANOVA null and alternative hypotheses in words and symbols. (c) Explain why one omnibus test is preferable to beginning with three unadjusted pairwise tests. (d) State what a significant omnibus result would and would not establish.

### T08-A01-V04: Reminder schedules and response delay

A study records response delay in hours and compares the levels none, one reminder, three reminders of the categorical factor reminder schedule. Cases were randomly assigned to the levels. (a) Identify the quantitative outcome, factor, and levels. (b) State the one-way ANOVA null and alternative hypotheses in words and symbols. (c) Explain why one omnibus test is preferable to beginning with three unadjusted pairwise tests. (d) State what a significant omnibus result would and would not establish.

### T08-A01-V05: Archive interfaces and retrieval accuracy

A study records retrieval accuracy in points and compares the levels standard, compact, guided of the categorical factor interface version. Cases were randomly assigned to the levels. (a) Identify the quantitative outcome, factor, and levels. (b) State the one-way ANOVA null and alternative hypotheses in words and symbols. (c) Explain why one omnibus test is preferable to beginning with three unadjusted pairwise tests. (d) State what a significant omnibus result would and would not establish.

### T08-A01-V06: Travel modes and commuting time

A study records commuting time in minutes and compares the levels walking, public transport, car of the categorical factor usual travel mode. The factor was observed without random assignment. (a) Identify the quantitative outcome, factor, and levels. (b) State the one-way ANOVA null and alternative hypotheses in words and symbols. (c) Explain why one omnibus test is preferable to beginning with three unadjusted pairwise tests. (d) State what a significant omnibus result would and would not establish.

### T08-A01-V07: Practice routines and delayed recall

A study records delayed-recall score in points and compares the levels rereading, self-testing, mixed practice of the categorical factor practice routine. Cases were randomly assigned to the levels. (a) Identify the quantitative outcome, factor, and levels. (b) State the one-way ANOVA null and alternative hypotheses in words and symbols. (c) Explain why one omnibus test is preferable to beginning with three unadjusted pairwise tests. (d) State what a significant omnibus result would and would not establish.

### T08-A01-V08: Workshop tracks and confidence

A study records confidence score in points and compares the levels methods, writing, presentation of the categorical factor chosen workshop track. The factor was observed without random assignment. (a) Identify the quantitative outcome, factor, and levels. (b) State the one-way ANOVA null and alternative hypotheses in words and symbols. (c) Explain why one omnibus test is preferable to beginning with three unadjusted pairwise tests. (d) State what a significant omnibus result would and would not establish.

### T08-A01-V09: Caption styles and tutorial understanding

A study records understanding score in points and compares the levels none, verbatim, edited of the categorical factor caption style. Cases were randomly assigned to the levels. (a) Identify the quantitative outcome, factor, and levels. (b) State the one-way ANOVA null and alternative hypotheses in words and symbols. (c) Explain why one omnibus test is preferable to beginning with three unadjusted pairwise tests. (d) State what a significant omnibus result would and would not establish.

### T08-A01-V10: Neighborhood types and park use

A study records weekly park visits in visits and compares the levels central, suburban, rural of the categorical factor neighborhood type. The factor was observed without random assignment. (a) Identify the quantitative outcome, factor, and levels. (b) State the one-way ANOVA null and alternative hypotheses in words and symbols. (c) Explain why one omnibus test is preferable to beginning with three unadjusted pairwise tests. (d) State what a significant omnibus result would and would not establish.

## A06: Defining a Comparison Family Before Looking at Results

### T08-A06-V01: Study routines

Five analysts receive the same five unadjusted results.

| Comparison | Unadjusted p-value |
|---|---|
| A versus B | 0.004 |
| A versus C | 0.018 |
| A versus D | 0.041 |
| B versus C | 0.083 |
| B versus D | 0.220 |

Their stated plans are:

| Analyst | Decision process |
|---|---|
| Analyst 1 | Before seeing outcomes, plans A versus B and A versus C only |
| Analyst 2 | Before seeing outcomes, plans all five displayed comparisons |
| Analyst 3 | Before seeing outcomes, plans A versus D only |
| Analyst 4 | Plans all five, then drops the comparison with the largest p-value after seeing outcomes |
| Analyst 5 | Makes no prior choice, inspects all five, then reports only the smallest p-value |

(a) For each analyst, define the comparison family that must be protected and explain why its size is 1, 2, or 5. (b) Calculate the analyst's Bonferroni threshold for familywise $\alpha=0.05$. (c) Identify which of that analyst's reported comparisons meet the threshold. (d) Explain why dropping or selecting a comparison after seeing outcomes does not make the family smaller or turn a comparison into a planned one. (e) State what each analyst would have needed to document before viewing outcomes.

### T08-A06-V02: Reading layouts

Five analysts receive the same five unadjusted results.

| Comparison | Unadjusted p-value |
|---|---|
| A versus B | 0.009 |
| A versus C | 0.011 |
| A versus D | 0.037 |
| B versus C | 0.120 |
| B versus D | 0.310 |

Their stated plans are:

| Analyst | Decision process |
|---|---|
| Analyst 1 | Before seeing outcomes, plans A versus B and A versus C only |
| Analyst 2 | Before seeing outcomes, plans all five displayed comparisons |
| Analyst 3 | Before seeing outcomes, plans A versus D only |
| Analyst 4 | Plans all five, then drops the comparison with the largest p-value after seeing outcomes |
| Analyst 5 | Makes no prior choice, inspects all five, then reports only the smallest p-value |

(a) For each analyst, define the comparison family that must be protected and explain why its size is 1, 2, or 5. (b) Calculate the analyst's Bonferroni threshold for familywise $\alpha=0.05$. (c) Identify which of that analyst's reported comparisons meet the threshold. (d) Explain why dropping or selecting a comparison after seeing outcomes does not make the family smaller or turn a comparison into a planned one. (e) State what each analyst would have needed to document before viewing outcomes.

### T08-A06-V03: Archive prompts

Five analysts receive the same five unadjusted results.

| Comparison | Unadjusted p-value |
|---|---|
| A versus B | 0.002 |
| A versus C | 0.015 |
| A versus D | 0.049 |
| B versus C | 0.070 |
| B versus D | 0.440 |

Their stated plans are:

| Analyst | Decision process |
|---|---|
| Analyst 1 | Before seeing outcomes, plans A versus B and A versus C only |
| Analyst 2 | Before seeing outcomes, plans all five displayed comparisons |
| Analyst 3 | Before seeing outcomes, plans A versus D only |
| Analyst 4 | Plans all five, then drops the comparison with the largest p-value after seeing outcomes |
| Analyst 5 | Makes no prior choice, inspects all five, then reports only the smallest p-value |

(a) For each analyst, define the comparison family that must be protected and explain why its size is 1, 2, or 5. (b) Calculate the analyst's Bonferroni threshold for familywise $\alpha=0.05$. (c) Identify which of that analyst's reported comparisons meet the threshold. (d) Explain why dropping or selecting a comparison after seeing outcomes does not make the family smaller or turn a comparison into a planned one. (e) State what each analyst would have needed to document before viewing outcomes.

### T08-A06-V04: Museum routes

Five analysts receive the same five unadjusted results.

| Comparison | Unadjusted p-value |
|---|---|
| A versus B | 0.006 |
| A versus C | 0.024 |
| A versus D | 0.032 |
| B versus C | 0.190 |
| B versus D | 0.270 |

Their stated plans are:

| Analyst | Decision process |
|---|---|
| Analyst 1 | Before seeing outcomes, plans A versus B and A versus C only |
| Analyst 2 | Before seeing outcomes, plans all five displayed comparisons |
| Analyst 3 | Before seeing outcomes, plans A versus D only |
| Analyst 4 | Plans all five, then drops the comparison with the largest p-value after seeing outcomes |
| Analyst 5 | Makes no prior choice, inspects all five, then reports only the smallest p-value |

(a) For each analyst, define the comparison family that must be protected and explain why its size is 1, 2, or 5. (b) Calculate the analyst's Bonferroni threshold for familywise $\alpha=0.05$. (c) Identify which of that analyst's reported comparisons meet the threshold. (d) Explain why dropping or selecting a comparison after seeing outcomes does not make the family smaller or turn a comparison into a planned one. (e) State what each analyst would have needed to document before viewing outcomes.

### T08-A06-V05: Reminder schedules

Five analysts receive the same five unadjusted results.

| Comparison | Unadjusted p-value |
|---|---|
| A versus B | 0.013 |
| A versus C | 0.021 |
| A versus D | 0.028 |
| B versus C | 0.055 |
| B versus D | 0.330 |

Their stated plans are:

| Analyst | Decision process |
|---|---|
| Analyst 1 | Before seeing outcomes, plans A versus B and A versus C only |
| Analyst 2 | Before seeing outcomes, plans all five displayed comparisons |
| Analyst 3 | Before seeing outcomes, plans A versus D only |
| Analyst 4 | Plans all five, then drops the comparison with the largest p-value after seeing outcomes |
| Analyst 5 | Makes no prior choice, inspects all five, then reports only the smallest p-value |

(a) For each analyst, define the comparison family that must be protected and explain why its size is 1, 2, or 5. (b) Calculate the analyst's Bonferroni threshold for familywise $\alpha=0.05$. (c) Identify which of that analyst's reported comparisons meet the threshold. (d) Explain why dropping or selecting a comparison after seeing outcomes does not make the family smaller or turn a comparison into a planned one. (e) State what each analyst would have needed to document before viewing outcomes.

### T08-A06-V06: Note templates

Five analysts receive the same five unadjusted results.

| Comparison | Unadjusted p-value |
|---|---|
| A versus B | 0.001 |
| A versus C | 0.017 |
| A versus D | 0.044 |
| B versus C | 0.099 |
| B versus D | 0.510 |

Their stated plans are:

| Analyst | Decision process |
|---|---|
| Analyst 1 | Before seeing outcomes, plans A versus B and A versus C only |
| Analyst 2 | Before seeing outcomes, plans all five displayed comparisons |
| Analyst 3 | Before seeing outcomes, plans A versus D only |
| Analyst 4 | Plans all five, then drops the comparison with the largest p-value after seeing outcomes |
| Analyst 5 | Makes no prior choice, inspects all five, then reports only the smallest p-value |

(a) For each analyst, define the comparison family that must be protected and explain why its size is 1, 2, or 5. (b) Calculate the analyst's Bonferroni threshold for familywise $\alpha=0.05$. (c) Identify which of that analyst's reported comparisons meet the threshold. (d) Explain why dropping or selecting a comparison after seeing outcomes does not make the family smaller or turn a comparison into a planned one. (e) State what each analyst would have needed to document before viewing outcomes.

### T08-A06-V07: Practice intervals

Five analysts receive the same five unadjusted results.

| Comparison | Unadjusted p-value |
|---|---|
| A versus B | 0.008 |
| A versus C | 0.019 |
| A versus D | 0.026 |
| B versus C | 0.078 |
| B versus D | 0.290 |

Their stated plans are:

| Analyst | Decision process |
|---|---|
| Analyst 1 | Before seeing outcomes, plans A versus B and A versus C only |
| Analyst 2 | Before seeing outcomes, plans all five displayed comparisons |
| Analyst 3 | Before seeing outcomes, plans A versus D only |
| Analyst 4 | Plans all five, then drops the comparison with the largest p-value after seeing outcomes |
| Analyst 5 | Makes no prior choice, inspects all five, then reports only the smallest p-value |

(a) For each analyst, define the comparison family that must be protected and explain why its size is 1, 2, or 5. (b) Calculate the analyst's Bonferroni threshold for familywise $\alpha=0.05$. (c) Identify which of that analyst's reported comparisons meet the threshold. (d) Explain why dropping or selecting a comparison after seeing outcomes does not make the family smaller or turn a comparison into a planned one. (e) State what each analyst would have needed to document before viewing outcomes.

### T08-A06-V08: Sound settings

Five analysts receive the same five unadjusted results.

| Comparison | Unadjusted p-value |
|---|---|
| A versus B | 0.003 |
| A versus C | 0.014 |
| A versus D | 0.039 |
| B versus C | 0.140 |
| B versus D | 0.410 |

Their stated plans are:

| Analyst | Decision process |
|---|---|
| Analyst 1 | Before seeing outcomes, plans A versus B and A versus C only |
| Analyst 2 | Before seeing outcomes, plans all five displayed comparisons |
| Analyst 3 | Before seeing outcomes, plans A versus D only |
| Analyst 4 | Plans all five, then drops the comparison with the largest p-value after seeing outcomes |
| Analyst 5 | Makes no prior choice, inspects all five, then reports only the smallest p-value |

(a) For each analyst, define the comparison family that must be protected and explain why its size is 1, 2, or 5. (b) Calculate the analyst's Bonferroni threshold for familywise $\alpha=0.05$. (c) Identify which of that analyst's reported comparisons meet the threshold. (d) Explain why dropping or selecting a comparison after seeing outcomes does not make the family smaller or turn a comparison into a planned one. (e) State what each analyst would have needed to document before viewing outcomes.

### T08-A06-V09: Navigation aids

Five analysts receive the same five unadjusted results.

| Comparison | Unadjusted p-value |
|---|---|
| A versus B | 0.007 |
| A versus C | 0.016 |
| A versus D | 0.047 |
| B versus C | 0.088 |
| B versus D | 0.360 |

Their stated plans are:

| Analyst | Decision process |
|---|---|
| Analyst 1 | Before seeing outcomes, plans A versus B and A versus C only |
| Analyst 2 | Before seeing outcomes, plans all five displayed comparisons |
| Analyst 3 | Before seeing outcomes, plans A versus D only |
| Analyst 4 | Plans all five, then drops the comparison with the largest p-value after seeing outcomes |
| Analyst 5 | Makes no prior choice, inspects all five, then reports only the smallest p-value |

(a) For each analyst, define the comparison family that must be protected and explain why its size is 1, 2, or 5. (b) Calculate the analyst's Bonferroni threshold for familywise $\alpha=0.05$. (c) Identify which of that analyst's reported comparisons meet the threshold. (d) Explain why dropping or selecting a comparison after seeing outcomes does not make the family smaller or turn a comparison into a planned one. (e) State what each analyst would have needed to document before viewing outcomes.

### T08-A06-V10: Feedback schedules

Five analysts receive the same five unadjusted results.

| Comparison | Unadjusted p-value |
|---|---|
| A versus B | 0.005 |
| A versus C | 0.023 |
| A versus D | 0.035 |
| B versus C | 0.110 |
| B versus D | 0.250 |

Their stated plans are:

| Analyst | Decision process |
|---|---|
| Analyst 1 | Before seeing outcomes, plans A versus B and A versus C only |
| Analyst 2 | Before seeing outcomes, plans all five displayed comparisons |
| Analyst 3 | Before seeing outcomes, plans A versus D only |
| Analyst 4 | Plans all five, then drops the comparison with the largest p-value after seeing outcomes |
| Analyst 5 | Makes no prior choice, inspects all five, then reports only the smallest p-value |

(a) For each analyst, define the comparison family that must be protected and explain why its size is 1, 2, or 5. (b) Calculate the analyst's Bonferroni threshold for familywise $\alpha=0.05$. (c) Identify which of that analyst's reported comparisons meet the threshold. (d) Explain why dropping or selecting a comparison after seeing outcomes does not make the family smaller or turn a comparison into a planned one. (e) State what each analyst would have needed to document before viewing outcomes.

# Part II: Calculator Practice

## A02: Group Means, Sum-of-Squares Partition, and the One-Way F Test

### T08-A02-V01: Study routines and learning score

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

A constructed study records learning score in points.

| Group | Observations |
|---|---|
| Reference | 9, 11, 13, 15 |
| Planning | 13, 15, 17, 19 |
| Retrieval | 17, 19, 21, 23 |

(a) Calculate the three group means and the grand mean. (b) Calculate $SS_A$, $SS_e$, and $SS_{total}$. (c) Verify $SS_{total}=SS_A+SS_e$. (d) Complete the degrees of freedom, mean squares, and $F$ statistic. (e) At the 5% level, compare the result with the supplied critical value $F_{2,9}=4.26$ and interpret the decision.

### T08-A02-V02: Reading layouts and speed

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

A constructed study records reading speed in words per minute above baseline.

| Group | Observations |
|---|---|
| Narrow | 17, 19, 21, 23 |
| Standard | 19, 21, 23, 25 |
| Wide | 21, 23, 25, 27 |

(a) Calculate the three group means and the grand mean. (b) Calculate $SS_A$, $SS_e$, and $SS_{total}$. (c) Verify $SS_{total}=SS_A+SS_e$. (d) Complete the degrees of freedom, mean squares, and $F$ statistic. (e) At the 5% level, compare the result with the supplied critical value $F_{2,9}=4.26$ and interpret the decision.

### T08-A02-V03: Archive prompts and correct records

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

A constructed study records correctly retrieved records in records.

| Group | Observations |
|---|---|
| None | 12, 14, 16, 18 |
| Checklist | 12, 14, 16, 18 |
| Examples | 12, 14, 16, 18 |

(a) Calculate the three group means and the grand mean. (b) Calculate $SS_A$, $SS_e$, and $SS_{total}$. (c) Verify $SS_{total}=SS_A+SS_e$. (d) Complete the degrees of freedom, mean squares, and $F$ statistic. (e) At the 5% level, compare the result with the supplied critical value $F_{2,9}=4.26$ and interpret the decision.

### T08-A02-V04: Museum maps and route confidence

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

A constructed study records route-confidence score in points.

| Group | Observations |
|---|---|
| Text | 42, 44, 46, 48 |
| Icons | 47, 49, 51, 53 |
| Combined | 44, 46, 48, 50 |

(a) Calculate the three group means and the grand mean. (b) Calculate $SS_A$, $SS_e$, and $SS_{total}$. (c) Verify $SS_{total}=SS_A+SS_e$. (d) Complete the degrees of freedom, mean squares, and $F$ statistic. (e) At the 5% level, compare the result with the supplied critical value $F_{2,9}=4.26$ and interpret the decision.

### T08-A02-V05: Reminder timing and completion

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

A constructed study records completion score in points.

| Group | Observations |
|---|---|
| Morning | 27, 29, 31, 33 |
| Midday | 32, 34, 36, 38 |
| Evening | 36, 38, 40, 42 |

(a) Calculate the three group means and the grand mean. (b) Calculate $SS_A$, $SS_e$, and $SS_{total}$. (c) Verify $SS_{total}=SS_A+SS_e$. (d) Complete the degrees of freedom, mean squares, and $F$ statistic. (e) At the 5% level, compare the result with the supplied critical value $F_{2,9}=4.26$ and interpret the decision.

### T08-A02-V06: Note formats and argument detection

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

A constructed study records argument-detection score in points.

| Group | Observations |
|---|---|
| Free | 49, 51, 53, 55 |
| Outline | 53, 55, 57, 59 |
| Matrix | 58, 60, 62, 64 |

(a) Calculate the three group means and the grand mean. (b) Calculate $SS_A$, $SS_e$, and $SS_{total}$. (c) Verify $SS_{total}=SS_A+SS_e$. (d) Complete the degrees of freedom, mean squares, and $F$ statistic. (e) At the 5% level, compare the result with the supplied critical value $F_{2,9}=4.26$ and interpret the decision.

### T08-A02-V07: Practice spacing and recall

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

A constructed study records recall score in points.

| Group | Observations |
|---|---|
| Massed | 37, 39, 41, 43 |
| Two sessions | 40, 42, 44, 46 |
| Four sessions | 45, 47, 49, 51 |

(a) Calculate the three group means and the grand mean. (b) Calculate $SS_A$, $SS_e$, and $SS_{total}$. (c) Verify $SS_{total}=SS_A+SS_e$. (d) Complete the degrees of freedom, mean squares, and $F$ statistic. (e) At the 5% level, compare the result with the supplied critical value $F_{2,9}=4.26$ and interpret the decision.

### T08-A02-V08: Sound settings and focus

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

A constructed study records focus score in points.

| Group | Observations |
|---|---|
| Quiet | 67, 69, 71, 73 |
| Ambient | 65, 67, 69, 71 |
| Music | 60, 62, 64, 66 |

(a) Calculate the three group means and the grand mean. (b) Calculate $SS_A$, $SS_e$, and $SS_{total}$. (c) Verify $SS_{total}=SS_A+SS_e$. (d) Complete the degrees of freedom, mean squares, and $F$ statistic. (e) At the 5% level, compare the result with the supplied critical value $F_{2,9}=4.26$ and interpret the decision.

### T08-A02-V09: Route instructions and errors

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

A constructed study records navigation-error score in errors.

| Group | Observations |
|---|---|
| Text | 15, 17, 19, 21 |
| Map | 11, 13, 15, 17 |
| Text plus map | 7, 9, 11, 13 |

(a) Calculate the three group means and the grand mean. (b) Calculate $SS_A$, $SS_e$, and $SS_{total}$. (c) Verify $SS_{total}=SS_A+SS_e$. (d) Complete the degrees of freedom, mean squares, and $F$ statistic. (e) At the 5% level, compare the result with the supplied critical value $F_{2,9}=4.26$ and interpret the decision.

### T08-A02-V10: Feedback timing and revision quality

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

A constructed study records revision-quality score in points.

| Group | Observations |
|---|---|
| Immediate | 61, 63, 65, 67 |
| Next day | 64, 66, 68, 70 |
| One week | 62, 64, 66, 68 |

(a) Calculate the three group means and the grand mean. (b) Calculate $SS_A$, $SS_e$, and $SS_{total}$. (c) Verify $SS_{total}=SS_A+SS_e$. (d) Complete the degrees of freedom, mean squares, and $F$ statistic. (e) At the 5% level, compare the result with the supplied critical value $F_{2,9}=4.26$ and interpret the decision.

## A03: Reconstructing an ANOVA Table and Reading the Design

### T08-A03-V01: Randomized reading prompts

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

A randomized study has group sizes $n_i=(8, 8, 8)$. Its incomplete ANOVA table reports $SS_A=96$ and $SS_e=144$. (a) State the equal-means hypotheses. (b) Complete $SS_{total}$ and all three degrees of freedom. (c) Calculate both mean squares and $F$. (d) Compare $F$ with the supplied 5% critical value 3.44. (e) Identify whether the design is balanced and explain the limit on a causal conclusion.

### T08-A03-V02: Observed commuting modes

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

A nonrandomized observational study has group sizes $n_i=(10, 7, 9)$. Its incomplete ANOVA table reports $SS_A=45$ and $SS_e=210$. (a) State the equal-means hypotheses. (b) Complete $SS_{total}$ and all three degrees of freedom. (c) Calculate both mean squares and $F$. (d) Compare $F$ with the supplied 5% critical value 3.42. (e) Identify whether the design is balanced and explain the limit on a causal conclusion.

### T08-A03-V03: Randomized archive interfaces

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

A randomized study has group sizes $n_i=(6, 6, 6, 6)$. Its incomplete ANOVA table reports $SS_A=180$ and $SS_e=220$. (a) State the equal-means hypotheses. (b) Complete $SS_{total}$ and all three degrees of freedom. (c) Calculate both mean squares and $F$. (d) Compare $F$ with the supplied 5% critical value 3.10. (e) Identify whether the design is balanced and explain the limit on a causal conclusion.

### T08-A03-V04: Self-selected workshop tracks

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

A nonrandomized observational study has group sizes $n_i=(12, 12, 12)$. Its incomplete ANOVA table reports $SS_A=30$ and $SS_e=330$. (a) State the equal-means hypotheses. (b) Complete $SS_{total}$ and all three degrees of freedom. (c) Calculate both mean squares and $F$. (d) Compare $F$ with the supplied 5% critical value 3.28. (e) Identify whether the design is balanced and explain the limit on a causal conclusion.

### T08-A03-V05: Randomized reminder schedules

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

A randomized study has group sizes $n_i=(9, 9, 9)$. Its incomplete ANOVA table reports $SS_A=120$ and $SS_e=180$. (a) State the equal-means hypotheses. (b) Complete $SS_{total}$ and all three degrees of freedom. (c) Calculate both mean squares and $F$. (d) Compare $F$ with the supplied 5% critical value 3.35. (e) Identify whether the design is balanced and explain the limit on a causal conclusion.

### T08-A03-V06: Observed neighborhood types

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

A nonrandomized observational study has group sizes $n_i=(14, 9, 7)$. Its incomplete ANOVA table reports $SS_A=75$ and $SS_e=270$. (a) State the equal-means hypotheses. (b) Complete $SS_{total}$ and all three degrees of freedom. (c) Calculate both mean squares and $F$. (d) Compare $F$ with the supplied 5% critical value 3.35. (e) Identify whether the design is balanced and explain the limit on a causal conclusion.

### T08-A03-V07: Randomized caption styles

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

A randomized study has group sizes $n_i=(7, 7, 7, 7)$. Its incomplete ANOVA table reports $SS_A=210$ and $SS_e=252$. (a) State the equal-means hypotheses. (b) Complete $SS_{total}$ and all three degrees of freedom. (c) Calculate both mean squares and $F$. (d) Compare $F$ with the supplied 5% critical value 3.01. (e) Identify whether the design is balanced and explain the limit on a causal conclusion.

### T08-A03-V08: Chosen study locations

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

A nonrandomized observational study has group sizes $n_i=(11, 11, 8)$. Its incomplete ANOVA table reports $SS_A=54$ and $SS_e=243$. (a) State the equal-means hypotheses. (b) Complete $SS_{total}$ and all three degrees of freedom. (c) Calculate both mean squares and $F$. (d) Compare $F$ with the supplied 5% critical value 3.35. (e) Identify whether the design is balanced and explain the limit on a causal conclusion.

### T08-A03-V09: Randomized route maps

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

A randomized study has group sizes $n_i=(10, 10, 10)$. Its incomplete ANOVA table reports $SS_A=160$ and $SS_e=240$. (a) State the equal-means hypotheses. (b) Complete $SS_{total}$ and all three degrees of freedom. (c) Calculate both mean squares and $F$. (d) Compare $F$ with the supplied 5% critical value 3.35. (e) Identify whether the design is balanced and explain the limit on a causal conclusion.

### T08-A03-V10: Observed employment sectors

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

A nonrandomized observational study has group sizes $n_i=(8, 12, 10)$. Its incomplete ANOVA table reports $SS_A=40$ and $SS_e=260$. (a) State the equal-means hypotheses. (b) Complete $SS_{total}$ and all three degrees of freedom. (c) Calculate both mean squares and $F$. (d) Compare $F$ with the supplied 5% critical value 3.35. (e) Identify whether the design is balanced and explain the limit on a causal conclusion.

## A04: Simple Pairwise and Pooled Complex Contrasts

### T08-A04-V01: Four study routines

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

Four balanced groups have means (62, 66, 70, 74), $n=8$ per group, and pooled error mean square $MS_e=25$. (a) Verify that $c=(-1,1,0,0)$ is a contrast and calculate its estimate, standard error, and $t$ statistic. (b) Repeat for the pooled comparison $c=(-1,-1,1,1)$. (c) Translate both weight patterns into plain-language questions. (d) Explain why the larger numerical contrast estimate is not automatically the stronger standardized result.

### T08-A04-V02: Four reading layouts

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

Four balanced groups have means (48, 53, 55, 59), $n=8$ per group, and pooled error mean square $MS_e=16$. (a) Verify that $c=(-1,1,0,0)$ is a contrast and calculate its estimate, standard error, and $t$ statistic. (b) Repeat for the pooled comparison $c=(-1,-1,1,1)$. (c) Translate both weight patterns into plain-language questions. (d) Explain why the larger numerical contrast estimate is not automatically the stronger standardized result.

### T08-A04-V03: Four archive prompts

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

Four balanced groups have means (18, 21, 24, 23), $n=8$ per group, and pooled error mean square $MS_e=9$. (a) Verify that $c=(-1,1,0,0)$ is a contrast and calculate its estimate, standard error, and $t$ statistic. (b) Repeat for the pooled comparison $c=(-1,-1,1,1)$. (c) Translate both weight patterns into plain-language questions. (d) Explain why the larger numerical contrast estimate is not automatically the stronger standardized result.

### T08-A04-V04: Four museum routes

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

Four balanced groups have means (72, 69, 76, 80), $n=8$ per group, and pooled error mean square $MS_e=36$. (a) Verify that $c=(-1,1,0,0)$ is a contrast and calculate its estimate, standard error, and $t$ statistic. (b) Repeat for the pooled comparison $c=(-1,-1,1,1)$. (c) Translate both weight patterns into plain-language questions. (d) Explain why the larger numerical contrast estimate is not automatically the stronger standardized result.

### T08-A04-V05: Four reminder schedules

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

Four balanced groups have means (40, 45, 47, 52), $n=8$ per group, and pooled error mean square $MS_e=20$. (a) Verify that $c=(-1,1,0,0)$ is a contrast and calculate its estimate, standard error, and $t$ statistic. (b) Repeat for the pooled comparison $c=(-1,-1,1,1)$. (c) Translate both weight patterns into plain-language questions. (d) Explain why the larger numerical contrast estimate is not automatically the stronger standardized result.

### T08-A04-V06: Four note templates

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

Four balanced groups have means (58, 61, 67, 69), $n=8$ per group, and pooled error mean square $MS_e=24$. (a) Verify that $c=(-1,1,0,0)$ is a contrast and calculate its estimate, standard error, and $t$ statistic. (b) Repeat for the pooled comparison $c=(-1,-1,1,1)$. (c) Translate both weight patterns into plain-language questions. (d) Explain why the larger numerical contrast estimate is not automatically the stronger standardized result.

### T08-A04-V07: Four practice intervals

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

Four balanced groups have means (63, 68, 71, 77), $n=8$ per group, and pooled error mean square $MS_e=30$. (a) Verify that $c=(-1,1,0,0)$ is a contrast and calculate its estimate, standard error, and $t$ statistic. (b) Repeat for the pooled comparison $c=(-1,-1,1,1)$. (c) Translate both weight patterns into plain-language questions. (d) Explain why the larger numerical contrast estimate is not automatically the stronger standardized result.

### T08-A04-V08: Four sound settings

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

Four balanced groups have means (74, 70, 68, 65), $n=8$ per group, and pooled error mean square $MS_e=18$. (a) Verify that $c=(-1,1,0,0)$ is a contrast and calculate its estimate, standard error, and $t$ statistic. (b) Repeat for the pooled comparison $c=(-1,-1,1,1)$. (c) Translate both weight patterns into plain-language questions. (d) Explain why the larger numerical contrast estimate is not automatically the stronger standardized result.

### T08-A04-V09: Four navigation aids

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

Four balanced groups have means (51, 56, 60, 64), $n=8$ per group, and pooled error mean square $MS_e=22$. (a) Verify that $c=(-1,1,0,0)$ is a contrast and calculate its estimate, standard error, and $t$ statistic. (b) Repeat for the pooled comparison $c=(-1,-1,1,1)$. (c) Translate both weight patterns into plain-language questions. (d) Explain why the larger numerical contrast estimate is not automatically the stronger standardized result.

### T08-A04-V10: Four feedback schedules

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

Four balanced groups have means (66, 70, 73, 71), $n=8$ per group, and pooled error mean square $MS_e=28$. (a) Verify that $c=(-1,1,0,0)$ is a contrast and calculate its estimate, standard error, and $t$ statistic. (b) Repeat for the pooled comparison $c=(-1,-1,1,1)$. (c) Translate both weight patterns into plain-language questions. (d) Explain why the larger numerical contrast estimate is not automatically the stronger standardized result.

## A05: All Pairwise Comparisons and Bonferroni Protection

### T08-A05-V01: All pairs among 3 levels

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

An analyst wants every pairwise comparison among $k=3$ factor levels and wants the familywise Type I error rate no larger than 0.05. (a) Count the distinct pairs. (b) Calculate the Bonferroni per-test threshold. (c) Under the simplifying assumption of independent tests, calculate the familywise risk if every comparison instead used 0.05. (d) Explain why the Bonferroni guarantee does not require the pairwise tests to be independent.

### T08-A05-V02: All pairs among 4 levels

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

An analyst wants every pairwise comparison among $k=4$ factor levels and wants the familywise Type I error rate no larger than 0.05. (a) Count the distinct pairs. (b) Calculate the Bonferroni per-test threshold. (c) Under the simplifying assumption of independent tests, calculate the familywise risk if every comparison instead used 0.05. (d) Explain why the Bonferroni guarantee does not require the pairwise tests to be independent.

### T08-A05-V03: All pairs among 5 levels

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

An analyst wants every pairwise comparison among $k=5$ factor levels and wants the familywise Type I error rate no larger than 0.05. (a) Count the distinct pairs. (b) Calculate the Bonferroni per-test threshold. (c) Under the simplifying assumption of independent tests, calculate the familywise risk if every comparison instead used 0.05. (d) Explain why the Bonferroni guarantee does not require the pairwise tests to be independent.

### T08-A05-V04: All pairs among 6 levels

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

An analyst wants every pairwise comparison among $k=6$ factor levels and wants the familywise Type I error rate no larger than 0.05. (a) Count the distinct pairs. (b) Calculate the Bonferroni per-test threshold. (c) Under the simplifying assumption of independent tests, calculate the familywise risk if every comparison instead used 0.05. (d) Explain why the Bonferroni guarantee does not require the pairwise tests to be independent.

### T08-A05-V05: All pairs among 7 levels

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

An analyst wants every pairwise comparison among $k=7$ factor levels and wants the familywise Type I error rate no larger than 0.05. (a) Count the distinct pairs. (b) Calculate the Bonferroni per-test threshold. (c) Under the simplifying assumption of independent tests, calculate the familywise risk if every comparison instead used 0.05. (d) Explain why the Bonferroni guarantee does not require the pairwise tests to be independent.

### T08-A05-V06: All pairs among 8 levels

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

An analyst wants every pairwise comparison among $k=8$ factor levels and wants the familywise Type I error rate no larger than 0.05. (a) Count the distinct pairs. (b) Calculate the Bonferroni per-test threshold. (c) Under the simplifying assumption of independent tests, calculate the familywise risk if every comparison instead used 0.05. (d) Explain why the Bonferroni guarantee does not require the pairwise tests to be independent.

### T08-A05-V07: All pairs among 4 levels

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

An analyst wants every pairwise comparison among $k=4$ factor levels and wants the familywise Type I error rate no larger than 0.05. (a) Count the distinct pairs. (b) Calculate the Bonferroni per-test threshold. (c) Under the simplifying assumption of independent tests, calculate the familywise risk if every comparison instead used 0.05. (d) Explain why the Bonferroni guarantee does not require the pairwise tests to be independent.

### T08-A05-V08: All pairs among 5 levels

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

An analyst wants every pairwise comparison among $k=5$ factor levels and wants the familywise Type I error rate no larger than 0.05. (a) Count the distinct pairs. (b) Calculate the Bonferroni per-test threshold. (c) Under the simplifying assumption of independent tests, calculate the familywise risk if every comparison instead used 0.05. (d) Explain why the Bonferroni guarantee does not require the pairwise tests to be independent.

### T08-A05-V09: All pairs among 6 levels

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

An analyst wants every pairwise comparison among $k=6$ factor levels and wants the familywise Type I error rate no larger than 0.05. (a) Count the distinct pairs. (b) Calculate the Bonferroni per-test threshold. (c) Under the simplifying assumption of independent tests, calculate the familywise risk if every comparison instead used 0.05. (d) Explain why the Bonferroni guarantee does not require the pairwise tests to be independent.

### T08-A05-V10: All pairs among 7 levels

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

An analyst wants every pairwise comparison among $k=7$ factor levels and wants the familywise Type I error rate no larger than 0.05. (a) Count the distinct pairs. (b) Calculate the Bonferroni per-test threshold. (c) Under the simplifying assumption of independent tests, calculate the familywise risk if every comparison instead used 0.05. (d) Explain why the Bonferroni guarantee does not require the pairwise tests to be independent.

## A07: A Prespecified Trend Contrast

### T08-A07-V01: Practice sessions and recall

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

Four equally spaced ordered levels have means (52, 57, 63, 69), $n=10$ per level, and $MS_e=25$. Three analysts propose $c_1=(0,1,2,3)$, $c_2=(-3,-1,1,3)$, and $c_3=(0.5,-0.5,-0.5,0.5)$. (a) Sketch each weight sequence against the four ordered levels and state the pattern it represents. (b) Check which vectors satisfy the contrast condition that their weights sum to zero. (c) Repair $c_1$ by subtracting its mean weight from every entry, and explain why the repaired vector represents the same linear direction as $c_2$. (d) Use the valid linear-trend weights $c_2$ to calculate the weighted estimate, its standard error, and its $t$ statistic. (e) Compare $|t|$ with the supplied two-sided 5% critical value 2.028 and interpret the sign as an ordered pattern rather than proof of a perfectly linear relationship.

### T08-A07-V02: Reminder intensity and response

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

Four equally spaced ordered levels have means (44, 48, 51, 55), $n=10$ per level, and $MS_e=16$. Three analysts propose $c_1=(0,1,2,3)$, $c_2=(-3,-1,1,3)$, and $c_3=(0.5,-0.5,-0.5,0.5)$. (a) Sketch each weight sequence against the four ordered levels and state the pattern it represents. (b) Check which vectors satisfy the contrast condition that their weights sum to zero. (c) Repair $c_1$ by subtracting its mean weight from every entry, and explain why the repaired vector represents the same linear direction as $c_2$. (d) Use the valid linear-trend weights $c_2$ to calculate the weighted estimate, its standard error, and its $t$ statistic. (e) Compare $|t|$ with the supplied two-sided 5% critical value 2.028 and interpret the sign as an ordered pattern rather than proof of a perfectly linear relationship.

### T08-A07-V03: Reading guidance and comprehension

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

Four equally spaced ordered levels have means (61, 64, 68, 73), $n=10$ per level, and $MS_e=20$. Three analysts propose $c_1=(0,1,2,3)$, $c_2=(-3,-1,1,3)$, and $c_3=(0.5,-0.5,-0.5,0.5)$. (a) Sketch each weight sequence against the four ordered levels and state the pattern it represents. (b) Check which vectors satisfy the contrast condition that their weights sum to zero. (c) Repair $c_1$ by subtracting its mean weight from every entry, and explain why the repaired vector represents the same linear direction as $c_2$. (d) Use the valid linear-trend weights $c_2$ to calculate the weighted estimate, its standard error, and its $t$ statistic. (e) Compare $|t|$ with the supplied two-sided 5% critical value 2.028 and interpret the sign as an ordered pattern rather than proof of a perfectly linear relationship.

### T08-A07-V04: Archive examples and accuracy

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

Four equally spaced ordered levels have means (18, 20, 24, 27), $n=10$ per level, and $MS_e=9$. Three analysts propose $c_1=(0,1,2,3)$, $c_2=(-3,-1,1,3)$, and $c_3=(0.5,-0.5,-0.5,0.5)$. (a) Sketch each weight sequence against the four ordered levels and state the pattern it represents. (b) Check which vectors satisfy the contrast condition that their weights sum to zero. (c) Repair $c_1$ by subtracting its mean weight from every entry, and explain why the repaired vector represents the same linear direction as $c_2$. (d) Use the valid linear-trend weights $c_2$ to calculate the weighted estimate, its standard error, and its $t$ statistic. (e) Compare $|t|$ with the supplied two-sided 5% critical value 2.028 and interpret the sign as an ordered pattern rather than proof of a perfectly linear relationship.

### T08-A07-V05: Route rehearsal and confidence

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

Four equally spaced ordered levels have means (50, 56, 59, 66), $n=10$ per level, and $MS_e=24$. Three analysts propose $c_1=(0,1,2,3)$, $c_2=(-3,-1,1,3)$, and $c_3=(0.5,-0.5,-0.5,0.5)$. (a) Sketch each weight sequence against the four ordered levels and state the pattern it represents. (b) Check which vectors satisfy the contrast condition that their weights sum to zero. (c) Repair $c_1$ by subtracting its mean weight from every entry, and explain why the repaired vector represents the same linear direction as $c_2$. (d) Use the valid linear-trend weights $c_2$ to calculate the weighted estimate, its standard error, and its $t$ statistic. (e) Compare $|t|$ with the supplied two-sided 5% critical value 2.028 and interpret the sign as an ordered pattern rather than proof of a perfectly linear relationship.

### T08-A07-V06: Note structure and reasoning

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

Four equally spaced ordered levels have means (58, 62, 65, 71), $n=10$ per level, and $MS_e=18$. Three analysts propose $c_1=(0,1,2,3)$, $c_2=(-3,-1,1,3)$, and $c_3=(0.5,-0.5,-0.5,0.5)$. (a) Sketch each weight sequence against the four ordered levels and state the pattern it represents. (b) Check which vectors satisfy the contrast condition that their weights sum to zero. (c) Repair $c_1$ by subtracting its mean weight from every entry, and explain why the repaired vector represents the same linear direction as $c_2$. (d) Use the valid linear-trend weights $c_2$ to calculate the weighted estimate, its standard error, and its $t$ statistic. (e) Compare $|t|$ with the supplied two-sided 5% critical value 2.028 and interpret the sign as an ordered pattern rather than proof of a perfectly linear relationship.

### T08-A07-V07: Feedback frequency and revision

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

Four equally spaced ordered levels have means (63, 66, 70, 72), $n=10$ per level, and $MS_e=22$. Three analysts propose $c_1=(0,1,2,3)$, $c_2=(-3,-1,1,3)$, and $c_3=(0.5,-0.5,-0.5,0.5)$. (a) Sketch each weight sequence against the four ordered levels and state the pattern it represents. (b) Check which vectors satisfy the contrast condition that their weights sum to zero. (c) Repair $c_1$ by subtracting its mean weight from every entry, and explain why the repaired vector represents the same linear direction as $c_2$. (d) Use the valid linear-trend weights $c_2$ to calculate the weighted estimate, its standard error, and its $t$ statistic. (e) Compare $|t|$ with the supplied two-sided 5% critical value 2.028 and interpret the sign as an ordered pattern rather than proof of a perfectly linear relationship.

### T08-A07-V08: Ambient noise and focus

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

Four equally spaced ordered levels have means (74, 71, 68, 62), $n=10$ per level, and $MS_e=16$. Three analysts propose $c_1=(0,1,2,3)$, $c_2=(-3,-1,1,3)$, and $c_3=(0.5,-0.5,-0.5,0.5)$. (a) Sketch each weight sequence against the four ordered levels and state the pattern it represents. (b) Check which vectors satisfy the contrast condition that their weights sum to zero. (c) Repair $c_1$ by subtracting its mean weight from every entry, and explain why the repaired vector represents the same linear direction as $c_2$. (d) Use the valid linear-trend weights $c_2$ to calculate the weighted estimate, its standard error, and its $t$ statistic. (e) Compare $|t|$ with the supplied two-sided 5% critical value 2.028 and interpret the sign as an ordered pattern rather than proof of a perfectly linear relationship.

### T08-A07-V09: Navigation support and errors

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

Four equally spaced ordered levels have means (20, 17, 13, 9), $n=10$ per level, and $MS_e=12$. Three analysts propose $c_1=(0,1,2,3)$, $c_2=(-3,-1,1,3)$, and $c_3=(0.5,-0.5,-0.5,0.5)$. (a) Sketch each weight sequence against the four ordered levels and state the pattern it represents. (b) Check which vectors satisfy the contrast condition that their weights sum to zero. (c) Repair $c_1$ by subtracting its mean weight from every entry, and explain why the repaired vector represents the same linear direction as $c_2$. (d) Use the valid linear-trend weights $c_2$ to calculate the weighted estimate, its standard error, and its $t$ statistic. (e) Compare $|t|$ with the supplied two-sided 5% critical value 2.028 and interpret the sign as an ordered pattern rather than proof of a perfectly linear relationship.

### T08-A07-V10: Delay before feedback and retention

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

Four equally spaced ordered levels have means (72, 69, 65, 60), $n=10$ per level, and $MS_e=20$. Three analysts propose $c_1=(0,1,2,3)$, $c_2=(-3,-1,1,3)$, and $c_3=(0.5,-0.5,-0.5,0.5)$. (a) Sketch each weight sequence against the four ordered levels and state the pattern it represents. (b) Check which vectors satisfy the contrast condition that their weights sum to zero. (c) Repair $c_1$ by subtracting its mean weight from every entry, and explain why the repaired vector represents the same linear direction as $c_2$. (d) Use the valid linear-trend weights $c_2$ to calculate the weighted estimate, its standard error, and its $t$ statistic. (e) Compare $|t|$ with the supplied two-sided 5% critical value 2.028 and interpret the sign as an ordered pattern rather than proof of a perfectly linear relationship.

## A08: Cell Means, Marginal Means, and Interaction in a Two-Factor ANOVA

### T08-A08-V01: Captioning and practice

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

A balanced $2\times2$ study has $n=6$ observations per cell. The cell means, ordered as $A_0B_0,A_0B_1,A_1B_0,A_1B_1$, are (62, 68, 70, 76). Factor A is Captioning; factor B is Practice. The pooled error mean square is $MS_e=16$. (a) Calculate the two marginal means for each factor and the grand mean. (b) Describe both main-effect patterns and the interaction pattern. (c) State the three null hypotheses. (d) Reconstruct $SS_A$, $SS_B$, $SS_{AB}$, $SS_e$, their degrees of freedom, and the three $F$ ratios. (e) Draw a means plot with $B_0$ and $B_1$ on the horizontal axis and one labeled line for each level of factor A. Explain how parallel or nonparallel lines express the interaction result.

### T08-A08-V02: Map and route rehearsal

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

A balanced $2\times2$ study has $n=6$ observations per cell. The cell means, ordered as $A_0B_0,A_0B_1,A_1B_0,A_1B_1$, are (54, 60, 58, 70). Factor A is Map; factor B is Rehearsal. The pooled error mean square is $MS_e=20$. (a) Calculate the two marginal means for each factor and the grand mean. (b) Describe both main-effect patterns and the interaction pattern. (c) State the three null hypotheses. (d) Reconstruct $SS_A$, $SS_B$, $SS_{AB}$, $SS_e$, their degrees of freedom, and the three $F$ ratios. (e) Draw a means plot with $B_0$ and $B_1$ on the horizontal axis and one labeled line for each level of factor A. Explain how parallel or nonparallel lines express the interaction result.

### T08-A08-V03: Quiet room and checklist

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

A balanced $2\times2$ study has $n=6$ observations per cell. The cell means, ordered as $A_0B_0,A_0B_1,A_1B_0,A_1B_1$, are (65, 71, 69, 75). Factor A is Quiet room; factor B is Checklist. The pooled error mean square is $MS_e=18$. (a) Calculate the two marginal means for each factor and the grand mean. (b) Describe both main-effect patterns and the interaction pattern. (c) State the three null hypotheses. (d) Reconstruct $SS_A$, $SS_B$, $SS_{AB}$, $SS_e$, their degrees of freedom, and the three $F$ ratios. (e) Draw a means plot with $B_0$ and $B_1$ on the horizontal axis and one labeled line for each level of factor A. Explain how parallel or nonparallel lines express the interaction result.

### T08-A08-V04: Prompt and feedback

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

A balanced $2\times2$ study has $n=6$ observations per cell. The cell means, ordered as $A_0B_0,A_0B_1,A_1B_0,A_1B_1$, are (50, 59, 56, 61). Factor A is Prompt; factor B is Feedback. The pooled error mean square is $MS_e=15$. (a) Calculate the two marginal means for each factor and the grand mean. (b) Describe both main-effect patterns and the interaction pattern. (c) State the three null hypotheses. (d) Reconstruct $SS_A$, $SS_B$, $SS_{AB}$, $SS_e$, their degrees of freedom, and the three $F$ ratios. (e) Draw a means plot with $B_0$ and $B_1$ on the horizontal axis and one labeled line for each level of factor A. Explain how parallel or nonparallel lines express the interaction result.

### T08-A08-V05: Icons and examples

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

A balanced $2\times2$ study has $n=6$ observations per cell. The cell means, ordered as $A_0B_0,A_0B_1,A_1B_0,A_1B_1$, are (72, 74, 76, 83). Factor A is Icons; factor B is Examples. The pooled error mean square is $MS_e=24$. (a) Calculate the two marginal means for each factor and the grand mean. (b) Describe both main-effect patterns and the interaction pattern. (c) State the three null hypotheses. (d) Reconstruct $SS_A$, $SS_B$, $SS_{AB}$, $SS_e$, their degrees of freedom, and the three $F$ ratios. (e) Draw a means plot with $B_0$ and $B_1$ on the horizontal axis and one labeled line for each level of factor A. Explain how parallel or nonparallel lines express the interaction result.

### T08-A08-V06: Planning and self-testing

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

A balanced $2\times2$ study has $n=6$ observations per cell. The cell means, ordered as $A_0B_0,A_0B_1,A_1B_0,A_1B_1$, are (60, 67, 66, 78). Factor A is Planning; factor B is Self-testing. The pooled error mean square is $MS_e=21$. (a) Calculate the two marginal means for each factor and the grand mean. (b) Describe both main-effect patterns and the interaction pattern. (c) State the three null hypotheses. (d) Reconstruct $SS_A$, $SS_B$, $SS_{AB}$, $SS_e$, their degrees of freedom, and the three $F$ ratios. (e) Draw a means plot with $B_0$ and $B_1$ on the horizontal axis and one labeled line for each level of factor A. Explain how parallel or nonparallel lines express the interaction result.

### T08-A08-V07: Lighting and background sound

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

A balanced $2\times2$ study has $n=6$ observations per cell. The cell means, ordered as $A_0B_0,A_0B_1,A_1B_0,A_1B_1$, are (74, 67, 70, 65). Factor A is Bright light; factor B is Sound. The pooled error mean square is $MS_e=17$. (a) Calculate the two marginal means for each factor and the grand mean. (b) Describe both main-effect patterns and the interaction pattern. (c) State the three null hypotheses. (d) Reconstruct $SS_A$, $SS_B$, $SS_{AB}$, $SS_e$, their degrees of freedom, and the three $F$ ratios. (e) Draw a means plot with $B_0$ and $B_1$ on the horizontal axis and one labeled line for each level of factor A. Explain how parallel or nonparallel lines express the interaction result.

### T08-A08-V08: Orientation and signs

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

A balanced $2\times2$ study has $n=6$ observations per cell. The cell means, ordered as $A_0B_0,A_0B_1,A_1B_0,A_1B_1$, are (48, 55, 59, 68). Factor A is Orientation; factor B is Signs. The pooled error mean square is $MS_e=19$. (a) Calculate the two marginal means for each factor and the grand mean. (b) Describe both main-effect patterns and the interaction pattern. (c) State the three null hypotheses. (d) Reconstruct $SS_A$, $SS_B$, $SS_{AB}$, $SS_e$, their degrees of freedom, and the three $F$ ratios. (e) Draw a means plot with $B_0$ and $B_1$ on the horizontal axis and one labeled line for each level of factor A. Explain how parallel or nonparallel lines express the interaction result.

### T08-A08-V09: Spacing and retrieval cues

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

A balanced $2\times2$ study has $n=6$ observations per cell. The cell means, ordered as $A_0B_0,A_0B_1,A_1B_0,A_1B_1$, are (64, 72, 69, 80). Factor A is Spacing; factor B is Retrieval cues. The pooled error mean square is $MS_e=23$. (a) Calculate the two marginal means for each factor and the grand mean. (b) Describe both main-effect patterns and the interaction pattern. (c) State the three null hypotheses. (d) Reconstruct $SS_A$, $SS_B$, $SS_{AB}$, $SS_e$, their degrees of freedom, and the three $F$ ratios. (e) Draw a means plot with $B_0$ and $B_1$ on the horizontal axis and one labeled line for each level of factor A. Explain how parallel or nonparallel lines express the interaction result.

### T08-A08-V10: Template and peer review

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

A balanced $2\times2$ study has $n=6$ observations per cell. The cell means, ordered as $A_0B_0,A_0B_1,A_1B_0,A_1B_1$, are (57, 66, 63, 74). Factor A is Template; factor B is Peer review. The pooled error mean square is $MS_e=20$. (a) Calculate the two marginal means for each factor and the grand mean. (b) Describe both main-effect patterns and the interaction pattern. (c) State the three null hypotheses. (d) Reconstruct $SS_A$, $SS_B$, $SS_{AB}$, $SS_e$, their degrees of freedom, and the three $F$ ratios. (e) Draw a means plot with $B_0$ and $B_1$ on the horizontal axis and one labeled line for each level of factor A. Explain how parallel or nonparallel lines express the interaction result.

## A09: Fixed and Random Factors, Variance Components, and the ICC

### T08-A09-V01: Libraries sampled from a regional population

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

A study includes a random sample of library levels from a wider population and also includes three deliberately chosen interface designs. For the balanced one-way analysis of the random library factor, $n=5$ observations occur at every sampled level, $MS_A=18$, and $MS_e=6$. (a) Explain why the library factor is random and the other factor is fixed. (b) State the population target of the random-factor analysis. (c) Estimate the between-level and error variance components. (d) Calculate and interpret the one-way ICC. (e) State why this formula should not be applied automatically to every grouped design.

### T08-A09-V02: Schools sampled from a district

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

A study includes a random sample of school levels from a wider population and also includes two named teaching programs. For the balanced one-way analysis of the random school factor, $n=6$ observations occur at every sampled level, $MS_A=20$, and $MS_e=5$. (a) Explain why the school factor is random and the other factor is fixed. (b) State the population target of the random-factor analysis. (c) Estimate the between-level and error variance components. (d) Calculate and interpret the one-way ICC. (e) State why this formula should not be applied automatically to every grouped design.

### T08-A09-V03: Interviewers sampled from a trained pool

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

A study includes a random sample of interviewer levels from a wider population and also includes three fixed questionnaire versions. For the balanced one-way analysis of the random interviewer factor, $n=4$ observations occur at every sampled level, $MS_A=15$, and $MS_e=7$. (a) Explain why the interviewer factor is random and the other factor is fixed. (b) State the population target of the random-factor analysis. (c) Estimate the between-level and error variance components. (d) Calculate and interpret the one-way ICC. (e) State why this formula should not be applied automatically to every grouped design.

### T08-A09-V04: Neighborhoods sampled from a city

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

A study includes a random sample of neighborhood levels from a wider population and also includes two selected outreach messages. For the balanced one-way analysis of the random neighborhood factor, $n=8$ observations occur at every sampled level, $MS_A=24$, and $MS_e=8$. (a) Explain why the neighborhood factor is random and the other factor is fixed. (b) State the population target of the random-factor analysis. (c) Estimate the between-level and error variance components. (d) Calculate and interpret the one-way ICC. (e) State why this formula should not be applied automatically to every grouped design.

### T08-A09-V05: Museum guides sampled from the staff roster

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

A study includes a random sample of guide levels from a wider population and also includes four fixed tour scripts. For the balanced one-way analysis of the random guide factor, $n=5$ observations occur at every sampled level, $MS_A=21$, and $MS_e=6$. (a) Explain why the guide factor is random and the other factor is fixed. (b) State the population target of the random-factor analysis. (c) Estimate the between-level and error variance components. (d) Calculate and interpret the one-way ICC. (e) State why this formula should not be applied automatically to every grouped design.

### T08-A09-V06: Archive boxes sampled from a collection

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

A study includes a random sample of archive box levels from a wider population and also includes three chosen scanning settings. For the balanced one-way analysis of the random archive box factor, $n=7$ observations occur at every sampled level, $MS_A=19$, and $MS_e=5$. (a) Explain why the archive box factor is random and the other factor is fixed. (b) State the population target of the random-factor analysis. (c) Estimate the between-level and error variance components. (d) Calculate and interpret the one-way ICC. (e) State why this formula should not be applied automatically to every grouped design.

### T08-A09-V07: Tutorial groups sampled from a program

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

A study includes a random sample of tutorial group levels from a wider population and also includes two fixed practice schedules. For the balanced one-way analysis of the random tutorial group factor, $n=6$ observations occur at every sampled level, $MS_A=17$, and $MS_e=7$. (a) Explain why the tutorial group factor is random and the other factor is fixed. (b) State the population target of the random-factor analysis. (c) Estimate the between-level and error variance components. (d) Calculate and interpret the one-way ICC. (e) State why this formula should not be applied automatically to every grouped design.

### T08-A09-V08: Routes sampled from a transport network

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

A study includes a random sample of route levels from a wider population and also includes three selected sign designs. For the balanced one-way analysis of the random route factor, $n=9$ observations occur at every sampled level, $MS_A=27$, and $MS_e=9$. (a) Explain why the route factor is random and the other factor is fixed. (b) State the population target of the random-factor analysis. (c) Estimate the between-level and error variance components. (d) Calculate and interpret the one-way ICC. (e) State why this formula should not be applied automatically to every grouped design.

### T08-A09-V09: Workshops sampled from an annual series

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

A study includes a random sample of workshop levels from a wider population and also includes two named facilitation formats. For the balanced one-way analysis of the random workshop factor, $n=5$ observations occur at every sampled level, $MS_A=16$, and $MS_e=4$. (a) Explain why the workshop factor is random and the other factor is fixed. (b) State the population target of the random-factor analysis. (c) Estimate the between-level and error variance components. (d) Calculate and interpret the one-way ICC. (e) State why this formula should not be applied automatically to every grouped design.

### T08-A09-V10: Days sampled from a semester

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

A study includes a random sample of day levels from a wider population and also includes three fixed reminder messages. For the balanced one-way analysis of the random day factor, $n=8$ observations occur at every sampled level, $MS_A=22$, and $MS_e=6$. (a) Explain why the day factor is random and the other factor is fixed. (b) State the population target of the random-factor analysis. (c) Estimate the between-level and error variance components. (d) Calculate and interpret the one-way ICC. (e) State why this formula should not be applied automatically to every grouped design.

## A10: Repeated Measures, Sphericity, and Greenhouse-Geisser Correction

### T08-A10-V01: Reading at three occasions

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

Twelve people are measured under three conditions. The sample variances and correlations are:

| Summary quantity | Value |
|---|---|
| Variance at condition 1 | 32.0000 |
| Variance at condition 2 | 32.0000 |
| Variance at condition 3 | 32.0000 |
| Correlation 1 with 2 | 0.7188 |
| Correlation 1 with 3 | 0.7031 |
| Correlation 2 with 3 | 0.6875 |

The repeated-measures table provides $SS_{condition}=84$, $SS_{person}=176$, and $SS_e=132$ with degrees of freedom 2, 11, and 22. A Greenhouse-Geisser estimate is $\widehat{\varepsilon}=0.82$. (a) Use $s_{j-k}^2=s_j^2+s_k^2-2r_{jk}s_js_k$ to calculate the three pairwise difference-score variances. Explain what sphericity asks and assess the pattern descriptively. (b) State the null hypotheses for the condition effect and person variation. Complete the three mean squares, calculate both $F_{condition}$ and $F_{person}$, obtain their upper-tail p-values, and interpret both decisions. (c) Estimate the person variance component and ICC. (d) Calculate the Greenhouse-Geisser-corrected condition and error degrees of freedom and the corrected p-value. (e) Explain what the correction changes, what remains unchanged, and why repeated rows do not become independent.

### T08-A10-V02: Focus under three sound settings

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

Twelve people are measured under three conditions. The sample variances and correlations are:

| Summary quantity | Value |
|---|---|
| Variance at condition 1 | 43.0000 |
| Variance at condition 2 | 43.0000 |
| Variance at condition 3 | 43.0000 |
| Correlation 1 with 2 | 0.8605 |
| Correlation 1 with 3 | 0.7442 |
| Correlation 2 with 3 | 0.6395 |

The repeated-measures table provides $SS_{condition}=66$, $SS_{person}=154$, and $SS_e=110$ with degrees of freedom 2, 11, and 22. A Greenhouse-Geisser estimate is $\widehat{\varepsilon}=0.74$. (a) Use $s_{j-k}^2=s_j^2+s_k^2-2r_{jk}s_js_k$ to calculate the three pairwise difference-score variances. Explain what sphericity asks and assess the pattern descriptively. (b) State the null hypotheses for the condition effect and person variation. Complete the three mean squares, calculate both $F_{condition}$ and $F_{person}$, obtain their upper-tail p-values, and interpret both decisions. (c) Estimate the person variance component and ICC. (d) Calculate the Greenhouse-Geisser-corrected condition and error degrees of freedom and the corrected p-value. (e) Explain what the correction changes, what remains unchanged, and why repeated rows do not become independent.

### T08-A10-V03: Recall across three delays

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

Twelve people are measured under three conditions. The sample variances and correlations are:

| Summary quantity | Value |
|---|---|
| Variance at condition 1 | 29.0000 |
| Variance at condition 2 | 29.0000 |
| Variance at condition 3 | 29.0000 |
| Correlation 1 with 2 | 0.7241 |
| Correlation 1 with 3 | 0.7069 |
| Correlation 2 with 3 | 0.7414 |

The repeated-measures table provides $SS_{condition}=72$, $SS_{person}=198$, and $SS_e=121$ with degrees of freedom 2, 11, and 22. A Greenhouse-Geisser estimate is $\widehat{\varepsilon}=0.91$. (a) Use $s_{j-k}^2=s_j^2+s_k^2-2r_{jk}s_js_k$ to calculate the three pairwise difference-score variances. Explain what sphericity asks and assess the pattern descriptively. (b) State the null hypotheses for the condition effect and person variation. Complete the three mean squares, calculate both $F_{condition}$ and $F_{person}$, obtain their upper-tail p-values, and interpret both decisions. (c) Estimate the person variance component and ICC. (d) Calculate the Greenhouse-Geisser-corrected condition and error degrees of freedom and the corrected p-value. (e) Explain what the correction changes, what remains unchanged, and why repeated rows do not become independent.

### T08-A10-V04: Navigation across three route trials

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

Twelve people are measured under three conditions. The sample variances and correlations are:

| Summary quantity | Value |
|---|---|
| Variance at condition 1 | 50.0000 |
| Variance at condition 2 | 50.0000 |
| Variance at condition 3 | 50.0000 |
| Correlation 1 with 2 | 0.9000 |
| Correlation 1 with 3 | 0.7500 |
| Correlation 2 with 3 | 0.6200 |

The repeated-measures table provides $SS_{condition}=90$, $SS_{person}=165$, and $SS_e=143$ with degrees of freedom 2, 11, and 22. A Greenhouse-Geisser estimate is $\widehat{\varepsilon}=0.68$. (a) Use $s_{j-k}^2=s_j^2+s_k^2-2r_{jk}s_js_k$ to calculate the three pairwise difference-score variances. Explain what sphericity asks and assess the pattern descriptively. (b) State the null hypotheses for the condition effect and person variation. Complete the three mean squares, calculate both $F_{condition}$ and $F_{person}$, obtain their upper-tail p-values, and interpret both decisions. (c) Estimate the person variance component and ICC. (d) Calculate the Greenhouse-Geisser-corrected condition and error degrees of freedom and the corrected p-value. (e) Explain what the correction changes, what remains unchanged, and why repeated rows do not become independent.

### T08-A10-V05: Confidence at three course points

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

Twelve people are measured under three conditions. The sample variances and correlations are:

| Summary quantity | Value |
|---|---|
| Variance at condition 1 | 33.0000 |
| Variance at condition 2 | 33.0000 |
| Variance at condition 3 | 33.0000 |
| Correlation 1 with 2 | 0.6970 |
| Correlation 1 with 3 | 0.6818 |
| Correlation 2 with 3 | 0.7121 |

The repeated-measures table provides $SS_{condition}=78$, $SS_{person}=187$, and $SS_e=126$ with degrees of freedom 2, 11, and 22. A Greenhouse-Geisser estimate is $\widehat{\varepsilon}=0.88$. (a) Use $s_{j-k}^2=s_j^2+s_k^2-2r_{jk}s_js_k$ to calculate the three pairwise difference-score variances. Explain what sphericity asks and assess the pattern descriptively. (b) State the null hypotheses for the condition effect and person variation. Complete the three mean squares, calculate both $F_{condition}$ and $F_{person}$, obtain their upper-tail p-values, and interpret both decisions. (c) Estimate the person variance component and ICC. (d) Calculate the Greenhouse-Geisser-corrected condition and error degrees of freedom and the corrected p-value. (e) Explain what the correction changes, what remains unchanged, and why repeated rows do not become independent.

### T08-A10-V06: Accuracy under three interfaces

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

Twelve people are measured under three conditions. The sample variances and correlations are:

| Summary quantity | Value |
|---|---|
| Variance at condition 1 | 47.0000 |
| Variance at condition 2 | 47.0000 |
| Variance at condition 3 | 47.0000 |
| Correlation 1 with 2 | 0.8511 |
| Correlation 1 with 3 | 0.7021 |
| Correlation 2 with 3 | 0.6277 |

The repeated-measures table provides $SS_{condition}=81$, $SS_{person}=143$, and $SS_e=119$ with degrees of freedom 2, 11, and 22. A Greenhouse-Geisser estimate is $\widehat{\varepsilon}=0.71$. (a) Use $s_{j-k}^2=s_j^2+s_k^2-2r_{jk}s_js_k$ to calculate the three pairwise difference-score variances. Explain what sphericity asks and assess the pattern descriptively. (b) State the null hypotheses for the condition effect and person variation. Complete the three mean squares, calculate both $F_{condition}$ and $F_{person}$, obtain their upper-tail p-values, and interpret both decisions. (c) Estimate the person variance component and ICC. (d) Calculate the Greenhouse-Geisser-corrected condition and error degrees of freedom and the corrected p-value. (e) Explain what the correction changes, what remains unchanged, and why repeated rows do not become independent.

### T08-A10-V07: Response time across three reminders

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

Twelve people are measured under three conditions. The sample variances and correlations are:

| Summary quantity | Value |
|---|---|
| Variance at condition 1 | 38.0000 |
| Variance at condition 2 | 38.0000 |
| Variance at condition 3 | 38.0000 |
| Correlation 1 with 2 | 0.6842 |
| Correlation 1 with 3 | 0.6974 |
| Correlation 2 with 3 | 0.6579 |

The repeated-measures table provides $SS_{condition}=63$, $SS_{person}=209$, and $SS_e=138$ with degrees of freedom 2, 11, and 22. A Greenhouse-Geisser estimate is $\widehat{\varepsilon}=0.95$. (a) Use $s_{j-k}^2=s_j^2+s_k^2-2r_{jk}s_js_k$ to calculate the three pairwise difference-score variances. Explain what sphericity asks and assess the pattern descriptively. (b) State the null hypotheses for the condition effect and person variation. Complete the three mean squares, calculate both $F_{condition}$ and $F_{person}$, obtain their upper-tail p-values, and interpret both decisions. (c) Estimate the person variance component and ICC. (d) Calculate the Greenhouse-Geisser-corrected condition and error degrees of freedom and the corrected p-value. (e) Explain what the correction changes, what remains unchanged, and why repeated rows do not become independent.

### T08-A10-V08: Comprehension across three formats

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

Twelve people are measured under three conditions. The sample variances and correlations are:

| Summary quantity | Value |
|---|---|
| Variance at condition 1 | 46.0000 |
| Variance at condition 2 | 46.0000 |
| Variance at condition 3 | 46.0000 |
| Correlation 1 with 2 | 0.8804 |
| Correlation 1 with 3 | 0.7826 |
| Correlation 2 with 3 | 0.6304 |

The repeated-measures table provides $SS_{condition}=96$, $SS_{person}=176$, and $SS_e=154$ with degrees of freedom 2, 11, and 22. A Greenhouse-Geisser estimate is $\widehat{\varepsilon}=0.65$. (a) Use $s_{j-k}^2=s_j^2+s_k^2-2r_{jk}s_js_k$ to calculate the three pairwise difference-score variances. Explain what sphericity asks and assess the pattern descriptively. (b) State the null hypotheses for the condition effect and person variation. Complete the three mean squares, calculate both $F_{condition}$ and $F_{person}$, obtain their upper-tail p-values, and interpret both decisions. (c) Estimate the person variance component and ICC. (d) Calculate the Greenhouse-Geisser-corrected condition and error degrees of freedom and the corrected p-value. (e) Explain what the correction changes, what remains unchanged, and why repeated rows do not become independent.

### T08-A10-V09: Revision quality at three drafts

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

Twelve people are measured under three conditions. The sample variances and correlations are:

| Summary quantity | Value |
|---|---|
| Variance at condition 1 | 30.0000 |
| Variance at condition 2 | 30.0000 |
| Variance at condition 3 | 30.0000 |
| Correlation 1 with 2 | 0.7167 |
| Correlation 1 with 3 | 0.7000 |
| Correlation 2 with 3 | 0.7333 |

The repeated-measures table provides $SS_{condition}=75$, $SS_{person}=220$, and $SS_e=132$ with degrees of freedom 2, 11, and 22. A Greenhouse-Geisser estimate is $\widehat{\varepsilon}=0.90$. (a) Use $s_{j-k}^2=s_j^2+s_k^2-2r_{jk}s_js_k$ to calculate the three pairwise difference-score variances. Explain what sphericity asks and assess the pattern descriptively. (b) State the null hypotheses for the condition effect and person variation. Complete the three mean squares, calculate both $F_{condition}$ and $F_{person}$, obtain their upper-tail p-values, and interpret both decisions. (c) Estimate the person variance component and ICC. (d) Calculate the Greenhouse-Geisser-corrected condition and error degrees of freedom and the corrected p-value. (e) Explain what the correction changes, what remains unchanged, and why repeated rows do not become independent.

### T08-A10-V10: Search skill at three practice points

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

Twelve people are measured under three conditions. The sample variances and correlations are:

| Summary quantity | Value |
|---|---|
| Variance at condition 1 | 52.0000 |
| Variance at condition 2 | 52.0000 |
| Variance at condition 3 | 52.0000 |
| Correlation 1 with 2 | 0.8750 |
| Correlation 1 with 3 | 0.7500 |
| Correlation 2 with 3 | 0.6154 |

The repeated-measures table provides $SS_{condition}=87$, $SS_{person}=187$, and $SS_e=143$ with degrees of freedom 2, 11, and 22. A Greenhouse-Geisser estimate is $\widehat{\varepsilon}=0.70$. (a) Use $s_{j-k}^2=s_j^2+s_k^2-2r_{jk}s_js_k$ to calculate the three pairwise difference-score variances. Explain what sphericity asks and assess the pattern descriptively. (b) State the null hypotheses for the condition effect and person variation. Complete the three mean squares, calculate both $F_{condition}$ and $F_{person}$, obtain their upper-tail p-values, and interpret both decisions. (c) Estimate the person variance component and ICC. (d) Calculate the Greenhouse-Geisser-corrected condition and error degrees of freedom and the corrected p-value. (e) Explain what the correction changes, what remains unchanged, and why repeated rows do not become independent.
