---
title: "Deskriptive Statistik"
subtitle: "Ein verständlicher Wegweiser zu Variablen, Verteilungen und numerischen Kennwerten"
document-id: "topic-01-descriptive-statistics-summary-de"
course-id: "intro-statistics"
topic-id: "topic-01-descriptive-statistics"
topic-number: "01"
topic-slug: "descriptive-statistics"
document-type: "summary"
locale: "de"
figure-asset: "topic-01-descriptive-statistics-summary-figure-de.png"
---

## Zweck und Grundlagen

Die deskriptive Statistik bietet dir ein geordnetes Vorgehen, um aus einer Sammlung von Beobachtungen eine verständliche Beschreibung zu entwickeln. Bestimme zuerst die **Fälle**, also die Personen oder Untersuchungseinheiten in den Zeilen eines Datensatzes, und die **Variablen**, also die in den Spalten erfassten Merkmale. Ein Wert ist ein aufgezeichnetes Ergebnis für eine Variable bei einem Fall. Frage vor jeder Berechnung, was die Variable bedeutet, wie sie gemessen wurde und welche Werte möglich sind. So verhinderst du, dass eine mathematisch korrekte Berechnung zu einer irreführenden Beschreibung wird.

Das Skalenniveau bestimmt, welche Auswertungen für eine Variable sinnvoll sind. Eine nominale Variable ordnet Fälle Kategorien zu, ohne diese zu reihen. Eine ordinale Variable besitzt geordnete Kategorien, doch die Abstände zwischen benachbarten Kategorien sind nicht als gleich bekannt. Eine Intervallvariable besitzt bedeutungsvolle gleiche Abstände, aber keinen inhaltlich bedeutsamen absoluten Nullpunkt. Eine Verhältnisvariable besitzt gleiche Abstände und einen bedeutsamen Nullpunkt, sodass auch Verhältnisse interpretiert werden können. Das Skalenniveau ist eine Eigenschaft der Definition und Messung einer Variablen. Es hängt nicht davon ab, wie ihre Werte in einem einzelnen Datensatz aussehen.

| Skalenniveau | Was die Werte aussagen | Geeignete erste Kennwerte |
|---|---|---|
| Nominal | Ob Fälle derselben oder verschiedenen Kategorien angehören | Häufigkeiten, Anteile, Modus |
| Ordinal | Kategorienzugehörigkeit und Reihenfolge | Häufigkeiten, Anteile, Median, Quantile |
| Intervall/Verhältnis | Reihenfolge und bedeutungsvoller numerischer Abstand | Mittelwert, Median, Varianz, Standardabweichung, Quantile |

Einige Lehrdatensätze dieses Kurses sind **simulierte Daten**. Das sind am Computer erzeugte Werte, die festgelegten Regeln folgen, und keine Messungen an realen Personen. Eine **Simulation** ist der Vorgang, mit dem diese Werte erzeugt werden. Der Computer verwendet dazu einen **Zufallszahlengenerator**, also einen Algorithmus, der Werte erzeugt, die sich wie Zufallsergebnisse verhalten. Ein **Seed** ist der Startwert für diesen Algorithmus. Wenn derselbe Seed mit denselben Anweisungen erneut verwendet wird, entsteht derselbe Datensatz. Dadurch ist ein Lehrbeispiel reproduzierbar: Du und eine andere lernende Person könnt dieselben Beobachtungen untersuchen und erhaltet dieselben Ergebnisse. Eine Simulation unterstützt das Lernen, doch erzeugte Werte werden dadurch nicht zu Evidenz über eine reale Grundgesamtheit.

## Zentrale Ideen

Eine Verteilung beschreibt, wie sich die Werte einer Variablen über ihren möglichen Bereich verteilen. Bei einer kategorialen Variable beginnst du mit einer Häufigkeitstabelle. Die absolute Häufigkeit ist die Anzahl Fälle in einer Kategorie. Die relative Häufigkeit ist diese Anzahl geteilt durch die Gesamtzahl der gültigen Fälle. Relative Häufigkeiten lassen sich als Anteile oder Prozentsätze angeben. Prüfe immer, ob fehlende Werte aus dem Nenner ausgeschlossen wurden. Ein Prozentsatz ist nur dann aussagekräftig, wenn seine Bezugsgrösse bekannt ist.

Bei einer numerischen Variable beschreibst du vier Merkmale gemeinsam: Lage, Streuung, Form und ungewöhnliche Beobachtungen. Der Mittelwert verwendet jeden Wert und bildet den Gleichgewichtspunkt der Verteilung. Der Median ist der mittlere geordnete Wert und teilt die Daten in zwei Hälften. Der Modus ist der häufigste Wert oder die häufigste Kategorie. Die Spannweite reicht vom kleinsten bis zum grössten Wert. Der Interquartilsabstand umfasst die mittlere Hälfte der geordneten Beobachtungen. Varianz und Standardabweichung fassen zusammen, wie weit die Werte typischerweise vom Mittelwert entfernt liegen.

| Frage | Nützliche Evidenz | Gute Lesegewohnheit |
|---|---|---|
| Wo liegt das Zentrum der Verteilung? | Mittelwert, Median und manchmal Modus | Mittelwert und Median vergleichen, statt nur eine Zahl anzugeben |
| Wie stark unterscheiden sich die Beobachtungen? | Spannweite, Interquartilsabstand, Varianz, Standardabweichung | Masseinheit nennen und auf ungewöhnliche Werte achten |
| Welche Form bilden die Werte? | Histogramm, Boxplot, Häufigkeiten, Schiefe | Auf Symmetrie, Schiefe, Lücken, Häufungen und mehrere Gipfel achten |
| Sind einzelne Werte überraschend? | Rohwerte, Grafik, Datenprüfung, standardisierte Werte | Zuerst untersuchen und erst danach entscheiden, ob ein Wert fehlerhaft ist |

Die Form beeinflusst die Interpretation. In einer annähernd symmetrischen Verteilung sind Mittelwert und Median oft ähnlich. Ein langer rechter Rand zieht den Mittelwert tendenziell nach oben, ein langer linker Rand zieht ihn nach unten. **Modalität** beschreibt die Anzahl und das Muster klarer Gipfel oder Hauptkonzentrationen. Eine Verteilung kann unimodal sein und einen Hauptgipfel besitzen oder multimodal sein und mehrere Häufungen von Beobachtungen zeigen. **Kurtosis** beschreibt, wie leicht Werte weit in den Randbereichen auftreten, verglichen mit einer symmetrischen glockenförmigen Referenzverteilung mit derselben Gesamtstreuung. Die Gipfelhöhe allein definiert die Kurtosis nicht. Eine einzelne Zahl wie der Mittelwert kann diese Merkmale nicht darstellen. Deshalb solltest du eine Grafik und numerische Kennwerte gemeinsam lesen.

Eine ungewöhnliche Beobachtung ist nicht automatisch ein Fehler. Sie kann ein gültiger, aber seltener Fall, ein Codierungsfehler, ein Messproblem oder ein Hinweis darauf sein, dass verschiedene Gruppen zusammengefasst wurden. Prüfe die ursprüngliche Definition und den Erfassungsvorgang, bevor du etwas ausschliesst. Wenn sich eine analytische Entscheidung nach dem Entfernen einer Beobachtung verändert, solltest du diese Empfindlichkeit offen berichten.

## Formelleitfaden

Für Kategorie oder Intervall $j$ sei $n_j$ die absolute Häufigkeit und $n$ die Anzahl gültiger Beobachtungen. Die relative Häufigkeit lautet

$$
f_j=\frac{n_j}{n}.
$$

Bei geordneten Kategorien oder numerischen Intervallen ist die kumulierte relative Häufigkeit bis einschliesslich Kategorie $j$

$$
F_j=\sum_{h=1}^{j}f_h.
$$

Die absoluten Häufigkeiten sollten sich zu $n$ und die relativen Häufigkeiten abgesehen von Rundungen zu 1 addieren. Die letzte kumulierte relative Häufigkeit sollte ebenfalls 1 betragen. Kumulierte Häufigkeiten sind nur bei Kategorien mit einer inhaltlich vertretbaren Reihenfolge sinnvoll.

Seien $x_1, x_2, \ldots, x_n$ die beobachteten Werte einer numerischen Variablen. Der Stichprobenmittelwert addiert alle Werte und teilt die Summe durch die Anzahl Beobachtungen:

$$
\bar{x}=\frac{1}{n}\sum_{i=1}^{n}x_i
$$

Das Zeichen $\sum$ bedeutet, dass die angegebenen Werte addiert werden. Der Index $i$ bezeichnet jeweils eine Beobachtung, von der ersten Beobachtung bis zur Beobachtung $n$. Die Abweichung $x_i-\bar{x}$ zeigt, wie weit ein Wert über oder unter dem Mittelwert liegt. Positive und negative Abweichungen heben sich beim Addieren gegenseitig auf. Deshalb werden sie für die Varianz zuerst quadriert. Die Stichprobenvarianz verwendet $n-1$ im Nenner:

$$
s^2=\frac{1}{n-1}\sum_{i=1}^{n}(x_i-\bar{x})^2
$$

Die entsprechende Populationsvarianz verwendet den Populationsmittelwert $\mu$ und teilt durch die Populationsgrösse $N$:

$$
\sigma^2=\frac{1}{N}\sum_{i=1}^{N}(x_i-\mu)^2.
$$

Halte die beiden Zielgrössen auseinander. Der Nenner $n-1$ gehört zur korrigierten Stichprobenvarianz, mit der die Variabilität der Grundgesamtheit geschätzt wird. Die Division durch $N$ beschreibt dagegen die vollständigen Werte der Grundgesamtheit selbst.

Die Varianz wird in quadrierten Einheiten angegeben. Mit ihrer Quadratwurzel kehren wir zur ursprünglichen Masseinheit zurück. Die Stichprobenstandardabweichung lautet deshalb:

$$
s=\sqrt{\frac{1}{n-1}\sum_{i=1}^{n}(x_i-\bar{x})^2}
$$

Ein standardisierter Wert drückt einen einzelnen Wert in Standardabweichungseinheiten aus. Dazu wird der Stichprobenmittelwert abgezogen und durch die Stichprobenstandardabweichung geteilt:

$$
z_i=\frac{x_i-\bar{x}}{s}
$$

Ein positives $z_i$ bedeutet, dass der Wert über dem Mittelwert liegt, ein negatives $z_i$ bedeutet, dass er darunter liegt. Der Betrag gibt den Abstand in Standardabweichungen an. Die Standardisierung verändert die Einheit und den Bezugspunkt, aber weder die Reihenfolge noch die Form der Beobachtungen.

Median und Quantile beginnen mit den geordneten Beobachtungen. Das erste Quartil $Q_1$ markiert das untere Viertel, der Median $Q_2$ die Hälfte und das dritte Quartil $Q_3$ die unteren drei Viertel. Spannweite und Interquartilsabstand lauten

$$
\text{Spannweite}=x_{\max}-x_{\min},
\qquad
IQR=Q_3-Q_1.
$$

Konventionen für Stichprobenquantile können unterschiedlich interpolieren. Bei einem kleinen Datensatz kann Software deshalb leicht verschiedene Quartile ausgeben. Eine verbreitete Boxplot-Diagnose verwendet die inneren Grenzen

$$
Q_1-1.5(IQR)
\qquad\text{und}\qquad
Q_3+1.5(IQR).
$$

Werte ausserhalb einer Grenze sind mögliche Ausreisser, die untersucht werden sollten, und keine automatisch zu löschenden Fehler. Die Whisker enden bei den extremsten beobachteten Werten, die noch innerhalb der Grenzen liegen. Sie enden nicht zwingend genau an den berechneten Grenzen.

Bei einer linearen Transformation $Y=a+bX$ verändern sich Lage und Streuung gemäss

$$
\bar y=a+b\bar x,
\qquad
s_y^2=b^2s_x^2,
\qquad
s_y=|b|s_x.
$$

Die Verschiebung $a$ verändert die Lage, aber nicht die Streuung. Der Faktor $b$ verändert Abstände um $|b|$, weshalb sich die Varianz um $b^2$ verändert. Die Standardisierung ist der Spezialfall, bei dem der Mittelwert abgezogen und durch die Standardabweichung geteilt wird.

Bei der Höhe von Histogrammbalken ist eine letzte Prüfung nötig. Besitzt Klasse $j$ die relative Häufigkeit $f_j$ und die Breite $w_j$, lautet ihre Dichtehöhe

$$
h_j=\frac{f_j}{w_j}.
$$

Die Balkenfläche ist dann $h_jw_j=f_j$. Bei gleich breiten Klassen kann die Höhe die Häufigkeit direkt wiedergeben. Bei ungleichen Klassenbreiten werden Dichtehöhen benötigt, damit weiterhin die Fläche und nicht allein die Höhe die Häufigkeit darstellt.

## Die erklärende Abbildung lesen

![Histogramm simulierter Prüfungsangstwerte von null bis vierzig, mit den höchsten Balken nahe der Mitte und schmaler besetzten Rändern an beiden Enden.](assets/topic-01-descriptive-statistics-summary-figure-de.png){#fig-summary-t01 width=92%}

Lies zuerst die horizontale Achse. Sie zeigt Prüfungsangstwerte auf einer Skala von 0 bis 40. Die vertikale Achse gibt die Anzahl der Studierenden an. Die Höhe jedes Balkens entspricht somit einer Häufigkeit. Die Balken bei Werten zwischen 18 und 22 sind am höchsten. Die grösste Häufung liegt also nahe der Skalenmitte. An den unteren und oberen Enden finden sich weniger Beobachtungen. Ein Balken nahe bei 40 zeigt, dass mindestens ein hoher Wert vorhanden ist. Aus der Grafik allein lässt sich jedoch nicht erkennen, ob dieser Wert fehlerhaft ist. Bevor du dies beurteilst, müsstest du zur Datendefinition und zum Erfassungsvorgang zurückkehren.

Die Balken berühren sich, weil eine numerische Skala über benachbarte Intervalle hinweg stetig verläuft. Auch ihre Breite ist wichtig: Andere Intervallgrenzen können dieselben Beobachtungen mehr oder weniger detailliert erscheinen lassen. Die Abbildung ist deshalb als Ansicht einer einzigen Verteilung zu lesen und nicht als Ansammlung getrennter Kategorien. Sie stützt Aussagen über Lage, Streuung, Form und ungewöhnliche Beobachtungen. Sie zeigt weder eine Ursache von Prüfungsangst noch einen Vergleich zwischen Grundgesamtheiten. Ebenso belegt sie nicht, dass dieses simulierte Muster bei realen Studierenden vorkommt.

## Checkliste zur Interpretation

Beginne jede deskriptive Beschreibung mit den Fällen, der Variable, ihrem Skalenniveau und dem gültigen Wertebereich. Gib die Anzahl der gültigen und fehlenden Beobachtungen an. Berichte bei einer kategorialen Variable die Häufigkeiten zusammen mit dem Nenner und den Anteilen. Verbinde bei einer numerischen Variable eine Grafik mit Kennwerten der Lage und Streuung. Verwende Mittelwert und Standardabweichung, wenn sie zur Verteilung passen. Untersuche zusätzlich Median und Interquartilsabstand, wenn Schiefe oder ungewöhnliche Beobachtungen eine Rolle spielen.

Halte die Masseinheit sichtbar. Eine Standardabweichung von fünf Punkten bedeutet etwas anderes als fünf Stunden. Bezeichne eine Gruppe nicht ohne einen sinnvollen Vergleich als homogen oder variabel. Prüfe, ob sich eine gerundete Tabelle noch zur erwarteten Gesamtsumme addiert. Kennzeichne simulierte Daten als simuliert. Trenne schliesslich Beschreibung und Erklärung: Ein Muster in den beobachteten Werten zeigt, was der Datensatz enthält. Eine kausale Erklärung erfordert dagegen ein geeignetes Forschungsdesign und Überlegungen, die über die deskriptive Statistik hinausgehen.

## Verbindung zu anderen Themen

Die deskriptive Statistik stellt die Sprache bereit, die in der gesamten Lernsequenz verwendet wird. Die Wahrscheinlichkeitsrechnung ergänzt Regeln für das Denken über unsichere Ergebnisse. Die statistische Inferenz verwendet anschliessend eine Stichprobe und ihre Streuung, um vorsichtige Aussagen über eine Grundgesamtheit zu machen. Kovarianz und Korrelation fragen, wie zwei Variablen gemeinsam variieren. Die Regression beschreibt eine Zielvariable als Funktion eines oder mehrerer Prädiktoren, während die partielle Korrelation einen Zusammenhang nach linearer Bereinigung untersucht. Die Varianzanalyse vergleicht Gruppenmittelwerte, indem sie die Gesamtvariation in inhaltlich bedeutsame Bestandteile zerlegt.

Die zentrale Gewohnheit bleibt dabei unverändert: Verstehe die Variablen, untersuche die Verteilung, berechne einen passenden Kennwert und interpretiere ihn im Kontext. Spätere Verfahren ergänzen Unsicherheit und Modelle. Sie ersetzen jedoch nie die verlässliche Beschreibung der Daten, die in die Analyse eingegangen sind.
