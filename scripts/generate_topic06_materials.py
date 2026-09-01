#!/usr/bin/env python3
"""Generate Ratiomera's canonical English Topic 6 practice pair.

The two registered worksheet groups define the skills only. The residual
sequences, correlations, scenarios, questions, and worked explanations here
are newly authored. German and Albanian remain gated on English review.
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


RESIDUAL_CASES = [
    ("Practice and reasoning after prior score", [-3,-2,-1,0,1,2,3], [-2.0,-0.3,-1.4,0.8,0.2,2.1,1.0], 0.52, 0.48),
    ("Search time and accuracy after experience", [-3,-2,-1,0,1,2,3], [1.8,0.1,1.2,-0.8,0.2,-2.0,-0.5], -0.46, 0.55),
    ("Reading and comprehension after prior knowledge", [-4,-2,-1,0,1,2,4], [-1.5,-0.2,-1.1,1.0,0.3,2.0,0.5], 0.58, 0.44),
    ("Notifications and focus after workload", [-3,-2,-1,0,1,2,3], [1.4,0.0,1.3,-0.7,0.1,-1.8,-0.3], -0.51, 0.49),
    ("Museum visits and knowledge after education", [-4,-2,-1,0,1,2,4], [-1.0,0.2,-0.8,0.9,-0.2,1.7,0.4], 0.47, 0.53),
    ("Route familiarity and travel time after distance", [-3,-2,-1,0,1,2,3], [1.7,0.3,0.9,-1.0,0.4,-1.5,-0.8], -0.43, 0.60),
    ("Workshop attendance and confidence after baseline", [-4,-2,-1,0,1,2,4], [-1.7,-0.1,-0.8,0.7,0.2,1.9,0.8], 0.62, 0.40),
    ("Task switching and completion after task load", [-3,-2,-1,0,1,2,3], [1.2,-0.1,1.4,-0.6,0.3,-1.6,-0.6], -0.55, 0.45),
    ("Discussion posts and reasoning after engagement", [-4,-2,-1,0,1,2,4], [-1.4,0.0,-0.9,0.8,-0.1,1.6,0.9], 0.50, 0.57),
    ("Practice regularity and retention after study time", [-3,-2,-1,0,1,2,3], [-1.1,0.2,-1.4,0.9,0.0,1.5,0.7], 0.56, 0.46),
]


CONCEPT_CASES = [
    ("Practice, prior knowledge, and reasoning", "weekly practice", "reasoning score", "prior knowledge", 0.68, 0.34, "prior knowledge is positively related to both practice and reasoning, so part of the bivariate association reflects their shared connection with it"),
    ("Search time, experience, and accuracy", "search time", "accuracy", "archive experience", -0.57, -0.26, "experience tends to shorten searches and improve accuracy, creating part of the negative bivariate relationship"),
    ("Reading time, workload, and comprehension", "reading time", "comprehension", "course workload", 0.18, 0.41, "high workload is associated with more reading but lower comprehension, suppressing part of the positive adjusted relationship"),
    ("Notifications, task load, and focus", "notification count", "focus", "task load", -0.49, -0.20, "heavier task load can increase notifications and reduce focus, accounting for part of the raw negative association"),
    ("Museum visits, education, and knowledge", "museum visits", "historical knowledge", "education", 0.54, 0.29, "education may encourage visits and support historical knowledge, so the raw association partly reflects this common connection"),
    ("Route familiarity, distance, and travel time", "route familiarity", "travel time", "route distance", -0.21, -0.48, "longer routes can be more familiar yet still take longer, hiding part of the negative familiarity-time relationship"),
    ("Workshop attendance, baseline confidence, and final confidence", "attendance", "final confidence", "baseline confidence", 0.61, 0.25, "learners who begin more confident may attend more and also finish more confident"),
    ("Task switching, workload, and completion", "task switching", "completion score", "workload", -0.52, -0.28, "workload can increase switching and make completion harder, producing part of the raw negative relationship"),
    ("Discussion posts, engagement, and reasoning", "discussion posts", "reasoning score", "general engagement", 0.59, 0.19, "engagement may lead to both more posts and higher reasoning scores"),
    ("Practice regularity, total time, and retention", "practice regularity", "retention", "total study time", 0.33, 0.47, "total time is positively related to both variables but can also blur the distinct contribution of regular scheduling in the bivariate coefficient"),
]


RESIDUAL_TITLES = {
    "en": [case[0] for case in RESIDUAL_CASES],
    "de": [
        "Übungszeit und statistisches Denken nach Bereinigung um den Ausgangswert",
        "Suchzeit und Genauigkeit nach Bereinigung um die Archiverfahrung",
        "Lesezeit und Textverständnis nach Bereinigung um das Vorwissen",
        "Benachrichtigungen und Konzentration nach Bereinigung um die Arbeitslast",
        "Museumsbesuche und Wissen nach Bereinigung um den Bildungsstand",
        "Streckenkenntnis und Reisezeit nach Bereinigung um die Streckenlänge",
        "Workshopteilnahme und Selbstvertrauen nach Bereinigung um den Ausgangswert",
        "Aufgabenwechsel und Aufgabenerledigung nach Bereinigung um die Aufgabenlast",
        "Diskussionsbeiträge und statistisches Denken nach Bereinigung um das Engagement",
        "Regelmässigkeit des Übens und Behaltensleistung nach Bereinigung um die Lernzeit",
    ],
    "sq": [
        "Ushtrimi dhe arsyetimi pas përshtatjes për rezultatin paraprak",
        "Koha e kërkimit dhe saktësia pas përshtatjes për përvojën në arkiv",
        "Koha e leximit dhe të kuptuarit pas përshtatjes për njohuritë paraprake",
        "Njoftimet dhe përqendrimi pas përshtatjes për ngarkesën e punës",
        "Vizitat në muze dhe njohuritë pas përshtatjes për nivelin e arsimimit",
        "Njohja e rrugës dhe koha e udhëtimit pas përshtatjes për gjatësinë e rrugës",
        "Pjesëmarrja në seminar dhe vetëbesimi pas përshtatjes për nivelin fillestar",
        "Kalimi mes detyrave dhe përfundimi pas përshtatjes për ngarkesën e detyrave",
        "Postimet në diskutim dhe arsyetimi pas përshtatjes për angazhimin",
        "Rregullsia e ushtrimit dhe mbajtja mend pas përshtatjes për kohën e studimit",
    ],
}


CONCEPT_CASES_LOCALIZED = {
    "en": CONCEPT_CASES,
    "de": [
        ("Übungszeit, Vorwissen und statistisches Denken", "wöchentliche Übungszeit", "Punktwert im statistischen Denken", "Vorwissen", 0.68, 0.34, "Vorwissen kann sowohl mit der wöchentlichen Übungszeit als auch mit dem statistischen Denken positiv zusammenhängen. Deshalb kann ein Teil des bivariaten Zusammenhangs auf diesen beiden Verbindungen beruhen"),
        ("Suchzeit, Archiverfahrung und Genauigkeit", "Suchzeit", "Genauigkeit", "Archiverfahrung", -0.57, -0.26, "Mehr Archiverfahrung kann die Suchzeit verkürzen und zugleich die Genauigkeit erhöhen. Dadurch kann ein Teil des negativen bivariaten Zusammenhangs entstehen"),
        ("Lesezeit, Kursarbeitslast und Textverständnis", "Lesezeit", "Textverständnis", "Arbeitslast im Kurs", 0.18, 0.41, "Eine hohe Arbeitslast im Kurs kann mit mehr Lesezeit, aber geringerem Textverständnis einhergehen. Dadurch kann sie einen Teil des positiven bereinigten Zusammenhangs verdecken"),
        ("Benachrichtigungen, Aufgabenlast und Konzentration", "Anzahl der Benachrichtigungen", "Konzentration", "Aufgabenlast", -0.49, -0.20, "Eine höhere Aufgabenlast kann die Zahl der Benachrichtigungen erhöhen und die Konzentration senken. Dadurch kann ein Teil des rohen negativen Zusammenhangs entstehen"),
        ("Museumsbesuche, Bildungsstand und historisches Wissen", "Museumsbesuche", "historisches Wissen", "Bildungsstand", 0.54, 0.29, "Ein höherer Bildungsstand kann Museumsbesuche fördern und historisches Wissen unterstützen. Deshalb kann der rohe Zusammenhang teilweise auf diesen beiden Verbindungen beruhen"),
        ("Streckenkenntnis, Streckenlänge und Reisezeit", "Streckenkenntnis", "Reisezeit", "Streckenlänge", -0.21, -0.48, "Längere Strecken können vertrauter sein und trotzdem mehr Reisezeit beanspruchen. Dadurch kann ein Teil des negativen Zusammenhangs zwischen Streckenkenntnis und Reisezeit verdeckt werden"),
        ("Workshopteilnahme sowie anfängliches und abschliessendes Selbstvertrauen", "Workshopteilnahme", "abschliessendes Selbstvertrauen", "anfängliches Selbstvertrauen", 0.61, 0.25, "Lernende mit höherem anfänglichem Selbstvertrauen können häufiger an Workshops teilnehmen und auch mit höherem Selbstvertrauen abschliessen"),
        ("Aufgabenwechsel, Arbeitslast und Aufgabenerledigung", "Häufigkeit des Aufgabenwechsels", "Punktwert für die Aufgabenerledigung", "Arbeitslast", -0.52, -0.28, "Eine hohe Arbeitslast kann häufigere Aufgabenwechsel begünstigen und den Punktwert für die Aufgabenerledigung senken. Dadurch kann ein Teil des rohen negativen Zusammenhangs entstehen"),
        ("Diskussionsbeiträge, Engagement und statistisches Denken", "Anzahl der Diskussionsbeiträge", "Punktwert im statistischen Denken", "allgemeines Engagement", 0.59, 0.19, "Ein höheres allgemeines Engagement kann sowohl zu mehr Diskussionsbeiträgen als auch zu höheren Punktwerten im statistischen Denken führen"),
        ("Regelmässigkeit, gesamte Lernzeit und Behaltensleistung", "Regelmässigkeit des Übens", "Behaltensleistung", "gesamte Lernzeit", 0.33, 0.47, "Die gesamte Lernzeit kann mit beiden Variablen positiv zusammenhängen und dabei den eigenständigen Zusammenhang zwischen regelmässigem Üben und der Behaltensleistung im bivariaten Koeffizienten teilweise verdecken"),
    ],
    "sq": [
        ("Ushtrimi, njohuritë paraprake dhe arsyetimi", "ushtrimi javor", "rezultati i arsyetimit", "njohuritë paraprake", 0.68, 0.34, "Njohuritë paraprake mund të lidhen pozitivisht si me ushtrimin javor, ashtu edhe me rezultatin e arsyetimit. Prandaj, një pjesë e lidhjes bivariate mund të pasqyrojë lidhjen që të dyja ndryshoret kanë me njohuritë paraprake"),
        ("Koha e kërkimit, përvoja dhe saktësia", "koha e kërkimit", "saktësia", "përvoja në arkiv", -0.57, -0.26, "Përvoja në arkiv mund ta shkurtojë kohën e kërkimit dhe njëkohësisht ta rrisë saktësinë. Kështu mund të krijohet një pjesë e lidhjes negative bivariate"),
        ("Koha e leximit, ngarkesa dhe të kuptuarit", "koha e leximit", "të kuptuarit e tekstit", "ngarkesa e kursit", 0.18, 0.41, "Ngarkesa e lartë e kursit mund të shoqërohet me më shumë kohë leximi, por me të kuptuar më të ulët. Kështu mund të fshihet një pjesë e lidhjes pozitive të përshtatur"),
        ("Njoftimet, ngarkesa e detyrave dhe përqendrimi", "numri i njoftimeve", "përqendrimi", "ngarkesa e detyrave", -0.49, -0.20, "Ngarkesa më e madhe e detyrave mund ta rrisë numrin e njoftimeve dhe ta ulë përqendrimin. Kështu mund të krijohet një pjesë e lidhjes së papërshtatur negative"),
        ("Vizitat në muze, arsimimi dhe njohuritë", "vizitat në muze", "njohuritë historike", "niveli i arsimimit", 0.54, 0.29, "Niveli i arsimimit mund t'i nxisë vizitat në muze dhe t'i mbështesë njohuritë historike. Prandaj, lidhja e papërshtatur mund të pasqyrojë pjesërisht të dyja këto lidhje"),
        ("Njohja e rrugës, gjatësia dhe koha e udhëtimit", "njohja e rrugës", "koha e udhëtimit", "gjatësia e rrugës", -0.21, -0.48, "Rrugët më të gjata mund të njihen më mirë, por prapë të kërkojnë më shumë kohë udhëtimi. Kështu mund të fshihet një pjesë e lidhjes negative mes njohjes së rrugës dhe kohës së udhëtimit"),
        ("Pjesëmarrja, vetëbesimi fillestar dhe ai përfundimtar", "pjesëmarrja në seminar", "vetëbesimi përfundimtar", "vetëbesimi fillestar", 0.61, 0.25, "Ata që fillojnë me më shumë vetëbesim mund të marrin pjesë më shpesh në seminar dhe ta përfundojnë atë me më shumë vetëbesim"),
        ("Kalimi mes detyrave, ngarkesa dhe përfundimi", "kalimi mes detyrave", "rezultati i përfundimit", "ngarkesa e punës", -0.52, -0.28, "Ngarkesa e madhe e punës mund ta shtojë kalimin mes detyrave dhe ta vështirësojë përfundimin. Kështu mund të krijohet një pjesë e lidhjes së papërshtatur negative"),
        ("Postimet në diskutim, angazhimi dhe arsyetimi", "numri i postimeve në diskutim", "rezultati i arsyetimit", "angazhimi i përgjithshëm", 0.59, 0.19, "Angazhimi i përgjithshëm mund të sjellë si më shumë postime në diskutim, ashtu edhe rezultate më të larta arsyetimi"),
        ("Rregullsia, koha totale e studimit dhe mbajtja mend", "rregullsia e ushtrimit", "mbajtja mend", "koha totale e studimit", 0.33, 0.47, "Koha totale e studimit mund të lidhet pozitivisht me të dyja ndryshoret. Kjo mund ta fshehë pjesërisht lidhjen e veçantë mes një orari të rregullt ushtrimi dhe mbajtjes mend"),
    ],
}


GROUP_TITLES = {
    "en": ("Partial Correlation by Residualization and by Formula", "Comparing Bivariate and Partial Correlation"),
    "de": ("Partielle Korrelation mit Residualisierung und direkter Formel", "Bivariate und partielle Korrelation vergleichen"),
    "sq": ("Korrelacioni i pjesshëm me rezidualizim dhe me formulën e drejtpërdrejtë", "Krahasimi i korrelacionit bivariat me atë të pjesshëm"),
}


def centered(values: list[float]) -> list[float]:
    mean=sample_mean(values)
    return [value-mean for value in values]


def vector(values: list[float]) -> str:
    return "("+", ".join(number(v,3) for v in values)+")"


def render_english()->tuple[list[str],list[str]]:
    ex=[];sol=[]
    exg=[group_heading(1,"Partial Correlation by Residualization and by Formula")]
    sog=[group_heading(1,"Partial Correlation by Residualization and by Formula")]
    for i,(title,xraw,yraw,rxz,ryz) in enumerate(RESIDUAL_CASES,1):
        x=centered(xraw);y=centered(yraw);rp=pearson(x,y);rxy=rp*math.sqrt((1-rxz*rxz)*(1-ryz*ryz))+rxz*ryz
        exg.append(task(6,1,i,title,f"After separately regressing focal variables $X$ and $Y$ on control variable $Z$, the residual columns are $e_X={vector(x)}$ and $e_Y={vector(y)}$. The original pairwise correlations are $r_{{XZ}}={number(rxz,4)}$, $r_{{YZ}}={number(ryz,4)}$, and $r_{{XY}}={number(rxy,4)}$. (a) Calculate the Pearson correlation between the two residual columns. (b) Verify it with $r_{{XY\\cdot Z}}=(r_{{XY}}-r_{{XZ}}r_{{YZ}})/\\sqrt{{(1-r_{{XZ}}^2)(1-r_{{YZ}}^2)}}$. (c) Explain in plain language what has been removed and what the remaining coefficient describes."))
        cross=sum(a*b for a,b in zip(x,y));ssx=sum(a*a for a in x);ssy=sum(b*b for b in y);formula=(rxy-rxz*ryz)/math.sqrt((1-rxz*rxz)*(1-ryz*ryz))
        sog.append(task(6,1,i,title,f"Both residual columns have mean zero apart from displayed rounding. Their cross-product sum is $\\sum e_Xe_Y={number(cross,4)}$, while $\\sum e_X^2={number(ssx,4)}$ and $\\sum e_Y^2={number(ssy,4)}$. Thus $r(e_X,e_Y)={number(cross,4)}/\\sqrt{{{number(ssx,4)}({number(ssy,4)})}}={number(rp,4)}$. The direct formula gives $[{number(rxy,4)}-({number(rxz,4)})({number(ryz,4)})]/\\sqrt{{[1-({number(rxz,4)})^2][1-({number(ryz,4)})^2]}}={number(formula,4)}$. Small differences can arise if the displayed correlations are rounded before substitution. Each residual is the part of its focal variable not linearly predicted by $Z$. Their correlation describes how those remaining parts move together. It is still an adjusted association, not automatically a causal effect."))
    ex.append("".join(exg));sol.append("".join(sog))

    exg=[group_heading(2,"Comparing Bivariate and Partial Correlation")]
    sog=[group_heading(2,"Comparing Bivariate and Partial Correlation")]
    for i,(title,x,y,z,raw,partial,mechanism) in enumerate(CONCEPT_CASES,1):
        direction="weaker" if abs(partial)<abs(raw) else "stronger"
        exg.append(task(6,2,i,title,f"A hypothetical study reports the bivariate correlation $r_{{XY}}={number(raw,2)}$ between {x} and {y}. After linear adjustment for {z}, it reports $r_{{XY\\cdot Z}}={number(partial,2)}$. (a) Draw a three-variable diagram that could make this change plausible. (b) Compare the signs and magnitudes and say whether adjustment weakened or strengthened the coefficient. (c) Explain the residual interpretation. (d) State why neither coefficient by itself identifies a causal effect. (e) Explain what information you would need before defending {z} as a control variable, and name one limitation of a linear adjustment."))
        sog.append(task(6,2,i,title,f"One plausible diagram is **Z → X, Z → Y, and X ↔ Y**. It connects {z} with both {x} and {y}; the focal $X$-$Y$ link remains a separate association. In this setting, {mechanism}. The coefficient changes from {number(raw,2)} to {number(partial,2)}, so adjustment makes the absolute association {direction}. Residualization first predicts {x} from {z} and predicts {y} from {z}; the partial correlation is the correlation between what remains in those two columns. A smaller coefficient suggests that the control variable accounts for part of the bivariate pattern. A larger coefficient suggests suppression, where adjustment reveals a relationship that was partly hidden. Neither result establishes time order, rules out unmeasured variables, repairs measurement error, or replaces experimental control. Defending {z} as a control requires subject-matter and research-design reasons, including a plausible time order and a clear account of the role assigned to the variable. The coefficients alone cannot supply that justification. Linear adjustment can remove only the fitted linear component under the stated model, so nonlinear structure, measurement problems, and relevant unmeasured variables may remain."))
    ex.append("".join(exg));sol.append("".join(sog));return ex,sol


def render_localized(locale: str)->tuple[list[str],list[str]]:
    """Render the reviewed German or Albanian adaptation from shared values."""

    if locale == "en":
        return render_english()
    if locale not in ("de", "sq"):
        raise ValueError(f"unsupported locale: {locale}")

    ex=[];sol=[]
    exg=[group_heading(1,GROUP_TITLES[locale][0])]
    sog=[group_heading(1,GROUP_TITLES[locale][0])]
    for i,((_,xraw,yraw,rxz,ryz),title) in enumerate(zip(RESIDUAL_CASES,RESIDUAL_TITLES[locale]),1):
        x=centered(xraw);y=centered(yraw);rp=pearson(x,y);rxy=rp*math.sqrt((1-rxz*rxz)*(1-ryz*ryz))+rxz*ryz
        cross=sum(a*b for a,b in zip(x,y));ssx=sum(a*a for a in x);ssy=sum(b*b for b in y);formula=(rxy-rxz*ryz)/math.sqrt((1-rxz*rxz)*(1-ryz*ryz))
        if locale == "de":
            prompt=rf"Nachdem die beiden interessierenden Variablen $X$ und $Y$ getrennt auf die Kontrollvariable $Z$ regressiert wurden, lauten die Residualspalten $e_X={vector(x)}$ und $e_Y={vector(y)}$. Die ursprünglichen paarweisen Korrelationen sind $r_{{XZ}}={number(rxz,4)}$, $r_{{YZ}}={number(ryz,4)}$ und $r_{{XY}}={number(rxy,4)}$. (a) Berechne die Pearson-Korrelation zwischen den beiden Residualspalten. (b) Überprüfe das Ergebnis mit $r_{{XY\cdot Z}}=(r_{{XY}}-r_{{XZ}}r_{{YZ}})/\sqrt{{(1-r_{{XZ}}^2)(1-r_{{YZ}}^2)}}$. (c) Erkläre in einfachen Worten, welche linearen Anteile bei der Bereinigung entfernt wurden und was der verbleibende Koeffizient beschreibt."
            solution=rf"Abgesehen von der dargestellten Rundung haben beide Residualspalten den Mittelwert null. Ihre Kreuzproduktsumme beträgt $\sum e_Xe_Y={number(cross,4)}$, während $\sum e_X^2={number(ssx,4)}$ und $\sum e_Y^2={number(ssy,4)}$ gelten. Somit ist $r(e_X,e_Y)={number(cross,4)}/\sqrt{{{number(ssx,4)}({number(ssy,4)})}}={number(rp,4)}$. Die direkte Formel ergibt $[{number(rxy,4)}-({number(rxz,4)})({number(ryz,4)})]/\sqrt{{[1-({number(rxz,4)})^2][1-({number(ryz,4)})^2]}}={number(formula,4)}$. Kleine Unterschiede können entstehen, wenn die dargestellten Korrelationen vor dem Einsetzen in die Formel gerundet werden. Jedes Residuum ist die Differenz zwischen dem beobachteten Wert und dem Wert derselben Variable, der aus $Z$ linear vorhergesagt wurde. Die Korrelation der beiden Residualspalten beschreibt, wie sich diese verbleibenden Abweichungen gemeinsam bewegen. Sie bleibt ein bereinigter Zusammenhang und ist nicht automatisch ein kausaler Effekt."
        else:
            prompt=rf"Pasi ndryshoret kryesore $X$ dhe $Y$ regresohen veçmas mbi ndryshoren e kontrollit $Z$, kolonat e rezidualeve janë $e_X={vector(x)}$ dhe $e_Y={vector(y)}$. Korrelacionet fillestare bivariate janë $r_{{XZ}}={number(rxz,4)}$, $r_{{YZ}}={number(ryz,4)}$ dhe $r_{{XY}}={number(rxy,4)}$. (a) Llogarit korrelacionin e Pearson-it mes dy kolonave të rezidualeve. (b) Verifikoje rezultatin me $r_{{XY\cdot Z}}=(r_{{XY}}-r_{{XZ}}r_{{YZ}})/\sqrt{{(1-r_{{XZ}}^2)(1-r_{{YZ}}^2)}}$. (c) Shpjego me fjalë të thjeshta cilat pjesë lineare janë hequr gjatë përshtatjes dhe çfarë përshkruan koeficienti i mbetur."
            solution=rf"Përveç rrumbullakimit të paraqitur, të dyja kolonat e rezidualeve kanë mesatare zero. Shuma e prodhimeve të kryqëzuara është $\sum e_Xe_Y={number(cross,4)}$, ndërsa $\sum e_X^2={number(ssx,4)}$ dhe $\sum e_Y^2={number(ssy,4)}$. Prandaj $r(e_X,e_Y)={number(cross,4)}/\sqrt{{{number(ssx,4)}({number(ssy,4)})}}={number(rp,4)}$. Formula e drejtpërdrejtë jep $[{number(rxy,4)}-({number(rxz,4)})({number(ryz,4)})]/\sqrt{{[1-({number(rxz,4)})^2][1-({number(ryz,4)})^2]}}={number(formula,4)}$. Mund të shfaqen dallime të vogla nëse korrelacionet e paraqitura rrumbullakosen para se të zëvendësohen në formulë. Çdo rezidual është diferenca mes vlerës së vrojtuar dhe vlerës së përshtatur nga regresioni linear mbi $Z$ për të njëjtën ndryshore. Korrelacioni mes dy kolonave të rezidualeve përshkruan si lëvizin së bashku këto shmangie të mbetura. Ai mbetet një lidhje e përshtatur dhe nuk është vetvetiu efekt shkakor."
        exg.append(task(6,1,i,title,prompt));sog.append(task(6,1,i,title,solution))
    ex.append("".join(exg));sol.append("".join(sog))

    exg=[group_heading(2,GROUP_TITLES[locale][1])]
    sog=[group_heading(2,GROUP_TITLES[locale][1])]
    for i,(title,x,y,z,raw,partial,mechanism) in enumerate(CONCEPT_CASES_LOCALIZED[locale],1):
        if locale == "de":
            direction="kleiner" if abs(partial)<abs(raw) else "grösser"
            prompt=rf"Eine hypothetische Studie berichtet die bivariate Korrelation $r_{{XY}}={number(raw,2)}$ zwischen den Variablen **«{x}»** und **«{y}»**. Nach der linearen Bereinigung um die Variable **«{z}»** berichtet sie die partielle Korrelation $r_{{XY\cdot Z}}={number(partial,2)}$. (a) Zeichne ein Diagramm mit drei Variablen, das diese Veränderung plausibel machen könnte. (b) Vergleiche Vorzeichen und Beträge und sage, ob die Bereinigung den Zusammenhang abgeschwächt oder verstärkt hat. (c) Erkläre die Residualinterpretation. (d) Begründe, weshalb keiner der beiden Koeffizienten für sich allein einen kausalen Effekt identifiziert. (e) Erkläre, welche Informationen du benötigst, bevor du **«{z}»** als Kontrollvariable begründest, und nenne eine Grenze der linearen Bereinigung."
            solution=rf"Ein plausibles Diagramm lautet **Z → X, Z → Y und X ↔ Y**. Es verbindet die Variable **«{z}»** sowohl mit **«{x}»** als auch mit **«{y}»**; die separate $X$-$Y$-Verbindung bleibt ein eigener Zusammenhang. Eine mögliche inhaltliche Erklärung lautet: {mechanism}. Der Koeffizient verändert sich von {number(raw,2)} zu {number(partial,2)}. Sein Betrag ist nach der Bereinigung {direction}. Bei der Residualisierung wird zuerst die Variable **«{x}»** aus **«{z}»** vorhergesagt und danach die Variable **«{y}»** aus **«{z}»**. Die partielle Korrelation ist die Korrelation zwischen den Abweichungen, die in diesen beiden Residualspalten verbleiben. Ein kleinerer Betrag deutet darauf hin, dass die Kontrollvariable einen Teil des bivariaten Musters beschreibt. Ein grösserer Betrag deutet auf Suppression hin: Die Bereinigung macht dann einen zuvor teilweise verdeckten Zusammenhang sichtbar. Keines der Ergebnisse stellt die zeitliche Reihenfolge her, schliesst nicht gemessene Variablen aus, behebt Messfehler oder ersetzt experimentelle Kontrolle. Die Begründung von **«{z}»** als Kontrollvariable braucht fachliche und forschungsplanerische Argumente, darunter eine plausible zeitliche Reihenfolge und eine klare Rolle der Variable. Die Koeffizienten allein liefern diese Begründung nicht. Eine lineare Bereinigung entfernt nur den angepassten linearen Anteil im angegebenen Modell. Nichtlineare Strukturen, Messprobleme und relevante nicht gemessene Variablen können bestehen bleiben."
        else:
            direction="më e vogël" if abs(partial)<abs(raw) else "më e madhe"
            prompt=rf"Një studim hipotetik raporton korrelacionin bivariat $r_{{XY}}={number(raw,2)}$ mes ndryshoreve **«{x}»** dhe **«{y}»**. Pas përshtatjes lineare për ndryshoren **«{z}»**, studimi raporton korrelacionin e pjesshëm $r_{{XY\cdot Z}}={number(partial,2)}$. (a) Vizato një diagram me tri ndryshore që mund ta bëjë të besueshëm këtë ndryshim. (b) Krahaso shenjat dhe madhësitë dhe thuaj nëse përshtatja e dobësoi apo e forcoi lidhjen. (c) Shpjego interpretimin përmes rezidualeve. (d) Trego pse asnjëri koeficient, i marrë veçmas, nuk identifikon një efekt shkakor. (e) Shpjego cilat informacione të duhen para se ta arsyetosh **«{z}»** si ndryshore kontrolli dhe emërto një kufizim të përshtatjes lineare."
            solution=rf"Një diagram i besueshëm është **Z → X, Z → Y dhe X ↔ Y**. Ai e lidh ndryshoren **«{z}»** si me **«{x}»**, ashtu edhe me **«{y}»**; lidhja e veçantë $X$-$Y$ mbetet një marrëdhënie më vete. Një shpjegim i mundshëm është ky: {mechanism}. Koeficienti ndryshon nga {number(raw,2)} në {number(partial,2)}. Vlera e tij absolute pas përshtatjes është {direction}. Gjatë rezidualizimit, fillimisht parashikohet ndryshorja **«{x}»** nga **«{z}»** dhe pastaj parashikohet ndryshorja **«{y}»** nga **«{z}»**. Korrelacioni i pjesshëm është korrelacioni mes shmangieve që mbeten në këto dy kolona rezidualesh. Një vlerë absolute më e vogël sugjeron se ndryshorja e kontrollit përshkruan një pjesë të modelit bivariat. Një vlerë absolute më e madhe sugjeron shtypje: përshtatja nxjerr në pah një lidhje që më parë ishte pjesërisht e fshehur. Asnjëri rezultat nuk vendos rendin kohor, nuk përjashton ndryshore të pamatura, nuk ndreq gabimet e matjes dhe nuk zëvendëson kontrollin eksperimental. Arsyetimi i **«{z}»** si ndryshore kontrolli kërkon arsye nga fusha dhe plani i studimit, duke përfshirë një rend kohor të besueshëm dhe një rol të qartë për ndryshoren. Vetëm koeficientët nuk e japin këtë arsyetim. Përshtatja lineare heq vetëm pjesën lineare të përshtatur në modelin e deklaruar. Struktura jolineare, problemet e matjes dhe ndryshoret përkatëse të pamatura mund të mbeten."
        exg.append(task(6,2,i,title,prompt));sog.append(task(6,2,i,title,solution))
    ex.append("".join(exg));sol.append("".join(sog));return ex,sol


def main()->int:
    parser=argparse.ArgumentParser();parser.add_argument("--locale",choices=("en","de","sq"),default="en");args=parser.parse_args()
    exercises,solutions=render_localized(args.locale);write_pair(6,args.locale,2,exercises,solutions);validate_sources_allowing_incomplete_locales(args.locale,topic=6)
    print(f"Generated and source-validated Topic 6 {args.locale} exercise and solution sources.");return 0


if __name__=="__main__":raise SystemExit(main())
