---
title: "Wahrscheinlichkeit"
subtitle: "Eine begleitete Einführung in Ereignisse, bedingtes Denken und Zufallsvariablen"
document-id: "topic-02-probability-summary-de"
course-id: "intro-statistics"
topic-id: "topic-02-probability"
topic-number: "02"
topic-slug: "probability"
document-type: "summary"
locale: "de"
figure-asset: "topic-02-probability-summary-figure-de.png"
---

## Zweck und Grundlagen

Die Wahrscheinlichkeitsrechnung bietet eine Sprache für Situationen, in denen ein Ergebnis nicht im Voraus bekannt ist. Der **Ergebnisraum**, meist als $\Omega$ geschrieben, ist die Menge aller betrachteten möglichen Ergebnisse. Ein **Ereignis** ist eine Sammlung von Ergebnissen aus diesem Ergebnisraum. Ein einzelnes Ergebnis gehört entweder zum Ereignis oder nicht. Diese Sichtweise mit Mengen ist wichtig, weil Wahrscheinlichkeitsregeln zuerst auf Ereignisse und erst danach auf Zahlen angewendet werden.

Stelle dir vor, dass ein beschriftetes Plättchen aus den Zahlen 1 bis 10 gezogen wird. Der Ergebnisraum lautet $\Omega=\{1,2,\ldots,10\}$. Das Ereignis $A$ könnte die Plättchen 1, 2 und 3 enthalten, während das Ereignis $D$ die Plättchen 2, 3 und 7 enthält. Eine Wahrscheinlichkeit ordnet jedem Ereignis eine Zahl zwischen 0 und 1 zu. Null bedeutet, dass das Ereignis innerhalb des angegebenen Ergebnisraums nicht eintreten kann. Eins bedeutet, dass es eintreten muss. Werte zwischen null und eins drücken Grade der Unsicherheit unter dem verwendeten Modell aus.

Wahrscheinlichkeit kann über gleich wahrscheinliche Ergebnisse, langfristige relative Häufigkeiten oder ein festgelegtes Modell erschlossen werden. Bei jedem dieser Zugänge definierst du den Vorgang und den Ergebnisraum vor der Berechnung. Eine Wahrscheinlichkeit ist nie von ihren Bedingungen losgelöst. Die Wahrscheinlichkeit eines Ereignisses kann sich ändern, wenn du neue Informationen erhältst, wenn sich das Auswahlverfahren ändert oder wenn sich die betrachtete Grundgesamtheit ändert.

| Mengenidee | Notation | Bedeutung in Worten |
|---|---|---|
| Vereinigung | $A\cup D$ | Ergebnisse in $A$, in $D$ oder in beiden |
| Schnitt | $A\cap D$ | Ergebnisse, die sowohl zu $A$ als auch zu $D$ gehören |
| Komplement | $A^c$ | Ergebnisse im Ergebnisraum, die nicht zu $A$ gehören |
| Disjunkte Ereignisse | $A\cap B=\varnothing$ | Ereignisse ohne gemeinsames Ergebnis |

## Zentrale Ideen

Die Komplementregel ist nützlich, wenn sich das Gegenereignis leichter zählen lässt. Die Additionsregel verhindert, dass die Überlappung zweier Ereignisse doppelt gezählt wird. Die bedingte Wahrscheinlichkeit verkleinert die Bezugsmenge: $P(A\mid D)$ fragt nach der Wahrscheinlichkeit von $A$ unter den Situationen, in denen $D$ bekanntermassen eingetreten ist. Der senkrechte Strich wird als «gegeben» oder «unter der Bedingung» gelesen. Der Nenner ist deshalb die Wahrscheinlichkeit der Bedingung und nicht die Wahrscheinlichkeit des vollständigen Ergebnisraums.

Unabhängigkeit hat eine genaue Bedeutung. Die Ereignisse $A$ und $D$ sind unabhängig, wenn die Information, dass $D$ eingetreten ist, die Wahrscheinlichkeit von $A$ nicht verändert. Dies ist nicht dasselbe wie Disjunktheit. Wenn zwei Ereignisse disjunkt sind und eines eintritt, kann das andere nicht eintreten. Diese Information verändert also seine Wahrscheinlichkeit. Abgesehen von besonderen Fällen mit Wahrscheinlichkeit null sind disjunkte Ereignisse nicht unabhängig.

Der Satz von Bayes kehrt eine bedingte Wahrscheinlichkeit um. Er verbindet die Wahrscheinlichkeit eines Ergebnisses unter einer Bedingung mit der vorherigen Häufigkeit dieser Bedingung. Basisraten sind wichtig: Selbst ein Ergebnis, das in einer Gruppe häufiger vorkommt, kann nur mit einer mässigen Wahrscheinlichkeit für die Zugehörigkeit zu dieser Gruppe sprechen, wenn die Gruppe selten ist. Schreibe jedes Ereignis in Worten auf, bevor du Zahlen einsetzt. So bleibt die Richtung der Bedingung sichtbar.

Eine **Zufallsvariable** ordnet jedem Ergebnis eines Zufallsvorgangs einen numerischen Wert zu. Eine diskrete Zufallsvariable besitzt getrennte, abzählbare Werte, etwa die Anzahl Antworten mit hoher Prüfungsangst in einer Gruppe. Eine stetige Zufallsvariable kann Werte über ein Intervall hinweg annehmen, etwa einen gemessenen Punktwert. Eine diskrete Wahrscheinlichkeitsfunktion weist einzelnen Werten Wahrscheinlichkeiten zu. Eine stetige Wahrscheinlichkeitsdichte beschreibt, wie sich Wahrscheinlichkeit über Intervalle verteilt. Die Wahrscheinlichkeit eines Intervalls wird durch die Fläche unter der Dichtekurve dargestellt.

| Modell oder Idee | Was beschrieben wird | Zentrale Lesefrage |
|---|---|---|
| Binomialverteilung | Anzahl Erfolge bei einer festen Zahl unabhängiger Versuche mit konstanter Erfolgswahrscheinlichkeit | Sind die feste Versuchszahl, zwei Ergebnisse, Unabhängigkeit und konstante Wahrscheinlichkeit vertretbar? |
| Normalverteilung | Ein symmetrisches glockenförmiges Modell, das durch Mittelwert und Standardabweichung beschrieben wird | Passt das Modell zur Variable und zur gestellten Frage? |
| Stichprobenverteilung | Wie ein Stichprobenkennwert über wiederholte Stichproben aus demselben Vorgang variiert | Wie viel Unsicherheit von Stichprobe zu Stichprobe ist zu erwarten? |
| Erwartungswert | Das mit Wahrscheinlichkeiten gewichtete langfristige Zentrum einer Zufallsvariablen | Welcher Durchschnitt würde sich bei vielen Wiederholungen des Modells ergeben? |

Eine Stichprobenverteilung ist nicht die Verteilung einzelner Werte. Sie ist die Verteilung eines Stichprobenkennwerts, beispielsweise eines Stichprobenmittelwerts, über hypothetisch wiederholte Stichproben. Ihre Streuung wird durch einen **Standardfehler** gemessen. Grössere Stichproben führen normalerweise zu weniger variablen Stichprobenmittelwerten, wenn der zugrunde liegende Vorgang gleich bleibt. Diese Idee verbindet die Wahrscheinlichkeitsrechnung mit Konfidenzintervallen und Hypothesentests.

## Formelleitfaden

Für ein beliebiges Ereignis $A$ enthält das Komplement alle Ergebnisse ausserhalb von $A$. Die beiden Wahrscheinlichkeiten addieren sich zu eins:

$$
P(A^c)=1-P(A)
$$

Bei zwei Ereignissen addierst du ihre Wahrscheinlichkeiten und ziehst ihre Überlappung einmal ab. Diese Subtraktion berichtigt die doppelte Zählung, die entsteht, wenn die gemeinsamen Ergebnisse in den ersten beiden Termen enthalten sind:

$$
P(A\cup D)=P(A)+P(D)-P(A\cap D)
$$

Sind die Ereignisse disjunkt, ist ihre Schnittmenge leer und der Term für die Überlappung beträgt null. Verwende die verkürzte Additionsregel für disjunkte Ereignisse erst, wenn der Ergebnisraum bestätigt, dass beide Ereignisse nicht gemeinsam eintreten können.

Die bedingte Wahrscheinlichkeit beschränkt die Betrachtung auf die Bedingung $D$. Dafür muss $P(D)>0$ gelten:

$$
P(A\mid D)=\frac{P(A\cap D)}{P(D)}
$$

Die Multiplikationsregel folgt aus demselben Zusammenhang. Sie zeigt auch die Bedingung für Unabhängigkeit. Sind $A$ und $D$ unabhängig, gilt $P(A\mid D)=P(A)$ und ihre gemeinsame Wahrscheinlichkeit lässt sich als Produkt schreiben:

$$
P(A\cap D)=P(A\mid D)P(D)=P(A)P(D)
$$

Der Satz von Bayes kehrt die Bedingung um, indem dasselbe gemeinsame Ereignis in der anderen Richtung verwendet wird:

$$
P(A\mid D)=\frac{P(D\mid A)P(A)}{P(D)}
$$

Wenn $A$ und $A^c$ alle Möglichkeiten abdecken, lässt sich der Nenner mit dem Satz der totalen Wahrscheinlichkeit bilden:

$$
P(D)=P(D\mid A)P(A)+P(D\mid A^c)P(A^c).
$$

Dieser Nenner hält die Basisrate sichtbar. Eine Tabelle mit natürlichen Häufigkeiten drückt dieselbe Aktualisierung durch Anzahlen aus. Sie ist oft der sicherste Weg, Sensitivität, Falsch-positiv-Wahrscheinlichkeit und die Wahrscheinlichkeit von $A$ nach der Beobachtung von $D$ auseinanderzuhalten.

Bei einer diskreten Zufallsvariablen ist die Wahrscheinlichkeitsfunktion $p(x)=P(X=x)$ und die Verteilungsfunktion lautet

$$
F(x)=P(X\leq x)=\sum_{u\leq x}p(u).
$$

Sind $x_1,\ldots,x_m$ die möglichen Werte, lauten Erwartungswert und Varianz

$$
E(X)=\sum_{j=1}^{m}x_jp(x_j),
\qquad
Var(X)=\sum_{j=1}^{m}\bigl(x_j-E(X)\bigr)^2p(x_j).
$$

Der Erwartungswert ist das langfristige, mit Wahrscheinlichkeiten gewichtete Zentrum des Modells. Er ist keine Zusicherung, dass eine einzelne Beobachtung genau diesen Wert annimmt.

Bei einer stetigen Zufallsvariablen mit Dichte $f$ entspricht Wahrscheinlichkeit der Fläche unter der Dichte über einem Intervall. Die Verteilungsfunktion gibt diese Intervallwahrscheinlichkeit ohne Integralnotation an:

$$
P(a\lt X\leq b)=F(b)-F(a).
$$

Die Höhe einer Dichte ist nicht selbst eine Wahrscheinlichkeit. Bei einem stetigen Modell gilt für einen einzelnen exakten Punkt $P(X=x)=0$.

Für eine binomialverteilte Zufallsvariable $X$ mit $n$ Versuchen und Erfolgswahrscheinlichkeit $p$ beträgt die Wahrscheinlichkeit von genau $k$ Erfolgen:

$$
P(X=k)={n\choose k}p^k(1-p)^{n-k}
$$

Der Koeffizient ${n\choose k}$ zählt, wie viele Versuchsfolgen genau $k$ Erfolge enthalten. Verwende dieses Modell erst, nachdem du seine Voraussetzungen geprüft hast. Die Tatsache, dass das Ergebnis eine Anzahl ist, reicht dafür nicht aus.

Für die Binomialverteilung gilt ausserdem

$$
E(X)=np,
\qquad
Var(X)=np(1-p).
$$

Eine obere Wahrscheinlichkeit wie $P(X>k)$ kann über ihr Komplement $1-P(X\leq k)$ berechnet werden. Das Modell setzt eine feste Zahl von Versuchen, zwei Ergebnisse pro Versuch, ein konstantes $p$ und unabhängige Versuche voraus.

Bei einer normalverteilten Variablen $X\sim N(\mu,\sigma^2)$ standardisierst du eine Grenze mit

$$
Z=\frac{X-\mu}{\sigma}.
$$

Für untere Verteilungsschwänze gilt $P(X\leq x)=\Phi(z)$, für obere $1-\Phi(z)$. Bei einem Intervall wird eine kumulierte Fläche von der anderen abgezogen. Eine inverse Frage beginnt mit einer kumulierten Wahrscheinlichkeit $q$, bestimmt $z_q=\Phi^{-1}(q)$ und kehrt mit $x_q=\mu+z_q\sigma$ zur ursprünglichen Skala zurück.

Für unabhängige Beobachtungen mit Populationsmittelwert $\mu$ und Populationsvarianz $\sigma^2$ gilt für die Stichprobenverteilung des Stichprobenmittelwerts

$$
E(\bar X)=\mu,
\qquad
Var(\bar X)=\frac{\sigma^2}{n},
\qquad
SE(\bar X)=\frac{\sigma}{\sqrt n}.
$$

Ist $\sigma$ unbekannt, schätzt $s/\sqrt n$ den Standardfehler. Ist die Grundgesamtheit normalverteilt, ist auch der Stichprobenmittelwert exakt normalverteilt. Bei geeigneten nicht normalverteilten Grundgesamtheiten kann seine Verteilung mit wachsendem $n$ annähernd normal werden. Die Güte dieser Annäherung hängt von der Form der Grundgesamtheit ab. Keine einzelne Grenze für die Stichprobengrösse garantiert sie.

| Gegenstand | Was variiert | Zu berichtende Streuung |
|---|---|---|
| Verteilung einzelner Werte | Einzelne Beobachtungen | Populations- oder Stichprobenstandardabweichung |
| Stichprobenverteilung von $\bar X$ | Stichprobenmittelwerte über wiederholte Stichproben | Standardfehler $\sigma/\sqrt n$ oder Schätzung $s/\sqrt n$ |
| Verzerrte realisierte Stichprobe | Fälle, die durch einen ungeeigneten Auswahlrahmen oder Antwortprozess aufgenommen wurden | Ein kleinerer Standardfehler behebt keine Auswahlverzerrung |

## Die erklärende Abbildung lesen

![Vier Felder verwenden nummerierte Plättchen, um Vereinigung, Schnitt, Komplement und disjunkte Ereignisse im selben Ergebnisraum mit zehn Ergebnissen zu zeigen.](assets/topic-02-probability-summary-figure-de.png){#fig-summary-t02 width=92%}

Beginne mit dem Feld oben links. Das Ereignis $A$ enthält 1, 2 und 3, während das Ereignis $D$ die Zahlen 2, 3 und 7 enthält. Ihre Vereinigung hebt 1, 2, 3 und 7 hervor, weil «oder» sowohl Ergebnisse aus einem der beiden Ereignisse als auch gemeinsame Ergebnisse einschliesst. Das Feld oben rechts zeigt den Schnitt. Nur 2 und 3 sind hervorgehoben, weil dies die gemeinsamen Ergebnisse sind.

Das Feld unten links zeigt das Komplement von $A$. Die Plättchen 4 bis 10 sind hervorgehoben, weil jedes Ergebnis im Ergebnisraum entweder zu $A$ oder ausserhalb von $A$ liegen muss. Das Feld unten rechts führt das Ereignis $B$ mit den Zahlen 4, 5, 6 und 7 ein. $A$ und $B$ enthalten kein gemeinsames Plättchen und sind daher disjunkt. Die Farben zeigen die Mengenzugehörigkeit und nicht die Grösse einer Wahrscheinlichkeit. Wären die zehn Plättchen gleich wahrscheinlich, könnte die Anzahl der hervorgehobenen Plättchen durch zehn geteilt werden. Wären die Ergebnisse nicht gleich wahrscheinlich, würde das Zählen nicht genügen. Dann wären die zugeordneten Wahrscheinlichkeiten erforderlich.

Die Abbildung hilft dir, die Notation vor der Verwendung einer Formel zu prüfen. Bestimme zuerst die relevanten Plättchen und übersetze diese Menge danach in eine Wahrscheinlichkeit. Diese Reihenfolge verringert häufige Fehler: «oder» wird nicht versehentlich ausschliessend verstanden, die Überlappung in der Additionsregel wird nicht vergessen und Disjunktheit wird nicht mit Unabhängigkeit verwechselt.

## Checkliste zur Interpretation

Definiere den Zufallsvorgang, den Ergebnisraum und jedes Ereignis in Worten. Prüfe, ob die Ergebnisse gleich wahrscheinlich sind, bevor du Anzahlen verwendest. Benenne bei einer bedingten Wahrscheinlichkeit die Bedingung und verwende sie als Bezugsgruppe. Zeichne eine Menge, eine Tabelle oder einen Wahrscheinlichkeitsbaum, wenn dir die Richtung einer Bedingung unsicher erscheint. Unterscheide disjunkte von unabhängigen Ereignissen. Gib bei einer Zufallsvariablen an, ob sie diskret oder stetig ist und was ein einzelner Wert bedeutet.

Stimme bei der Wahl einer Verteilung ihre Voraussetzungen auf den Vorgang ab. Gib an, ob eine Wahrscheinlichkeit aus einem theoretischen Modell, einer beobachteten relativen Häufigkeit oder einer Simulation stammt. Eine Simulation nähert die Folgen ihrer festgelegten Regeln an. Sie kann ungeeignete Annahmen nicht korrigieren. Halte bei einer Stichprobenverteilung einzelne Beobachtungen und Stichprobenkennwerte auseinander und benenne, was sich über wiederholte Stichproben verändern würde.

## Verbindung zu anderen Themen

Die deskriptive Statistik fasste den beobachteten Datensatz zusammen. Die Wahrscheinlichkeitsrechnung beschreibt nun, wie Ergebnisse unter einem Zufallsvorgang variieren könnten. Die statistische Inferenz verbindet beide Ideen: Sie verwendet die Stichprobenverteilung eines Stichprobenkennwerts, um die Vereinbarkeit eines beobachteten Ergebnisses mit einer Aussage über die Grundgesamtheit zu beurteilen und die Unsicherheit einer Schätzung auszudrücken.

Auch spätere Modelle beruhen auf Wahrscheinlichkeit. Ein Korrelations- oder Regressionskoeffizient verändert sich von Stichprobe zu Stichprobe. Konfidenzintervalle und Tests beschreiben diese Streuung mit Wahrscheinlichkeitsmodellen. Die Varianzanalyse vergleicht systematische und verbleibende Variation mithilfe einer $F$-Verteilung. Die Notation wird umfangreicher, doch die Grundfragen bleiben vertraut: Welche Ergebnisse sind möglich, welche Bedingungen werden vorausgesetzt und welche Unsicherheit beschreibt die Wahrscheinlichkeit?
