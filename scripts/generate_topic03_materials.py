#!/usr/bin/env python3
"""Generate Ratiomera's multilingual Topic 3 practice pair.

The registered worksheets determine the twelve learning objectives only. All
contexts, wording, values, calculations, and explanations in this generator
are newly authored for Ratiomera. English remains canonical; the reviewed German
and Albanian adaptations reuse its identifiers, values, formulas, and results.
"""

from __future__ import annotations

import argparse
import math

from intro_stats_practice_support import (
    group_heading,
    normal_cdf,
    normal_ppf,
    number,
    sample_mean,
    sample_variance,
    task,
    validate_sources_allowing_incomplete_locales,
    write_pair,
)


HYPOTHESIS_SCENARIOS = [
    ("Guided map practice", "mean route-planning score", "learners using guided map practice", "learners using the standard activity", "higher"),
    ("Quiet reading spaces", "mean reading-comprehension score", "students assigned a quiet reading room", "students assigned the usual room", "different"),
    ("Archive-search checklist", "mean number of correctly retrieved records", "learners using a search checklist", "learners using the ordinary instructions", "higher"),
    ("Short movement break", "mean sustained-attention score", "participants offered a short movement break", "participants following the usual schedule", "higher"),
    ("Captioned tutorial", "mean tutorial-comprehension score", "learners viewing a captioned tutorial", "learners viewing the same tutorial without captions", "different"),
    ("Reduced notification setting", "mean task-completion time", "participants using a reduced-notification setting", "participants using the standard setting", "lower"),
    ("Retrieval-practice cards", "mean delayed-recall score", "learners using retrieval-practice cards", "learners rereading the same material", "higher"),
    ("Museum orientation map", "mean number of navigation errors", "visitors receiving an orientation map", "visitors receiving the standard leaflet", "lower"),
    ("Peer explanation prompt", "mean concept-explanation score", "students receiving a peer-explanation prompt", "students receiving an individual review prompt", "different"),
    ("Structured note template", "mean number of correctly identified arguments", "learners using a structured note template", "learners taking notes in their usual way", "higher"),
]


RAW_DATA = [
    ("Daily reading minutes", "minutes", [32, 41, 28, 35, 46, 39, 31, 44, 37]),
    ("Archive requests completed", "requests", [7, 5, 8, 6, 9, 4, 7, 6]),
    ("Focus ratings", "points", [12, 15, 11, 13, 16, 14, 10, 15, 12, 14]),
    ("Museum visit durations", "minutes", [54, 61, 48, 57, 65, 52, 59, 63]),
    ("Correctly coded records", "records", [18, 21, 17, 20, 22, 19, 23, 16, 21]),
    ("Weekly practice hours", "hours", [4, 6, 5, 7, 3, 8, 5, 6, 4, 7]),
    ("Route-planning scores", "points", [68, 74, 71, 66, 79, 72, 70, 77, 69]),
    ("Response latencies", "seconds", [23, 19, 26, 21, 24, 18, 22, 25]),
    ("Completed diary prompts", "prompts", [9, 11, 8, 10, 12, 7, 9, 10, 11]),
    ("Catalog accuracy scores", "points", [84, 88, 81, 86, 90, 83, 87, 85]),
]


KNOWN_SIGMA_SAMPLES = [
    ("reading score", "points", 72, 12, [25, 49, 100, 400], [69, 74, 71, 73]),
    ("processing time", "minutes", 48, 10, [16, 36, 64, 144], [52, 46, 49, 47]),
    ("focus rating", "points", 60, 9, [25, 81, 121, 225], [57, 62, 61, 60]),
    ("visit duration", "minutes", 90, 18, [36, 64, 100, 324], [85, 94, 92, 89]),
    ("memory score", "points", 105, 15, [25, 49, 100, 225], [101, 108, 104, 106]),
    ("sound index", "points", 42, 8, [16, 64, 144, 256], [45, 40, 43, 42]),
    ("confidence score", "points", 55, 11, [25, 100, 121, 400], [51, 58, 56, 55]),
    ("response time", "milliseconds", 520, 80, [16, 64, 100, 256], [548, 505, 530, 518]),
    ("trust rating", "points", 50, 7, [25, 49, 196, 400], [47, 52, 51, 50]),
    ("accuracy score", "points", 86, 6, [36, 81, 144, 324], [84, 88, 87, 86]),
]


INTERVAL_WIDTH_CASES = [
    ("reading fluency", "points", 78, 12, 36, 9, 144),
    ("archive processing", "minutes", 44, 10, 25, 9, 100),
    ("wellbeing index", "points", 63, 15, 49, 16, 196),
    ("museum duration", "minutes", 96, 18, 64, 16, 256),
    ("memory score", "points", 108, 14, 36, 9, 144),
    ("sound level", "decibels", 39, 6, 25, 9, 100),
    ("course confidence", "points", 58, 10, 64, 16, 256),
    ("response latency", "milliseconds", 480, 72, 36, 9, 144),
    ("community trust", "points", 52, 8, 49, 16, 196),
    ("catalog accuracy", "points", 87, 7, 25, 9, 100),
]


ONE_SIDED_Z = [
    ("Guided route rehearsal", "route-planning score", "points", 70, 10, 25, 72, "higher"),
    ("Streamlined archive form", "completion time", "minutes", 45, 8, 36, 42, "lower"),
    ("Retrieval-practice prompts", "delayed-recall score", "points", 62, 12, 49, 64, "higher"),
    ("Orientation map", "navigation-error count", "errors", 8, 3, 25, 6.8, "lower"),
    ("Structured note template", "argument-identification score", "points", 55, 9, 36, 56.5, "higher"),
    ("Quiet work period", "task-switch count", "switches", 14, 4, 64, 12.8, "lower"),
    ("Captioned demonstration", "comprehension score", "points", 76, 11, 49, 78, "higher"),
    ("Reminder checklist", "missed-step count", "steps", 5, 2, 25, 4.1, "lower"),
    ("Peer explanation", "reasoning score", "points", 68, 10, 100, 69.2, "higher"),
    ("Reduced notifications", "completion time", "minutes", 52, 9, 81, 50.0, "lower"),
]


TWO_SIDED_Z = [
    ("Alternative reading layout", "reading speed", "words per minute", 210, 30, 64, 215),
    ("New catalog interface", "search time", "seconds", 75, 12, 49, 70),
    ("Ambient sound setting", "focus score", "points", 58, 10, 36, 60),
    ("Museum route markers", "visit duration", "minutes", 95, 18, 81, 89),
    ("Memory cue format", "recall score", "points", 72, 14, 49, 75),
    ("Survey reminder wording", "response delay", "hours", 30, 8, 64, 27),
    ("Workshop seating plan", "participation score", "points", 50, 9, 100, 51.2),
    ("Archive image contrast", "inspection time", "seconds", 42, 7, 49, 39.5),
    ("Route-description style", "navigation score", "points", 66, 12, 144, 67.5),
    ("Note-taking display", "concept score", "points", 80, 15, 100, 76.5),
]


POWER_CASES = [
    ("guided map practice", "score points", 70, 10, 36, 71.5, 4),
    ("an archive-search checklist", "correct records", 18, 5, 49, 20, 2.5),
    ("retrieval-practice cards", "score points", 60, 12, 64, 61.5, 4),
    ("a quiet reading room", "score points", 75, 14, 49, 78.5, 5),
    ("a structured note template", "arguments", 12, 3, 36, 12.5, 1.5),
    ("a captioned tutorial", "score points", 68, 9, 81, 70, 2.5),
    ("a reminder checklist", "completed steps", 20, 4, 49, 20.6, 2),
    ("peer explanation", "score points", 72, 11, 100, 74.1, 3),
    ("a museum orientation map", "route points", 50, 8, 64, 51, 2.5),
    ("a reduced-notification setting", "focus points", 55, 10, 100, 57.0, 3),
]


FULL_INFERENCE_Z = [
    ("Memory-support schedule", "memory score", "points", 65, 8, 64, 67.5),
    ("Revised search protocol", "search time", "seconds", 50, 10, 100, 48),
    ("New reading prompt", "reading-comprehension score", "points", 72, 12, 36, 74),
    ("Gallery route signs", "navigation time", "minutes", 40, 9, 81, 37.5),
    ("Concept-map format", "concept score", "points", 60, 10, 49, 61.5),
    ("Appointment reminder", "response delay", "hours", 24, 6, 64, 22),
    ("Peer-review structure", "revision score", "points", 55, 8, 100, 56),
    ("Document preview tool", "inspection time", "seconds", 35, 7, 49, 32.5),
    ("Route rehearsal card", "route-confidence score", "points", 70, 9, 144, 71),
    ("Annotation display", "argument score", "points", 48, 6, 100, 46.5),
]


T_PERCENTILES = [
    (5, 3.3649), (6, 3.1427), (7, 2.9980), (8, 2.8965), (9, 2.8214),
    (10, 2.7638), (11, 2.7181), (12, 2.6810), (15, 2.6025), (20, 2.5280),
]


ONE_SAMPLE_T = [
    ("guided search training", "search-accuracy score", "points", 70, 8, 76, 6.5, 1.8946),
    ("a shorter intake form", "completion time", "minutes", 45, 9, 41.5, 5.4, 1.8595),
    ("a retrieval cue", "recall score", "points", 62, 10, 66, 6.2, 1.8331),
    ("an orientation card", "navigation-error count", "errors", 9, 11, 7.1, 3.8, 1.8125),
    ("a structured note page", "argument score", "points", 54, 12, 57.5, 5.5, 1.7959),
    ("a quiet work block", "task-switch count", "switches", 15, 13, 13.0, 4.0, 1.7823),
    ("a captioned demonstration", "comprehension score", "points", 74, 14, 77.2, 6.0, 1.7709),
    ("a reminder checklist", "missed-step count", "steps", 6, 15, 4.9, 2.1, 1.7613),
    ("peer explanation", "reasoning score", "points", 67, 16, 69.6, 5.3, 1.7531),
    ("a reduced-notification setting", "completion time", "minutes", 50, 17, 47.8, 4.9, 1.7459),
]


T_INTERVALS = [
    ("reading fluency", "points", 8, 76, 7, 2.3646, 70),
    ("archive processing", "minutes", 9, 43, 6, 2.3060, 47),
    ("focus rating", "points", 10, 61, 8, 2.2622, 55),
    ("museum duration", "minutes", 11, 92, 15, 2.2281, 100),
    ("memory score", "points", 12, 106, 10, 2.2010, 100),
    ("sound index", "points", 13, 40, 5, 2.1788, 43),
    ("confidence score", "points", 14, 57, 7, 2.1604, 52),
    ("response latency", "milliseconds", 15, 490, 54, 2.1448, 520),
    ("trust rating", "points", 16, 51, 6, 2.1314, 48),
    ("catalog accuracy", "points", 17, 86, 5, 2.1199, 83),
]


POOLED_T = [
    ("guided versus self-directed map practice", "route-planning score", 10, 10, 74, 68, 36, 25, 1.7341),
    ("captioned versus uncaptioned tutorials", "comprehension score", 11, 11, 79, 74, 30, 28, 1.7247),
    ("quiet versus usual reading rooms", "reading score", 12, 12, 82, 76, 42, 35, 1.7171),
    ("checklist versus usual archive searches", "correctly retrieved records", 13, 13, 22, 19, 9, 12, 1.7109),
    ("structured versus free-form notes", "argument score", 14, 14, 61, 56, 28, 32, 1.7056),
    ("orientation map versus standard leaflet", "navigation score", 15, 15, 70, 65, 40, 36, 1.7011),
    ("peer explanation versus private rereading", "reasoning score", 16, 16, 73, 69, 25, 30, 1.6973),
    ("reduced versus usual notifications", "focus score", 17, 17, 64, 60, 34, 38, 1.6939),
    ("retrieval cards versus summary rereading", "delayed-recall score", 18, 18, 77, 72, 45, 41, 1.6909),
    ("visual versus text-only route guidance", "route-completion score", 19, 19, 81, 76, 50, 44, 1.6883),
]


def z_test(mean: float, null: float, sigma: float, n: int) -> float:
    return (mean - null) / (sigma / math.sqrt(n))


def render_english() -> tuple[list[str], list[str]]:
    ex: list[str] = []
    sol: list[str] = []

    ex_group = [group_heading(1, "Hypotheses and the Two Possible Errors")]
    sol_group = [group_heading(1, "Hypotheses and the Two Possible Errors")]
    for i, (title, outcome, treatment, comparison, direction) in enumerate(HYPOTHESIS_SCENARIOS, 1):
        if direction == "higher":
            alternative = "higher than"
            effect_description = "higher in the treatment population"
            symbols = "$H_0:\\mu_T\\leq\\mu_C$ and $H_1:\\mu_T>\\mu_C$"
        elif direction == "lower":
            alternative = "lower than"
            effect_description = "lower in the treatment population"
            symbols = "$H_0:\\mu_T\\geq\\mu_C$ and $H_1:\\mu_T<\\mu_C$"
        else:
            alternative = "different from"
            effect_description = "different between the two populations"
            symbols = "$H_0:\\mu_T=\\mu_C$ and $H_1:\\mu_T\\ne\\mu_C$"
        ex_group.append(task(3, 1, i, title, f"A fictional study asks whether the {outcome} for {treatment} is {alternative} the corresponding population mean for {comparison}. Let $\\mu_T$ and $\\mu_C$ denote those two population means. (a) Write the null and alternative hypotheses in words and symbols. (b) Explain a Type I error and a Type II error in this setting. (c) State why a test decision cannot reveal with certainty whether either error occurred."))
        sol_group.append(task(3, 1, i, title, f"A hypothesis concerns population means, not the two observed sample means. A suitable formulation is {symbols}. A Type I error would mean concluding that the population {outcome} is {effect_description} when the null hypothesis is true. A Type II error would mean failing to detect that the population {outcome} is {effect_description} when that relationship is genuinely present. The sample provides uncertain evidence rather than direct access to both population means. We therefore know the long-run error rates of the procedure under specified conditions, but the decision from one study does not come with a label telling us whether it was correct."))
    ex.append("".join(ex_group)); sol.append("".join(sol_group))

    ex_group = [group_heading(2, "Sample Estimates and the Standard Error")]
    sol_group = [group_heading(2, "Sample Estimates and the Standard Error")]
    for i, (title, unit, values) in enumerate(RAW_DATA, 1):
        rendered = ", ".join(str(v) for v in values)
        mean = sample_mean(values); variance = sample_variance(values); sd = math.sqrt(variance); se = sd / math.sqrt(len(values))
        ex_group.append(task(3, 2, i, title, f"A simple random sample records the following {len(values)} values in {unit}: {rendered}. (a) Calculate the sample mean $\\bar x$ and sample variance $s^2$. (b) Name the population parameters estimated by these two statistics. (c) Calculate the plug-in standard error $s/\\sqrt n$ and explain what it describes across repeated samples."))
        sol_group.append(task(3, 2, i, title, f"There are $n={len(values)}$ observations and their total is {number(sum(values), 2)}. Thus $\\bar x={number(sum(values),2)}/{len(values)}={number(mean,3)}$ {unit}. The squared deviations from $\\bar x$ sum to {number(variance*(len(values)-1),3)}, so $s^2={number(variance*(len(values)-1),3)}/({len(values)}-1)={number(variance,3)}$ squared {unit}, and $s={number(sd,3)}$ {unit}. The sample mean estimates the population mean $\\mu$; the sample variance estimates the population variance $\\sigma^2$. The plug-in standard error is $s/\\sqrt n={number(sd,3)}/\\sqrt{{{len(values)}}}={number(se,3)}$ {unit}. It estimates the standard deviation of sample means across repeated samples of the same size. It is not the spread of the individual observations."))
    ex.append("".join(ex_group)); sol.append("".join(sol_group))

    ex_group = [group_heading(3, "Known-Sigma Confidence Intervals Across Sample Sizes")]
    sol_group = [group_heading(3, "Known-Sigma Confidence Intervals Across Sample Sizes")]
    for i, (context, unit, mu, sigma, ns, means) in enumerate(KNOWN_SIGMA_SAMPLES, 1):
        pairs = "; ".join(f"$n={n}$, $\\bar x={m}$" for n, m in zip(ns, means))
        ex_group.append(task(3, 3, i, f"Four samples of {context}", f"A population standard deviation of $\\sigma={sigma}$ {unit} is treated as known. Four independent samples give {pairs}. (a) Calculate the standard error for each sample. (b) Construct each 95% z confidence interval using $\\bar x\\pm1.96\\sigma/\\sqrt n$. (c) Explain why the intervals have different widths and why the point estimates need not equal the reference population mean {mu}."))
        result_parts=[]
        for n, mean in zip(ns,means):
            se=sigma/math.sqrt(n); margin=1.96*se
            result_parts.append(f"for $n={n}$, $SE={sigma}/\\sqrt{{{n}}}={number(se,3)}$ and the interval is ${mean}\\pm1.96({number(se,3)})=[{number(mean-margin,3)}, {number(mean+margin,3)}]$")
        sol_group.append(task(3, 3, i, f"Four samples of {context}", "The four calculations are " + "; ".join(result_parts) + f". Holding $\\sigma={sigma}$ fixed, the standard error falls with $1/\\sqrt n$, so larger samples produce narrower intervals. Each $\\bar x$ is a sample statistic and can vary from sample to sample around the population mean. A 95% confidence procedure has 95% long-run coverage under its assumptions; it does not require every sample mean to equal {mu} {unit}."))
    ex.append("".join(ex_group)); sol.append("".join(sol_group))

    ex_group = [group_heading(4, "Confidence Level, Sample Size, and Interval Width")]
    sol_group = [group_heading(4, "Confidence Level, Sample Size, and Interval Width")]
    criticals=[(0.80,1.2816),(0.90,1.6449),(0.95,1.9600),(0.99,2.5758)]
    for i,(context,unit,mean,sigma,n,n_small,n_large) in enumerate(INTERVAL_WIDTH_CASES,1):
        ex_group.append(task(3,4,i,f"Interval width for {context}",f"A sample has $\\bar x={mean}$ {unit}, known $\\sigma={sigma}$ {unit}, and $n={n}$. (a) Construct 80%, 90%, 95%, and 99% z confidence intervals using critical values 1.2816, 1.6449, 1.9600, and 2.5758. (b) At the 95% level, compare the interval widths for $n={n_small}$, $n={n}$, and $n={n_large}$ while keeping the same mean and standard deviation. (c) Explain separately how confidence level, sample size, and population variability affect interval width."))
        intervals=[]
        for conf,z in criticals:
            margin=z*sigma/math.sqrt(n); intervals.append(f"{number(conf*100,0)}%: $[{number(mean-margin,3)}, {number(mean+margin,3)}]$ with margin {number(margin,3)}")
        widths=[]
        for size in (n_small,n,n_large): widths.append(f"$n={size}$ gives width $2(1.96)({sigma})/\\sqrt{{{size}}}={number(2*1.96*sigma/math.sqrt(size),3)}$")
        sol_group.append(task(3,4,i,f"Interval width for {context}",f"The standard error at $n={n}$ is ${sigma}/\\sqrt{{{n}}}={number(sigma/math.sqrt(n),3)}$ {unit}. The intervals are " + "; ".join(intervals) + ". At 95%, " + "; ".join(widths) + ". A higher confidence level uses a larger critical value and widens the interval. A larger sample lowers the standard error and narrows it. A larger population standard deviation increases the standard error and widens it. The center remains $\\bar x$ in every calculation."))
    ex.append("".join(ex_group)); sol.append("".join(sol_group))

    ex_group = [group_heading(5, "One-Sided z Tests and the Possible Decision Error")]
    sol_group = [group_heading(5, "One-Sided z Tests and the Possible Decision Error")]
    for i,(title,outcome,unit,mu,sigma,n,mean,direction) in enumerate(ONE_SIDED_Z,1):
        symbol = ">" if direction=="higher" else "<"
        ex_group.append(task(3,5,i,title,f"In this hypothetical teaching setting, the null model specifies $\\mu_0={mu}$ and the population standard deviation is treated as known at $\\sigma={sigma}$ {unit}. A random sample of $n={n}$ after the stated procedure has mean $\\bar x={mean}$ {unit}. Test $H_0:\\mu={mu}$ against $H_1:\\mu{symbol}{mu}$ at $\\alpha=0.05$. The null value is a claim to be tested, not a population truth supplied in advance. (a) Calculate the z statistic. (b) Use the one-sided critical value 1.6449 in the appropriate tail to decide. (c) Name the statistical error that remains possible after that decision and interpret it for {outcome}."))
        z=z_test(mean,mu,sigma,n); reject=(z>1.6449 if direction=="higher" else z< -1.6449)
        err=("A Type I error remains possible: the procedure could report the stated directional population difference even though the null value is correct." if reject else "A Type II error remains possible: the procedure could miss a genuine population difference in the stated direction.")
        sol_group.append(task(3,5,i,title,f"The standard error is $SE={sigma}/\\sqrt{{{n}}}={number(sigma/math.sqrt(n),4)}$ {unit}. Therefore $z=({mean}-{mu})/{number(sigma/math.sqrt(n),4)}={number(z,4)}$. The rejection boundary is {'$z>1.6449$' if direction=='higher' else '$z<-1.6449$'}. Because {number(z,4)} {'crosses' if reject else 'does not cross'} that boundary, we {'reject' if reject else 'fail to reject'} $H_0$ at the 5% level. The evidence is {'consistent with a ' + direction + ' population ' + outcome if reject else 'not strong enough to establish the stated ' + direction + ' population ' + outcome}. {err} A test decision manages long-run error rates; it does not prove which hypothesis is true."))
    ex.append("".join(ex_group)); sol.append("".join(sol_group))

    ex_group = [group_heading(6, "Two-Sided z Tests")]
    sol_group = [group_heading(6, "Two-Sided z Tests")]
    for i,(title,outcome,unit,mu,sigma,n,mean) in enumerate(FULL_INFERENCE_Z,1):
        ex_group.append(task(3,6,i,title,f"Suppose {outcome} has reference population mean $\\mu_0={mu}$ and known standard deviation $\\sigma={sigma}$ {unit}. A sample of $n={n}$ after the named change has $\\bar x={mean}$ {unit}. (a) State a two-sided null and alternative hypothesis. (b) Calculate the z statistic and two-sided p-value. (c) Decide at $\\alpha=0.05$ and interpret the result without claiming that nonsignificance proves no effect."))
        z=z_test(mean,mu,sigma,n); p=2*(1-normal_cdf(abs(z))); reject=p<.05
        sol_group.append(task(3,6,i,title,f"The hypotheses are $H_0:\\mu={mu}$ and $H_1:\\mu\\ne{mu}$. The standard error is ${sigma}/\\sqrt{{{n}}}={number(sigma/math.sqrt(n),4)}$ {unit}, so $z=({mean}-{mu})/{number(sigma/math.sqrt(n),4)}={number(z,4)}$. The two-sided p-value is $2[1-\\Phi(|{number(z,4)}|)]={number(p,4)}$. Because {number(p,4)} is {'below' if reject else 'not below'} 0.05, we {'reject' if reject else 'fail to reject'} $H_0$. The sample {'provides evidence that the population mean differs from the reference value' if reject else 'does not provide sufficiently strong evidence of a population-mean difference at this significance level'}. A failure to reject would reflect limited evidence, not proof of exact equality."))
    ex.append("".join(ex_group)); sol.append("".join(sol_group))

    ex_group = [group_heading(7, "p-Values, Power, and Planned Sample Size")]
    sol_group = [group_heading(7, "p-Values, Power, and Planned Sample Size")]
    z_alpha=normal_ppf(.95); z_power=normal_ppf(.90)
    for i,(context,unit,mu,sigma,n,mean,delta) in enumerate(POWER_CASES,1):
        ex_group.append(task(3,7,i,f"Planning a study of {context}",f"A one-sided upper-tail z test uses $H_0:\\mu={mu}$, known $\\sigma={sigma}$ {unit}, $\\alpha=0.05$, and sample size $n={n}$. The observed sample mean is $\\bar x={mean}$. (a) Calculate the z statistic and p-value and make the decision. (b) If the true population mean is $\\mu={mu+delta}$, calculate power using $1-\\Phi(z_{{0.95}}-\\delta\\sqrt n/\\sigma)$. (c) Find the smallest planned sample size for 90% power using $n=\\lceil[(z_{{0.95}}+z_{{0.90}})\\sigma/\\delta]^2\\rceil$. Interpret the p-value and power as different conditional probabilities."))
        z=z_test(mean,mu,sigma,n); p=1-normal_cdf(z); power=1-normal_cdf(z_alpha-delta*math.sqrt(n)/sigma); need=math.ceil(((z_alpha+z_power)*sigma/delta)**2)
        sol_group.append(task(3,7,i,f"Planning a study of {context}",f"The observed statistic is $z=({mean}-{mu})/({sigma}/\\sqrt{{{n}}})={number(z,4)}$. Its upper-tail p-value is $1-\\Phi({number(z,4)})={number(p,4)}$, so we {'reject' if p<.05 else 'fail to reject'} $H_0$ at $\\alpha=0.05$. This p-value describes results at least this large under the null model; it is not the probability that $H_0$ is true. If the true improvement is $\\delta={delta}$, power is $1-\\Phi({number(z_alpha,4)}-{delta}\\sqrt{{{n}}}/{sigma})={number(power,4)}$. Power is the long-run probability of rejection under that specified alternative. For 90% planned power, $n=\\lceil[({number(z_alpha,4)}+{number(z_power,4)}){sigma}/{delta}]^2\\rceil={need}$. Rounding up is necessary because a fraction of an observation cannot meet the target."))
    ex.append("".join(ex_group)); sol.append("".join(sol_group))

    ex_group = [group_heading(8, "Two-Sided Testing, Confidence Intervals, and Practical Size")]
    sol_group = [group_heading(8, "Two-Sided Testing, Confidence Intervals, and Practical Size")]
    for i,(title,outcome,unit,mu,sigma,n,mean) in enumerate(TWO_SIDED_Z,1):
        se=sigma/math.sqrt(n); margin=1.96*se; lower=mean-margin; upper=mean+margin; z=z_test(mean,mu,sigma,n); p=2*(1-normal_cdf(abs(z))); diff=mean-mu
        ex_group.append(task(3,8,i,f"Full inference for {title.lower()}",f"In an independent hypothetical setting, the reference mean is {mu}, known $\\sigma={sigma}$ {unit}, $n={n}$, and $\\bar x={mean}$. (a) Construct the 95% confidence interval for $\\mu$. (b) Use the interval to make the two-sided 5% test decision about $H_0:\\mu={mu}$ and verify it with a p-value. (c) Report the observed mean difference in {unit} and explain why statistical significance alone does not determine whether that difference is practically important."))
        sol_group.append(task(3,8,i,f"Full inference for {title.lower()}",f"The standard error is ${sigma}/\\sqrt{{{n}}}={number(se,4)}$ {unit}, and the margin is $1.96({number(se,4)})={number(margin,4)}$. The 95% interval is ${mean}\\pm{number(margin,4)}=[{number(lower,4)}, {number(upper,4)}]$. The null value {mu} {'is outside' if not lower<=mu<=upper else 'is inside'} this interval, so the matching two-sided test {'rejects' if p<.05 else 'fails to reject'} $H_0$. Directly, $z={number(z,4)}$ and $p={number(p,4)}$, which gives the same decision. The observed difference is ${mean}-{mu}={number(diff,3)}$ {unit}. Its practical importance depends on subject-matter consequences and the measurement scale, not on the p-value alone."))
    ex.append("".join(ex_group)); sol.append("".join(sol_group))

    ex_group = [group_heading(9, "t Quantiles and Degrees of Freedom")]
    sol_group = [group_heading(9, "t Quantiles and Degrees of Freedom")]
    for i,(df,q99) in enumerate(T_PERCENTILES,1):
        ex_group.append(task(3,9,i,f"Quantiles with {df} degrees of freedom",f"For a t distribution with {df} degrees of freedom, a reference table gives $t_{{0.99}}({df})={number(q99,4)}$. (a) State $t_{{0.01}}({df})$ using symmetry. (b) Explain what each quantile means as a cumulative area. (c) Compare the magnitude with the standard-normal 0.99 quantile 2.3263 and explain what happens as the degrees of freedom increase."))
        sol_group.append(task(3,9,i,f"Quantiles with {df} degrees of freedom",f"By symmetry, $t_{{0.01}}({df})=-t_{{0.99}}({df})=-{number(q99,4)}$. The upper quantile satisfies $P(T\\leq {number(q99,4)})=0.99$; the lower one satisfies $P(T\\leq-{number(q99,4)})=0.01$. Its magnitude {number(q99,4)} is larger than 2.3263 because a t distribution with finite degrees of freedom has heavier tails than the standard normal. As the degrees of freedom grow, the extra uncertainty from estimating $\\sigma$ diminishes and the t distribution approaches the standard normal distribution."))
    ex.append("".join(ex_group)); sol.append("".join(sol_group))

    ex_group = [group_heading(10, "One-Sample t Tests")]
    sol_group = [group_heading(10, "One-Sample t Tests")]
    for i,(context,outcome,unit,mu,n,mean,sd,crit) in enumerate(ONE_SAMPLE_T,1):
        lower = "time" in outcome or "count" in outcome
        symbol="<" if lower else ">"
        ex_group.append(task(3,10,i,f"Testing {context}",f"A sample of $n={n}$ observations after {context} has {outcome} mean $\\bar x={mean}$ {unit} and sample standard deviation $s={sd}$ {unit}. The population standard deviation is unknown. Test $H_0:\\mu={mu}$ against $H_1:\\mu{symbol}{mu}$ at $\\alpha=0.05$. (a) Explain why the one-sample t procedure is used. (b) Calculate the statistic with {n-1} degrees of freedom. (c) Compare it with the one-sided critical magnitude {number(crit,4)} and interpret the decision."))
        stat=(mean-mu)/(sd/math.sqrt(n)); reject=(stat < -crit if lower else stat > crit)
        sol_group.append(task(3,10,i,f"Testing {context}",f"The population standard deviation is unknown and is replaced by $s={sd}$, so the source's one-sample procedure uses $T=(\\bar X-\\mu_0)/(S/\\sqrt n)$ with $df=n-1={n-1}$. Here $SE={sd}/\\sqrt{{{n}}}={number(sd/math.sqrt(n),4)}$ {unit} and $t=({mean}-{mu})/{number(sd/math.sqrt(n),4)}={number(stat,4)}$. The rejection rule is {'$t<-'+number(crit,4)+'$' if lower else '$t>'+number(crit,4)+'$'}. The statistic {'crosses' if reject else 'does not cross'} that boundary, so we {'reject' if reject else 'fail to reject'} $H_0$. The sample {'supports' if reject else 'does not provide sufficiently strong evidence for'} the stated directional change in {outcome}, subject to independent observations and an approximately normal population model for this small-sample procedure."))
    ex.append("".join(ex_group)); sol.append("".join(sol_group))

    ex_group = [group_heading(11, "One-Sample t Confidence Intervals and Test Duality")]
    sol_group = [group_heading(11, "One-Sample t Confidence Intervals and Test Duality")]
    for i,(context,unit,n,mean,sd,crit,null) in enumerate(T_INTERVALS,1):
        ex_group.append(task(3,11,i,f"Estimating mean {context}",f"A random sample of $n={n}$ has $\\bar x={mean}$ {unit} and $s={sd}$ {unit}. A t table gives $t_{{0.975}}({n-1})={number(crit,4)}$. (a) Construct a 95% confidence interval for the population mean. (b) Use the interval to test $H_0:\\mu={null}$ against $H_1:\\mu\\ne{null}$ at 5%. (c) Explain why the interval and matching two-sided test agree and state the correct repeated-sampling interpretation of 95% confidence."))
        se=sd/math.sqrt(n); margin=crit*se; lo=mean-margin;hi=mean+margin; reject=not(lo<=null<=hi)
        sol_group.append(task(3,11,i,f"Estimating mean {context}",f"The estimated standard error is $s/\\sqrt n={sd}/\\sqrt{{{n}}}={number(se,4)}$ {unit}. The margin is ${number(crit,4)}({number(se,4)})={number(margin,4)}$, so the interval is ${mean}\\pm{number(margin,4)}=[{number(lo,4)}, {number(hi,4)}]$. The null value {null} {'falls outside' if reject else 'falls inside'} the interval, so the matching two-sided 5% test {'rejects' if reject else 'fails to reject'} $H_0$. Both procedures use the same standard error and symmetric 2.5% tail boundaries, which makes their decisions agree. In repeated sampling, 95% of intervals produced by this method cover the fixed population mean under the model assumptions; the completed interval does not assign a 95% probability to that fixed parameter."))
    ex.append("".join(ex_group)); sol.append("".join(sol_group))

    ex_group = [group_heading(12, "Pooled Independent-Samples t Tests")]
    sol_group = [group_heading(12, "Pooled Independent-Samples t Tests")]
    for i,(context,outcome,n1,n2,m1,m2,var1,var2,crit) in enumerate(POOLED_T,1):
        ex_group.append(task(3,12,i,f"Comparing {context}",f"Two independent groups are compared on {outcome}. Group 1 has $n_1={n1}$, $\\bar x_1={m1}$, and $s_1^2={var1}$; Group 2 has $n_2={n2}$, $\\bar x_2={m2}$, and $s_2^2={var2}$. Use the registered equal-population-variance model. (a) Explain why the samples are independent rather than paired. (b) Calculate the pooled variance, standard error, and t statistic for the directional alternative $\\mu_1>\\mu_2$. (c) Compare with the one-sided critical value {number(crit,4)} at $\\alpha=0.05$ and interpret the result. (d) State the key design and model conditions."))
        df=n1+n2-2; sp2=((n1-1)*var1+(n2-1)*var2)/df; se=math.sqrt(sp2*(1/n1+1/n2)); stat=(m1-m2)/se; reject=stat>crit
        sol_group.append(task(3,12,i,f"Comparing {context}",f"Different observational units belong to the two groups, so no case-level pairing is available. Under the equal-population-variance model, $s_p^2=[({n1}-1){var1}+({n2}-1){var2}]/({n1}+{n2}-2)={number(sp2,4)}$. The standard error is $\\sqrt{{{number(sp2,4)}(1/{n1}+1/{n2})}}={number(se,4)}$. With $df={df}$, $t=({m1}-{m2})/{number(se,4)}={number(stat,4)}$. Because {number(stat,4)} {'exceeds' if reject else 'does not exceed'} {number(crit,4)}, we {'reject' if reject else 'fail to reject'} the equal-mean null in favor of $\\mu_1>\\mu_2$. The result {'supports' if reject else 'does not provide sufficiently strong evidence for'} a higher population mean in Group 1. The procedure requires independent observations, independently sampled groups, an approximately normal outcome within each population for these sample sizes, and equal population variances. Random assignment is additionally needed for a causal interpretation."))
    ex.append("".join(ex_group)); sol.append("".join(sol_group))

    return ex, sol


GROUP_TITLES = {
    "de": (
        "Hypothesen und die zwei möglichen Fehler",
        "Stichprobenschätzungen und Standardfehler",
        "Konfidenzintervalle bei bekannter Standardabweichung und verschiedenen Stichprobenumfängen",
        "Konfidenzniveau, Stichprobenumfang und Intervallbreite",
        "Einseitige z-Tests und der mögliche Entscheidungsfehler",
        "Zweiseitige z-Tests",
        "p-Werte, Teststärke und geplanter Stichprobenumfang",
        "Zweiseitige Tests, Konfidenzintervalle und praktische Grösse",
        "t-Quantile und Freiheitsgrade",
        "t-Tests für eine Stichprobe",
        "t-Konfidenzintervalle für eine Stichprobe und Test-Intervall-Dualität",
        "t-Tests für zwei unabhängige Stichproben mit gepoolter Varianz",
    ),
    "sq": (
        "Hipotezat dhe dy gabimet e mundshme",
        "Vlerësimet nga kampioni dhe gabimi standard",
        "Intervalet e besimit me devijim standard të njohur dhe madhësi të ndryshme kampioni",
        "Niveli i besimit, madhësia e kampionit dhe gjerësia e intervalit",
        "Testet z njëanëshe dhe gabimi i mundshëm i vendimit",
        "Testet z dyanëshe",
        "Vlerat p, fuqia statistikore dhe madhësia e planifikuar e kampionit",
        "Testimi dyanësh, intervalet e besimit dhe madhësia praktike",
        "Kuantilet t dhe shkallët e lirisë",
        "Testet t për një kampion",
        "Intervalet t të besimit për një kampion dhe lidhja me testin",
        "Testet t për dy kampione të pavarura me variancë të përbashkët",
    ),
}


HYPOTHESIS_LOCALIZED = {
    "de": (
        ("Angeleitetes Üben mit Karten", "mittlerer Routenplanungswert", "Lernende mit angeleitetem Kartenüben", "Lernende mit der Standardaktivität"),
        ("Ruhige Leseräume", "mittlerer Leseverständniswert", "Studierende im zugewiesenen ruhigen Leseraum", "Studierende im zugewiesenen üblichen Raum"),
        ("Checkliste für die Archivsuche", "mittlere Anzahl korrekt abgerufener Datensätze", "Lernende mit einer Suchcheckliste", "Lernende mit den üblichen Anweisungen"),
        ("Kurze Bewegungspause", "mittlerer Wert der anhaltenden Aufmerksamkeit", "Teilnehmende mit einer kurzen Bewegungspause", "Teilnehmende mit dem üblichen Zeitplan"),
        ("Tutorial mit Untertiteln", "mittlerer Tutorialverständniswert", "Lernende mit einem Tutorial mit Untertiteln", "Lernende mit demselben Tutorial ohne Untertitel"),
        ("Reduzierte Benachrichtigungen", "mittlere Aufgabenbearbeitungszeit", "Teilnehmende mit reduzierten Benachrichtigungen", "Teilnehmende mit den Standardeinstellungen"),
        ("Karten zum Abrufüben", "mittlerer Wert der verzögerten Erinnerung", "Lernende mit Karten zum Abrufüben", "Lernende mit erneutem Lesen desselben Materials"),
        ("Orientierungskarte für das Museum", "mittlere Anzahl von Navigationsfehlern", "Besuchende mit einer Orientierungskarte", "Besuchende mit dem Standardfaltblatt"),
        ("Impuls für gegenseitiges Erklären", "mittlerer Wert der Konzepterklärung", "Studierende mit einem Impuls für gegenseitiges Erklären", "Studierende mit einem Impuls zur individuellen Wiederholung"),
        ("Strukturierte Notizvorlage", "mittlere Anzahl korrekt erkannter Argumente", "Lernende mit einer strukturierten Notizvorlage", "Lernende mit ihrer üblichen Art, Notizen zu machen"),
    ),
    "sq": (
        ("Ushtrim i udhëzuar me hartë", "rezultati mesatar i planifikimit të rrugës", "nxënësit me ushtrim të udhëzuar me hartë", "nxënësit me aktivitetin standard"),
        ("Hapësira të qeta leximi", "rezultati mesatar i të kuptuarit gjatë leximit", "studentët e caktuar në një dhomë të qetë leximi", "studentët e caktuar në dhomën e zakonshme"),
        ("Listë kontrolli për kërkim në arkiv", "numri mesatar i regjistrimeve të gjetura saktë", "nxënësit me listë kontrolli për kërkim", "nxënësit me udhëzimet e zakonshme"),
        ("Pushim i shkurtër me lëvizje", "rezultati mesatar i vëmendjes së qëndrueshme", "pjesëmarrësit me një pushim të shkurtër me lëvizje", "pjesëmarrësit me orarin e zakonshëm"),
        ("Tutorial me titra", "rezultati mesatar i të kuptuarit të tutorialit", "nxënësit që shohin tutorial me titra", "nxënësit që shohin të njëjtin tutorial pa titra"),
        ("Cilësim me më pak njoftime", "koha mesatare e përfundimit të detyrës", "pjesëmarrësit me më pak njoftime", "pjesëmarrësit me cilësimin standard"),
        ("Karta për ushtrimin e rikujtimit", "rezultati mesatar i rikujtimit të vonuar", "nxënësit me karta për ushtrimin e rikujtimit", "nxënësit që rilexojnë të njëjtin material"),
        ("Hartë orientimi për muzeun", "numri mesatar i gabimeve të navigimit", "vizitorët me hartë orientimi", "vizitorët me fletëpalosjen standarde"),
        ("Nxitje për shpjegim mes bashkëmoshatarësh", "rezultati mesatar i shpjegimit të konceptit", "studentët me nxitje për shpjegim mes bashkëmoshatarësh", "studentët me nxitje për përsëritje individuale"),
        ("Model i strukturuar shënimesh", "numri mesatar i argumenteve të dalluara saktë", "nxënësit me model të strukturuar shënimesh", "nxënësit që mbajnë shënime në mënyrën e zakonshme"),
    ),
}


CASE_LABELS = {
    "de": {
        2: ("Tägliche Leseminuten", "Abgeschlossene Archivanfragen", "Konzentrationsbewertungen", "Dauer von Museumsbesuchen", "Korrekt codierte Datensätze", "Wöchentliche Übungsstunden", "Routenplanungswerte", "Reaktionszeiten", "Abgeschlossene Tagebuchimpulse", "Kataloggenauigkeitswerte"),
        3: ("Leseleistung", "Bearbeitungszeit", "Konzentrationsbewertung", "Besuchsdauer", "Erinnerungsleistung", "Geräuschindex", "Selbstvertrauenswert", "Reaktionszeit", "Vertrauensbewertung", "Genauigkeitswert"),
        4: ("Leseflüssigkeit", "Archivbearbeitung", "Wohlbefindensindex", "Museumsdauer", "Erinnerungswert", "Geräuschpegel", "Selbstvertrauen im Kurs", "Reaktionsverzögerung", "Gemeinschaftsvertrauen", "Kataloggenauigkeit"),
        5: ("Angeleitetes Routenüben", "Vereinfachtes Archivformular", "Impulse zum Abrufüben", "Orientierungskarte", "Strukturierte Notizvorlage", "Ruhige Arbeitsphase", "Demonstration mit Untertiteln", "Erinnerungscheckliste", "Gegenseitiges Erklären", "Reduzierte Benachrichtigungen"),
        6: ("Unterstützungsplan für das Gedächtnis", "Überarbeitetes Suchprotokoll", "Neuer Leseimpuls", "Routenschilder in einer Galerie", "Format einer Konzeptkarte", "Terminerinnerung", "Struktur für Peer-Review", "Werkzeug zur Dokumentvorschau", "Karte zum Routenüben", "Anzeige für Annotationen"),
        7: ("Angeleitetes Üben mit Karten", "Checkliste für die Archivsuche", "Karten zum Abrufüben", "Ruhiger Leseraum", "Strukturierte Notizvorlage", "Tutorial mit Untertiteln", "Erinnerungscheckliste", "Gegenseitiges Erklären", "Orientierungskarte für das Museum", "Reduzierte Benachrichtigungen"),
        8: ("Alternative Leseanordnung", "Neue Katalogoberfläche", "Umgebungsgeräusche", "Markierungen einer Museumsroute", "Format von Gedächtnishinweisen", "Formulierung einer Umfrageerinnerung", "Sitzordnung im Workshop", "Kontrast von Archivbildern", "Stil der Routenbeschreibung", "Anzeige für Notizen"),
        10: ("Angeleitetes Suchtraining", "Kürzeres Aufnahmeformular", "Abrufhinweis", "Orientierungskarte", "Strukturierte Notizseite", "Ruhiger Arbeitsblock", "Demonstration mit Untertiteln", "Erinnerungscheckliste", "Gegenseitiges Erklären", "Reduzierte Benachrichtigungen"),
        11: ("Leseflüssigkeit", "Archivbearbeitung", "Konzentrationsbewertung", "Museumsdauer", "Erinnerungswert", "Geräuschindex", "Selbstvertrauenswert", "Reaktionsverzögerung", "Vertrauensbewertung", "Kataloggenauigkeit"),
        12: ("Angeleitetes und selbstständiges Kartenüben", "Tutorials mit und ohne Untertitel", "Ruhige und übliche Leseräume", "Checkliste und übliche Archivsuche", "Strukturierte und freie Notizen", "Orientierungskarte und Standardfaltblatt", "Gegenseitiges Erklären und privates Wiederlesen", "Reduzierte und übliche Benachrichtigungen", "Abrufkarten und erneutes Lesen der Zusammenfassung", "Visuelle und reine Text-Routenführung"),
    },
    "sq": {
        2: ("Minutat ditore të leximit", "Kërkesat e përfunduara në arkiv", "Vlerësimet e përqendrimit", "Kohëzgjatja e vizitave në muze", "Regjistrimet e koduara saktë", "Orët javore të ushtrimit", "Rezultatet e planifikimit të rrugës", "Vonesat e përgjigjes", "Nxitjet e përfunduara të ditarit", "Rezultatet e saktësisë së katalogut"),
        3: ("Rezultati i leximit", "Koha e përpunimit", "Vlerësimi i përqendrimit", "Kohëzgjatja e vizitës", "Rezultati i kujtesës", "Indeksi i zhurmës", "Rezultati i vetëbesimit", "Koha e përgjigjes", "Vlerësimi i besimit", "Rezultati i saktësisë"),
        4: ("Rrjedhshmëria e leximit", "Përpunimi në arkiv", "Indeksi i mirëqenies", "Kohëzgjatja në muze", "Rezultati i kujtesës", "Niveli i zërit", "Vetëbesimi në kurs", "Vonesa e përgjigjes", "Besimi në komunitet", "Saktësia e katalogut"),
        5: ("Përsëritje e udhëzuar e rrugës", "Formular i thjeshtuar i arkivit", "Nxitje për ushtrimin e rikujtimit", "Hartë orientimi", "Model i strukturuar shënimesh", "Periudhë e qetë pune", "Demonstrim me titra", "Listë kontrolli për kujtesat", "Shpjegim mes bashkëmoshatarësh", "Më pak njoftime"),
        6: ("Plan mbështetës për kujtesën", "Protokoll kërkimi i rishikuar", "Nxitje e re leximi", "Shenja të rrugës në galeri", "Format harte konceptuale", "Kujtesë për takim", "Strukturë e shqyrtimit nga bashkëmoshatarët", "Mjet për parashikim dokumenti", "Kartë për ushtrimin e rrugës", "Paraqitje e shënimeve"),
        7: ("Ushtrim i udhëzuar me hartë", "Listë kontrolli për kërkim në arkiv", "Karta për ushtrimin e rikujtimit", "Dhomë e qetë leximi", "Model i strukturuar shënimesh", "Tutorial me titra", "Listë kontrolli për kujtesat", "Shpjegim mes bashkëmoshatarësh", "Hartë orientimi për muzeun", "Cilësim me më pak njoftime"),
        8: ("Paraqitje alternative e tekstit", "Ndërfaqe e re katalogu", "Mjedis me zhurmë", "Shenja të rrugës në muze", "Format i shenjave të kujtesës", "Formulim i kujtesës së anketës", "Plan i ulëseve në seminar", "Kontrast i imazhit të arkivit", "Stil i përshkrimit të rrugës", "Paraqitje për mbajtjen e shënimeve"),
        10: ("Trajnim i udhëzuar për kërkim", "Formular më i shkurtër pranimi", "Shenjë rikujtimi", "Kartë orientimi", "Faqe e strukturuar shënimesh", "Bllok i qetë pune", "Demonstrim me titra", "Listë kontrolli për kujtesat", "Shpjegim mes bashkëmoshatarësh", "Cilësim me më pak njoftime"),
        11: ("Rrjedhshmëria e leximit", "Përpunimi në arkiv", "Vlerësimi i përqendrimit", "Kohëzgjatja në muze", "Rezultati i kujtesës", "Indeksi i zhurmës", "Rezultati i vetëbesimit", "Vonesa e përgjigjes", "Vlerësimi i besimit", "Saktësia e katalogut"),
        12: ("Ushtrim i udhëzuar dhe i pavarur me hartë", "Tutoriale me dhe pa titra", "Dhoma të qeta dhe të zakonshme leximi", "Listë kontrolli dhe kërkim i zakonshëm në arkiv", "Shënime të strukturuara dhe të lira", "Hartë orientimi dhe fletëpalosje standarde", "Shpjegim mes bashkëmoshatarësh dhe rilexim individual", "Më pak njoftime dhe njoftime të zakonshme", "Karta rikujtimi dhe rilexim i përmbledhjes", "Udhëzim pamor dhe vetëm me tekst për rrugën"),
    },
}


UNITS = {
    "de": {
        "minutes": "Minuten", "requests": "Anfragen", "points": "Punkte",
        "records": "Datensätze", "hours": "Stunden", "seconds": "Sekunden",
        "prompts": "Impulse", "milliseconds": "Millisekunden", "errors": "Fehler",
        "switches": "Wechsel", "steps": "Schritte", "words per minute": "Wörter pro Minute",
        "decibels": "Dezibel", "score points": "Punkte", "correct records": "korrekte Datensätze",
        "arguments": "Argumente", "completed steps": "abgeschlossene Schritte",
        "route points": "Routenpunkte", "focus points": "Konzentrationspunkte",
    },
    "sq": {
        "minutes": "minuta", "requests": "kërkesa", "points": "pikë",
        "records": "regjistrime", "hours": "orë", "seconds": "sekonda",
        "prompts": "nxitje", "milliseconds": "milisekonda", "errors": "gabime",
        "switches": "kalime", "steps": "hapa", "words per minute": "fjalë në minutë",
        "decibels": "decibel", "score points": "pikë", "correct records": "regjistrime të sakta",
        "arguments": "argumente", "completed steps": "hapa të përfunduar",
        "route points": "pikë orientimi", "focus points": "pikë përqendrimi",
    },
}


def render_localized(locale: str) -> tuple[list[str], list[str]]:
    """Render the reviewed de-CH or Albanian adaptation from canonical values."""

    if locale == "en":
        return render_english()
    if locale not in ("de", "sq"):
        raise ValueError(f"unsupported locale: {locale}")

    labels=CASE_LABELS[locale]; units=UNITS[locale]; titles=GROUP_TITLES[locale]
    ex: list[str]=[]; sol: list[str]=[]

    exg=[group_heading(1,titles[0])];sog=[group_heading(1,titles[0])]
    for i,(_title,_outcome,_treatment,_comparison,direction) in enumerate(HYPOTHESIS_SCENARIOS,1):
        label,outcome,treatment,comparison=HYPOTHESIS_LOCALIZED[locale][i-1]
        if direction=="higher": symbols="$H_0:\\mu_T\\leq\\mu_C$ und $H_1:\\mu_T>\\mu_C$" if locale=="de" else "$H_0:\\mu_T\\leq\\mu_C$ dhe $H_1:\\mu_T>\\mu_C$"; relation="höher" if locale=="de" else "më e lartë"
        elif direction=="lower": symbols="$H_0:\\mu_T\\geq\\mu_C$ und $H_1:\\mu_T<\\mu_C$" if locale=="de" else "$H_0:\\mu_T\\geq\\mu_C$ dhe $H_1:\\mu_T<\\mu_C$"; relation="tiefer" if locale=="de" else "më e ulët"
        else: symbols="$H_0:\\mu_T=\\mu_C$ und $H_1:\\mu_T\\ne\\mu_C$" if locale=="de" else "$H_0:\\mu_T=\\mu_C$ dhe $H_1:\\mu_T\\ne\\mu_C$"; relation="unterschiedlich" if locale=="de" else "e ndryshme"
        if locale=="de":
            prompt=rf"Eine fiktive Studie untersucht «{label}». Gruppe T umfasst {treatment}; Gruppe C umfasst {comparison}. Das quantitative Ergebnis ist «{outcome}». $\mu_T$ und $\mu_C$ bezeichnen die entsprechenden Populationsmittelwerte. Die Forschungsfrage erwartet, dass der Mittelwert der Interventionspopulation {relation} ist. (a) Formuliere Null- und Alternativhypothese in Worten und Symbolen. (b) Erkläre einen Fehler vom Typ I und einen Fehler vom Typ II in diesem Kontext. (c) Begründe, weshalb eine Testentscheidung nicht mit Sicherheit zeigt, ob einer dieser Fehler aufgetreten ist."
            solution=rf"Eine Hypothese betrifft Mittelwerte der Grundgesamtheit und nicht die zwei beobachteten Stichprobenmittelwerte. Eine passende Formulierung ist {symbols}. Ein Fehler vom Typ I würde bedeuten, beim Ergebnis «{outcome}» einen {relation}en Mittelwert in der Interventionspopulation festzustellen, obwohl die Nullhypothese gilt. Ein Fehler vom Typ II würde bedeuten, diesen tatsächlich vorhandenen Unterschied nicht zu erkennen. Die Stichprobe liefert unsichere Evidenz und keinen direkten Zugang zu beiden Populationsmittelwerten. Deshalb kennen wir unter festgelegten Bedingungen die langfristigen Fehlerraten des Verfahrens, aber eine einzelne Entscheidung trägt kein Etikett, das sie als richtig oder falsch ausweist."
        else:
            prompt=rf"Një studim i trilluar shqyrton «{label}». Ai krahason {treatment} me {comparison}. Rezultati sasior është «{outcome}». $\mu_T$ dhe $\mu_C$ shënojnë mesataret përkatëse të popullatave. Pyetja kërkimore pret që mesatarja e popullatës në kushtin e ndërhyrjes të jetë {relation}. (a) Shkruaj hipotezën zero dhe atë alternative me fjalë dhe simbole. (b) Shpjego një gabim të llojit I dhe një gabim të llojit II në këtë situatë. (c) Trego pse një vendim testi nuk zbulon me siguri nëse ka ndodhur ndonjëri gabim."
            solution=rf"Hipoteza lidhet me mesataret e popullatave, jo me dy mesataret e vrojtuara të kampioneve. Një formulim i përshtatshëm është {symbols}. Gabimi i llojit I do të thoshte të arrihej në përfundimin se mesatarja e rezultatit «{outcome}» në popullatën me ndërhyrje është {relation}, edhe pse hipoteza zero është e vërtetë. Gabimi i llojit II do të thoshte të mos zbulohej ky dallim kur ai ekziston vërtet. Kampioni jep evidencë të pasigurt, jo qasje të drejtpërdrejtë te të dyja mesataret e popullatave. Prandaj njihen normat afatgjata të gabimeve të procedurës në kushte të caktuara, por vendimi i një studimi nuk tregon vetë nëse ishte i saktë."
        exg.append(task(3,1,i,label,prompt));sog.append(task(3,1,i,label,solution))
    ex.append("".join(exg));sol.append("".join(sog))

    exg=[group_heading(2,titles[1])];sog=[group_heading(2,titles[1])]
    for i,(_title,unit,values) in enumerate(RAW_DATA,1):
        label=labels[2][i-1];u=units[unit];rendered=", ".join(str(v) for v in values)
        mean=sample_mean(values);variance=sample_variance(values);sd=math.sqrt(variance);se=sd/math.sqrt(len(values))
        if locale=="de":
            prompt=rf"Eine einfache Zufallsstichprobe zum Merkmal «{label}» enthält die folgenden {len(values)} Werte: {rendered}. Als Einheit wird «{u}» verwendet. (a) Berechne Stichprobenmittelwert $\bar x$ und Stichprobenvarianz $s^2$. (b) Nenne die Parameter der Grundgesamtheit, die diese zwei Kennwerte schätzen. (c) Berechne den eingesetzten Standardfehler $s/\sqrt n$ und erkläre, was er über wiederholte Stichproben beschreibt."
            solution=rf"Es gibt $n={len(values)}$ Beobachtungen mit der Summe {number(sum(values),2)}. Somit ist $\bar x={number(sum(values),2)}/{len(values)}={number(mean,3)}$ {u}. Die quadrierten Abweichungen von $\bar x$ summieren sich zu {number(variance*(len(values)-1),3)}. Deshalb gilt $s^2={number(variance*(len(values)-1),3)}/({len(values)}-1)={number(variance,3)}$ {u} zum Quadrat und $s={number(sd,3)}$ {u}. Der Stichprobenmittelwert schätzt den Populationsmittelwert $\mu$; die Stichprobenvarianz schätzt die Populationsvarianz $\sigma^2$. Der eingesetzte Standardfehler ist $s/\sqrt n={number(sd,3)}/\sqrt{{{len(values)}}}={number(se,3)}$ {u}. Er schätzt die Standardabweichung von Stichprobenmittelwerten über wiederholte Stichproben gleichen Umfangs und nicht die Streuung einzelner Beobachtungen."
        else:
            prompt=rf"Një kampion i thjeshtë i rastësishëm për ndryshoren «{label}» përmban këto {len(values)} vlera: {rendered}. Njësia matëse është «{u}». (a) Llogarit mesataren e kampionit $\bar x$ dhe variancën e kampionit $s^2$. (b) Emërto parametrat e popullatës që vlerësohen nga këta dy tregues. (c) Llogarit gabimin standard të vlerësuar $s/\sqrt n$ dhe shpjego çfarë përshkruan ai në kampione të përsëritura."
            solution=rf"Ka $n={len(values)}$ vrojtime dhe shuma e tyre është {number(sum(values),2)}. Prandaj $\bar x={number(sum(values),2)}/{len(values)}={number(mean,3)}$ {u}. Shuma e devijimeve të ngritura në katror nga $\bar x$ është {number(variance*(len(values)-1),3)}, kështu që $s^2={number(variance*(len(values)-1),3)}/({len(values)}-1)={number(variance,3)}$ {u} në katror dhe $s={number(sd,3)}$ {u}. Mesatarja e kampionit vlerëson mesataren e popullatës $\mu$; varianca e kampionit vlerëson variancën e popullatës $\sigma^2$. Gabimi standard i vlerësuar është $s/\sqrt n={number(sd,3)}/\sqrt{{{len(values)}}}={number(se,3)}$ {u}. Ai vlerëson devijimin standard të mesatareve të kampioneve në kampione të përsëritura me të njëjtën madhësi, jo shpërndarjen e vrojtimeve individuale."
        exg.append(task(3,2,i,label,prompt));sog.append(task(3,2,i,label,solution))
    ex.append("".join(exg));sol.append("".join(sog))

    exg=[group_heading(3,titles[2])];sog=[group_heading(3,titles[2])]
    for i,(_context,unit,mu,sigma,ns,means) in enumerate(KNOWN_SIGMA_SAMPLES,1):
        label=labels[3][i-1];u=units[unit];pairs="; ".join(f"$n={n}$, $\\bar x={m}$" for n,m in zip(ns,means));parts=[]
        for n,mean in zip(ns,means):
            se=sigma/math.sqrt(n);margin=1.96*se
            parts.append((f"für $n={n}$ gilt $SE={sigma}/\\sqrt{{{n}}}={number(se,3)}$ und das Intervall ist ${mean}\\pm1.96({number(se,3)})=[{number(mean-margin,3)}, {number(mean+margin,3)}]$" if locale=="de" else f"për $n={n}$, $SE={sigma}/\\sqrt{{{n}}}={number(se,3)}$ dhe intervali është ${mean}\\pm1.96({number(se,3)})=[{number(mean-margin,3)}, {number(mean+margin,3)}]$"))
        if locale=="de":
            prompt=rf"Für das Merkmal «{label}» wird die Populationsstandardabweichung $\sigma={sigma}$ {u} als bekannt behandelt. Vier unabhängige Stichproben ergeben {pairs}. (a) Berechne den Standardfehler jeder Stichprobe. (b) Konstruiere jedes 95%-z-Konfidenzintervall mit $\bar x\pm1.96\sigma/\sqrt n$. (c) Erkläre die unterschiedlichen Breiten und weshalb die Punktschätzungen nicht dem Referenzmittelwert der Grundgesamtheit {mu} entsprechen müssen."
            solution="Für die vier Stichproben ergeben sich folgende Berechnungen: " + "; ".join(parts) + rf". Bei festem $\sigma={sigma}$ sinkt der Standardfehler mit $1/\sqrt n$, weshalb grössere Stichproben schmalere Intervalle ergeben. Jedes $\bar x$ ist ein Stichprobenkennwert und kann von Stichprobe zu Stichprobe um den Populationsmittelwert schwanken. Ein 95%-Konfidenzverfahren erreicht unter seinen Annahmen langfristig 95% Überdeckung; es verlangt nicht, dass jeder Stichprobenmittelwert {mu} {u} entspricht."
        else:
            prompt=rf"Për ndryshoren «{label}», devijimi standard i popullatës $\sigma={sigma}$ {u} trajtohet si i njohur. Katër kampione të pavarura japin {pairs}. (a) Llogarit gabimin standard për secilin kampion. (b) Ndërto secilin interval z të besimit 95% me $\bar x\pm1.96\sigma/\sqrt n$. (c) Shpjego pse intervalet kanë gjerësi të ndryshme dhe pse vlerësimet pikësore nuk duhet të barazohen me mesataren referuese të popullatës {mu}."
            solution="Katër llogaritjet janë " + "; ".join(parts) + rf". Kur $\sigma={sigma}$ mbahet e pandryshuar, gabimi standard zvogëlohet me $1/\sqrt n$, prandaj kampionet më të mëdha japin intervale më të ngushta. Çdo $\bar x$ është tregues kampioni dhe mund të ndryshojë nga një kampion te tjetri rreth mesatares së popullatës. Nën supozimet përkatëse, një procedurë besimi 95% ka mbulim afatgjatë 95%; nuk kërkon që çdo mesatare kampioni të jetë {mu} {u}."
        exg.append(task(3,3,i,label,prompt));sog.append(task(3,3,i,label,solution))
    ex.append("".join(exg));sol.append("".join(sog))

    exg=[group_heading(4,titles[3])];sog=[group_heading(4,titles[3])];criticals=[(0.80,1.2816),(0.90,1.6449),(0.95,1.9600),(0.99,2.5758)]
    for i,(_context,unit,mean,sigma,n,n_small,n_large) in enumerate(INTERVAL_WIDTH_CASES,1):
        label=labels[4][i-1];u=units[unit];intervals=[]
        for conf,z in criticals:
            margin=z*sigma/math.sqrt(n); intervals.append(f"{number(conf*100,0)}%: $[{number(mean-margin,3)}, {number(mean+margin,3)}]$ " + ((f"mit Fehlerspanne {number(margin,3)}") if locale=="de" else f"me kufi gabimi {number(margin,3)}"))
        widths=[]
        for size in (n_small,n,n_large): widths.append(f"$n={size}$ " + ((f"ergibt die Breite $2(1.96)({sigma})/\\sqrt{{{size}}}={number(2*1.96*sigma/math.sqrt(size),3)}$") if locale=="de" else f"jep gjerësinë $2(1.96)({sigma})/\\sqrt{{{size}}}={number(2*1.96*sigma/math.sqrt(size),3)}$"))
        if locale=="de":
            prompt=rf"Eine Stichprobe zum Merkmal «{label}» hat $\bar x={mean}$ {u}, die bekannte Populationsstandardabweichung $\sigma={sigma}$ {u} und $n={n}$. (a) Konstruiere 80%-, 90%-, 95%- und 99%-z-Konfidenzintervalle mit den kritischen Werten 1.2816, 1.6449, 1.9600 und 2.5758. (b) Vergleiche auf dem 95%-Niveau die Intervallbreiten für $n={n_small}$, $n={n}$ und $n={n_large}$ bei gleichem Mittelwert und gleicher Standardabweichung. (c) Erkläre getrennt, wie Konfidenzniveau, Stichprobenumfang und Populationsstreuung die Breite beeinflussen."
            solution=rf"Der Standardfehler bei $n={n}$ ist ${sigma}/\sqrt{{{n}}}={number(sigma/math.sqrt(n),3)}$ {u}. Die Intervalle sind " + "; ".join(intervals) + ". Bei 95% gilt: " + "; ".join(widths) + r". Ein höheres Konfidenzniveau verwendet einen grösseren kritischen Wert und verbreitert das Intervall. Eine grössere Stichprobe senkt den Standardfehler und verengt das Intervall. Eine grössere Populationsstandardabweichung erhöht den Standardfehler und verbreitert das Intervall. Die Mitte bleibt bei jeder Berechnung $\bar x$."
        else:
            prompt=rf"Një kampion për ndryshoren «{label}» ka $\bar x={mean}$ {u}; devijimi standard i njohur i popullatës është $\sigma={sigma}$ {u} dhe $n={n}$. (a) Ndërto intervalet z të besimit 80%, 90%, 95% dhe 99% duke përdorur vlerat kritike 1.2816, 1.6449, 1.9600 dhe 2.5758. (b) Në nivelin 95%, krahaso gjerësitë e intervaleve për $n={n_small}$, $n={n}$ dhe $n={n_large}$ duke mbajtur të njëjtën mesatare dhe të njëjtin devijim standard. (c) Shpjego veçmas si ndikojnë niveli i besimit, madhësia e kampionit dhe ndryshueshmëria e popullatës në gjerësinë e intervalit."
            solution=rf"Gabimi standard për $n={n}$ është ${sigma}/\sqrt{{{n}}}={number(sigma/math.sqrt(n),3)}$ {u}. Intervalet janë " + "; ".join(intervals) + ". Në nivelin 95%, " + "; ".join(widths) + r". Një nivel më i lartë besimi përdor vlerë kritike më të madhe dhe e zgjeron intervalin. Një kampion më i madh e ul gabimin standard dhe e ngushton intervalin. Një devijim standard më i madh i popullatës e rrit gabimin standard dhe e zgjeron intervalin. Qendra mbetet $\bar x$ në çdo llogaritje."
        exg.append(task(3,4,i,label,prompt));sog.append(task(3,4,i,label,solution))
    ex.append("".join(exg));sol.append("".join(sog))

    # The remaining groups retain every canonical calculation while adapting the prose.
    exg=[group_heading(5,titles[4])];sog=[group_heading(5,titles[4])]
    for i,(_title,_outcome,unit,mu,sigma,n,mean,direction) in enumerate(ONE_SIDED_Z,1):
        label=labels[5][i-1];u=units[unit];symbol=">" if direction=="higher" else "<";z=z_test(mean,mu,sigma,n);reject=(z>1.6449 if direction=="higher" else z< -1.6449)
        boundary="$z>1.6449$" if direction=="higher" else "$z<-1.6449$"
        if locale=="de":
            prompt=rf"Im konstruierten Lehrbeispiel «{label}» legt das Nullmodell $\mu_0={mu}$ fest; die bekannte Populationsstandardabweichung beträgt $\sigma={sigma}$ {u}. Eine Zufallsstichprobe mit $n={n}$ hat $\bar x={mean}$ {u}. Teste $H_0:\mu={mu}$ gegen $H_1:\mu{symbol}{mu}$ bei $\alpha=0.05$. Der Nullwert ist eine zu prüfende Behauptung und keine vorab bekannte Populationswahrheit. (a) Berechne die z-Statistik. (b) Entscheide mit dem einseitigen kritischen Wert 1.6449 im passenden Verteilungsschwanz. (c) Nenne den nach dieser Entscheidung weiterhin möglichen Fehler und interpretiere ihn im Kontext."
            error="Ein Fehler vom Typ I bleibt möglich: Das Verfahren könnte den gerichteten Populationsunterschied melden, obwohl der Nullwert richtig ist." if reject else "Ein Fehler vom Typ II bleibt möglich: Das Verfahren könnte einen echten Populationsunterschied in der festgelegten Richtung übersehen."
            solution=rf"Der Standardfehler ist $SE={sigma}/\sqrt{{{n}}}={number(sigma/math.sqrt(n),4)}$ {u}. Deshalb gilt $z=({mean}-{mu})/{number(sigma/math.sqrt(n),4)}={number(z,4)}$. Die Ablehnungsgrenze lautet {boundary}. Da {number(z,4)} diese Grenze {'überschreitet' if reject else 'nicht überschreitet'}, {'lehnen wir' if reject else 'lehnen wir'} $H_0$ auf dem 5%-Niveau {'ab' if reject else 'nicht ab'}. Die Evidenz {'spricht für den festgelegten gerichteten Populationsunterschied' if reject else 'reicht nicht aus, um den festgelegten gerichteten Populationsunterschied zu belegen'}. {error} Eine Testentscheidung steuert langfristige Fehlerraten; sie beweist nicht, welche Hypothese wahr ist."
        else:
            prompt=rf"Në shembullin mësimor të krijuar «{label}», modeli zero përcakton $\mu_0={mu}$ dhe devijimi standard i njohur i popullatës është $\sigma={sigma}$ {u}. Një kampion i rastësishëm me $n={n}$ ka mesatare $\bar x={mean}$ {u}. Testo $H_0:\mu={mu}$ kundrejt $H_1:\mu{symbol}{mu}$ në $\alpha=0.05$. Vlera zero është pretendim për t'u testuar, jo e vërtetë e popullatës e dhënë paraprakisht. (a) Llogarit statistikën z. (b) Merr vendimin me vlerën kritike njëanëshe 1.6449 në bishtin përkatës. (c) Emërto gabimin statistikor që mbetet i mundshëm pas vendimit dhe interpretoje në këtë kontekst."
            error="Mbetet i mundshëm gabimi i llojit I: procedura mund të raportojë dallimin e drejtuar në popullatë edhe pse vlera zero është e saktë." if reject else "Mbetet i mundshëm gabimi i llojit II: procedura mund të mos zbulojë një dallim të vërtetë në drejtimin e përcaktuar."
            solution=rf"Gabimi standard është $SE={sigma}/\sqrt{{{n}}}={number(sigma/math.sqrt(n),4)}$ {u}. Prandaj $z=({mean}-{mu})/{number(sigma/math.sqrt(n),4)}={number(z,4)}$. Kufiri i refuzimit është {boundary}. Meqë {number(z,4)} {'e kalon' if reject else 'nuk e kalon'} këtë kufi, {'e refuzojmë' if reject else 'nuk e refuzojmë'} $H_0$ në nivelin 5%. Evidenca {'mbështet dallimin e drejtuar të përcaktuar në popullatë' if reject else 'nuk është mjaftueshëm e fortë për të mbështetur përfundimin për dallimin e drejtuar të përcaktuar në popullatë'}. {error} Vendimi i testit kontrollon normat afatgjata të gabimit; nuk provon se cila hipotezë është e vërtetë."
        exg.append(task(3,5,i,label,prompt));sog.append(task(3,5,i,label,solution))
    ex.append("".join(exg));sol.append("".join(sog))

    exg=[group_heading(6,titles[5])];sog=[group_heading(6,titles[5])]
    for i,(_title,_outcome,unit,mu,sigma,n,mean) in enumerate(FULL_INFERENCE_Z,1):
        label=labels[6][i-1];u=units[unit];z=z_test(mean,mu,sigma,n);p=2*(1-normal_cdf(abs(z)));reject=p<.05
        if locale=="de":
            prompt=rf"Im Kontext «{label}» gilt der Referenzmittelwert $\mu_0={mu}$ und die bekannte Standardabweichung $\sigma={sigma}$ {u}. Eine Stichprobe mit $n={n}$ hat $\bar x={mean}$ {u}. (a) Formuliere eine zweiseitige Null- und Alternativhypothese. (b) Berechne z-Statistik und zweiseitigen p-Wert. (c) Entscheide bei $\alpha=0.05$ und interpretiere das Ergebnis, ohne aus einem nicht signifikanten Ergebnis auf das Fehlen eines Effekts zu schliessen."
            solution=rf"Die Hypothesen lauten $H_0:\mu={mu}$ und $H_1:\mu\ne{mu}$. Der Standardfehler ist ${sigma}/\sqrt{{{n}}}={number(sigma/math.sqrt(n),4)}$ {u}; somit gilt $z=({mean}-{mu})/{number(sigma/math.sqrt(n),4)}={number(z,4)}$. Der zweiseitige p-Wert ist $2[1-\Phi(|{number(z,4)}|)]={number(p,4)}$. Da {number(p,4)} {'unter' if reject else 'nicht unter'} 0.05 liegt, {'lehnen wir' if reject else 'lehnen wir'} $H_0$ {'ab' if reject else 'nicht ab'}. Die Stichprobe {'liefert Evidenz dafür, dass der Populationsmittelwert vom Referenzwert abweicht' if reject else 'liefert auf diesem Signifikanzniveau keine ausreichend starke Evidenz für einen Unterschied des Populationsmittelwerts'}. Nichtablehnen wäre begrenzte Evidenz und kein Beweis exakter Gleichheit."
        else:
            prompt=rf"Në kontekstin «{label}», mesatarja referuese e popullatës është $\mu_0={mu}$ dhe devijimi standard i njohur është $\sigma={sigma}$ {u}. Një kampion me $n={n}$ ka $\bar x={mean}$ {u}. (a) Shkruaj hipotezën zero dhe alternative dyanëshe. (b) Llogarit statistikën z dhe vlerën p dyanëshe. (c) Merr vendimin në $\alpha=0.05$ dhe interpretoje pa e trajtuar një rezultat jo domethënës si dëshmi të mungesës së efektit."
            solution=rf"Hipotezat janë $H_0:\mu={mu}$ dhe $H_1:\mu\ne{mu}$. Gabimi standard është ${sigma}/\sqrt{{{n}}}={number(sigma/math.sqrt(n),4)}$ {u}, prandaj $z=({mean}-{mu})/{number(sigma/math.sqrt(n),4)}={number(z,4)}$. Vlera p dyanëshe është $2[1-\Phi(|{number(z,4)}|)]={number(p,4)}$. Meqë {number(p,4)} {'është nën' if reject else 'nuk është nën'} 0.05, {'e refuzojmë' if reject else 'nuk e refuzojmë'} $H_0$. Kampioni {'jep evidencë se mesatarja e popullatës ndryshon nga vlera referuese' if reject else 'nuk jep evidencë mjaftueshëm të fortë për një dallim të mesatares së popullatës në këtë nivel domethënieje'}. Mosrefuzimi pasqyron evidencë të kufizuar, jo provë të barazisë së saktë."
        exg.append(task(3,6,i,label,prompt));sog.append(task(3,6,i,label,solution))
    ex.append("".join(exg));sol.append("".join(sog))

    exg=[group_heading(7,titles[6])];sog=[group_heading(7,titles[6])];z_alpha=normal_ppf(.95);z_power=normal_ppf(.90)
    for i,(_context,unit,mu,sigma,n,mean,delta) in enumerate(POWER_CASES,1):
        label=labels[7][i-1];u=units[unit];z=z_test(mean,mu,sigma,n);p=1-normal_cdf(z);power=1-normal_cdf(z_alpha-delta*math.sqrt(n)/sigma);need=math.ceil(((z_alpha+z_power)*sigma/delta)**2)
        if locale=="de":
            prompt=rf"Ein rechtsseitiger z-Test im Kontext «{label}» verwendet $H_0:\mu={mu}$, die bekannte Populationsstandardabweichung $\sigma={sigma}$ {u}, $\alpha=0.05$ und $n={n}$. Beobachtet wird $\bar x={mean}$. (a) Berechne z-Statistik und p-Wert und entscheide. (b) Berechne bei wahrem Populationsmittelwert $\mu={mu+delta}$ die Teststärke mit $1-\Phi(z_{{0.95}}-\delta\sqrt n/\sigma)$. (c) Bestimme den kleinsten geplanten Stichprobenumfang für 90% Teststärke mit $n=\lceil[(z_{{0.95}}+z_{{0.90}})\sigma/\delta]^2\rceil$. Interpretiere p-Wert und Teststärke als verschiedene bedingte Wahrscheinlichkeiten."
            solution=rf"Die beobachtete Statistik ist $z=({mean}-{mu})/({sigma}/\sqrt{{{n}}})={number(z,4)}$. Ihr rechtsseitiger p-Wert ist $1-\Phi({number(z,4)})={number(p,4)}$; daher {'lehnen wir' if p<.05 else 'lehnen wir'} $H_0$ bei $\alpha=0.05$ {'ab' if p<.05 else 'nicht ab'}. Dieser p-Wert beschreibt mindestens so grosse Ergebnisse unter dem Nullmodell; er ist nicht die Wahrscheinlichkeit, dass $H_0$ wahr ist. Wenn die wahre Verbesserung $\delta={delta}$ beträgt, ist die Teststärke $1-\Phi({number(z_alpha,4)}-{delta}\sqrt{{{n}}}/{sigma})={number(power,4)}$. Sie ist die langfristige Ablehnungswahrscheinlichkeit unter dieser festgelegten Alternative. Für 90% geplante Teststärke gilt $n=\lceil[({number(z_alpha,4)}+{number(z_power,4)}){sigma}/{delta}]^2\rceil={need}$. Es muss aufgerundet werden, weil ein Bruchteil einer Beobachtung das Ziel nicht erfüllen kann."
        else:
            prompt=rf"Një test z me bisht të djathtë në kontekstin «{label}» përdor $H_0:\mu={mu}$; devijimi standard i njohur i popullatës është $\sigma={sigma}$ {u}, ndërsa $\alpha=0.05$ dhe $n={n}$. Mesatarja e vrojtuar është $\bar x={mean}$. (a) Llogarit statistikën z dhe vlerën p dhe merr vendimin. (b) Nëse mesatarja e vërtetë e popullatës është $\mu={mu+delta}$, llogarit fuqinë me $1-\Phi(z_{{0.95}}-\delta\sqrt n/\sigma)$. (c) Gjej madhësinë më të vogël të planifikuar për fuqi 90% me $n=\lceil[(z_{{0.95}}+z_{{0.90}})\sigma/\delta]^2\rceil$. Interpreto vlerën p dhe fuqinë si probabilitete të ndryshme të kushtëzuara."
            solution=rf"Statistika e vrojtuar është $z=({mean}-{mu})/({sigma}/\sqrt{{{n}}})={number(z,4)}$. Vlera p e bishtit të djathtë është $1-\Phi({number(z,4)})={number(p,4)}$, prandaj {'e refuzojmë' if p<.05 else 'nuk e refuzojmë'} $H_0$ në $\alpha=0.05$. Kjo vlerë p përshkruan rezultate të paktën kaq të mëdha nën modelin zero; nuk është probabiliteti që $H_0$ është e vërtetë. Nëse përmirësimi i vërtetë është $\delta={delta}$, fuqia është $1-\Phi({number(z_alpha,4)}-{delta}\sqrt{{{n}}}/{sigma})={number(power,4)}$. Fuqia është probabiliteti afatgjatë i refuzimit nën këtë alternativë të përcaktuar. Për fuqi të planifikuar 90%, $n=\lceil[({number(z_alpha,4)}+{number(z_power,4)}){sigma}/{delta}]^2\rceil={need}$. Rrumbullakosja lart është e domosdoshme sepse një pjesë e vrojtimit nuk mund ta arrijë synimin."
        exg.append(task(3,7,i,label,prompt));sog.append(task(3,7,i,label,solution))
    ex.append("".join(exg));sol.append("".join(sog))

    exg=[group_heading(8,titles[7])];sog=[group_heading(8,titles[7])]
    for i,(_title,_outcome,unit,mu,sigma,n,mean) in enumerate(TWO_SIDED_Z,1):
        label=labels[8][i-1];u=units[unit];se=sigma/math.sqrt(n);margin=1.96*se;lower=mean-margin;upper=mean+margin;z=z_test(mean,mu,sigma,n);p=2*(1-normal_cdf(abs(z)));diff=mean-mu
        if locale=="de":
            prompt=rf"Im unabhängigen konstruierten Beispiel «{label}» gelten der Referenzmittelwert {mu}, die bekannte Populationsstandardabweichung $\sigma={sigma}$ {u}, $n={n}$ und $\bar x={mean}$. (a) Konstruiere das 95%-Konfidenzintervall für $\mu$. (b) Entscheide anhand des Intervalls über den zweiseitigen 5%-Test zu $H_0:\mu={mu}$ und überprüfe die Entscheidung mit einem p-Wert. (c) Berichte den beobachteten Mittelwertunterschied mit der Einheit «{u}» und erkläre, weshalb statistische Signifikanz allein nicht über seine praktische Bedeutung entscheidet."
            solution=rf"Der Standardfehler ist ${sigma}/\sqrt{{{n}}}={number(se,4)}$ {u}, die Fehlerspanne beträgt $1.96({number(se,4)})={number(margin,4)}$. Das 95%-Intervall ist ${mean}\pm{number(margin,4)}=[{number(lower,4)}, {number(upper,4)}]$. Der Nullwert {mu} liegt {'ausserhalb' if not lower<=mu<=upper else 'innerhalb'} dieses Intervalls; daher {'lehnt' if p<.05 else 'lehnt'} der passende zweiseitige Test $H_0$ {'ab' if p<.05 else 'nicht ab'}. Direkt berechnet sind $z={number(z,4)}$ und $p={number(p,4)}$, was dieselbe Entscheidung ergibt. Der beobachtete Unterschied ist ${mean}-{mu}={number(diff,3)}$ {u}. Seine praktische Bedeutung hängt von fachlichen Folgen und der Messskala ab, nicht allein vom p-Wert."
        else:
            prompt=rf"Në shembullin e pavarur të krijuar «{label}», mesatarja referuese është {mu}, devijimi standard i njohur i popullatës është $\sigma={sigma}$ {u}, $n={n}$ dhe $\bar x={mean}$. (a) Ndërto intervalin e besimit 95% për $\mu$. (b) Përdore intervalin për vendimin e testit dyanësh 5% për $H_0:\mu={mu}$ dhe verifikoje me një vlerë p. (c) Raporto dallimin e vrojtuar të mesatareve me njësinë «{u}» dhe shpjego pse domethënia statistikore nuk përcakton vetë rëndësinë praktike."
            solution=rf"Gabimi standard është ${sigma}/\sqrt{{{n}}}={number(se,4)}$ {u}, ndërsa kufiri i gabimit është $1.96({number(se,4)})={number(margin,4)}$. Intervali 95% është ${mean}\pm{number(margin,4)}=[{number(lower,4)}, {number(upper,4)}]$. Vlera zero {mu} është {'jashtë' if not lower<=mu<=upper else 'brenda'} këtij intervali, prandaj testi përkatës dyanësh {'e refuzon' if p<.05 else 'nuk e refuzon'} $H_0$. Drejtpërdrejt, $z={number(z,4)}$ dhe $p={number(p,4)}$, që japin të njëjtin vendim. Dallimi i vrojtuar është ${mean}-{mu}={number(diff,3)}$ {u}. Rëndësia praktike varet nga pasojat në fushën përkatëse dhe nga shkalla e matjes, jo vetëm nga vlera p."
        exg.append(task(3,8,i,label,prompt));sog.append(task(3,8,i,label,solution))
    ex.append("".join(exg));sol.append("".join(sog))

    exg=[group_heading(9,titles[8])];sog=[group_heading(9,titles[8])]
    for i,(df,q99) in enumerate(T_PERCENTILES,1):
        title=(f"Quantile bei {df} Freiheitsgraden" if locale=="de" else f"Kuantilet me {df} shkallë lirie")
        if locale=="de":
            prompt=rf"Für eine t-Verteilung mit {df} Freiheitsgraden gibt eine Referenztabelle $t_{{0.99}}({df})={number(q99,4)}$ an. (a) Bestimme $t_{{0.01}}({df})$ mithilfe der Symmetrie. (b) Erkläre beide Quantile als kumulierte Flächen. (c) Vergleiche den Betrag mit dem 0.99-Quantil der Standardnormalverteilung 2.3263 und erkläre die Entwicklung bei zunehmenden Freiheitsgraden."
            solution=rf"Wegen der Symmetrie gilt $t_{{0.01}}({df})=-t_{{0.99}}({df})=-{number(q99,4)}$. Das obere Quantil erfüllt $P(T\leq {number(q99,4)})=0.99$; das untere erfüllt $P(T\leq-{number(q99,4)})=0.01$. Sein Betrag {number(q99,4)} ist grösser als 2.3263, weil eine t-Verteilung mit endlich vielen Freiheitsgraden schwerere Verteilungsschwänze als die Standardnormalverteilung hat. Mit wachsenden Freiheitsgraden nimmt die zusätzliche Unsicherheit aus der Schätzung von $\sigma$ ab und die t-Verteilung nähert sich der Standardnormalverteilung."
        else:
            prompt=rf"Për një shpërndarje t me {df} shkallë lirie, një tabelë referuese jep $t_{{0.99}}({df})={number(q99,4)}$. (a) Përcakto $t_{{0.01}}({df})$ duke përdorur simetrinë. (b) Shpjego çfarë do të thotë secili kuantil si sipërfaqe kumulative. (c) Krahaso madhësinë me kuantilin 0.99 të normales standarde 2.3263 dhe shpjego çfarë ndodh kur rriten shkallët e lirisë."
            solution=rf"Nga simetria, $t_{{0.01}}({df})=-t_{{0.99}}({df})=-{number(q99,4)}$. Kuantili i sipërm plotëson $P(T\leq {number(q99,4)})=0.99$; i poshtmi plotëson $P(T\leq-{number(q99,4)})=0.01$. Madhësia e tij {number(q99,4)} është më e madhe se 2.3263 sepse shpërndarja t me shkallë të fundme lirie ka bishta më të rëndë se normalja standarde. Kur rriten shkallët e lirisë, zvogëlohet pasiguria shtesë nga vlerësimi i $\sigma$ dhe shpërndarja t i afrohet normales standarde."
        exg.append(task(3,9,i,title,prompt));sog.append(task(3,9,i,title,solution))
    ex.append("".join(exg));sol.append("".join(sog))

    exg=[group_heading(10,titles[9])];sog=[group_heading(10,titles[9])]
    for i,(_context,_outcome,unit,mu,n,mean,sd,crit) in enumerate(ONE_SAMPLE_T,1):
        label=labels[10][i-1];u=units[unit];lower=(i in (2,4,6,8,10));symbol="<" if lower else ">";stat=(mean-mu)/(sd/math.sqrt(n));reject=(stat < -crit if lower else stat > crit);boundary=('$t<-'+number(crit,4)+'$' if lower else '$t>'+number(crit,4)+'$')
        if locale=="de":
            prompt=rf"Eine Stichprobe mit $n={n}$ im Kontext «{label}» hat $\bar x={mean}$ {u} und die Stichprobenstandardabweichung $s={sd}$ {u}. Die Populationsstandardabweichung ist unbekannt. Teste $H_0:\mu={mu}$ gegen $H_1:\mu{symbol}{mu}$ bei $\alpha=0.05$. (a) Erkläre, weshalb das t-Verfahren für eine Stichprobe verwendet wird. (b) Berechne die Statistik mit {n-1} Freiheitsgraden. (c) Vergleiche sie mit dem einseitigen kritischen Betrag {number(crit,4)} und interpretiere die Entscheidung."
            solution=rf"Die Populationsstandardabweichung ist unbekannt und wird durch $s={sd}$ ersetzt. Deshalb verwendet das Verfahren $T=(\bar X-\mu_0)/(S/\sqrt n)$ mit $df=n-1={n-1}$. Hier sind $SE={sd}/\sqrt{{{n}}}={number(sd/math.sqrt(n),4)}$ {u} und $t=({mean}-{mu})/{number(sd/math.sqrt(n),4)}={number(stat,4)}$. Die Ablehnungsregel ist {boundary}. Die Statistik {'überschreitet' if reject else 'überschreitet nicht'} diese Grenze; daher {'lehnen wir' if reject else 'lehnen wir'} $H_0$ {'ab' if reject else 'nicht ab'}. Die Stichprobe {'stützt' if reject else 'liefert keine ausreichend starke Evidenz für'} die festgelegte gerichtete Veränderung. Diese Interpretation setzt unabhängige Beobachtungen und bei dieser kleinen Stichprobe eine annähernd normal verteilte Grundgesamtheit voraus."
        else:
            prompt=rf"Një kampion me $n={n}$ në kontekstin «{label}» ka $\bar x={mean}$ {u} dhe devijim standard të kampionit $s={sd}$ {u}. Devijimi standard i popullatës është i panjohur. Testo $H_0:\mu={mu}$ kundrejt $H_1:\mu{symbol}{mu}$ në $\alpha=0.05$. (a) Shpjego pse përdoret procedura t për një kampion. (b) Llogarit statistikën me {n-1} shkallë lirie. (c) Krahasoje me madhësinë kritike njëanëshe {number(crit,4)} dhe interpreto vendimin."
            solution=rf"Devijimi standard i popullatës është i panjohur dhe zëvendësohet me $s={sd}$, prandaj procedura përdor $T=(\bar X-\mu_0)/(S/\sqrt n)$ me $df=n-1={n-1}$. Këtu $SE={sd}/\sqrt{{{n}}}={number(sd/math.sqrt(n),4)}$ {u} dhe $t=({mean}-{mu})/{number(sd/math.sqrt(n),4)}={number(stat,4)}$. Rregulla e refuzimit është {boundary}. Statistika {'e kalon' if reject else 'nuk e kalon'} këtë kufi, prandaj {'e refuzojmë' if reject else 'nuk e refuzojmë'} $H_0$. Kampioni {'e mbështet' if reject else 'nuk jep evidencë mjaftueshëm të fortë për'} ndryshimin e drejtuar të përcaktuar, duke supozuar vrojtime të pavarura dhe një model afërsisht normal të popullatës për këtë procedurë me kampion të vogël."
        exg.append(task(3,10,i,label,prompt));sog.append(task(3,10,i,label,solution))
    ex.append("".join(exg));sol.append("".join(sog))

    exg=[group_heading(11,titles[10])];sog=[group_heading(11,titles[10])]
    for i,(_context,unit,n,mean,sd,crit,null) in enumerate(T_INTERVALS,1):
        label=labels[11][i-1];u=units[unit];se=sd/math.sqrt(n);margin=crit*se;lo=mean-margin;hi=mean+margin;reject=not(lo<=null<=hi)
        if locale=="de":
            prompt=rf"Eine Zufallsstichprobe im Kontext «{label}» mit $n={n}$ hat $\bar x={mean}$ {u} und $s={sd}$ {u}. Eine t-Tabelle gibt $t_{{0.975}}({n-1})={number(crit,4)}$ an. (a) Konstruiere ein 95%-Konfidenzintervall für den Populationsmittelwert. (b) Teste damit $H_0:\mu={null}$ gegen $H_1:\mu\ne{null}$ bei 5%. (c) Erkläre, weshalb Intervall und passender zweiseitiger Test übereinstimmen, und formuliere die richtige Interpretation von 95% Konfidenz über wiederholte Stichproben."
            solution=rf"Der geschätzte Standardfehler ist $s/\sqrt n={sd}/\sqrt{{{n}}}={number(se,4)}$ {u}. Die Fehlerspanne ist ${number(crit,4)}({number(se,4)})={number(margin,4)}$; damit lautet das Intervall ${mean}\pm{number(margin,4)}=[{number(lo,4)}, {number(hi,4)}]$. Der Nullwert {null} liegt {'ausserhalb' if reject else 'innerhalb'} des Intervalls, weshalb der passende zweiseitige 5%-Test $H_0$ {'ablehnt' if reject else 'nicht ablehnt'}. Beide Verfahren verwenden denselben Standardfehler und symmetrische Grenzen von 2.5% in den Verteilungsschwänzen. Bei wiederholten Stichproben überdecken 95% der nach dieser Methode erzeugten Intervalle unter den Modellannahmen den festen Populationsmittelwert; das fertige Intervall weist dem festen Parameter keine Wahrscheinlichkeit von 95% zu."
        else:
            prompt=rf"Një kampion i rastësishëm në kontekstin «{label}» me $n={n}$ ka $\bar x={mean}$ {u} dhe $s={sd}$ {u}. Një tabelë t jep $t_{{0.975}}({n-1})={number(crit,4)}$. (a) Ndërto një interval besimi 95% për mesataren e popullatës. (b) Përdore për të testuar $H_0:\mu={null}$ kundrejt $H_1:\mu\ne{null}$ në 5%. (c) Shpjego pse intervali dhe testi dyanësh përkatës pajtohen dhe jep interpretimin e saktë të besimit 95% në kampione të përsëritura."
            solution=rf"Gabimi standard i vlerësuar është $s/\sqrt n={sd}/\sqrt{{{n}}}={number(se,4)}$ {u}. Kufiri i gabimit është ${number(crit,4)}({number(se,4)})={number(margin,4)}$, kështu që intervali është ${mean}\pm{number(margin,4)}=[{number(lo,4)}, {number(hi,4)}]$. Vlera zero {null} është {'jashtë' if reject else 'brenda'} intervalit, prandaj testi përkatës dyanësh 5% {'e refuzon' if reject else 'nuk e refuzon'} $H_0$. Të dyja procedurat përdorin të njëjtin gabim standard dhe kufij simetrikë prej 2.5% në bishta, ndaj vendimet pajtohen. Në kampione të përsëritura, 95% e intervaleve të prodhuara me këtë metodë e mbulojnë mesataren fikse të popullatës nën supozimet e modelit; intervali i përfunduar nuk i cakton probabilitet 95% atij parametri fiks."
        exg.append(task(3,11,i,label,prompt));sog.append(task(3,11,i,label,solution))
    ex.append("".join(exg));sol.append("".join(sog))

    exg=[group_heading(12,titles[11])];sog=[group_heading(12,titles[11])]
    for i,(_context,_outcome,n1,n2,m1,m2,var1,var2,crit) in enumerate(POOLED_T,1):
        label=labels[12][i-1];df=n1+n2-2;sp2=((n1-1)*var1+(n2-1)*var2)/df;se=math.sqrt(sp2*(1/n1+1/n2));stat=(m1-m2)/se;reject=stat>crit
        if locale=="de":
            prompt=rf"Zwei unabhängige Gruppen werden im konstruierten Kontext «{label}» verglichen. Gruppe 1 hat $n_1={n1}$, $\bar x_1={m1}$ und $s_1^2={var1}$; Gruppe 2 hat $n_2={n2}$, $\bar x_2={m2}$ und $s_2^2={var2}$. Verwende das Modell gleicher Populationsvarianzen. (a) Erkläre, weshalb die Stichproben unabhängig und nicht gepaart sind. (b) Berechne gepoolte Varianz, Standardfehler und t-Statistik für $\mu_1>\mu_2$. (c) Vergleiche mit dem einseitigen kritischen Wert {number(crit,4)} bei $\alpha=0.05$ und interpretiere. (d) Nenne die zentralen Bedingungen von Design und Modell."
            solution=rf"Verschiedene Beobachtungseinheiten gehören zu den zwei Gruppen; deshalb gibt es keine fallweise Paarung. Unter dem Modell gleicher Populationsvarianzen ist $s_p^2=[({n1}-1){var1}+({n2}-1){var2}]/({n1}+{n2}-2)={number(sp2,4)}$. Der Standardfehler beträgt $\sqrt{{{number(sp2,4)}(1/{n1}+1/{n2})}}={number(se,4)}$. Mit $df={df}$ gilt $t=({m1}-{m2})/{number(se,4)}={number(stat,4)}$. Da {number(stat,4)} den Wert {number(crit,4)} {'überschreitet' if reject else 'nicht überschreitet'}, {'lehnen wir' if reject else 'lehnen wir'} die Nullhypothese gleicher Mittelwerte zugunsten von $\mu_1>\mu_2$ {'ab' if reject else 'nicht ab'}. Das Ergebnis {'stützt' if reject else 'liefert keine ausreichend starke Evidenz für'} einen höheren Populationsmittelwert in Gruppe 1. Erforderlich sind unabhängige Beobachtungen, unabhängig gezogene Gruppen, in beiden Populationen ein für diese Stichprobenumfänge annähernd normales Ergebnis und gleiche Populationsvarianzen. Eine kausale Interpretation verlangt zusätzlich eine zufällige Zuweisung."
        else:
            prompt=rf"Dy grupe të pavarura krahasohen në kontekstin e krijuar «{label}». Grupi 1 ka $n_1={n1}$, $\bar x_1={m1}$ dhe $s_1^2={var1}$; Grupi 2 ka $n_2={n2}$, $\bar x_2={m2}$ dhe $s_2^2={var2}$. Përdor modelin me varianca të barabarta të popullatave. (a) Shpjego pse kampionet janë të pavarura dhe jo të çiftuara. (b) Llogarit variancën e përbashkët, gabimin standard dhe statistikën t për $\mu_1>\mu_2$. (c) Krahasoje me vlerën kritike njëanëshe {number(crit,4)} në $\alpha=0.05$ dhe interpretoje. (d) Jep kushtet kryesore të dizajnit dhe modelit."
            solution=rf"Njësi të ndryshme vrojtimi u përkasin dy grupeve, prandaj nuk ka çiftim rast për rast. Nën modelin me varianca të barabarta të popullatave, $s_p^2=[({n1}-1){var1}+({n2}-1){var2}]/({n1}+{n2}-2)={number(sp2,4)}$. Gabimi standard është $\sqrt{{{number(sp2,4)}(1/{n1}+1/{n2})}}={number(se,4)}$. Me $df={df}$, $t=({m1}-{m2})/{number(se,4)}={number(stat,4)}$. Meqë {number(stat,4)} {'e tejkalon' if reject else 'nuk e tejkalon'} {number(crit,4)}, {'e refuzojmë' if reject else 'nuk e refuzojmë'} hipotezën zero të mesatareve të barabarta në favor të $\mu_1>\mu_2$. Rezultati {'mbështet' if reject else 'nuk jep evidencë mjaftueshëm të fortë për'} një mesatare më të lartë të popullatës në Grupin 1. Procedura kërkon vrojtime të pavarura, grupe të kampionuara në mënyrë të pavarur, rezultat afërsisht normal brenda secilës popullatë për këto madhësi kampioni dhe varianca të barabarta të popullatave. Për interpretim shkakor nevojitet edhe caktim i rastësishëm."
        exg.append(task(3,12,i,label,prompt));sog.append(task(3,12,i,label,solution))
    ex.append("".join(exg));sol.append("".join(sog))
    return ex,sol


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--locale", choices=("en", "de", "sq"), default="en")
    args = parser.parse_args()
    exercises, solutions = render_localized(args.locale)
    write_pair(3, args.locale, 12, exercises, solutions)
    validate_sources_allowing_incomplete_locales(args.locale, topic=3)
    print(f"Generated and source-validated Topic 3 {args.locale} exercise and solution sources.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
