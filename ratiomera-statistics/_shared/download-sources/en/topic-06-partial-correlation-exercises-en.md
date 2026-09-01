---
title: "Exercise Sheet"
subtitle: "Partial Correlation"
document-id: "topic-06-partial-correlation-exercises-en"
topic-id: "topic-06-partial-correlation"
topic-number: "06"
topic-slug: "partial-correlation"
document-type: "exercises"
locale: "en"
paired-document-id: "topic-06-partial-correlation-solutions-en"
---

This sheet contains 20 exercises organized into 2 learning-objective groups. Work through each exercise before consulting its matching complete solution. Show the relevant formula or rule, substituted values, units, and an interpretation. All settings, values, data, and software outputs are constructed teaching material; they are not empirical findings.

# Part I: Theory

## A02: Comparing Bivariate and Partial Correlation

### T06-A02-V01: Practice, prior knowledge, and reasoning

A hypothetical study reports the bivariate correlation $r_{XY}=0.68$ between weekly practice and reasoning score. After linear adjustment for prior knowledge, it reports $r_{XY\cdot Z}=0.34$. (a) Draw a three-variable diagram that could make this change plausible. (b) Compare the signs and magnitudes and say whether adjustment weakened or strengthened the coefficient. (c) Explain the residual interpretation. (d) State why neither coefficient by itself identifies a causal effect. (e) Explain what information you would need before defending prior knowledge as a control variable, and name one limitation of a linear adjustment.

### T06-A02-V02: Search time, experience, and accuracy

A hypothetical study reports the bivariate correlation $r_{XY}=-0.57$ between search time and accuracy. After linear adjustment for archive experience, it reports $r_{XY\cdot Z}=-0.26$. (a) Draw a three-variable diagram that could make this change plausible. (b) Compare the signs and magnitudes and say whether adjustment weakened or strengthened the coefficient. (c) Explain the residual interpretation. (d) State why neither coefficient by itself identifies a causal effect. (e) Explain what information you would need before defending archive experience as a control variable, and name one limitation of a linear adjustment.

### T06-A02-V03: Reading time, workload, and comprehension

A hypothetical study reports the bivariate correlation $r_{XY}=0.18$ between reading time and comprehension. After linear adjustment for course workload, it reports $r_{XY\cdot Z}=0.41$. (a) Draw a three-variable diagram that could make this change plausible. (b) Compare the signs and magnitudes and say whether adjustment weakened or strengthened the coefficient. (c) Explain the residual interpretation. (d) State why neither coefficient by itself identifies a causal effect. (e) Explain what information you would need before defending course workload as a control variable, and name one limitation of a linear adjustment.

### T06-A02-V04: Notifications, task load, and focus

A hypothetical study reports the bivariate correlation $r_{XY}=-0.49$ between notification count and focus. After linear adjustment for task load, it reports $r_{XY\cdot Z}=-0.20$. (a) Draw a three-variable diagram that could make this change plausible. (b) Compare the signs and magnitudes and say whether adjustment weakened or strengthened the coefficient. (c) Explain the residual interpretation. (d) State why neither coefficient by itself identifies a causal effect. (e) Explain what information you would need before defending task load as a control variable, and name one limitation of a linear adjustment.

### T06-A02-V05: Museum visits, education, and knowledge

A hypothetical study reports the bivariate correlation $r_{XY}=0.54$ between museum visits and historical knowledge. After linear adjustment for education, it reports $r_{XY\cdot Z}=0.29$. (a) Draw a three-variable diagram that could make this change plausible. (b) Compare the signs and magnitudes and say whether adjustment weakened or strengthened the coefficient. (c) Explain the residual interpretation. (d) State why neither coefficient by itself identifies a causal effect. (e) Explain what information you would need before defending education as a control variable, and name one limitation of a linear adjustment.

### T06-A02-V06: Route familiarity, distance, and travel time

A hypothetical study reports the bivariate correlation $r_{XY}=-0.21$ between route familiarity and travel time. After linear adjustment for route distance, it reports $r_{XY\cdot Z}=-0.48$. (a) Draw a three-variable diagram that could make this change plausible. (b) Compare the signs and magnitudes and say whether adjustment weakened or strengthened the coefficient. (c) Explain the residual interpretation. (d) State why neither coefficient by itself identifies a causal effect. (e) Explain what information you would need before defending route distance as a control variable, and name one limitation of a linear adjustment.

### T06-A02-V07: Workshop attendance, baseline confidence, and final confidence

A hypothetical study reports the bivariate correlation $r_{XY}=0.61$ between attendance and final confidence. After linear adjustment for baseline confidence, it reports $r_{XY\cdot Z}=0.25$. (a) Draw a three-variable diagram that could make this change plausible. (b) Compare the signs and magnitudes and say whether adjustment weakened or strengthened the coefficient. (c) Explain the residual interpretation. (d) State why neither coefficient by itself identifies a causal effect. (e) Explain what information you would need before defending baseline confidence as a control variable, and name one limitation of a linear adjustment.

### T06-A02-V08: Task switching, workload, and completion

A hypothetical study reports the bivariate correlation $r_{XY}=-0.52$ between task switching and completion score. After linear adjustment for workload, it reports $r_{XY\cdot Z}=-0.28$. (a) Draw a three-variable diagram that could make this change plausible. (b) Compare the signs and magnitudes and say whether adjustment weakened or strengthened the coefficient. (c) Explain the residual interpretation. (d) State why neither coefficient by itself identifies a causal effect. (e) Explain what information you would need before defending workload as a control variable, and name one limitation of a linear adjustment.

### T06-A02-V09: Discussion posts, engagement, and reasoning

A hypothetical study reports the bivariate correlation $r_{XY}=0.59$ between discussion posts and reasoning score. After linear adjustment for general engagement, it reports $r_{XY\cdot Z}=0.19$. (a) Draw a three-variable diagram that could make this change plausible. (b) Compare the signs and magnitudes and say whether adjustment weakened or strengthened the coefficient. (c) Explain the residual interpretation. (d) State why neither coefficient by itself identifies a causal effect. (e) Explain what information you would need before defending general engagement as a control variable, and name one limitation of a linear adjustment.

### T06-A02-V10: Practice regularity, total time, and retention

A hypothetical study reports the bivariate correlation $r_{XY}=0.33$ between practice regularity and retention. After linear adjustment for total study time, it reports $r_{XY\cdot Z}=0.47$. (a) Draw a three-variable diagram that could make this change plausible. (b) Compare the signs and magnitudes and say whether adjustment weakened or strengthened the coefficient. (c) Explain the residual interpretation. (d) State why neither coefficient by itself identifies a causal effect. (e) Explain what information you would need before defending total study time as a control variable, and name one limitation of a linear adjustment.

# Part II: Calculator Practice

## A01: Partial Correlation by Residualization and by Formula

### T06-A01-V01: Practice and reasoning after prior score

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

After separately regressing focal variables $X$ and $Y$ on control variable $Z$, the residual columns are $e_X=(-3.000, -2.000, -1.000, 0.000, 1.000, 2.000, 3.000)$ and $e_Y=(-2.057, -0.357, -1.457, 0.743, 0.143, 2.043, 0.943)$. The original pairwise correlations are $r_{XZ}=0.5200$, $r_{YZ}=0.4800$, and $r_{XY}=0.8761$. (a) Calculate the Pearson correlation between the two residual columns. (b) Verify it with $r_{XY\cdot Z}=(r_{XY}-r_{XZ}r_{YZ})/\sqrt{(1-r_{XZ}^2)(1-r_{YZ}^2)}$. (c) Explain in plain language what has been removed and what the remaining coefficient describes.

### T06-A01-V02: Search time and accuracy after experience

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

After separately regressing focal variables $X$ and $Y$ on control variable $Z$, the residual columns are $e_X=(-3.000, -2.000, -1.000, 0.000, 1.000, 2.000, 3.000)$ and $e_Y=(1.800, 0.100, 1.200, -0.800, 0.200, -2.000, -0.500)$. The original pairwise correlations are $r_{XZ}=-0.4600$, $r_{YZ}=0.5500$, and $r_{XY}=-0.7997$. (a) Calculate the Pearson correlation between the two residual columns. (b) Verify it with $r_{XY\cdot Z}=(r_{XY}-r_{XZ}r_{YZ})/\sqrt{(1-r_{XZ}^2)(1-r_{YZ}^2)}$. (c) Explain in plain language what has been removed and what the remaining coefficient describes.

### T06-A01-V03: Reading and comprehension after prior knowledge

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

After separately regressing focal variables $X$ and $Y$ on control variable $Z$, the residual columns are $e_X=(-4.000, -2.000, -1.000, 0.000, 1.000, 2.000, 4.000)$ and $e_Y=(-1.643, -0.343, -1.243, 0.857, 0.157, 1.857, 0.357)$. The original pairwise correlations are $r_{XZ}=0.5800$, $r_{YZ}=0.4400$, and $r_{XY}=0.7834$. (a) Calculate the Pearson correlation between the two residual columns. (b) Verify it with $r_{XY\cdot Z}=(r_{XY}-r_{XZ}r_{YZ})/\sqrt{(1-r_{XZ}^2)(1-r_{YZ}^2)}$. (c) Explain in plain language what has been removed and what the remaining coefficient describes.

### T06-A01-V04: Notifications and focus after workload

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

After separately regressing focal variables $X$ and $Y$ on control variable $Z$, the residual columns are $e_X=(-3.000, -2.000, -1.000, 0.000, 1.000, 2.000, 3.000)$ and $e_Y=(1.400, 0.000, 1.300, -0.700, 0.100, -1.800, -0.300)$. The original pairwise correlations are $r_{XZ}=-0.5100$, $r_{YZ}=0.4900$, and $r_{XY}=-0.7628$. (a) Calculate the Pearson correlation between the two residual columns. (b) Verify it with $r_{XY\cdot Z}=(r_{XY}-r_{XZ}r_{YZ})/\sqrt{(1-r_{XZ}^2)(1-r_{YZ}^2)}$. (c) Explain in plain language what has been removed and what the remaining coefficient describes.

### T06-A01-V05: Museum visits and knowledge after education

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

After separately regressing focal variables $X$ and $Y$ on control variable $Z$, the residual columns are $e_X=(-4.000, -2.000, -1.000, 0.000, 1.000, 2.000, 4.000)$ and $e_Y=(-1.171, 0.029, -0.971, 0.729, -0.371, 1.529, 0.229)$. The original pairwise correlations are $r_{XZ}=0.4700$, $r_{YZ}=0.5300$, and $r_{XY}=0.7074$. (a) Calculate the Pearson correlation between the two residual columns. (b) Verify it with $r_{XY\cdot Z}=(r_{XY}-r_{XZ}r_{YZ})/\sqrt{(1-r_{XZ}^2)(1-r_{YZ}^2)}$. (c) Explain in plain language what has been removed and what the remaining coefficient describes.

### T06-A01-V06: Route familiarity and travel time after distance

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

After separately regressing focal variables $X$ and $Y$ on control variable $Z$, the residual columns are $e_X=(-3.000, -2.000, -1.000, 0.000, 1.000, 2.000, 3.000)$ and $e_Y=(1.700, 0.300, 0.900, -1.000, 0.400, -1.500, -0.800)$. The original pairwise correlations are $r_{XZ}=-0.4300$, $r_{YZ}=0.6000$, and $r_{XY}=-0.8235$. (a) Calculate the Pearson correlation between the two residual columns. (b) Verify it with $r_{XY\cdot Z}=(r_{XY}-r_{XZ}r_{YZ})/\sqrt{(1-r_{XZ}^2)(1-r_{YZ}^2)}$. (c) Explain in plain language what has been removed and what the remaining coefficient describes.

### T06-A01-V07: Workshop attendance and confidence after baseline

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

After separately regressing focal variables $X$ and $Y$ on control variable $Z$, the residual columns are $e_X=(-4.000, -2.000, -1.000, 0.000, 1.000, 2.000, 4.000)$ and $e_Y=(-1.843, -0.243, -0.943, 0.557, 0.057, 1.757, 0.657)$. The original pairwise correlations are $r_{XZ}=0.6200$, $r_{YZ}=0.4000$, and $r_{XY}=0.8300$. (a) Calculate the Pearson correlation between the two residual columns. (b) Verify it with $r_{XY\cdot Z}=(r_{XY}-r_{XZ}r_{YZ})/\sqrt{(1-r_{XZ}^2)(1-r_{YZ}^2)}$. (c) Explain in plain language what has been removed and what the remaining coefficient describes.

### T06-A01-V08: Task switching and completion after task load

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

After separately regressing focal variables $X$ and $Y$ on control variable $Z$, the residual columns are $e_X=(-3.000, -2.000, -1.000, 0.000, 1.000, 2.000, 3.000)$ and $e_Y=(1.200, -0.100, 1.400, -0.600, 0.300, -1.600, -0.600)$. The original pairwise correlations are $r_{XZ}=-0.5500$, $r_{YZ}=0.4500$, and $r_{XY}=-0.7617$. (a) Calculate the Pearson correlation between the two residual columns. (b) Verify it with $r_{XY\cdot Z}=(r_{XY}-r_{XZ}r_{YZ})/\sqrt{(1-r_{XZ}^2)(1-r_{YZ}^2)}$. (c) Explain in plain language what has been removed and what the remaining coefficient describes.

### T06-A01-V09: Discussion posts and reasoning after engagement

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

After separately regressing focal variables $X$ and $Y$ on control variable $Z$, the residual columns are $e_X=(-4.000, -2.000, -1.000, 0.000, 1.000, 2.000, 4.000)$ and $e_Y=(-1.529, -0.129, -1.029, 0.671, -0.229, 1.471, 0.771)$. The original pairwise correlations are $r_{XZ}=0.5000$, $r_{YZ}=0.5700$, and $r_{XY}=0.8460$. (a) Calculate the Pearson correlation between the two residual columns. (b) Verify it with $r_{XY\cdot Z}=(r_{XY}-r_{XZ}r_{YZ})/\sqrt{(1-r_{XZ}^2)(1-r_{YZ}^2)}$. (c) Explain in plain language what has been removed and what the remaining coefficient describes.

### T06-A01-V10: Practice regularity and retention after study time

**Reason first.** Before calculating, state the relationship, rule, or expected pattern that makes the calculation appropriate.

After separately regressing focal variables $X$ and $Y$ on control variable $Z$, the residual columns are $e_X=(-3.000, -2.000, -1.000, 0.000, 1.000, 2.000, 3.000)$ and $e_Y=(-1.214, 0.086, -1.514, 0.786, -0.114, 1.386, 0.586)$. The original pairwise correlations are $r_{XZ}=0.5600$, $r_{YZ}=0.4600$, and $r_{XY}=0.7637$. (a) Calculate the Pearson correlation between the two residual columns. (b) Verify it with $r_{XY\cdot Z}=(r_{XY}-r_{XZ}r_{YZ})/\sqrt{(1-r_{XZ}^2)(1-r_{YZ}^2)}$. (c) Explain in plain language what has been removed and what the remaining coefficient describes.
