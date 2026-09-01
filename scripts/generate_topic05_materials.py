#!/usr/bin/env python3
"""Generate Ratiomera's multilingual Topic 5 practice pair.

The ten registered worksheet groups determine skills and approximate
difficulty only. The generator uses new settings, values, questions, and worked
solutions. English remains canonical; the reviewed German and Albanian
versions reuse its identifiers, values, formulas, and results.
"""

from __future__ import annotations

import argparse
import math

from intro_stats_practice_support import (
    group_heading,
    number,
    student_t_ppf,
    student_t_two_sided_p,
    task,
    validate_sources_allowing_incomplete_locales,
    write_pair,
)


CONTEXTS = [
    ("Weekly practice and reasoning", "weekly practice hours", "hours", "reasoning score", "points"),
    ("Archive experience and retrieval time", "months of archive experience", "months", "retrieval time", "minutes"),
    ("Museum visits and knowledge", "museum visits this year", "visits", "historical-knowledge score", "points"),
    ("Reading time and comprehension", "weekly reading time", "hours", "comprehension score", "points"),
    ("Route familiarity and navigation errors", "route-familiarity score", "points", "navigation-error count", "errors"),
    ("Workshop attendance and confidence", "workshop sessions attended", "sessions", "confidence score", "points"),
    ("Notification load and focus", "daily notification count", "notifications", "focus score", "points"),
    ("Search practice and accuracy", "completed search-practice sets", "sets", "search-accuracy score", "points"),
    ("Travel distance and visit duration", "travel distance", "kilometers", "visit duration", "minutes"),
    ("Discussion participation and reasoning", "discussion contributions", "contributions", "reasoning score", "points"),
]


SINGULAR_UNITS = {
    "hours": "hour",
    "months": "month",
    "visits": "visit",
    "points": "point",
    "sessions": "session",
    "notifications": "notification",
    "sets": "set",
    "kilometers": "kilometer",
    "contributions": "contribution",
    "pages": "page",
    "attempts": "attempt",
    "blocks": "block",
    "stops": "stop",
}


RAW_SUM_CASES = [
    ([2,3,4,5,6,7,8,9], [58,60,65,67,71,73,78,80], 6),
    ([2,4,6,8,10,12,14,16], [68,64,61,57,55,50,48,45], 9),
    ([0,1,2,3,4,5,6,7], [45,48,52,56,61,65,68,74], 4),
    ([1,2,3,4,5,6,7,8], [52,56,60,63,69,72,76,81], 5),
    ([2,3,4,5,6,7,8,9], [14,12,11,9,8,6,5,4], 6),
    ([0,1,2,3,4,5,6,7], [38,43,47,53,56,62,65,70], 4),
    ([10,20,30,40,50,60,70,80], [88,84,79,73,69,64,58,54], 45),
    ([1,2,3,4,5,6,7,8], [55,59,63,68,72,77,81,86], 5),
    ([2,4,6,8,10,12,14,16], [65,70,75,82,88,94,101,107], 9),
    ([0,1,2,3,4,5,6,7], [50,54,58,61,66,69,73,78], 4),
]


SUMMARY_CASES = [
    (5.5, 68, 2.2, 8.0, 11.0, 7.0),
    (18, 42, 6.0, 9.0, -36.0, 24),
    (4.5, 62, 1.8, 10.0, 13.5, 6),
    (7, 74, 2.5, 9.0, 15.75, 9),
    (55, 8, 12.0, 3.0, -25.2, 65),
    (3.5, 51, 1.5, 7.0, 7.35, 5),
    (48, 70, 15.0, 11.0, -82.5, 35),
    (6, 76, 2.0, 8.0, 11.2, 9),
    (14, 95, 5.0, 18.0, 54.0, 18),
    (8, 67, 3.0, 10.0, 18.0, 11),
]


COEFFICIENT_CASES = [
    (42, 3.2, 1.5, 8.0, 2),
    (75, -1.2, 6.0, 9.0, 20),
    (48, 4.5, 1.8, 10.0, 3),
    (55, 2.8, 2.5, 9.0, 8),
    (18, -0.12, 12.0, 3.0, 60),
    (35, 3.5, 1.5, 7.0, 4),
    (82, -0.30, 15.0, 11.0, 50),
    (60, 4.0, 2.0, 8.0, 7),
    (50, 2.4, 5.0, 18.0, 16),
    (40, 3.0, 3.0, 10.0, 10),
]


SECOND_PREDICTORS = [
    ("guided-study sessions", "sessions"),
    ("retrieval-practice sessions", "sessions"),
    ("history-reading sessions", "sessions"),
    ("annotated pages per week", "pages"),
    ("prior route attempts", "attempts"),
    ("peer-feedback sessions", "sessions"),
    ("scheduled focus blocks", "blocks"),
    ("months of archive experience", "months"),
    ("planned stops", "stops"),
    ("preparation time", "hours"),
]


OUTPUT_COMPARISONS = [
    (38, 2.6, 0.7, 0.49, 45, 3.1, 0.9, 0.58),
    (80, -1.5, 0.5, -0.46, 70, -2.2, 0.8, -0.35),
    (45, 4.2, 1.1, 0.58, 50, 3.6, 1.0, 0.44),
    (52, 3.0, 0.9, 0.40, 48, 0.9, 0.3, 0.55),
    (15, -0.10, 0.04, -0.35, 13, -0.55, 0.16, -0.62),
    (33, 3.8, 1.0, 0.55, 40, 2.7, 0.8, 0.47),
    (85, -0.28, 0.08, -0.42, 78, 2.4, 0.7, 0.51),
    (58, 4.4, 1.2, 0.63, 62, 1.5, 0.5, 0.39),
    (47, 2.1, 0.8, 0.38, 55, 4.5, 1.1, 0.66),
    (43, 2.7, 0.9, 0.45, 49, 3.4, 1.0, 0.52),
]


FIT_CASES = [
    (40, 120, 180, 720, 8),
    (42, -84, 210, 630, 20),
    (36, 144, 240, 840, 6),
    (50, 135, 225, 900, 9),
    (44, -66, 132, 528, 60),
    (38, 114, 190, 760, 5),
    (48, -96, 240, 960, 45),
    (46, 138, 230, 920, 8),
    (52, 104, 208, 832, 18),
    (40, 100, 200, 800, 10),
]


INFERENCE_CASES = [
    (24, 2.4, 0.75), (30, -1.6, 0.60),
    (36, 3.1, 1.05), (42, 2.0, 0.68),
    (50, -0.11, 0.05), (60, 2.8, 0.90),
    (70, -0.24, 0.10), (80, 3.6, 1.10),
    (90, 1.5, 0.72), (100, 1.2, 0.62),
]


MODEL_CASES = [
    (20, 0.28, 4.414), (25, 0.22, 4.279), (30, 0.18, 4.196),
    (35, 0.15, 4.139), (40, 0.12, 4.098), (50, 0.10, 4.043),
    (60, 0.08, 4.007), (75, 0.07, 3.972), (90, 0.06, 3.949),
    (120, 0.05, 3.921),
]


WEAK_CASES = [
    (28, 0.16, 0.14, 1.11, 0.276), (34, -0.12, 0.11, -1.08, 0.288),
    (40, 0.10, 0.09, 1.09, 0.283), (46, 0.08, 0.08, 0.99, 0.329),
    (52, -0.07, 0.07, -1.00, 0.323), (60, 0.06, 0.06, 0.99, 0.326),
    (70, -0.05, 0.05, -0.99, 0.326), (80, 0.05, 0.05, 1.00, 0.320),
    (90, 0.04, 0.04, 0.99, 0.325), (100, -0.04, 0.04, -1.00, 0.320),
]


RESIDUAL_HISTOGRAMS = [
    ("roughly symmetric", [2,7,15,22,15,7,2], "approximately normal"),
    ("strong right tail", [18,20,14,8,4,2,1], "right-skewed"),
    ("roughly symmetric", [1,6,14,20,14,6,1], "approximately normal"),
    ("one extreme upper bin", [3,8,16,22,15,5,1,0,1], "an upper outlier or heavy right tail"),
    ("flat shoulders", [5,9,12,13,12,9,5], "symmetric but flatter than a normal shape"),
    ("strong left tail", [1,2,4,8,14,20,18], "left-skewed"),
    ("roughly symmetric", [2,8,17,24,17,8,2], "approximately normal"),
    ("two peaks", [3,12,18,7,6,17,11,3], "bimodal"),
    ("roughly symmetric with heavy tails", [5,7,12,20,12,7,5], "symmetric with heavier tails"),
    ("strong center", [1,4,10,30,10,4,1], "symmetric but more sharply peaked"),
]


RESIDUAL_PATTERNS = [
    ([-0.1,0.2,-0.2,0.1,0.0], [2.1,2.0,2.2,2.1,2.0], "random horizontal band"),
    ([2.4,0.6,-1.0,0.5,2.3], [1.5,1.6,1.7,1.6,1.5], "curvature"),
    ([0.0,0.1,-0.1,0.2,0.0], [0.8,1.2,1.8,2.6,3.5], "increasing spread"),
    ([-2.0,-0.7,0.8,0.4,-1.8], [1.4,1.5,1.6,1.5,1.4], "curvature"),
    ([0.1,-0.1,0.0,0.1,-0.1], [3.2,2.6,1.9,1.3,0.8], "decreasing spread"),
    ([0.2,-0.2,0.1,-0.1,0.0], [1.8,1.9,1.7,1.8,1.9], "random horizontal band"),
    ([-1.5,-0.4,0.6,0.3,-1.4], [1.2,1.3,1.4,1.3,1.2], "curvature"),
    ([0.0,0.1,0.0,-0.1,0.1], [0.7,1.1,1.7,2.4,3.2], "increasing spread"),
    ([0.1,0.0,-0.1,0.0,0.1], [2.0,2.1,1.9,2.0,2.1], "random horizontal band"),
    ([1.8,0.5,-0.9,0.4,1.7], [1.3,1.4,1.5,1.4,1.3], "curvature"),
]


def render_english() -> tuple[list[str],list[str]]:
    ex=[];sol=[]

    exg=[group_heading(1,"Least-Squares Coefficients from Raw Sums")]; sog=[group_heading(1,"Least-Squares Coefficients from Raw Sums")]
    for i,((title,x,xunit,y,yunit),(x_values,y_values,x0)) in enumerate(zip(CONTEXTS,RAW_SUM_CASES),1):
        x_unit_singular=SINGULAR_UNITS[xunit]
        n=len(x_values);sx=sum(x_values);sy=sum(y_values);sx2=sum(value*value for value in x_values);sxy=sum(a*b for a,b in zip(x_values,y_values))
        xbar=sx/n;ybar=sy/n;sxx=sx2-sx*sx/n;sxyc=sxy-sx*sy/n;b1=sxyc/sxx;b0=ybar-b1*xbar;pred=b0+b1*x0
        coordinates=", ".join(f"({a}, {b})" for a,b in zip(x_values,y_values));x_min=min(x_values);x_max=max(x_values)
        direction="upward" if b1>0 else "downward"
        zero_scope=(f"Zero is inside the observed range [{x_min}, {x_max}], so the intercept describes a fitted baseline represented by these data." if x_min<=0<=x_max else f"Zero is outside the observed range [{x_min}, {x_max}], so the intercept is mathematically needed but should not be treated as a supported observed baseline.")
        exg.append(task(5,1,i,title,f"A hypothetical dataset contains these ordered pairs $(X,Y)$: {coordinates}. Here $X$ is {x} and $Y$ is {y}. The calculation summaries are $n={n}$, $\\sum x={sx}$, $\\sum y={sy}$, $\\sum x^2={sx2}$, and $\\sum xy={sxy}$. (a) Plot the coordinates, report the observed $X$ range, and describe whether an approximately straight upward or downward pattern is plausible and whether any listed point is visibly isolated. (b) Calculate $\\bar x$, $\\bar y$, $S_{{xx}}=\\sum x^2-(\\sum x)^2/n$, and $S_{{xy}}=\\sum xy-(\\sum x)(\\sum y)/n$. (c) Find $b_1=S_{{xy}}/S_{{xx}}$ and $b_0=\\bar y-b_1\\bar x$ and interpret both coefficients with units and appropriate scope. (d) Predict $Y$ at $X={x0}$ {xunit} and verify that this is an in-range prediction."))
        sog.append(task(5,1,i,title,f"The completed scatterplot uses the coordinates {coordinates}, with horizontal range [{x_min}, {x_max}]. Reading the ordered points from left to right shows an approximately straight {direction} pattern and no single coordinate separated sharply from all neighboring points. The means are $\\bar x={sx}/{n}={number(xbar,4)}$ {xunit} and $\\bar y={sy}/{n}={number(ybar,4)}$ {yunit}. The corrected sums are $S_{{xx}}={sx2}-{sx}^2/{n}={number(sxx,4)}$ and $S_{{xy}}={sxy}-{sx}({sy})/{n}={number(sxyc,4)}$. Thus $b_1={number(sxyc,4)}/{number(sxx,4)}={number(b1,4)}$ {yunit} per {x_unit_singular}, and $b_0={number(ybar,4)}-({number(b1,4)})({number(xbar,4)})={number(b0,4)}$ {yunit}. The slope is the fitted outcome difference of {number(b1,4)} {yunit} for a one-{x_unit_singular} increase in {x}. The intercept is the fitted outcome at $X=0$. {zero_scope} The fitted equation is $\\widehat Y={number(b0,4)}+({number(b1,4)})X$. Because {x_min} $\\leq$ {x0} $\\leq$ {x_max}, the request is interpolation. At $X={x0}$, $\\widehat Y={number(b0,4)}+({number(b1,4)})({x0})={number(pred,4)}$ {yunit}. This is an estimated conditional mean, not a guaranteed outcome for one case."))
    ex.append("".join(exg));sol.append("".join(sog))

    exg=[group_heading(2,"From Means, Standard Deviations, and Covariance to a Line")];sog=[group_heading(2,"From Means, Standard Deviations, and Covariance to a Line")]
    for i,((title,x,xunit,y,yunit),(mx,my,sx,sy,cov,x0)) in enumerate(zip(CONTEXTS,SUMMARY_CASES),1):
        r=cov/(sx*sy);b1=cov/(sx*sx);b0=my-b1*mx;pred=b0+b1*x0
        exg.append(task(5,2,i,title,f"Summary statistics are $\\bar x={mx}$, $\\bar y={my}$, $s_x={sx}$, $s_y={sy}$, and sample covariance $s_{{xy}}={cov}$. (a) Calculate Pearson's $r=s_{{xy}}/(s_xs_y)$. (b) Find the regression slope $b_1=s_{{xy}}/s_x^2$ and intercept. (c) Predict {y} when {x} equals {x0} {xunit}. (d) Explain how correlation and slope use the same joint variation but answer different questions."))
        sog.append(task(5,2,i,title,f"The correlation is $r={cov}/({sx}\\times{sy})={number(r,4)}$. The slope is $b_1={cov}/{sx}^2={number(b1,4)}$ {yunit} per one unit of $X$, and $b_0={my}-({number(b1,4)})({mx})={number(b0,4)}$ {yunit}. At $X={x0}$, $\\widehat Y={number(b0,4)}+({number(b1,4)})({x0})={number(pred,4)}$ {yunit}. Correlation is unit-free and symmetric between $X$ and $Y$. The regression slope names $Y$ as the outcome, retains measurement units, and describes fitted outcome change per predictor unit. Both begin with the same signed co-variation."))
    ex.append("".join(exg));sol.append("".join(sog))

    exg=[group_heading(3,"Unstandardized and Standardized Slopes")];sog=[group_heading(3,"Unstandardized and Standardized Slopes")]
    for i,((title,x,xunit,y,yunit),(b0,b1,sx,sy,x0)) in enumerate(zip(CONTEXTS,COEFFICIENT_CASES),1):
        beta=b1*sx/sy;pred=b0+b1*x0
        exg.append(task(5,3,i,title,f"A fitted model is $\\widehat Y={b0}+({b1})X$, with $s_x={sx}$ {xunit} and $s_y={sy}$ {yunit}. (a) Interpret the unstandardized slope in original units and calculate the fitted value at $X={x0}$. (b) Calculate the standardized slope $\\beta^*=b_1s_x/s_y$. (c) Explain what one predictor standard deviation means in the standardized interpretation and why the two slope numbers should not be compared without their scales."))
        sog.append(task(5,3,i,title,f"The unstandardized slope {b1} means that a one-unit difference in {x} accompanies a fitted difference of {b1} {yunit} in {y}. The prediction is $\\widehat Y={b0}+({b1})({x0})={number(pred,4)}$ {yunit}. The standardized slope is $\\beta^*=({b1})({sx})/{sy}={number(beta,4)}$. Thus a one-standard-deviation difference in the predictor, equal to {sx} {xunit}, accompanies a fitted difference of {number(beta,4)} outcome standard deviations. The unstandardized number answers an original-unit question; the standardized number answers a standard-deviation question."))
    ex.append("".join(exg));sol.append("".join(sog))

    exg=[group_heading(4,"Comparing Two Simple-Regression Outputs")];sog=[group_heading(4,"Comparing Two Simple-Regression Outputs")]
    for i,((title,x,xunit,y,yunit),(second_x,second_unit),(b0a,b1a,se1a,beta_a,b0b,b1b,se1b,beta_b)) in enumerate(zip(CONTEXTS,SECOND_PREDICTORS,OUTPUT_COMPARISONS),1):
        x_unit_singular=SINGULAR_UNITS[xunit];second_unit_singular=SINGULAR_UNITS[second_unit]
        t_a=b1a/se1a;t_b=b1b/se1b
        stronger=x if abs(beta_a)>abs(beta_b) else second_x
        exg.append(task(5,4,i,title,f"Two separate simple regressions use {y} as the outcome. Output A, with {x} as predictor, reports: intercept estimate {b0a}; predictor estimate {b1a}, $SE={se1a}$, $t={number(t_a,2)}$, standardized slope $\\beta^*={beta_a}$. Output B, with {second_x} as predictor, reports: intercept estimate {b0b}; predictor estimate {b1b}, $SE={se1b}$, $t={number(t_b,2)}$, standardized slope $\\beta^*={beta_b}$. (a) Locate the two predictor coefficients and distinguish them from the intercepts. (b) Interpret each unstandardized slope with its original units. (c) Compare the directions and absolute standardized slopes. (d) Explain why the unstandardized slopes should not be ranked directly when predictor units differ and why neither separate model proves causation."))
        sog.append(task(5,4,i,title,f"The predictor estimates are {b1a} in Output A and {b1b} in Output B; {b0a} and {b0b} are intercepts. In Output A, a one-{x_unit_singular} increase in {x} accompanies a fitted {'increase' if b1a>0 else 'decrease'} of {number(abs(b1a),2)} {yunit} in {y}. In Output B, a one-{second_unit_singular} increase in {second_x} accompanies a fitted {'increase' if b1b>0 else 'decrease'} of {number(abs(b1b),2)} {yunit}. The standardized slopes are {beta_a} and {beta_b}. They express fitted changes in outcome standard deviations per one predictor standard deviation, so their absolute values can be compared: {stronger} has the larger absolute standardized association in these two separate models. In a simple regression with an intercept, each standardized slope also equals that predictor's Pearson correlation with the outcome. The raw slopes cannot be ranked as strengths because a one-{x_unit_singular} change in {x} is not the same scale as a one-{second_unit_singular} change in {second_x}. These are two bivariate associations; they neither hold the other predictor constant nor establish a causal effect."))
    ex.append("".join(exg));sol.append("".join(sog))

    exg=[group_heading(5,"Coefficients and Explained Variation")];sog=[group_heading(5,"Coefficients and Explained Variation")]
    for i,((title,x,xunit,y,yunit),(b0,sxy,sxx,sst,x0)) in enumerate(zip(CONTEXTS,FIT_CASES),1):
        b1=sxy/sxx;ssr=sxy*sxy/sxx;sse=sst-ssr;r2=ssr/sst;pred=b0+b1*x0
        exg.append(task(5,5,i,title,f"A centered calculation gives $S_{{xy}}={sxy}$, $S_{{xx}}={sxx}$, total sum of squares $SST={sst}$, error sum of squares $SSE={number(sse,4)}$, and intercept $b_0={b0}$. (a) Calculate $b_1$. (b) Find $SSR=SST-SSE$ and $R^2=SSR/SST$. (c) Verify that $SSR=b_1S_{{xy}}$, predict at $X={x0}$, and interpret $R^2$ as sample variation explained by the fitted line rather than as the proportion of people whose outcomes were predicted correctly."))
        sog.append(task(5,5,i,title,f"The slope is $b_1=S_{{xy}}/S_{{xx}}={sxy}/{sxx}={number(b1,4)}$. Explained variation is $SSR={sst}-{number(sse,4)}={number(ssr,4)}$, which also equals $b_1S_{{xy}}={number(b1,4)}({sxy})={number(ssr,4)}$. Therefore $R^2={number(ssr,4)}/{sst}={number(r2,4)}$. The fitted value is $\\widehat Y={b0}+({number(b1,4)})({x0})={number(pred,4)}$. The model accounts for {number(100*r2,1)}% of the sample's total squared variation around $\\bar y$; the remaining {number(100*(1-r2),1)}% is represented by squared residual variation. This is a variation decomposition for the fitted sample, not a success rate and not causal evidence."))
    ex.append("".join(exg));sol.append("".join(sog))

    exg=[group_heading(6,"Slope Tests and Confidence Intervals")];sog=[group_heading(6,"Slope Tests and Confidence Intervals")]
    for i,((title,x,xunit,y,yunit),(n,b,se)) in enumerate(zip(CONTEXTS,INFERENCE_CASES),1):
        x_unit_singular=SINGULAR_UNITS[xunit]
        df=n-2;stat=b/se;p=student_t_two_sided_p(stat,df);crit=student_t_ppf(0.975,df);lo=b-crit*se;hi=b+crit*se;reject=not(lo<=0<=hi)
        exg.append(task(5,6,i,title,f"For $n={n}$ cases, the estimated {x} slope is $b_1={b}$ with $SE(b_1)={se}$. Use the t distribution with $df=n-2={df}$ and the displayed 95% critical value {number(crit,4)}. (a) Test $H_0:\\beta_1=0$ with $t=b_1/SE(b_1)$ and calculate the exact two-sided t-distribution p-value. (b) Construct the 95% interval $b_1\\pm t^*SE$. (c) Explain why the interval and two-sided decision agree and interpret the slope with units."))
        sog.append(task(5,6,i,title,f"The statistic is $t={b}/{se}={number(stat,4)}$ with $df={df}$. The exact two-sided t-distribution p-value is $p=2P(T_{{{df}}}\\geq|{number(stat,4)}|)={number(p,4)}$. The 95% critical value is $t_{{0.975}}({df})={number(crit,4)}$, so the interval is ${b}\\pm{number(crit,4)}({se})=[{number(lo,4)}, {number(hi,4)}]$. Zero {'is outside' if reject else 'is inside'} the interval, so the matching two-sided test {'rejects' if reject else 'fails to reject'} $H_0$. The estimated fitted change is {b} {yunit} for a one-{x_unit_singular} increase in {x}. The interval shows the range of population slopes compatible with this procedure and sample under the linear-model assumptions. The p-value and interval use the same t reference distribution, so their decisions agree."))
    ex.append("".join(exg));sol.append("".join(sog))

    exg=[group_heading(7,"The Simple-Regression Model Test through R-Squared")];sog=[group_heading(7,"The Simple-Regression Model Test through R-Squared")]
    for i,((title,x,xunit,y,yunit),(n,r2,crit)) in enumerate(zip(CONTEXTS,MODEL_CASES),1):
        f=(r2)/(1-r2)*(n-2);reject=f>crit
        exg.append(task(5,7,i,title,f"A simple regression with $n={n}$ has $R^2={r2}$. (a) State the global model null in terms of $\\beta_1$ and, equivalently, population explained variation. (b) Calculate $F=[R^2/1]/[(1-R^2)/(n-2)]$. (c) Compare it with $F_{{0.95}}(1,{n-2})={crit}$ and interpret the decision. (d) Explain why this one-predictor $F$ test matches the two-sided slope test."))
        sog.append(task(5,7,i,title,f"The null is $H_0:\\beta_1=0$, equivalently $H_0:R_{{population}}^2=0$ for this one-predictor linear model. $F=[{r2}/1]/[(1-{r2})/({n}-2)]={number(f,4)}$. Because {number(f,4)} {'exceeds' if reject else 'does not exceed'} {crit}, we {'reject' if reject else 'fail to reject'} the null at 5%. The sample {'provides evidence of a nonzero linear population slope' if reject else 'does not provide sufficiently strong evidence of a nonzero linear population slope'}. With one predictor, $F=t^2$ for the slope test, so the global model and two-sided coefficient tests ask the same question and produce the same decision."))
    ex.append("".join(exg));sol.append("".join(sog))

    exg=[group_heading(8,"Weak Evidence and Careful Interpretation")];sog=[group_heading(8,"Weak Evidence and Careful Interpretation")]
    for i,((title,x,xunit,y,yunit),(n,b,se,tval,p)) in enumerate(zip(CONTEXTS,WEAK_CASES),1):
        x_unit_singular=SINGULAR_UNITS[xunit]
        r2=min((tval*tval)/(tval*tval+n-2),0.99);lo=b-2*se;hi=b+2*se
        exg.append(task(5,8,i,title,f"A simple regression reports $n={n}$, slope $b_1={b}$, $SE={se}$, $t={tval}$, and two-sided $p={p}$. (a) State the 5% decision. (b) Form the approximate 95% interval $b_1\\pm2SE$. (c) Calculate $R^2=t^2/(t^2+n-2)$. (d) Write a careful conclusion that distinguishes the estimated direction, weak statistical evidence, small explained variation, uncertainty, and absence of causal proof."))
        sog.append(task(5,8,i,title,f"Because $p={p}>0.05$, we fail to reject $H_0:\\beta_1=0$. The approximate interval is ${b}\\pm2({se})=[{number(lo,4)}, {number(hi,4)}]$ and contains zero. The fit is $R^2=({number(tval,2)})^2/[({number(tval,2)})^2+{n}-2]={number(r2,4)}$, or {number(100*r2,1)}% of sample variation. The estimated slope is {b} {yunit} per {x_unit_singular}, but the data remain compatible with zero and nearby slopes. The appropriate conclusion is weak or inconclusive linear evidence, not proof of no relationship. Neither the sign nor a low p-value would establish causation without a suitable design."))
    ex.append("".join(exg));sol.append("".join(sog))

    exg=[group_heading(9,"Residual Distribution Checks")];sog=[group_heading(9,"Residual Distribution Checks")]
    for i,((title,x,xunit,y,yunit),(label,counts,diagnosis)) in enumerate(zip(CONTEXTS,RESIDUAL_HISTOGRAMS),1):
        centers=[position-(len(counts)-1)/2 for position in range(len(counts))]
        coordinates=", ".join(f"({number(center,1)}, {count})" for center,count in zip(centers,counts))
        exg.append(task(5,9,i,title,f"A hypothetical residual histogram uses equal-width bins. From left to right, the bin-center and count coordinates are {coordinates}; its initial visual description is '{label}'. (a) Complete the histogram by drawing one bar at every listed center with the listed height. (b) Decide whether approximate residual normality looks plausible or whether skewness, unusual tails, multiple peaks, or an outlier needs attention. (c) Explain which regression quantities rely most directly on this distributional check and why a histogram alone cannot assess linearity or constant variance."))
        plausible=diagnosis=="approximately normal"
        sog.append(task(5,9,i,title,f"A complete coordinate specification for the bars is {coordinates}; each second coordinate is the bar height at the first coordinate. The resulting pattern is {diagnosis}. Approximate residual normality {'looks plausible from this coarse histogram' if plausible else 'is questionable and should be investigated with the original residuals and a normal-quantile plot'}. This check matters chiefly for small-sample t and F reference distributions and their intervals and p-values. The fitted line can still be calculated without perfect normality. A histogram ignores fitted values, so it cannot show whether the residual mean bends with the predictor or whether residual spread changes. Those questions require a residual-versus-fitted plot."))
    ex.append("".join(exg));sol.append("".join(sog))

    exg=[group_heading(10,"Residual-versus-Fitted Patterns")];sog=[group_heading(10,"Residual-versus-Fitted Patterns")]
    for i,((title,x,xunit,y,yunit),(means,spreads,pattern)) in enumerate(zip(CONTEXTS,RESIDUAL_PATTERNS),1):
        bands=[1,2,3,4,5]
        mean_coordinates=", ".join(f"({band}, {number(mean,1)})" for band,mean in zip(bands,means))
        bar_coordinates=", ".join(f"band {band}: [{number(mean-spread,1)}, {number(mean+spread,1)}]" for band,mean,spread in zip(bands,means,spreads))
        if pattern=="random horizontal band":
            original_pattern="an approximately straight center with a similar vertical spread from left to right"
        elif pattern=="curvature":
            original_pattern="a visibly curved center rather than one adequate straight line"
        else:
            original_pattern=f"an approximately straight center whose vertical spread shows {pattern}"
        exg.append(task(5,10,i,title,f"Across five increasing fitted-value bands numbered 1 through 5, the mean residuals are {means} and the residual standard deviations are {spreads}. (a) Before drawing residuals, sketch a plausible original-data scatterplot of {y} against {x} that has {original_pattern}. Label both axes and add the fitted straight line that would be checked. (b) Now plot the residual mean coordinates {mean_coordinates}. At each point, draw a vertical one-standard-deviation bar from mean minus spread to mean plus spread. (c) Compare the original-data and residual views, then identify whether the main residual pattern is a random horizontal band, curvature, increasing spread, or decreasing spread. (d) State which linear-model condition is challenged and one reasonable next diagnostic or modeling step."))
        if pattern=="random horizontal band": message="The residual means stay near zero and the spreads remain similar, which is the expected pattern. No obvious nonlinearity or unequal variance is visible in this grouped summary"
        elif pattern=="curvature": message="The residual means change systematically from positive to negative and back, revealing curvature. The straight-line mean function is inadequate"
        else: message=f"The residual means stay near zero but the spread shows {pattern}. The constant-variance condition is questionable"
        display_pattern=("a random horizontal band" if pattern=="random horizontal band" else "curvature" if pattern=="curvature" else pattern)
        sog.append(task(5,10,i,title,f"(a) In the original-data panel, place {x} on the horizontal axis and {y} on the vertical axis. Draw {original_pattern}, then add the fitted straight line as the reference the residuals evaluate. (b) The completed residual mean coordinates are {mean_coordinates}. The five vertical bar endpoints are {bar_coordinates}. (c) Read the two panels together: distances above and below the fitted line in the original-data panel become positive and negative residuals in the second panel. The grouped residual display shows {display_pattern}. {message}. (d) Inspect the case-level residual-versus-fitted plot rather than relying only on five bands. For curvature, consider whether a transformed predictor or explicitly justified nonlinear term matches the research question. For changing spread, inspect measurement, subgroups, outcome scale, and variance modeling. A clean pattern supports the diagnostic conditions but does not prove them or establish causation."))
    ex.append("".join(exg));sol.append("".join(sog))
    return ex,sol


GROUP_TITLES = {
    "de": (
        "Kleinste-Quadrate-Koeffizienten aus Rohsummen",
        "Von Mittelwerten, Standardabweichungen und Kovarianz zur Geraden",
        "Unstandardisierte und standardisierte Steigungen",
        "Zwei Ausgaben einfacher Regressionen vergleichen",
        "Koeffizienten und erklärte Variation",
        "Tests und Konfidenzintervalle für die Steigung",
        "Der Modelltest der einfachen Regression über R-Quadrat",
        "Schwache Evidenz sorgfältig interpretieren",
        "Verteilung der Residuen prüfen",
        "Muster von Residuen gegen vorhergesagte Werte",
    ),
    "sq": (
        "Koeficientët e katrorëve më të vegjël nga shumat e papërpunuara",
        "Nga mesataret, devijimet standarde dhe kovarianca te vija",
        "Pjerrësitë e pastandardizuara dhe të standardizuara",
        "Krahasimi i dy rezultateve të regresionit të thjeshtë",
        "Koeficientët dhe ndryshueshmëria e shpjeguar",
        "Testet dhe intervalet e besimit për pjerrësinë",
        "Testi i modelit të regresionit të thjeshtë përmes R-katrorit",
        "Interpretimi i kujdesshëm i evidencës së dobët",
        "Kontrolli i shpërndarjes së rezidualeve",
        "Modelet e rezidualeve kundrejt vlerave të përshtatura",
    ),
}


CONTEXTS_LOCALIZED = {
    "de": (
        ("Wöchentliches Üben und statistisches Denken", "wöchentliche Übungszeit", "Stunden", "Punktwert im statistischen Denken", "Punkte", "Stunde"),
        ("Archiverfahrung und Suchzeit", "Monate Archiverfahrung", "Monate", "Suchzeit", "Minuten", "Monat"),
        ("Museumsbesuche und Wissen", "Museumsbesuche in diesem Jahr", "Besuche", "Punktwert im historischen Wissen", "Punkte", "Besuch"),
        ("Lesezeit und Verständnis", "wöchentliche Lesezeit", "Stunden", "Verständnispunktwert", "Punkte", "Stunde"),
        ("Streckenkenntnis und Navigationsfehler", "Punktwert der Streckenkenntnis", "Punkte", "Anzahl Navigationsfehler", "Fehler", "Punkt"),
        ("Workshopteilnahme und Selbstvertrauen", "besuchte Workshopsitzungen", "Sitzungen", "Punktwert des Selbstvertrauens", "Punkte", "Sitzung"),
        ("Benachrichtigungen und Konzentration", "tägliche Anzahl Benachrichtigungen", "Benachrichtigungen", "Konzentrationspunktwert", "Punkte", "Benachrichtigung"),
        ("Suchübung und Genauigkeit", "abgeschlossene Suchübungen", "Übungen", "Punktwert der Suchgenauigkeit", "Punkte", "Übung"),
        ("Reisedistanz und Besuchsdauer", "Reisedistanz", "Kilometer", "Besuchsdauer", "Minuten", "Kilometer"),
        ("Diskussionsbeteiligung und statistisches Denken", "Diskussionsbeiträge", "Beiträge", "Punktwert im statistischen Denken", "Punkte", "Beitrag"),
    ),
    "sq": (
        ("Ushtrimi javor dhe arsyetimi", "orët e ushtrimit javor", "orë", "pikët e arsyetimit", "pikë", "orë"),
        ("Përvoja në arkiv dhe koha e kërkimit", "muajt e përvojës në arkiv", "muaj", "koha e kërkimit", "minuta", "muaj"),
        ("Vizitat në muze dhe njohuritë", "vizitat në muze gjatë këtij viti", "vizita", "pikët e njohurive historike", "pikë", "vizitë"),
        ("Koha e leximit dhe të kuptuarit", "koha javore e leximit", "orë", "pikët e të kuptuarit", "pikë", "orë"),
        ("Njohja e rrugës dhe gabimet e orientimit", "pikët e njohjes së rrugës", "pikë", "numri i gabimeve të orientimit", "gabime", "pikë"),
        ("Pjesëmarrja në seminar dhe vetëbesimi", "seancat e ndjekura të seminarit", "seanca", "pikët e vetëbesimit", "pikë", "seancë"),
        ("Njoftimet dhe përqendrimi", "numri ditor i njoftimeve", "njoftime", "pikët e përqendrimit", "pikë", "njoftim"),
        ("Ushtrimi i kërkimit dhe saktësia", "ushtrimet e përfunduara të kërkimit", "ushtrime", "pikët e saktësisë së kërkimit", "pikë", "ushtrim"),
        ("Distanca e udhëtimit dhe kohëzgjatja e vizitës", "distanca e udhëtimit", "kilometra", "kohëzgjatja e vizitës", "minuta", "kilometër"),
        ("Pjesëmarrja në diskutim dhe arsyetimi", "kontributet në diskutim", "kontribute", "pikët e arsyetimit", "pikë", "kontribut"),
    ),
}


SECOND_LOCALIZED = {
    "de": (("angeleitete Lernsitzungen","Sitzung"),("Abrufsitzungen","Sitzung"),("historische Lesesitzungen","Sitzung"),("annotierte Seiten pro Woche","Seite"),("frühere Streckenversuche","Versuch"),("Sitzungen mit Peer-Feedback","Sitzung"),("geplante Konzentrationsblöcke","Block"),("Monate Archiverfahrung","Monat"),("geplante Stopps","Stopp"),("Vorbereitungszeit","Stunde")),
    "sq": (("seancat e udhëzuara të studimit","seancë"),("seancat e praktikës së rikujtimit","seancë"),("seancat e leximit të historisë","seancë"),("faqet e shënuara në javë","faqe"),("përpjekjet e mëparshme në rrugë","përpjekje"),("seancat me komente nga bashkëmoshatarët","seancë"),("blloqet e planifikuara të përqendrimit","bllok"),("muajt e përvojës në arkiv","muaj"),("ndalesat e planifikuara","ndalesë"),("koha e përgatitjes","orë")),
}


HISTOGRAM_TEXT = {
    "de": {
        "roughly symmetric":"ungefähr symmetrisch", "strong right tail":"starker rechter Verteilungsschwanz", "one extreme upper bin":"eine extreme obere Klasse", "flat shoulders":"flache Schultern", "strong left tail":"starker linker Verteilungsschwanz", "two peaks":"zwei Gipfel", "roughly symmetric with heavy tails":"ungefähr symmetrisch mit schweren Verteilungsschwänzen", "strong center":"starkes Zentrum",
        "approximately normal":"annähernd normal", "right-skewed":"rechtsschief", "an upper outlier or heavy right tail":"ein oberer Ausreisser oder ein schwerer rechter Verteilungsschwanz", "symmetric but flatter than a normal shape":"symmetrisch, aber flacher als eine Normalverteilung", "left-skewed":"linksschief", "bimodal":"bimodal", "symmetric with heavier tails":"symmetrisch mit schwereren Verteilungsschwänzen", "symmetric but more sharply peaked":"symmetrisch, aber stärker zugespitzt",
    },
    "sq": {
        "roughly symmetric":"përafërsisht simetrik", "strong right tail":"bisht i fortë djathtas", "one extreme upper bin":"një klasë e sipërme skajore", "flat shoulders":"shpatulla të sheshta", "strong left tail":"bisht i fortë majtas", "two peaks":"dy kulme", "roughly symmetric with heavy tails":"përafërsisht simetrik me bishta të rëndë", "strong center":"qendër e fortë",
        "approximately normal":"përafërsisht normal", "right-skewed":"i anuar djathtas", "an upper outlier or heavy right tail":"një vlerë skajore e sipërme ose bisht i rëndë djathtas", "symmetric but flatter than a normal shape":"simetrik, por më i sheshtë se trajta normale", "left-skewed":"i anuar majtas", "bimodal":"bimodal", "symmetric with heavier tails":"simetrik me bishta më të rëndë", "symmetric but more sharply peaked":"simetrik, por me kulm më të mprehtë",
    },
}


def render_localized(locale: str) -> tuple[list[str], list[str]]:
    """Render the reviewed de-CH or Albanian adaptation from canonical values."""

    if locale=="en": return render_english()
    if locale not in ("de","sq"): raise ValueError(f"unsupported locale: {locale}")
    contexts=CONTEXTS_LOCALIZED[locale];titles=GROUP_TITLES[locale];ex=[];sol=[]

    exg=[group_heading(1,titles[0])];sog=[group_heading(1,titles[0])]
    for i,((title,x,xunit,y,yunit,xsing),(x_values,y_values,x0)) in enumerate(zip(contexts,RAW_SUM_CASES),1):
        n=len(x_values);sx=sum(x_values);sy=sum(y_values);sx2=sum(v*v for v in x_values);sxy=sum(a*b for a,b in zip(x_values,y_values));xbar=sx/n;ybar=sy/n;sxx=sx2-sx*sx/n;sxyc=sxy-sx*sy/n;b1=sxyc/sxx;b0=ybar-b1*xbar;pred=b0+b1*x0;coordinates=", ".join(f"({a}, {b})" for a,b in zip(x_values,y_values));x_min=min(x_values);x_max=max(x_values);up=b1>0
        if locale=="de":
            zero_scope=(f"Null liegt im beobachteten Bereich [{x_min}, {x_max}]. Deshalb beschreibt der Achsenabschnitt eine durch diese Daten gestützte angepasste Ausgangslage." if x_min<=0<=x_max else f"Null liegt ausserhalb des beobachteten Bereichs [{x_min}, {x_max}]. Der Achsenabschnitt wird mathematisch benötigt, darf aber nicht als beobachtete Ausgangslage behandelt werden.")
            prompt=rf"Ein hypothetischer Datensatz enthält die geordneten Paare $(X,Y)$: {coordinates}. Dabei steht $X$ für «{x}» und $Y$ für «{y}». Die Rechensummen sind $n={n}$, $\sum x={sx}$, $\sum y={sy}$, $\sum x^2={sx2}$ und $\sum xy={sxy}$. (a) Zeichne die Koordinaten, berichte den beobachteten $X$-Bereich und beurteile, ob ein ungefähr geradlinig steigendes oder fallendes Muster plausibel ist und ob ein Punkt sichtbar isoliert liegt. (b) Berechne $\bar x$, $\bar y$, $S_{{xx}}=\sum x^2-(\sum x)^2/n$ und $S_{{xy}}=\sum xy-(\sum x)(\sum y)/n$. (c) Bestimme $b_1=S_{{xy}}/S_{{xx}}$ und $b_0=\bar y-b_1\bar x$ und interpretiere beide Koeffizienten mit Einheiten und passendem Geltungsbereich. (d) Sage $Y$ bei $X={x0}$ {xunit} vorher und bestätige, dass dies eine Vorhersage innerhalb des beobachteten Bereichs ist."
            solution=rf"Das vollständige Streudiagramm verwendet die Koordinaten {coordinates} mit horizontalem Bereich [{x_min}, {x_max}]. Von links nach rechts zeigen die Punkte ein ungefähr geradlinig {'steigendes' if up else 'fallendes'} Muster; keine einzelne Koordinate ist klar von allen benachbarten Punkten getrennt. Die Mittelwerte sind $\bar x={sx}/{n}={number(xbar,4)}$ {xunit} und $\bar y={sy}/{n}={number(ybar,4)}$ {yunit}. Die korrigierten Summen sind $S_{{xx}}={sx2}-{sx}^2/{n}={number(sxx,4)}$ und $S_{{xy}}={sxy}-{sx}({sy})/{n}={number(sxyc,4)}$. Somit ist $b_1={number(sxyc,4)}/{number(sxx,4)}={number(b1,4)}$ {yunit} pro {xsing} und $b_0={number(ybar,4)}-({number(b1,4)})({number(xbar,4)})={number(b0,4)}$ {yunit}. Die Steigung ist der angepasste Ergebnisunterschied von {number(b1,4)} {yunit}, wenn der Prädiktor «{x}» um eine Einheit zunimmt. Der Achsenabschnitt ist das angepasste Ergebnis bei $X=0$. {zero_scope} Die angepasste Gleichung ist $\widehat Y={number(b0,4)}+({number(b1,4)})X$. Weil {x_min} $\leq$ {x0} $\leq$ {x_max}, liegt Interpolation vor. Bei $X={x0}$ gilt $\widehat Y={number(b0,4)}+({number(b1,4)})({x0})={number(pred,4)}$ {yunit}. Dies ist ein geschätzter bedingter Mittelwert und kein garantiertes Ergebnis eines einzelnen Falls."
        else:
            zero_scope=(f"Zeroja është brenda intervalit të vrojtuar [{x_min}, {x_max}], prandaj prerja përshkruan një nivel fillestar të përshtatur që mbështetet nga këto të dhëna." if x_min<=0<=x_max else f"Zeroja është jashtë intervalit të vrojtuar [{x_min}, {x_max}], prandaj prerja nevojitet matematikisht, por nuk duhet trajtuar si nivel fillestar i vrojtuar.")
            prompt=rf"Një grup hipotetik të dhënash përmban këto çifte të renditura $(X,Y)$: {coordinates}. Këtu $X$ përfaqëson «{x}», ndërsa $Y$ përfaqëson «{y}». Përmbledhjet e llogaritjes janë $n={n}$, $\sum x={sx}$, $\sum y={sy}$, $\sum x^2={sx2}$ dhe $\sum xy={sxy}$. (a) Vizato koordinatat, raporto intervalin e vrojtuar të $X$ dhe vlerëso nëse është i besueshëm një model afërsisht i drejtë rritës ose zbritës dhe nëse ndonjë pikë është dukshëm e izoluar. (b) Llogarit $\bar x$, $\bar y$, $S_{{xx}}=\sum x^2-(\sum x)^2/n$ dhe $S_{{xy}}=\sum xy-(\sum x)(\sum y)/n$. (c) Gjej $b_1=S_{{xy}}/S_{{xx}}$ dhe $b_0=\bar y-b_1\bar x$ dhe interpreto të dy koeficientët me njësi dhe shtrirje të përshtatshme. (d) Parashiko $Y$ kur $X={x0}$ {xunit} dhe verifiko se parashikimi është brenda intervalit."
            solution=rf"Diagrami i plotë i shpërndarjes përdor koordinatat {coordinates}, me interval horizontal [{x_min}, {x_max}]. Duke i lexuar pikat nga e majta në të djathtë, shfaqet një model afërsisht i drejtë {'rritës' if up else 'zbritës'} dhe asnjë koordinatë nuk ndahet qartë nga të gjitha pikat fqinje. Mesataret janë $\bar x={sx}/{n}={number(xbar,4)}$ {xunit} dhe $\bar y={sy}/{n}={number(ybar,4)}$ {yunit}. Shumat e korrigjuara janë $S_{{xx}}={sx2}-{sx}^2/{n}={number(sxx,4)}$ dhe $S_{{xy}}={sxy}-{sx}({sy})/{n}={number(sxyc,4)}$. Prandaj $b_1={number(sxyc,4)}/{number(sxx,4)}={number(b1,4)}$ {yunit} për {xsing} dhe $b_0={number(ybar,4)}-({number(b1,4)})({number(xbar,4)})={number(b0,4)}$ {yunit}. Pjerrësia është dallimi i përshtatur prej {number(b1,4)} {yunit} kur parashikuesi «{x}» rritet me një {xsing}. Prerja është rezultati i përshtatur në $X=0$. {zero_scope} Ekuacioni i përshtatur është $\widehat Y={number(b0,4)}+({number(b1,4)})X$. Meqë {x_min} $\leq$ {x0} $\leq$ {x_max}, kërkesa është interpolim. Në $X={x0}$, $\widehat Y={number(b0,4)}+({number(b1,4)})({x0})={number(pred,4)}$ {yunit}. Kjo është mesatare e kushtëzuar e vlerësuar, jo rezultat i garantuar për një rast."
        exg.append(task(5,1,i,title,prompt));sog.append(task(5,1,i,title,solution))
    ex.append("".join(exg));sol.append("".join(sog))

    exg=[group_heading(2,titles[1])];sog=[group_heading(2,titles[1])]
    for i,((title,x,xunit,y,yunit,xsing),(mx,my,sx,sy,cov,x0)) in enumerate(zip(contexts,SUMMARY_CASES),1):
        r=cov/(sx*sy);b1=cov/(sx*sx);b0=my-b1*mx;pred=b0+b1*x0
        if locale=="de":
            prompt=rf"Die zusammenfassenden Kennwerte sind $\bar x={mx}$, $\bar y={my}$, $s_x={sx}$, $s_y={sy}$ und die Stichprobenkovarianz $s_{{xy}}={cov}$. (a) Berechne Pearsons $r=s_{{xy}}/(s_xs_y)$. (b) Bestimme Regressionssteigung $b_1=s_{{xy}}/s_x^2$ und Achsenabschnitt. (c) Berechne die Vorhersage für die Ergebnisvariable «{y}», wenn die Prädiktorvariable «{x}» den Wert {x0} {xunit} annimmt. (d) Erkläre, wie Korrelation und Steigung dieselbe gemeinsame Variation verwenden, aber verschiedene Fragen beantworten."
            solution=rf"Die Korrelation ist $r={cov}/({sx}\times{sy})={number(r,4)}$. Die Steigung ist $b_1={cov}/{sx}^2={number(b1,4)}$ {yunit} pro Einheit von $X$ und $b_0={my}-({number(b1,4)})({mx})={number(b0,4)}$ {yunit}. Bei $X={x0}$ gilt $\widehat Y={number(b0,4)}+({number(b1,4)})({x0})={number(pred,4)}$ {yunit}. Korrelation ist einheitsfrei und symmetrisch zwischen $X$ und $Y$. Die Regressionssteigung bezeichnet $Y$ als Ergebnis, behält die Messeinheiten und beschreibt die angepasste Ergebnisänderung pro Prädiktoreinheit. Beide beginnen mit derselben vorzeichenbehafteten Kovariation."
        else:
            prompt=rf"Treguesit përmbledhës janë $\bar x={mx}$, $\bar y={my}$, $s_x={sx}$, $s_y={sy}$ dhe kovarianca e kampionit $s_{{xy}}={cov}$. (a) Llogarit $r=s_{{xy}}/(s_xs_y)$ të Pearson-it. (b) Gjej pjerrësinë e regresionit $b_1=s_{{xy}}/s_x^2$ dhe prerjen. (c) Llogarit parashikimin për ndryshoren e rezultatit «{y}» kur ndryshorja parashikuese «{x}» ka vlerën {x0} {xunit}. (d) Shpjego si e përdorin korrelacioni dhe pjerrësia të njëjtën ndryshueshmëri të përbashkët, por u përgjigjen pyetjeve të ndryshme."
            solution=rf"Korrelacioni është $r={cov}/({sx}\times{sy})={number(r,4)}$. Pjerrësia është $b_1={cov}/{sx}^2={number(b1,4)}$ {yunit} për një njësi të $X$, dhe $b_0={my}-({number(b1,4)})({mx})={number(b0,4)}$ {yunit}. Në $X={x0}$, $\widehat Y={number(b0,4)}+({number(b1,4)})({x0})={number(pred,4)}$ {yunit}. Korrelacioni nuk ka njësi dhe është simetrik mes $X$ dhe $Y$. Pjerrësia e regresionit e cakton $Y$ si rezultat, i ruan njësitë e matjes dhe përshkruan ndryshimin e përshtatur të rezultatit për njësi të parashikuesit. Të dy fillojnë nga e njëjta bashkëndryshueshmëri me shenjë."
        exg.append(task(5,2,i,title,prompt));sog.append(task(5,2,i,title,solution))
    ex.append("".join(exg));sol.append("".join(sog))

    exg=[group_heading(3,titles[2])];sog=[group_heading(3,titles[2])]
    for i,((title,x,xunit,y,yunit,xsing),(b0,b1,sx,sy,x0)) in enumerate(zip(contexts,COEFFICIENT_CASES),1):
        beta=b1*sx/sy;pred=b0+b1*x0
        if locale=="de":
            prompt=rf"Ein angepasstes Modell lautet $\widehat Y={b0}+({b1})X$, mit $s_x={sx}$ {xunit} und $s_y={sy}$ {yunit}. (a) Interpretiere die unstandardisierte Steigung in Originaleinheiten und berechne den angepassten Wert bei $X={x0}$. (b) Berechne die standardisierte Steigung $\beta^*=b_1s_x/s_y$. (c) Erkläre, was eine Prädiktorstandardabweichung in der standardisierten Interpretation bedeutet und weshalb die zwei Steigungszahlen nicht ohne ihre Skalen verglichen werden dürfen."
            solution=rf"Die unstandardisierte Steigung {b1} bedeutet, dass ein Unterschied von einer Einheit im Prädiktor «{x}» mit einem angepassten Unterschied von {b1} {yunit} im Ergebnis «{y}» einhergeht. Die Vorhersage ist $\widehat Y={b0}+({b1})({x0})={number(pred,4)}$ {yunit}. Die standardisierte Steigung ist $\beta^*=({b1})({sx})/{sy}={number(beta,4)}$. Ein Unterschied von einer Standardabweichung im Prädiktor, also {sx} {xunit}, geht somit mit einem angepassten Unterschied von {number(beta,4)} Ergebnisstandardabweichungen einher. Die unstandardisierte Zahl beantwortet eine Frage in Originaleinheiten, die standardisierte Zahl eine Frage in Standardabweichungen."
        else:
            prompt=rf"Një model i përshtatur është $\widehat Y={b0}+({b1})X$, me $s_x={sx}$ {xunit} dhe $s_y={sy}$ {yunit}. (a) Interpreto pjerrësinë e pastandardizuar në njësitë fillestare dhe llogarit vlerën e përshtatur në $X={x0}$. (b) Llogarit pjerrësinë e standardizuar $\beta^*=b_1s_x/s_y$. (c) Shpjego çfarë do të thotë një devijim standard i parashikuesit në interpretimin e standardizuar dhe pse dy numrat e pjerrësisë nuk duhet të krahasohen pa shkallët e tyre."
            solution=rf"Pjerrësia e pastandardizuar {b1} do të thotë se një dallim prej një njësie në parashikuesin «{x}» shoqërohet me dallim të përshtatur prej {b1} {yunit} në rezultatin «{y}». Parashikimi është $\widehat Y={b0}+({b1})({x0})={number(pred,4)}$ {yunit}. Pjerrësia e standardizuar është $\beta^*=({b1})({sx})/{sy}={number(beta,4)}$. Kështu, një dallim prej një devijimi standard në parashikues, i barabartë me {sx} {xunit}, shoqërohet me dallim të përshtatur prej {number(beta,4)} devijimesh standarde të rezultatit. Numri i pastandardizuar i përgjigjet pyetjes në njësitë fillestare; numri i standardizuar i përgjigjet pyetjes në devijime standarde."
        exg.append(task(5,3,i,title,prompt));sog.append(task(5,3,i,title,solution))
    ex.append("".join(exg));sol.append("".join(sog))

    exg=[group_heading(4,titles[3])];sog=[group_heading(4,titles[3])]
    for i,((title,x,xunit,y,yunit,xsing),(second_x,secondsing),(b0a,b1a,se1a,beta_a,b0b,b1b,se1b,beta_b)) in enumerate(zip(contexts,SECOND_LOCALIZED[locale],OUTPUT_COMPARISONS),1):
        t_a=b1a/se1a;t_b=b1b/se1b;stronger=x if abs(beta_a)>abs(beta_b) else second_x
        if locale=="de":
            prompt=rf"Zwei getrennte einfache Regressionen verwenden «{y}» als Ergebnis. Ausgabe A mit dem Prädiktor «{x}» berichtet: Achsenabschnitt {b0a}; Prädiktorkoeffizient {b1a}, $SE={se1a}$, $t={number(t_a,2)}$, standardisierte Steigung $\beta^*={beta_a}$. Ausgabe B mit dem Prädiktor «{second_x}» berichtet: Achsenabschnitt {b0b}; Prädiktorkoeffizient {b1b}, $SE={se1b}$, $t={number(t_b,2)}$, standardisierte Steigung $\beta^*={beta_b}$. (a) Finde die zwei Prädiktorkoeffizienten und unterscheide sie von den Achsenabschnitten. (b) Interpretiere jede unstandardisierte Steigung in Originaleinheiten. (c) Vergleiche Richtungen und Beträge der standardisierten Steigungen. (d) Erkläre, weshalb unstandardisierte Steigungen bei verschiedenen Prädiktoreinheiten nicht direkt nach Stärke geordnet werden dürfen und weshalb keines der getrennten Modelle Kausalität belegt."
            solution=rf"Die Prädiktorkoeffizienten sind {b1a} in Ausgabe A und {b1b} in Ausgabe B; {b0a} und {b0b} sind Achsenabschnitte. Wenn der Prädiktor «{x}» um eine Einheit zunimmt, {'steigt' if b1a>0 else 'sinkt'} das angepasste Ergebnis «{y}» um {number(abs(b1a),2)} {yunit}. Wenn der Prädiktor «{second_x}» um eine Einheit zunimmt, {'steigt' if b1b>0 else 'sinkt'} das angepasste Ergebnis um {number(abs(b1b),2)} {yunit}. Die standardisierten Steigungen sind {beta_a} und {beta_b}. Sie geben angepasste Änderungen in Ergebnisstandardabweichungen pro Prädiktorstandardabweichung an; deshalb sind ihre Beträge vergleichbar: Der Prädiktor «{stronger}» hat in den zwei getrennten Modellen den grösseren absoluten standardisierten Zusammenhang. Bei einfacher Regression mit Achsenabschnitt entspricht jede standardisierte Steigung zudem der Pearson-Korrelation zwischen Prädiktor und Ergebnis. Die rohen Steigungen dürfen nicht als Stärken geordnet werden, weil die Einheit «{xsing}» beim Prädiktor «{x}» nicht dieselbe Skala wie die Einheit «{secondsing}» beim Prädiktor «{second_x}» hat. Es sind zwei bivariate Zusammenhänge; keiner hält den jeweils anderen Prädiktor konstant oder belegt einen kausalen Effekt."
        else:
            prompt=rf"Dy regresione të thjeshta të veçanta përdorin «{y}» si rezultat. Rezultati A, me parashikuesin «{x}», raporton: vlerësimi i prerjes {b0a}; vlerësimi i parashikuesit {b1a}, $SE={se1a}$, $t={number(t_a,2)}$, pjerrësia e standardizuar $\beta^*={beta_a}$. Rezultati B, me parashikuesin «{second_x}», raporton: vlerësimi i prerjes {b0b}; vlerësimi i parashikuesit {b1b}, $SE={se1b}$, $t={number(t_b,2)}$, pjerrësia e standardizuar $\beta^*={beta_b}$. (a) Gjej dy koeficientët e parashikuesve dhe dalloji nga prerjet. (b) Interpreto secilën pjerrësi të pastandardizuar me njësitë fillestare. (c) Krahaso drejtimet dhe madhësitë absolute të pjerrësive të standardizuara. (d) Shpjego pse pjerrësitë e pastandardizuara nuk duhet të renditen drejtpërdrejt kur njësitë e parashikuesve ndryshojnë dhe pse asnjëri model i veçantë nuk provon shkakësi."
            solution=rf"Vlerësimet e parashikuesve janë {b1a} në Rezultatin A dhe {b1b} në Rezultatin B; {b0a} dhe {b0b} janë prerje. Kur parashikuesi «{x}» rritet me një {xsing}, rezultati i përshtatur «{y}» {'rritet' if b1a>0 else 'ulet'} me {number(abs(b1a),2)} {yunit}. Kur parashikuesi «{second_x}» rritet me një {secondsing}, rezultati i përshtatur {'rritet' if b1b>0 else 'ulet'} me {number(abs(b1b),2)} {yunit}. Pjerrësitë e standardizuara janë {beta_a} dhe {beta_b}. Ato shprehin ndryshime të përshtatura në devijime standarde të rezultatit për një devijim standard të parashikuesit, ndaj mund të krahasohen madhësitë absolute: parashikuesi «{stronger}» ka lidhjen absolute të standardizuar më të madhe në këto dy modele të veçanta. Në regresionin e thjeshtë me prerje, secila pjerrësi e standardizuar është edhe korrelacioni i Pearson-it mes atij parashikuesi dhe rezultatit. Pjerrësitë e papërpunuara nuk mund të renditen sipas forcës, sepse një {xsing} te parashikuesi «{x}» nuk ka të njëjtën shkallë si një {secondsing} te parashikuesi «{second_x}». Këto janë dy lidhje bivariate; asnjëra nuk e mban parashikuesin tjetër konstant dhe nuk vendos efekt shkakor."
        exg.append(task(5,4,i,title,prompt));sog.append(task(5,4,i,title,solution))
    ex.append("".join(exg));sol.append("".join(sog))

    exg=[group_heading(5,titles[4])];sog=[group_heading(5,titles[4])]
    for i,((title,x,xunit,y,yunit,xsing),(b0,sxy,sxx,sst,x0)) in enumerate(zip(contexts,FIT_CASES),1):
        b1=sxy/sxx;ssr=sxy*sxy/sxx;sse=sst-ssr;r2=ssr/sst;pred=b0+b1*x0
        if locale=="de":
            prompt=rf"Eine zentrierte Berechnung ergibt $S_{{xy}}={sxy}$, $S_{{xx}}={sxx}$, Gesamtquadratsumme $SST={sst}$, Fehlerquadratsumme $SSE={number(sse,4)}$ und Achsenabschnitt $b_0={b0}$. (a) Berechne $b_1$. (b) Bestimme $SSR=SST-SSE$ und $R^2=SSR/SST$. (c) Überprüfe $SSR=b_1S_{{xy}}$, berechne den angepassten Wert bei $X={x0}$ und interpretiere $R^2$ als durch die angepasste Gerade erklärte Stichprobenvariation, nicht als Anteil der Personen mit richtig vorhergesagtem Ergebnis."
            solution=rf"Die Steigung ist $b_1=S_{{xy}}/S_{{xx}}={sxy}/{sxx}={number(b1,4)}$. Die erklärte Variation ist $SSR={sst}-{number(sse,4)}={number(ssr,4)}$; dies entspricht auch $b_1S_{{xy}}={number(b1,4)}({sxy})={number(ssr,4)}$. Somit ist $R^2={number(ssr,4)}/{sst}={number(r2,4)}$. Der angepasste Wert lautet $\widehat Y={b0}+({number(b1,4)})({x0})={number(pred,4)}$. Das Modell erklärt {number(100*r2,1)}% der gesamten quadrierten Stichprobenvariation um $\bar y$; die verbleibenden {number(100*(1-r2),1)}% werden durch quadrierte Residualvariation dargestellt. Dies ist eine Variationszerlegung für die angepasste Stichprobe, keine Erfolgsrate und keine kausale Evidenz."
        else:
            prompt=rf"Një llogaritje e qendërzuar jep $S_{{xy}}={sxy}$, $S_{{xx}}={sxx}$, shumën totale të katrorëve $SST={sst}$, shumën e katrorëve të gabimit $SSE={number(sse,4)}$ dhe prerjen $b_0={b0}$. (a) Llogarit $b_1$. (b) Gjej $SSR=SST-SSE$ dhe $R^2=SSR/SST$. (c) Verifiko $SSR=b_1S_{{xy}}$, llogarit vlerën e përshtatur në $X={x0}$ dhe interpreto $R^2$ si ndryshueshmëri të kampionit të shpjeguar nga vija e përshtatur, jo si përqindje njerëzish rezultatet e të cilëve u parashikuan saktë."
            solution=rf"Pjerrësia është $b_1=S_{{xy}}/S_{{xx}}={sxy}/{sxx}={number(b1,4)}$. Ndryshueshmëria e shpjeguar është $SSR={sst}-{number(sse,4)}={number(ssr,4)}$, që është gjithashtu $b_1S_{{xy}}={number(b1,4)}({sxy})={number(ssr,4)}$. Prandaj $R^2={number(ssr,4)}/{sst}={number(r2,4)}$. Vlera e përshtatur është $\widehat Y={b0}+({number(b1,4)})({x0})={number(pred,4)}$. Modeli shpjegon {number(100*r2,1)}% të ndryshueshmërisë totale në katror të kampionit rreth $\bar y$; {number(100*(1-r2),1)}% e mbetur paraqitet nga ndryshueshmëria e rezidualeve në katror. Kjo është ndarje e ndryshueshmërisë për kampionin e përshtatur, jo normë suksesi dhe jo evidencë shkakore."
        exg.append(task(5,5,i,title,prompt));sog.append(task(5,5,i,title,solution))
    ex.append("".join(exg));sol.append("".join(sog))

    exg=[group_heading(6,titles[5])];sog=[group_heading(6,titles[5])]
    for i,((title,x,xunit,y,yunit,xsing),(n,b,se)) in enumerate(zip(contexts,INFERENCE_CASES),1):
        df=n-2;stat=b/se;p=student_t_two_sided_p(stat,df);crit=student_t_ppf(0.975,df);lo=b-crit*se;hi=b+crit*se;reject=not(lo<=0<=hi)
        if locale=="de":
            prompt=rf"Für $n={n}$ Fälle ist die geschätzte Steigung für den Prädiktor «{x}» $b_1={b}$ mit $SE(b_1)={se}$. Verwende die t-Verteilung mit $df=n-2={df}$ und dem angegebenen kritischen 95%-Wert {number(crit,4)}. (a) Teste $H_0:\beta_1=0$ mit $t=b_1/SE(b_1)$ und berechne den exakten zweiseitigen p-Wert der t-Verteilung. (b) Konstruiere das 95%-Intervall $b_1\pm t^*SE$. (c) Erkläre die Übereinstimmung von Intervall und zweiseitiger Entscheidung und interpretiere die Steigung mit Einheiten."
            solution=rf"Die Statistik ist $t={b}/{se}={number(stat,4)}$ mit $df={df}$. Der exakte zweiseitige p-Wert der t-Verteilung ist $p=2P(T_{{{df}}}\geq|{number(stat,4)}|)={number(p,4)}$. Der kritische 95%-Wert ist $t_{{0.975}}({df})={number(crit,4)}$; das Intervall lautet ${b}\pm{number(crit,4)}({se})=[{number(lo,4)}, {number(hi,4)}]$. Null liegt {'ausserhalb' if reject else 'innerhalb'} des Intervalls, weshalb der passende zweiseitige Test $H_0$ {'ablehnt' if reject else 'nicht ablehnt'}. Die geschätzte angepasste Änderung beträgt {b} {yunit}, wenn der Prädiktor «{x}» um eine Einheit zunimmt. Das Intervall zeigt unter den linearen Modellannahmen den Bereich von Populationssteigungen, die mit diesem Verfahren und der Stichprobe vereinbar sind. p-Wert und Intervall verwenden dieselbe t-Referenzverteilung und stimmen deshalb in der Entscheidung überein."
        else:
            prompt=rf"Për $n={n}$ raste, pjerrësia e vlerësuar për parashikuesin «{x}» është $b_1={b}$ me $SE(b_1)={se}$. Përdor shpërndarjen t me $df=n-2={df}$ dhe vlerën kritike 95% të paraqitur {number(crit,4)}. (a) Testo $H_0:\beta_1=0$ me $t=b_1/SE(b_1)$ dhe llogarit vlerën e saktë p dyanëshe nga shpërndarja t. (b) Ndërto intervalin 95% $b_1\pm t^*SE$. (c) Shpjego pse intervali dhe vendimi dyanësh pajtohen dhe interpreto pjerrësinë me njësi."
            solution=rf"Statistika është $t={b}/{se}={number(stat,4)}$ me $df={df}$. Vlera e saktë p dyanëshe nga shpërndarja t është $p=2P(T_{{{df}}}\geq|{number(stat,4)}|)={number(p,4)}$. Vlera kritike 95% është $t_{{0.975}}({df})={number(crit,4)}$, prandaj intervali është ${b}\pm{number(crit,4)}({se})=[{number(lo,4)}, {number(hi,4)}]$. Zeroja është {'jashtë' if reject else 'brenda'} intervalit, ndaj testi përkatës dyanësh {'e refuzon' if reject else 'nuk e refuzon'} $H_0$. Ndryshimi i përshtatur i vlerësuar është {b} {yunit} kur parashikuesi «{x}» rritet me një {xsing}. Intervali tregon gamën e pjerrësive të popullatës që përputhen me këtë procedurë dhe kampion nën supozimet e modelit linear. Vlera p dhe intervali përdorin të njëjtën shpërndarje t referuese, ndaj vendimet e tyre pajtohen."
        exg.append(task(5,6,i,title,prompt));sog.append(task(5,6,i,title,solution))
    ex.append("".join(exg));sol.append("".join(sog))

    exg=[group_heading(7,titles[6])];sog=[group_heading(7,titles[6])]
    for i,((title,x,xunit,y,yunit,xsing),(n,r2,crit)) in enumerate(zip(contexts,MODEL_CASES),1):
        f=r2/(1-r2)*(n-2);reject=f>crit
        if locale=="de":
            prompt=rf"Eine einfache Regression mit $n={n}$ hat $R^2={r2}$. (a) Formuliere die globale Modellnullhypothese anhand von $\beta_1$ und gleichbedeutend anhand der erklärten Populationsvariation. (b) Berechne $F=[R^2/1]/[(1-R^2)/(n-2)]$. (c) Vergleiche mit $F_{{0.95}}(1,{n-2})={crit}$ und interpretiere die Entscheidung. (d) Erkläre, weshalb dieser $F$-Test mit einem Prädiktor dem zweiseitigen Steigungstest entspricht."
            solution=rf"Die Nullhypothese ist $H_0:\beta_1=0$, gleichbedeutend mit $H_0:R_{{population}}^2=0$ für dieses lineare Modell mit einem Prädiktor. $F=[{r2}/1]/[(1-{r2})/({n}-2)]={number(f,4)}$. Da {number(f,4)} den Wert {crit} {'überschreitet' if reject else 'nicht überschreitet'}, {'lehnen wir' if reject else 'lehnen wir'} die Nullhypothese bei 5% {'ab' if reject else 'nicht ab'}. Die Stichprobe {'liefert Evidenz für eine von null verschiedene lineare Populationssteigung' if reject else 'liefert keine ausreichend starke Evidenz für eine von null verschiedene lineare Populationssteigung'}. Bei einem Prädiktor ist $F=t^2$ für den Steigungstest. Deshalb stellen globaler Modelltest und zweiseitiger Koeffiziententest dieselbe Frage und ergeben dieselbe Entscheidung."
        else:
            prompt=rf"Një regresion i thjeshtë me $n={n}$ ka $R^2={r2}$. (a) Shkruaj hipotezën zero globale të modelit përmes $\beta_1$ dhe, në mënyrë të barasvlershme, përmes ndryshueshmërisë së shpjeguar në popullatë. (b) Llogarit $F=[R^2/1]/[(1-R^2)/(n-2)]$. (c) Krahasoje me $F_{{0.95}}(1,{n-2})={crit}$ dhe interpreto vendimin. (d) Shpjego pse ky test $F$ me një parashikues përputhet me testin dyanësh të pjerrësisë."
            solution=rf"Hipoteza zero është $H_0:\beta_1=0$, në mënyrë të barasvlershme $H_0:R_{{population}}^2=0$ për këtë model linear me një parashikues. $F=[{r2}/1]/[(1-{r2})/({n}-2)]={number(f,4)}$. Meqë {number(f,4)} {'e tejkalon' if reject else 'nuk e tejkalon'} {crit}, {'e refuzojmë' if reject else 'nuk e refuzojmë'} hipotezën zero në 5%. Kampioni {'jep evidencë për një pjerrësi lineare të popullatës të ndryshme nga zero' if reject else 'nuk jep evidencë mjaftueshëm të fortë për një pjerrësi lineare të popullatës të ndryshme nga zero'}. Me një parashikues, $F=t^2$ për testin e pjerrësisë, ndaj testi global i modelit dhe testi dyanësh i koeficientit bëjnë të njëjtën pyetje dhe japin të njëjtin vendim."
        exg.append(task(5,7,i,title,prompt));sog.append(task(5,7,i,title,solution))
    ex.append("".join(exg));sol.append("".join(sog))

    exg=[group_heading(8,titles[7])];sog=[group_heading(8,titles[7])]
    for i,((title,x,xunit,y,yunit,xsing),(n,b,se,tval,p)) in enumerate(zip(contexts,WEAK_CASES),1):
        r2=min((tval*tval)/(tval*tval+n-2),0.99);lo=b-2*se;hi=b+2*se
        if locale=="de":
            prompt=rf"Eine einfache Regression berichtet $n={n}$, Steigung $b_1={b}$, $SE={se}$, $t={tval}$ und zweiseitigen Wert $p={p}$. (a) Formuliere die 5%-Entscheidung. (b) Bilde das angenäherte 95%-Intervall $b_1\pm2SE$. (c) Berechne $R^2=t^2/(t^2+n-2)$. (d) Schreibe einen sorgfältigen Schluss, der geschätzte Richtung, schwache statistische Evidenz, geringe erklärte Variation, Unsicherheit und fehlenden Kausalitätsnachweis unterscheidet."
            solution=rf"Weil $p={p}>0.05$, lehnen wir $H_0:\beta_1=0$ nicht ab. Das angenäherte Intervall ist ${b}\pm2({se})=[{number(lo,4)}, {number(hi,4)}]$ und enthält null. Die Anpassung ist $R^2=({number(tval,2)})^2/[({number(tval,2)})^2+{n}-2]={number(r2,4)}$, also {number(100*r2,1)}% der Stichprobenvariation. Die geschätzte Steigung beträgt {b} {yunit} pro {xsing}; die Daten bleiben jedoch mit null und nahe gelegenen Steigungen vereinbar. Der passende Schluss lautet schwache oder nicht eindeutige lineare Evidenz und nicht Beweis für fehlenden Zusammenhang. Weder das Vorzeichen noch ein kleiner p-Wert würde ohne geeignetes Design Kausalität belegen."
        else:
            prompt=rf"Një regresion i thjeshtë raporton $n={n}$, pjerrësinë $b_1={b}$, $SE={se}$, $t={tval}$ dhe vlerën dyanëshe $p={p}$. (a) Jep vendimin në 5%. (b) Formo intervalin e përafërt 95% $b_1\pm2SE$. (c) Llogarit $R^2=t^2/(t^2+n-2)$. (d) Shkruaj përfundim të kujdesshëm që dallon drejtimin e vlerësuar, evidencën e dobët statistikore, ndryshueshmërinë e vogël të shpjeguar, pasigurinë dhe mungesën e provës shkakore."
            solution=rf"Meqë $p={p}>0.05$, nuk e refuzojmë $H_0:\beta_1=0$. Intervali i përafërt është ${b}\pm2({se})=[{number(lo,4)}, {number(hi,4)}]$ dhe përmban zeron. Përshtatja është $R^2=({number(tval,2)})^2/[({number(tval,2)})^2+{n}-2]={number(r2,4)}$, ose {number(100*r2,1)}% e ndryshueshmërisë së kampionit. Pjerrësia e vlerësuar është {b} {yunit} për {xsing}, por të dhënat mbeten të përputhshme me zeron dhe pjerrësi të afërta. Përfundimi i duhur është evidencë lineare e dobët ose jo përfundimtare, jo provë e mungesës së lidhjes. As shenja dhe as një vlerë e vogël p nuk do të vendosnin shkakësi pa dizajn të përshtatshëm."
        exg.append(task(5,8,i,title,prompt));sog.append(task(5,8,i,title,solution))
    ex.append("".join(exg));sol.append("".join(sog))

    exg=[group_heading(9,titles[8])];sog=[group_heading(9,titles[8])]
    for i,((title,x,xunit,y,yunit,xsing),(label,counts,diagnosis)) in enumerate(zip(contexts,RESIDUAL_HISTOGRAMS),1):
        centers=[position-(len(counts)-1)/2 for position in range(len(counts))];coordinates=", ".join(f"({number(center,1)}, {count})" for center,count in zip(centers,counts));plausible=diagnosis=="approximately normal";lt=HISTOGRAM_TEXT[locale][label];dt=HISTOGRAM_TEXT[locale][diagnosis]
        if locale=="de":
            prompt=rf"Ein hypothetisches Residuenhistogramm verwendet Klassen gleicher Breite. Von links nach rechts lauten die Koordinaten aus Klassenmitte und Häufigkeit {coordinates}; die erste visuelle Beschreibung ist «{lt}». (a) Vervollständige das Histogramm, indem du an jeder genannten Mitte einen Balken mit der genannten Höhe zeichnest. (b) Entscheide, ob annähernde Normalität der Residuen plausibel ist oder ob Schiefe, ungewöhnliche Verteilungsschwänze, mehrere Gipfel oder ein Ausreisser untersucht werden müssen. (c) Erkläre, welche Regressionsgrössen am direktesten auf dieser Verteilungsprüfung beruhen und weshalb ein Histogramm allein Linearität oder konstante Varianz nicht beurteilen kann."
            solution=rf"Die vollständige Koordinatenangabe der Balken lautet {coordinates}; jeweils die zweite Koordinate ist die Balkenhöhe an der ersten. Das entstehende Muster ist {dt}. Annähernde Normalität der Residuen {'erscheint anhand dieses groben Histogramms plausibel' if plausible else 'ist fraglich und sollte anhand der ursprünglichen Residuen und eines Normalquantildiagramms untersucht werden'}. Diese Prüfung ist vor allem für die t- und F-Referenzverteilungen bei kleinen Stichproben sowie ihre Intervalle und p-Werte wichtig. Die angepasste Gerade lässt sich auch ohne perfekte Normalität berechnen. Ein Histogramm ignoriert die angepassten Werte und zeigt deshalb weder eine Krümmung des mittleren Residuums mit dem Prädiktor noch wechselnde Residuenstreuung. Dafür braucht es ein Diagramm der Residuen gegen die angepassten Werte."
        else:
            prompt=rf"Një histogram hipotetik i rezidualeve përdor klasa me gjerësi të barabartë. Nga e majta në të djathtë, koordinatat e qendrës së klasës dhe numërimit janë {coordinates}; përshkrimi fillestar pamor është «{lt}». (a) Plotëso histogramin duke vizatuar një shtyllë në çdo qendër të dhënë me lartësinë përkatëse. (b) Vendos nëse normaliteti i përafërt i rezidualeve duket i besueshëm ose nëse duhet vëmendje për anueshmëri, bishta të pazakontë, disa kulme apo vlerë skajore. (c) Shpjego cilat madhësi të regresionit mbështeten më drejtpërdrejt në këtë kontroll të shpërndarjes dhe pse vetëm histogrami nuk mund të vlerësojë linearitetin ose variancën konstante."
            solution=rf"Përcaktimi i plotë i koordinatave të shtyllave është {coordinates}; koordinata e dytë është lartësia e shtyllës në koordinatën e parë. Modeli që rezulton është {dt}. Normaliteti i përafërt i rezidualeve {'duket i besueshëm nga ky histogram i përgjithshëm' if plausible else 'është i dyshimtë dhe duhet shqyrtuar me rezidualet fillestare dhe diagram normal të kuantileve'}. Ky kontroll ka rëndësi kryesisht për shpërndarjet referuese t dhe F në kampione të vogla, si edhe për intervalet dhe vlerat e tyre p. Vija e përshtatur mund të llogaritet edhe pa normalitet të përsosur. Histogrami i shpërfill vlerat e përshtatura, ndaj nuk mund të tregojë nëse mesatarja e rezidualeve lakohet me parashikuesin ose nëse ndryshon shpërndarja e rezidualeve. Këto pyetje kërkojnë diagramin e rezidualeve kundrejt vlerave të përshtatura."
        exg.append(task(5,9,i,title,prompt));sog.append(task(5,9,i,title,solution))
    ex.append("".join(exg));sol.append("".join(sog))

    exg=[group_heading(10,titles[9])];sog=[group_heading(10,titles[9])]
    for i,((title,x,xunit,y,yunit,xsing),(means,spreads,pattern)) in enumerate(zip(contexts,RESIDUAL_PATTERNS),1):
        bands=[1,2,3,4,5];mean_coordinates=", ".join(f"({band}, {number(mean,1)})" for band,mean in zip(bands,means));bar_coordinates=", ".join(f"{'Band' if locale=='de' else 'brezi'} {band}: [{number(mean-spread,1)}, {number(mean+spread,1)}]" for band,mean,spread in zip(bands,means,spreads))
        if locale=="de":
            display={"random horizontal band":"ein zufälliges horizontales Band","curvature":"Krümmung","increasing spread":"zunehmende Streuung","decreasing spread":"abnehmende Streuung"}[pattern]
            if pattern=="random horizontal band": message="Die mittleren Residuen bleiben nahe null und die Streuungen ähnlich; das ist das erwartete Muster. In dieser gruppierten Zusammenfassung ist keine deutliche Nichtlinearität oder ungleiche Varianz sichtbar"
            elif pattern=="curvature": message="Die mittleren Residuen wechseln systematisch von positiv zu negativ und zurück; dies zeigt Krümmung. Die geradlinige Mittelwertfunktion ist unzureichend"
            else: message=f"Die mittleren Residuen bleiben nahe null, aber die Streuung zeigt {display}. Die Bedingung konstanter Varianz ist fraglich"
            prompt=rf"Über fünf zunehmende Bänder angepasster Werte, nummeriert von 1 bis 5, sind die mittleren Residuen {means} und die Residuenstandardabweichungen {spreads}. (a) Zeichne die mittleren Koordinaten {mean_coordinates}. Zeichne an jedem Punkt einen vertikalen Balken von Mittelwert minus einer Standardabweichung bis Mittelwert plus einer Standardabweichung. (b) Bestimme, ob das Hauptmuster ein zufälliges horizontales Band, Krümmung, zunehmende Streuung oder abnehmende Streuung ist. (c) Nenne die betroffene Bedingung des linearen Modells und einen sinnvollen nächsten Diagnose- oder Modellierungsschritt."
            solution=rf"Die vollständigen mittleren Koordinaten sind {mean_coordinates}. Die Endpunkte der fünf vertikalen Balken sind {bar_coordinates}. Zusammen zeigt die gruppierte Darstellung {display}. {message}. Prüfe das Diagramm der einzelnen Residuen gegen die angepassten Werte, statt dich nur auf fünf Bänder zu verlassen. Bei Krümmung ist zu prüfen, ob ein transformierter Prädiktor oder ein ausdrücklich begründeter nichtlinearer Term zur Forschungsfrage passt. Bei wechselnder Streuung sind Messung, Untergruppen, Ergebnisskala und Varianzmodellierung zu untersuchen. Ein sauberes Muster stützt die Diagnosebedingungen, beweist sie aber nicht und begründet keine Kausalität."
        else:
            display={"random horizontal band":"një brez horizontal të rastësishëm","curvature":"lakim","increasing spread":"shpërndarje në rritje","decreasing spread":"shpërndarje në ulje"}[pattern]
            if pattern=="random horizontal band": message="Mesataret e rezidualeve qëndrojnë afër zeros dhe shpërndarjet mbeten të ngjashme, siç pritet. Në këtë përmbledhje të grupuar nuk duket jolinearitet apo pabarazi e variancës"
            elif pattern=="curvature": message="Mesataret e rezidualeve ndryshojnë sistematikisht nga pozitive në negative dhe përsëri, duke treguar lakim. Funksioni mesatar në vijë të drejtë nuk mjafton"
            else: message=f"Mesataret e rezidualeve qëndrojnë afër zeros, por shpërndarja tregon {display}. Kushti i variancës konstante është i dyshimtë"
            prompt=rf"Në pesë breza në rritje të vlerave të përshtatura, të numëruar nga 1 deri në 5, mesataret e rezidualeve janë {means} dhe devijimet standarde të rezidualeve janë {spreads}. (a) Vizato koordinatat mesatare {mean_coordinates}. Në çdo pikë vizato një shtyllë vertikale prej mesatares minus një devijim standard deri te mesatarja plus një devijim standard. (b) Përcakto nëse modeli kryesor është brez horizontal i rastësishëm, lakim, shpërndarje në rritje apo shpërndarje në ulje. (c) Emërto kushtin e modelit linear që vihet në dyshim dhe një hap të arsyeshëm të mëtejshëm diagnostik ose modelues."
            solution=rf"Koordinatat e plota mesatare janë {mean_coordinates}. Pikat fundore të pesë shtyllave vertikale janë {bar_coordinates}. Së bashku, paraqitja e grupuar tregon {display}. {message}. Shqyrto diagramin e rezidualeve për çdo rast kundrejt vlerave të përshtatura, jo vetëm pesë brezat. Për lakimin, shqyrto nëse një parashikues i transformuar ose term jolinear i arsyetuar qartë përputhet me pyetjen kërkimore. Për ndryshim të shpërndarjes, kontrollo matjen, nëngrupet, shkallën e rezultatit dhe modelimin e variancës. Një model i pastër i mbështet kushtet diagnostike, por nuk i provon dhe nuk vendos shkakësi."
        exg.append(task(5,10,i,title,prompt));sog.append(task(5,10,i,title,solution))
    ex.append("".join(exg));sol.append("".join(sog));return ex,sol


def main()->int:
    parser=argparse.ArgumentParser();parser.add_argument("--locale",choices=("en","de","sq"),default="en");args=parser.parse_args()
    exercises,solutions=render_localized(args.locale);write_pair(5,args.locale,10,exercises,solutions);validate_sources_allowing_incomplete_locales(args.locale,topic=5)
    print(f"Generated and source-validated Topic 5 {args.locale} exercise and solution sources.");return 0


if __name__=="__main__": raise SystemExit(main())
