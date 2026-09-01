---
title: "Covariance and Correlation"
subtitle: "Understanding how two variables vary together"
document-id: "topic-04-covariance-correlation-summary-en"
course-id: "intro-statistics"
topic-id: "topic-04-covariance-correlation"
topic-number: "04"
topic-slug: "covariance-correlation"
document-type: "summary"
locale: "en"
figure-asset: "topic-04-covariance-correlation-summary-figure-en.png"
---

## Purpose and foundations

Covariance and correlation describe how two numerical variables vary together across the same cases. Each case must contribute a matched pair $(x_i,y_i)$. A scatterplot is the essential starting point: place one variable on the horizontal axis, the other on the vertical axis, and represent every case by one point. The resulting cloud shows direction, form, strength, clusters, and unusual observations in a way that a single coefficient cannot.

A positive association means that cases with larger $x$ values tend to have larger $y$ values. A negative association means that larger $x$ values tend to accompany smaller $y$ values. A value near zero for a linear coefficient means little linear association, not necessarily no relationship. Curved patterns, separate subgroups, or a restricted range can all make a coefficient incomplete or misleading.

Covariance begins with deviations from the two means. A case contributes positively when both values are above their means or both are below. It contributes negatively when one value is above its mean and the other is below. Averaging these cross-products gives the sample covariance. Its sign is informative, but its magnitude depends on the measurement units. Measuring hours in minutes, for example, changes the covariance even though the underlying pairing of cases has not changed.

| Feature | Covariance | Pearson correlation |
|---|---|---|
| Direction | Sign shows positive or negative co-variation | Sign shows positive or negative linear association |
| Scale | Depends on both variables' units | Unit-free because both variables are standardized |
| Numerical range | Not restricted to a fixed interval | Always between $-1$ and $1$ |
| Main role | Building block for association and regression | Comparable summary of linear direction and strength |

## Core ideas

Pearson's correlation $r$ standardizes covariance by dividing by the two sample standard deviations. A value near $1$ indicates that the points follow a strong positive straight-line pattern. A value near $-1$ indicates a strong negative straight-line pattern. A value near zero indicates little straight-line pattern. The coefficient describes the sample. The population correlation is commonly written $\rho$, and inference is needed when the goal is a population conclusion.

Spearman's rank correlation replaces observed values with their ranks and assesses whether the variables follow a **monotonic** relationship. Monotonic means that the tendency moves consistently in one direction: as one variable increases, the other generally increases, or it generally decreases. The pattern may curve while preserving that order. Spearman correlation can therefore remain high for a curved monotonic association that Pearson correlation summarizes less fully. Neither coefficient represents a U-shaped relationship well because the direction reverses across the range.

| Diagnostic question | What to inspect | Why it changes interpretation |
|---|---|---|
| Is the form approximately linear? | Scatterplot and possible smooth pattern | Pearson $r$ summarizes a straight-line tendency |
| Are unusual points influential? | Labeled scatterplot and sensitivity comparison | One distant point can change direction or magnitude |
| Are groups mixed together? | Colors or panels for meaningful groups | A pooled association may differ from within-group associations |
| Is the observed range restricted? | Variable ranges and sampling process | Limited variation can weaken an observed coefficient |
| Is the pairing valid? | Case identifiers and measurement timing | Correlation requires both values to refer to the same case |

Correlation does not establish causation. An observed association may reflect a direct influence, a reverse direction of influence, a third variable related to both, selection into the sample, measurement artifacts, or chance. Temporal order and a credible research design provide information that a coefficient alone cannot. Even when causal reasoning is not intended, the substantive context still determines whether the paired variables and their interpretation make sense.

When a population conclusion is intended, the sample coefficient can be tested against $H_0:\rho=0$. Keep that test separate from magnitude and practical meaning. A small p-value concerns compatibility with a zero population correlation under the model; it does not make the association large, important, or causal.

## Formula guide

The sample covariance averages paired cross-products of deviations, using $n-1$ in the denominator:

$$
s_{xy}=\frac{1}{n-1}\sum_{i=1}^{n}(x_i-\bar{x})(y_i-\bar{y})
$$

The sign of each product records whether the two deviations point in the same or opposite directions. Large deviations receive more weight because their product has greater magnitude.

Pearson's sample correlation divides covariance by the product of the two sample standard deviations:

$$
r_{xy}=\frac{s_{xy}}{s_xs_y}
$$

When corrected sums are available, the same coefficient can be calculated directly as

$$
r_{xy}=
\frac{\sum_{i=1}^{n}(x_i-\bar{x})(y_i-\bar{y})}
{\sqrt{\sum_{i=1}^{n}(x_i-\bar{x})^2
\sum_{i=1}^{n}(y_i-\bar{y})^2}}.
$$

Both forms require the same paired cases in the two variables. Reordering one column without its partner destroys the pairs and changes the question.

The same calculation can be written as a sum of products of standardized scores. This makes the unit-free nature of the coefficient visible:

$$
r_{xy}=\frac{1}{n-1}\sum_{i=1}^{n}z_{xi}z_{yi}
$$

For a sample without tied ranks, Spearman's rank correlation can be calculated from the difference $d_i$ between each case's two ranks:

$$
r_s=1-\frac{6\sum_{i=1}^{n}d_i^2}{n(n^2-1)}
$$

With tied ranks, calculate Pearson correlation on the assigned ranks instead. In all forms, the coefficient must be read with the scatterplot or rank pattern that produced it.

To test the population Pearson correlation against $H_0:\rho=0$, use

$$
t=\frac{r\sqrt{n-2}}{\sqrt{1-r^2}},
\qquad
df=n-2.
$$

The alternative determines whether the reference area is one-sided or two-sided. The calculation relies on independent paired cases, a relationship for which a linear Pearson summary is defensible, and the absence of design or influential-point problems that would invalidate the interpretation.

| Result to report | Question it answers | What it cannot establish alone |
|---|---|---|
| Scatterplot form | What pattern, clusters, range, and unusual points are visible? | A population conclusion |
| $r$ or $r_s$ | What direction and linear or monotonic strength appears in the sample? | Causation |
| $t$, $df$, and p-value | How compatible is the sample Pearson coefficient with $\rho=0$ under the model? | Practical importance or a large association |

## Reading the explanatory figure

![Two scatterplots compare a curved monotonic pattern with a U-shaped pattern and report Pearson and Spearman correlations above each panel.](assets/topic-04-covariance-correlation-summary-figure-en.png){#fig-summary-t04 width=92%}

The left panel rises throughout the observed range. The increase is curved rather than straight, but the ordering is highly consistent: larger $x$ values nearly always accompany larger $y$ values. Spearman's correlation is therefore close to one because ranks preserve this upward order. Pearson's correlation is also strongly positive, but its focus remains the overall straight-line component of the pattern. The visible curve tells you that a straight-line summary does not capture every feature.

The right panel is U-shaped. Moving from the far left toward the center, $y$ decreases as $x$ increases. Moving from the center toward the far right, $y$ increases as $x$ increases. These opposite directions cancel in both Pearson and Spearman calculations, producing values near zero. Yet the variables have a pronounced relationship. The correct conclusion is not “no association.” It is that neither a linear nor a monotonic coefficient summarizes this form well.

The connecting lines in the figure help reveal the order of the points; they are not fitted regression lines. The coefficients printed above the panels describe the displayed simulated values. They are teaching results, not estimates from real participants. This example is a reminder to let the plot identify the form and then let a coefficient summarize the feature it was designed to measure.

## Interpretation checklist

Confirm that the variables are numerical or that a rank-based analysis is appropriate. Verify that the values are paired by case. Inspect a scatterplot before calculating a coefficient. Describe direction, form, strength, clusters, range, and unusual points. Choose Pearson correlation for a substantively meaningful linear summary and Spearman correlation for a monotonic rank-based summary. Report the sample size and coefficient, and add an interval or test when a population conclusion is required.

Do not label fixed universal cutoffs as weak, moderate, or strong without context. A coefficient's practical meaning depends on measurement reliability, field, design, and consequences. Check how the result changes when an influential point or meaningful subgroup is examined, but do not remove cases merely to improve a coefficient. Avoid causal verbs unless the design supports them.

## How this topic connects

Covariance is the bridge from descriptive variability to regression. In simple linear regression, the slope can be written as covariance between predictor and outcome divided by predictor variance. Correlation standardizes the same paired tendency, while regression keeps the outcome's unit and gives a fitted change in that outcome for a one-unit predictor change.

Partial correlation later asks how two variables remain associated after linear adjustment for a third. Multiple regression extends the same logic by estimating the conditional association of each predictor while holding the others fixed. Analysis of variance also belongs to this family: it explains variation in an outcome using group membership rather than beginning with a numerical predictor. The shared question is how outcome variation aligns with information supplied by one or more predictors.
