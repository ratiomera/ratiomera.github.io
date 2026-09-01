---
title: "Vollständige Lösungen"
subtitle: "Multiple Regression"
document-id: "topic-07-multiple-regression-solutions-de"
topic-id: "topic-07-multiple-regression"
topic-number: "07"
topic-slug: "multiple-regression"
document-type: "solutions"
locale: "de"
paired-document-id: "topic-07-multiple-regression-exercises-de"
---

Diese vollständigen Lösungen verwenden dieselben Kennungen und dieselbe Reihenfolge wie das Übungsblatt. Zwischenwerte werden bis zum angegebenen Rundungsschritt beibehalten. Kleine Abweichungen durch früheres Runden sind deshalb dort zulässig, wo dies vermerkt ist. Alle Kontexte, Werte, Daten und Softwareausgaben sind eigens erstelltes Lehrmaterial; sie sind keine empirischen Befunde.

# Teil I: Theorie

## A06: Dummy-Variablen bilden und die Referenzkategorie bestimmen

### T07-A06-V01: Tutorialformat

**Fragestellung bestimmen, Teil (a)**

Mit einem Achsenabschnitt werden $k-1=2$ Dummy-Variablen benötigt. Die ausgelassene Kategorie wird durch den Achsenabschnitt dargestellt und bildet die Vergleichsbasis.

**Evidenz schrittweise beurteilen, Teil (b)**

Die vollständige Codierung lautet:

| Kategorie | $D_1$ (Video) | $D_2$ (Interaktiv) |
| --- | --- | --- |
| Text | 0 | 0 |
| Video | 1 | 0 |
| Interaktiv | 0 | 1 |

**Evidenz schrittweise beurteilen, Teil (c)**

Die Kategorie „Text“ ist die Referenz, weil in dieser Zeile jede Dummy-Variable null ist. Die angepassten Werte der Kategorien lauten:

| Kategorie | Angepasster Wert der Ergebnisvariable „Punktwert im statistischen Denken“ |
| --- | --- |
| Text | 61.00 |
| Video | 64.50 |
| Interaktiv | 67.00 |

Der Koeffizient von $D_1$ ist 3.50. Somit liegt der angepasste Wert der Ergebnisvariable „Punktwert im statistischen Denken“ für die Kategorie „Video“ um 3.50 Punkte höher als für die Referenzkategorie „Text“. Der Achsenabschnitt 61.00 ist der angepasste Wert für „Text“.

**Schluss und Grenzen festhalten, Teil (d)**

Für jeden Fall würden sich die $k$ Kategorieindikatoren genau zu eins summieren. Diese Eins ist bereits die Achsenabschnittsspalte. Werden alle Indikatoren zusammen mit dem Achsenabschnitt aufgenommen, ist eine Spalte eine exakte Kombination der anderen und die Koeffizienten sind nicht eindeutig bestimmt. Eine andere Referenz verändert den angezeigten Achsenabschnitt und die Kategoriekontraste, aber nicht den angepassten Wert einer Kategorie.

### T07-A06-V02: Lernort

**Fragestellung bestimmen, Teil (a)**

Mit einem Achsenabschnitt werden $k-1=3$ Dummy-Variablen benötigt. Die ausgelassene Kategorie wird durch den Achsenabschnitt dargestellt und bildet die Vergleichsbasis.

**Evidenz schrittweise beurteilen, Teil (b)**

Die vollständige Codierung lautet:

| Kategorie | $D_1$ (Bibliothek) | $D_2$ (Lernraum) | $D_3$ (Draussen) |
| --- | --- | --- | --- |
| Zu Hause | 0 | 0 | 0 |
| Bibliothek | 1 | 0 | 0 |
| Lernraum | 0 | 1 | 0 |
| Draussen | 0 | 0 | 1 |

**Evidenz schrittweise beurteilen, Teil (c)**

Die Kategorie „Zu Hause“ ist die Referenz, weil in dieser Zeile jede Dummy-Variable null ist. Die angepassten Werte der Kategorien lauten:

| Kategorie | Angepasster Wert der Ergebnisvariable „Konzentrationswert“ |
| --- | --- |
| Zu Hause | 54.00 |
| Bibliothek | 58.00 |
| Lernraum | 56.50 |
| Draussen | 52.50 |

Der Koeffizient von $D_1$ ist 4.00. Somit liegt der angepasste Wert der Ergebnisvariable „Konzentrationswert“ für die Kategorie „Bibliothek“ um 4.00 Punkte höher als für die Referenzkategorie „Zu Hause“. Der Achsenabschnitt 54.00 ist der angepasste Wert für „Zu Hause“.

**Schluss und Grenzen festhalten, Teil (d)**

Für jeden Fall würden sich die $k$ Kategorieindikatoren genau zu eins summieren. Diese Eins ist bereits die Achsenabschnittsspalte. Werden alle Indikatoren zusammen mit dem Achsenabschnitt aufgenommen, ist eine Spalte eine exakte Kombination der anderen und die Koeffizienten sind nicht eindeutig bestimmt. Eine andere Referenz verändert den angezeigten Achsenabschnitt und die Kategoriekontraste, aber nicht den angepassten Wert einer Kategorie.

### T07-A06-V03: Feedbackkanal

**Fragestellung bestimmen, Teil (a)**

Mit einem Achsenabschnitt werden $k-1=2$ Dummy-Variablen benötigt. Die ausgelassene Kategorie wird durch den Achsenabschnitt dargestellt und bildet die Vergleichsbasis.

**Evidenz schrittweise beurteilen, Teil (b)**

Die vollständige Codierung lautet:

| Kategorie | $D_1$ (Audio) | $D_2$ (Video) |
| --- | --- | --- |
| Schriftlich | 0 | 0 |
| Audio | 1 | 0 |
| Video | 0 | 1 |

**Evidenz schrittweise beurteilen, Teil (c)**

Die Kategorie „Schriftlich“ ist die Referenz, weil in dieser Zeile jede Dummy-Variable null ist. Die angepassten Werte der Kategorien lauten:

| Kategorie | Angepasster Wert der Ergebnisvariable „Punktwert der Überarbeitung“ |
| --- | --- |
| Schriftlich | 66.00 |
| Audio | 68.00 |
| Video | 70.50 |

Der Koeffizient von $D_1$ ist 2.00. Somit liegt der angepasste Wert der Ergebnisvariable „Punktwert der Überarbeitung“ für die Kategorie „Audio“ um 2.00 Punkte höher als für die Referenzkategorie „Schriftlich“. Der Achsenabschnitt 66.00 ist der angepasste Wert für „Schriftlich“.

**Schluss und Grenzen festhalten, Teil (d)**

Für jeden Fall würden sich die $k$ Kategorieindikatoren genau zu eins summieren. Diese Eins ist bereits die Achsenabschnittsspalte. Werden alle Indikatoren zusammen mit dem Achsenabschnitt aufgenommen, ist eine Spalte eine exakte Kombination der anderen und die Koeffizienten sind nicht eindeutig bestimmt. Eine andere Referenz verändert den angezeigten Achsenabschnitt und die Kategoriekontraste, aber nicht den angepassten Wert einer Kategorie.

### T07-A06-V04: Methode der Notizerfassung

**Fragestellung bestimmen, Teil (a)**

Mit einem Achsenabschnitt werden $k-1=3$ Dummy-Variablen benötigt. Die ausgelassene Kategorie wird durch den Achsenabschnitt dargestellt und bildet die Vergleichsbasis.

**Evidenz schrittweise beurteilen, Teil (b)**

Die vollständige Codierung lautet:

| Kategorie | $D_1$ (Tablet) | $D_2$ (Laptop) | $D_3$ (Gemischt) |
| --- | --- | --- | --- |
| Papier | 0 | 0 | 0 |
| Tablet | 1 | 0 | 0 |
| Laptop | 0 | 1 | 0 |
| Gemischt | 0 | 0 | 1 |

**Evidenz schrittweise beurteilen, Teil (c)**

Die Kategorie „Papier“ ist die Referenz, weil in dieser Zeile jede Dummy-Variable null ist. Die angepassten Werte der Kategorien lauten:

| Kategorie | Angepasster Wert der Ergebnisvariable „Erinnerungswert“ |
| --- | --- |
| Papier | 58.00 |
| Tablet | 56.50 |
| Laptop | 55.50 |
| Gemischt | 61.00 |

Der Koeffizient von $D_1$ ist -1.50. Somit liegt der angepasste Wert der Ergebnisvariable „Erinnerungswert“ für die Kategorie „Tablet“ um 1.50 Punkte tiefer als für die Referenzkategorie „Papier“. Der Achsenabschnitt 58.00 ist der angepasste Wert für „Papier“.

**Schluss und Grenzen festhalten, Teil (d)**

Für jeden Fall würden sich die $k$ Kategorieindikatoren genau zu eins summieren. Diese Eins ist bereits die Achsenabschnittsspalte. Werden alle Indikatoren zusammen mit dem Achsenabschnitt aufgenommen, ist eine Spalte eine exakte Kombination der anderen und die Koeffizienten sind nicht eindeutig bestimmt. Eine andere Referenz verändert den angezeigten Achsenabschnitt und die Kategoriekontraste, aber nicht den angepassten Wert einer Kategorie.

### T07-A06-V05: Workshopzeit

**Fragestellung bestimmen, Teil (a)**

Mit einem Achsenabschnitt werden $k-1=2$ Dummy-Variablen benötigt. Die ausgelassene Kategorie wird durch den Achsenabschnitt dargestellt und bildet die Vergleichsbasis.

**Evidenz schrittweise beurteilen, Teil (b)**

Die vollständige Codierung lautet:

| Kategorie | $D_1$ (Nachmittag) | $D_2$ (Abend) |
| --- | --- | --- |
| Morgen | 0 | 0 |
| Nachmittag | 1 | 0 |
| Abend | 0 | 1 |

**Evidenz schrittweise beurteilen, Teil (c)**

Die Kategorie „Morgen“ ist die Referenz, weil in dieser Zeile jede Dummy-Variable null ist. Die angepassten Werte der Kategorien lauten:

| Kategorie | Angepasster Wert der Ergebnisvariable „Punktwert des Selbstvertrauens“ |
| --- | --- |
| Morgen | 49.00 |
| Nachmittag | 51.50 |
| Abend | 46.00 |

Der Koeffizient von $D_1$ ist 2.50. Somit liegt der angepasste Wert der Ergebnisvariable „Punktwert des Selbstvertrauens“ für die Kategorie „Nachmittag“ um 2.50 Punkte höher als für die Referenzkategorie „Morgen“. Der Achsenabschnitt 49.00 ist der angepasste Wert für „Morgen“.

**Schluss und Grenzen festhalten, Teil (d)**

Für jeden Fall würden sich die $k$ Kategorieindikatoren genau zu eins summieren. Diese Eins ist bereits die Achsenabschnittsspalte. Werden alle Indikatoren zusammen mit dem Achsenabschnitt aufgenommen, ist eine Spalte eine exakte Kombination der anderen und die Koeffizienten sind nicht eindeutig bestimmt. Eine andere Referenz verändert den angezeigten Achsenabschnitt und die Kategoriekontraste, aber nicht den angepassten Wert einer Kategorie.

### T07-A06-V06: Archivhilfe

**Fragestellung bestimmen, Teil (a)**

Mit einem Achsenabschnitt werden $k-1=3$ Dummy-Variablen benötigt. Die ausgelassene Kategorie wird durch den Achsenabschnitt dargestellt und bildet die Vergleichsbasis.

**Evidenz schrittweise beurteilen, Teil (b)**

Die vollständige Codierung lautet:

| Kategorie | $D_1$ (Karte) | $D_2$ (Mentor) | $D_3$ (Suchwerkzeug) |
| --- | --- | --- | --- |
| Checkliste | 0 | 0 | 0 |
| Karte | 1 | 0 | 0 |
| Mentor | 0 | 1 | 0 |
| Suchwerkzeug | 0 | 0 | 1 |

**Evidenz schrittweise beurteilen, Teil (c)**

Die Kategorie „Checkliste“ ist die Referenz, weil in dieser Zeile jede Dummy-Variable null ist. Die angepassten Werte der Kategorien lauten:

| Kategorie | Angepasster Wert der Ergebnisvariable „Punktwert der Suche“ |
| --- | --- |
| Checkliste | 63.00 |
| Karte | 64.50 |
| Mentor | 68.00 |
| Suchwerkzeug | 66.00 |

Der Koeffizient von $D_1$ ist 1.50. Somit liegt der angepasste Wert der Ergebnisvariable „Punktwert der Suche“ für die Kategorie „Karte“ um 1.50 Punkte höher als für die Referenzkategorie „Checkliste“. Der Achsenabschnitt 63.00 ist der angepasste Wert für „Checkliste“.

**Schluss und Grenzen festhalten, Teil (d)**

Für jeden Fall würden sich die $k$ Kategorieindikatoren genau zu eins summieren. Diese Eins ist bereits die Achsenabschnittsspalte. Werden alle Indikatoren zusammen mit dem Achsenabschnitt aufgenommen, ist eine Spalte eine exakte Kombination der anderen und die Koeffizienten sind nicht eindeutig bestimmt. Eine andere Referenz verändert den angezeigten Achsenabschnitt und die Kategoriekontraste, aber nicht den angepassten Wert einer Kategorie.

### T07-A06-V07: Überarbeitungsstrategie

**Fragestellung bestimmen, Teil (a)**

Mit einem Achsenabschnitt werden $k-1=2$ Dummy-Variablen benötigt. Die ausgelassene Kategorie wird durch den Achsenabschnitt dargestellt und bildet die Vergleichsbasis.

**Evidenz schrittweise beurteilen, Teil (b)**

Die vollständige Codierung lautet:

| Kategorie | $D_1$ (Peer-Review) | $D_2$ (Beurteilung durch Lehrperson) |
| --- | --- | --- |
| Selbstkontrolle | 0 | 0 |
| Peer-Review | 1 | 0 |
| Beurteilung durch Lehrperson | 0 | 1 |

**Evidenz schrittweise beurteilen, Teil (c)**

Die Kategorie „Selbstkontrolle“ ist die Referenz, weil in dieser Zeile jede Dummy-Variable null ist. Die angepassten Werte der Kategorien lauten:

| Kategorie | Angepasster Wert der Ergebnisvariable „Qualitätswert“ |
| --- | --- |
| Selbstkontrolle | 60.00 |
| Peer-Review | 64.00 |
| Beurteilung durch Lehrperson | 67.00 |

Der Koeffizient von $D_1$ ist 4.00. Somit liegt der angepasste Wert der Ergebnisvariable „Qualitätswert“ für die Kategorie „Peer-Review“ um 4.00 Punkte höher als für die Referenzkategorie „Selbstkontrolle“. Der Achsenabschnitt 60.00 ist der angepasste Wert für „Selbstkontrolle“.

**Schluss und Grenzen festhalten, Teil (d)**

Für jeden Fall würden sich die $k$ Kategorieindikatoren genau zu eins summieren. Diese Eins ist bereits die Achsenabschnittsspalte. Werden alle Indikatoren zusammen mit dem Achsenabschnitt aufgenommen, ist eine Spalte eine exakte Kombination der anderen und die Koeffizienten sind nicht eindeutig bestimmt. Eine andere Referenz verändert den angezeigten Achsenabschnitt und die Kategoriekontraste, aber nicht den angepassten Wert einer Kategorie.

### T07-A06-V08: Museumsroute

**Fragestellung bestimmen, Teil (a)**

Mit einem Achsenabschnitt werden $k-1=4$ Dummy-Variablen benötigt. Die ausgelassene Kategorie wird durch den Achsenabschnitt dargestellt und bildet die Vergleichsbasis.

**Evidenz schrittweise beurteilen, Teil (b)**

Die vollständige Codierung lautet:

| Kategorie | $D_1$ (Thematisch) | $D_2$ (Freie Wahl) | $D_3$ (Geführt) | $D_4$ (Hybrid) |
| --- | --- | --- | --- | --- |
| Chronologisch | 0 | 0 | 0 | 0 |
| Thematisch | 1 | 0 | 0 | 0 |
| Freie Wahl | 0 | 1 | 0 | 0 |
| Geführt | 0 | 0 | 1 | 0 |
| Hybrid | 0 | 0 | 0 | 1 |

**Evidenz schrittweise beurteilen, Teil (c)**

Die Kategorie „Chronologisch“ ist die Referenz, weil in dieser Zeile jede Dummy-Variable null ist. Die angepassten Werte der Kategorien lauten:

| Kategorie | Angepasster Wert der Ergebnisvariable „Punktwert des Wissens“ |
| --- | --- |
| Chronologisch | 57.00 |
| Thematisch | 60.00 |
| Freie Wahl | 56.00 |
| Geführt | 62.50 |
| Hybrid | 61.00 |

Der Koeffizient von $D_1$ ist 3.00. Somit liegt der angepasste Wert der Ergebnisvariable „Punktwert des Wissens“ für die Kategorie „Thematisch“ um 3.00 Punkte höher als für die Referenzkategorie „Chronologisch“. Der Achsenabschnitt 57.00 ist der angepasste Wert für „Chronologisch“.

**Schluss und Grenzen festhalten, Teil (d)**

Für jeden Fall würden sich die $k$ Kategorieindikatoren genau zu eins summieren. Diese Eins ist bereits die Achsenabschnittsspalte. Werden alle Indikatoren zusammen mit dem Achsenabschnitt aufgenommen, ist eine Spalte eine exakte Kombination der anderen und die Koeffizienten sind nicht eindeutig bestimmt. Eine andere Referenz verändert den angezeigten Achsenabschnitt und die Kategoriekontraste, aber nicht den angepassten Wert einer Kategorie.

### T07-A06-V09: Lernplan

**Fragestellung bestimmen, Teil (a)**

Mit einem Achsenabschnitt werden $k-1=2$ Dummy-Variablen benötigt. Die ausgelassene Kategorie wird durch den Achsenabschnitt dargestellt und bildet die Vergleichsbasis.

**Evidenz schrittweise beurteilen, Teil (b)**

Die vollständige Codierung lautet:

| Kategorie | $D_1$ (Zweimal wöchentlich) | $D_2$ (Wöchentlich) |
| --- | --- | --- |
| Täglich | 0 | 0 |
| Zweimal wöchentlich | 1 | 0 |
| Wöchentlich | 0 | 1 |

**Evidenz schrittweise beurteilen, Teil (c)**

Die Kategorie „Täglich“ ist die Referenz, weil in dieser Zeile jede Dummy-Variable null ist. Die angepassten Werte der Kategorien lauten:

| Kategorie | Angepasster Wert der Ergebnisvariable „Punktwert des Behaltens“ |
| --- | --- |
| Täglich | 69.00 |
| Zweimal wöchentlich | 67.00 |
| Wöchentlich | 64.00 |

Der Koeffizient von $D_1$ ist -2.00. Somit liegt der angepasste Wert der Ergebnisvariable „Punktwert des Behaltens“ für die Kategorie „Zweimal wöchentlich“ um 2.00 Punkte tiefer als für die Referenzkategorie „Täglich“. Der Achsenabschnitt 69.00 ist der angepasste Wert für „Täglich“.

**Schluss und Grenzen festhalten, Teil (d)**

Für jeden Fall würden sich die $k$ Kategorieindikatoren genau zu eins summieren. Diese Eins ist bereits die Achsenabschnittsspalte. Werden alle Indikatoren zusammen mit dem Achsenabschnitt aufgenommen, ist eine Spalte eine exakte Kombination der anderen und die Koeffizienten sind nicht eindeutig bestimmt. Eine andere Referenz verändert den angezeigten Achsenabschnitt und die Kategoriekontraste, aber nicht den angepassten Wert einer Kategorie.

### T07-A06-V10: Aufgabenoberfläche

**Fragestellung bestimmen, Teil (a)**

Mit einem Achsenabschnitt werden $k-1=3$ Dummy-Variablen benötigt. Die ausgelassene Kategorie wird durch den Achsenabschnitt dargestellt und bildet die Vergleichsbasis.

**Evidenz schrittweise beurteilen, Teil (b)**

Die vollständige Codierung lautet:

| Kategorie | $D_1$ (Tafel) | $D_2$ (Kalender) | $D_3$ (Zeitachse) |
| --- | --- | --- | --- |
| Liste | 0 | 0 | 0 |
| Tafel | 1 | 0 | 0 |
| Kalender | 0 | 1 | 0 |
| Zeitachse | 0 | 0 | 1 |

**Evidenz schrittweise beurteilen, Teil (c)**

Die Kategorie „Liste“ ist die Referenz, weil in dieser Zeile jede Dummy-Variable null ist. Die angepassten Werte der Kategorien lauten:

| Kategorie | Angepasster Wert der Ergebnisvariable „Punktwert des Abschlusses“ |
| --- | --- |
| Liste | 62.00 |
| Tafel | 64.50 |
| Kalender | 66.00 |
| Zeitachse | 63.00 |

Der Koeffizient von $D_1$ ist 2.50. Somit liegt der angepasste Wert der Ergebnisvariable „Punktwert des Abschlusses“ für die Kategorie „Tafel“ um 2.50 Punkte höher als für die Referenzkategorie „Liste“. Der Achsenabschnitt 62.00 ist der angepasste Wert für „Liste“.

**Schluss und Grenzen festhalten, Teil (d)**

Für jeden Fall würden sich die $k$ Kategorieindikatoren genau zu eins summieren. Diese Eins ist bereits die Achsenabschnittsspalte. Werden alle Indikatoren zusammen mit dem Achsenabschnitt aufgenommen, ist eine Spalte eine exakte Kombination der anderen und die Koeffizienten sind nicht eindeutig bestimmt. Eine andere Referenz verändert den angezeigten Achsenabschnitt und die Kategoriekontraste, aber nicht den angepassten Wert einer Kategorie.

# Teil II: Rechnerpraxis

## A01: Eine Gleichung und Ausgabe der multiplen Regression lesen

### T07-A01-V01: Begleitete Übung und statistisches Denken

**Vor dem Rechnen begründen, Teil (a)**

Die angepasste Gleichung lautet $\hat Y=38.000+(2.400)X_1+(0.310)X_2$. Eine unstandardisierte Steigung verwendet die ursprünglichen Messeinheiten. Ein standardisierter Koeffizient beschreibt dagegen die angepasste Veränderung in Standardabweichungen der Ergebnisvariable bei einer Zunahme des Prädiktors um eine Standardabweichung, bedingt auf den anderen Prädiktor.

**Berechnung durchführen, Teil (b)**

Wenn der Prädiktor „Punktwert der vorherigen Vorbereitung“ festgehalten wird, geht eine Zunahme des Prädiktors „Stunden begleiteter Übung“ um eine Einheit mit einer angepassten Veränderung der Ergebnisvariable „Punktwert im statistischen Denken“ um 2.400 Punkte einher. Wenn der Prädiktor „Stunden begleiteter Übung“ festgehalten wird, geht eine Zunahme des Prädiktors „Punktwert der vorherigen Vorbereitung“ um eine Einheit mit einer angepassten Veränderung der Ergebnisvariable um 0.310 Punkte einher. Dies sind bedingte Zusammenhänge und nicht automatisch kausale Effekte.

**Berechnung durchführen, Teil (c)**

Für $X_1$ gilt $t=2.400/0.580=4.136$ mit 77 Freiheitsgraden und damit $p < 0.0001$; folglich wird die Nullhypothese für den Koeffizienten bei $\alpha=.05$ verworfen. Für $X_2$ gilt $t=0.310/0.108=2.879$ und damit $p = 0.0052$; folglich wird die Nullhypothese für den Koeffizienten verworfen. Jeder Test betrifft diesen einen Populationskoeffizienten, bedingt auf genau den anderen Term in diesem Modell.

**Ergebnis interpretieren und prüfen, Teil (d)**

$R^2=0.370$ bedeutet, dass das angepasste Modell mit zwei Prädiktoren 37.0% der Stichprobenvariation der Ergebnisvariable „Punktwert im statistischen Denken“ darstellt. Das korrigierte $R^2=0.354$ berücksichtigt innerhalb der Stichprobe, dass zwei Steigungen geschätzt wurden. Es ist kein Test an neuen Daten. Der Residualstandardfehler besagt, dass die beobachteten Ergebnisse unter dem Modell typischerweise noch ungefähr 5.60 Punkte von ihren angepassten Werten abweichen. Die standardisierten Steigungen 0.419 und 0.292 unterscheiden sich von den bivariaten Korrelationen 0.550 und 0.480, weil jede Steigung den bedingten Zusammenhang eines Prädiktors von der mit dem anderen Prädiktor geteilten Variation trennt.

### T07-A01-V02: Arbeitsablauf im Archiv und Suchzeit

**Vor dem Rechnen begründen, Teil (a)**

Die angepasste Gleichung lautet $\hat Y=70.000+(-1.750)X_1+(-0.220)X_2$. Eine unstandardisierte Steigung verwendet die ursprünglichen Messeinheiten. Ein standardisierter Koeffizient beschreibt dagegen die angepasste Veränderung in Standardabweichungen der Ergebnisvariable bei einer Zunahme des Prädiktors um eine Standardabweichung, bedingt auf den anderen Prädiktor.

**Berechnung durchführen, Teil (b)**

Wenn der Prädiktor „Monate Archiverfahrung“ festgehalten wird, geht eine Zunahme des Prädiktors „Übungssitzungen mit Checkliste“ um eine Einheit mit einer angepassten Veränderung der Ergebnisvariable „Suchzeit“ um -1.750 Minuten einher. Wenn der Prädiktor „Übungssitzungen mit Checkliste“ festgehalten wird, geht eine Zunahme des Prädiktors „Monate Archiverfahrung“ um eine Einheit mit einer angepassten Veränderung der Ergebnisvariable um -0.220 Minuten einher. Dies sind bedingte Zusammenhänge und nicht automatisch kausale Effekte.

**Berechnung durchführen, Teil (c)**

Für $X_1$ gilt $t=-1.750/0.467=-3.747$ mit 69 Freiheitsgraden und damit $p = 0.0004$; folglich wird die Nullhypothese für den Koeffizienten bei $\alpha=.05$ verworfen. Für $X_2$ gilt $t=-0.220/0.093=-2.366$ und damit $p = 0.0208$; folglich wird die Nullhypothese für den Koeffizienten verworfen. Jeder Test betrifft diesen einen Populationskoeffizienten, bedingt auf genau den anderen Term in diesem Modell.

**Ergebnis interpretieren und prüfen, Teil (d)**

$R^2=0.316$ bedeutet, dass das angepasste Modell mit zwei Prädiktoren 31.6% der Stichprobenvariation der Ergebnisvariable „Suchzeit“ darstellt. Das korrigierte $R^2=0.296$ berücksichtigt innerhalb der Stichprobe, dass zwei Steigungen geschätzt wurden. Es ist kein Test an neuen Daten. Der Residualstandardfehler besagt, dass die beobachteten Ergebnisse unter dem Modell typischerweise noch ungefähr 4.80 Minuten von ihren angepassten Werten abweichen. Die standardisierten Steigungen -0.407 und -0.257 unterscheiden sich von den bivariaten Korrelationen -0.510 und -0.420, weil jede Steigung den bedingten Zusammenhang eines Prädiktors von der mit dem anderen Prädiktor geteilten Variation trennt.

### T07-A01-V03: Leseroutinen und Textverständnis

**Vor dem Rechnen begründen, Teil (a)**

Die angepasste Gleichung lautet $\hat Y=42.000+(1.850)X_1+(0.280)X_2$. Eine unstandardisierte Steigung verwendet die ursprünglichen Messeinheiten. Ein standardisierter Koeffizient beschreibt dagegen die angepasste Veränderung in Standardabweichungen der Ergebnisvariable bei einer Zunahme des Prädiktors um eine Standardabweichung, bedingt auf den anderen Prädiktor.

**Berechnung durchführen, Teil (b)**

Wenn der Prädiktor „Ausgangswert des Wortschatzes“ festgehalten wird, geht eine Zunahme des Prädiktors „wöchentliche Lesestunden“ um eine Einheit mit einer angepassten Veränderung der Ergebnisvariable „Punktwert im Textverständnis“ um 1.850 Punkte einher. Wenn der Prädiktor „wöchentliche Lesestunden“ festgehalten wird, geht eine Zunahme des Prädiktors „Ausgangswert des Wortschatzes“ um eine Einheit mit einer angepassten Veränderung der Ergebnisvariable um 0.280 Punkte einher. Dies sind bedingte Zusammenhänge und nicht automatisch kausale Effekte.

**Berechnung durchführen, Teil (c)**

Für $X_1$ gilt $t=1.850/0.443=4.179$ mit 92 Freiheitsgraden und damit $p < 0.0001$; folglich wird die Nullhypothese für den Koeffizienten bei $\alpha=.05$ verworfen. Für $X_2$ gilt $t=0.280/0.084=3.340$ und damit $p = 0.0012$; folglich wird die Nullhypothese für den Koeffizienten verworfen. Jeder Test betrifft diesen einen Populationskoeffizienten, bedingt auf genau den anderen Term in diesem Modell.

**Ergebnis interpretieren und prüfen, Teil (d)**

$R^2=0.322$ bedeutet, dass das angepasste Modell mit zwei Prädiktoren 32.2% der Stichprobenvariation der Ergebnisvariable „Punktwert im Textverständnis“ darstellt. Das korrigierte $R^2=0.308$ berücksichtigt innerhalb der Stichprobe, dass zwei Steigungen geschätzt wurden. Es ist kein Test an neuen Daten. Der Residualstandardfehler besagt, dass die beobachteten Ergebnisse unter dem Modell typischerweise noch ungefähr 5.10 Punkte von ihren angepassten Werten abweichen. Die standardisierten Steigungen 0.383 und 0.306 unterscheiden sich von den bivariaten Korrelationen 0.490 und 0.440, weil jede Steigung den bedingten Zusammenhang eines Prädiktors von der mit dem anderen Prädiktor geteilten Variation trennt.

### T07-A01-V04: Streckenübung und Navigationszeit

**Vor dem Rechnen begründen, Teil (a)**

Die angepasste Gleichung lautet $\hat Y=65.000+(-2.100)X_1+(-0.160)X_2$. Eine unstandardisierte Steigung verwendet die ursprünglichen Messeinheiten. Ein standardisierter Koeffizient beschreibt dagegen die angepasste Veränderung in Standardabweichungen der Ergebnisvariable bei einer Zunahme des Prädiktors um eine Standardabweichung, bedingt auf den anderen Prädiktor.

**Berechnung durchführen, Teil (b)**

Wenn der Prädiktor „Punktwert der Streckenkenntnis“ festgehalten wird, geht eine Zunahme des Prädiktors „Versuche zur Streckenübung“ um eine Einheit mit einer angepassten Veränderung der Ergebnisvariable „Navigationszeit“ um -2.100 Minuten einher. Wenn der Prädiktor „Versuche zur Streckenübung“ festgehalten wird, geht eine Zunahme des Prädiktors „Punktwert der Streckenkenntnis“ um eine Einheit mit einer angepassten Veränderung der Ergebnisvariable um -0.160 Minuten einher. Dies sind bedingte Zusammenhänge und nicht automatisch kausale Effekte.

**Berechnung durchführen, Teil (c)**

Für $X_1$ gilt $t=-2.100/0.519=-4.043$ mit 65 Freiheitsgraden und damit $p = 0.0001$; folglich wird die Nullhypothese für den Koeffizienten bei $\alpha=.05$ verworfen. Für $X_2$ gilt $t=-0.160/0.080=-1.997$ und damit $p = 0.0500$; folglich wird die Nullhypothese für den Koeffizienten nicht verworfen. Jeder Test betrifft diesen einen Populationskoeffizienten, bedingt auf genau den anderen Term in diesem Modell.

**Ergebnis interpretieren und prüfen, Teil (d)**

$R^2=0.322$ bedeutet, dass das angepasste Modell mit zwei Prädiktoren 32.2% der Stichprobenvariation der Ergebnisvariable „Navigationszeit“ darstellt. Das korrigierte $R^2=0.302$ berücksichtigt innerhalb der Stichprobe, dass zwei Steigungen geschätzt wurden. Es ist kein Test an neuen Daten. Der Residualstandardfehler besagt, dass die beobachteten Ergebnisse unter dem Modell typischerweise noch ungefähr 6.00 Minuten von ihren angepassten Werten abweichen. Die standardisierten Steigungen -0.446 und -0.220 unterscheiden sich von den bivariaten Korrelationen -0.530 und -0.390, weil jede Steigung den bedingten Zusammenhang eines Prädiktors von der mit dem anderen Prädiktor geteilten Variation trennt.

### T07-A01-V05: Suchübung und Kataloggenauigkeit

**Vor dem Rechnen begründen, Teil (a)**

Die angepasste Gleichung lautet $\hat Y=48.000+(1.550)X_1+(0.340)X_2$. Eine unstandardisierte Steigung verwendet die ursprünglichen Messeinheiten. Ein standardisierter Koeffizient beschreibt dagegen die angepasste Veränderung in Standardabweichungen der Ergebnisvariable bei einer Zunahme des Prädiktors um eine Standardabweichung, bedingt auf den anderen Prädiktor.

**Berechnung durchführen, Teil (b)**

Wenn der Prädiktor „Punktwert des Katalogvorwissens“ festgehalten wird, geht eine Zunahme des Prädiktors „Suchübungsblöcke“ um eine Einheit mit einer angepassten Veränderung der Ergebnisvariable „Punktwert der Kataloggenauigkeit“ um 1.550 Punkte einher. Wenn der Prädiktor „Suchübungsblöcke“ festgehalten wird, geht eine Zunahme des Prädiktors „Punktwert des Katalogvorwissens“ um eine Einheit mit einer angepassten Veränderung der Ergebnisvariable um 0.340 Punkte einher. Dies sind bedingte Zusammenhänge und nicht automatisch kausale Effekte.

**Berechnung durchführen, Teil (c)**

Für $X_1$ gilt $t=1.550/0.413=3.752$ mit 107 Freiheitsgraden und damit $p = 0.0003$; folglich wird die Nullhypothese für den Koeffizienten bei $\alpha=.05$ verworfen. Für $X_2$ gilt $t=0.340/0.107=3.180$ und damit $p = 0.0019$; folglich wird die Nullhypothese für den Koeffizienten verworfen. Jeder Test betrifft diesen einen Populationskoeffizienten, bedingt auf genau den anderen Term in diesem Modell.

**Ergebnis interpretieren und prüfen, Teil (d)**

$R^2=0.280$ bedeutet, dass das angepasste Modell mit zwei Prädiktoren 28.0% der Stichprobenvariation der Ergebnisvariable „Punktwert der Kataloggenauigkeit“ darstellt. Das korrigierte $R^2=0.266$ berücksichtigt innerhalb der Stichprobe, dass zwei Steigungen geschätzt wurden. Es ist kein Test an neuen Daten. Der Residualstandardfehler besagt, dass die beobachteten Ergebnisse unter dem Modell typischerweise noch ungefähr 4.60 Punkte von ihren angepassten Werten abweichen. Die standardisierten Steigungen 0.339 und 0.288 unterscheiden sich von den bivariaten Korrelationen 0.460 und 0.430, weil jede Steigung den bedingten Zusammenhang eines Prädiktors von der mit dem anderen Prädiktor geteilten Variation trennt.

### T07-A01-V06: Workshopteilnahme und Selbstvertrauen

**Vor dem Rechnen begründen, Teil (a)**

Die angepasste Gleichung lautet $\hat Y=30.000+(2.200)X_1+(0.450)X_2$. Eine unstandardisierte Steigung verwendet die ursprünglichen Messeinheiten. Ein standardisierter Koeffizient beschreibt dagegen die angepasste Veränderung in Standardabweichungen der Ergebnisvariable bei einer Zunahme des Prädiktors um eine Standardabweichung, bedingt auf den anderen Prädiktor.

**Berechnung durchführen, Teil (b)**

Wenn der Prädiktor „Ausgangswert des Selbstvertrauens“ festgehalten wird, geht eine Zunahme des Prädiktors „Workshopsitzungen“ um eine Einheit mit einer angepassten Veränderung der Ergebnisvariable „Punktwert des Selbstvertrauens“ um 2.200 Punkte einher. Wenn der Prädiktor „Workshopsitzungen“ festgehalten wird, geht eine Zunahme des Prädiktors „Ausgangswert des Selbstvertrauens“ um eine Einheit mit einer angepassten Veränderung der Ergebnisvariable um 0.450 Punkte einher. Dies sind bedingte Zusammenhänge und nicht automatisch kausale Effekte.

**Berechnung durchführen, Teil (c)**

Für $X_1$ gilt $t=2.200/0.546=4.027$ mit 73 Freiheitsgraden und damit $p = 0.0001$; folglich wird die Nullhypothese für den Koeffizienten bei $\alpha=.05$ verworfen. Für $X_2$ gilt $t=0.450/0.125=3.590$ und damit $p = 0.0006$; folglich wird die Nullhypothese für den Koeffizienten verworfen. Jeder Test betrifft diesen einen Populationskoeffizienten, bedingt auf genau den anderen Term in diesem Modell.

**Ergebnis interpretieren und prüfen, Teil (d)**

$R^2=0.363$ bedeutet, dass das angepasste Modell mit zwei Prädiktoren 36.3% der Stichprobenvariation der Ergebnisvariable „Punktwert des Selbstvertrauens“ darstellt. Das korrigierte $R^2=0.345$ berücksichtigt innerhalb der Stichprobe, dass zwei Steigungen geschätzt wurden. Es ist kein Test an neuen Daten. Der Residualstandardfehler besagt, dass die beobachteten Ergebnisse unter dem Modell typischerweise noch ungefähr 5.00 Punkte von ihren angepassten Werten abweichen. Die standardisierten Steigungen 0.395 und 0.352 unterscheiden sich von den bivariaten Korrelationen 0.500 und 0.470, weil jede Steigung den bedingten Zusammenhang eines Prädiktors von der mit dem anderen Prädiktor geteilten Variation trennt.

### T07-A01-V07: Konzentrationsblöcke und Aufgabengenauigkeit

**Vor dem Rechnen begründen, Teil (a)**

Die angepasste Gleichung lautet $\hat Y=55.000+(1.300)X_1+(1.150)X_2$. Eine unstandardisierte Steigung verwendet die ursprünglichen Messeinheiten. Ein standardisierter Koeffizient beschreibt dagegen die angepasste Veränderung in Standardabweichungen der Ergebnisvariable bei einer Zunahme des Prädiktors um eine Standardabweichung, bedingt auf den anderen Prädiktor.

**Berechnung durchführen, Teil (b)**

Wenn der Prädiktor „Schlafdauer in Stunden“ festgehalten wird, geht eine Zunahme des Prädiktors „benachrichtigungsfreie Blöcke“ um eine Einheit mit einer angepassten Veränderung der Ergebnisvariable „Punktwert der Aufgabengenauigkeit“ um 1.300 Punkte einher. Wenn der Prädiktor „benachrichtigungsfreie Blöcke“ festgehalten wird, geht eine Zunahme des Prädiktors „Schlafdauer in Stunden“ um eine Einheit mit einer angepassten Veränderung der Ergebnisvariable um 1.150 Punkte einher. Dies sind bedingte Zusammenhänge und nicht automatisch kausale Effekte.

**Berechnung durchführen, Teil (c)**

Für $X_1$ gilt $t=1.300/0.330=3.935$ mit 117 Freiheitsgraden und damit $p = 0.0001$; folglich wird die Nullhypothese für den Koeffizienten bei $\alpha=.05$ verworfen. Für $X_2$ gilt $t=1.150/0.335=3.438$ und damit $p = 0.0008$; folglich wird die Nullhypothese für den Koeffizienten verworfen. Jeder Test betrifft diesen einen Populationskoeffizienten, bedingt auf genau den anderen Term in diesem Modell.

**Ergebnis interpretieren und prüfen, Teil (d)**

$R^2=0.244$ bedeutet, dass das angepasste Modell mit zwei Prädiktoren 24.4% der Stichprobenvariation der Ergebnisvariable „Punktwert der Aufgabengenauigkeit“ darstellt. Das korrigierte $R^2=0.231$ berücksichtigt innerhalb der Stichprobe, dass zwei Steigungen geschätzt wurden. Es ist kein Test an neuen Daten. Der Residualstandardfehler besagt, dass die beobachteten Ergebnisse unter dem Modell typischerweise noch ungefähr 4.30 Punkte von ihren angepassten Werten abweichen. Die standardisierten Steigungen 0.329 und 0.288 unterscheiden sich von den bivariaten Korrelationen 0.410 und 0.380, weil jede Steigung den bedingten Zusammenhang eines Prädiktors von der mit dem anderen Prädiktor geteilten Variation trennt.

### T07-A01-V08: Museumsbesuche und historisches Wissen

**Vor dem Rechnen begründen, Teil (a)**

Die angepasste Gleichung lautet $\hat Y=40.000+(2.650)X_1+(0.370)X_2$. Eine unstandardisierte Steigung verwendet die ursprünglichen Messeinheiten. Ein standardisierter Koeffizient beschreibt dagegen die angepasste Veränderung in Standardabweichungen der Ergebnisvariable bei einer Zunahme des Prädiktors um eine Standardabweichung, bedingt auf den anderen Prädiktor.

**Berechnung durchführen, Teil (b)**

Wenn der Prädiktor „Punktwert des geschichtlichen Vorwissens“ festgehalten wird, geht eine Zunahme des Prädiktors „Museumsbesuche“ um eine Einheit mit einer angepassten Veränderung der Ergebnisvariable „Punktwert des historischen Wissens“ um 2.650 Punkte einher. Wenn der Prädiktor „Museumsbesuche“ festgehalten wird, geht eine Zunahme des Prädiktors „Punktwert des geschichtlichen Vorwissens“ um eine Einheit mit einer angepassten Veränderung der Ergebnisvariable um 0.370 Punkte einher. Dies sind bedingte Zusammenhänge und nicht automatisch kausale Effekte.

**Berechnung durchführen, Teil (c)**

Für $X_1$ gilt $t=2.650/0.619=4.283$ mit 81 Freiheitsgraden und damit $p < 0.0001$; folglich wird die Nullhypothese für den Koeffizienten bei $\alpha=.05$ verworfen. Für $X_2$ gilt $t=0.370/0.118=3.144$ und damit $p = 0.0023$; folglich wird die Nullhypothese für den Koeffizienten verworfen. Jeder Test betrifft diesen einen Populationskoeffizienten, bedingt auf genau den anderen Term in diesem Modell.

**Ergebnis interpretieren und prüfen, Teil (d)**

$R^2=0.350$ bedeutet, dass das angepasste Modell mit zwei Prädiktoren 35.0% der Stichprobenvariation der Ergebnisvariable „Punktwert des historischen Wissens“ darstellt. Das korrigierte $R^2=0.334$ berücksichtigt innerhalb der Stichprobe, dass zwei Steigungen geschätzt wurden. Es ist kein Test an neuen Daten. Der Residualstandardfehler besagt, dass die beobachteten Ergebnisse unter dem Modell typischerweise noch ungefähr 5.50 Punkte von ihren angepassten Werten abweichen. Die standardisierten Steigungen 0.411 und 0.302 unterscheiden sich von den bivariaten Korrelationen 0.520 und 0.450, weil jede Steigung den bedingten Zusammenhang eines Prädiktors von der mit dem anderen Prädiktor geteilten Variation trennt.

### T07-A01-V09: Peer-Feedback und Überarbeitungsqualität

**Vor dem Rechnen begründen, Teil (a)**

Die angepasste Gleichung lautet $\hat Y=44.000+(2.100)X_1+(0.300)X_2$. Eine unstandardisierte Steigung verwendet die ursprünglichen Messeinheiten. Ein standardisierter Koeffizient beschreibt dagegen die angepasste Veränderung in Standardabweichungen der Ergebnisvariable bei einer Zunahme des Prädiktors um eine Standardabweichung, bedingt auf den anderen Prädiktor.

**Berechnung durchführen, Teil (b)**

Wenn der Prädiktor „Ausgangswert der Schreibqualität“ festgehalten wird, geht eine Zunahme des Prädiktors „Runden mit Peer-Feedback“ um eine Einheit mit einer angepassten Veränderung der Ergebnisvariable „Punktwert der Überarbeitungsqualität“ um 2.100 Punkte einher. Wenn der Prädiktor „Runden mit Peer-Feedback“ festgehalten wird, geht eine Zunahme des Prädiktors „Ausgangswert der Schreibqualität“ um eine Einheit mit einer angepassten Veränderung der Ergebnisvariable um 0.300 Punkte einher. Dies sind bedingte Zusammenhänge und nicht automatisch kausale Effekte.

**Berechnung durchführen, Teil (c)**

Für $X_1$ gilt $t=2.100/0.507=4.145$ mit 89 Freiheitsgraden und damit $p < 0.0001$; folglich wird die Nullhypothese für den Koeffizienten bei $\alpha=.05$ verworfen. Für $X_2$ gilt $t=0.300/0.104=2.877$ und damit $p = 0.0050$; folglich wird die Nullhypothese für den Koeffizienten verworfen. Jeder Test betrifft diesen einen Populationskoeffizienten, bedingt auf genau den anderen Term in diesem Modell.

**Ergebnis interpretieren und prüfen, Teil (d)**

$R^2=0.296$ bedeutet, dass das angepasste Modell mit zwei Prädiktoren 29.6% der Stichprobenvariation der Ergebnisvariable „Punktwert der Überarbeitungsqualität“ darstellt. Das korrigierte $R^2=0.280$ berücksichtigt innerhalb der Stichprobe, dass zwei Steigungen geschätzt wurden. Es ist kein Test an neuen Daten. Der Residualstandardfehler besagt, dass die beobachteten Ergebnisse unter dem Modell typischerweise noch ungefähr 4.90 Punkte von ihren angepassten Werten abweichen. Die standardisierten Steigungen 0.391 und 0.271 unterscheiden sich von den bivariaten Korrelationen 0.480 und 0.400, weil jede Steigung den bedingten Zusammenhang eines Prädiktors von der mit dem anderen Prädiktor geteilten Variation trennt.

### T07-A01-V10: Planungssitzungen und Bearbeitungszeit

**Vor dem Rechnen begründen, Teil (a)**

Die angepasste Gleichung lautet $\hat Y=82.000+(-1.900)X_1+(0.850)X_2$. Eine unstandardisierte Steigung verwendet die ursprünglichen Messeinheiten. Ein standardisierter Koeffizient beschreibt dagegen die angepasste Veränderung in Standardabweichungen der Ergebnisvariable bei einer Zunahme des Prädiktors um eine Standardabweichung, bedingt auf den anderen Prädiktor.

**Berechnung durchführen, Teil (b)**

Wenn der Prädiktor „Punktwert der Aufgabenkomplexität“ festgehalten wird, geht eine Zunahme des Prädiktors „Planungssitzungen“ um eine Einheit mit einer angepassten Veränderung der Ergebnisvariable „Bearbeitungszeit“ um -1.900 Minuten einher. Wenn der Prädiktor „Planungssitzungen“ festgehalten wird, geht eine Zunahme des Prädiktors „Punktwert der Aufgabenkomplexität“ um eine Einheit mit einer angepassten Veränderung der Ergebnisvariable um 0.850 Minuten einher. Dies sind bedingte Zusammenhänge und nicht automatisch kausale Effekte.

**Berechnung durchführen, Teil (c)**

Für $X_1$ gilt $t=-1.900/0.384=-4.954$ mit 85 Freiheitsgraden und damit $p < 0.0001$; folglich wird die Nullhypothese für den Koeffizienten bei $\alpha=.05$ verworfen. Für $X_2$ gilt $t=0.850/0.185=4.590$ und damit $p < 0.0001$; folglich wird die Nullhypothese für den Koeffizienten verworfen. Jeder Test betrifft diesen einen Populationskoeffizienten, bedingt auf genau den anderen Term in diesem Modell.

**Ergebnis interpretieren und prüfen, Teil (d)**

$R^2=0.361$ bedeutet, dass das angepasste Modell mit zwei Prädiktoren 36.1% der Stichprobenvariation der Ergebnisvariable „Bearbeitungszeit“ darstellt. Das korrigierte $R^2=0.346$ berücksichtigt innerhalb der Stichprobe, dass zwei Steigungen geschätzt wurden. Es ist kein Test an neuen Daten. Der Residualstandardfehler besagt, dass die beobachteten Ergebnisse unter dem Modell typischerweise noch ungefähr 5.70 Minuten von ihren angepassten Werten abweichen. Die standardisierten Steigungen -0.430 und 0.398 unterscheiden sich von den bivariaten Korrelationen -0.450 und 0.420, weil jede Steigung den bedingten Zusammenhang eines Prädiktors von der mit dem anderen Prädiktor geteilten Variation trennt.

## A02: Eine vorab festgelegte Folge verschachtelter Modelle vergleichen

### T07-A02-V01: Begleitete Übung und statistisches Denken

**Vor dem Rechnen begründen, Teil (a)**

Wende $SSE=1840.0(1-R^2)$ an und subtrahiere aufeinanderfolgende $R^2$-Werte.

**Berechnung durchführen, Teil (b)**

Setze für jedes Modell seine eigene Prädiktorenzahl in die korrigierte Formel ein:

| Modell | SSE | Veränderung in R-Quadrat | Korrigiertes R-Quadrat |
| --- | --- | --- | --- |
| M1 | 1435.20 | kein späterer Schritt | 0.2085 |
| M2 | 1159.20 | 0.150 | 0.3512 |
| M3 | 1122.40 | 0.020 | 0.3623 |

**Berechnung durchführen, Teil (c)**

Das gewöhnliche $R^2$ steigt von 0.370 auf 0.390, wenn der Prädiktor „Zahl der Reflexionssitzungen“ hinzugefügt wird. Der Zuwachs beträgt 0.020, also 2.0 Prozentpunkte der Stichprobenvariation. Das gewöhnliche $R^2$ kann nicht sinken, wenn diesem Modell mit denselben Fällen und demselben Achsenabschnitt ein Prädiktor hinzugefügt wird. Das korrigierte $R^2$ steigt von 0.3512 auf 0.3623, weil es den Anpassungsgewinn gegen die zusätzlich geschätzte Steigung abwägt. Diese Korrektur ist deskriptiv und gilt innerhalb der Stichprobe.

**Berechnung durchführen, Teil (d)**

Die eingeschränkte Gleichung lautet $Y=\beta_0+\beta_1X_1+\beta_2X_2+\varepsilon$. Die uneingeschränkte Gleichung ergänzt den Prädiktor „Zahl der Reflexionssitzungen“: $Y=\beta_0+\beta_1X_1+\beta_2X_2+\beta_3X_3+\varepsilon$. Die Nullhypothese lautet $H_0:\beta_3=0$, bedingt auf die bereits in M2 enthaltenen Terme. Die inkrementelle Statistik beträgt $F=[(0.390-0.370)/1]/[(1-0.390)/(70-3-1)]=2.1639$ mit 1 und 66 Freiheitsgraden. Der p-Wert beträgt 0.1460. Der hinzugefügte Term erfüllt nicht das 5%-Kriterium.

**Ergebnis interpretieren und prüfen, Teil (e)**

M1 ist in M2 enthalten und M2 ist in M3 enthalten: Wird jeder neu hinzugefügte Koeffizient auf null gesetzt, entsteht wieder das vorherige Modell. Die Ergebnisvariable, die Fälle und der Achsenabschnitt bleiben ebenfalls gleich. Deshalb lassen sich die Anpassungsänderungen als verschachtelte Schritte vergleichen. Die Folge randomisiert keine Prädiktoren, schliesst ausgelassene Variablen nicht aus, beweist keinen Mechanismus und misst die Vorhersage für neue Fälle nicht. Diese Fragen erfordern Angaben zum Design und eine getrennte Validierung.

### T07-A02-V02: Arbeitsablauf im Archiv und Suchzeit

**Vor dem Rechnen begründen, Teil (a)**

Wende $SSE=1320.0(1-R^2)$ an und subtrahiere aufeinanderfolgende $R^2$-Werte.

**Berechnung durchführen, Teil (b)**

Setze für jedes Modell seine eigene Prädiktorenzahl in die korrigierte Formel ein:

| Modell | SSE | Veränderung in R-Quadrat | Korrigiertes R-Quadrat |
| --- | --- | --- | --- |
| M1 | 950.40 | kein späterer Schritt | 0.2708 |
| M2 | 858.00 | 0.070 | 0.3331 |
| M3 | 856.68 | 0.001 | 0.3254 |

**Berechnung durchführen, Teil (c)**

Das gewöhnliche $R^2$ steigt von 0.350 auf 0.351, wenn der Prädiktor „Punktwert zur Katalogvertrautheit“ hinzugefügt wird. Der Zuwachs beträgt 0.001, also 0.1 Prozentpunkte der Stichprobenvariation. Das gewöhnliche $R^2$ kann nicht sinken, wenn diesem Modell mit denselben Fällen und demselben Achsenabschnitt ein Prädiktor hinzugefügt wird. Das korrigierte $R^2$ sinkt von 0.3331 auf 0.3254, weil es den Anpassungsgewinn gegen die zusätzlich geschätzte Steigung abwägt. Diese Korrektur ist deskriptiv und gilt innerhalb der Stichprobe.

**Berechnung durchführen, Teil (d)**

Die eingeschränkte Gleichung lautet $Y=\beta_0+\beta_1X_1+\beta_2X_2+\varepsilon$. Die uneingeschränkte Gleichung ergänzt den Prädiktor „Punktwert zur Katalogvertrautheit“: $Y=\beta_0+\beta_1X_1+\beta_2X_2+\beta_3X_3+\varepsilon$. Die Nullhypothese lautet $H_0:\beta_3=0$, bedingt auf die bereits in M2 enthaltenen Terme. Die inkrementelle Statistik beträgt $F=[(0.351-0.350)/1]/[(1-0.351)/(80-3-1)]=0.1171$ mit 1 und 76 Freiheitsgraden. Der p-Wert beträgt 0.7331. Der hinzugefügte Term erfüllt nicht das 5%-Kriterium.

**Ergebnis interpretieren und prüfen, Teil (e)**

M1 ist in M2 enthalten und M2 ist in M3 enthalten: Wird jeder neu hinzugefügte Koeffizient auf null gesetzt, entsteht wieder das vorherige Modell. Die Ergebnisvariable, die Fälle und der Achsenabschnitt bleiben ebenfalls gleich. Deshalb lassen sich die Anpassungsänderungen als verschachtelte Schritte vergleichen. Die Folge randomisiert keine Prädiktoren, schliesst ausgelassene Variablen nicht aus, beweist keinen Mechanismus und misst die Vorhersage für neue Fälle nicht. Diese Fragen erfordern Angaben zum Design und eine getrennte Validierung.

### T07-A02-V03: Leseroutinen und Textverständnis

**Vor dem Rechnen begründen, Teil (a)**

Wende $SSE=1560.0(1-R^2)$ an und subtrahiere aufeinanderfolgende $R^2$-Werte.

**Berechnung durchführen, Teil (b)**

Setze für jedes Modell seine eigene Prädiktorenzahl in die korrigierte Formel ein:

| Modell | SSE | Veränderung in R-Quadrat | Korrigiertes R-Quadrat |
| --- | --- | --- | --- |
| M1 | 1279.20 | kein späterer Schritt | 0.1659 |
| M2 | 1076.40 | 0.130 | 0.2858 |
| M3 | 998.40 | 0.050 | 0.3257 |

**Berechnung durchführen, Teil (c)**

Das gewöhnliche $R^2$ steigt von 0.310 auf 0.360, wenn der Prädiktor „Zahl der Annotationssitzungen“ hinzugefügt wird. Der Zuwachs beträgt 0.050, also 5.0 Prozentpunkte der Stichprobenvariation. Das gewöhnliche $R^2$ kann nicht sinken, wenn diesem Modell mit denselben Fällen und demselben Achsenabschnitt ein Prädiktor hinzugefügt wird. Das korrigierte $R^2$ steigt von 0.2858 auf 0.3257, weil es den Anpassungsgewinn gegen die zusätzlich geschätzte Steigung abwägt. Diese Korrektur ist deskriptiv und gilt innerhalb der Stichprobe.

**Berechnung durchführen, Teil (d)**

Die eingeschränkte Gleichung lautet $Y=\beta_0+\beta_1X_1+\beta_2X_2+\varepsilon$. Die uneingeschränkte Gleichung ergänzt den Prädiktor „Zahl der Annotationssitzungen“: $Y=\beta_0+\beta_1X_1+\beta_2X_2+\beta_3X_3+\varepsilon$. Die Nullhypothese lautet $H_0:\beta_3=0$, bedingt auf die bereits in M2 enthaltenen Terme. Die inkrementelle Statistik beträgt $F=[(0.360-0.310)/1]/[(1-0.360)/(60-3-1)]=4.3750$ mit 1 und 56 Freiheitsgraden. Der p-Wert beträgt 0.0410. Der hinzugefügte Term erfüllt das 5%-Kriterium.

**Ergebnis interpretieren und prüfen, Teil (e)**

M1 ist in M2 enthalten und M2 ist in M3 enthalten: Wird jeder neu hinzugefügte Koeffizient auf null gesetzt, entsteht wieder das vorherige Modell. Die Ergebnisvariable, die Fälle und der Achsenabschnitt bleiben ebenfalls gleich. Deshalb lassen sich die Anpassungsänderungen als verschachtelte Schritte vergleichen. Die Folge randomisiert keine Prädiktoren, schliesst ausgelassene Variablen nicht aus, beweist keinen Mechanismus und misst die Vorhersage für neue Fälle nicht. Diese Fragen erfordern Angaben zum Design und eine getrennte Validierung.

### T07-A02-V04: Streckenübung und Navigationszeit

**Vor dem Rechnen begründen, Teil (a)**

Wende $SSE=2100.0(1-R^2)$ an und subtrahiere aufeinanderfolgende $R^2$-Werte.

**Berechnung durchführen, Teil (b)**

Setze für jedes Modell seine eigene Prädiktorenzahl in die korrigierte Formel ein:

| Modell | SSE | Veränderung in R-Quadrat | Korrigiertes R-Quadrat |
| --- | --- | --- | --- |
| M1 | 1575.00 | kein späterer Schritt | 0.2415 |
| M2 | 1407.00 | 0.080 | 0.3146 |
| M3 | 1398.60 | 0.004 | 0.3108 |

**Berechnung durchführen, Teil (c)**

Das gewöhnliche $R^2$ steigt von 0.330 auf 0.334, wenn der Prädiktor „Punktwert zur Erinnerung an Orientierungspunkte“ hinzugefügt wird. Der Zuwachs beträgt 0.004, also 0.4 Prozentpunkte der Stichprobenvariation. Das gewöhnliche $R^2$ kann nicht sinken, wenn diesem Modell mit denselben Fällen und demselben Achsenabschnitt ein Prädiktor hinzugefügt wird. Das korrigierte $R^2$ sinkt von 0.3146 auf 0.3108, weil es den Anpassungsgewinn gegen die zusätzlich geschätzte Steigung abwägt. Diese Korrektur ist deskriptiv und gilt innerhalb der Stichprobe.

**Berechnung durchführen, Teil (d)**

Die eingeschränkte Gleichung lautet $Y=\beta_0+\beta_1X_1+\beta_2X_2+\varepsilon$. Die uneingeschränkte Gleichung ergänzt den Prädiktor „Punktwert zur Erinnerung an Orientierungspunkte“: $Y=\beta_0+\beta_1X_1+\beta_2X_2+\beta_3X_3+\varepsilon$. Die Nullhypothese lautet $H_0:\beta_3=0$, bedingt auf die bereits in M2 enthaltenen Terme. Die inkrementelle Statistik beträgt $F=[(0.334-0.330)/1]/[(1-0.334)/(90-3-1)]=0.5165$ mit 1 und 86 Freiheitsgraden. Der p-Wert beträgt 0.4743. Der hinzugefügte Term erfüllt nicht das 5%-Kriterium.

**Ergebnis interpretieren und prüfen, Teil (e)**

M1 ist in M2 enthalten und M2 ist in M3 enthalten: Wird jeder neu hinzugefügte Koeffizient auf null gesetzt, entsteht wieder das vorherige Modell. Die Ergebnisvariable, die Fälle und der Achsenabschnitt bleiben ebenfalls gleich. Deshalb lassen sich die Anpassungsänderungen als verschachtelte Schritte vergleichen. Die Folge randomisiert keine Prädiktoren, schliesst ausgelassene Variablen nicht aus, beweist keinen Mechanismus und misst die Vorhersage für neue Fälle nicht. Diese Fragen erfordern Angaben zum Design und eine getrennte Validierung.

### T07-A02-V05: Suchübung und Kataloggenauigkeit

**Vor dem Rechnen begründen, Teil (a)**

Wende $SSE=1750.0(1-R^2)$ an und subtrahiere aufeinanderfolgende $R^2$-Werte.

**Berechnung durchführen, Teil (b)**

Setze für jedes Modell seine eigene Prädiktorenzahl in die korrigierte Formel ein:

| Modell | SSE | Veränderung in R-Quadrat | Korrigiertes R-Quadrat |
| --- | --- | --- | --- |
| M1 | 1225.00 | kein späterer Schritt | 0.2929 |
| M2 | 1032.50 | 0.110 | 0.3978 |
| M3 | 980.00 | 0.030 | 0.4225 |

**Berechnung durchführen, Teil (c)**

Das gewöhnliche $R^2$ steigt von 0.410 auf 0.440, wenn der Prädiktor „Punktwert der Suchplanung“ hinzugefügt wird. Der Zuwachs beträgt 0.030, also 3.0 Prozentpunkte der Stichprobenvariation. Das gewöhnliche $R^2$ kann nicht sinken, wenn diesem Modell mit denselben Fällen und demselben Achsenabschnitt ein Prädiktor hinzugefügt wird. Das korrigierte $R^2$ steigt von 0.3978 auf 0.4225, weil es den Anpassungsgewinn gegen die zusätzlich geschätzte Steigung abwägt. Diese Korrektur ist deskriptiv und gilt innerhalb der Stichprobe.

**Berechnung durchführen, Teil (d)**

Die eingeschränkte Gleichung lautet $Y=\beta_0+\beta_1X_1+\beta_2X_2+\varepsilon$. Die uneingeschränkte Gleichung ergänzt den Prädiktor „Punktwert der Suchplanung“: $Y=\beta_0+\beta_1X_1+\beta_2X_2+\beta_3X_3+\varepsilon$. Die Nullhypothese lautet $H_0:\beta_3=0$, bedingt auf die bereits in M2 enthaltenen Terme. Die inkrementelle Statistik beträgt $F=[(0.440-0.410)/1]/[(1-0.440)/(100-3-1)]=5.1429$ mit 1 und 96 Freiheitsgraden. Der p-Wert beträgt 0.0256. Der hinzugefügte Term erfüllt das 5%-Kriterium.

**Ergebnis interpretieren und prüfen, Teil (e)**

M1 ist in M2 enthalten und M2 ist in M3 enthalten: Wird jeder neu hinzugefügte Koeffizient auf null gesetzt, entsteht wieder das vorherige Modell. Die Ergebnisvariable, die Fälle und der Achsenabschnitt bleiben ebenfalls gleich. Deshalb lassen sich die Anpassungsänderungen als verschachtelte Schritte vergleichen. Die Folge randomisiert keine Prädiktoren, schliesst ausgelassene Variablen nicht aus, beweist keinen Mechanismus und misst die Vorhersage für neue Fälle nicht. Diese Fragen erfordern Angaben zum Design und eine getrennte Validierung.

### T07-A02-V06: Workshopteilnahme und Selbstvertrauen

**Vor dem Rechnen begründen, Teil (a)**

Wende $SSE=980.0(1-R^2)$ an und subtrahiere aufeinanderfolgende $R^2$-Werte.

**Berechnung durchführen, Teil (b)**

Setze für jedes Modell seine eigene Prädiktorenzahl in die korrigierte Formel ein:

| Modell | SSE | Veränderung in R-Quadrat | Korrigiertes R-Quadrat |
| --- | --- | --- | --- |
| M1 | 823.20 | kein späterer Schritt | 0.1442 |
| M2 | 695.80 | 0.130 | 0.2627 |
| M3 | 693.84 | 0.002 | 0.2504 |

**Berechnung durchführen, Teil (c)**

Das gewöhnliche $R^2$ steigt von 0.290 auf 0.292, wenn der Prädiktor „Zahl der Reflexionsprotokolle“ hinzugefügt wird. Der Zuwachs beträgt 0.002, also 0.2 Prozentpunkte der Stichprobenvariation. Das gewöhnliche $R^2$ kann nicht sinken, wenn diesem Modell mit denselben Fällen und demselben Achsenabschnitt ein Prädiktor hinzugefügt wird. Das korrigierte $R^2$ sinkt von 0.2627 auf 0.2504, weil es den Anpassungsgewinn gegen die zusätzlich geschätzte Steigung abwägt. Diese Korrektur ist deskriptiv und gilt innerhalb der Stichprobe.

**Berechnung durchführen, Teil (d)**

Die eingeschränkte Gleichung lautet $Y=\beta_0+\beta_1X_1+\beta_2X_2+\varepsilon$. Die uneingeschränkte Gleichung ergänzt den Prädiktor „Zahl der Reflexionsprotokolle“: $Y=\beta_0+\beta_1X_1+\beta_2X_2+\beta_3X_3+\varepsilon$. Die Nullhypothese lautet $H_0:\beta_3=0$, bedingt auf die bereits in M2 enthaltenen Terme. Die inkrementelle Statistik beträgt $F=[(0.292-0.290)/1]/[(1-0.292)/(55-3-1)]=0.1441$ mit 1 und 51 Freiheitsgraden. Der p-Wert beträgt 0.7058. Der hinzugefügte Term erfüllt nicht das 5%-Kriterium.

**Ergebnis interpretieren und prüfen, Teil (e)**

M1 ist in M2 enthalten und M2 ist in M3 enthalten: Wird jeder neu hinzugefügte Koeffizient auf null gesetzt, entsteht wieder das vorherige Modell. Die Ergebnisvariable, die Fälle und der Achsenabschnitt bleiben ebenfalls gleich. Deshalb lassen sich die Anpassungsänderungen als verschachtelte Schritte vergleichen. Die Folge randomisiert keine Prädiktoren, schliesst ausgelassene Variablen nicht aus, beweist keinen Mechanismus und misst die Vorhersage für neue Fälle nicht. Diese Fragen erfordern Angaben zum Design und eine getrennte Validierung.

### T07-A02-V07: Konzentrationsblöcke und Aufgabengenauigkeit

**Vor dem Rechnen begründen, Teil (a)**

Wende $SSE=2280.0(1-R^2)$ an und subtrahiere aufeinanderfolgende $R^2$-Werte.

**Berechnung durchführen, Teil (b)**

Setze für jedes Modell seine eigene Prädiktorenzahl in die korrigierte Formel ein:

| Modell | SSE | Veränderung in R-Quadrat | Korrigiertes R-Quadrat |
| --- | --- | --- | --- |
| M1 | 1801.20 | kein späterer Schritt | 0.2033 |
| M2 | 1504.80 | 0.130 | 0.3287 |
| M3 | 1436.40 | 0.030 | 0.3537 |

**Berechnung durchführen, Teil (c)**

Das gewöhnliche $R^2$ steigt von 0.340 auf 0.370, wenn der Prädiktor „Zahl der Planungspausen“ hinzugefügt wird. Der Zuwachs beträgt 0.030, also 3.0 Prozentpunkte der Stichprobenvariation. Das gewöhnliche $R^2$ kann nicht sinken, wenn diesem Modell mit denselben Fällen und demselben Achsenabschnitt ein Prädiktor hinzugefügt wird. Das korrigierte $R^2$ steigt von 0.3287 auf 0.3537, weil es den Anpassungsgewinn gegen die zusätzlich geschätzte Steigung abwägt. Diese Korrektur ist deskriptiv und gilt innerhalb der Stichprobe.

**Berechnung durchführen, Teil (d)**

Die eingeschränkte Gleichung lautet $Y=\beta_0+\beta_1X_1+\beta_2X_2+\varepsilon$. Die uneingeschränkte Gleichung ergänzt den Prädiktor „Zahl der Planungspausen“: $Y=\beta_0+\beta_1X_1+\beta_2X_2+\beta_3X_3+\varepsilon$. Die Nullhypothese lautet $H_0:\beta_3=0$, bedingt auf die bereits in M2 enthaltenen Terme. Die inkrementelle Statistik beträgt $F=[(0.370-0.340)/1]/[(1-0.370)/(120-3-1)]=5.5238$ mit 1 und 116 Freiheitsgraden. Der p-Wert beträgt 0.0204. Der hinzugefügte Term erfüllt das 5%-Kriterium.

**Ergebnis interpretieren und prüfen, Teil (e)**

M1 ist in M2 enthalten und M2 ist in M3 enthalten: Wird jeder neu hinzugefügte Koeffizient auf null gesetzt, entsteht wieder das vorherige Modell. Die Ergebnisvariable, die Fälle und der Achsenabschnitt bleiben ebenfalls gleich. Deshalb lassen sich die Anpassungsänderungen als verschachtelte Schritte vergleichen. Die Folge randomisiert keine Prädiktoren, schliesst ausgelassene Variablen nicht aus, beweist keinen Mechanismus und misst die Vorhersage für neue Fälle nicht. Diese Fragen erfordern Angaben zum Design und eine getrennte Validierung.

### T07-A02-V08: Museumsbesuche und historisches Wissen

**Vor dem Rechnen begründen, Teil (a)**

Wende $SSE=1440.0(1-R^2)$ an und subtrahiere aufeinanderfolgende $R^2$-Werte.

**Berechnung durchführen, Teil (b)**

Setze für jedes Modell seine eigene Prädiktorenzahl in die korrigierte Formel ein:

| Modell | SSE | Veränderung in R-Quadrat | Korrigiertes R-Quadrat |
| --- | --- | --- | --- |
| M1 | 1094.40 | kein späterer Schritt | 0.2296 |
| M2 | 979.20 | 0.080 | 0.3011 |
| M3 | 977.76 | 0.001 | 0.2923 |

**Berechnung durchführen, Teil (c)**

Das gewöhnliche $R^2$ steigt von 0.320 auf 0.321, wenn der Prädiktor „Zahl der Ausstellungsnotizen“ hinzugefügt wird. Der Zuwachs beträgt 0.001, also 0.1 Prozentpunkte der Stichprobenvariation. Das gewöhnliche $R^2$ kann nicht sinken, wenn diesem Modell mit denselben Fällen und demselben Achsenabschnitt ein Prädiktor hinzugefügt wird. Das korrigierte $R^2$ sinkt von 0.3011 auf 0.2923, weil es den Anpassungsgewinn gegen die zusätzlich geschätzte Steigung abwägt. Diese Korrektur ist deskriptiv und gilt innerhalb der Stichprobe.

**Berechnung durchführen, Teil (d)**

Die eingeschränkte Gleichung lautet $Y=\beta_0+\beta_1X_1+\beta_2X_2+\varepsilon$. Die uneingeschränkte Gleichung ergänzt den Prädiktor „Zahl der Ausstellungsnotizen“: $Y=\beta_0+\beta_1X_1+\beta_2X_2+\beta_3X_3+\varepsilon$. Die Nullhypothese lautet $H_0:\beta_3=0$, bedingt auf die bereits in M2 enthaltenen Terme. Die inkrementelle Statistik beträgt $F=[(0.321-0.320)/1]/[(1-0.321)/(75-3-1)]=0.1046$ mit 1 und 71 Freiheitsgraden. Der p-Wert beträgt 0.7474. Der hinzugefügte Term erfüllt nicht das 5%-Kriterium.

**Ergebnis interpretieren und prüfen, Teil (e)**

M1 ist in M2 enthalten und M2 ist in M3 enthalten: Wird jeder neu hinzugefügte Koeffizient auf null gesetzt, entsteht wieder das vorherige Modell. Die Ergebnisvariable, die Fälle und der Achsenabschnitt bleiben ebenfalls gleich. Deshalb lassen sich die Anpassungsänderungen als verschachtelte Schritte vergleichen. Die Folge randomisiert keine Prädiktoren, schliesst ausgelassene Variablen nicht aus, beweist keinen Mechanismus und misst die Vorhersage für neue Fälle nicht. Diese Fragen erfordern Angaben zum Design und eine getrennte Validierung.

### T07-A02-V09: Peer-Feedback und Überarbeitungsqualität

**Vor dem Rechnen begründen, Teil (a)**

Wende $SSE=1620.0(1-R^2)$ an und subtrahiere aufeinanderfolgende $R^2$-Werte.

**Berechnung durchführen, Teil (b)**

Setze für jedes Modell seine eigene Prädiktorenzahl in die korrigierte Formel ein:

| Modell | SSE | Veränderung in R-Quadrat | Korrigiertes R-Quadrat |
| --- | --- | --- | --- |
| M1 | 1312.20 | kein späterer Schritt | 0.1771 |
| M2 | 1036.80 | 0.170 | 0.3394 |
| M3 | 939.60 | 0.060 | 0.3915 |

**Berechnung durchführen, Teil (c)**

Das gewöhnliche $R^2$ steigt von 0.360 auf 0.420, wenn der Prädiktor „Punktwert des Überarbeitungsplans“ hinzugefügt wird. Der Zuwachs beträgt 0.060, also 6.0 Prozentpunkte der Stichprobenvariation. Das gewöhnliche $R^2$ kann nicht sinken, wenn diesem Modell mit denselben Fällen und demselben Achsenabschnitt ein Prädiktor hinzugefügt wird. Das korrigierte $R^2$ steigt von 0.3394 auf 0.3915, weil es den Anpassungsgewinn gegen die zusätzlich geschätzte Steigung abwägt. Diese Korrektur ist deskriptiv und gilt innerhalb der Stichprobe.

**Berechnung durchführen, Teil (d)**

Die eingeschränkte Gleichung lautet $Y=\beta_0+\beta_1X_1+\beta_2X_2+\varepsilon$. Die uneingeschränkte Gleichung ergänzt den Prädiktor „Punktwert des Überarbeitungsplans“: $Y=\beta_0+\beta_1X_1+\beta_2X_2+\beta_3X_3+\varepsilon$. Die Nullhypothese lautet $H_0:\beta_3=0$, bedingt auf die bereits in M2 enthaltenen Terme. Die inkrementelle Statistik beträgt $F=[(0.420-0.360)/1]/[(1-0.420)/(65-3-1)]=6.3103$ mit 1 und 61 Freiheitsgraden. Der p-Wert beträgt 0.0147. Der hinzugefügte Term erfüllt das 5%-Kriterium.

**Ergebnis interpretieren und prüfen, Teil (e)**

M1 ist in M2 enthalten und M2 ist in M3 enthalten: Wird jeder neu hinzugefügte Koeffizient auf null gesetzt, entsteht wieder das vorherige Modell. Die Ergebnisvariable, die Fälle und der Achsenabschnitt bleiben ebenfalls gleich. Deshalb lassen sich die Anpassungsänderungen als verschachtelte Schritte vergleichen. Die Folge randomisiert keine Prädiktoren, schliesst ausgelassene Variablen nicht aus, beweist keinen Mechanismus und misst die Vorhersage für neue Fälle nicht. Diese Fragen erfordern Angaben zum Design und eine getrennte Validierung.

### T07-A02-V10: Planungssitzungen und Bearbeitungszeit

**Vor dem Rechnen begründen, Teil (a)**

Wende $SSE=1960.0(1-R^2)$ an und subtrahiere aufeinanderfolgende $R^2$-Werte.

**Berechnung durchführen, Teil (b)**

Setze für jedes Modell seine eigene Prädiktorenzahl in die korrigierte Formel ein:

| Modell | SSE | Veränderung in R-Quadrat | Korrigiertes R-Quadrat |
| --- | --- | --- | --- |
| M1 | 1430.80 | kein späterer Schritt | 0.2632 |
| M2 | 1195.60 | 0.120 | 0.3786 |
| M3 | 1185.80 | 0.005 | 0.3779 |

**Berechnung durchführen, Teil (c)**

Das gewöhnliche $R^2$ steigt von 0.390 auf 0.395, wenn der Prädiktor „Zahl der Fortschrittskontrollen“ hinzugefügt wird. Der Zuwachs beträgt 0.005, also 0.5 Prozentpunkte der Stichprobenvariation. Das gewöhnliche $R^2$ kann nicht sinken, wenn diesem Modell mit denselben Fällen und demselben Achsenabschnitt ein Prädiktor hinzugefügt wird. Das korrigierte $R^2$ sinkt von 0.3786 auf 0.3779, weil es den Anpassungsgewinn gegen die zusätzlich geschätzte Steigung abwägt. Diese Korrektur ist deskriptiv und gilt innerhalb der Stichprobe.

**Berechnung durchführen, Teil (d)**

Die eingeschränkte Gleichung lautet $Y=\beta_0+\beta_1X_1+\beta_2X_2+\varepsilon$. Die uneingeschränkte Gleichung ergänzt den Prädiktor „Zahl der Fortschrittskontrollen“: $Y=\beta_0+\beta_1X_1+\beta_2X_2+\beta_3X_3+\varepsilon$. Die Nullhypothese lautet $H_0:\beta_3=0$, bedingt auf die bereits in M2 enthaltenen Terme. Die inkrementelle Statistik beträgt $F=[(0.395-0.390)/1]/[(1-0.395)/(110-3-1)]=0.8760$ mit 1 und 106 Freiheitsgraden. Der p-Wert beträgt 0.3514. Der hinzugefügte Term erfüllt nicht das 5%-Kriterium.

**Ergebnis interpretieren und prüfen, Teil (e)**

M1 ist in M2 enthalten und M2 ist in M3 enthalten: Wird jeder neu hinzugefügte Koeffizient auf null gesetzt, entsteht wieder das vorherige Modell. Die Ergebnisvariable, die Fälle und der Achsenabschnitt bleiben ebenfalls gleich. Deshalb lassen sich die Anpassungsänderungen als verschachtelte Schritte vergleichen. Die Folge randomisiert keine Prädiktoren, schliesst ausgelassene Variablen nicht aus, beweist keinen Mechanismus und misst die Vorhersage für neue Fälle nicht. Diese Fragen erfordern Angaben zum Design und eine getrennte Validierung.

## A03: Den globalen F-Test von den t-Tests der Koeffizienten unterscheiden

### T07-A03-V01: Begleitete Übung und statistisches Denken

**Vor dem Rechnen begründen, Teil (a)**

Die globale Nullhypothese lautet $H_0:\beta_1=\beta_2=\beta_3=0$. Die Statistik ist $F=(0.220/3)/[(1-0.220)/46]=4.325$. Weil 4.325 grösser als 2.80684 ist, wird die globale Nullhypothese bei $\alpha=.05$ verworfen.

**Berechnung durchführen, Teil (b)**

Die Berechnungen für die Koeffizienten lauten: Stunden begleiteter Übung: $t=1.800/0.600=3.000$, $p = 0.0043$, somit wird die Nullhypothese für den Koeffizienten verworfen; Punktwert der vorherigen Vorbereitung: $t=0.220/0.180=1.222$, $p = 0.2278$, somit wird die Nullhypothese für den Koeffizienten nicht verworfen; Reflexionssitzungen: $t=0.120/0.160=0.750$, $p = 0.4571$, somit wird die Nullhypothese für den Koeffizienten nicht verworfen. In 1 von drei gezeigten Tests wird die individuelle Nullhypothese auf dem angegebenen Niveau verworfen.

**Berechnung durchführen, Teil (c)**

Für Prädiktor $X_j$ lautet die individuelle Nullhypothese $H_0:\beta_j=0$, bedingt auf jeden anderen Term in genau diesem Modell. Der globale Test stellt eine gemeinsame Frage zu allen drei Steigungen. Wird die globale Nullhypothese verworfen, unterscheidet sich unter dem Modell mindestens eine Populationssteigung ausser dem Achsenabschnitt von null. Die globale Statistik nennt jedoch keinen Prädiktor. Wird sie nicht verworfen, beweist dies umgekehrt nicht, dass jede Populationssteigung null ist.

**Ergebnis interpretieren und prüfen, Teil (d)**

Die beiden Entscheidungsarten können sich unterscheiden, weil der globale Test die Prädiktoren gemeinsam beurteilt, während jeder $t$-Test einen einzelnen bedingten Koeffizienten und seine Unsicherheit isoliert. Geteilte Prädiktorvariation kann individuelle Standardfehler vergrössern, obwohl der Prädiktorensatz gemeinsam Erklärungswert besitzt. Umgekehrt kann Stichprobenvariation in einem Modell, dessen globaler Test nicht verworfen wird, zu einem kleinen individuellen p-Wert führen. Ein p-Wert misst weder Effektgrösse noch praktische Bedeutung, künftige Vorhersage oder Kausalität.

### T07-A03-V02: Arbeitsablauf im Archiv und Suchzeit

**Vor dem Rechnen begründen, Teil (a)**

Die globale Nullhypothese lautet $H_0:\beta_1=\beta_2=\beta_3=0$. Die Statistik ist $F=(0.300/3)/[(1-0.300)/56]=8.000$. Weil 8.000 grösser als 2.76943 ist, wird die globale Nullhypothese bei $\alpha=.05$ verworfen.

**Berechnung durchführen, Teil (b)**

Die Berechnungen für die Koeffizienten lauten: Übungssitzungen mit Checkliste: $t=-1.400/0.450=-3.111$, $p = 0.0029$, somit wird die Nullhypothese für den Koeffizienten verworfen; Monate Archiverfahrung: $t=-0.200/0.160=-1.250$, $p = 0.2165$, somit wird die Nullhypothese für den Koeffizienten nicht verworfen; Katalogvertrautheit: $t=0.300/0.120=2.500$, $p = 0.0154$, somit wird die Nullhypothese für den Koeffizienten verworfen. In 2 von drei gezeigten Tests wird die individuelle Nullhypothese auf dem angegebenen Niveau verworfen.

**Berechnung durchführen, Teil (c)**

Für Prädiktor $X_j$ lautet die individuelle Nullhypothese $H_0:\beta_j=0$, bedingt auf jeden anderen Term in genau diesem Modell. Der globale Test stellt eine gemeinsame Frage zu allen drei Steigungen. Wird die globale Nullhypothese verworfen, unterscheidet sich unter dem Modell mindestens eine Populationssteigung ausser dem Achsenabschnitt von null. Die globale Statistik nennt jedoch keinen Prädiktor. Wird sie nicht verworfen, beweist dies umgekehrt nicht, dass jede Populationssteigung null ist.

**Ergebnis interpretieren und prüfen, Teil (d)**

Die beiden Entscheidungsarten können sich unterscheiden, weil der globale Test die Prädiktoren gemeinsam beurteilt, während jeder $t$-Test einen einzelnen bedingten Koeffizienten und seine Unsicherheit isoliert. Geteilte Prädiktorvariation kann individuelle Standardfehler vergrössern, obwohl der Prädiktorensatz gemeinsam Erklärungswert besitzt. Umgekehrt kann Stichprobenvariation in einem Modell, dessen globaler Test nicht verworfen wird, zu einem kleinen individuellen p-Wert führen. Ein p-Wert misst weder Effektgrösse noch praktische Bedeutung, künftige Vorhersage oder Kausalität.

### T07-A03-V03: Leseroutinen und Textverständnis

**Vor dem Rechnen begründen, Teil (a)**

Die globale Nullhypothese lautet $H_0:\beta_1=\beta_2=\beta_3=0$. Die Statistik ist $F=(0.100/3)/[(1-0.100)/66]=2.444$. Weil 2.444 nicht grösser als 2.74371 ist, wird die globale Nullhypothese bei $\alpha=.05$ nicht verworfen.

**Berechnung durchführen, Teil (b)**

Die Berechnungen für die Koeffizienten lauten: wöchentliche Lesestunden: $t=1.100/0.580=1.897$, $p = 0.0623$, somit wird die Nullhypothese für den Koeffizienten nicht verworfen; Ausgangswert des Wortschatzes: $t=0.180/0.130=1.385$, $p = 0.1708$, somit wird die Nullhypothese für den Koeffizienten nicht verworfen; Annotationssitzungen: $t=-0.150/0.140=-1.071$, $p = 0.2879$, somit wird die Nullhypothese für den Koeffizienten nicht verworfen. In 0 von drei gezeigten Tests wird die individuelle Nullhypothese auf dem angegebenen Niveau verworfen.

**Berechnung durchführen, Teil (c)**

Für Prädiktor $X_j$ lautet die individuelle Nullhypothese $H_0:\beta_j=0$, bedingt auf jeden anderen Term in genau diesem Modell. Der globale Test stellt eine gemeinsame Frage zu allen drei Steigungen. Wird die globale Nullhypothese verworfen, unterscheidet sich unter dem Modell mindestens eine Populationssteigung ausser dem Achsenabschnitt von null. Die globale Statistik nennt jedoch keinen Prädiktor. Wird sie nicht verworfen, beweist dies umgekehrt nicht, dass jede Populationssteigung null ist.

**Ergebnis interpretieren und prüfen, Teil (d)**

Die beiden Entscheidungsarten können sich unterscheiden, weil der globale Test die Prädiktoren gemeinsam beurteilt, während jeder $t$-Test einen einzelnen bedingten Koeffizienten und seine Unsicherheit isoliert. Geteilte Prädiktorvariation kann individuelle Standardfehler vergrössern, obwohl der Prädiktorensatz gemeinsam Erklärungswert besitzt. Umgekehrt kann Stichprobenvariation in einem Modell, dessen globaler Test nicht verworfen wird, zu einem kleinen individuellen p-Wert führen. Ein p-Wert misst weder Effektgrösse noch praktische Bedeutung, künftige Vorhersage oder Kausalität.

### T07-A03-V04: Streckenübung und Navigationszeit

**Vor dem Rechnen begründen, Teil (a)**

Die globale Nullhypothese lautet $H_0:\beta_1=\beta_2=\beta_3=0$. Die Statistik ist $F=(0.250/3)/[(1-0.250)/76]=8.444$. Weil 8.444 grösser als 2.72494 ist, wird die globale Nullhypothese bei $\alpha=.05$ verworfen.

**Berechnung durchführen, Teil (b)**

Die Berechnungen für die Koeffizienten lauten: Versuche zur Streckenübung: $t=-1.800/0.550=-3.273$, $p = 0.0016$, somit wird die Nullhypothese für den Koeffizienten verworfen; Punktwert der Streckenkenntnis: $t=-0.120/0.100=-1.200$, $p = 0.2339$, somit wird die Nullhypothese für den Koeffizienten nicht verworfen; Erinnerung an Orientierungspunkte: $t=0.280/0.110=2.545$, $p = 0.0129$, somit wird die Nullhypothese für den Koeffizienten verworfen. In 2 von drei gezeigten Tests wird die individuelle Nullhypothese auf dem angegebenen Niveau verworfen.

**Berechnung durchführen, Teil (c)**

Für Prädiktor $X_j$ lautet die individuelle Nullhypothese $H_0:\beta_j=0$, bedingt auf jeden anderen Term in genau diesem Modell. Der globale Test stellt eine gemeinsame Frage zu allen drei Steigungen. Wird die globale Nullhypothese verworfen, unterscheidet sich unter dem Modell mindestens eine Populationssteigung ausser dem Achsenabschnitt von null. Die globale Statistik nennt jedoch keinen Prädiktor. Wird sie nicht verworfen, beweist dies umgekehrt nicht, dass jede Populationssteigung null ist.

**Ergebnis interpretieren und prüfen, Teil (d)**

Die beiden Entscheidungsarten können sich unterscheiden, weil der globale Test die Prädiktoren gemeinsam beurteilt, während jeder $t$-Test einen einzelnen bedingten Koeffizienten und seine Unsicherheit isoliert. Geteilte Prädiktorvariation kann individuelle Standardfehler vergrössern, obwohl der Prädiktorensatz gemeinsam Erklärungswert besitzt. Umgekehrt kann Stichprobenvariation in einem Modell, dessen globaler Test nicht verworfen wird, zu einem kleinen individuellen p-Wert führen. Ein p-Wert misst weder Effektgrösse noch praktische Bedeutung, künftige Vorhersage oder Kausalität.

### T07-A03-V05: Suchübung und Kataloggenauigkeit

**Vor dem Rechnen begründen, Teil (a)**

Die globale Nullhypothese lautet $H_0:\beta_1=\beta_2=\beta_3=0$. Die Statistik ist $F=(0.080/3)/[(1-0.080)/86]=2.493$. Weil 2.493 nicht grösser als 2.71065 ist, wird die globale Nullhypothese bei $\alpha=.05$ nicht verworfen.

**Berechnung durchführen, Teil (b)**

Die Berechnungen für die Koeffizienten lauten: Suchübungsblöcke: $t=1.000/0.570=1.754$, $p = 0.0829$, somit wird die Nullhypothese für den Koeffizienten nicht verworfen; Punktwert des Katalogvorwissens: $t=0.150/0.120=1.250$, $p = 0.2147$, somit wird die Nullhypothese für den Koeffizienten nicht verworfen; Suchplanung: $t=0.180/0.140=1.286$, $p = 0.2020$, somit wird die Nullhypothese für den Koeffizienten nicht verworfen. In 0 von drei gezeigten Tests wird die individuelle Nullhypothese auf dem angegebenen Niveau verworfen.

**Berechnung durchführen, Teil (c)**

Für Prädiktor $X_j$ lautet die individuelle Nullhypothese $H_0:\beta_j=0$, bedingt auf jeden anderen Term in genau diesem Modell. Der globale Test stellt eine gemeinsame Frage zu allen drei Steigungen. Wird die globale Nullhypothese verworfen, unterscheidet sich unter dem Modell mindestens eine Populationssteigung ausser dem Achsenabschnitt von null. Die globale Statistik nennt jedoch keinen Prädiktor. Wird sie nicht verworfen, beweist dies umgekehrt nicht, dass jede Populationssteigung null ist.

**Ergebnis interpretieren und prüfen, Teil (d)**

Die beiden Entscheidungsarten können sich unterscheiden, weil der globale Test die Prädiktoren gemeinsam beurteilt, während jeder $t$-Test einen einzelnen bedingten Koeffizienten und seine Unsicherheit isoliert. Geteilte Prädiktorvariation kann individuelle Standardfehler vergrössern, obwohl der Prädiktorensatz gemeinsam Erklärungswert besitzt. Umgekehrt kann Stichprobenvariation in einem Modell, dessen globaler Test nicht verworfen wird, zu einem kleinen individuellen p-Wert führen. Ein p-Wert misst weder Effektgrösse noch praktische Bedeutung, künftige Vorhersage oder Kausalität.

### T07-A03-V06: Workshopteilnahme und Selbstvertrauen

**Vor dem Rechnen begründen, Teil (a)**

Die globale Nullhypothese lautet $H_0:\beta_1=\beta_2=\beta_3=0$. Die Statistik ist $F=(0.350/3)/[(1-0.350)/96]=17.231$. Weil 17.231 grösser als 2.69939 ist, wird die globale Nullhypothese bei $\alpha=.05$ verworfen.

**Berechnung durchführen, Teil (b)**

Die Berechnungen für die Koeffizienten lauten: Workshopsitzungen: $t=2.100/0.500=4.200$, $p < 0.0001$, somit wird die Nullhypothese für den Koeffizienten verworfen; Ausgangswert des Selbstvertrauens: $t=0.380/0.140=2.714$, $p = 0.0079$, somit wird die Nullhypothese für den Koeffizienten verworfen; Reflexionsprotokolle: $t=-0.100/0.130=-0.769$, $p = 0.4436$, somit wird die Nullhypothese für den Koeffizienten nicht verworfen. In 2 von drei gezeigten Tests wird die individuelle Nullhypothese auf dem angegebenen Niveau verworfen.

**Berechnung durchführen, Teil (c)**

Für Prädiktor $X_j$ lautet die individuelle Nullhypothese $H_0:\beta_j=0$, bedingt auf jeden anderen Term in genau diesem Modell. Der globale Test stellt eine gemeinsame Frage zu allen drei Steigungen. Wird die globale Nullhypothese verworfen, unterscheidet sich unter dem Modell mindestens eine Populationssteigung ausser dem Achsenabschnitt von null. Die globale Statistik nennt jedoch keinen Prädiktor. Wird sie nicht verworfen, beweist dies umgekehrt nicht, dass jede Populationssteigung null ist.

**Ergebnis interpretieren und prüfen, Teil (d)**

Die beiden Entscheidungsarten können sich unterscheiden, weil der globale Test die Prädiktoren gemeinsam beurteilt, während jeder $t$-Test einen einzelnen bedingten Koeffizienten und seine Unsicherheit isoliert. Geteilte Prädiktorvariation kann individuelle Standardfehler vergrössern, obwohl der Prädiktorensatz gemeinsam Erklärungswert besitzt. Umgekehrt kann Stichprobenvariation in einem Modell, dessen globaler Test nicht verworfen wird, zu einem kleinen individuellen p-Wert führen. Ein p-Wert misst weder Effektgrösse noch praktische Bedeutung, künftige Vorhersage oder Kausalität.

### T07-A03-V07: Konzentrationsblöcke und Aufgabengenauigkeit

**Vor dem Rechnen begründen, Teil (a)**

Die globale Nullhypothese lautet $H_0:\beta_1=\beta_2=\beta_3=0$. Die Statistik ist $F=(0.200/3)/[(1-0.200)/106]=8.833$. Weil 8.833 grösser als 2.69030 ist, wird die globale Nullhypothese bei $\alpha=.05$ verworfen.

**Berechnung durchführen, Teil (b)**

Die Berechnungen für die Koeffizienten lauten: benachrichtigungsfreie Blöcke: $t=1.300/0.400=3.250$, $p = 0.0015$, somit wird die Nullhypothese für den Koeffizienten verworfen; Schlafdauer in Stunden: $t=0.120/0.110=1.091$, $p = 0.2778$, somit wird die Nullhypothese für den Koeffizienten nicht verworfen; Planungspausen: $t=0.250/0.150=1.667$, $p = 0.0985$, somit wird die Nullhypothese für den Koeffizienten nicht verworfen. In 1 von drei gezeigten Tests wird die individuelle Nullhypothese auf dem angegebenen Niveau verworfen.

**Berechnung durchführen, Teil (c)**

Für Prädiktor $X_j$ lautet die individuelle Nullhypothese $H_0:\beta_j=0$, bedingt auf jeden anderen Term in genau diesem Modell. Der globale Test stellt eine gemeinsame Frage zu allen drei Steigungen. Wird die globale Nullhypothese verworfen, unterscheidet sich unter dem Modell mindestens eine Populationssteigung ausser dem Achsenabschnitt von null. Die globale Statistik nennt jedoch keinen Prädiktor. Wird sie nicht verworfen, beweist dies umgekehrt nicht, dass jede Populationssteigung null ist.

**Ergebnis interpretieren und prüfen, Teil (d)**

Die beiden Entscheidungsarten können sich unterscheiden, weil der globale Test die Prädiktoren gemeinsam beurteilt, während jeder $t$-Test einen einzelnen bedingten Koeffizienten und seine Unsicherheit isoliert. Geteilte Prädiktorvariation kann individuelle Standardfehler vergrössern, obwohl der Prädiktorensatz gemeinsam Erklärungswert besitzt. Umgekehrt kann Stichprobenvariation in einem Modell, dessen globaler Test nicht verworfen wird, zu einem kleinen individuellen p-Wert führen. Ein p-Wert misst weder Effektgrösse noch praktische Bedeutung, künftige Vorhersage oder Kausalität.

### T07-A03-V08: Museumsbesuche und historisches Wissen

**Vor dem Rechnen begründen, Teil (a)**

Die globale Nullhypothese lautet $H_0:\beta_1=\beta_2=\beta_3=0$. Die Statistik ist $F=(0.280/3)/[(1-0.280)/116]=15.037$. Weil 15.037 grösser als 2.68281 ist, wird die globale Nullhypothese bei $\alpha=.05$ verworfen.

**Berechnung durchführen, Teil (b)**

Die Berechnungen für die Koeffizienten lauten: Museumsbesuche: $t=2.000/0.480=4.167$, $p < 0.0001$, somit wird die Nullhypothese für den Koeffizienten verworfen; Punktwert des geschichtlichen Vorwissens: $t=0.310/0.130=2.385$, $p = 0.0187$, somit wird die Nullhypothese für den Koeffizienten verworfen; Ausstellungsnotizen: $t=0.080/0.120=0.667$, $p = 0.5063$, somit wird die Nullhypothese für den Koeffizienten nicht verworfen. In 2 von drei gezeigten Tests wird die individuelle Nullhypothese auf dem angegebenen Niveau verworfen.

**Berechnung durchführen, Teil (c)**

Für Prädiktor $X_j$ lautet die individuelle Nullhypothese $H_0:\beta_j=0$, bedingt auf jeden anderen Term in genau diesem Modell. Der globale Test stellt eine gemeinsame Frage zu allen drei Steigungen. Wird die globale Nullhypothese verworfen, unterscheidet sich unter dem Modell mindestens eine Populationssteigung ausser dem Achsenabschnitt von null. Die globale Statistik nennt jedoch keinen Prädiktor. Wird sie nicht verworfen, beweist dies umgekehrt nicht, dass jede Populationssteigung null ist.

**Ergebnis interpretieren und prüfen, Teil (d)**

Die beiden Entscheidungsarten können sich unterscheiden, weil der globale Test die Prädiktoren gemeinsam beurteilt, während jeder $t$-Test einen einzelnen bedingten Koeffizienten und seine Unsicherheit isoliert. Geteilte Prädiktorvariation kann individuelle Standardfehler vergrössern, obwohl der Prädiktorensatz gemeinsam Erklärungswert besitzt. Umgekehrt kann Stichprobenvariation in einem Modell, dessen globaler Test nicht verworfen wird, zu einem kleinen individuellen p-Wert führen. Ein p-Wert misst weder Effektgrösse noch praktische Bedeutung, künftige Vorhersage oder Kausalität.

### T07-A03-V09: Peer-Feedback und Überarbeitungsqualität

**Vor dem Rechnen begründen, Teil (a)**

Die globale Nullhypothese lautet $H_0:\beta_1=\beta_2=\beta_3=0$. Die Statistik ist $F=(0.160/3)/[(1-0.160)/71]=4.508$. Weil 4.508 grösser als 2.73365 ist, wird die globale Nullhypothese bei $\alpha=.05$ verworfen.

**Berechnung durchführen, Teil (b)**

Die Berechnungen für die Koeffizienten lauten: Runden mit Peer-Feedback: $t=1.200/0.520=2.308$, $p = 0.0239$, somit wird die Nullhypothese für den Koeffizienten verworfen; Ausgangswert der Schreibqualität: $t=0.190/0.150=1.267$, $p = 0.2094$, somit wird die Nullhypothese für den Koeffizienten nicht verworfen; Überarbeitungsplanung: $t=-0.090/0.130=-0.692$, $p = 0.4910$, somit wird die Nullhypothese für den Koeffizienten nicht verworfen. In 1 von drei gezeigten Tests wird die individuelle Nullhypothese auf dem angegebenen Niveau verworfen.

**Berechnung durchführen, Teil (c)**

Für Prädiktor $X_j$ lautet die individuelle Nullhypothese $H_0:\beta_j=0$, bedingt auf jeden anderen Term in genau diesem Modell. Der globale Test stellt eine gemeinsame Frage zu allen drei Steigungen. Wird die globale Nullhypothese verworfen, unterscheidet sich unter dem Modell mindestens eine Populationssteigung ausser dem Achsenabschnitt von null. Die globale Statistik nennt jedoch keinen Prädiktor. Wird sie nicht verworfen, beweist dies umgekehrt nicht, dass jede Populationssteigung null ist.

**Ergebnis interpretieren und prüfen, Teil (d)**

Die beiden Entscheidungsarten können sich unterscheiden, weil der globale Test die Prädiktoren gemeinsam beurteilt, während jeder $t$-Test einen einzelnen bedingten Koeffizienten und seine Unsicherheit isoliert. Geteilte Prädiktorvariation kann individuelle Standardfehler vergrössern, obwohl der Prädiktorensatz gemeinsam Erklärungswert besitzt. Umgekehrt kann Stichprobenvariation in einem Modell, dessen globaler Test nicht verworfen wird, zu einem kleinen individuellen p-Wert führen. Ein p-Wert misst weder Effektgrösse noch praktische Bedeutung, künftige Vorhersage oder Kausalität.

### T07-A03-V10: Planungssitzungen und Bearbeitungszeit

**Vor dem Rechnen begründen, Teil (a)**

Die globale Nullhypothese lautet $H_0:\beta_1=\beta_2=\beta_3=0$. Die Statistik ist $F=(0.240/3)/[(1-0.240)/61]=6.421$. Weil 6.421 grösser als 2.75548 ist, wird die globale Nullhypothese bei $\alpha=.05$ verworfen.

**Berechnung durchführen, Teil (b)**

Die Berechnungen für die Koeffizienten lauten: Planungssitzungen: $t=-1.600/0.500=-3.200$, $p = 0.0022$, somit wird die Nullhypothese für den Koeffizienten verworfen; Punktwert der Aufgabenkomplexität: $t=0.420/0.170=2.471$, $p = 0.0163$, somit wird die Nullhypothese für den Koeffizienten verworfen; Fortschrittskontrollen: $t=0.160/0.140=1.143$, $p = 0.2576$, somit wird die Nullhypothese für den Koeffizienten nicht verworfen. In 2 von drei gezeigten Tests wird die individuelle Nullhypothese auf dem angegebenen Niveau verworfen.

**Berechnung durchführen, Teil (c)**

Für Prädiktor $X_j$ lautet die individuelle Nullhypothese $H_0:\beta_j=0$, bedingt auf jeden anderen Term in genau diesem Modell. Der globale Test stellt eine gemeinsame Frage zu allen drei Steigungen. Wird die globale Nullhypothese verworfen, unterscheidet sich unter dem Modell mindestens eine Populationssteigung ausser dem Achsenabschnitt von null. Die globale Statistik nennt jedoch keinen Prädiktor. Wird sie nicht verworfen, beweist dies umgekehrt nicht, dass jede Populationssteigung null ist.

**Ergebnis interpretieren und prüfen, Teil (d)**

Die beiden Entscheidungsarten können sich unterscheiden, weil der globale Test die Prädiktoren gemeinsam beurteilt, während jeder $t$-Test einen einzelnen bedingten Koeffizienten und seine Unsicherheit isoliert. Geteilte Prädiktorvariation kann individuelle Standardfehler vergrössern, obwohl der Prädiktorensatz gemeinsam Erklärungswert besitzt. Umgekehrt kann Stichprobenvariation in einem Modell, dessen globaler Test nicht verworfen wird, zu einem kleinen individuellen p-Wert führen. Ein p-Wert misst weder Effektgrösse noch praktische Bedeutung, künftige Vorhersage oder Kausalität.

## A04: Semipartielle Korrelation und zusätzliches R-Quadrat

### T07-A04-V01: Begleitete Übung und statistisches Denken

**Vor dem Rechnen begründen, Teil (a)**

Jeder Kandidat wird um die aktuellen Prädiktoren residualisiert, während die Ergebnisvariable in ihrer ursprünglichen Form bleibt. Diese einseitige Residualisierung definiert eine semipartielle Korrelation. Bei einer partiellen Korrelation würden sowohl der Kandidat als auch die Ergebnisvariable um den aktuellen Prädiktorensatz residualisiert.

**Berechnung durchführen, Teil (b)**

Das Quadrieren jeder semipartiellen Korrelation ergibt den Zuwachs durch einen Prädiktor:

| Kandidat | Semipartielles r | Zuwachs in R-Quadrat | Neues R-Quadrat |
| --- | --- | --- | --- |
| Reflexionssitzungen | 0.240 | 0.0576 | 0.3576 |
| Treffen mit Lernpartnern | 0.100 | 0.0100 | 0.3100 |
| Planungskontrollen | -0.180 | 0.0324 | 0.3324 |

**Berechnung durchführen, Teil (c)**

Die grösste quadrierte semipartielle Korrelation beträgt 0.0576 und gehört zu Reflexionssitzungen. Eine Vorwärtsregel, die nur auf den gezeigten Kandidaten beruht, würde diesen Prädiktor zuerst aufnehmen und das Stichproben-$R^2$ von 0.300 auf 0.3576 erhöhen.

**Ergebnis interpretieren und prüfen, Teil (d)**

Der Schritt ordnet diese drei Kandidaten danach, wie viel zusätzliche Stichprobenvariation jeder nach den aktuellen Prädiktoren erklärt. Durch das Quadrieren verschwindet das Vorzeichen. Das Vorzeichen von $r_{sp}$ bleibt jedoch für die Richtung des Zusammenhangs wichtig, auch wenn es $\Delta R^2$ nicht beeinflusst. Die Rangfolge gilt bedingt auf das gegenwärtige Modell, die Kandidaten und die Stichprobe. Nach Aufnahme eines weiteren Prädiktors verändert die geteilte Variation, was in jedem anderen Kandidaten übrig bleibt. Die Auswahl beweist weder Wahrheit noch kausale Wirkung, inhaltliche Bedeutung oder Leistung an neuen Daten.

### T07-A04-V02: Arbeitsablauf im Archiv und Suchzeit

**Vor dem Rechnen begründen, Teil (a)**

Jeder Kandidat wird um die aktuellen Prädiktoren residualisiert, während die Ergebnisvariable in ihrer ursprünglichen Form bleibt. Diese einseitige Residualisierung definiert eine semipartielle Korrelation. Bei einer partiellen Korrelation würden sowohl der Kandidat als auch die Ergebnisvariable um den aktuellen Prädiktorensatz residualisiert.

**Berechnung durchführen, Teil (b)**

Das Quadrieren jeder semipartiellen Korrelation ergibt den Zuwachs durch einen Prädiktor:

| Kandidat | Semipartielles r | Zuwachs in R-Quadrat | Neues R-Quadrat |
| --- | --- | --- | --- |
| Katalogvertrautheit | -0.120 | 0.0144 | 0.2744 |
| Nutzung eines Schreibtischplans | -0.270 | 0.0729 | 0.3329 |
| Beratungen durch Mentoren | 0.080 | 0.0064 | 0.2664 |

**Berechnung durchführen, Teil (c)**

Die grösste quadrierte semipartielle Korrelation beträgt 0.0729 und gehört zu Nutzung eines Schreibtischplans. Eine Vorwärtsregel, die nur auf den gezeigten Kandidaten beruht, würde diesen Prädiktor zuerst aufnehmen und das Stichproben-$R^2$ von 0.260 auf 0.3329 erhöhen.

**Ergebnis interpretieren und prüfen, Teil (d)**

Der Schritt ordnet diese drei Kandidaten danach, wie viel zusätzliche Stichprobenvariation jeder nach den aktuellen Prädiktoren erklärt. Durch das Quadrieren verschwindet das Vorzeichen. Das Vorzeichen von $r_{sp}$ bleibt jedoch für die Richtung des Zusammenhangs wichtig, auch wenn es $\Delta R^2$ nicht beeinflusst. Die Rangfolge gilt bedingt auf das gegenwärtige Modell, die Kandidaten und die Stichprobe. Nach Aufnahme eines weiteren Prädiktors verändert die geteilte Variation, was in jedem anderen Kandidaten übrig bleibt. Die Auswahl beweist weder Wahrheit noch kausale Wirkung, inhaltliche Bedeutung oder Leistung an neuen Daten.

### T07-A04-V03: Leseroutinen und Textverständnis

**Vor dem Rechnen begründen, Teil (a)**

Jeder Kandidat wird um die aktuellen Prädiktoren residualisiert, während die Ergebnisvariable in ihrer ursprünglichen Form bleibt. Diese einseitige Residualisierung definiert eine semipartielle Korrelation. Bei einer partiellen Korrelation würden sowohl der Kandidat als auch die Ergebnisvariable um den aktuellen Prädiktorensatz residualisiert.

**Berechnung durchführen, Teil (b)**

Das Quadrieren jeder semipartiellen Korrelation ergibt den Zuwachs durch einen Prädiktor:

| Kandidat | Semipartielles r | Zuwachs in R-Quadrat | Neues R-Quadrat |
| --- | --- | --- | --- |
| Annotationssitzungen | 0.150 | 0.0225 | 0.3625 |
| Diskussionsbeiträge | 0.310 | 0.0961 | 0.4361 |
| Blöcke stillen Lesens | 0.200 | 0.0400 | 0.3800 |

**Berechnung durchführen, Teil (c)**

Die grösste quadrierte semipartielle Korrelation beträgt 0.0961 und gehört zu Diskussionsbeiträge. Eine Vorwärtsregel, die nur auf den gezeigten Kandidaten beruht, würde diesen Prädiktor zuerst aufnehmen und das Stichproben-$R^2$ von 0.340 auf 0.4361 erhöhen.

**Ergebnis interpretieren und prüfen, Teil (d)**

Der Schritt ordnet diese drei Kandidaten danach, wie viel zusätzliche Stichprobenvariation jeder nach den aktuellen Prädiktoren erklärt. Durch das Quadrieren verschwindet das Vorzeichen. Das Vorzeichen von $r_{sp}$ bleibt jedoch für die Richtung des Zusammenhangs wichtig, auch wenn es $\Delta R^2$ nicht beeinflusst. Die Rangfolge gilt bedingt auf das gegenwärtige Modell, die Kandidaten und die Stichprobe. Nach Aufnahme eines weiteren Prädiktors verändert die geteilte Variation, was in jedem anderen Kandidaten übrig bleibt. Die Auswahl beweist weder Wahrheit noch kausale Wirkung, inhaltliche Bedeutung oder Leistung an neuen Daten.

### T07-A04-V04: Streckenübung und Navigationszeit

**Vor dem Rechnen begründen, Teil (a)**

Jeder Kandidat wird um die aktuellen Prädiktoren residualisiert, während die Ergebnisvariable in ihrer ursprünglichen Form bleibt. Diese einseitige Residualisierung definiert eine semipartielle Korrelation. Bei einer partiellen Korrelation würden sowohl der Kandidat als auch die Ergebnisvariable um den aktuellen Prädiktorensatz residualisiert.

**Berechnung durchführen, Teil (b)**

Das Quadrieren jeder semipartiellen Korrelation ergibt den Zuwachs durch einen Prädiktor:

| Kandidat | Semipartielles r | Zuwachs in R-Quadrat | Neues R-Quadrat |
| --- | --- | --- | --- |
| Erinnerung an Orientierungspunkte | -0.280 | 0.0784 | 0.3684 |
| Kartenkontrollen | -0.140 | 0.0196 | 0.3096 |
| Streckenvorschauen | 0.190 | 0.0361 | 0.3261 |

**Berechnung durchführen, Teil (c)**

Die grösste quadrierte semipartielle Korrelation beträgt 0.0784 und gehört zu Erinnerung an Orientierungspunkte. Eine Vorwärtsregel, die nur auf den gezeigten Kandidaten beruht, würde diesen Prädiktor zuerst aufnehmen und das Stichproben-$R^2$ von 0.290 auf 0.3684 erhöhen.

**Ergebnis interpretieren und prüfen, Teil (d)**

Der Schritt ordnet diese drei Kandidaten danach, wie viel zusätzliche Stichprobenvariation jeder nach den aktuellen Prädiktoren erklärt. Durch das Quadrieren verschwindet das Vorzeichen. Das Vorzeichen von $r_{sp}$ bleibt jedoch für die Richtung des Zusammenhangs wichtig, auch wenn es $\Delta R^2$ nicht beeinflusst. Die Rangfolge gilt bedingt auf das gegenwärtige Modell, die Kandidaten und die Stichprobe. Nach Aufnahme eines weiteren Prädiktors verändert die geteilte Variation, was in jedem anderen Kandidaten übrig bleibt. Die Auswahl beweist weder Wahrheit noch kausale Wirkung, inhaltliche Bedeutung oder Leistung an neuen Daten.

### T07-A04-V05: Suchübung und Kataloggenauigkeit

**Vor dem Rechnen begründen, Teil (a)**

Jeder Kandidat wird um die aktuellen Prädiktoren residualisiert, während die Ergebnisvariable in ihrer ursprünglichen Form bleibt. Diese einseitige Residualisierung definiert eine semipartielle Korrelation. Bei einer partiellen Korrelation würden sowohl der Kandidat als auch die Ergebnisvariable um den aktuellen Prädiktorensatz residualisiert.

**Berechnung durchführen, Teil (b)**

Das Quadrieren jeder semipartiellen Korrelation ergibt den Zuwachs durch einen Prädiktor:

| Kandidat | Semipartielles r | Zuwachs in R-Quadrat | Neues R-Quadrat |
| --- | --- | --- | --- |
| Suchplanung | 0.110 | 0.0121 | 0.3821 |
| Stichwortübungen | 0.220 | 0.0484 | 0.4184 |
| genutzte Kataloghinweise | 0.290 | 0.0841 | 0.4541 |

**Berechnung durchführen, Teil (c)**

Die grösste quadrierte semipartielle Korrelation beträgt 0.0841 und gehört zu genutzte Kataloghinweise. Eine Vorwärtsregel, die nur auf den gezeigten Kandidaten beruht, würde diesen Prädiktor zuerst aufnehmen und das Stichproben-$R^2$ von 0.370 auf 0.4541 erhöhen.

**Ergebnis interpretieren und prüfen, Teil (d)**

Der Schritt ordnet diese drei Kandidaten danach, wie viel zusätzliche Stichprobenvariation jeder nach den aktuellen Prädiktoren erklärt. Durch das Quadrieren verschwindet das Vorzeichen. Das Vorzeichen von $r_{sp}$ bleibt jedoch für die Richtung des Zusammenhangs wichtig, auch wenn es $\Delta R^2$ nicht beeinflusst. Die Rangfolge gilt bedingt auf das gegenwärtige Modell, die Kandidaten und die Stichprobe. Nach Aufnahme eines weiteren Prädiktors verändert die geteilte Variation, was in jedem anderen Kandidaten übrig bleibt. Die Auswahl beweist weder Wahrheit noch kausale Wirkung, inhaltliche Bedeutung oder Leistung an neuen Daten.

### T07-A04-V06: Workshopteilnahme und Selbstvertrauen

**Vor dem Rechnen begründen, Teil (a)**

Jeder Kandidat wird um die aktuellen Prädiktoren residualisiert, während die Ergebnisvariable in ihrer ursprünglichen Form bleibt. Diese einseitige Residualisierung definiert eine semipartielle Korrelation. Bei einer partiellen Korrelation würden sowohl der Kandidat als auch die Ergebnisvariable um den aktuellen Prädiktorensatz residualisiert.

**Berechnung durchführen, Teil (b)**

Das Quadrieren jeder semipartiellen Korrelation ergibt den Zuwachs durch einen Prädiktor:

| Kandidat | Semipartielles r | Zuwachs in R-Quadrat | Neues R-Quadrat |
| --- | --- | --- | --- |
| Reflexionsprotokolle | 0.260 | 0.0676 | 0.3876 |
| Peer-Treffen | 0.170 | 0.0289 | 0.3489 |
| praktische Demonstrationen | -0.090 | 0.0081 | 0.3281 |

**Berechnung durchführen, Teil (c)**

Die grösste quadrierte semipartielle Korrelation beträgt 0.0676 und gehört zu Reflexionsprotokolle. Eine Vorwärtsregel, die nur auf den gezeigten Kandidaten beruht, würde diesen Prädiktor zuerst aufnehmen und das Stichproben-$R^2$ von 0.320 auf 0.3876 erhöhen.

**Ergebnis interpretieren und prüfen, Teil (d)**

Der Schritt ordnet diese drei Kandidaten danach, wie viel zusätzliche Stichprobenvariation jeder nach den aktuellen Prädiktoren erklärt. Durch das Quadrieren verschwindet das Vorzeichen. Das Vorzeichen von $r_{sp}$ bleibt jedoch für die Richtung des Zusammenhangs wichtig, auch wenn es $\Delta R^2$ nicht beeinflusst. Die Rangfolge gilt bedingt auf das gegenwärtige Modell, die Kandidaten und die Stichprobe. Nach Aufnahme eines weiteren Prädiktors verändert die geteilte Variation, was in jedem anderen Kandidaten übrig bleibt. Die Auswahl beweist weder Wahrheit noch kausale Wirkung, inhaltliche Bedeutung oder Leistung an neuen Daten.

### T07-A04-V07: Konzentrationsblöcke und Aufgabengenauigkeit

**Vor dem Rechnen begründen, Teil (a)**

Jeder Kandidat wird um die aktuellen Prädiktoren residualisiert, während die Ergebnisvariable in ihrer ursprünglichen Form bleibt. Diese einseitige Residualisierung definiert eine semipartielle Korrelation. Bei einer partiellen Korrelation würden sowohl der Kandidat als auch die Ergebnisvariable um den aktuellen Prädiktorensatz residualisiert.

**Berechnung durchführen, Teil (b)**

Das Quadrieren jeder semipartiellen Korrelation ergibt den Zuwachs durch einen Prädiktor:

| Kandidat | Semipartielles r | Zuwachs in R-Quadrat | Neues R-Quadrat |
| --- | --- | --- | --- |
| Planungspausen | 0.130 | 0.0169 | 0.2669 |
| bildschirmfreie Zeiträume | 0.210 | 0.0441 | 0.2941 |
| Aufgabenvorschauen | 0.070 | 0.0049 | 0.2549 |

**Berechnung durchführen, Teil (c)**

Die grösste quadrierte semipartielle Korrelation beträgt 0.0441 und gehört zu bildschirmfreie Zeiträume. Eine Vorwärtsregel, die nur auf den gezeigten Kandidaten beruht, würde diesen Prädiktor zuerst aufnehmen und das Stichproben-$R^2$ von 0.250 auf 0.2941 erhöhen.

**Ergebnis interpretieren und prüfen, Teil (d)**

Der Schritt ordnet diese drei Kandidaten danach, wie viel zusätzliche Stichprobenvariation jeder nach den aktuellen Prädiktoren erklärt. Durch das Quadrieren verschwindet das Vorzeichen. Das Vorzeichen von $r_{sp}$ bleibt jedoch für die Richtung des Zusammenhangs wichtig, auch wenn es $\Delta R^2$ nicht beeinflusst. Die Rangfolge gilt bedingt auf das gegenwärtige Modell, die Kandidaten und die Stichprobe. Nach Aufnahme eines weiteren Prädiktors verändert die geteilte Variation, was in jedem anderen Kandidaten übrig bleibt. Die Auswahl beweist weder Wahrheit noch kausale Wirkung, inhaltliche Bedeutung oder Leistung an neuen Daten.

### T07-A04-V08: Museumsbesuche und historisches Wissen

**Vor dem Rechnen begründen, Teil (a)**

Jeder Kandidat wird um die aktuellen Prädiktoren residualisiert, während die Ergebnisvariable in ihrer ursprünglichen Form bleibt. Diese einseitige Residualisierung definiert eine semipartielle Korrelation. Bei einer partiellen Korrelation würden sowohl der Kandidat als auch die Ergebnisvariable um den aktuellen Prädiktorensatz residualisiert.

**Berechnung durchführen, Teil (b)**

Das Quadrieren jeder semipartiellen Korrelation ergibt den Zuwachs durch einen Prädiktor:

| Kandidat | Semipartielles r | Zuwachs in R-Quadrat | Neues R-Quadrat |
| --- | --- | --- | --- |
| Ausstellungsnotizen | 0.180 | 0.0324 | 0.3424 |
| Stationen einer Führung | 0.120 | 0.0144 | 0.3244 |
| weiterführende Lektüre | 0.250 | 0.0625 | 0.3725 |

**Berechnung durchführen, Teil (c)**

Die grösste quadrierte semipartielle Korrelation beträgt 0.0625 und gehört zu weiterführende Lektüre. Eine Vorwärtsregel, die nur auf den gezeigten Kandidaten beruht, würde diesen Prädiktor zuerst aufnehmen und das Stichproben-$R^2$ von 0.310 auf 0.3725 erhöhen.

**Ergebnis interpretieren und prüfen, Teil (d)**

Der Schritt ordnet diese drei Kandidaten danach, wie viel zusätzliche Stichprobenvariation jeder nach den aktuellen Prädiktoren erklärt. Durch das Quadrieren verschwindet das Vorzeichen. Das Vorzeichen von $r_{sp}$ bleibt jedoch für die Richtung des Zusammenhangs wichtig, auch wenn es $\Delta R^2$ nicht beeinflusst. Die Rangfolge gilt bedingt auf das gegenwärtige Modell, die Kandidaten und die Stichprobe. Nach Aufnahme eines weiteren Prädiktors verändert die geteilte Variation, was in jedem anderen Kandidaten übrig bleibt. Die Auswahl beweist weder Wahrheit noch kausale Wirkung, inhaltliche Bedeutung oder Leistung an neuen Daten.

### T07-A04-V09: Peer-Feedback und Überarbeitungsqualität

**Vor dem Rechnen begründen, Teil (a)**

Jeder Kandidat wird um die aktuellen Prädiktoren residualisiert, während die Ergebnisvariable in ihrer ursprünglichen Form bleibt. Diese einseitige Residualisierung definiert eine semipartielle Korrelation. Bei einer partiellen Korrelation würden sowohl der Kandidat als auch die Ergebnisvariable um den aktuellen Prädiktorensatz residualisiert.

**Berechnung durchführen, Teil (b)**

Das Quadrieren jeder semipartiellen Korrelation ergibt den Zuwachs durch einen Prädiktor:

| Kandidat | Semipartielles r | Zuwachs in R-Quadrat | Neues R-Quadrat |
| --- | --- | --- | --- |
| Überarbeitungsplanung | 0.090 | 0.0081 | 0.3681 |
| genutzte Peer-Kommentare | 0.280 | 0.0784 | 0.4384 |
| Korrekturdurchgänge | 0.160 | 0.0256 | 0.3856 |

**Berechnung durchführen, Teil (c)**

Die grösste quadrierte semipartielle Korrelation beträgt 0.0784 und gehört zu genutzte Peer-Kommentare. Eine Vorwärtsregel, die nur auf den gezeigten Kandidaten beruht, würde diesen Prädiktor zuerst aufnehmen und das Stichproben-$R^2$ von 0.360 auf 0.4384 erhöhen.

**Ergebnis interpretieren und prüfen, Teil (d)**

Der Schritt ordnet diese drei Kandidaten danach, wie viel zusätzliche Stichprobenvariation jeder nach den aktuellen Prädiktoren erklärt. Durch das Quadrieren verschwindet das Vorzeichen. Das Vorzeichen von $r_{sp}$ bleibt jedoch für die Richtung des Zusammenhangs wichtig, auch wenn es $\Delta R^2$ nicht beeinflusst. Die Rangfolge gilt bedingt auf das gegenwärtige Modell, die Kandidaten und die Stichprobe. Nach Aufnahme eines weiteren Prädiktors verändert die geteilte Variation, was in jedem anderen Kandidaten übrig bleibt. Die Auswahl beweist weder Wahrheit noch kausale Wirkung, inhaltliche Bedeutung oder Leistung an neuen Daten.

### T07-A04-V10: Planungssitzungen und Bearbeitungszeit

**Vor dem Rechnen begründen, Teil (a)**

Jeder Kandidat wird um die aktuellen Prädiktoren residualisiert, während die Ergebnisvariable in ihrer ursprünglichen Form bleibt. Diese einseitige Residualisierung definiert eine semipartielle Korrelation. Bei einer partiellen Korrelation würden sowohl der Kandidat als auch die Ergebnisvariable um den aktuellen Prädiktorensatz residualisiert.

**Berechnung durchführen, Teil (b)**

Das Quadrieren jeder semipartiellen Korrelation ergibt den Zuwachs durch einen Prädiktor:

| Kandidat | Semipartielles r | Zuwachs in R-Quadrat | Neues R-Quadrat |
| --- | --- | --- | --- |
| Fortschrittskontrollen | -0.230 | 0.0529 | 0.3329 |
| Kalendererinnerungen | -0.110 | 0.0121 | 0.2921 |
| Aufgabenvorschauen | 0.200 | 0.0400 | 0.3200 |

**Berechnung durchführen, Teil (c)**

Die grösste quadrierte semipartielle Korrelation beträgt 0.0529 und gehört zu Fortschrittskontrollen. Eine Vorwärtsregel, die nur auf den gezeigten Kandidaten beruht, würde diesen Prädiktor zuerst aufnehmen und das Stichproben-$R^2$ von 0.280 auf 0.3329 erhöhen.

**Ergebnis interpretieren und prüfen, Teil (d)**

Der Schritt ordnet diese drei Kandidaten danach, wie viel zusätzliche Stichprobenvariation jeder nach den aktuellen Prädiktoren erklärt. Durch das Quadrieren verschwindet das Vorzeichen. Das Vorzeichen von $r_{sp}$ bleibt jedoch für die Richtung des Zusammenhangs wichtig, auch wenn es $\Delta R^2$ nicht beeinflusst. Die Rangfolge gilt bedingt auf das gegenwärtige Modell, die Kandidaten und die Stichprobe. Nach Aufnahme eines weiteren Prädiktors verändert die geteilte Variation, was in jedem anderen Kandidaten übrig bleibt. Die Auswahl beweist weder Wahrheit noch kausale Wirkung, inhaltliche Bedeutung oder Leistung an neuen Daten.

## A05: Vorab festgelegte Kandidatenmodelle mit AIC vergleichen

### T07-A05-V01: Begleitete Übung und statistisches Denken

**Vor dem Rechnen begründen, Teil (a)**

Für M1 ergibt sich zum Beispiel $-2(-155.0)+2(3)=316.00$. Dieselbe Regel ergibt für alle vier Modelle:

| Modell | AIC | Delta AIC |
| --- | --- | --- |
| M1 | 316.00 | 21.00 |
| M2 | 300.00 | 5.00 |
| M3 | 295.00 | 0.00 |
| M4 | 295.80 | 0.80 |

**Berechnung durchführen, Teil (b)**

In Schritt 1 wird M2 ausgewählt, weil 300.00 kleiner als die anderen angezeigten Werte von Schritt 1 und kleiner als der Wert 316.00 von M1 ist. In Schritt 2 wird M3 ausgewählt, weil sein AIC kleiner als der aktuelle Wert von M2 ist. Auf diesem Vorwärtspfad wird später kein Produktterm ausgewählt.

**Berechnung durchführen, Teil (c)**

Die Koordinaten des ausgewählten Pfads lauten (0, 316.00), (1, 300.00), (2, 295.00). Trage den Schritt auf der horizontalen Achse und den AIC auf der vertikalen Achse ab. Verbinde nur aufeinanderfolgende ausgewählte Modelle und ende dort, wo die Regel stoppt. Die fallenden Abschnitte zeigen Verbesserungen des relativen Gleichgewichts zwischen Anpassung und Komplexität entlang dieses bestimmten Pfads.

**Berechnung durchführen, Teil (d)**

Die endgültige ausgewählte Formel lautet `Punktwert im statistischen Denken ~ Stunden begleiteter Übung + Punktwert der vorherigen Vorbereitung + Zahl der Reflexionssitzungen`. Ihre Terme beschreiben bedingte angepasste Zusammenhänge für diese Ergebnisvariable und diese Fälle. Sie identifizieren für sich allein keine Ursachen.

**Ergebnis interpretieren und prüfen, Teil (e)**

Bei einem Vorwärtspfad wird die Wahl nach jedem ausgewählten Term neu berechnet. Eine Ergänzung, die in einem Schritt nützlich erscheint, kann deshalb in einem späteren Schritt redundant werden. Der Pfad kann zudem stoppen, bevor er den global kleinsten AIC unter Kombinationen erreicht, die durch seine früheren Entscheidungen nie verfügbar wurden. AIC belohnt Anpassung und fügt eine Komplexitätsstrafe hinzu. Das Kriterium belegt weder, dass ein ausgewähltes Modell die Wahrheit der Datenerzeugung darstellt, noch dass seine Vorhersagen generalisieren. Die Leistung an neuen Daten erfordert eine getrennte Validierung. AIC-Werte für unterschiedliche Ergebnisvariablen oder Fallmengen gehören nicht zu einer gemeinsam vergleichbaren Kandidatenfamilie.

### T07-A05-V02: Arbeitsablauf im Archiv und Suchzeit

**Vor dem Rechnen begründen, Teil (a)**

Für M1 ergibt sich zum Beispiel $-2(-142.0)+2(3)=290.00$. Dieselbe Regel ergibt für alle vier Modelle:

| Modell | AIC | Delta AIC |
| --- | --- | --- |
| M1 | 290.00 | 14.40 |
| M2 | 276.00 | 0.40 |
| M3 | 276.80 | 1.20 |
| M4 | 275.60 | 0.00 |

**Berechnung durchführen, Teil (b)**

In Schritt 1 wird M2 ausgewählt, weil 276.00 kleiner als die anderen angezeigten Werte von Schritt 1 und kleiner als der Wert 290.00 von M1 ist. In Schritt 2 wird gestoppt, weil keine Ergänzung einen AIC unter dem aktuellen Wert von M2 besitzt. Auf diesem Vorwärtspfad wird später kein Produktterm ausgewählt.

**Berechnung durchführen, Teil (c)**

Die Koordinaten des ausgewählten Pfads lauten (0, 290.00), (1, 276.00). Trage den Schritt auf der horizontalen Achse und den AIC auf der vertikalen Achse ab. Verbinde nur aufeinanderfolgende ausgewählte Modelle und ende dort, wo die Regel stoppt. Die fallenden Abschnitte zeigen Verbesserungen des relativen Gleichgewichts zwischen Anpassung und Komplexität entlang dieses bestimmten Pfads.

**Berechnung durchführen, Teil (d)**

Die endgültige ausgewählte Formel lautet `Suchzeit ~ Übungssitzungen mit Checkliste + Monate Archiverfahrung`. Ihre Terme beschreiben bedingte angepasste Zusammenhänge für diese Ergebnisvariable und diese Fälle. Sie identifizieren für sich allein keine Ursachen.

**Ergebnis interpretieren und prüfen, Teil (e)**

Bei einem Vorwärtspfad wird die Wahl nach jedem ausgewählten Term neu berechnet. Eine Ergänzung, die in einem Schritt nützlich erscheint, kann deshalb in einem späteren Schritt redundant werden. Der Pfad kann zudem stoppen, bevor er den global kleinsten AIC unter Kombinationen erreicht, die durch seine früheren Entscheidungen nie verfügbar wurden. AIC belohnt Anpassung und fügt eine Komplexitätsstrafe hinzu. Das Kriterium belegt weder, dass ein ausgewähltes Modell die Wahrheit der Datenerzeugung darstellt, noch dass seine Vorhersagen generalisieren. Die Leistung an neuen Daten erfordert eine getrennte Validierung. AIC-Werte für unterschiedliche Ergebnisvariablen oder Fallmengen gehören nicht zu einer gemeinsam vergleichbaren Kandidatenfamilie.

### T07-A05-V03: Leseroutinen und Textverständnis

**Vor dem Rechnen begründen, Teil (a)**

Für M1 ergibt sich zum Beispiel $-2(-180.0)+2(3)=366.00$. Dieselbe Regel ergibt für alle vier Modelle:

| Modell | AIC | Delta AIC |
| --- | --- | --- |
| M1 | 366.00 | 24.00 |
| M2 | 348.00 | 6.00 |
| M3 | 342.00 | 0.00 |
| M4 | 343.00 | 1.00 |

**Berechnung durchführen, Teil (b)**

In Schritt 1 wird M2 ausgewählt, weil 348.00 kleiner als die anderen angezeigten Werte von Schritt 1 und kleiner als der Wert 366.00 von M1 ist. In Schritt 2 wird M3 ausgewählt, weil sein AIC kleiner als der aktuelle Wert von M2 ist. Auf diesem Vorwärtspfad wird später kein Produktterm ausgewählt.

**Berechnung durchführen, Teil (c)**

Die Koordinaten des ausgewählten Pfads lauten (0, 366.00), (1, 348.00), (2, 342.00). Trage den Schritt auf der horizontalen Achse und den AIC auf der vertikalen Achse ab. Verbinde nur aufeinanderfolgende ausgewählte Modelle und ende dort, wo die Regel stoppt. Die fallenden Abschnitte zeigen Verbesserungen des relativen Gleichgewichts zwischen Anpassung und Komplexität entlang dieses bestimmten Pfads.

**Berechnung durchführen, Teil (d)**

Die endgültige ausgewählte Formel lautet `Punktwert im Textverständnis ~ wöchentliche Lesestunden + Ausgangswert des Wortschatzes + Zahl der Annotationssitzungen`. Ihre Terme beschreiben bedingte angepasste Zusammenhänge für diese Ergebnisvariable und diese Fälle. Sie identifizieren für sich allein keine Ursachen.

**Ergebnis interpretieren und prüfen, Teil (e)**

Bei einem Vorwärtspfad wird die Wahl nach jedem ausgewählten Term neu berechnet. Eine Ergänzung, die in einem Schritt nützlich erscheint, kann deshalb in einem späteren Schritt redundant werden. Der Pfad kann zudem stoppen, bevor er den global kleinsten AIC unter Kombinationen erreicht, die durch seine früheren Entscheidungen nie verfügbar wurden. AIC belohnt Anpassung und fügt eine Komplexitätsstrafe hinzu. Das Kriterium belegt weder, dass ein ausgewähltes Modell die Wahrheit der Datenerzeugung darstellt, noch dass seine Vorhersagen generalisieren. Die Leistung an neuen Daten erfordert eine getrennte Validierung. AIC-Werte für unterschiedliche Ergebnisvariablen oder Fallmengen gehören nicht zu einer gemeinsam vergleichbaren Kandidatenfamilie.

### T07-A05-V04: Streckenübung und Navigationszeit

**Vor dem Rechnen begründen, Teil (a)**

Für M1 ergibt sich zum Beispiel $-2(-130.0)+2(3)=266.00$. Dieselbe Regel ergibt für alle vier Modelle:

| Modell | AIC | Delta AIC |
| --- | --- | --- |
| M1 | 266.00 | 6.00 |
| M2 | 260.00 | 0.00 |
| M3 | 261.00 | 1.00 |
| M4 | 262.40 | 2.40 |

**Berechnung durchführen, Teil (b)**

In Schritt 1 wird M2 ausgewählt, weil 260.00 kleiner als die anderen angezeigten Werte von Schritt 1 und kleiner als der Wert 266.00 von M1 ist. In Schritt 2 wird gestoppt, weil keine Ergänzung einen AIC unter dem aktuellen Wert von M2 besitzt. Auf diesem Vorwärtspfad wird später kein Produktterm ausgewählt.

**Berechnung durchführen, Teil (c)**

Die Koordinaten des ausgewählten Pfads lauten (0, 266.00), (1, 260.00). Trage den Schritt auf der horizontalen Achse und den AIC auf der vertikalen Achse ab. Verbinde nur aufeinanderfolgende ausgewählte Modelle und ende dort, wo die Regel stoppt. Die fallenden Abschnitte zeigen Verbesserungen des relativen Gleichgewichts zwischen Anpassung und Komplexität entlang dieses bestimmten Pfads.

**Berechnung durchführen, Teil (d)**

Die endgültige ausgewählte Formel lautet `Navigationszeit ~ Versuche zur Streckenübung + Punktwert der Streckenkenntnis`. Ihre Terme beschreiben bedingte angepasste Zusammenhänge für diese Ergebnisvariable und diese Fälle. Sie identifizieren für sich allein keine Ursachen.

**Ergebnis interpretieren und prüfen, Teil (e)**

Bei einem Vorwärtspfad wird die Wahl nach jedem ausgewählten Term neu berechnet. Eine Ergänzung, die in einem Schritt nützlich erscheint, kann deshalb in einem späteren Schritt redundant werden. Der Pfad kann zudem stoppen, bevor er den global kleinsten AIC unter Kombinationen erreicht, die durch seine früheren Entscheidungen nie verfügbar wurden. AIC belohnt Anpassung und fügt eine Komplexitätsstrafe hinzu. Das Kriterium belegt weder, dass ein ausgewähltes Modell die Wahrheit der Datenerzeugung darstellt, noch dass seine Vorhersagen generalisieren. Die Leistung an neuen Daten erfordert eine getrennte Validierung. AIC-Werte für unterschiedliche Ergebnisvariablen oder Fallmengen gehören nicht zu einer gemeinsam vergleichbaren Kandidatenfamilie.

### T07-A05-V05: Suchübung und Kataloggenauigkeit

**Vor dem Rechnen begründen, Teil (a)**

Für M1 ergibt sich zum Beispiel $-2(-200.0)+2(3)=406.00$. Dieselbe Regel ergibt für alle vier Modelle:

| Modell | AIC | Delta AIC |
| --- | --- | --- |
| M1 | 406.00 | 34.00 |
| M2 | 384.00 | 12.00 |
| M3 | 376.00 | 4.00 |
| M4 | 372.00 | 0.00 |

**Berechnung durchführen, Teil (b)**

In Schritt 1 wird M2 ausgewählt, weil 384.00 kleiner als die anderen angezeigten Werte von Schritt 1 und kleiner als der Wert 406.00 von M1 ist. In Schritt 2 wird M3 ausgewählt, weil sein AIC kleiner als der aktuelle Wert von M2 ist. In Schritt 3 wird danach M4 ausgewählt, weil sein AIC unter demjenigen von M3 liegt.

**Berechnung durchführen, Teil (c)**

Die Koordinaten des ausgewählten Pfads lauten (0, 406.00), (1, 384.00), (2, 376.00), (3, 372.00). Trage den Schritt auf der horizontalen Achse und den AIC auf der vertikalen Achse ab. Verbinde nur aufeinanderfolgende ausgewählte Modelle und ende dort, wo die Regel stoppt. Die fallenden Abschnitte zeigen Verbesserungen des relativen Gleichgewichts zwischen Anpassung und Komplexität entlang dieses bestimmten Pfads.

**Berechnung durchführen, Teil (d)**

Die endgültige ausgewählte Formel lautet `Punktwert der Kataloggenauigkeit ~ Suchübungsblöcke + Punktwert des Katalogvorwissens + Punktwert der Suchplanung + ein vorab festgelegter Produktterm`. Ihre Terme beschreiben bedingte angepasste Zusammenhänge für diese Ergebnisvariable und diese Fälle. Sie identifizieren für sich allein keine Ursachen.

**Ergebnis interpretieren und prüfen, Teil (e)**

Bei einem Vorwärtspfad wird die Wahl nach jedem ausgewählten Term neu berechnet. Eine Ergänzung, die in einem Schritt nützlich erscheint, kann deshalb in einem späteren Schritt redundant werden. Der Pfad kann zudem stoppen, bevor er den global kleinsten AIC unter Kombinationen erreicht, die durch seine früheren Entscheidungen nie verfügbar wurden. AIC belohnt Anpassung und fügt eine Komplexitätsstrafe hinzu. Das Kriterium belegt weder, dass ein ausgewähltes Modell die Wahrheit der Datenerzeugung darstellt, noch dass seine Vorhersagen generalisieren. Die Leistung an neuen Daten erfordert eine getrennte Validierung. AIC-Werte für unterschiedliche Ergebnisvariablen oder Fallmengen gehören nicht zu einer gemeinsam vergleichbaren Kandidatenfamilie.

### T07-A05-V06: Workshopteilnahme und Selbstvertrauen

**Vor dem Rechnen begründen, Teil (a)**

Für M1 ergibt sich zum Beispiel $-2(-165.0)+2(3)=336.00$. Dieselbe Regel ergibt für alle vier Modelle:

| Modell | AIC | Delta AIC |
| --- | --- | --- |
| M1 | 336.00 | 14.00 |
| M2 | 322.00 | 0.00 |
| M3 | 322.80 | 0.80 |
| M4 | 323.60 | 1.60 |

**Berechnung durchführen, Teil (b)**

In Schritt 1 wird M2 ausgewählt, weil 322.00 kleiner als die anderen angezeigten Werte von Schritt 1 und kleiner als der Wert 336.00 von M1 ist. In Schritt 2 wird gestoppt, weil keine Ergänzung einen AIC unter dem aktuellen Wert von M2 besitzt. Auf diesem Vorwärtspfad wird später kein Produktterm ausgewählt.

**Berechnung durchführen, Teil (c)**

Die Koordinaten des ausgewählten Pfads lauten (0, 336.00), (1, 322.00). Trage den Schritt auf der horizontalen Achse und den AIC auf der vertikalen Achse ab. Verbinde nur aufeinanderfolgende ausgewählte Modelle und ende dort, wo die Regel stoppt. Die fallenden Abschnitte zeigen Verbesserungen des relativen Gleichgewichts zwischen Anpassung und Komplexität entlang dieses bestimmten Pfads.

**Berechnung durchführen, Teil (d)**

Die endgültige ausgewählte Formel lautet `Punktwert des Selbstvertrauens ~ Workshopsitzungen + Ausgangswert des Selbstvertrauens`. Ihre Terme beschreiben bedingte angepasste Zusammenhänge für diese Ergebnisvariable und diese Fälle. Sie identifizieren für sich allein keine Ursachen.

**Ergebnis interpretieren und prüfen, Teil (e)**

Bei einem Vorwärtspfad wird die Wahl nach jedem ausgewählten Term neu berechnet. Eine Ergänzung, die in einem Schritt nützlich erscheint, kann deshalb in einem späteren Schritt redundant werden. Der Pfad kann zudem stoppen, bevor er den global kleinsten AIC unter Kombinationen erreicht, die durch seine früheren Entscheidungen nie verfügbar wurden. AIC belohnt Anpassung und fügt eine Komplexitätsstrafe hinzu. Das Kriterium belegt weder, dass ein ausgewähltes Modell die Wahrheit der Datenerzeugung darstellt, noch dass seine Vorhersagen generalisieren. Die Leistung an neuen Daten erfordert eine getrennte Validierung. AIC-Werte für unterschiedliche Ergebnisvariablen oder Fallmengen gehören nicht zu einer gemeinsam vergleichbaren Kandidatenfamilie.

### T07-A05-V07: Konzentrationsblöcke und Aufgabengenauigkeit

**Vor dem Rechnen begründen, Teil (a)**

Für M1 ergibt sich zum Beispiel $-2(-175.0)+2(3)=356.00$. Dieselbe Regel ergibt für alle vier Modelle:

| Modell | AIC | Delta AIC |
| --- | --- | --- |
| M1 | 356.00 | 22.00 |
| M2 | 340.00 | 6.00 |
| M3 | 334.00 | 0.00 |
| M4 | 334.40 | 0.40 |

**Berechnung durchführen, Teil (b)**

In Schritt 1 wird M2 ausgewählt, weil 340.00 kleiner als die anderen angezeigten Werte von Schritt 1 und kleiner als der Wert 356.00 von M1 ist. In Schritt 2 wird M3 ausgewählt, weil sein AIC kleiner als der aktuelle Wert von M2 ist. Auf diesem Vorwärtspfad wird später kein Produktterm ausgewählt.

**Berechnung durchführen, Teil (c)**

Die Koordinaten des ausgewählten Pfads lauten (0, 356.00), (1, 340.00), (2, 334.00). Trage den Schritt auf der horizontalen Achse und den AIC auf der vertikalen Achse ab. Verbinde nur aufeinanderfolgende ausgewählte Modelle und ende dort, wo die Regel stoppt. Die fallenden Abschnitte zeigen Verbesserungen des relativen Gleichgewichts zwischen Anpassung und Komplexität entlang dieses bestimmten Pfads.

**Berechnung durchführen, Teil (d)**

Die endgültige ausgewählte Formel lautet `Punktwert der Aufgabengenauigkeit ~ benachrichtigungsfreie Blöcke + Schlafdauer in Stunden + Zahl der Planungspausen`. Ihre Terme beschreiben bedingte angepasste Zusammenhänge für diese Ergebnisvariable und diese Fälle. Sie identifizieren für sich allein keine Ursachen.

**Ergebnis interpretieren und prüfen, Teil (e)**

Bei einem Vorwärtspfad wird die Wahl nach jedem ausgewählten Term neu berechnet. Eine Ergänzung, die in einem Schritt nützlich erscheint, kann deshalb in einem späteren Schritt redundant werden. Der Pfad kann zudem stoppen, bevor er den global kleinsten AIC unter Kombinationen erreicht, die durch seine früheren Entscheidungen nie verfügbar wurden. AIC belohnt Anpassung und fügt eine Komplexitätsstrafe hinzu. Das Kriterium belegt weder, dass ein ausgewähltes Modell die Wahrheit der Datenerzeugung darstellt, noch dass seine Vorhersagen generalisieren. Die Leistung an neuen Daten erfordert eine getrennte Validierung. AIC-Werte für unterschiedliche Ergebnisvariablen oder Fallmengen gehören nicht zu einer gemeinsam vergleichbaren Kandidatenfamilie.

### T07-A05-V08: Museumsbesuche und historisches Wissen

**Vor dem Rechnen begründen, Teil (a)**

Für M1 ergibt sich zum Beispiel $-2(-145.0)+2(3)=296.00$. Dieselbe Regel ergibt für alle vier Modelle:

| Modell | AIC | Delta AIC |
| --- | --- | --- |
| M1 | 296.00 | 11.20 |
| M2 | 288.00 | 3.20 |
| M3 | 286.00 | 1.20 |
| M4 | 284.80 | 0.00 |

**Berechnung durchführen, Teil (b)**

In Schritt 1 wird M2 ausgewählt, weil 288.00 kleiner als die anderen angezeigten Werte von Schritt 1 und kleiner als der Wert 296.00 von M1 ist. In Schritt 2 wird M3 ausgewählt, weil sein AIC kleiner als der aktuelle Wert von M2 ist. In Schritt 3 wird danach M4 ausgewählt, weil sein AIC unter demjenigen von M3 liegt.

**Berechnung durchführen, Teil (c)**

Die Koordinaten des ausgewählten Pfads lauten (0, 296.00), (1, 288.00), (2, 286.00), (3, 284.80). Trage den Schritt auf der horizontalen Achse und den AIC auf der vertikalen Achse ab. Verbinde nur aufeinanderfolgende ausgewählte Modelle und ende dort, wo die Regel stoppt. Die fallenden Abschnitte zeigen Verbesserungen des relativen Gleichgewichts zwischen Anpassung und Komplexität entlang dieses bestimmten Pfads.

**Berechnung durchführen, Teil (d)**

Die endgültige ausgewählte Formel lautet `Punktwert des historischen Wissens ~ Museumsbesuche + Punktwert des geschichtlichen Vorwissens + Zahl der Ausstellungsnotizen + ein vorab festgelegter Produktterm`. Ihre Terme beschreiben bedingte angepasste Zusammenhänge für diese Ergebnisvariable und diese Fälle. Sie identifizieren für sich allein keine Ursachen.

**Ergebnis interpretieren und prüfen, Teil (e)**

Bei einem Vorwärtspfad wird die Wahl nach jedem ausgewählten Term neu berechnet. Eine Ergänzung, die in einem Schritt nützlich erscheint, kann deshalb in einem späteren Schritt redundant werden. Der Pfad kann zudem stoppen, bevor er den global kleinsten AIC unter Kombinationen erreicht, die durch seine früheren Entscheidungen nie verfügbar wurden. AIC belohnt Anpassung und fügt eine Komplexitätsstrafe hinzu. Das Kriterium belegt weder, dass ein ausgewähltes Modell die Wahrheit der Datenerzeugung darstellt, noch dass seine Vorhersagen generalisieren. Die Leistung an neuen Daten erfordert eine getrennte Validierung. AIC-Werte für unterschiedliche Ergebnisvariablen oder Fallmengen gehören nicht zu einer gemeinsam vergleichbaren Kandidatenfamilie.

### T07-A05-V09: Peer-Feedback und Überarbeitungsqualität

**Vor dem Rechnen begründen, Teil (a)**

Für M1 ergibt sich zum Beispiel $-2(-190.0)+2(3)=386.00$. Dieselbe Regel ergibt für alle vier Modelle:

| Modell | AIC | Delta AIC |
| --- | --- | --- |
| M1 | 386.00 | 16.00 |
| M2 | 370.00 | 0.00 |
| M3 | 370.60 | 0.60 |
| M4 | 371.80 | 1.80 |

**Berechnung durchführen, Teil (b)**

In Schritt 1 wird M2 ausgewählt, weil 370.00 kleiner als die anderen angezeigten Werte von Schritt 1 und kleiner als der Wert 386.00 von M1 ist. In Schritt 2 wird gestoppt, weil keine Ergänzung einen AIC unter dem aktuellen Wert von M2 besitzt. Auf diesem Vorwärtspfad wird später kein Produktterm ausgewählt.

**Berechnung durchführen, Teil (c)**

Die Koordinaten des ausgewählten Pfads lauten (0, 386.00), (1, 370.00). Trage den Schritt auf der horizontalen Achse und den AIC auf der vertikalen Achse ab. Verbinde nur aufeinanderfolgende ausgewählte Modelle und ende dort, wo die Regel stoppt. Die fallenden Abschnitte zeigen Verbesserungen des relativen Gleichgewichts zwischen Anpassung und Komplexität entlang dieses bestimmten Pfads.

**Berechnung durchführen, Teil (d)**

Die endgültige ausgewählte Formel lautet `Punktwert der Überarbeitungsqualität ~ Runden mit Peer-Feedback + Ausgangswert der Schreibqualität`. Ihre Terme beschreiben bedingte angepasste Zusammenhänge für diese Ergebnisvariable und diese Fälle. Sie identifizieren für sich allein keine Ursachen.

**Ergebnis interpretieren und prüfen, Teil (e)**

Bei einem Vorwärtspfad wird die Wahl nach jedem ausgewählten Term neu berechnet. Eine Ergänzung, die in einem Schritt nützlich erscheint, kann deshalb in einem späteren Schritt redundant werden. Der Pfad kann zudem stoppen, bevor er den global kleinsten AIC unter Kombinationen erreicht, die durch seine früheren Entscheidungen nie verfügbar wurden. AIC belohnt Anpassung und fügt eine Komplexitätsstrafe hinzu. Das Kriterium belegt weder, dass ein ausgewähltes Modell die Wahrheit der Datenerzeugung darstellt, noch dass seine Vorhersagen generalisieren. Die Leistung an neuen Daten erfordert eine getrennte Validierung. AIC-Werte für unterschiedliche Ergebnisvariablen oder Fallmengen gehören nicht zu einer gemeinsam vergleichbaren Kandidatenfamilie.

### T07-A05-V10: Planungssitzungen und Bearbeitungszeit

**Vor dem Rechnen begründen, Teil (a)**

Für M1 ergibt sich zum Beispiel $-2(-158.0)+2(3)=322.00$. Dieselbe Regel ergibt für alle vier Modelle:

| Modell | AIC | Delta AIC |
| --- | --- | --- |
| M1 | 322.00 | 22.00 |
| M2 | 306.00 | 6.00 |
| M3 | 300.00 | 0.00 |
| M4 | 300.80 | 0.80 |

**Berechnung durchführen, Teil (b)**

In Schritt 1 wird M2 ausgewählt, weil 306.00 kleiner als die anderen angezeigten Werte von Schritt 1 und kleiner als der Wert 322.00 von M1 ist. In Schritt 2 wird M3 ausgewählt, weil sein AIC kleiner als der aktuelle Wert von M2 ist. Auf diesem Vorwärtspfad wird später kein Produktterm ausgewählt.

**Berechnung durchführen, Teil (c)**

Die Koordinaten des ausgewählten Pfads lauten (0, 322.00), (1, 306.00), (2, 300.00). Trage den Schritt auf der horizontalen Achse und den AIC auf der vertikalen Achse ab. Verbinde nur aufeinanderfolgende ausgewählte Modelle und ende dort, wo die Regel stoppt. Die fallenden Abschnitte zeigen Verbesserungen des relativen Gleichgewichts zwischen Anpassung und Komplexität entlang dieses bestimmten Pfads.

**Berechnung durchführen, Teil (d)**

Die endgültige ausgewählte Formel lautet `Bearbeitungszeit ~ Planungssitzungen + Punktwert der Aufgabenkomplexität + Zahl der Fortschrittskontrollen`. Ihre Terme beschreiben bedingte angepasste Zusammenhänge für diese Ergebnisvariable und diese Fälle. Sie identifizieren für sich allein keine Ursachen.

**Ergebnis interpretieren und prüfen, Teil (e)**

Bei einem Vorwärtspfad wird die Wahl nach jedem ausgewählten Term neu berechnet. Eine Ergänzung, die in einem Schritt nützlich erscheint, kann deshalb in einem späteren Schritt redundant werden. Der Pfad kann zudem stoppen, bevor er den global kleinsten AIC unter Kombinationen erreicht, die durch seine früheren Entscheidungen nie verfügbar wurden. AIC belohnt Anpassung und fügt eine Komplexitätsstrafe hinzu. Das Kriterium belegt weder, dass ein ausgewähltes Modell die Wahrheit der Datenerzeugung darstellt, noch dass seine Vorhersagen generalisieren. Die Leistung an neuen Daten erfordert eine getrennte Validierung. AIC-Werte für unterschiedliche Ergebnisvariablen oder Fallmengen gehören nicht zu einer gemeinsam vergleichbaren Kandidatenfamilie.

## A07: Ein additives Gruppenmodell interpretieren

### T07-A07-V01: Lernbegleitung und statistisches Denken

**Vor dem Rechnen begründen, Teil (a)**

Setze für die Gruppe „Ohne Lernbegleitung“ $G=0$: $\hat Y=42.00+(3.00)X$. Setze für die Gruppe „Mit Lernbegleitung“ $G=1$: $\hat Y=47.00+(3.00)X$. Der Achsenabschnitt 42.00 ist der angepasste Wert der Ergebnisvariable „Punktwert im statistischen Denken“ in der Gruppe „Ohne Lernbegleitung“, wenn der Prädiktor „Übungsstunden“ null ist. Er kann mathematisch notwendig, aber inhaltlich wenig hilfreich sein, wenn null ausserhalb des sinnvollen Bereichs liegt.

**Berechnung durchführen, Teil (b)**

Innerhalb jeder Gruppe geht eine Zunahme des Prädiktors „Übungsstunden“ um eine Einheit mit einer angepassten Veränderung der Ergebnisvariable „Punktwert im statistischen Denken“ um 3.00 Einheiten einher. Beim selben Wert des Prädiktors liegt der angepasste Wert für die Gruppe „Mit Lernbegleitung“ um 5.00 Einheiten höher als für „Ohne Lernbegleitung“. "Beim selben Wert" bezeichnet den bedingten Modellvergleich und keinen Eingriff.

**Berechnung durchführen, Teil (c)**

Einsetzen ergibt:

| Gruppe | X | Angepasster Wert der Ergebnisvariable „Punktwert im statistischen Denken“ |
| --- | --- | --- |
| Ohne Lernbegleitung | 2.0 | 48.00 |
| Ohne Lernbegleitung | 6.0 | 60.00 |
| Mit Lernbegleitung | 2.0 | 53.00 |
| Mit Lernbegleitung | 6.0 | 65.00 |

**Ergebnis interpretieren und prüfen, Teil (d)**

Beide Gleichungen haben die Steigung 3.00. Gleiche horizontale Veränderungen erzeugen deshalb gleiche angepasste vertikale Veränderungen. Ihre Achsenabschnitte unterscheiden sich um 5.00. Werden die beiden angepassten Werte an einem der gezeigten $X$-Werte voneinander subtrahiert, entsteht derselbe konstante Abstand. Das Modell enthält keinen $XG$-Produktterm und erzwingt daher parallele angepasste Linien. Der Abstand ist ein bereinigter Zusammenhang. Ohne ein geeignetes Design und geeignete Annahmen beweist er nicht, dass eine Veränderung der Gruppenzugehörigkeit die Ergebnisvariable verändern würde.

### T07-A07-V02: Archiverfahrung und Suche

**Vor dem Rechnen begründen, Teil (a)**

Setze für die Gruppe „Neue Mitarbeitende“ $G=0$: $\hat Y=36.00+(-1.80)X$. Setze für die Gruppe „Erfahrene Mitarbeitende“ $G=1$: $\hat Y=32.00+(-1.80)X$. Der Achsenabschnitt 36.00 ist der angepasste Wert der Ergebnisvariable „Suchzeit“ in der Gruppe „Neue Mitarbeitende“, wenn der Prädiktor „Übungssitzungen“ null ist. Er kann mathematisch notwendig, aber inhaltlich wenig hilfreich sein, wenn null ausserhalb des sinnvollen Bereichs liegt.

**Berechnung durchführen, Teil (b)**

Innerhalb jeder Gruppe geht eine Zunahme des Prädiktors „Übungssitzungen“ um eine Einheit mit einer angepassten Veränderung der Ergebnisvariable „Suchzeit“ um -1.80 Einheiten einher. Beim selben Wert des Prädiktors liegt der angepasste Wert für die Gruppe „Erfahrene Mitarbeitende“ um 4.00 Einheiten tiefer als für „Neue Mitarbeitende“. "Beim selben Wert" bezeichnet den bedingten Modellvergleich und keinen Eingriff.

**Berechnung durchführen, Teil (c)**

Einsetzen ergibt:

| Gruppe | X | Angepasster Wert der Ergebnisvariable „Suchzeit“ |
| --- | --- | --- |
| Neue Mitarbeitende | 1.0 | 34.20 |
| Neue Mitarbeitende | 5.0 | 27.00 |
| Erfahrene Mitarbeitende | 1.0 | 30.20 |
| Erfahrene Mitarbeitende | 5.0 | 23.00 |

**Ergebnis interpretieren und prüfen, Teil (d)**

Beide Gleichungen haben die Steigung -1.80. Gleiche horizontale Veränderungen erzeugen deshalb gleiche angepasste vertikale Veränderungen. Ihre Achsenabschnitte unterscheiden sich um -4.00. Werden die beiden angepassten Werte an einem der gezeigten $X$-Werte voneinander subtrahiert, entsteht derselbe konstante Abstand. Das Modell enthält keinen $XG$-Produktterm und erzwingt daher parallele angepasste Linien. Der Abstand ist ein bereinigter Zusammenhang. Ohne ein geeignetes Design und geeignete Annahmen beweist er nicht, dass eine Veränderung der Gruppenzugehörigkeit die Ergebnisvariable verändern würde.

### T07-A07-V03: Leseformat und Textverständnis

**Vor dem Rechnen begründen, Teil (a)**

Setze für die Gruppe „Gedruckt“ $G=0$: $\hat Y=51.00+(2.20)X$. Setze für die Gruppe „Digital“ $G=1$: $\hat Y=48.50+(2.20)X$. Der Achsenabschnitt 51.00 ist der angepasste Wert der Ergebnisvariable „Punktwert im Textverständnis“ in der Gruppe „Gedruckt“, wenn der Prädiktor „Lesestunden“ null ist. Er kann mathematisch notwendig, aber inhaltlich wenig hilfreich sein, wenn null ausserhalb des sinnvollen Bereichs liegt.

**Berechnung durchführen, Teil (b)**

Innerhalb jeder Gruppe geht eine Zunahme des Prädiktors „Lesestunden“ um eine Einheit mit einer angepassten Veränderung der Ergebnisvariable „Punktwert im Textverständnis“ um 2.20 Einheiten einher. Beim selben Wert des Prädiktors liegt der angepasste Wert für die Gruppe „Digital“ um 2.50 Einheiten tiefer als für „Gedruckt“. "Beim selben Wert" bezeichnet den bedingten Modellvergleich und keinen Eingriff.

**Berechnung durchführen, Teil (c)**

Einsetzen ergibt:

| Gruppe | X | Angepasster Wert der Ergebnisvariable „Punktwert im Textverständnis“ |
| --- | --- | --- |
| Gedruckt | 2.0 | 55.40 |
| Gedruckt | 7.0 | 66.40 |
| Digital | 2.0 | 52.90 |
| Digital | 7.0 | 63.90 |

**Ergebnis interpretieren und prüfen, Teil (d)**

Beide Gleichungen haben die Steigung 2.20. Gleiche horizontale Veränderungen erzeugen deshalb gleiche angepasste vertikale Veränderungen. Ihre Achsenabschnitte unterscheiden sich um -2.50. Werden die beiden angepassten Werte an einem der gezeigten $X$-Werte voneinander subtrahiert, entsteht derselbe konstante Abstand. Das Modell enthält keinen $XG$-Produktterm und erzwingt daher parallele angepasste Linien. Der Abstand ist ein bereinigter Zusammenhang. Ohne ein geeignetes Design und geeignete Annahmen beweist er nicht, dass eine Veränderung der Gruppenzugehörigkeit die Ergebnisvariable verändern würde.

### T07-A07-V04: Streckenhilfe und Navigation

**Vor dem Rechnen begründen, Teil (a)**

Setze für die Gruppe „Papierkarte“ $G=0$: $\hat Y=44.00+(-2.00)X$. Setze für die Gruppe „Karten-App“ $G=1$: $\hat Y=41.00+(-2.00)X$. Der Achsenabschnitt 44.00 ist der angepasste Wert der Ergebnisvariable „Navigationszeit“ in der Gruppe „Papierkarte“, wenn der Prädiktor „Übungsversuche“ null ist. Er kann mathematisch notwendig, aber inhaltlich wenig hilfreich sein, wenn null ausserhalb des sinnvollen Bereichs liegt.

**Berechnung durchführen, Teil (b)**

Innerhalb jeder Gruppe geht eine Zunahme des Prädiktors „Übungsversuche“ um eine Einheit mit einer angepassten Veränderung der Ergebnisvariable „Navigationszeit“ um -2.00 Einheiten einher. Beim selben Wert des Prädiktors liegt der angepasste Wert für die Gruppe „Karten-App“ um 3.00 Einheiten tiefer als für „Papierkarte“. "Beim selben Wert" bezeichnet den bedingten Modellvergleich und keinen Eingriff.

**Berechnung durchführen, Teil (c)**

Einsetzen ergibt:

| Gruppe | X | Angepasster Wert der Ergebnisvariable „Navigationszeit“ |
| --- | --- | --- |
| Papierkarte | 1.0 | 42.00 |
| Papierkarte | 4.0 | 36.00 |
| Karten-App | 1.0 | 39.00 |
| Karten-App | 4.0 | 33.00 |

**Ergebnis interpretieren und prüfen, Teil (d)**

Beide Gleichungen haben die Steigung -2.00. Gleiche horizontale Veränderungen erzeugen deshalb gleiche angepasste vertikale Veränderungen. Ihre Achsenabschnitte unterscheiden sich um -3.00. Werden die beiden angepassten Werte an einem der gezeigten $X$-Werte voneinander subtrahiert, entsteht derselbe konstante Abstand. Das Modell enthält keinen $XG$-Produktterm und erzwingt daher parallele angepasste Linien. Der Abstand ist ein bereinigter Zusammenhang. Ohne ein geeignetes Design und geeignete Annahmen beweist er nicht, dass eine Veränderung der Gruppenzugehörigkeit die Ergebnisvariable verändern würde.

### T07-A07-V05: Suchhilfe und Genauigkeit

**Vor dem Rechnen begründen, Teil (a)**

Setze für die Gruppe „Keine Hilfe“ $G=0$: $\hat Y=55.00+(2.50)X$. Setze für die Gruppe „Checkliste“ $G=1$: $\hat Y=59.00+(2.50)X$. Der Achsenabschnitt 55.00 ist der angepasste Wert der Ergebnisvariable „Punktwert der Genauigkeit“ in der Gruppe „Keine Hilfe“, wenn der Prädiktor „Übungsblöcke“ null ist. Er kann mathematisch notwendig, aber inhaltlich wenig hilfreich sein, wenn null ausserhalb des sinnvollen Bereichs liegt.

**Berechnung durchführen, Teil (b)**

Innerhalb jeder Gruppe geht eine Zunahme des Prädiktors „Übungsblöcke“ um eine Einheit mit einer angepassten Veränderung der Ergebnisvariable „Punktwert der Genauigkeit“ um 2.50 Einheiten einher. Beim selben Wert des Prädiktors liegt der angepasste Wert für die Gruppe „Checkliste“ um 4.00 Einheiten höher als für „Keine Hilfe“. "Beim selben Wert" bezeichnet den bedingten Modellvergleich und keinen Eingriff.

**Berechnung durchführen, Teil (c)**

Einsetzen ergibt:

| Gruppe | X | Angepasster Wert der Ergebnisvariable „Punktwert der Genauigkeit“ |
| --- | --- | --- |
| Keine Hilfe | 0.0 | 55.00 |
| Keine Hilfe | 4.0 | 65.00 |
| Checkliste | 0.0 | 59.00 |
| Checkliste | 4.0 | 69.00 |

**Ergebnis interpretieren und prüfen, Teil (d)**

Beide Gleichungen haben die Steigung 2.50. Gleiche horizontale Veränderungen erzeugen deshalb gleiche angepasste vertikale Veränderungen. Ihre Achsenabschnitte unterscheiden sich um 4.00. Werden die beiden angepassten Werte an einem der gezeigten $X$-Werte voneinander subtrahiert, entsteht derselbe konstante Abstand. Das Modell enthält keinen $XG$-Produktterm und erzwingt daher parallele angepasste Linien. Der Abstand ist ein bereinigter Zusammenhang. Ohne ein geeignetes Design und geeignete Annahmen beweist er nicht, dass eine Veränderung der Gruppenzugehörigkeit die Ergebnisvariable verändern würde.

### T07-A07-V06: Workshopformat und Selbstvertrauen

**Vor dem Rechnen begründen, Teil (a)**

Setze für die Gruppe „Online“ $G=0$: $\hat Y=38.00+(3.20)X$. Setze für die Gruppe „Vor Ort“ $G=1$: $\hat Y=41.50+(3.20)X$. Der Achsenabschnitt 38.00 ist der angepasste Wert der Ergebnisvariable „Punktwert des Selbstvertrauens“ in der Gruppe „Online“, wenn der Prädiktor „besuchte Sitzungen“ null ist. Er kann mathematisch notwendig, aber inhaltlich wenig hilfreich sein, wenn null ausserhalb des sinnvollen Bereichs liegt.

**Berechnung durchführen, Teil (b)**

Innerhalb jeder Gruppe geht eine Zunahme des Prädiktors „besuchte Sitzungen“ um eine Einheit mit einer angepassten Veränderung der Ergebnisvariable „Punktwert des Selbstvertrauens“ um 3.20 Einheiten einher. Beim selben Wert des Prädiktors liegt der angepasste Wert für die Gruppe „Vor Ort“ um 3.50 Einheiten höher als für „Online“. "Beim selben Wert" bezeichnet den bedingten Modellvergleich und keinen Eingriff.

**Berechnung durchführen, Teil (c)**

Einsetzen ergibt:

| Gruppe | X | Angepasster Wert der Ergebnisvariable „Punktwert des Selbstvertrauens“ |
| --- | --- | --- |
| Online | 1.0 | 41.20 |
| Online | 5.0 | 54.00 |
| Vor Ort | 1.0 | 44.70 |
| Vor Ort | 5.0 | 57.50 |

**Ergebnis interpretieren und prüfen, Teil (d)**

Beide Gleichungen haben die Steigung 3.20. Gleiche horizontale Veränderungen erzeugen deshalb gleiche angepasste vertikale Veränderungen. Ihre Achsenabschnitte unterscheiden sich um 3.50. Werden die beiden angepassten Werte an einem der gezeigten $X$-Werte voneinander subtrahiert, entsteht derselbe konstante Abstand. Das Modell enthält keinen $XG$-Produktterm und erzwingt daher parallele angepasste Linien. Der Abstand ist ein bereinigter Zusammenhang. Ohne ein geeignetes Design und geeignete Annahmen beweist er nicht, dass eine Veränderung der Gruppenzugehörigkeit die Ergebnisvariable verändern würde.

### T07-A07-V07: Konzentrationsumgebung und Genauigkeit

**Vor dem Rechnen begründen, Teil (a)**

Setze für die Gruppe „Gemeinschaftsraum“ $G=0$: $\hat Y=60.00+(1.70)X$. Setze für die Gruppe „Ruhiger Raum“ $G=1$: $\hat Y=64.50+(1.70)X$. Der Achsenabschnitt 60.00 ist der angepasste Wert der Ergebnisvariable „Punktwert der Aufgabengenauigkeit“ in der Gruppe „Gemeinschaftsraum“, wenn der Prädiktor „Konzentrationsblöcke“ null ist. Er kann mathematisch notwendig, aber inhaltlich wenig hilfreich sein, wenn null ausserhalb des sinnvollen Bereichs liegt.

**Berechnung durchführen, Teil (b)**

Innerhalb jeder Gruppe geht eine Zunahme des Prädiktors „Konzentrationsblöcke“ um eine Einheit mit einer angepassten Veränderung der Ergebnisvariable „Punktwert der Aufgabengenauigkeit“ um 1.70 Einheiten einher. Beim selben Wert des Prädiktors liegt der angepasste Wert für die Gruppe „Ruhiger Raum“ um 4.50 Einheiten höher als für „Gemeinschaftsraum“. "Beim selben Wert" bezeichnet den bedingten Modellvergleich und keinen Eingriff.

**Berechnung durchführen, Teil (c)**

Einsetzen ergibt:

| Gruppe | X | Angepasster Wert der Ergebnisvariable „Punktwert der Aufgabengenauigkeit“ |
| --- | --- | --- |
| Gemeinschaftsraum | 2.0 | 63.40 |
| Gemeinschaftsraum | 8.0 | 73.60 |
| Ruhiger Raum | 2.0 | 67.90 |
| Ruhiger Raum | 8.0 | 78.10 |

**Ergebnis interpretieren und prüfen, Teil (d)**

Beide Gleichungen haben die Steigung 1.70. Gleiche horizontale Veränderungen erzeugen deshalb gleiche angepasste vertikale Veränderungen. Ihre Achsenabschnitte unterscheiden sich um 4.50. Werden die beiden angepassten Werte an einem der gezeigten $X$-Werte voneinander subtrahiert, entsteht derselbe konstante Abstand. Das Modell enthält keinen $XG$-Produktterm und erzwingt daher parallele angepasste Linien. Der Abstand ist ein bereinigter Zusammenhang. Ohne ein geeignetes Design und geeignete Annahmen beweist er nicht, dass eine Veränderung der Gruppenzugehörigkeit die Ergebnisvariable verändern würde.

### T07-A07-V08: Museumsführung und Wissen

**Vor dem Rechnen begründen, Teil (a)**

Setze für die Gruppe „Selbstständig“ $G=0$: $\hat Y=47.00+(4.00)X$. Setze für die Gruppe „Geführt“ $G=1$: $\hat Y=53.00+(4.00)X$. Der Achsenabschnitt 47.00 ist der angepasste Wert der Ergebnisvariable „Punktwert des Wissens“ in der Gruppe „Selbstständig“, wenn der Prädiktor „Besuche“ null ist. Er kann mathematisch notwendig, aber inhaltlich wenig hilfreich sein, wenn null ausserhalb des sinnvollen Bereichs liegt.

**Berechnung durchführen, Teil (b)**

Innerhalb jeder Gruppe geht eine Zunahme des Prädiktors „Besuche“ um eine Einheit mit einer angepassten Veränderung der Ergebnisvariable „Punktwert des Wissens“ um 4.00 Einheiten einher. Beim selben Wert des Prädiktors liegt der angepasste Wert für die Gruppe „Geführt“ um 6.00 Einheiten höher als für „Selbstständig“. "Beim selben Wert" bezeichnet den bedingten Modellvergleich und keinen Eingriff.

**Berechnung durchführen, Teil (c)**

Einsetzen ergibt:

| Gruppe | X | Angepasster Wert der Ergebnisvariable „Punktwert des Wissens“ |
| --- | --- | --- |
| Selbstständig | 0.0 | 47.00 |
| Selbstständig | 3.0 | 59.00 |
| Geführt | 0.0 | 53.00 |
| Geführt | 3.0 | 65.00 |

**Ergebnis interpretieren und prüfen, Teil (d)**

Beide Gleichungen haben die Steigung 4.00. Gleiche horizontale Veränderungen erzeugen deshalb gleiche angepasste vertikale Veränderungen. Ihre Achsenabschnitte unterscheiden sich um 6.00. Werden die beiden angepassten Werte an einem der gezeigten $X$-Werte voneinander subtrahiert, entsteht derselbe konstante Abstand. Das Modell enthält keinen $XG$-Produktterm und erzwingt daher parallele angepasste Linien. Der Abstand ist ein bereinigter Zusammenhang. Ohne ein geeignetes Design und geeignete Annahmen beweist er nicht, dass eine Veränderung der Gruppenzugehörigkeit die Ergebnisvariable verändern würde.

### T07-A07-V09: Feedbackformat und Überarbeitung

**Vor dem Rechnen begründen, Teil (a)**

Setze für die Gruppe „Schriftlich“ $G=0$: $\hat Y=52.00+(3.50)X$. Setze für die Gruppe „Gespräch“ $G=1$: $\hat Y=54.00+(3.50)X$. Der Achsenabschnitt 52.00 ist der angepasste Wert der Ergebnisvariable „Punktwert der Überarbeitung“ in der Gruppe „Schriftlich“, wenn der Prädiktor „Feedbackrunden“ null ist. Er kann mathematisch notwendig, aber inhaltlich wenig hilfreich sein, wenn null ausserhalb des sinnvollen Bereichs liegt.

**Berechnung durchführen, Teil (b)**

Innerhalb jeder Gruppe geht eine Zunahme des Prädiktors „Feedbackrunden“ um eine Einheit mit einer angepassten Veränderung der Ergebnisvariable „Punktwert der Überarbeitung“ um 3.50 Einheiten einher. Beim selben Wert des Prädiktors liegt der angepasste Wert für die Gruppe „Gespräch“ um 2.00 Einheiten höher als für „Schriftlich“. "Beim selben Wert" bezeichnet den bedingten Modellvergleich und keinen Eingriff.

**Berechnung durchführen, Teil (c)**

Einsetzen ergibt:

| Gruppe | X | Angepasster Wert der Ergebnisvariable „Punktwert der Überarbeitung“ |
| --- | --- | --- |
| Schriftlich | 1.0 | 55.50 |
| Schriftlich | 4.0 | 66.00 |
| Gespräch | 1.0 | 57.50 |
| Gespräch | 4.0 | 68.00 |

**Ergebnis interpretieren und prüfen, Teil (d)**

Beide Gleichungen haben die Steigung 3.50. Gleiche horizontale Veränderungen erzeugen deshalb gleiche angepasste vertikale Veränderungen. Ihre Achsenabschnitte unterscheiden sich um 2.00. Werden die beiden angepassten Werte an einem der gezeigten $X$-Werte voneinander subtrahiert, entsteht derselbe konstante Abstand. Das Modell enthält keinen $XG$-Produktterm und erzwingt daher parallele angepasste Linien. Der Abstand ist ein bereinigter Zusammenhang. Ohne ein geeignetes Design und geeignete Annahmen beweist er nicht, dass eine Veränderung der Gruppenzugehörigkeit die Ergebnisvariable verändern würde.

### T07-A07-V10: Planungsformat und Abschluss

**Vor dem Rechnen begründen, Teil (a)**

Setze für die Gruppe „Papier“ $G=0$: $\hat Y=70.00+(-2.40)X$. Setze für die Gruppe „Digital“ $G=1$: $\hat Y=66.50+(-2.40)X$. Der Achsenabschnitt 70.00 ist der angepasste Wert der Ergebnisvariable „Bearbeitungszeit“ in der Gruppe „Papier“, wenn der Prädiktor „Planungssitzungen“ null ist. Er kann mathematisch notwendig, aber inhaltlich wenig hilfreich sein, wenn null ausserhalb des sinnvollen Bereichs liegt.

**Berechnung durchführen, Teil (b)**

Innerhalb jeder Gruppe geht eine Zunahme des Prädiktors „Planungssitzungen“ um eine Einheit mit einer angepassten Veränderung der Ergebnisvariable „Bearbeitungszeit“ um -2.40 Einheiten einher. Beim selben Wert des Prädiktors liegt der angepasste Wert für die Gruppe „Digital“ um 3.50 Einheiten tiefer als für „Papier“. "Beim selben Wert" bezeichnet den bedingten Modellvergleich und keinen Eingriff.

**Berechnung durchführen, Teil (c)**

Einsetzen ergibt:

| Gruppe | X | Angepasster Wert der Ergebnisvariable „Bearbeitungszeit“ |
| --- | --- | --- |
| Papier | 1.0 | 67.60 |
| Papier | 6.0 | 55.60 |
| Digital | 1.0 | 64.10 |
| Digital | 6.0 | 52.10 |

**Ergebnis interpretieren und prüfen, Teil (d)**

Beide Gleichungen haben die Steigung -2.40. Gleiche horizontale Veränderungen erzeugen deshalb gleiche angepasste vertikale Veränderungen. Ihre Achsenabschnitte unterscheiden sich um -3.50. Werden die beiden angepassten Werte an einem der gezeigten $X$-Werte voneinander subtrahiert, entsteht derselbe konstante Abstand. Das Modell enthält keinen $XG$-Produktterm und erzwingt daher parallele angepasste Linien. Der Abstand ist ein bereinigter Zusammenhang. Ohne ein geeignetes Design und geeignete Annahmen beweist er nicht, dass eine Veränderung der Gruppenzugehörigkeit die Ergebnisvariable verändern würde.

## A08: Die Referenz wechseln, ohne angepasste Beziehungen zu verändern

### T07-A08-V01: Übungsformat neu referenzieren

**Vor dem Rechnen begründen, Teil (a)**

Die neue Referenz ist die alte Gruppe mit $G=1$. Ihr alter Achsenabschnitt wird daher zum neuen Achsenabschnitt: $b'_0=40.00+(4.50)=44.50$. Die gemeinsame Steigung bleibt $b'_1=2.80$. Der Kontrast kehrt seine Richtung um, somit gilt $b'_2=-(4.50)=-4.50$.

**Berechnung durchführen, Teil (b)**

Für die Gruppe „Zu zweit“ ist $H=0$, woraus $\hat Y=44.50+(2.80)X$ folgt. Für die Gruppe „Allein“ ist $H=1$, woraus $\hat Y=44.50+(2.80)X+(-4.50)=40.00+(2.80)X$ folgt. Beim selben $X$ liegt der angepasste Wert für „Allein“ um 4.50 Einheiten tiefer als für „Zu zweit“.

**Berechnung durchführen, Teil (c)**

Beide Codierungen ergeben:

| Gruppe | X | Anpassung aus alter Codierung | Anpassung aus neuer Codierung |
| --- | --- | --- | --- |
| Allein | 1.0 | 42.80 | 42.80 |
| Allein | 5.0 | 54.00 | 54.00 |
| Zu zweit | 1.0 | 47.30 | 47.30 |
| Zu zweit | 5.0 | 58.50 | 58.50 |

**Ergebnis interpretieren und prüfen, Teil (d)**

In jeder Zeile sind die angepassten Werte unter beiden Codierungen identisch. Das Wechseln der Referenz verändert, welche Gruppe der Achsenabschnitt darstellt, und kehrt den angezeigten Gruppenkontrast um. Es beschreibt jedoch dieselben zwei Linien. Weil jeder Fall denselben angepassten Wert behält, bleibt auch jedes Residuum unverändert, wenn der angepasste Wert von der beobachteten Ergebnisvariable subtrahiert wird. Die Referenzwahl verändert die Darstellung, nicht die Modellanpassung oder die zugrunde liegenden angepassten Beziehungen.

### T07-A08-V02: Archivrolle neu referenzieren

**Vor dem Rechnen begründen, Teil (a)**

Die neue Referenz ist die alte Gruppe mit $G=1$. Ihr alter Achsenabschnitt wird daher zum neuen Achsenabschnitt: $b'_0=35.00+(-5.00)=30.00$. Die gemeinsame Steigung bleibt $b'_1=-1.60$. Der Kontrast kehrt seine Richtung um, somit gilt $b'_2=-(-5.00)=5.00$.

**Berechnung durchführen, Teil (b)**

Für die Gruppe „Koordination“ ist $H=0$, woraus $\hat Y=30.00+(-1.60)X$ folgt. Für die Gruppe „Assistenz“ ist $H=1$, woraus $\hat Y=30.00+(-1.60)X+(5.00)=35.00+(-1.60)X$ folgt. Beim selben $X$ liegt der angepasste Wert für „Assistenz“ um 5.00 Einheiten höher als für „Koordination“.

**Berechnung durchführen, Teil (c)**

Beide Codierungen ergeben:

| Gruppe | X | Anpassung aus alter Codierung | Anpassung aus neuer Codierung |
| --- | --- | --- | --- |
| Assistenz | 0.0 | 35.00 | 35.00 |
| Assistenz | 4.0 | 28.60 | 28.60 |
| Koordination | 0.0 | 30.00 | 30.00 |
| Koordination | 4.0 | 23.60 | 23.60 |

**Ergebnis interpretieren und prüfen, Teil (d)**

In jeder Zeile sind die angepassten Werte unter beiden Codierungen identisch. Das Wechseln der Referenz verändert, welche Gruppe der Achsenabschnitt darstellt, und kehrt den angezeigten Gruppenkontrast um. Es beschreibt jedoch dieselben zwei Linien. Weil jeder Fall denselben angepassten Wert behält, bleibt auch jedes Residuum unverändert, wenn der angepasste Wert von der beobachteten Ergebnisvariable subtrahiert wird. Die Referenzwahl verändert die Darstellung, nicht die Modellanpassung oder die zugrunde liegenden angepassten Beziehungen.

### T07-A08-V03: Lesemedium neu referenzieren

**Vor dem Rechnen begründen, Teil (a)**

Die neue Referenz ist die alte Gruppe mit $G=1$. Ihr alter Achsenabschnitt wird daher zum neuen Achsenabschnitt: $b'_0=50.00+(-3.00)=47.00$. Die gemeinsame Steigung bleibt $b'_1=2.00$. Der Kontrast kehrt seine Richtung um, somit gilt $b'_2=-(-3.00)=3.00$.

**Berechnung durchführen, Teil (b)**

Für die Gruppe „Audio“ ist $H=0$, woraus $\hat Y=47.00+(2.00)X$ folgt. Für die Gruppe „Gedruckt“ ist $H=1$, woraus $\hat Y=47.00+(2.00)X+(3.00)=50.00+(2.00)X$ folgt. Beim selben $X$ liegt der angepasste Wert für „Gedruckt“ um 3.00 Einheiten höher als für „Audio“.

**Berechnung durchführen, Teil (c)**

Beide Codierungen ergeben:

| Gruppe | X | Anpassung aus alter Codierung | Anpassung aus neuer Codierung |
| --- | --- | --- | --- |
| Gedruckt | 2.0 | 54.00 | 54.00 |
| Gedruckt | 6.0 | 62.00 | 62.00 |
| Audio | 2.0 | 51.00 | 51.00 |
| Audio | 6.0 | 59.00 | 59.00 |

**Ergebnis interpretieren und prüfen, Teil (d)**

In jeder Zeile sind die angepassten Werte unter beiden Codierungen identisch. Das Wechseln der Referenz verändert, welche Gruppe der Achsenabschnitt darstellt, und kehrt den angezeigten Gruppenkontrast um. Es beschreibt jedoch dieselben zwei Linien. Weil jeder Fall denselben angepassten Wert behält, bleibt auch jedes Residuum unverändert, wenn der angepasste Wert von der beobachteten Ergebnisvariable subtrahiert wird. Die Referenzwahl verändert die Darstellung, nicht die Modellanpassung oder die zugrunde liegenden angepassten Beziehungen.

### T07-A08-V04: Navigationsanzeige neu referenzieren

**Vor dem Rechnen begründen, Teil (a)**

Die neue Referenz ist die alte Gruppe mit $G=1$. Ihr alter Achsenabschnitt wird daher zum neuen Achsenabschnitt: $b'_0=46.00+(-4.00)=42.00$. Die gemeinsame Steigung bleibt $b'_1=-2.20$. Der Kontrast kehrt seine Richtung um, somit gilt $b'_2=-(-4.00)=4.00$.

**Berechnung durchführen, Teil (b)**

Für die Gruppe „Interaktiv“ ist $H=0$, woraus $\hat Y=42.00+(-2.20)X$ folgt. Für die Gruppe „Statisch“ ist $H=1$, woraus $\hat Y=42.00+(-2.20)X+(4.00)=46.00+(-2.20)X$ folgt. Beim selben $X$ liegt der angepasste Wert für „Statisch“ um 4.00 Einheiten höher als für „Interaktiv“.

**Berechnung durchführen, Teil (c)**

Beide Codierungen ergeben:

| Gruppe | X | Anpassung aus alter Codierung | Anpassung aus neuer Codierung |
| --- | --- | --- | --- |
| Statisch | 1.0 | 43.80 | 43.80 |
| Statisch | 5.0 | 35.00 | 35.00 |
| Interaktiv | 1.0 | 39.80 | 39.80 |
| Interaktiv | 5.0 | 31.00 | 31.00 |

**Ergebnis interpretieren und prüfen, Teil (d)**

In jeder Zeile sind die angepassten Werte unter beiden Codierungen identisch. Das Wechseln der Referenz verändert, welche Gruppe der Achsenabschnitt darstellt, und kehrt den angezeigten Gruppenkontrast um. Es beschreibt jedoch dieselben zwei Linien. Weil jeder Fall denselben angepassten Wert behält, bleibt auch jedes Residuum unverändert, wenn der angepasste Wert von der beobachteten Ergebnisvariable subtrahiert wird. Die Referenzwahl verändert die Darstellung, nicht die Modellanpassung oder die zugrunde liegenden angepassten Beziehungen.

### T07-A08-V05: Kataloghilfe neu referenzieren

**Vor dem Rechnen begründen, Teil (a)**

Die neue Referenz ist die alte Gruppe mit $G=1$. Ihr alter Achsenabschnitt wird daher zum neuen Achsenabschnitt: $b'_0=53.00+(3.00)=56.00$. Die gemeinsame Steigung bleibt $b'_1=2.60$. Der Kontrast kehrt seine Richtung um, somit gilt $b'_2=-(3.00)=-3.00$.

**Berechnung durchführen, Teil (b)**

Für die Gruppe „Suchleiste“ ist $H=0$, woraus $\hat Y=56.00+(2.60)X$ folgt. Für die Gruppe „Index“ ist $H=1$, woraus $\hat Y=56.00+(2.60)X+(-3.00)=53.00+(2.60)X$ folgt. Beim selben $X$ liegt der angepasste Wert für „Index“ um 3.00 Einheiten tiefer als für „Suchleiste“.

**Berechnung durchführen, Teil (c)**

Beide Codierungen ergeben:

| Gruppe | X | Anpassung aus alter Codierung | Anpassung aus neuer Codierung |
| --- | --- | --- | --- |
| Index | 0.0 | 53.00 | 53.00 |
| Index | 3.0 | 60.80 | 60.80 |
| Suchleiste | 0.0 | 56.00 | 56.00 |
| Suchleiste | 3.0 | 63.80 | 63.80 |

**Ergebnis interpretieren und prüfen, Teil (d)**

In jeder Zeile sind die angepassten Werte unter beiden Codierungen identisch. Das Wechseln der Referenz verändert, welche Gruppe der Achsenabschnitt darstellt, und kehrt den angezeigten Gruppenkontrast um. Es beschreibt jedoch dieselben zwei Linien. Weil jeder Fall denselben angepassten Wert behält, bleibt auch jedes Residuum unverändert, wenn der angepasste Wert von der beobachteten Ergebnisvariable subtrahiert wird. Die Referenzwahl verändert die Darstellung, nicht die Modellanpassung oder die zugrunde liegenden angepassten Beziehungen.

### T07-A08-V06: Workshopumgebung neu referenzieren

**Vor dem Rechnen begründen, Teil (a)**

Die neue Referenz ist die alte Gruppe mit $G=1$. Ihr alter Achsenabschnitt wird daher zum neuen Achsenabschnitt: $b'_0=37.00+(5.00)=42.00$. Die gemeinsame Steigung bleibt $b'_1=3.00$. Der Kontrast kehrt seine Richtung um, somit gilt $b'_2=-(5.00)=-5.00$.

**Berechnung durchführen, Teil (b)**

Für die Gruppe „Kursraum“ ist $H=0$, woraus $\hat Y=42.00+(3.00)X$ folgt. Für die Gruppe „Online“ ist $H=1$, woraus $\hat Y=42.00+(3.00)X+(-5.00)=37.00+(3.00)X$ folgt. Beim selben $X$ liegt der angepasste Wert für „Online“ um 5.00 Einheiten tiefer als für „Kursraum“.

**Berechnung durchführen, Teil (c)**

Beide Codierungen ergeben:

| Gruppe | X | Anpassung aus alter Codierung | Anpassung aus neuer Codierung |
| --- | --- | --- | --- |
| Online | 1.0 | 40.00 | 40.00 |
| Online | 4.0 | 49.00 | 49.00 |
| Kursraum | 1.0 | 45.00 | 45.00 |
| Kursraum | 4.0 | 54.00 | 54.00 |

**Ergebnis interpretieren und prüfen, Teil (d)**

In jeder Zeile sind die angepassten Werte unter beiden Codierungen identisch. Das Wechseln der Referenz verändert, welche Gruppe der Achsenabschnitt darstellt, und kehrt den angezeigten Gruppenkontrast um. Es beschreibt jedoch dieselben zwei Linien. Weil jeder Fall denselben angepassten Wert behält, bleibt auch jedes Residuum unverändert, wenn der angepasste Wert von der beobachteten Ergebnisvariable subtrahiert wird. Die Referenzwahl verändert die Darstellung, nicht die Modellanpassung oder die zugrunde liegenden angepassten Beziehungen.

### T07-A08-V07: Konzentrationsraum neu referenzieren

**Vor dem Rechnen begründen, Teil (a)**

Die neue Referenz ist die alte Gruppe mit $G=1$. Ihr alter Achsenabschnitt wird daher zum neuen Achsenabschnitt: $b'_0=59.00+(4.00)=63.00$. Die gemeinsame Steigung bleibt $b'_1=1.80$. Der Kontrast kehrt seine Richtung um, somit gilt $b'_2=-(4.00)=-4.00$.

**Berechnung durchführen, Teil (b)**

Für die Gruppe „Privater Raum“ ist $H=0$, woraus $\hat Y=63.00+(1.80)X$ folgt. Für die Gruppe „Offener Raum“ ist $H=1$, woraus $\hat Y=63.00+(1.80)X+(-4.00)=59.00+(1.80)X$ folgt. Beim selben $X$ liegt der angepasste Wert für „Offener Raum“ um 4.00 Einheiten tiefer als für „Privater Raum“.

**Berechnung durchführen, Teil (c)**

Beide Codierungen ergeben:

| Gruppe | X | Anpassung aus alter Codierung | Anpassung aus neuer Codierung |
| --- | --- | --- | --- |
| Offener Raum | 2.0 | 62.60 | 62.60 |
| Offener Raum | 7.0 | 71.60 | 71.60 |
| Privater Raum | 2.0 | 66.60 | 66.60 |
| Privater Raum | 7.0 | 75.60 | 75.60 |

**Ergebnis interpretieren und prüfen, Teil (d)**

In jeder Zeile sind die angepassten Werte unter beiden Codierungen identisch. Das Wechseln der Referenz verändert, welche Gruppe der Achsenabschnitt darstellt, und kehrt den angezeigten Gruppenkontrast um. Es beschreibt jedoch dieselben zwei Linien. Weil jeder Fall denselben angepassten Wert behält, bleibt auch jedes Residuum unverändert, wenn der angepasste Wert von der beobachteten Ergebnisvariable subtrahiert wird. Die Referenzwahl verändert die Darstellung, nicht die Modellanpassung oder die zugrunde liegenden angepassten Beziehungen.

### T07-A08-V08: Museumsroute neu referenzieren

**Vor dem Rechnen begründen, Teil (a)**

Die neue Referenz ist die alte Gruppe mit $G=1$. Ihr alter Achsenabschnitt wird daher zum neuen Achsenabschnitt: $b'_0=45.00+(6.50)=51.50$. Die gemeinsame Steigung bleibt $b'_1=4.20$. Der Kontrast kehrt seine Richtung um, somit gilt $b'_2=-(6.50)=-6.50$.

**Berechnung durchführen, Teil (b)**

Für die Gruppe „Zusammengestellte Route“ ist $H=0$, woraus $\hat Y=51.50+(4.20)X$ folgt. Für die Gruppe „Freie Route“ ist $H=1$, woraus $\hat Y=51.50+(4.20)X+(-6.50)=45.00+(4.20)X$ folgt. Beim selben $X$ liegt der angepasste Wert für „Freie Route“ um 6.50 Einheiten tiefer als für „Zusammengestellte Route“.

**Berechnung durchführen, Teil (c)**

Beide Codierungen ergeben:

| Gruppe | X | Anpassung aus alter Codierung | Anpassung aus neuer Codierung |
| --- | --- | --- | --- |
| Freie Route | 0.0 | 45.00 | 45.00 |
| Freie Route | 3.0 | 57.60 | 57.60 |
| Zusammengestellte Route | 0.0 | 51.50 | 51.50 |
| Zusammengestellte Route | 3.0 | 64.10 | 64.10 |

**Ergebnis interpretieren und prüfen, Teil (d)**

In jeder Zeile sind die angepassten Werte unter beiden Codierungen identisch. Das Wechseln der Referenz verändert, welche Gruppe der Achsenabschnitt darstellt, und kehrt den angezeigten Gruppenkontrast um. Es beschreibt jedoch dieselben zwei Linien. Weil jeder Fall denselben angepassten Wert behält, bleibt auch jedes Residuum unverändert, wenn der angepasste Wert von der beobachteten Ergebnisvariable subtrahiert wird. Die Referenzwahl verändert die Darstellung, nicht die Modellanpassung oder die zugrunde liegenden angepassten Beziehungen.

### T07-A08-V09: Überarbeitungstreffen neu referenzieren

**Vor dem Rechnen begründen, Teil (a)**

Die neue Referenz ist die alte Gruppe mit $G=1$. Ihr alter Achsenabschnitt wird daher zum neuen Achsenabschnitt: $b'_0=51.00+(2.50)=53.50$. Die gemeinsame Steigung bleibt $b'_1=3.40$. Der Kontrast kehrt seine Richtung um, somit gilt $b'_2=-(2.50)=-2.50$.

**Berechnung durchführen, Teil (b)**

Für die Gruppe „Live“ ist $H=0$, woraus $\hat Y=53.50+(3.40)X$ folgt. Für die Gruppe „Asynchron“ ist $H=1$, woraus $\hat Y=53.50+(3.40)X+(-2.50)=51.00+(3.40)X$ folgt. Beim selben $X$ liegt der angepasste Wert für „Asynchron“ um 2.50 Einheiten tiefer als für „Live“.

**Berechnung durchführen, Teil (c)**

Beide Codierungen ergeben:

| Gruppe | X | Anpassung aus alter Codierung | Anpassung aus neuer Codierung |
| --- | --- | --- | --- |
| Asynchron | 1.0 | 54.40 | 54.40 |
| Asynchron | 5.0 | 68.00 | 68.00 |
| Live | 1.0 | 56.90 | 56.90 |
| Live | 5.0 | 70.50 | 70.50 |

**Ergebnis interpretieren und prüfen, Teil (d)**

In jeder Zeile sind die angepassten Werte unter beiden Codierungen identisch. Das Wechseln der Referenz verändert, welche Gruppe der Achsenabschnitt darstellt, und kehrt den angezeigten Gruppenkontrast um. Es beschreibt jedoch dieselben zwei Linien. Weil jeder Fall denselben angepassten Wert behält, bleibt auch jedes Residuum unverändert, wenn der angepasste Wert von der beobachteten Ergebnisvariable subtrahiert wird. Die Referenzwahl verändert die Darstellung, nicht die Modellanpassung oder die zugrunde liegenden angepassten Beziehungen.

### T07-A08-V10: Planungswerkzeug neu referenzieren

**Vor dem Rechnen begründen, Teil (a)**

Die neue Referenz ist die alte Gruppe mit $G=1$. Ihr alter Achsenabschnitt wird daher zum neuen Achsenabschnitt: $b'_0=72.00+(-4.00)=68.00$. Die gemeinsame Steigung bleibt $b'_1=-2.50$. Der Kontrast kehrt seine Richtung um, somit gilt $b'_2=-(-4.00)=4.00$.

**Berechnung durchführen, Teil (b)**

Für die Gruppe „Kalender“ ist $H=0$, woraus $\hat Y=68.00+(-2.50)X$ folgt. Für die Gruppe „Notizbuch“ ist $H=1$, woraus $\hat Y=68.00+(-2.50)X+(4.00)=72.00+(-2.50)X$ folgt. Beim selben $X$ liegt der angepasste Wert für „Notizbuch“ um 4.00 Einheiten höher als für „Kalender“.

**Berechnung durchführen, Teil (c)**

Beide Codierungen ergeben:

| Gruppe | X | Anpassung aus alter Codierung | Anpassung aus neuer Codierung |
| --- | --- | --- | --- |
| Notizbuch | 1.0 | 69.50 | 69.50 |
| Notizbuch | 6.0 | 57.00 | 57.00 |
| Kalender | 1.0 | 65.50 | 65.50 |
| Kalender | 6.0 | 53.00 | 53.00 |

**Ergebnis interpretieren und prüfen, Teil (d)**

In jeder Zeile sind die angepassten Werte unter beiden Codierungen identisch. Das Wechseln der Referenz verändert, welche Gruppe der Achsenabschnitt darstellt, und kehrt den angezeigten Gruppenkontrast um. Es beschreibt jedoch dieselben zwei Linien. Weil jeder Fall denselben angepassten Wert behält, bleibt auch jedes Residuum unverändert, wenn der angepasste Wert von der beobachteten Ergebnisvariable subtrahiert wird. Die Referenzwahl verändert die Darstellung, nicht die Modellanpassung oder die zugrunde liegenden angepassten Beziehungen.

## A09: Eine Interaktion zwischen Gruppe und quantitativem Prädiktor interpretieren

### T07-A09-V01: Übungsstunden nach Lernbegleitung

**Vor dem Rechnen begründen, Teil (a)**

Wenn $G=0$ ist, ist das Produkt $XG$ für jedes $X$ null. Wenn $G=1$ ist, gilt $XG=X$.

**Berechnung durchführen, Teil (b)**

Einsetzen ergibt für die Gruppe „Ohne Lernbegleitung“: $\hat Y=40.00+(2.00)X$, mit der Steigung 2.00. Für die Gruppe „Mit Lernbegleitung“ ergibt sich: $\hat Y=44.00+(3.20)X$, mit der Steigung $b_1+b_3=2.00+(1.20)=3.20$.

**Berechnung durchführen, Teil (c)**

Die Produktterme und angepassten Koordinaten lauten:

| Gruppe | G | X | XG | Angepasster Wert der Ergebnisvariable „Punktwert im statistischen Denken“ |
| --- | --- | --- | --- | --- |
| Ohne Lernbegleitung | 0 | 1.0 | 0.0 | 42.00 |
| Ohne Lernbegleitung | 0 | 5.0 | 0.0 | 50.00 |
| Mit Lernbegleitung | 1 | 1.0 | 1.0 | 47.20 |
| Mit Lernbegleitung | 1 | 5.0 | 5.0 | 60.00 |

**Berechnung durchführen, Teil (d)**

Trage den Prädiktor „Übungsstunden“ auf der horizontalen Achse und den angepassten Wert der Ergebnisvariable „Punktwert im statistischen Denken“ auf der vertikalen Achse ab. Verbinde für die Gruppe „Ohne Lernbegleitung“ ihre beiden Koordinaten aus der Tabelle. Verbinde für die Gruppe „Mit Lernbegleitung“ ihre beiden Koordinaten zu einer zweiten beschrifteten Geraden. Zeichne bei $X=1.0$ und $X=5.0$ vertikale Strecken zwischen den Geraden und beschrifte ihre Längen mit 5.20 und 10.00. Die nicht parallelen Steigungen machen den sich verändernden Abstand sichtbar.

**Ergebnis interpretieren und prüfen, Teil (e)**

$b_1=2.00$ ist die Steigung des Prädiktors „Übungsstunden“ in der Referenzgruppe. $b_2=4.00$ ist die angepasste Differenz „Mit Lernbegleitung“ minus „Ohne Lernbegleitung“, und zwar genau bei $X=0$. Der Koeffizient bleibt dort interpretierbar, auch wenn null inhaltlich nicht zentral ist. $b_3=1.20$ ist die Differenz zwischen den beiden Gruppensteigungen. Der angepasste Gruppenabstand lautet daher $b_2+b_3X$: Er beträgt 5.20 bei $X=1.0$ und 10.00 bei $X=5.0$. Die Interaktion beschreibt, wie sich ein bedingter Zusammenhang zwischen Gruppen unterscheidet. Sie belegt nicht, dass die Gruppe oder $X$ die Ergebnisvariable verursacht.

### T07-A09-V02: Übungssitzungen nach Archivrolle

**Vor dem Rechnen begründen, Teil (a)**

Wenn $G=0$ ist, ist das Produkt $XG$ für jedes $X$ null. Wenn $G=1$ ist, gilt $XG=X$.

**Berechnung durchführen, Teil (b)**

Einsetzen ergibt für die Gruppe „Neue Mitarbeitende“: $\hat Y=38.00+(-1.20)X$, mit der Steigung -1.20. Für die Gruppe „Erfahrene Mitarbeitende“ ergibt sich: $\hat Y=35.00+(-2.00)X$, mit der Steigung $b_1+b_3=-1.20+(-0.80)=-2.00$.

**Berechnung durchführen, Teil (c)**

Die Produktterme und angepassten Koordinaten lauten:

| Gruppe | G | X | XG | Angepasster Wert der Ergebnisvariable „Suchzeit“ |
| --- | --- | --- | --- | --- |
| Neue Mitarbeitende | 0 | 0.0 | 0.0 | 38.00 |
| Neue Mitarbeitende | 0 | 4.0 | 0.0 | 33.20 |
| Erfahrene Mitarbeitende | 1 | 0.0 | 0.0 | 35.00 |
| Erfahrene Mitarbeitende | 1 | 4.0 | 4.0 | 27.00 |

**Berechnung durchführen, Teil (d)**

Trage den Prädiktor „Übungssitzungen“ auf der horizontalen Achse und den angepassten Wert der Ergebnisvariable „Suchzeit“ auf der vertikalen Achse ab. Verbinde für die Gruppe „Neue Mitarbeitende“ ihre beiden Koordinaten aus der Tabelle. Verbinde für die Gruppe „Erfahrene Mitarbeitende“ ihre beiden Koordinaten zu einer zweiten beschrifteten Geraden. Zeichne bei $X=0.0$ und $X=4.0$ vertikale Strecken zwischen den Geraden und beschrifte ihre Längen mit -3.00 und -6.20. Die nicht parallelen Steigungen machen den sich verändernden Abstand sichtbar.

**Ergebnis interpretieren und prüfen, Teil (e)**

$b_1=-1.20$ ist die Steigung des Prädiktors „Übungssitzungen“ in der Referenzgruppe. $b_2=-3.00$ ist die angepasste Differenz „Erfahrene Mitarbeitende“ minus „Neue Mitarbeitende“, und zwar genau bei $X=0$. Der Koeffizient bleibt dort interpretierbar, auch wenn null inhaltlich nicht zentral ist. $b_3=-0.80$ ist die Differenz zwischen den beiden Gruppensteigungen. Der angepasste Gruppenabstand lautet daher $b_2+b_3X$: Er beträgt -3.00 bei $X=0.0$ und -6.20 bei $X=4.0$. Die Interaktion beschreibt, wie sich ein bedingter Zusammenhang zwischen Gruppen unterscheidet. Sie belegt nicht, dass die Gruppe oder $X$ die Ergebnisvariable verursacht.

### T07-A09-V03: Lesestunden nach Medium

**Vor dem Rechnen begründen, Teil (a)**

Wenn $G=0$ ist, ist das Produkt $XG$ für jedes $X$ null. Wenn $G=1$ ist, gilt $XG=X$.

**Berechnung durchführen, Teil (b)**

Einsetzen ergibt für die Gruppe „Gedruckt“: $\hat Y=49.00+(2.60)X$, mit der Steigung 2.60. Für die Gruppe „Audio“ ergibt sich: $\hat Y=51.00+(1.60)X$, mit der Steigung $b_1+b_3=2.60+(-1.00)=1.60$.

**Berechnung durchführen, Teil (c)**

Die Produktterme und angepassten Koordinaten lauten:

| Gruppe | G | X | XG | Angepasster Wert der Ergebnisvariable „Punktwert im Textverständnis“ |
| --- | --- | --- | --- | --- |
| Gedruckt | 0 | 2.0 | 0.0 | 54.20 |
| Gedruckt | 0 | 6.0 | 0.0 | 64.60 |
| Audio | 1 | 2.0 | 2.0 | 54.20 |
| Audio | 1 | 6.0 | 6.0 | 60.60 |

**Berechnung durchführen, Teil (d)**

Trage den Prädiktor „Lesestunden“ auf der horizontalen Achse und den angepassten Wert der Ergebnisvariable „Punktwert im Textverständnis“ auf der vertikalen Achse ab. Verbinde für die Gruppe „Gedruckt“ ihre beiden Koordinaten aus der Tabelle. Verbinde für die Gruppe „Audio“ ihre beiden Koordinaten zu einer zweiten beschrifteten Geraden. Zeichne bei $X=2.0$ und $X=6.0$ vertikale Strecken zwischen den Geraden und beschrifte ihre Längen mit 0.00 und -4.00. Die nicht parallelen Steigungen machen den sich verändernden Abstand sichtbar.

**Ergebnis interpretieren und prüfen, Teil (e)**

$b_1=2.60$ ist die Steigung des Prädiktors „Lesestunden“ in der Referenzgruppe. $b_2=2.00$ ist die angepasste Differenz „Audio“ minus „Gedruckt“, und zwar genau bei $X=0$. Der Koeffizient bleibt dort interpretierbar, auch wenn null inhaltlich nicht zentral ist. $b_3=-1.00$ ist die Differenz zwischen den beiden Gruppensteigungen. Der angepasste Gruppenabstand lautet daher $b_2+b_3X$: Er beträgt 0.00 bei $X=2.0$ und -4.00 bei $X=6.0$. Die Interaktion beschreibt, wie sich ein bedingter Zusammenhang zwischen Gruppen unterscheidet. Sie belegt nicht, dass die Gruppe oder $X$ die Ergebnisvariable verursacht.

### T07-A09-V04: Streckenübung nach Navigationsanzeige

**Vor dem Rechnen begründen, Teil (a)**

Wenn $G=0$ ist, ist das Produkt $XG$ für jedes $X$ null. Wenn $G=1$ ist, gilt $XG=X$.

**Berechnung durchführen, Teil (b)**

Einsetzen ergibt für die Gruppe „Statisch“: $\hat Y=48.00+(-1.50)X$, mit der Steigung -1.50. Für die Gruppe „Interaktiv“ ergibt sich: $\hat Y=46.00+(-2.40)X$, mit der Steigung $b_1+b_3=-1.50+(-0.90)=-2.40$.

**Berechnung durchführen, Teil (c)**

Die Produktterme und angepassten Koordinaten lauten:

| Gruppe | G | X | XG | Angepasster Wert der Ergebnisvariable „Navigationszeit“ |
| --- | --- | --- | --- | --- |
| Statisch | 0 | 1.0 | 0.0 | 46.50 |
| Statisch | 0 | 5.0 | 0.0 | 40.50 |
| Interaktiv | 1 | 1.0 | 1.0 | 43.60 |
| Interaktiv | 1 | 5.0 | 5.0 | 34.00 |

**Berechnung durchführen, Teil (d)**

Trage den Prädiktor „Übungsversuche“ auf der horizontalen Achse und den angepassten Wert der Ergebnisvariable „Navigationszeit“ auf der vertikalen Achse ab. Verbinde für die Gruppe „Statisch“ ihre beiden Koordinaten aus der Tabelle. Verbinde für die Gruppe „Interaktiv“ ihre beiden Koordinaten zu einer zweiten beschrifteten Geraden. Zeichne bei $X=1.0$ und $X=5.0$ vertikale Strecken zwischen den Geraden und beschrifte ihre Längen mit -2.90 und -6.50. Die nicht parallelen Steigungen machen den sich verändernden Abstand sichtbar.

**Ergebnis interpretieren und prüfen, Teil (e)**

$b_1=-1.50$ ist die Steigung des Prädiktors „Übungsversuche“ in der Referenzgruppe. $b_2=-2.00$ ist die angepasste Differenz „Interaktiv“ minus „Statisch“, und zwar genau bei $X=0$. Der Koeffizient bleibt dort interpretierbar, auch wenn null inhaltlich nicht zentral ist. $b_3=-0.90$ ist die Differenz zwischen den beiden Gruppensteigungen. Der angepasste Gruppenabstand lautet daher $b_2+b_3X$: Er beträgt -2.90 bei $X=1.0$ und -6.50 bei $X=5.0$. Die Interaktion beschreibt, wie sich ein bedingter Zusammenhang zwischen Gruppen unterscheidet. Sie belegt nicht, dass die Gruppe oder $X$ die Ergebnisvariable verursacht.

### T07-A09-V05: Übungsblöcke nach Kataloghilfe

**Vor dem Rechnen begründen, Teil (a)**

Wenn $G=0$ ist, ist das Produkt $XG$ für jedes $X$ null. Wenn $G=1$ ist, gilt $XG=X$.

**Berechnung durchführen, Teil (b)**

Einsetzen ergibt für die Gruppe „Index“: $\hat Y=52.00+(2.00)X$, mit der Steigung 2.00. Für die Gruppe „Suchleiste“ ergibt sich: $\hat Y=55.00+(2.70)X$, mit der Steigung $b_1+b_3=2.00+(0.70)=2.70$.

**Berechnung durchführen, Teil (c)**

Die Produktterme und angepassten Koordinaten lauten:

| Gruppe | G | X | XG | Angepasster Wert der Ergebnisvariable „Punktwert der Genauigkeit“ |
| --- | --- | --- | --- | --- |
| Index | 0 | 0.0 | 0.0 | 52.00 |
| Index | 0 | 4.0 | 0.0 | 60.00 |
| Suchleiste | 1 | 0.0 | 0.0 | 55.00 |
| Suchleiste | 1 | 4.0 | 4.0 | 65.80 |

**Berechnung durchführen, Teil (d)**

Trage den Prädiktor „Übungsblöcke“ auf der horizontalen Achse und den angepassten Wert der Ergebnisvariable „Punktwert der Genauigkeit“ auf der vertikalen Achse ab. Verbinde für die Gruppe „Index“ ihre beiden Koordinaten aus der Tabelle. Verbinde für die Gruppe „Suchleiste“ ihre beiden Koordinaten zu einer zweiten beschrifteten Geraden. Zeichne bei $X=0.0$ und $X=4.0$ vertikale Strecken zwischen den Geraden und beschrifte ihre Längen mit 3.00 und 5.80. Die nicht parallelen Steigungen machen den sich verändernden Abstand sichtbar.

**Ergebnis interpretieren und prüfen, Teil (e)**

$b_1=2.00$ ist die Steigung des Prädiktors „Übungsblöcke“ in der Referenzgruppe. $b_2=3.00$ ist die angepasste Differenz „Suchleiste“ minus „Index“, und zwar genau bei $X=0$. Der Koeffizient bleibt dort interpretierbar, auch wenn null inhaltlich nicht zentral ist. $b_3=0.70$ ist die Differenz zwischen den beiden Gruppensteigungen. Der angepasste Gruppenabstand lautet daher $b_2+b_3X$: Er beträgt 3.00 bei $X=0.0$ und 5.80 bei $X=4.0$. Die Interaktion beschreibt, wie sich ein bedingter Zusammenhang zwischen Gruppen unterscheidet. Sie belegt nicht, dass die Gruppe oder $X$ die Ergebnisvariable verursacht.

### T07-A09-V06: Sitzungen nach Workshopumgebung

**Vor dem Rechnen begründen, Teil (a)**

Wenn $G=0$ ist, ist das Produkt $XG$ für jedes $X$ null. Wenn $G=1$ ist, gilt $XG=X$.

**Berechnung durchführen, Teil (b)**

Einsetzen ergibt für die Gruppe „Online“: $\hat Y=36.00+(2.40)X$, mit der Steigung 2.40. Für die Gruppe „Kursraum“ ergibt sich: $\hat Y=41.00+(3.20)X$, mit der Steigung $b_1+b_3=2.40+(0.80)=3.20$.

**Berechnung durchführen, Teil (c)**

Die Produktterme und angepassten Koordinaten lauten:

| Gruppe | G | X | XG | Angepasster Wert der Ergebnisvariable „Punktwert des Selbstvertrauens“ |
| --- | --- | --- | --- | --- |
| Online | 0 | 1.0 | 0.0 | 38.40 |
| Online | 0 | 5.0 | 0.0 | 48.00 |
| Kursraum | 1 | 1.0 | 1.0 | 44.20 |
| Kursraum | 1 | 5.0 | 5.0 | 57.00 |

**Berechnung durchführen, Teil (d)**

Trage den Prädiktor „Sitzungen“ auf der horizontalen Achse und den angepassten Wert der Ergebnisvariable „Punktwert des Selbstvertrauens“ auf der vertikalen Achse ab. Verbinde für die Gruppe „Online“ ihre beiden Koordinaten aus der Tabelle. Verbinde für die Gruppe „Kursraum“ ihre beiden Koordinaten zu einer zweiten beschrifteten Geraden. Zeichne bei $X=1.0$ und $X=5.0$ vertikale Strecken zwischen den Geraden und beschrifte ihre Längen mit 5.80 und 9.00. Die nicht parallelen Steigungen machen den sich verändernden Abstand sichtbar.

**Ergebnis interpretieren und prüfen, Teil (e)**

$b_1=2.40$ ist die Steigung des Prädiktors „Sitzungen“ in der Referenzgruppe. $b_2=5.00$ ist die angepasste Differenz „Kursraum“ minus „Online“, und zwar genau bei $X=0$. Der Koeffizient bleibt dort interpretierbar, auch wenn null inhaltlich nicht zentral ist. $b_3=0.80$ ist die Differenz zwischen den beiden Gruppensteigungen. Der angepasste Gruppenabstand lautet daher $b_2+b_3X$: Er beträgt 5.80 bei $X=1.0$ und 9.00 bei $X=5.0$. Die Interaktion beschreibt, wie sich ein bedingter Zusammenhang zwischen Gruppen unterscheidet. Sie belegt nicht, dass die Gruppe oder $X$ die Ergebnisvariable verursacht.

### T07-A09-V07: Konzentrationsblöcke nach Raumart

**Vor dem Rechnen begründen, Teil (a)**

Wenn $G=0$ ist, ist das Produkt $XG$ für jedes $X$ null. Wenn $G=1$ ist, gilt $XG=X$.

**Berechnung durchführen, Teil (b)**

Einsetzen ergibt für die Gruppe „Offener Raum“: $\hat Y=58.00+(2.10)X$, mit der Steigung 2.10. Für die Gruppe „Privater Raum“ ergibt sich: $\hat Y=62.00+(1.50)X$, mit der Steigung $b_1+b_3=2.10+(-0.60)=1.50$.

**Berechnung durchführen, Teil (c)**

Die Produktterme und angepassten Koordinaten lauten:

| Gruppe | G | X | XG | Angepasster Wert der Ergebnisvariable „Punktwert der Aufgabengenauigkeit“ |
| --- | --- | --- | --- | --- |
| Offener Raum | 0 | 2.0 | 0.0 | 62.20 |
| Offener Raum | 0 | 7.0 | 0.0 | 72.70 |
| Privater Raum | 1 | 2.0 | 2.0 | 65.00 |
| Privater Raum | 1 | 7.0 | 7.0 | 72.50 |

**Berechnung durchführen, Teil (d)**

Trage den Prädiktor „Konzentrationsblöcke“ auf der horizontalen Achse und den angepassten Wert der Ergebnisvariable „Punktwert der Aufgabengenauigkeit“ auf der vertikalen Achse ab. Verbinde für die Gruppe „Offener Raum“ ihre beiden Koordinaten aus der Tabelle. Verbinde für die Gruppe „Privater Raum“ ihre beiden Koordinaten zu einer zweiten beschrifteten Geraden. Zeichne bei $X=2.0$ und $X=7.0$ vertikale Strecken zwischen den Geraden und beschrifte ihre Längen mit 2.80 und -0.20. Die nicht parallelen Steigungen machen den sich verändernden Abstand sichtbar.

**Ergebnis interpretieren und prüfen, Teil (e)**

$b_1=2.10$ ist die Steigung des Prädiktors „Konzentrationsblöcke“ in der Referenzgruppe. $b_2=4.00$ ist die angepasste Differenz „Privater Raum“ minus „Offener Raum“, und zwar genau bei $X=0$. Der Koeffizient bleibt dort interpretierbar, auch wenn null inhaltlich nicht zentral ist. $b_3=-0.60$ ist die Differenz zwischen den beiden Gruppensteigungen. Der angepasste Gruppenabstand lautet daher $b_2+b_3X$: Er beträgt 2.80 bei $X=2.0$ und -0.20 bei $X=7.0$. Die Interaktion beschreibt, wie sich ein bedingter Zusammenhang zwischen Gruppen unterscheidet. Sie belegt nicht, dass die Gruppe oder $X$ die Ergebnisvariable verursacht.

### T07-A09-V08: Besuche nach Museumsroute

**Vor dem Rechnen begründen, Teil (a)**

Wenn $G=0$ ist, ist das Produkt $XG$ für jedes $X$ null. Wenn $G=1$ ist, gilt $XG=X$.

**Berechnung durchführen, Teil (b)**

Einsetzen ergibt für die Gruppe „Freie Route“: $\hat Y=44.00+(3.50)X$, mit der Steigung 3.50. Für die Gruppe „Zusammengestellte Route“ ergibt sich: $\hat Y=47.00+(5.00)X$, mit der Steigung $b_1+b_3=3.50+(1.50)=5.00$.

**Berechnung durchführen, Teil (c)**

Die Produktterme und angepassten Koordinaten lauten:

| Gruppe | G | X | XG | Angepasster Wert der Ergebnisvariable „Punktwert des Wissens“ |
| --- | --- | --- | --- | --- |
| Freie Route | 0 | 0.0 | 0.0 | 44.00 |
| Freie Route | 0 | 3.0 | 0.0 | 54.50 |
| Zusammengestellte Route | 1 | 0.0 | 0.0 | 47.00 |
| Zusammengestellte Route | 1 | 3.0 | 3.0 | 62.00 |

**Berechnung durchführen, Teil (d)**

Trage den Prädiktor „Besuche“ auf der horizontalen Achse und den angepassten Wert der Ergebnisvariable „Punktwert des Wissens“ auf der vertikalen Achse ab. Verbinde für die Gruppe „Freie Route“ ihre beiden Koordinaten aus der Tabelle. Verbinde für die Gruppe „Zusammengestellte Route“ ihre beiden Koordinaten zu einer zweiten beschrifteten Geraden. Zeichne bei $X=0.0$ und $X=3.0$ vertikale Strecken zwischen den Geraden und beschrifte ihre Längen mit 3.00 und 7.50. Die nicht parallelen Steigungen machen den sich verändernden Abstand sichtbar.

**Ergebnis interpretieren und prüfen, Teil (e)**

$b_1=3.50$ ist die Steigung des Prädiktors „Besuche“ in der Referenzgruppe. $b_2=3.00$ ist die angepasste Differenz „Zusammengestellte Route“ minus „Freie Route“, und zwar genau bei $X=0$. Der Koeffizient bleibt dort interpretierbar, auch wenn null inhaltlich nicht zentral ist. $b_3=1.50$ ist die Differenz zwischen den beiden Gruppensteigungen. Der angepasste Gruppenabstand lautet daher $b_2+b_3X$: Er beträgt 3.00 bei $X=0.0$ und 7.50 bei $X=3.0$. Die Interaktion beschreibt, wie sich ein bedingter Zusammenhang zwischen Gruppen unterscheidet. Sie belegt nicht, dass die Gruppe oder $X$ die Ergebnisvariable verursacht.

### T07-A09-V09: Feedbackrunden nach Sitzungsform

**Vor dem Rechnen begründen, Teil (a)**

Wenn $G=0$ ist, ist das Produkt $XG$ für jedes $X$ null. Wenn $G=1$ ist, gilt $XG=X$.

**Berechnung durchführen, Teil (b)**

Einsetzen ergibt für die Gruppe „Asynchron“: $\hat Y=50.00+(2.80)X$, mit der Steigung 2.80. Für die Gruppe „Live“ ergibt sich: $\hat Y=54.00+(2.30)X$, mit der Steigung $b_1+b_3=2.80+(-0.50)=2.30$.

**Berechnung durchführen, Teil (c)**

Die Produktterme und angepassten Koordinaten lauten:

| Gruppe | G | X | XG | Angepasster Wert der Ergebnisvariable „Punktwert der Überarbeitung“ |
| --- | --- | --- | --- | --- |
| Asynchron | 0 | 1.0 | 0.0 | 52.80 |
| Asynchron | 0 | 5.0 | 0.0 | 64.00 |
| Live | 1 | 1.0 | 1.0 | 56.30 |
| Live | 1 | 5.0 | 5.0 | 65.50 |

**Berechnung durchführen, Teil (d)**

Trage den Prädiktor „Feedbackrunden“ auf der horizontalen Achse und den angepassten Wert der Ergebnisvariable „Punktwert der Überarbeitung“ auf der vertikalen Achse ab. Verbinde für die Gruppe „Asynchron“ ihre beiden Koordinaten aus der Tabelle. Verbinde für die Gruppe „Live“ ihre beiden Koordinaten zu einer zweiten beschrifteten Geraden. Zeichne bei $X=1.0$ und $X=5.0$ vertikale Strecken zwischen den Geraden und beschrifte ihre Längen mit 3.50 und 1.50. Die nicht parallelen Steigungen machen den sich verändernden Abstand sichtbar.

**Ergebnis interpretieren und prüfen, Teil (e)**

$b_1=2.80$ ist die Steigung des Prädiktors „Feedbackrunden“ in der Referenzgruppe. $b_2=4.00$ ist die angepasste Differenz „Live“ minus „Asynchron“, und zwar genau bei $X=0$. Der Koeffizient bleibt dort interpretierbar, auch wenn null inhaltlich nicht zentral ist. $b_3=-0.50$ ist die Differenz zwischen den beiden Gruppensteigungen. Der angepasste Gruppenabstand lautet daher $b_2+b_3X$: Er beträgt 3.50 bei $X=1.0$ und 1.50 bei $X=5.0$. Die Interaktion beschreibt, wie sich ein bedingter Zusammenhang zwischen Gruppen unterscheidet. Sie belegt nicht, dass die Gruppe oder $X$ die Ergebnisvariable verursacht.

### T07-A09-V10: Planung nach Werkzeugart

**Vor dem Rechnen begründen, Teil (a)**

Wenn $G=0$ ist, ist das Produkt $XG$ für jedes $X$ null. Wenn $G=1$ ist, gilt $XG=X$.

**Berechnung durchführen, Teil (b)**

Einsetzen ergibt für die Gruppe „Notizbuch“: $\hat Y=74.00+(-1.80)X$, mit der Steigung -1.80. Für die Gruppe „Kalender“ ergibt sich: $\hat Y=72.00+(-2.70)X$, mit der Steigung $b_1+b_3=-1.80+(-0.90)=-2.70$.

**Berechnung durchführen, Teil (c)**

Die Produktterme und angepassten Koordinaten lauten:

| Gruppe | G | X | XG | Angepasster Wert der Ergebnisvariable „Bearbeitungszeit“ |
| --- | --- | --- | --- | --- |
| Notizbuch | 0 | 1.0 | 0.0 | 72.20 |
| Notizbuch | 0 | 6.0 | 0.0 | 63.20 |
| Kalender | 1 | 1.0 | 1.0 | 69.30 |
| Kalender | 1 | 6.0 | 6.0 | 55.80 |

**Berechnung durchführen, Teil (d)**

Trage den Prädiktor „Planungssitzungen“ auf der horizontalen Achse und den angepassten Wert der Ergebnisvariable „Bearbeitungszeit“ auf der vertikalen Achse ab. Verbinde für die Gruppe „Notizbuch“ ihre beiden Koordinaten aus der Tabelle. Verbinde für die Gruppe „Kalender“ ihre beiden Koordinaten zu einer zweiten beschrifteten Geraden. Zeichne bei $X=1.0$ und $X=6.0$ vertikale Strecken zwischen den Geraden und beschrifte ihre Längen mit -2.90 und -7.40. Die nicht parallelen Steigungen machen den sich verändernden Abstand sichtbar.

**Ergebnis interpretieren und prüfen, Teil (e)**

$b_1=-1.80$ ist die Steigung des Prädiktors „Planungssitzungen“ in der Referenzgruppe. $b_2=-2.00$ ist die angepasste Differenz „Kalender“ minus „Notizbuch“, und zwar genau bei $X=0$. Der Koeffizient bleibt dort interpretierbar, auch wenn null inhaltlich nicht zentral ist. $b_3=-0.90$ ist die Differenz zwischen den beiden Gruppensteigungen. Der angepasste Gruppenabstand lautet daher $b_2+b_3X$: Er beträgt -2.90 bei $X=1.0$ und -7.40 bei $X=6.0$. Die Interaktion beschreibt, wie sich ein bedingter Zusammenhang zwischen Gruppen unterscheidet. Sie belegt nicht, dass die Gruppe oder $X$ die Ergebnisvariable verursacht.
