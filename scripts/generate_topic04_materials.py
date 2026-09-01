#!/usr/bin/env python3
"""Generate Ratiomera's multilingual Topic 4 practice pair.

The seven registered worksheet groups contribute learning objectives only.
Every context, dataset, value, question, and explanation below is new Ratiomera
content. English remains canonical; the reviewed German and Albanian versions
reuse its identifiers, values, formulas, and results.
"""

from __future__ import annotations

import argparse
import math

from intro_stats_practice_support import (
    group_heading,
    number,
    pearson,
    sample_mean,
    task,
    validate_sources_allowing_incomplete_locales,
    write_pair,
)


NONLINEAR_CONTEXTS = [
    ("Background sound and proofreading errors", "background-sound setting in coded units", "proofreading errors", 4, 1),
    ("Room temperature and concentration loss", "room temperature in degrees Celsius", "concentration-loss score", 22, 2),
    ("Daily practice and fatigue at both extremes", "daily practice time in hours", "fatigue score", 4, 1),
    ("Museum crowding and visit discomfort", "museum-crowding score", "discomfort rating", 4, 3),
    ("Text size and reading difficulty", "text size in typographic points", "reading-difficulty score", 12, 2),
    ("Notification frequency and task disruption", "notifications per hour", "disruption score", 3, 1),
    ("Route complexity and navigation strain", "route-complexity score", "navigation-strain score", 5, 3),
    ("Session length and restlessness", "session length in ten-minute units", "restlessness score", 6, 1),
    ("Archive humidity and preservation risk", "relative humidity in ten-percentage-point units", "preservation-risk score", 5, 2),
    ("Lighting intensity and visual discomfort", "lighting intensity in coded units", "visual-discomfort score", 4, 2),
]


THIRD_VARIABLE_CASES = [
    ("Library visits and course marks", "weekly library visits", "course marks", "study motivation and course workload", "motivated learners may both visit more often and study more effectively", "measure relevant study habits prospectively and avoid calling the adjusted association a causal effect"),
    ("Park access and neighborhood trust", "nearby park space", "average trust", "neighborhood income and public investment", "better-resourced areas may receive both parks and services that support trust", "compare changes around planned park openings with comparable neighborhoods and resident-level measurements"),
    ("Remote work and volunteer hours", "remote-work frequency", "volunteer hours", "schedule flexibility and occupation", "flexible occupations can permit both remote work and volunteering", "measure the time order and use a credible policy comparison or randomized access when feasible"),
    ("Museum membership and cultural participation", "museum membership", "cultural-event attendance", "prior interest in cultural activities", "existing interest can lead to both membership and attendance", "measure baseline interest and distinguish prediction from a membership effect"),
    ("Cycling lanes and retail visits", "protected cycling infrastructure", "weekend shop visits", "street centrality and store mix", "central streets can attract infrastructure and visitors for separate reasons", "use repeated before-and-after counts on treated and comparable untreated streets"),
    ("Caption availability and course completion", "caption availability", "course completion", "course production quality and subject area", "better-funded courses may provide both captions and stronger learner support", "compare otherwise similar courses or randomize a phased caption rollout"),
    ("Garden plots and wellbeing", "community-garden participation", "wellbeing", "baseline health and social connection", "healthier or more connected residents may be more likely to obtain and use a plot", "measure wellbeing before allocation and exploit randomized plot offers if demand exceeds supply"),
    ("Transit use and daily activity", "public-transit use", "daily step count", "urban density and car access", "dense neighborhoods may encourage both transit use and walking", "collect neighborhood and mobility information and use longitudinal or policy-change evidence"),
    ("Music lessons and memory", "years of music lessons", "memory score", "family resources and educational support", "resources can affect access to lessons and cognitive opportunities", "measure baseline scores and relevant family conditions, or evaluate randomized lesson access"),
    ("Online discussion and exam performance", "discussion-board posts", "exam score", "prior understanding and engagement", "engaged students may both post more and prepare more thoroughly", "measure prior achievement and use a designed encouragement or other credible comparison"),
]


CORRELATION_TESTS = [
    ("Practice time and reasoning score", "weekly practice hours", "reasoning score", 20, 0.41, 2.0, 5.0, 1.7341, "positive"),
    ("Search time and archive accuracy", "search time", "accuracy score", 25, -0.36, 4.0, 3.0, 1.7139, "negative"),
    ("Reading time and comprehension", "reading time", "comprehension score", 30, 0.28, 2.5, 8.0, 1.7011, "positive"),
    ("Navigation errors and route confidence", "navigation-error count", "route-confidence score", 35, -0.33, 3.0, 6.0, 1.6924, "negative"),
    ("Workshop attendance and concept score", "sessions attended", "concept score", 40, 0.24, 1.5, 10.0, 1.6860, "positive"),
    ("Notification count and focus rating", "daily notifications", "focus rating", 45, -0.22, 5.0, 2.0, 1.6811, "negative"),
    ("Museum visits and historical knowledge", "museum visits", "knowledge score", 50, 0.20, 2.0, 7.0, 1.6772, "positive"),
    ("Response delay and satisfaction", "response delay", "satisfaction score", 60, -0.18, 4.0, 4.0, 1.6716, "negative"),
    ("Practice sets and confidence", "practice sets completed", "confidence score", 80, 0.17, 3.0, 5.0, 1.6646, "positive"),
    ("Route familiarity and travel time", "route-familiarity score", "travel time", 100, -0.14, 6.0, 2.5, 1.6606, "negative"),
]


RANK_PAIRS = [
    ("Reading frequency and vocabulary rank", [1,2,3,4,5,6], [1,3,2,5,4,6]),
    ("Search efficiency and accuracy rank", [1,2,3,4,5,6,7], [2,1,4,3,6,5,7]),
    ("Practice rank and reasoning rank", [1,2,3,4,5,6], [1,2,4,3,6,5]),
    ("Attendance rank and confidence rank", [1,2,3,4,5,6,7], [1,3,2,4,6,7,5]),
    ("Navigation skill and error rank", [1,2,3,4,5,6], [6,5,3,4,2,1]),
    ("Response-delay and satisfaction rank", [1,2,3,4,5,6,7], [7,5,6,4,3,1,2]),
    ("Museum visits and knowledge rank", [1,2,3,4,5,6], [2,1,3,5,4,6]),
    ("Practice regularity and retention rank", [1,2,3,4,5,6,7], [1,2,4,3,5,7,6]),
    ("Task switching and focus rank", [1,2,3,4,5,6], [5,6,4,3,1,2]),
    ("Archive experience and search rank", [1,2,3,4,5,6,7], [1,3,2,5,4,7,6]),
]


MONOTONIC_CASES = [
    ("Practice hours and fluent-recall score", [1,2,3,4,5,6,7], [2,3,5,8,12,17,23]),
    ("Archive experience and retrieval speed", [1,2,3,4,5,6,7], [70,53,41,32,26,22,19]),
    ("Museum visits and knowledge score", [1,2,3,4,5,6,7], [10,13,17,22,28,35,43]),
    ("Route familiarity and navigation time", [1,2,3,4,5,6,7], [65,48,37,29,24,20,17]),
    ("Practice sets and confidence score", [1,2,3,4,5,6,7], [20,22,25,29,34,40,47]),
    ("Notification load and focus score", [1,2,3,4,5,6,7], [82,69,59,51,45,40,36]),
    ("Reading sessions and vocabulary score", [1,2,3,4,5,6,7], [30,31,34,39,46,55,66]),
    ("Search attempts and remaining errors", [1,2,3,4,5,6,7], [24,18,14,11,9,8,7]),
    ("Workshop sessions and reasoning score", [1,2,3,4,5,6,7], [40,43,47,52,58,65,73]),
    ("Route complexity and completion rate", [1,2,3,4,5,6,7], [95,83,72,62,53,45,38]),
]


TIED_CASES = [
    ("Practice days and confidence", [1,1,2,3,3,4,5,5], [42,45,45,51,54,54,60,63], 5, 2),
    ("Museum visits and knowledge", [0,1,1,2,3,3,4,4], [30,34,36,36,41,45,45,48], 7, 3),
    ("Archive shifts and retrieval skill", [1,2,2,2,3,4,4,5], [18,21,21,24,27,27,30,33], 4, 2),
    ("Reading sessions and recall", [2,2,3,4,4,5,6,6], [50,50,55,59,62,62,68,71], 3, 4),
    ("Route attempts and accuracy", [1,1,2,2,3,4,5,5], [61,64,64,68,72,72,77,80], 6, 2),
    ("Workshop attendance and reasoning", [0,1,1,2,2,3,4,4], [35,39,42,42,47,50,50,54], 8, 3),
    ("Practice sets and fluency", [1,2,2,3,4,4,5,5], [44,47,47,52,56,59,59,63], 2, 5),
    ("Search experience and speed", [1,1,2,3,3,4,4,5], [75,69,69,62,58,58,53,49], 100, 2),
    ("Discussion posts and confidence", [0,1,1,2,3,3,4,5], [40,43,46,46,51,55,55,59], 9, 2),
    ("Navigation practice and errors", [1,2,2,3,3,4,5,5], [18,16,16,13,11,11,8,6], 20, 3),
]


CLAIM_CASES = [
    ("Puzzle apps and navigation", "A one-time volunteer survey finds that puzzle-app users report better navigation than nonusers and concludes that the app creates navigation ability.", "individual survey respondents, with both variables recorded at the individual level", "self-selection, self-reported measurement, uncertain time order, and differences in age or prior spatial interest", "measure navigation objectively at baseline and follow-up and, when feasible, randomly assign access to comparable activities"),
    ("Parks and individual trust", "Districts with more parks have higher average trust, so a report claims that adding one park will make every resident more trusting.", "districts, with both measurements aggregated to the district level before the claim jumps to individual residents", "the ecological jump from district averages to individuals, income, density, safety, and public investment", "collect representative resident-level repeated measurements around park changes and use comparable districts"),
    ("Blue notebooks and memory", "An online poll reports higher self-reported grades among people choosing blue notebooks and says blue paper improves memory.", "individual online-poll respondents, with notebook choice and reported grade recorded at the individual level", "volunteer sampling, unverified outcomes, study habits, school differences, and reverse timing", "randomly assign otherwise equivalent notebook colors and assess a common objective outcome"),
    ("Remote work and volunteering", "Employees who choose remote work report more volunteer hours, and a blog says remote work produces civic responsibility.", "individual employees, with work arrangement and volunteer hours recorded at the individual level", "occupation, schedule flexibility, commuting time, income, caregiving, and employee preference", "measure outcomes before and after a credible policy change with comparable employees"),
    ("Morning markets and diet", "Towns with morning markets have higher household dietary-variety averages, and a report claims that attending a market improves every household's diet.", "towns, with dietary variety aggregated across households before the claim shifts to every household", "town-level aggregation, wealth, agriculture, transport, tourism, and unmeasured market attendance", "sample households directly and compare changes in matched towns before and after openings"),
    ("Digital reminders and attendance", "Clinic attendance rose from 69% to 77% after reminders were introduced, without a concurrent comparison group, and the clinic attributes the full change to reminders.", "scheduled appointments or patients summarized within two clinic time periods, making this a before-and-after aggregate comparison", "patient mix, staffing, appointment types, season, scheduling, and changes in the recorded denominator", "use randomized reminder assignment or a concurrent comparable clinic with consistent outcome definitions"),
    ("Poetry clubs and empathy", "Poetry-club members report higher empathy than an unrelated online benchmark, and a feature claims club membership produces empathy.", "individual club members and separate online respondents, with individual-level scores drawn from incomparable samples", "self-selection, incomparable samples, self-report measurement, and pre-existing literary interest", "measure baseline empathy in comparable groups and use randomized invitations if participation cannot be assigned"),
    ("Cycle lanes and retail traffic", "Streets with cycle lanes receive more weekend visits, and an association says adding lanes will produce the entire observed difference.", "streets, with visitor counts aggregated at the street level", "street centrality, shop mix, events, parking, pedestrian access, and pre-existing visitor levels", "collect repeated counts before and after installation on treated and matched untreated streets"),
    ("Garden plots and wellbeing", "Plot renters report greater wellbeing than people on a waiting list, and a release says gardening cures low wellbeing.", "individual plot renters and waiting-list members, with participation and wellbeing recorded at the individual level", "health, mobility, motivation, social ties, selective allocation, and lack of baseline measurement", "measure validated outcomes before allocation and use a lottery when scarce plots permit one"),
    ("Captioned courses and completion", "Courses offering captions have higher completion averages, and a platform says captions alone cause persistence.", "courses, with completion aggregated across learners at the course level", "course topic, budget, instructional quality, support, learner composition, and course-level aggregation", "compare matched courses or a randomized phased caption introduction using learner-level outcomes"),
]


def midranks(values: list[float]) -> list[float]:
    order = sorted(range(len(values)), key=lambda i: values[i])
    ranks = [0.0] * len(values)
    position = 0
    while position < len(order):
        end = position
        while end + 1 < len(order) and values[order[end + 1]] == values[order[position]]:
            end += 1
        average_rank = ((position + 1) + (end + 1)) / 2
        for location in range(position, end + 1):
            ranks[order[location]] = average_rank
        position = end + 1
    return ranks


def vector(values: list[float]) -> str:
    return "(" + ", ".join(number(v, 1) if isinstance(v, float) and not v.is_integer() else str(int(v)) for v in values) + ")"


def render_english() -> tuple[list[str], list[str]]:
    ex: list[str] = []
    sol: list[str] = []

    ex_group=[group_heading(1,"Pearson Correlation and Hidden Nonlinearity")]
    sol_group=[group_heading(1,"Pearson Correlation and Hidden Nonlinearity")]
    for i,(title,x_label,y_label,offset,scale) in enumerate(NONLINEAR_CONTEXTS,1):
        centered=[-3,-2,-1,0,1,2,3]; x=[v+offset for v in centered]; y=[scale*v*v+2 for v in centered]; r=pearson(x,y)
        ex_group.append(task(4,1,i,title,f"Seven constructed cases give $X={vector(x)}$ for {x_label} and $Y={vector(y)}$ for {y_label}. (a) Calculate both means, the cross-product sum $\\sum(x_i-\\bar x)(y_i-\\bar y)$, and Pearson's $r$. (b) Describe the pattern you would see in a scatterplot. (c) Explain why a coefficient near zero does not mean that the two variables are unrelated in every sense."))
        cross=sum((a-sample_mean(x))*(b-sample_mean(y)) for a,b in zip(x,y)); ssx=sum((a-sample_mean(x))**2 for a in x);ssy=sum((b-sample_mean(y))**2 for b in y)
        sol_group.append(task(4,1,i,title,f"The means are $\\bar x={number(sample_mean(x),3)}$ and $\\bar y={number(sample_mean(y),3)}$. Symmetric low and high $X$ values have the same $Y$ values, so the positive and negative cross-products cancel: $\\sum(x_i-\\bar x)(y_i-\\bar y)={number(cross,3)}$. The denominator is $\\sqrt{{{number(ssx,3)}({number(ssy,3)})}}$, giving $r={number(r,4)}$. A scatterplot forms a U shape: the outcome is lowest near the middle of {x_label} and rises toward either extreme. Pearson's $r$ summarizes a straight-line pattern only. Here it is near zero because there is no overall upward or downward line, not because the visible nonlinear relationship is absent."))
    ex.append("".join(ex_group));sol.append("".join(sol_group))

    ex_group=[group_heading(2,"Third Variables and the Boundary of Causal Claims")]
    sol_group=[group_heading(2,"Third Variables and the Boundary of Causal Claims")]
    for i,(title,x,y,third,mechanism,design) in enumerate(THIRD_VARIABLE_CASES,1):
        ex_group.append(task(4,2,i,title,f"In an invented teaching scenario, a hypothetical study reports a correlation between {x} and {y}. (a) Explain how {third} could act as a third variable. (b) Draw or describe a three-variable diagram with arrows that represents this explanation. (c) State what the hypothetical correlation does and does not establish. (d) Propose a stronger design or analysis without pretending that statistical adjustment creates random assignment."))
        sol_group.append(task(4,2,i,title,f"A plausible diagram places {third} before both focal variables, with one arrow toward {x} and another toward {y}. The mechanism is that {mechanism}. The reported coefficient describes the sample's linear association between the two measured variables. It does not identify the direction of influence, rule out common causes, or establish a causal effect. A stronger approach would {design}. Even after measured third variables are adjusted for, unmeasured confounding and design limitations remain, so the conclusion must stay model-based rather than causal unless the design supplies causal identification."))
    ex.append("".join(ex_group));sol.append("".join(sol_group))

    ex_group=[group_heading(3,"Testing a Directional Population Correlation")]
    sol_group=[group_heading(3,"Testing a Directional Population Correlation")]
    for i,(title,x,y,n,r,sx,sy,crit,direction) in enumerate(CORRELATION_TESTS,1):
        sign=">" if direction=="positive" else "<"; boundary=crit if direction=="positive" else -crit
        covariance=r*sx*sy
        ex_group.append(task(4,3,i,title,f"A hypothetical sample of $n={n}$ gives sample standard deviations $s_x={number(sx,2)}$ and $s_y={number(sy,2)}$ and sample covariance $s_{{xy}}={number(covariance,4)}$ for {x} and {y}. Before seeing the values, the directional alternative was specified as $H_1:\\rho{sign}0$. (a) Calculate Pearson's $r=s_{{xy}}/(s_xs_y)$ and state $H_0$. (b) Calculate $t=r\\sqrt{{(n-2)/(1-r^2)}}$ with $df=n-2$. (c) Use the one-sided 5% boundary {'+' if direction=='positive' else '-'}{number(crit,4)} to decide. (d) Interpret the sign, strength, statistical evidence, and practical importance separately."))
        stat=r*math.sqrt((n-2)/(1-r*r));reject=stat>boundary if direction=="positive" else stat<boundary
        sol_group.append(task(4,3,i,title,f"First, $r=s_{{xy}}/(s_xs_y)={number(covariance,4)}/[{number(sx,2)}({number(sy,2)})]={number(r,4)}$. The null is $H_0:\\rho=0$. The test statistic is $t={number(r,4)}\\sqrt{{({n}-2)/(1-({number(r,4)})^2)}}={number(stat,4)}$ with $df={n-2}$. It {'crosses' if reject else 'does not cross'} the directional boundary {number(boundary,4)}, so we {'reject' if reject else 'fail to reject'} $H_0$ at 5%. The sample association is {direction}: larger values of {x} tend to accompany {'larger' if r>0 else 'smaller'} values of {y} in a linear sense. Its magnitude is $|r|={number(abs(r),2)}$, which describes the observed linear association. Statistical evidence depends on both $r$ and $n$, while practical importance depends on the variables, consequences, precision, and design. A significant coefficient would still not establish causation."))
    ex.append("".join(ex_group));sol.append("".join(sol_group))

    ex_group=[group_heading(4,"Spearman Correlation from Separate Ranks")]
    sol_group=[group_heading(4,"Spearman Correlation from Separate Ranks")]
    for i,(title,rx,ry) in enumerate(RANK_PAIRS,1):
        n=len(rx);d=[a-b for a,b in zip(rx,ry)];sumd=sum(v*v for v in d);rho=1-6*sumd/(n*(n*n-1))
        ex_group.append(task(4,4,i,title,f"The same {n} cases have rank vectors $R_X={vector(rx)}$ and $R_Y={vector(ry)}$, where rank 1 is the smallest value for each variable. (a) Calculate each difference $d_i=R_{{Xi}}-R_{{Yi}}$ and $\\sum d_i^2$. (b) Use $r_s=1-6\\sum d_i^2/[n(n^2-1)]$. (c) Interpret the sign and magnitude as a monotonic rank association, not as a difference in measurement units."))
        sol_group.append(task(4,4,i,title,f"The rank differences are $d={vector(d)}$, so $\\sum d_i^2={sumd}$. With $n={n}$, $r_s=1-6({sumd})/[{n}({n}^2-1)]={number(rho,4)}$. The {'positive' if rho>0 else 'negative'} sign means that cases with higher ranks on one variable tend to have {'higher' if rho>0 else 'lower'} ranks on the other. The magnitude $|r_s|={number(abs(rho),4)}$ describes how consistently the ordering follows one monotonic direction. Because ranks replace original values, the result does not describe an original-unit slope."))
    ex.append("".join(ex_group));sol.append("".join(sol_group))

    ex_group=[group_heading(5,"Pearson and Spearman under Monotonic Curvature")]
    sol_group=[group_heading(5,"Pearson and Spearman under Monotonic Curvature")]
    for i,(title,x,y) in enumerate(MONOTONIC_CASES,1):
        rp=pearson(x,y); ranks_x=midranks(x); ranks_y=midranks(y);rs=pearson(ranks_x,ranks_y)
        direction="decreasing" if y[-1]<y[0] else "increasing"
        change="decrease" if y[-1]<y[0] else "increase"
        article="a" if direction=="decreasing" else "an"
        x_mean=sample_mean(x);y_mean=sample_mean(y)
        original_cross=sum((a-x_mean)*(b-y_mean) for a,b in zip(x,y))
        original_x_ss=sum((a-x_mean)**2 for a in x);original_y_ss=sum((b-y_mean)**2 for b in y)
        rank_mean=sample_mean(ranks_x)
        rank_cross=sum((a-rank_mean)*(b-rank_mean) for a,b in zip(ranks_x,ranks_y))
        rank_x_ss=sum((a-rank_mean)**2 for a in ranks_x);rank_y_ss=sum((b-rank_mean)**2 for b in ranks_y)
        coordinates=", ".join(f"({a}, {b})" for a,b in zip(x,y))
        ex_group.append(task(4,5,i,title,f"Constructed values are $X={vector(x)}$ and $Y={vector(y)}$. (a) Sketch the point pattern or describe its direction and curvature. (b) Calculate Pearson's $r$ from the original values. (c) Rank both variables and calculate Spearman's $r_s$. (d) Explain why the coefficients differ even though both variables move monotonically."))
        sol_group.append(task(4,5,i,title,f"Plotting the coordinates {coordinates} gives {article} {direction} curve. Every increase in $X$ accompanies {'a' if change=='decrease' else 'an'} {change} in $Y$, but the amount of change is not constant. For the original values, $\\bar x={number(x_mean,4)}$, $\\bar y={number(y_mean,4)}$, $S_{{xy}}={number(original_cross,4)}$, $S_{{xx}}={number(original_x_ss,4)}$, and $S_{{yy}}={number(original_y_ss,4)}$. Thus $r=S_{{xy}}/\\sqrt{{S_{{xx}}S_{{yy}}}}={number(original_cross,4)}/\\sqrt{{{number(original_x_ss,4)}({number(original_y_ss,4)})}}={number(rp,4)}$. The rank vectors are $R_X={vector(ranks_x)}$ and $R_Y={vector(ranks_y)}$, both with mean rank {number(rank_mean,1)}. Their cross-product sum is {number(rank_cross,4)}, and their squared-deviation sums are {number(rank_x_ss,4)} and {number(rank_y_ss,4)}, so $r_s={number(rank_cross,4)}/\\sqrt{{{number(rank_x_ss,4)}({number(rank_y_ss,4)})}}={number(rs,4)}$. Spearman reaches {'-1' if rs<0 else '1'} because the ordering is perfectly monotonic. Pearson is smaller in magnitude because it asks how closely the points follow a straight line and therefore responds to the changing slope."))
    ex.append("".join(ex_group));sol.append("".join(sol_group))

    ex_group=[group_heading(6,"Spearman Correlation with Ties and Positive Transformations")]
    sol_group=[group_heading(6,"Spearman Correlation with Ties and Positive Transformations")]
    for i,(title,x,y,a,b) in enumerate(TIED_CASES,1):
        rx=midranks(x);ry=midranks(y);rs=pearson(rx,ry);transformed=[a+b*v for v in y];rst=pearson(rx,midranks(transformed))
        rank_mean=sample_mean(rx)
        rank_cross=sum((left-rank_mean)*(right-rank_mean) for left,right in zip(rx,ry))
        rank_x_ss=sum((value-rank_mean)**2 for value in rx);rank_y_ss=sum((value-rank_mean)**2 for value in ry)
        ex_group.append(task(4,6,i,title,f"Eight cases have $X={vector(x)}$ and $Y={vector(y)}$. (a) Assign average ranks to every tied block and calculate Spearman's correlation as the Pearson correlation of the two rank columns. (b) Transform the second variable to $Y^*={a}+{b}Y$. Explain before recalculating whether the ranks and $r_s$ should change. (c) State what would be different if the multiplier were negative."))
        sol_group.append(task(4,6,i,title,f"Average ranks give $R_X={vector(rx)}$ and $R_Y={vector(ry)}$. Both rank columns have mean {number(rank_mean,1)}. Their cross-product sum is {number(rank_cross,4)}, while the two squared-deviation sums are {number(rank_x_ss,4)} and {number(rank_y_ss,4)}. Therefore $r_s={number(rank_cross,4)}/\\sqrt{{{number(rank_x_ss,4)}({number(rank_y_ss,4)})}}={number(rs,4)}$. The transformation $Y^*={a}+{b}Y$ has a positive multiplier, so it preserves every ordering and every tie. Therefore $R_{{Y^*}}={vector(midranks(transformed))}$ and $r_s^*={number(rst,4)}$, exactly the same coefficient. Adding a constant changes location and multiplying by a positive constant changes scale, but neither changes ranks. A negative multiplier would reverse the ordering and therefore reverse the sign of Spearman's coefficient."))
    ex.append("".join(ex_group));sol.append("".join(sol_group))

    ex_group=[group_heading(7,"Diagnosing Association and Causal Claims")]
    sol_group=[group_heading(7,"Diagnosing Association and Causal Claims")]
    for i,(title,scenario,units,threats,design) in enumerate(CLAIM_CASES,1):
        ex_group.append(task(4,7,i,title,f"The following report is invented solely for this teaching exercise; it is not an empirical claim: {scenario} (a) Identify the observational units and whether the claim is individual-level or aggregate. (b) List at least three specific threats involving measurement, sampling, time order, aggregation, or third variables. (c) Rewrite the result as a defensible association statement. (d) Propose evidence that would address the causal question more credibly."))
        sol_group.append(task(4,7,i,title,f"The observational units and measurement level are {units}. The reported comparison supports, at most, an association at that recorded level. Key threats include {threats}. A defensible statement would say that the measured variables were associated in this particular sample or aggregate dataset, without saying that one produced the other or that every individual follows the group pattern. A stronger evaluation would {design}. The revised design must also report its sampling frame, missingness, measurement quality, time order, and any remaining limits. No correlation coefficient alone can convert an observational comparison into a causal effect."))
    ex.append("".join(ex_group));sol.append("".join(sol_group))
    return ex,sol


GROUP_TITLES = {
    "de": (
        "Pearson-Korrelation und verborgene Nichtlinearität",
        "Drittvariablen und die Grenze kausaler Aussagen",
        "Eine gerichtete Populationskorrelation testen",
        "Spearman-Korrelation aus getrennten Rangfolgen",
        "Pearson und Spearman bei monotoner Krümmung",
        "Spearman-Korrelation bei Bindungen und positiven Transformationen",
        "Zusammenhänge und kausale Aussagen beurteilen",
    ),
    "sq": (
        "Korrelacioni i Pearson-it dhe jolineariteti i fshehur",
        "Ndryshoret e treta dhe kufiri i pohimeve shkakore",
        "Testimi i një korrelacioni të drejtuar në popullatë",
        "Korrelacioni i rangjeve të Spearman-it nga rangje të veçanta",
        "Pearson-i dhe Spearman-i në lakim monoton",
        "Korrelacioni i rangjeve të Spearman-it me vlera të barabarta dhe transformime pozitive",
        "Vlerësimi i lidhjeve dhe pohimeve shkakore",
    ),
}


CASE_LABELS = {
    "de": {
        1: (
            "Hintergrundgeräusche und Korrekturlesefehler", "Raumtemperatur und Konzentrationsverlust",
            "Tägliche Übungszeit und Ermüdung an beiden Extremen", "Gedränge im Museum und Unbehagen beim Besuch",
            "Textgrösse und Leseschwierigkeit", "Häufigkeit von Benachrichtigungen und Aufgabenunterbrechung",
            "Routenkomplexität und Navigationsbelastung", "Sitzungsdauer und Unruhe",
            "Luftfeuchtigkeit im Archiv und Erhaltungsrisiko", "Beleuchtungsstärke und visuelles Unbehagen",
        ),
        2: (
            "Bibliotheksbesuche und Kursnoten", "Parkzugang und Vertrauen im Wohnquartier",
            "Remote-Arbeit und Freiwilligenstunden", "Museumsmitgliedschaft und kulturelle Teilhabe",
            "Velowege und Besuche im Detailhandel", "Verfügbarkeit von Untertiteln und Kursabschluss",
            "Gartenparzellen und Wohlbefinden", "Nutzung des öffentlichen Verkehrs und tägliche Aktivität",
            "Musikunterricht und Gedächtnis", "Online-Diskussionen und Prüfungsleistung",
        ),
        3: (
            "Übungszeit und logisches Denken", "Suchzeit und Archivgenauigkeit",
            "Lesezeit und Textverständnis", "Navigationsfehler und Routenvertrauen",
            "Workshop-Teilnahme und Konzeptverständnis", "Benachrichtigungen und Konzentration",
            "Museumsbesuche und historisches Wissen", "Antwortverzögerung und Zufriedenheit",
            "Übungsserien und Selbstvertrauen", "Routenkenntnis und Reisezeit",
        ),
        4: (
            "Lesehäufigkeit und Wortschatzrang", "Sucheffizienz und Genauigkeitsrang",
            "Übungsrang und Rang des logischen Denkens", "Teilnahmerang und Selbstvertrauensrang",
            "Navigationsfähigkeit und Fehlerrang", "Antwortverzögerung und Zufriedenheitsrang",
            "Museumsbesuche und Wissensrang", "Regelmässigkeit des Übens und Behaltensrang",
            "Aufgabenwechsel und Konzentrationsrang", "Archiverfahrung und Suchrang",
        ),
        5: (
            "Übungsstunden und flüssiger Abruf", "Archiverfahrung und Abrufgeschwindigkeit",
            "Museumsbesuche und Wissensstand", "Routenkenntnis und Navigationszeit",
            "Übungsserien und Selbstvertrauen", "Benachrichtigungsbelastung und Konzentration",
            "Lesesitzungen und Wortschatz", "Suchversuche und verbleibende Fehler",
            "Workshop-Sitzungen und logisches Denken", "Routenkomplexität und Abschlussrate",
        ),
        6: (
            "Übungstage und Selbstvertrauen", "Museumsbesuche und Wissen",
            "Archivschichten und Abruffähigkeit", "Lesesitzungen und Erinnerung",
            "Routenversuche und Genauigkeit", "Workshop-Teilnahme und logisches Denken",
            "Übungsserien und Flüssigkeit", "Sucherfahrung und Geschwindigkeit",
            "Diskussionsbeiträge und Selbstvertrauen", "Navigationsübung und Fehler",
        ),
        7: (
            "Puzzle-Apps und Navigation", "Parks und individuelles Vertrauen",
            "Blaue Notizbücher und Gedächtnis", "Remote-Arbeit und Freiwilligenarbeit",
            "Morgenmärkte und Ernährung", "Digitale Erinnerungen und Anwesenheit",
            "Lyrikgruppen und Empathie", "Velowege und Kundenfrequenz",
            "Gartenparzellen und Wohlbefinden", "Kurse mit Untertiteln und Abschluss",
        ),
    },
    "sq": {
        1: (
            "Zhurma në sfond dhe gabimet në korrigjimin e tekstit", "Temperatura e dhomës dhe humbja e përqendrimit",
            "Ushtrimi ditor dhe lodhja në të dyja skajet", "Mbipopullimi në muze dhe parehatia gjatë vizitës",
            "Madhësia e tekstit dhe vështirësia në lexim", "Shpeshtësia e njoftimeve dhe ndërprerja e detyrës",
            "Ndërlikueshmëria e rrugës dhe ngarkesa e navigimit", "Kohëzgjatja e seancës dhe shqetësimi",
            "Lagështia në arkiv dhe rreziku i ruajtjes", "Intensiteti i ndriçimit dhe parehatia pamore",
        ),
        2: (
            "Vizitat në bibliotekë dhe notat e kursit", "Qasja në park dhe besimi në lagje",
            "Puna në distancë dhe orët e vullnetarizmit", "Anëtarësimi në muze dhe pjesëmarrja kulturore",
            "Korsitë e biçikletave dhe vizitat në dyqane", "Titrimi dhe përfundimi i kursit",
            "Parcelat e kopshtit dhe mirëqenia", "Transporti publik dhe aktiviteti ditor",
            "Mësimet e muzikës dhe kujtesa", "Diskutimet online dhe rezultati në provim",
        ),
        3: (
            "Koha e ushtrimit dhe rezultati i arsyetimit", "Koha e kërkimit dhe saktësia në arkiv",
            "Koha e leximit dhe të kuptuarit", "Gabimet e navigimit dhe siguria për rrugën",
            "Pjesëmarrja në seminar dhe rezultati i koncepteve", "Numri i njoftimeve dhe përqendrimi",
            "Vizitat në muze dhe njohuritë historike", "Vonesa e përgjigjes dhe kënaqësia",
            "Seritë e ushtrimeve dhe vetëbesimi", "Njohja e rrugës dhe koha e udhëtimit",
        ),
        4: (
            "Shpeshtësia e leximit dhe renditja e fjalorit", "Efikasiteti i kërkimit dhe renditja e saktësisë",
            "Renditja e ushtrimit dhe e arsyetimit", "Renditja e pjesëmarrjes dhe e vetëbesimit",
            "Aftësia e navigimit dhe renditja e gabimeve", "Vonesa e përgjigjes dhe renditja e kënaqësisë",
            "Vizitat në muze dhe renditja e njohurive", "Rregullsia e ushtrimit dhe renditja e mbajtjes mend",
            "Kalimi mes detyrave dhe renditja e përqendrimit", "Përvoja në arkiv dhe renditja e kërkimit",
        ),
        5: (
            "Orët e ushtrimit dhe rikujtimi i rrjedhshëm", "Përvoja në arkiv dhe shpejtësia e gjetjes",
            "Vizitat në muze dhe rezultati i njohurive", "Njohja e rrugës dhe koha e navigimit",
            "Seritë e ushtrimeve dhe vetëbesimi", "Ngarkesa e njoftimeve dhe përqendrimi",
            "Seancat e leximit dhe fjalori", "Përpjekjet e kërkimit dhe gabimet e mbetura",
            "Seancat e seminarit dhe arsyetimi", "Ndërlikueshmëria e rrugës dhe shkalla e përfundimit",
        ),
        6: (
            "Ditët e ushtrimit dhe vetëbesimi", "Vizitat në muze dhe njohuritë",
            "Turnet në arkiv dhe aftësia e gjetjes", "Seancat e leximit dhe rikujtimi",
            "Përpjekjet për rrugën dhe saktësia", "Pjesëmarrja në seminar dhe arsyetimi",
            "Seritë e ushtrimeve dhe rrjedhshmëria", "Përvoja në kërkim dhe shpejtësia",
            "Postimet në diskutim dhe vetëbesimi", "Ushtrimi i navigimit dhe gabimet",
        ),
        7: (
            "Aplikacionet me enigma dhe navigimi", "Parqet dhe besimi individual",
            "Fletoret blu dhe kujtesa", "Puna në distancë dhe vullnetarizmi",
            "Tregjet e mëngjesit dhe ushqyerja", "Kujtesat digjitale dhe pjesëmarrja",
            "Klubet e poezisë dhe empatia", "Korsitë e biçikletave dhe vizitat në dyqane",
            "Parcelat e kopshtit dhe mirëqenia", "Kurset me titra dhe përfundimi",
        ),
    },
}


THIRD_VARIABLE_LOCALIZED = {
    "de": (
        ("wöchentliche Bibliotheksbesuche", "Kursnoten", "Lernmotivation und Arbeitsbelastung im Kurs", "Motivierte Lernende besuchen möglicherweise häufiger die Bibliothek und lernen zugleich wirkungsvoller", "wichtige Lerngewohnheiten vorausschauend erfassen und den bereinigten Zusammenhang nicht als kausalen Effekt bezeichnen"),
        ("nahe gelegene Parkflächen", "durchschnittliches Vertrauen", "Einkommen im Wohnquartier und öffentliche Investitionen", "besser ausgestattete Quartiere können sowohl Parks als auch vertrauensfördernde Dienstleistungen erhalten", "Veränderungen rund um geplante Parkeröffnungen mit vergleichbaren Quartieren und Messungen bei den Bewohnenden untersuchen"),
        ("Häufigkeit von Remote-Arbeit", "Freiwilligenstunden", "zeitliche Flexibilität und Beruf", "flexible Berufe können sowohl Remote-Arbeit als auch Freiwilligenarbeit ermöglichen", "die zeitliche Reihenfolge messen und eine glaubwürdige politische Vergleichssituation oder, wenn möglich, zufällig vergebenen Zugang nutzen"),
        ("Museumsmitgliedschaft", "Besuche kultureller Veranstaltungen", "früheres Interesse an kulturellen Aktivitäten", "bestehendes Interesse kann sowohl zur Mitgliedschaft als auch zu mehr Veranstaltungsbesuchen führen", "das Ausgangsinteresse messen und Vorhersage klar von einem Effekt der Mitgliedschaft unterscheiden"),
        ("geschützte Veloinfrastruktur", "Wochenendbesuche in Geschäften", "Zentralität der Strasse und Zusammensetzung der Geschäfte", "zentrale Strassen können aus verschiedenen Gründen sowohl Infrastruktur als auch viele Besuchende anziehen", "wiederholte Vorher-Nachher-Zählungen auf behandelten und vergleichbaren unbehandelten Strassen verwenden"),
        ("Verfügbarkeit von Untertiteln", "Kursabschluss", "Produktionsqualität und Fachgebiet des Kurses", "besser finanzierte Kurse können sowohl Untertitel als auch stärkere Lernunterstützung anbieten", "ansonsten ähnliche Kurse vergleichen oder die schrittweise Einführung von Untertiteln zufällig festlegen"),
        ("Teilnahme an einem Gemeinschaftsgarten", "Wohlbefinden", "Ausgangsgesundheit und soziale Einbindung", "gesündere oder stärker eingebundene Personen erhalten und nutzen möglicherweise eher eine Parzelle", "das Wohlbefinden vor der Vergabe messen und zufällige Parzellenangebote nutzen, wenn die Nachfrage das Angebot übersteigt"),
        ("Nutzung des öffentlichen Verkehrs", "tägliche Schrittzahl", "städtische Dichte und Zugang zu einem Auto", "dichte Wohngebiete können sowohl die Nutzung des öffentlichen Verkehrs als auch das Gehen fördern", "Informationen zu Wohngebiet und Mobilität erheben und Längsschnittdaten oder Änderungen der Verkehrspolitik untersuchen"),
        ("Jahre mit Musikunterricht", "Gedächtniswert", "familiäre Ressourcen und Bildungsunterstützung", "Ressourcen können sowohl den Zugang zu Musikunterricht als auch kognitive Lerngelegenheiten beeinflussen", "Ausgangswerte und relevante familiäre Bedingungen messen oder zufällig vergebenen Zugang zu Musikunterricht untersuchen"),
        ("Beiträge in Online-Diskussionen", "Prüfungswert", "Vorwissen und Engagement", "engagierte Studierende können sowohl mehr Beiträge schreiben als auch gründlicher für die Prüfung lernen", "frühere Leistungen messen und eine geplante Ermutigung oder einen anderen glaubwürdigen Vergleich verwenden"),
    ),
    "sq": (
        ("vizitat javore në bibliotekë", "notat e kursit", "motivimi për të mësuar dhe ngarkesa e kursit", "nxënësit më të motivuar mund ta vizitojnë më shpesh bibliotekën dhe njëkohësisht të mësojnë më me efekt", "të maten paraprakisht zakonet përkatëse të të mësuarit dhe lidhja e përshtatur të mos quhet efekt shkakor"),
        ("hapësira e parkut pranë banesës", "besimi mesatar", "të ardhurat e lagjes dhe investimet publike", "lagjet me më shumë burime mund të marrin si parqe, ashtu edhe shërbime që e mbështesin besimin", "të krahasohen ndryshimet rreth hapjeve të planifikuara të parqeve me lagje të krahasueshme dhe me matje te banorët"),
        ("shpeshtësia e punës në distancë", "orët e vullnetarizmit", "fleksibiliteti i orarit dhe profesioni", "profesionet me orar fleksibël mund të mundësojnë edhe punën në distancë, edhe vullnetarizmin", "të matet rendi kohor dhe të përdoret një krahasim i besueshëm politikash ose, kur është e mundur, qasje e caktuar rastësisht"),
        ("anëtarësimi në muze", "pjesëmarrja në veprimtari kulturore", "interesi i mëparshëm për veprimtaritë kulturore", "interesi ekzistues mund të çojë si te anëtarësimi, ashtu edhe te pjesëmarrja", "të matet interesi fillestar dhe parashikimi të dallohet nga një efekt i anëtarësimit"),
        ("infrastruktura e mbrojtur për biçikleta", "vizitat në dyqane gjatë fundjavës", "pozita qendrore e rrugës dhe llojet e dyqaneve", "rrugët qendrore mund të tërheqin për arsye të ndryshme edhe infrastrukturë, edhe vizitorë", "të përdoren numërime të përsëritura para dhe pas në rrugët e trajtuara dhe në rrugë të krahasueshme të patrajtuara"),
        ("disponueshmëria e titrave", "përfundimi i kursit", "cilësia e prodhimit dhe fusha e kursit", "kurset me më shumë financim mund të ofrojnë edhe titra, edhe mbështetje më të fortë për nxënësit", "të krahasohen kurse të ngjashme në aspektet e tjera ose të caktohet rastësisht një futje graduale e titrave"),
        ("pjesëmarrja në kopshtin e komunitetit", "mirëqenia", "shëndeti fillestar dhe lidhjet shoqërore", "banorët më të shëndetshëm ose më të lidhur mund ta marrin dhe ta përdorin më shpesh një parcelë", "të matet mirëqenia para ndarjes dhe të shfrytëzohen oferta të rastësishme kur kërkesa për parcela është më e madhe se oferta"),
        ("përdorimi i transportit publik", "numri ditor i hapave", "dendësia urbane dhe qasja në makinë", "lagjet e dendura mund të nxisin edhe përdorimin e transportit publik, edhe ecjen", "të mblidhen të dhëna për lagjen dhe lëvizshmërinë dhe të përdoren të dhëna gjatësore ose ndryshime politikash"),
        ("vitet e mësimeve të muzikës", "rezultati i kujtesës", "burimet familjare dhe mbështetja arsimore", "burimet mund të ndikojnë edhe te qasja në mësime, edhe te mundësitë për zhvillim njohës", "të maten rezultatet fillestare dhe kushtet përkatëse familjare ose të vlerësohet qasja e caktuar rastësisht në mësime"),
        ("postimet në diskutimet online", "rezultati në provim", "njohuritë paraprake dhe angazhimi", "studentët e angazhuar mund të postojnë më shumë dhe njëkohësisht të përgatiten më mirë për provim", "të matet arritja paraprake dhe të përdoret një nxitje e planifikuar ose një krahasim tjetër i besueshëm"),
    ),
}


CLAIM_LOCALIZED = {
    "de": (
        ("Eine einmalige Befragung von Freiwilligen zeigt, dass Personen mit Puzzle-App eine bessere Navigation angeben als Personen ohne App. Daraus wird geschlossen, die App erzeuge Navigationsfähigkeit.", "einzelne Befragte; beide Variablen wurden auf Personenebene erfasst", "Selbstselektion, Selbstauskunft, unklare zeitliche Reihenfolge sowie Unterschiede in Alter oder früherem räumlichem Interesse", "die Navigation zu Beginn und später objektiv messen und den Zugang zu vergleichbaren Aktivitäten nach Möglichkeit zufällig zuweisen"),
        ("Bezirke mit mehr Parks haben ein höheres durchschnittliches Vertrauen. Daraus wird geschlossen, ein zusätzlicher Park mache jede dort lebende Person vertrauensvoller.", "Bezirke; beide Messungen wurden auf Bezirksebene zusammengefasst, bevor die Aussage auf Einzelpersonen übertragen wurde", "der unzulässige Sprung von Bezirksmittelwerten zu Einzelpersonen, Einkommen, Dichte, Sicherheit und öffentliche Investitionen", "wiederholte repräsentative Messungen bei Bewohnenden rund um Parkveränderungen durchführen und vergleichbare Bezirke einbeziehen"),
        ("Eine Online-Umfrage berichtet höhere selbst angegebene Noten bei Personen, die blaue Notizbücher wählen. Daraus wird geschlossen, blaues Papier verbessere das Gedächtnis.", "einzelne Teilnehmende einer Online-Umfrage; Notizbuchwahl und angegebene Note wurden auf Personenebene erfasst", "freiwillige Teilnahme, ungeprüfte Ergebnisse, Lerngewohnheiten, Unterschiede zwischen Schulen und umgekehrte zeitliche Reihenfolge", "ansonsten gleiche Notizbuchfarben zufällig zuweisen und ein gemeinsames objektives Ergebnis messen"),
        ("Beschäftigte, die Remote-Arbeit wählen, berichten mehr Freiwilligenstunden. Ein Blog schliesst daraus, Remote-Arbeit erzeuge gesellschaftliches Verantwortungsgefühl.", "einzelne Beschäftigte; Arbeitsform und Freiwilligenstunden wurden auf Personenebene erfasst", "Beruf, zeitliche Flexibilität, Pendelzeit, Einkommen, Betreuungspflichten und persönliche Präferenzen", "Ergebnisse vor und nach einer glaubwürdigen Richtlinienänderung bei vergleichbaren Beschäftigten messen"),
        ("Orte mit Morgenmärkten haben im Mittel eine grössere Ernährungsvielfalt der Haushalte. Daraus wird geschlossen, der Marktbesuch verbessere die Ernährung jedes Haushalts.", "Orte; die Ernährungsvielfalt wurde über Haushalte zusammengefasst, bevor die Aussage auf jeden Haushalt übertragen wurde", "Aggregation auf Ortsebene, Wohlstand, Landwirtschaft, Verkehr, Tourismus und nicht gemessene Marktbesuche", "Haushalte direkt befragen und Veränderungen in passenden Orten vor und nach Markteröffnungen vergleichen"),
        ("Die Anwesenheitsquote einer Klinik stieg nach Einführung digitaler Erinnerungen von 69% auf 77%. Ohne zeitgleiche Vergleichsgruppe schreibt die Klinik die gesamte Veränderung den Erinnerungen zu.", "Termine oder Patientinnen und Patienten, zusammengefasst über zwei Zeiträume derselben Klinik", "veränderte Zusammensetzung der Patientengruppe, Personal, Terminarten, Jahreszeit, Planung und Definition des Nenners", "Erinnerungen zufällig zuweisen oder eine zeitgleiche vergleichbare Klinik mit gleichbleibender Ergebnisdefinition einbeziehen"),
        ("Mitglieder einer Lyrikgruppe berichten mehr Empathie als eine unabhängige Online-Vergleichsgruppe. Daraus wird geschlossen, die Mitgliedschaft erzeuge Empathie.", "einzelne Gruppenmitglieder und getrennt erhobene Online-Befragte aus nicht vergleichbaren Stichproben", "Selbstselektion, nicht vergleichbare Stichproben, Selbstauskunft und bereits vorhandenes literarisches Interesse", "Empathie zu Beginn in vergleichbaren Gruppen messen und Einladungen nach Möglichkeit zufällig vergeben"),
        ("Strassen mit Velowegen haben mehr Besuche am Wochenende. Daraus wird geschlossen, neue Velowege würden den gesamten beobachteten Unterschied erzeugen.", "Strassen; die Besuchszahlen wurden auf Strassenebene zusammengefasst", "Zentralität der Strasse, Zusammensetzung der Geschäfte, Veranstaltungen, Parkplätze, Zugang zu Fuss und frühere Besuchszahlen", "wiederholte Zählungen vor und nach dem Bau auf behandelten und passenden unbehandelten Strassen durchführen"),
        ("Mietende von Gartenparzellen berichten höheres Wohlbefinden als Personen auf einer Warteliste. Daraus wird geschlossen, Gartenarbeit heile geringes Wohlbefinden.", "einzelne Mietende und Personen auf der Warteliste; Teilnahme und Wohlbefinden wurden auf Personenebene erfasst", "Gesundheit, Mobilität, Motivation, soziale Beziehungen, selektive Vergabe und fehlende Ausgangsmessung", "validierte Ergebnisse vor der Vergabe messen und bei knappen Parzellen eine Lotterie nutzen"),
        ("Kurse mit Untertiteln haben höhere durchschnittliche Abschlussraten. Daraus wird geschlossen, Untertitel allein verursachten das Durchhalten.", "Kurse; die Abschlussrate wurde über Lernende auf Kursebene zusammengefasst", "Kursthema, Budget, Unterrichtsqualität, Unterstützung, Zusammensetzung der Lernenden und Aggregation auf Kursebene", "passende Kurse vergleichen oder Untertitel schrittweise und zufällig einführen und Ergebnisse auf Lernendenebene messen"),
    ),
    "sq": (
        ("Një anketë e vetme me vullnetarë gjen se përdoruesit e një aplikacioni me enigma raportojnë navigim më të mirë se jopërdoruesit. Prej kësaj nxirret përfundimi se aplikacioni krijon aftësi navigimi.", "të anketuar individualë; të dyja ndryshoret janë regjistruar në nivel individi", "vetëpërzgjedhja, vetëraportimi, rendi kohor i paqartë dhe dallimet në moshë ose në interesin e mëparshëm hapësinor", "të matet objektivisht navigimi në fillim dhe më vonë dhe, kur është e mundur, qasja në veprimtari të krahasueshme të caktohet rastësisht"),
        ("Rajonet me më shumë parqe kanë besim mesatar më të lartë. Prej kësaj thuhet se shtimi i një parku do ta rriste besimin e çdo banori.", "rajonet; të dyja matjet janë përmbledhur në nivel rajoni para se pohimi të kalojë te individët", "kalimi i gabuar nga mesataret e rajonit te individët, të ardhurat, dendësia, siguria dhe investimet publike", "të mblidhen matje të përsëritura e përfaqësuese te banorët rreth ndryshimeve të parqeve dhe të përdoren rajone të krahasueshme"),
        ("Një anketë online raporton nota më të larta të vetëraportuara te personat që zgjedhin fletore blu. Prej kësaj thuhet se letra blu e përmirëson kujtesën.", "të anketuar individualë online; zgjedhja e fletores dhe nota e raportuar janë regjistruar në nivel individi", "pjesëmarrja vullnetare, rezultatet e paverifikuara, zakonet e të mësuarit, dallimet mes shkollave dhe rendi i kundërt kohor", "ngjyrat e fletoreve, të njëjta në aspektet e tjera, të caktohen rastësisht dhe të matet një rezultat i përbashkët objektiv"),
        ("Punonjësit që zgjedhin punën në distancë raportojnë më shumë orë vullnetarizmi. Një blog thotë se puna në distancë prodhon përgjegjësi qytetare.", "punonjës individualë; mënyra e punës dhe orët e vullnetarizmit janë regjistruar në nivel individi", "profesioni, fleksibiliteti i orarit, koha e udhëtimit, të ardhurat, përgjegjësitë familjare dhe parapëlqimi i punonjësit", "të maten rezultatet para dhe pas një ndryshimi të besueshëm të politikës te punonjës të krahasueshëm"),
        ("Qytetet me tregje të mëngjesit kanë mesatare më të lartë të shumëllojshmërisë ushqimore të familjeve. Prej kësaj thuhet se vizita në treg e përmirëson ushqyerjen e çdo familjeje.", "qytetet; shumëllojshmëria ushqimore është përmbledhur për familjet para se pohimi të kalojë te çdo familje", "grumbullimi në nivel qyteti, pasuria, bujqësia, transporti, turizmi dhe vizitat e pamatura në treg", "të merren kampione drejtpërdrejt nga familjet dhe të krahasohen ndryshimet para e pas hapjes në qytete të ngjashme"),
        ("Pjesëmarrja në një klinikë u rrit nga 69% në 77% pas futjes së kujtesave digjitale. Pa grup krahasimi në të njëjtën kohë, klinika ia atribuon kujtesave tërë ndryshimin.", "takimet ose pacientët, të përmbledhur në dy periudha të së njëjtës klinikë", "përbërja e pacientëve, personeli, llojet e takimeve, stina, planifikimi dhe ndryshimet në emërues", "kujtuesit të caktohen rastësisht ose të përdoret një klinikë e krahasueshme në të njëjtën kohë me përkufizime të pandryshuara të rezultatit"),
        ("Anëtarët e një klubi poezie raportojnë më shumë empati se një grup i veçantë online. Prej kësaj thuhet se anëtarësimi në klub prodhon empati.", "anëtarë individualë të klubit dhe të anketuar të veçantë online nga kampione të pakrahasueshme", "vetëpërzgjedhja, kampionet e pakrahasueshme, vetëraportimi dhe interesi letrar që ekzistonte më parë", "të matet empatia fillestare në grupe të krahasueshme dhe, kur është e mundur, ftesat të caktohen rastësisht"),
        ("Rrugët me korsi biçikletash marrin më shumë vizita gjatë fundjavës. Prej kësaj thuhet se shtimi i korsive do ta prodhojë tërë dallimin e vrojtuar.", "rrugët; numri i vizitorëve është përmbledhur në nivel rruge", "pozita qendrore, llojet e dyqaneve, veprimtaritë, parkimi, qasja në këmbë dhe nivelet e mëparshme të vizitave", "të mblidhen numërime të përsëritura para e pas ndërtimit në rrugët e trajtuara dhe në rrugë të ngjashme të patrajtuara"),
        ("Qiramarrësit e parcelave raportojnë mirëqenie më të lartë se personat në listën e pritjes. Prej kësaj thuhet se kopshtaria e shëron mirëqenien e ulët.", "qiramarrës individualë dhe persona në listën e pritjes; pjesëmarrja dhe mirëqenia janë regjistruar në nivel individi", "shëndeti, lëvizshmëria, motivimi, lidhjet shoqërore, ndarja përzgjedhëse dhe mungesa e matjes fillestare", "të maten rezultate të vlefshme para ndarjes dhe të përdoret shorti kur parcelat janë të pakta"),
        ("Kurset që ofrojnë titra kanë mesatare më të lartë të përfundimit. Prej kësaj thuhet se vetëm titrat e shkaktojnë këmbënguljen.", "kurset; përfundimi është përmbledhur për nxënësit në nivel kursi", "tema, buxheti, cilësia e mësimdhënies, mbështetja, përbërja e nxënësve dhe grumbullimi në nivel kursi", "të krahasohen kurse të ngjashme ose titrat të futen gradualisht e rastësisht duke matur rezultate në nivel nxënësi"),
    ),
}


def render_localized(locale: str) -> tuple[list[str], list[str]]:
    """Render the reviewed de-CH or Albanian adaptation from canonical values."""

    if locale == "en":
        return render_english()
    if locale not in ("de", "sq"):
        raise ValueError(f"unsupported locale: {locale}")
    titles=GROUP_TITLES[locale];labels=CASE_LABELS[locale];ex=[];sol=[]

    exg=[group_heading(1,titles[0])];sog=[group_heading(1,titles[0])]
    for i,(_title,_x_label,_y_label,offset,scale) in enumerate(NONLINEAR_CONTEXTS,1):
        title=labels[1][i-1];centered=[-3,-2,-1,0,1,2,3];x=[v+offset for v in centered];y=[scale*v*v+2 for v in centered];r=pearson(x,y)
        cross=sum((a-sample_mean(x))*(b-sample_mean(y)) for a,b in zip(x,y));ssx=sum((a-sample_mean(x))**2 for a in x);ssy=sum((b-sample_mean(y))**2 for b in y)
        if locale=="de":
            prompt=rf"Sieben konstruierte Fälle im Kontext «{title}» ergeben $X={vector(x)}$ und $Y={vector(y)}$. (a) Berechne beide Mittelwerte, die Kreuzproduktsumme $\sum(x_i-\bar x)(y_i-\bar y)$ und Pearsons $r$. (b) Beschreibe das Muster in einem Streudiagramm. (c) Erkläre, weshalb ein Koeffizient nahe null nicht bedeutet, dass die zwei Variablen in jeder Hinsicht unverbunden sind."
            solution=rf"Die Mittelwerte sind $\bar x={number(sample_mean(x),3)}$ und $\bar y={number(sample_mean(y),3)}$. Symmetrische tiefe und hohe $X$-Werte besitzen dieselben $Y$-Werte. Deshalb heben sich positive und negative Kreuzprodukte auf: $\sum(x_i-\bar x)(y_i-\bar y)={number(cross,3)}$. Der Nenner ist $\sqrt{{{number(ssx,3)}({number(ssy,3)})}}$; damit ergibt sich $r={number(r,4)}$. Das Streudiagramm bildet eine U-Form: Die Ergebnisvariable ist nahe der Mitte der Prädiktorvariable am tiefsten und steigt zu beiden Extremen. Pearsons $r$ fasst nur ein geradliniges Muster zusammen. Hier liegt er nahe null, weil keine allgemeine auf- oder absteigende Gerade vorliegt, nicht weil der sichtbare nichtlineare Zusammenhang fehlt."
        else:
            prompt=rf"Shtatë raste të krijuara në kontekstin «{title}» japin $X={vector(x)}$ dhe $Y={vector(y)}$. (a) Llogarit të dyja mesataret, shumën e prodhimeve të kryqëzuara $\sum(x_i-\bar x)(y_i-\bar y)$ dhe $r$ të Pearson-it. (b) Përshkruaj modelin që do të shfaqej në diagramin e shpërndarjes. (c) Shpjego pse një koeficient afër zeros nuk do të thotë se dy ndryshoret nuk kanë asnjë lloj lidhjeje."
            solution=rf"Mesataret janë $\bar x={number(sample_mean(x),3)}$ dhe $\bar y={number(sample_mean(y),3)}$. Vlerat simetrike të ulëta dhe të larta të $X$ kanë të njëjtat vlera të $Y$, prandaj prodhimet e kryqëzuara pozitive dhe negative anulohen: $\sum(x_i-\bar x)(y_i-\bar y)={number(cross,3)}$. Emëruesi është $\sqrt{{{number(ssx,3)}({number(ssy,3)})}}$, duke dhënë $r={number(r,4)}$. Diagrami i shpërndarjes formon trajtën U: ndryshorja e rezultatit është më e ulët afër mesit të ndryshores parashikuese dhe rritet drejt të dyja skajeve. $r$ i Pearson-it përmbledh vetëm një model në vijë të drejtë. Këtu është afër zeros sepse nuk ka një vijë të përgjithshme rritëse ose zbritëse, jo sepse mungon lidhja e dukshme jolineare."
        exg.append(task(4,1,i,title,prompt));sog.append(task(4,1,i,title,solution))
    ex.append("".join(exg));sol.append("".join(sog))

    exg=[group_heading(2,titles[1])];sog=[group_heading(2,titles[1])]
    for i,(_title,_x,_y,_third,_mechanism,_design) in enumerate(THIRD_VARIABLE_CASES,1):
        title=labels[2][i-1]
        x,y,third,mechanism,design=THIRD_VARIABLE_LOCALIZED[locale][i-1]
        if locale=="de":
            prompt=rf"In einem erfundenen Lehrszenario berichtet eine hypothetische Studie im Kontext «{title}» eine Korrelation zwischen «{x}» und «{y}». (a) Erkläre, wie «{third}» als Drittvariable beide Variablen beeinflussen könnte. (b) Zeichne oder beschreibe ein Diagramm mit drei Variablen und Pfeilen, das diese Erklärung darstellt. (c) Formuliere, was die hypothetische Korrelation zeigt und was nicht. (d) Schlage ein stärkeres Design oder eine stärkere Analyse vor, ohne so zu tun, als erzeuge statistische Bereinigung eine zufällige Zuweisung."
            solution=rf"Ein plausibles Diagramm setzt die Drittvariable «{third}» zeitlich vor die zwei interessierenden Variablen. Ein Pfeil führt zu «{x}», ein zweiter zu «{y}». Der angenommene Mechanismus lautet: {mechanism}. Der berichtete Koeffizient beschreibt den linearen Zusammenhang der zwei gemessenen Variablen in der Stichprobe. Er bestimmt weder die Wirkungsrichtung noch schliesst er gemeinsame Ursachen aus oder belegt einen kausalen Effekt. Ein stärkerer Ansatz würde {design}. Auch nach der Bereinigung um gemessene Drittvariablen bleiben nicht gemessene Störfaktoren und Designgrenzen bestehen. Ohne kausal identifizierendes Design muss der Schluss modellbasiert und nicht kausal bleiben."
        else:
            prompt=rf"Në një skenar mësimor të trilluar, një studim hipotetik në kontekstin «{title}» raporton korrelacion mes «{x}» dhe «{y}». (a) Shpjego si mund të ndikojë ndryshorja e tretë «{third}» në të dyja ndryshoret. (b) Vizato ose përshkruaj një diagram me tri ndryshore dhe shigjeta që e paraqet këtë shpjegim. (c) Thuaj çfarë tregon dhe çfarë nuk tregon korrelacioni hipotetik. (d) Propozo një dizajn ose analizë më të fortë pa pretenduar se përshtatja statistikore krijon caktim të rastësishëm."
            solution=rf"Një diagram i besueshëm e vendos ndryshoren e tretë «{third}» para dy ndryshoreve kryesore. Një shigjetë shkon drejt «{x}» dhe tjetra drejt «{y}». Mekanizmi i supozuar është ky: {mechanism}. Koeficienti i raportuar përshkruan lidhjen lineare të dy ndryshoreve të matura në kampion. Nuk përcakton drejtimin e ndikimit, nuk përjashton shkaqe të përbashkëta dhe nuk vendos efekt shkakor. Një qasje më e fortë do të ishte {design}. Edhe pas përshtatjes për ndryshore të treta të matura, mbeten faktorë ngatërrues të pamatur dhe kufizime të dizajnit. Pa një dizajn që identifikon shkakun, përfundimi duhet të mbetet i bazuar në model dhe jo shkakor."
        exg.append(task(4,2,i,title,prompt));sog.append(task(4,2,i,title,solution))
    ex.append("".join(exg));sol.append("".join(sog))

    exg=[group_heading(3,titles[2])];sog=[group_heading(3,titles[2])]
    for i,(_title,_x,_y,n,r,sx,sy,crit,direction) in enumerate(CORRELATION_TESTS,1):
        title=labels[3][i-1];sign=">" if direction=="positive" else "<";boundary=crit if direction=="positive" else -crit;covariance=r*sx*sy;stat=r*math.sqrt((n-2)/(1-r*r));reject=stat>boundary if direction=="positive" else stat<boundary
        if locale=="de":
            prompt=rf"Eine hypothetische Stichprobe im Kontext «{title}» mit $n={n}$ ergibt die Stichprobenstandardabweichungen $s_x={number(sx,2)}$ und $s_y={number(sy,2)}$ sowie die Stichprobenkovarianz $s_{{xy}}={number(covariance,4)}$. Vor Einsicht in die Werte wurde $H_1:\rho{sign}0$ festgelegt. (a) Berechne Pearsons $r=s_{{xy}}/(s_xs_y)$ und formuliere $H_0$. (b) Berechne $t=r\sqrt{{(n-2)/(1-r^2)}}$ mit $df=n-2$. (c) Entscheide mit der einseitigen 5%-Grenze {'+' if direction=='positive' else '-'}{number(crit,4)}. (d) Interpretiere Vorzeichen, Stärke, statistische Evidenz und praktische Bedeutung getrennt."
            solution=rf"Zuerst gilt $r=s_{{xy}}/(s_xs_y)={number(covariance,4)}/[{number(sx,2)}({number(sy,2)})]={number(r,4)}$. Die Nullhypothese lautet $H_0:\rho=0$. Die Teststatistik ist $t={number(r,4)}\sqrt{{({n}-2)/(1-({number(r,4)})^2)}}={number(stat,4)}$ mit $df={n-2}$. Sie {'überschreitet' if reject else 'überschreitet nicht'} die gerichtete Grenze {number(boundary,4)}; deshalb {'lehnen wir' if reject else 'lehnen wir'} $H_0$ bei 5% {'ab' if reject else 'nicht ab'}. Der Stichprobenzusammenhang ist {'positiv' if r>0 else 'negativ'}: Grössere Werte der Prädiktorvariable treten im linearen Sinn tendenziell mit {'grösseren' if r>0 else 'kleineren'} Werten der Ergebnisvariable auf. Der Betrag $|r|={number(abs(r),2)}$ beschreibt den beobachteten linearen Zusammenhang. Statistische Evidenz hängt von $r$ und $n$ ab; praktische Bedeutung zusätzlich von Variablen, Folgen, Präzision und Design. Auch ein signifikanter Koeffizient würde keine Kausalität belegen."
        else:
            prompt=rf"Një kampion hipotetik në kontekstin «{title}» me $n={n}$ jep devijimet standarde të kampionit $s_x={number(sx,2)}$ dhe $s_y={number(sy,2)}$ dhe kovariancën e kampionit $s_{{xy}}={number(covariance,4)}$. Para se të shiheshin vlerat, alternativa e drejtuar u përcaktua si $H_1:\rho{sign}0$. (a) Llogarit $r=s_{{xy}}/(s_xs_y)$ të Pearson-it dhe shkruaj $H_0$. (b) Llogarit $t=r\sqrt{{(n-2)/(1-r^2)}}$ me $df=n-2$. (c) Merr vendimin me kufirin njëanësh 5% {'+' if direction=='positive' else '-'}{number(crit,4)}. (d) Interpreto veçmas shenjën, forcën, evidencën statistikore dhe rëndësinë praktike."
            solution=rf"Së pari, $r=s_{{xy}}/(s_xs_y)={number(covariance,4)}/[{number(sx,2)}({number(sy,2)})]={number(r,4)}$. Hipoteza zero është $H_0:\rho=0$. Statistika e testit është $t={number(r,4)}\sqrt{{({n}-2)/(1-({number(r,4)})^2)}}={number(stat,4)}$ me $df={n-2}$. Ajo {'e kalon' if reject else 'nuk e kalon'} kufirin e drejtuar {number(boundary,4)}, prandaj {'e refuzojmë' if reject else 'nuk e refuzojmë'} $H_0$ në 5%. Lidhja në kampion është {'pozitive' if r>0 else 'negative'}: vlerat më të mëdha të ndryshores parashikuese priren të shoqërohen me vlera {'më të mëdha' if r>0 else 'më të vogla'} të ndryshores së rezultatit në kuptimin linear. Madhësia $|r|={number(abs(r),2)}$ përshkruan lidhjen lineare të vrojtuar. Evidenca statistikore varet si nga $r$, ashtu edhe nga $n$, ndërsa rëndësia praktike varet edhe nga ndryshoret, pasojat, saktësia dhe dizajni. Edhe një koeficient domethënës nuk do të vendoste shkakësi."
        exg.append(task(4,3,i,title,prompt));sog.append(task(4,3,i,title,solution))
    ex.append("".join(exg));sol.append("".join(sog))

    exg=[group_heading(4,titles[3])];sog=[group_heading(4,titles[3])]
    for i,(_title,rx,ry) in enumerate(RANK_PAIRS,1):
        title=labels[4][i-1];n=len(rx);d=[a-b for a,b in zip(rx,ry)];sumd=sum(v*v for v in d);rho=1-6*sumd/(n*(n*n-1))
        if locale=="de":
            prompt=rf"Dieselben {n} Fälle haben die Rangvektoren $R_X={vector(rx)}$ und $R_Y={vector(ry)}$; Rang 1 bezeichnet bei jeder Variable den kleinsten Wert. (a) Berechne jede Differenz $d_i=R_{{Xi}}-R_{{Yi}}$ und $\sum d_i^2$. (b) Verwende $r_s=1-6\sum d_i^2/[n(n^2-1)]$. (c) Interpretiere Vorzeichen und Betrag als monotonen Rangzusammenhang und nicht als Unterschied in Messeinheiten."
            solution=rf"Die Rangdifferenzen sind $d={vector(d)}$; somit gilt $\sum d_i^2={sumd}$. Mit $n={n}$ ergibt sich $r_s=1-6({sumd})/[{n}({n}^2-1)]={number(rho,4)}$. Das {'positive' if rho>0 else 'negative'} Vorzeichen bedeutet, dass Fälle mit höheren Rängen bei einer Variable tendenziell {'höhere' if rho>0 else 'tiefere'} Ränge bei der anderen besitzen. Der Betrag $|r_s|={number(abs(rho),4)}$ beschreibt, wie einheitlich die Ordnung einer monotonen Richtung folgt. Weil Ränge die ursprünglichen Werte ersetzen, beschreibt das Ergebnis keine Steigung in Originaleinheiten."
        else:
            prompt=rf"Të njëjtat {n} raste kanë vektorët e renditjeve $R_X={vector(rx)}$ dhe $R_Y={vector(ry)}$, ku renditja 1 është vlera më e vogël për secilën ndryshore. (a) Llogarit secilin dallim $d_i=R_{{Xi}}-R_{{Yi}}$ dhe $\sum d_i^2$. (b) Përdor $r_s=1-6\sum d_i^2/[n(n^2-1)]$. (c) Interpreto shenjën dhe madhësinë si lidhje monotone renditjesh, jo si dallim në njësitë e matjes."
            solution=rf"Dallimet e renditjeve janë $d={vector(d)}$, prandaj $\sum d_i^2={sumd}$. Me $n={n}$, $r_s=1-6({sumd})/[{n}({n}^2-1)]={number(rho,4)}$. Shenja {'pozitive' if rho>0 else 'negative'} do të thotë se rastet me renditje më të lartë në njërën ndryshore priren të kenë renditje {'më të lartë' if rho>0 else 'më të ulët'} në tjetrën. Madhësia $|r_s|={number(abs(rho),4)}$ përshkruan sa njëtrajtshëm ndjek renditja një drejtim monoton. Meqë renditjet zëvendësojnë vlerat fillestare, rezultati nuk përshkruan pjerrësi në njësitë fillestare."
        exg.append(task(4,4,i,title,prompt));sog.append(task(4,4,i,title,solution))
    ex.append("".join(exg));sol.append("".join(sog))

    exg=[group_heading(5,titles[4])];sog=[group_heading(5,titles[4])]
    for i,(_title,x,y) in enumerate(MONOTONIC_CASES,1):
        title=labels[5][i-1];rp=pearson(x,y);ranks_x=midranks(x);ranks_y=midranks(y);rs=pearson(ranks_x,ranks_y);decreasing=y[-1]<y[0];x_mean=sample_mean(x);y_mean=sample_mean(y);original_cross=sum((a-x_mean)*(b-y_mean) for a,b in zip(x,y));original_x_ss=sum((a-x_mean)**2 for a in x);original_y_ss=sum((b-y_mean)**2 for b in y);rank_mean=sample_mean(ranks_x);rank_cross=sum((a-rank_mean)*(b-rank_mean) for a,b in zip(ranks_x,ranks_y));rank_x_ss=sum((a-rank_mean)**2 for a in ranks_x);rank_y_ss=sum((b-rank_mean)**2 for b in ranks_y);coordinates=", ".join(f"({a}, {b})" for a,b in zip(x,y))
        if locale=="de":
            prompt=rf"Die konstruierten Werte sind $X={vector(x)}$ und $Y={vector(y)}$. (a) Skizziere das Punktmuster oder beschreibe Richtung und Krümmung. (b) Berechne Pearsons $r$ aus den ursprünglichen Werten. (c) Bilde für beide Variablen Ränge und berechne Spearmans $r_s$. (d) Erkläre, weshalb sich die Koeffizienten unterscheiden, obwohl sich beide Variablen monoton bewegen."
            solution=rf"Die Koordinaten {coordinates} bilden eine {'fallende' if decreasing else 'steigende'} Kurve. Bei jeder Zunahme von $X$ {'nimmt' if decreasing else 'nimmt'} $Y$ {'ab' if decreasing else 'zu'}, aber das Ausmass der Veränderung ist nicht konstant. Für die Originalwerte gelten $\bar x={number(x_mean,4)}$, $\bar y={number(y_mean,4)}$, $S_{{xy}}={number(original_cross,4)}$, $S_{{xx}}={number(original_x_ss,4)}$ und $S_{{yy}}={number(original_y_ss,4)}$. Somit ist $r=S_{{xy}}/\sqrt{{S_{{xx}}S_{{yy}}}}={number(original_cross,4)}/\sqrt{{{number(original_x_ss,4)}({number(original_y_ss,4)})}}={number(rp,4)}$. Die Rangvektoren sind $R_X={vector(ranks_x)}$ und $R_Y={vector(ranks_y)}$, beide mit mittlerem Rang {number(rank_mean,1)}. Ihre Kreuzproduktsumme ist {number(rank_cross,4)}, die quadrierten Abweichungssummen sind {number(rank_x_ss,4)} und {number(rank_y_ss,4)}; deshalb $r_s={number(rank_cross,4)}/\sqrt{{{number(rank_x_ss,4)}({number(rank_y_ss,4)})}}={number(rs,4)}$. Spearman erreicht {'-1' if rs<0 else '1'}, weil die Ordnung perfekt monoton ist. Pearson hat einen kleineren Betrag, weil er die Nähe zu einer Geraden misst und auf die wechselnde Steigung reagiert."
        else:
            prompt=rf"Vlerat e krijuara janë $X={vector(x)}$ dhe $Y={vector(y)}$. (a) Skico modelin e pikave ose përshkruaj drejtimin dhe lakimin. (b) Llogarit $r$ të Pearson-it nga vlerat fillestare. (c) Rendit të dyja ndryshoret dhe llogarit $r_s$ të Spearman-it. (d) Shpjego pse koeficientët ndryshojnë edhe pse të dyja ndryshoret lëvizin në mënyrë monotone."
            solution=rf"Koordinatat {coordinates} japin një lakore {'zbritëse' if decreasing else 'rritëse'}. Çdo rritje e $X$ shoqërohet me {'ulje' if decreasing else 'rritje'} të $Y$, por sasia e ndryshimit nuk është konstante. Për vlerat fillestare, $\bar x={number(x_mean,4)}$, $\bar y={number(y_mean,4)}$, $S_{{xy}}={number(original_cross,4)}$, $S_{{xx}}={number(original_x_ss,4)}$ dhe $S_{{yy}}={number(original_y_ss,4)}$. Prandaj $r=S_{{xy}}/\sqrt{{S_{{xx}}S_{{yy}}}}={number(original_cross,4)}/\sqrt{{{number(original_x_ss,4)}({number(original_y_ss,4)})}}={number(rp,4)}$. Vektorët e renditjeve janë $R_X={vector(ranks_x)}$ dhe $R_Y={vector(ranks_y)}$, të dy me renditje mesatare {number(rank_mean,1)}. Shuma e prodhimeve të kryqëzuara është {number(rank_cross,4)}, ndërsa shumat e devijimeve në katror janë {number(rank_x_ss,4)} dhe {number(rank_y_ss,4)}, kështu që $r_s={number(rank_cross,4)}/\sqrt{{{number(rank_x_ss,4)}({number(rank_y_ss,4)})}}={number(rs,4)}$. Spearman-i arrin {'-1' if rs<0 else '1'} sepse renditja është plotësisht monotone. Pearson-i ka madhësi më të vogël sepse mat sa afër një vije të drejtë janë pikat dhe reagon ndaj pjerrësisë që ndryshon."
        exg.append(task(4,5,i,title,prompt));sog.append(task(4,5,i,title,solution))
    ex.append("".join(exg));sol.append("".join(sog))

    exg=[group_heading(6,titles[5])];sog=[group_heading(6,titles[5])]
    for i,(_title,x,y,a,b) in enumerate(TIED_CASES,1):
        title=labels[6][i-1];rx=midranks(x);ry=midranks(y);rs=pearson(rx,ry);transformed=[a+b*v for v in y];rst=pearson(rx,midranks(transformed));rank_mean=sample_mean(rx);rank_cross=sum((left-rank_mean)*(right-rank_mean) for left,right in zip(rx,ry));rank_x_ss=sum((value-rank_mean)**2 for value in rx);rank_y_ss=sum((value-rank_mean)**2 for value in ry)
        if locale=="de":
            prompt=rf"Acht Fälle haben $X={vector(x)}$ und $Y={vector(y)}$. (a) Weise jedem Block gebundener Werte mittlere Ränge zu und berechne Spearmans Korrelation als Pearson-Korrelation der zwei Rangspalten. (b) Transformiere die zweite Variable zu $Y^*={a}+{b}Y$. Erkläre vor der Neuberechnung, ob sich Ränge und $r_s$ verändern sollten. (c) Nenne den Unterschied bei einem negativen Multiplikator."
            solution=rf"Mittlere Ränge ergeben $R_X={vector(rx)}$ und $R_Y={vector(ry)}$. Beide Rangspalten haben den Mittelwert {number(rank_mean,1)}. Ihre Kreuzproduktsumme beträgt {number(rank_cross,4)}, ihre quadrierten Abweichungssummen {number(rank_x_ss,4)} und {number(rank_y_ss,4)}. Somit ist $r_s={number(rank_cross,4)}/\sqrt{{{number(rank_x_ss,4)}({number(rank_y_ss,4)})}}={number(rs,4)}$. Die Transformation $Y^*={a}+{b}Y$ hat einen positiven Multiplikator und erhält deshalb jede Reihenfolge und jede Bindung. Somit gelten $R_{{Y^*}}={vector(midranks(transformed))}$ und $r_s^*={number(rst,4)}$, also genau derselbe Koeffizient. Addition einer Konstante verändert die Lage, Multiplikation mit einer positiven Konstante die Skala; beides verändert die Ränge nicht. Ein negativer Multiplikator würde die Ordnung und damit das Vorzeichen von Spearmans Koeffizient umkehren."
        else:
            prompt=rf"Tetë raste kanë $X={vector(x)}$ dhe $Y={vector(y)}$. (a) Cakto renditjet mesatare për çdo bllok vlerash të barabarta dhe llogarit korrelacionin e Spearman-it si korrelacion Pearson të dy kolonave të renditjeve. (b) Transformo ndryshoren e dytë në $Y^*={a}+{b}Y$. Para rillogaritjes, shpjego nëse duhet të ndryshojnë renditjet dhe $r_s$. (c) Thuaj çfarë do të ndryshonte me shumëzues negativ."
            solution=rf"Renditjet mesatare japin $R_X={vector(rx)}$ dhe $R_Y={vector(ry)}$. Të dyja kolonat e renditjeve kanë mesatare {number(rank_mean,1)}. Shuma e prodhimeve të kryqëzuara është {number(rank_cross,4)}, ndërsa shumat e devijimeve në katror janë {number(rank_x_ss,4)} dhe {number(rank_y_ss,4)}. Prandaj $r_s={number(rank_cross,4)}/\sqrt{{{number(rank_x_ss,4)}({number(rank_y_ss,4)})}}={number(rs,4)}$. Transformimi $Y^*={a}+{b}Y$ ka shumëzues pozitiv, ndaj ruan çdo renditje dhe çdo barazim. Prandaj $R_{{Y^*}}={vector(midranks(transformed))}$ dhe $r_s^*={number(rst,4)}$, pikërisht i njëjti koeficient. Shtimi i një konstante ndryshon vendndodhjen dhe shumëzimi me konstante pozitive ndryshon shkallën, por asnjëri nuk ndryshon renditjet. Shumëzuesi negativ do ta përmbyste renditjen dhe shenjën e koeficientit të Spearman-it."
        exg.append(task(4,6,i,title,prompt));sog.append(task(4,6,i,title,solution))
    ex.append("".join(exg));sol.append("".join(sog))

    exg=[group_heading(7,titles[6])];sog=[group_heading(7,titles[6])]
    for i,(_title,_scenario,_units,_threats,_design) in enumerate(CLAIM_CASES,1):
        title=labels[7][i-1]
        scenario,units,threats,design=CLAIM_LOCALIZED[locale][i-1]
        if locale=="de":
            prompt=rf"Der folgende Bericht zum Kontext «{title}» wurde ausschliesslich für diese Übung erfunden und ist kein empirischer Befund: {scenario} (a) Bestimme Beobachtungseinheiten und Aussageebene. (b) Nenne mindestens drei konkrete Gefahren aus Messung, Stichprobenziehung, zeitlicher Reihenfolge, Aggregation oder Drittvariablen. (c) Formuliere das Ergebnis als vertretbare Zusammenhangsaussage. (d) Schlage Evidenz vor, die die kausale Frage glaubwürdiger beantworten würde."
            solution=rf"Die Beobachtungseinheiten und die Aussageebene sind: {units}. Der berichtete Vergleich stützt höchstens einen Zusammenhang auf dieser aufgezeichneten Ebene. Zu den zentralen Gefahren gehören {threats}. Vertretbar wäre die Aussage, dass die gemessenen Variablen in dieser Stichprobe oder diesem aggregierten Datensatz zusammenhingen, ohne zu behaupten, die eine habe die andere erzeugt oder jedes Individuum folge dem Gruppenmuster. Eine stärkere Untersuchung würde {design}. Zudem muss sie Stichprobenrahmen, fehlende Werte, Messqualität, zeitliche Reihenfolge und verbleibende Grenzen berichten. Kein Korrelationskoeffizient allein verwandelt einen beobachteten Vergleich in einen kausalen Effekt."
        else:
            prompt=rf"Raporti vijues për kontekstin «{title}» është trilluar vetëm për këtë ushtrim dhe nuk është pohim empirik: {scenario} (a) Përcakto njësitë e vrojtimit dhe nivelin e pohimit. (b) Rendit të paktën tri kërcënime konkrete që lidhen me matjen, kampionimin, rendin kohor, grumbullimin ose ndryshoret e treta. (c) Rishkruaje rezultatin si pohim të mbrojtshëm për lidhjen. (d) Propozo evidencë që do ta trajtonte më bindshëm pyetjen shkakore."
            solution=rf"Njësitë e vrojtimit dhe niveli i pohimit janë: {units}. Krahasimi i raportuar mbështet, në rastin më të mirë, një lidhje në atë nivel. Kërcënimet kryesore janë: {threats}. Një pohim i mbrojtshëm do të thoshte se ndryshoret e matura ishin të lidhura në këtë kampion ose grup të dhënash të agreguara, pa thënë se njëra e prodhoi tjetrën ose se çdo individ ndjek modelin e grupit. Një vlerësim më i fortë do të ishte: {design}. Duhet të raportohen edhe korniza e kampionimit, të dhënat që mungojnë, cilësia e matjes, rendi kohor dhe kufizimet e mbetura. Asnjë koeficient korrelacioni nuk e kthen vetë një krahasim vrojtues në efekt shkakor."
        exg.append(task(4,7,i,title,prompt));sog.append(task(4,7,i,title,solution))
    ex.append("".join(exg));sol.append("".join(sog));return ex,sol


def main() -> int:
    parser=argparse.ArgumentParser()
    parser.add_argument("--locale",choices=("en","de","sq"),default="en")
    args=parser.parse_args()
    exercises,solutions=render_localized(args.locale)
    write_pair(4,args.locale,7,exercises,solutions)
    validate_sources_allowing_incomplete_locales(args.locale, topic=4)
    print(f"Generated and source-validated Topic 4 {args.locale} exercise and solution sources.")
    return 0


if __name__=="__main__":
    raise SystemExit(main())
