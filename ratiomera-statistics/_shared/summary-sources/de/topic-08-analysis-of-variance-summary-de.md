---
title: "Varianzanalyse"
subtitle: "Gruppenmittelwerte durch die Zerlegung der Zielvariablenstreuung vergleichen"
document-id: "topic-08-analysis-of-variance-summary-de"
course-id: "intro-statistics"
topic-id: "topic-08-analysis-of-variance"
topic-number: "08"
topic-slug: "analysis-of-variance"
document-type: "summary"
locale: "de"
figure-asset: "topic-08-analysis-of-variance-summary-figure-de.png"
---

## Zweck und Grundlagen

Die Varianzanalyse, abgekürzt ANOVA, vergleicht mittlere Ergebnisse zwischen Gruppen, indem sie die Streuung untersucht. Der Name kann überraschen, weil sich die Forschungsfrage auf Mittelwerte bezieht. Das Verfahren trennt die Gesamtvariation der Zielvariable in einen mit Gruppenunterschieden verbundenen Teil und einen Teil, der zwischen Fällen innerhalb derselben Gruppen verbleibt. Ist die gruppenbezogene Komponente im Verhältnis zur Residualvariation gross, liefern die Daten Evidenz dafür, dass nicht alle Populationsmittelwerte der Gruppen gleich sind.

Bei einer einfaktoriellen ANOVA mit unabhängigen Gruppen gibt es einen kategorialen Faktor und eine numerische Zielvariable. Ein **Faktor** ist ein kategorialer Prädiktor. Seine Kategorien werden als **Stufen** bezeichnet. Jeder Fall gehört zu einer Stufe, und in den verschiedenen Gruppen befinden sich verschiedene Fälle. Die Nullhypothese besagt, dass alle Populationsmittelwerte der Gruppen gleich sind. Die Alternative besagt, dass nicht alle Populationsmittelwerte gleich sind, also dass sich mindestens zwei unterscheiden. Das Verwerfen der Nullhypothese zeigt weder, welche Gruppen sich unterscheiden, noch wie gross diese Unterschiede sind.

Beginne mit dem Design. Bestimme die Beobachtungs- oder Versuchseinheit, die Faktorstufen, die Zielvariable und ihr Skalenniveau sowie die Frage, ob Beobachtungen unabhängig oder wiederholt sind. Stelle die Zielvariable nach Gruppen grafisch dar und berichte Stichprobengrössen, Mittelwerte, Standardabweichungen und Intervalle der Gruppen. Eine Teststatistik kann eine fehlende Übereinstimmung zwischen Design und Modell nicht beheben.

| ANOVA-Grösse | Was sie erfasst | Freiheitsgrade bei einem einfaktoriellen Design |
|---|---|---|
| Gesamtquadratsumme | Quadrierte Abweichung jedes Falles vom Gesamtmittelwert | $N-1$ |
| Faktorquadratsumme | Mit der Gruppengrösse gewichtete Abweichungen der Gruppenmittelwerte vom Gesamtmittelwert | $k-1$ |
| Fehlerquadratsumme | Individuelle Abweichungen von den jeweiligen Gruppenmittelwerten | $N-k$ |
| Mittleres Quadrat | Quadratsumme geteilt durch ihre Freiheitsgrade | Hängt von der Komponente ab |

## Zentrale Ideen

Der **Gesamtmittelwert** ist der Mittelwert über alle Beobachtungen. Die Gesamtquadratsumme misst, wie weit jeder Wert der Zielvariable von diesem Gesamtmittelwert entfernt liegt. Die Faktorquadratsumme fragt, wie weit jeder Gruppenmittelwert vom Gesamtmittelwert entfernt liegt, und gewichtet diesen quadrierten Abstand mit der Gruppengrösse. Die Fehlerquadratsumme misst, wie weit jede Beobachtung von ihrem eigenen Gruppenmittelwert entfernt liegt. Im gewöhnlichen einfaktoriellen Modell mit Achsenabschnitt addieren sich Faktor- und Fehlerquadratsumme genau zur Gesamtquadratsumme.

Quadratsummen wachsen mit der Stichprobengrösse und berücksichtigen nicht, wie viele unabhängige Informationsbestandteile verwendet wurden. Wird jede Komponente durch ihre Freiheitsgrade geteilt, entsteht ein mittleres Quadrat. Die $F$-Statistik teilt das mittlere Quadrat des Faktors durch das mittlere Quadrat des Fehlers. Unter der Nullhypothese und den Modellannahmen schätzen beide dieselbe Fehlervarianz auf verschiedene Weise. Ein Verhältnis nahe eins ist daher plausibel. Ein grosses Verhältnis zeigt, dass die Trennung der Gruppenmittelwerte im Verhältnis zur typischen Variation innerhalb der Gruppen gross ist.

| Weiterführende Frage | Geeignetes Werkzeug | Schwerpunkt der Interpretation |
|---|---|---|
| Unterscheidet sich ein geplanter wissenschaftlicher Vergleich? | Geplanter Kontrast | Der festgelegte gewichtete Mittelwertvergleich und seine Unsicherheit |
| Welche Paare unterscheiden sich nach einem Omnibusergebnis? | Für Multiplizität korrigierte Paarvergleiche | Paardifferenzen mit gleichzeitiger Fehlerkontrolle |
| Wie soll die Omnibusanalyse dokumentiert werden? | Vollständige ANOVA-Tabelle | Quadratsummen, Freiheitsgrade, mittlere Quadrate, $F$ und p-Wert |
| Hängt das Muster eines Faktors von einem anderen ab? | Faktorielle ANOVA mit Interaktion | Differenzen von Differenzen anstelle isolierter Haupteffekte |

Mehrere nicht korrigierte Tests erhöhen die Wahrscheinlichkeit mindestens eines Fehlers 1. Art innerhalb einer Familie von Vergleichen. Eine Omnibus-ANOVA kontrolliert eine einzige Gesamtfrage, ersetzt aber keine sorgfältig gewählten Folgeanalysen. Geplante Kontraste sollten aus der Forschungsfrage hervorgehen. Post-hoc-Verfahren für Paarvergleiche verwenden eine Korrektur, die auf die interpretierte Familie abgestimmt ist. Berichte die geschätzten Mittelwertdifferenzen oder Kontraste, ihre Unsicherheit und korrigierte p-Werte.

Eine faktorielle ANOVA enthält mehr als einen Faktor. Haupteffekte fassen die mittleren Unterschiede eines Faktors über die Stufen des anderen Faktors zusammen. Eine Interaktion fragt, ob sich der Effekt eines Faktors über die Stufen des anderen Faktors verändert. Wenn eine Interaktion inhaltlich bedeutsam ist, solltest du bedingte Gruppenmittelwerte und Kontraste interpretieren, statt dich allein auf Haupteffekte zu stützen.

Daten mit Messwiederholung benötigen ein Modell, das berücksichtigt, dass mehrere Beobachtungen zur selben Person oder Einheit gehören. Diese Beobachtungen sind korreliert und dürfen nicht wie unabhängige Gruppen behandelt werden. Sphärizität ist eine Bedingung bei Messwiederholungen und betrifft die Varianzen der paarweisen Differenzen zwischen den Stufen. Ist sie nicht plausibel, wird eine Korrektur der Freiheitsgrade oder ein geeignetes Modell für wiederholte Daten benötigt. Aus der Perspektive zufälliger Effekte wird die Variation zwischen Clustern oder Personen von der Variation innerhalb dieser Einheiten getrennt. Die Intraklassenkorrelation fasst zusammen, wie stark sich Beobachtungen aus demselben Cluster ähneln.

Das gewöhnliche Modell mit unabhängigen Gruppen setzt unabhängige Beobachtungen, eine geeignete Mittelwertstruktur und Residualvarianzen voraus, die für die beabsichtigte $F$-Inferenz angemessen sind. Residualdiagnosen und Gruppendarstellungen sind wichtig. Bei ungleichen Varianzen und Gruppengrössen kann der gewöhnliche Test mit zusammengefasster Fehlervarianz ungeeignet sein. Die Reaktion darauf sollte dem Design und dem im Material festgelegten Verfahren folgen und nicht in einer automatischen Transformation oder im Löschen von Fällen bestehen.

## Formelleitfaden

Das einfaktorielle Modell schreibt jeden Wert der Zielvariable als Gesamtmittelwert, Gruppeneffekt und individuellen Fehler:

$$
Y_{ij}=\mu+\alpha_j+\varepsilon_{ij}
$$

Dabei bezeichnet $i$ einen Fall innerhalb der Gruppe $j$, $\mu$ ist die Gesamtreferenz, $\alpha_j$ die Gruppenkomponente und $\varepsilon_{ij}$ die Residualvariation. Die Gesamtquadratsumme lautet:

$$
SS_{\text{total}}=\sum_{j=1}^{k}\sum_{i=1}^{n_j}(y_{ij}-\bar{y})^2
$$

Ihre exakte Zerlegung ist:

$$
SS_{\text{total}}=SS_{\text{factor}}+SS_{\text{error}}
$$

Die beiden Komponenten werden wie folgt berechnet:

$$
SS_{\text{factor}}=\sum_{j=1}^{k}n_j(\bar{y}_j-\bar{y})^2,\qquad
SS_{\text{error}}=\sum_{j=1}^{k}\sum_{i=1}^{n_j}(y_{ij}-\bar{y}_j)^2
$$

Die mittleren Quadrate teilen durch die jeweiligen Freiheitsgrade, und der Omnibustest vergleicht sie:

$$
F=\frac{MS_{\text{factor}}}{MS_{\text{error}}}
=\frac{SS_{\text{factor}}/(k-1)}{SS_{\text{error}}/(N-k)}
$$

Bei genau zwei unabhängigen Gruppen sind dieser einfaktorielle Test mit festen Effekten und der zweiseitige t-Test für unabhängige Stichproben mit zusammengefasster Varianz nur dann äquivalent, wenn sie dasselbe Modell mit gleichen Varianzen verwenden:

$$
F(1,N-2)=t(N-2)^2.
$$

Das Omnibusergebnis koordiniert den Gruppenvergleich, zeigt aber nicht, welche Mittelwerte sich unterscheiden. Ein gezielter **Kontrast** kombiniert Gruppenmittelwerte mit Gewichten, deren Summe null ergibt:

$$
D=\sum_{i=1}^{k}c_i\bar y_i,
\qquad
\sum_{i=1}^{k}c_i=0.
$$

Positive und negative Gewichte stellen die Stufen auf gegenüberliegende Seiten des beabsichtigten Vergleichs. Bei einem balancierten Design mit $n$ Fällen in jeder Stufe lautet die im bereitgestellten Material verwendete Kontrastberechnung:

$$
SS_D=\frac{nD^2}{\sum_i c_i^2},
\qquad
F_D=\frac{SS_D}{MS_{\text{error}}},
$$

mit 1 Freiheitsgrad im Zähler und den Fehlerfreiheitsgraden des Omnibustests im Nenner. Ein Vergleich ist nur dann geplant, wenn seine Gewichte festgelegt wurden, bevor die Ergebnisse betrachtet wurden.

Die Anzahl verschiedener Paare unter $k$ Stufen beträgt:

$$
m=\frac{k(k-1)}{2}.
$$

Bei $m$ voneinander unabhängigen Tests mit einer testbezogenen Wahrscheinlichkeit eines Fehlers 1. Art von jeweils $\alpha_{\text{test}}$ ist die exakte familienweise Fehlerrate:

$$
\alpha_{\text{family}}
=1-(1-\alpha_{\text{test}})^m.
$$

Wird diese Beziehung nach einem angestrebten familienweisen Niveau aufgelöst, ergibt sich die Sidak-Schwelle. Bonferroni liefert dagegen eine Schranke, die keine unabhängigen Tests voraussetzt:

$$
\alpha_{\text{test,Sidak}}
=1-(1-\alpha_{\text{family}})^{1/m},
\qquad
\alpha_{\text{test,Bonferroni}}
=\frac{\alpha_{\text{family}}}{m}.
$$

Die Sidak-Gleichung ist nur bei voneinander unabhängigen Tests exakt. Paarvergleiche mit gemeinsamen Gruppen sind im Allgemeinen abhängig. Bonferroni kontrolliert die familienweise Fehlerrate mithilfe einer oberen Schranke und benötigt diese Unabhängigkeitsannahme nicht, kann jedoch konservativ sein.

Eine zweifaktorielle ANOVA mit festen Effekten schreibt den Wert einer Zelle als Gesamtmittelwert, zwei Haupteffektkomponenten, ihre Interaktion und einen individuellen Fehler:

$$
y_{ijm}
=\mu+\alpha_i+\beta_j+(\alpha\beta)_{ij}+\varepsilon_{ijm}.
$$

Ein **Zellenmittelwert** gehört zu einer bestimmten Kombination von Faktorstufen. Ein **Randmittelwert** mittelt über die Zellen, die zu einer Stufe eines Faktors gehören. Haupteffekte vergleichen Randmittelwerte. Die Interaktion fragt, ob sich der Effekt eines Faktors über die Stufen des anderen verändert. Es handelt sich also um eine Differenz von Differenzen. Nicht parallele Mittelwertprofile zeigen ein Interaktionsmuster. Die Linien müssen sich nicht kreuzen.

Bei einem balancierten einfaktoriellen Modell mit zufälligem Faktor und $n$ Beobachtungen pro gezogener Stufe werden die Varianzkomponenten zwischen und innerhalb der Stufen im bereitgestellten Material wie folgt geschätzt:

$$
\widehat{\sigma}_A^2=\frac{MS_A-MS_{\text{error}}}{n},
\qquad
\widehat{\sigma}_{\text{error}}^2=MS_{\text{error}},
$$

und die Ähnlichkeit innerhalb einer Stufe wird zusammengefasst durch:

$$
ICC=
\frac{\widehat{\sigma}_A^2}
{\widehat{\sigma}_A^2+\widehat{\sigma}_{\text{error}}^2}.
$$

Diese Gleichungen gehören zu diesem balancierten einfaktoriellen Modell mit zufälligem Faktor. Sie sind keine allgemeingültige ICC-Formel für jedes geclusterte Design oder jedes Design mit Messwiederholung.

Bei einem Faktor mit Messwiederholung bewahrt der Personenterm die Verbindung zwischen Messungen derselben Person:

$$
y_{im}=\mu+\alpha_i+\pi_m+\varepsilon_{im},
$$

wobei $\alpha_i$ die feste Komponente der Gelegenheit oder Bedingung und $\pi_m$ die zufällige Personenkomponente bezeichnet. Die entsprechende Zerlegung der Variation lautet:

$$
SS_{\text{total}}
=SS_{\text{condition}}+SS_{\text{person}}+SS_{\text{error}}.
$$

Für zwei wiederholte Stufen $j$ und $k$ lautet die Varianz der Differenz innerhalb einer Person:

$$
Var(Y_j-Y_k)
=Var(Y_j)+Var(Y_k)-2\,Cov(Y_j,Y_k).
$$

Sphärizität verlangt, dass die Populationsvarianzen aller solchen paarweisen Differenzwerte gleich sind. Wird das festgelegte Greenhouse-Geisser-Verfahren verwendet, reduziert dessen Schätzung $\widehat\varepsilon\leq1$ beide Referenzfreiheitsgrade:

$$
df_{\text{condition}}^*=\widehat\varepsilon\,df_{\text{condition}},
\qquad
df_{\text{error}}^*=\widehat\varepsilon\,df_{\text{error}}.
$$

Die beobachtete $F$-Statistik verändert sich nicht. Es verändern sich ihre Referenzfreiheitsgrade und der daraus folgende p-Wert oder kritische Wert.

| Designfrage | Grösse oder Vergleich | Wesentliche Begrenzung |
|---|---|---|
| Sind alle festen Populationsmittelwerte der Gruppen gleich? | Omnibus-$F$ der einfaktoriellen ANOVA | Das Verwerfen lokalisiert den Unterschied nicht |
| Welche vorab festgelegten gewichteten Mittelwerte unterscheiden sich? | Geplanter Kontrast $D$ und $F_D$ | Die Planung muss vor der Betrachtung der Ergebnisse erfolgen |
| Hängt der Effekt eines Faktors von einem anderen ab? | Faktorielle Interaktion | Haupteffekte allein können das Zellenmuster verdecken |
| Wie viel Variation gehört zu den gezogenen Stufen? | Varianzkomponente des zufälligen Faktors und ICC | Die Formel hängt vom festgelegten Zufallseffektdesign ab |
| Unterscheiden sich miteinander verbundene Gelegenheiten? | Bedingungseffekt bei Messwiederholung | Abhängigkeit innerhalb von Personen und Sphärizitätsverfahren sind zu berücksichtigen |

## Die erklärende Abbildung lesen

![Zwei Balken zeigen die Gesamtquadratsumme neben einem gleich hohen gestapelten Balken, der mit numerischen Beschriftungen in Faktor- und Fehlerquadratsumme unterteilt ist.](assets/topic-08-analysis-of-variance-summary-figure-de.png){#fig-summary-t08 width=92%}

Der linke Balken enthält die Gesamtquadratsumme 11,350.4. Sie stellt die quadrierten Abweichungen jedes beobachteten Punktwerts vom Gesamtmittelwert dar. Der rechte Balken besitzt dieselbe Gesamthöhe, ist aber gestapelt. Das untere blaue Segment ist die Faktorquadratsumme 2,093.5 und stellt die Trennung der Gruppenmittelwerte dar. Das obere graue Segment ist die Fehlerquadratsumme 9,256.9 und stellt die Unterschiede zwischen den Fällen um ihre jeweiligen Gruppenmittelwerte dar.

Die beiden Beschriftungen auf der rechten Seite addieren sich zur Gesamtsumme links. Diese visuelle Gleichheit ist die zentrale ANOVA-Identität. Die Fehlerkomponente ist in diesem Datensatz grösser. Der $F$-Test vergleicht jedoch nicht direkt die rohen Segmenthöhen. Jede Quadratsumme wird zuerst durch ihre Freiheitsgrade geteilt. Das daraus entstehende Verhältnis der mittleren Quadrate wird danach unter dem Nullmodell anhand einer $F$-Verteilung beurteilt.

Die Balken zeigen weder, welcher Gruppenmittelwert am höchsten ist, noch welche Paare sich unterscheiden. Ebenso zeigen sie nicht, ob die Residualannahmen plausibel sind oder ob das Design eine kausale Aussage stützt. Diese Fragen erfordern die Gruppengrafik, die deskriptive Tabelle, Diagnosen und geplante Kontraste. Die dargestellten Werte stammen aus simulierten Lehrdaten. Sie veranschaulichen daher die Berechnung und liefern keine Evidenz über eine reale Grundgesamtheit.

## Checkliste zur Interpretation

Bestimme Faktor, Stufen, Zielvariable, Analyseeinheit und die Struktur als unabhängige Gruppen oder Messwiederholung. Berichte Gruppengrössen, Mittelwerte, Standardabweichungen und eine klare Gruppendarstellung. Formuliere die Null- und Alternativhypothese des Omnibustests. Prüfe die Unabhängigkeit anhand des Designs und untersuche Residualvariation und ungewöhnliche Beobachtungen. Berichte die vollständige ANOVA-Tabelle mit Quadratsummen, Freiheitsgraden, mittleren Quadraten, $F$ und p-Wert. Ergänze danach die Schätzungen und Unsicherheit geplanter oder korrigierter Vergleiche.

Beantworte nach einem Omnibusergebnis die inhaltliche Frage mit geplanten oder für Multiplizität korrigierten Vergleichen. Interpretiere bei einem faktoriellen Design Interaktionen, bevor du über sie hinweg mittelst. Bewahre bei wiederholten Messungen die Abhängigkeit innerhalb von Personen und berücksichtige das dokumentierte Verfahren zur Sphärizität. Behaupte weder, ein nicht signifikantes Ergebnis beweise gleiche Mittelwerte, noch, ein signifikantes Ergebnis beweise einen wichtigen oder kausalen Unterschied.

## Verbindung zu anderen Themen

Die ANOVA schliesst die Lernsequenz ab, indem sie zur Varianz zurückkehrt, die in der deskriptiven Statistik eingeführt wurde. Wahrscheinlichkeit und Inferenz erklären die $F$-Referenzverteilung und den Entscheidungsprozess. Kovarianz und Korrelation zeigen, wie Variablen lineare Variation teilen. Die einfache Regression zerlegt die Variation der Zielvariable in angepasste und verbleibende Teile. Partielle Korrelation und multiple Regression erklären bedingte Zusammenhänge, nachdem weitere Informationen berücksichtigt wurden.

Die Gruppenzugehörigkeit in der ANOVA kann in einem Regressionsmodell durch Indikatorprädiktoren codiert werden. Die Faktorquadratsumme ist modellbezogene Variation, die Fehlerquadratsumme ist Residualvariation und der Omnibus-$F$-Test vergleicht das vollständige Gruppenmodell mit einem Modell, das nur einen Achsenabschnitt enthält. Faktorielle Interaktionen entsprechen Regressionsinteraktionen, und geplante Kontraste sind gezielte lineare Vergleiche angepasster Mittelwerte. Dieser gemeinsame Rahmen lässt sich am besten als **Verbindung über das allgemeine lineare Modell** verstehen: Die späteren Themen sind verschiedene Sichtweisen darauf, wie strukturierte Prädiktorinformation zur Erklärung der Variation einer Zielvariable verwendet wird, während Unsicherheit und Residualvariation sichtbar bleiben.
