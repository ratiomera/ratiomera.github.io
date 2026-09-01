---
title: "Übungsblatt"
subtitle: "Multiple Regression"
document-id: "topic-07-multiple-regression-exercises-de"
topic-id: "topic-07-multiple-regression"
topic-number: "07"
topic-slug: "multiple-regression"
document-type: "exercises"
locale: "de"
paired-document-id: "topic-07-multiple-regression-solutions-de"
---

Dieses Blatt enthält 90 Übungen in 9 Gruppen von Lernzielen. Bearbeite jede Übung, bevor du die passende vollständige Lösung anschaust. Zeige die relevante Formel oder Regel, die eingesetzten Werte, die Einheiten und eine Interpretation. Alle Kontexte, Werte, Daten und Softwareausgaben sind eigens erstelltes Lehrmaterial; sie sind keine empirischen Befunde.

# Teil I: Theorie

## A06: Dummy-Variablen bilden und die Referenzkategorie bestimmen

### T07-A06-V01: Tutorialformat

In einem konstruierten Modell hat der kategoriale Prädiktor „Tutorialformat“ $k=3$ Kategorien: Text, Video, Interaktiv. Verwende „Text“ als Referenzkategorie und behalte einen Achsenabschnitt bei. $D_1$ bis $D_2$ kennzeichnen die Nichtreferenzkategorien in der aufgeführten Reihenfolge. Das angepasste Modell für die Ergebnisvariable „Punktwert im statistischen Denken“ lautet $\hat Y=61.00 + 3.50D_1 + 6.00D_2$.

(a) Gib an, wie viele Dummy-Variablen benötigt werden, und erkläre weshalb. (b) Erstelle für jede Kategorie die vollständige Codierungstabelle mit Nullen und Einsen. (c) Bestimme die Referenzzeile, berechne den angepassten Wert jeder Kategorie und interpretiere den Koeffizienten von $D_1$ als Vergleich mit der Referenz. (d) Erkläre, weshalb eine eigene Dummy-Variable für alle $k$ Kategorien bei beibehaltenem Achsenabschnitt eine exakte Redundanz erzeugt. Beschreibe zudem, was sich bei einer anderen Referenz ändern und was gleich bleiben würde.

### T07-A06-V02: Lernort

In einem konstruierten Modell hat der kategoriale Prädiktor „Lernort“ $k=4$ Kategorien: Zu Hause, Bibliothek, Lernraum, Draussen. Verwende „Zu Hause“ als Referenzkategorie und behalte einen Achsenabschnitt bei. $D_1$ bis $D_3$ kennzeichnen die Nichtreferenzkategorien in der aufgeführten Reihenfolge. Das angepasste Modell für die Ergebnisvariable „Konzentrationswert“ lautet $\hat Y=54.00 + 4.00D_1 + 2.50D_2 - 1.50D_3$.

(a) Gib an, wie viele Dummy-Variablen benötigt werden, und erkläre weshalb. (b) Erstelle für jede Kategorie die vollständige Codierungstabelle mit Nullen und Einsen. (c) Bestimme die Referenzzeile, berechne den angepassten Wert jeder Kategorie und interpretiere den Koeffizienten von $D_1$ als Vergleich mit der Referenz. (d) Erkläre, weshalb eine eigene Dummy-Variable für alle $k$ Kategorien bei beibehaltenem Achsenabschnitt eine exakte Redundanz erzeugt. Beschreibe zudem, was sich bei einer anderen Referenz ändern und was gleich bleiben würde.

### T07-A06-V03: Feedbackkanal

In einem konstruierten Modell hat der kategoriale Prädiktor „Feedbackkanal“ $k=3$ Kategorien: Schriftlich, Audio, Video. Verwende „Schriftlich“ als Referenzkategorie und behalte einen Achsenabschnitt bei. $D_1$ bis $D_2$ kennzeichnen die Nichtreferenzkategorien in der aufgeführten Reihenfolge. Das angepasste Modell für die Ergebnisvariable „Punktwert der Überarbeitung“ lautet $\hat Y=66.00 + 2.00D_1 + 4.50D_2$.

(a) Gib an, wie viele Dummy-Variablen benötigt werden, und erkläre weshalb. (b) Erstelle für jede Kategorie die vollständige Codierungstabelle mit Nullen und Einsen. (c) Bestimme die Referenzzeile, berechne den angepassten Wert jeder Kategorie und interpretiere den Koeffizienten von $D_1$ als Vergleich mit der Referenz. (d) Erkläre, weshalb eine eigene Dummy-Variable für alle $k$ Kategorien bei beibehaltenem Achsenabschnitt eine exakte Redundanz erzeugt. Beschreibe zudem, was sich bei einer anderen Referenz ändern und was gleich bleiben würde.

### T07-A06-V04: Methode der Notizerfassung

In einem konstruierten Modell hat der kategoriale Prädiktor „Methode der Notizerfassung“ $k=4$ Kategorien: Papier, Tablet, Laptop, Gemischt. Verwende „Papier“ als Referenzkategorie und behalte einen Achsenabschnitt bei. $D_1$ bis $D_3$ kennzeichnen die Nichtreferenzkategorien in der aufgeführten Reihenfolge. Das angepasste Modell für die Ergebnisvariable „Erinnerungswert“ lautet $\hat Y=58.00 - 1.50D_1 - 2.50D_2 + 3.00D_3$.

(a) Gib an, wie viele Dummy-Variablen benötigt werden, und erkläre weshalb. (b) Erstelle für jede Kategorie die vollständige Codierungstabelle mit Nullen und Einsen. (c) Bestimme die Referenzzeile, berechne den angepassten Wert jeder Kategorie und interpretiere den Koeffizienten von $D_1$ als Vergleich mit der Referenz. (d) Erkläre, weshalb eine eigene Dummy-Variable für alle $k$ Kategorien bei beibehaltenem Achsenabschnitt eine exakte Redundanz erzeugt. Beschreibe zudem, was sich bei einer anderen Referenz ändern und was gleich bleiben würde.

### T07-A06-V05: Workshopzeit

In einem konstruierten Modell hat der kategoriale Prädiktor „Workshopzeit“ $k=3$ Kategorien: Morgen, Nachmittag, Abend. Verwende „Morgen“ als Referenzkategorie und behalte einen Achsenabschnitt bei. $D_1$ bis $D_2$ kennzeichnen die Nichtreferenzkategorien in der aufgeführten Reihenfolge. Das angepasste Modell für die Ergebnisvariable „Punktwert des Selbstvertrauens“ lautet $\hat Y=49.00 + 2.50D_1 - 3.00D_2$.

(a) Gib an, wie viele Dummy-Variablen benötigt werden, und erkläre weshalb. (b) Erstelle für jede Kategorie die vollständige Codierungstabelle mit Nullen und Einsen. (c) Bestimme die Referenzzeile, berechne den angepassten Wert jeder Kategorie und interpretiere den Koeffizienten von $D_1$ als Vergleich mit der Referenz. (d) Erkläre, weshalb eine eigene Dummy-Variable für alle $k$ Kategorien bei beibehaltenem Achsenabschnitt eine exakte Redundanz erzeugt. Beschreibe zudem, was sich bei einer anderen Referenz ändern und was gleich bleiben würde.

### T07-A06-V06: Archivhilfe

In einem konstruierten Modell hat der kategoriale Prädiktor „Archivhilfe“ $k=4$ Kategorien: Checkliste, Karte, Mentor, Suchwerkzeug. Verwende „Checkliste“ als Referenzkategorie und behalte einen Achsenabschnitt bei. $D_1$ bis $D_3$ kennzeichnen die Nichtreferenzkategorien in der aufgeführten Reihenfolge. Das angepasste Modell für die Ergebnisvariable „Punktwert der Suche“ lautet $\hat Y=63.00 + 1.50D_1 + 5.00D_2 + 3.00D_3$.

(a) Gib an, wie viele Dummy-Variablen benötigt werden, und erkläre weshalb. (b) Erstelle für jede Kategorie die vollständige Codierungstabelle mit Nullen und Einsen. (c) Bestimme die Referenzzeile, berechne den angepassten Wert jeder Kategorie und interpretiere den Koeffizienten von $D_1$ als Vergleich mit der Referenz. (d) Erkläre, weshalb eine eigene Dummy-Variable für alle $k$ Kategorien bei beibehaltenem Achsenabschnitt eine exakte Redundanz erzeugt. Beschreibe zudem, was sich bei einer anderen Referenz ändern und was gleich bleiben würde.

### T07-A06-V07: Überarbeitungsstrategie

In einem konstruierten Modell hat der kategoriale Prädiktor „Überarbeitungsstrategie“ $k=3$ Kategorien: Selbstkontrolle, Peer-Review, Beurteilung durch Lehrperson. Verwende „Selbstkontrolle“ als Referenzkategorie und behalte einen Achsenabschnitt bei. $D_1$ bis $D_2$ kennzeichnen die Nichtreferenzkategorien in der aufgeführten Reihenfolge. Das angepasste Modell für die Ergebnisvariable „Qualitätswert“ lautet $\hat Y=60.00 + 4.00D_1 + 7.00D_2$.

(a) Gib an, wie viele Dummy-Variablen benötigt werden, und erkläre weshalb. (b) Erstelle für jede Kategorie die vollständige Codierungstabelle mit Nullen und Einsen. (c) Bestimme die Referenzzeile, berechne den angepassten Wert jeder Kategorie und interpretiere den Koeffizienten von $D_1$ als Vergleich mit der Referenz. (d) Erkläre, weshalb eine eigene Dummy-Variable für alle $k$ Kategorien bei beibehaltenem Achsenabschnitt eine exakte Redundanz erzeugt. Beschreibe zudem, was sich bei einer anderen Referenz ändern und was gleich bleiben würde.

### T07-A06-V08: Museumsroute

In einem konstruierten Modell hat der kategoriale Prädiktor „Museumsroute“ $k=5$ Kategorien: Chronologisch, Thematisch, Freie Wahl, Geführt, Hybrid. Verwende „Chronologisch“ als Referenzkategorie und behalte einen Achsenabschnitt bei. $D_1$ bis $D_4$ kennzeichnen die Nichtreferenzkategorien in der aufgeführten Reihenfolge. Das angepasste Modell für die Ergebnisvariable „Punktwert des Wissens“ lautet $\hat Y=57.00 + 3.00D_1 - 1.00D_2 + 5.50D_3 + 4.00D_4$.

(a) Gib an, wie viele Dummy-Variablen benötigt werden, und erkläre weshalb. (b) Erstelle für jede Kategorie die vollständige Codierungstabelle mit Nullen und Einsen. (c) Bestimme die Referenzzeile, berechne den angepassten Wert jeder Kategorie und interpretiere den Koeffizienten von $D_1$ als Vergleich mit der Referenz. (d) Erkläre, weshalb eine eigene Dummy-Variable für alle $k$ Kategorien bei beibehaltenem Achsenabschnitt eine exakte Redundanz erzeugt. Beschreibe zudem, was sich bei einer anderen Referenz ändern und was gleich bleiben würde.

### T07-A06-V09: Lernplan

In einem konstruierten Modell hat der kategoriale Prädiktor „Lernplan“ $k=3$ Kategorien: Täglich, Zweimal wöchentlich, Wöchentlich. Verwende „Täglich“ als Referenzkategorie und behalte einen Achsenabschnitt bei. $D_1$ bis $D_2$ kennzeichnen die Nichtreferenzkategorien in der aufgeführten Reihenfolge. Das angepasste Modell für die Ergebnisvariable „Punktwert des Behaltens“ lautet $\hat Y=69.00 - 2.00D_1 - 5.00D_2$.

(a) Gib an, wie viele Dummy-Variablen benötigt werden, und erkläre weshalb. (b) Erstelle für jede Kategorie die vollständige Codierungstabelle mit Nullen und Einsen. (c) Bestimme die Referenzzeile, berechne den angepassten Wert jeder Kategorie und interpretiere den Koeffizienten von $D_1$ als Vergleich mit der Referenz. (d) Erkläre, weshalb eine eigene Dummy-Variable für alle $k$ Kategorien bei beibehaltenem Achsenabschnitt eine exakte Redundanz erzeugt. Beschreibe zudem, was sich bei einer anderen Referenz ändern und was gleich bleiben würde.

### T07-A06-V10: Aufgabenoberfläche

In einem konstruierten Modell hat der kategoriale Prädiktor „Aufgabenoberfläche“ $k=4$ Kategorien: Liste, Tafel, Kalender, Zeitachse. Verwende „Liste“ als Referenzkategorie und behalte einen Achsenabschnitt bei. $D_1$ bis $D_3$ kennzeichnen die Nichtreferenzkategorien in der aufgeführten Reihenfolge. Das angepasste Modell für die Ergebnisvariable „Punktwert des Abschlusses“ lautet $\hat Y=62.00 + 2.50D_1 + 4.00D_2 + 1.00D_3$.

(a) Gib an, wie viele Dummy-Variablen benötigt werden, und erkläre weshalb. (b) Erstelle für jede Kategorie die vollständige Codierungstabelle mit Nullen und Einsen. (c) Bestimme die Referenzzeile, berechne den angepassten Wert jeder Kategorie und interpretiere den Koeffizienten von $D_1$ als Vergleich mit der Referenz. (d) Erkläre, weshalb eine eigene Dummy-Variable für alle $k$ Kategorien bei beibehaltenem Achsenabschnitt eine exakte Redundanz erzeugt. Beschreibe zudem, was sich bei einer anderen Referenz ändern und was gleich bleiben würde.

# Teil II: Rechnerpraxis

## A01: Eine Gleichung und Ausgabe der multiplen Regression lesen

### T07-A01-V01: Begleitete Übung und statistisches Denken

**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel oder das erwartete Muster, das die Berechnung begründet.

Eine konstruierte Studie umfasst 80 Fälle. Die Ergebnisvariable $Y$ trägt die Bezeichnung „Punktwert im statistischen Denken“; die zugehörige Einheit lautet „Punkte“. $X_1$ ist der Prädiktor „Stunden begleiteter Übung“ und $X_2$ ist der Prädiktor „Punktwert der vorherigen Vorbereitung“. Der angepasste Achsenabschnitt beträgt 38.000. Die ausgewählte Ausgabe lautet:

| Term | Schätzwert | SE | Standardisiert | Bivariates r |
| --- | --- | --- | --- | --- |
| $X_1$ | 2.400 | 0.580 | 0.419 | 0.550 |
| $X_2$ | 0.310 | 0.108 | 0.292 | 0.480 |

Das Modell berichtet $R^2=0.370$, korrigiertes $R^2=0.354$, Residualstandardfehler $=5.60$ Punkte und residuale Freiheitsgrade von $df=77$.

(a) Schreibe die angepasste Gleichung auf und erkläre, wie sich ein unstandardisierter Schätzwert von einem standardisierten Koeffizienten unterscheidet. (b) Interpretiere beide unstandardisierten Steigungen bedingt. Verwende dabei die Ergebniseinheit und die Formulierung "während der andere Prädiktor festgehalten wird". (c) Berechne jede $t$-Statistik als Schätzwert geteilt durch ihren Standardfehler, bestimme die zweiseitigen $p$-Werte und entscheide bei $\alpha=.05$. (d) Interpretiere $R^2$, korrigiertes $R^2$ und den Residualstandardfehler. Erkläre danach, weshalb jeder standardisierte Koeffizient der multiplen Regression von seiner bivariaten Korrelation abweichen kann.

### T07-A01-V02: Arbeitsablauf im Archiv und Suchzeit

**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel oder das erwartete Muster, das die Berechnung begründet.

Eine konstruierte Studie umfasst 72 Fälle. Die Ergebnisvariable $Y$ trägt die Bezeichnung „Suchzeit“; die zugehörige Einheit lautet „Minuten“. $X_1$ ist der Prädiktor „Übungssitzungen mit Checkliste“ und $X_2$ ist der Prädiktor „Monate Archiverfahrung“. Der angepasste Achsenabschnitt beträgt 70.000. Die ausgewählte Ausgabe lautet:

| Term | Schätzwert | SE | Standardisiert | Bivariates r |
| --- | --- | --- | --- | --- |
| $X_1$ | -1.750 | 0.467 | -0.407 | -0.510 |
| $X_2$ | -0.220 | 0.093 | -0.257 | -0.420 |

Das Modell berichtet $R^2=0.316$, korrigiertes $R^2=0.296$, Residualstandardfehler $=4.80$ Minuten und residuale Freiheitsgrade von $df=69$.

(a) Schreibe die angepasste Gleichung auf und erkläre, wie sich ein unstandardisierter Schätzwert von einem standardisierten Koeffizienten unterscheidet. (b) Interpretiere beide unstandardisierten Steigungen bedingt. Verwende dabei die Ergebniseinheit und die Formulierung "während der andere Prädiktor festgehalten wird". (c) Berechne jede $t$-Statistik als Schätzwert geteilt durch ihren Standardfehler, bestimme die zweiseitigen $p$-Werte und entscheide bei $\alpha=.05$. (d) Interpretiere $R^2$, korrigiertes $R^2$ und den Residualstandardfehler. Erkläre danach, weshalb jeder standardisierte Koeffizient der multiplen Regression von seiner bivariaten Korrelation abweichen kann.

### T07-A01-V03: Leseroutinen und Textverständnis

**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel oder das erwartete Muster, das die Berechnung begründet.

Eine konstruierte Studie umfasst 95 Fälle. Die Ergebnisvariable $Y$ trägt die Bezeichnung „Punktwert im Textverständnis“; die zugehörige Einheit lautet „Punkte“. $X_1$ ist der Prädiktor „wöchentliche Lesestunden“ und $X_2$ ist der Prädiktor „Ausgangswert des Wortschatzes“. Der angepasste Achsenabschnitt beträgt 42.000. Die ausgewählte Ausgabe lautet:

| Term | Schätzwert | SE | Standardisiert | Bivariates r |
| --- | --- | --- | --- | --- |
| $X_1$ | 1.850 | 0.443 | 0.383 | 0.490 |
| $X_2$ | 0.280 | 0.084 | 0.306 | 0.440 |

Das Modell berichtet $R^2=0.322$, korrigiertes $R^2=0.308$, Residualstandardfehler $=5.10$ Punkte und residuale Freiheitsgrade von $df=92$.

(a) Schreibe die angepasste Gleichung auf und erkläre, wie sich ein unstandardisierter Schätzwert von einem standardisierten Koeffizienten unterscheidet. (b) Interpretiere beide unstandardisierten Steigungen bedingt. Verwende dabei die Ergebniseinheit und die Formulierung "während der andere Prädiktor festgehalten wird". (c) Berechne jede $t$-Statistik als Schätzwert geteilt durch ihren Standardfehler, bestimme die zweiseitigen $p$-Werte und entscheide bei $\alpha=.05$. (d) Interpretiere $R^2$, korrigiertes $R^2$ und den Residualstandardfehler. Erkläre danach, weshalb jeder standardisierte Koeffizient der multiplen Regression von seiner bivariaten Korrelation abweichen kann.

### T07-A01-V04: Streckenübung und Navigationszeit

**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel oder das erwartete Muster, das die Berechnung begründet.

Eine konstruierte Studie umfasst 68 Fälle. Die Ergebnisvariable $Y$ trägt die Bezeichnung „Navigationszeit“; die zugehörige Einheit lautet „Minuten“. $X_1$ ist der Prädiktor „Versuche zur Streckenübung“ und $X_2$ ist der Prädiktor „Punktwert der Streckenkenntnis“. Der angepasste Achsenabschnitt beträgt 65.000. Die ausgewählte Ausgabe lautet:

| Term | Schätzwert | SE | Standardisiert | Bivariates r |
| --- | --- | --- | --- | --- |
| $X_1$ | -2.100 | 0.519 | -0.446 | -0.530 |
| $X_2$ | -0.160 | 0.080 | -0.220 | -0.390 |

Das Modell berichtet $R^2=0.322$, korrigiertes $R^2=0.302$, Residualstandardfehler $=6.00$ Minuten und residuale Freiheitsgrade von $df=65$.

(a) Schreibe die angepasste Gleichung auf und erkläre, wie sich ein unstandardisierter Schätzwert von einem standardisierten Koeffizienten unterscheidet. (b) Interpretiere beide unstandardisierten Steigungen bedingt. Verwende dabei die Ergebniseinheit und die Formulierung "während der andere Prädiktor festgehalten wird". (c) Berechne jede $t$-Statistik als Schätzwert geteilt durch ihren Standardfehler, bestimme die zweiseitigen $p$-Werte und entscheide bei $\alpha=.05$. (d) Interpretiere $R^2$, korrigiertes $R^2$ und den Residualstandardfehler. Erkläre danach, weshalb jeder standardisierte Koeffizient der multiplen Regression von seiner bivariaten Korrelation abweichen kann.

### T07-A01-V05: Suchübung und Kataloggenauigkeit

**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel oder das erwartete Muster, das die Berechnung begründet.

Eine konstruierte Studie umfasst 110 Fälle. Die Ergebnisvariable $Y$ trägt die Bezeichnung „Punktwert der Kataloggenauigkeit“; die zugehörige Einheit lautet „Punkte“. $X_1$ ist der Prädiktor „Suchübungsblöcke“ und $X_2$ ist der Prädiktor „Punktwert des Katalogvorwissens“. Der angepasste Achsenabschnitt beträgt 48.000. Die ausgewählte Ausgabe lautet:

| Term | Schätzwert | SE | Standardisiert | Bivariates r |
| --- | --- | --- | --- | --- |
| $X_1$ | 1.550 | 0.413 | 0.339 | 0.460 |
| $X_2$ | 0.340 | 0.107 | 0.288 | 0.430 |

Das Modell berichtet $R^2=0.280$, korrigiertes $R^2=0.266$, Residualstandardfehler $=4.60$ Punkte und residuale Freiheitsgrade von $df=107$.

(a) Schreibe die angepasste Gleichung auf und erkläre, wie sich ein unstandardisierter Schätzwert von einem standardisierten Koeffizienten unterscheidet. (b) Interpretiere beide unstandardisierten Steigungen bedingt. Verwende dabei die Ergebniseinheit und die Formulierung "während der andere Prädiktor festgehalten wird". (c) Berechne jede $t$-Statistik als Schätzwert geteilt durch ihren Standardfehler, bestimme die zweiseitigen $p$-Werte und entscheide bei $\alpha=.05$. (d) Interpretiere $R^2$, korrigiertes $R^2$ und den Residualstandardfehler. Erkläre danach, weshalb jeder standardisierte Koeffizient der multiplen Regression von seiner bivariaten Korrelation abweichen kann.

### T07-A01-V06: Workshopteilnahme und Selbstvertrauen

**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel oder das erwartete Muster, das die Berechnung begründet.

Eine konstruierte Studie umfasst 76 Fälle. Die Ergebnisvariable $Y$ trägt die Bezeichnung „Punktwert des Selbstvertrauens“; die zugehörige Einheit lautet „Punkte“. $X_1$ ist der Prädiktor „Workshopsitzungen“ und $X_2$ ist der Prädiktor „Ausgangswert des Selbstvertrauens“. Der angepasste Achsenabschnitt beträgt 30.000. Die ausgewählte Ausgabe lautet:

| Term | Schätzwert | SE | Standardisiert | Bivariates r |
| --- | --- | --- | --- | --- |
| $X_1$ | 2.200 | 0.546 | 0.395 | 0.500 |
| $X_2$ | 0.450 | 0.125 | 0.352 | 0.470 |

Das Modell berichtet $R^2=0.363$, korrigiertes $R^2=0.345$, Residualstandardfehler $=5.00$ Punkte und residuale Freiheitsgrade von $df=73$.

(a) Schreibe die angepasste Gleichung auf und erkläre, wie sich ein unstandardisierter Schätzwert von einem standardisierten Koeffizienten unterscheidet. (b) Interpretiere beide unstandardisierten Steigungen bedingt. Verwende dabei die Ergebniseinheit und die Formulierung "während der andere Prädiktor festgehalten wird". (c) Berechne jede $t$-Statistik als Schätzwert geteilt durch ihren Standardfehler, bestimme die zweiseitigen $p$-Werte und entscheide bei $\alpha=.05$. (d) Interpretiere $R^2$, korrigiertes $R^2$ und den Residualstandardfehler. Erkläre danach, weshalb jeder standardisierte Koeffizient der multiplen Regression von seiner bivariaten Korrelation abweichen kann.

### T07-A01-V07: Konzentrationsblöcke und Aufgabengenauigkeit

**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel oder das erwartete Muster, das die Berechnung begründet.

Eine konstruierte Studie umfasst 120 Fälle. Die Ergebnisvariable $Y$ trägt die Bezeichnung „Punktwert der Aufgabengenauigkeit“; die zugehörige Einheit lautet „Punkte“. $X_1$ ist der Prädiktor „benachrichtigungsfreie Blöcke“ und $X_2$ ist der Prädiktor „Schlafdauer in Stunden“. Der angepasste Achsenabschnitt beträgt 55.000. Die ausgewählte Ausgabe lautet:

| Term | Schätzwert | SE | Standardisiert | Bivariates r |
| --- | --- | --- | --- | --- |
| $X_1$ | 1.300 | 0.330 | 0.329 | 0.410 |
| $X_2$ | 1.150 | 0.335 | 0.288 | 0.380 |

Das Modell berichtet $R^2=0.244$, korrigiertes $R^2=0.231$, Residualstandardfehler $=4.30$ Punkte und residuale Freiheitsgrade von $df=117$.

(a) Schreibe die angepasste Gleichung auf und erkläre, wie sich ein unstandardisierter Schätzwert von einem standardisierten Koeffizienten unterscheidet. (b) Interpretiere beide unstandardisierten Steigungen bedingt. Verwende dabei die Ergebniseinheit und die Formulierung "während der andere Prädiktor festgehalten wird". (c) Berechne jede $t$-Statistik als Schätzwert geteilt durch ihren Standardfehler, bestimme die zweiseitigen $p$-Werte und entscheide bei $\alpha=.05$. (d) Interpretiere $R^2$, korrigiertes $R^2$ und den Residualstandardfehler. Erkläre danach, weshalb jeder standardisierte Koeffizient der multiplen Regression von seiner bivariaten Korrelation abweichen kann.

### T07-A01-V08: Museumsbesuche und historisches Wissen

**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel oder das erwartete Muster, das die Berechnung begründet.

Eine konstruierte Studie umfasst 84 Fälle. Die Ergebnisvariable $Y$ trägt die Bezeichnung „Punktwert des historischen Wissens“; die zugehörige Einheit lautet „Punkte“. $X_1$ ist der Prädiktor „Museumsbesuche“ und $X_2$ ist der Prädiktor „Punktwert des geschichtlichen Vorwissens“. Der angepasste Achsenabschnitt beträgt 40.000. Die ausgewählte Ausgabe lautet:

| Term | Schätzwert | SE | Standardisiert | Bivariates r |
| --- | --- | --- | --- | --- |
| $X_1$ | 2.650 | 0.619 | 0.411 | 0.520 |
| $X_2$ | 0.370 | 0.118 | 0.302 | 0.450 |

Das Modell berichtet $R^2=0.350$, korrigiertes $R^2=0.334$, Residualstandardfehler $=5.50$ Punkte und residuale Freiheitsgrade von $df=81$.

(a) Schreibe die angepasste Gleichung auf und erkläre, wie sich ein unstandardisierter Schätzwert von einem standardisierten Koeffizienten unterscheidet. (b) Interpretiere beide unstandardisierten Steigungen bedingt. Verwende dabei die Ergebniseinheit und die Formulierung "während der andere Prädiktor festgehalten wird". (c) Berechne jede $t$-Statistik als Schätzwert geteilt durch ihren Standardfehler, bestimme die zweiseitigen $p$-Werte und entscheide bei $\alpha=.05$. (d) Interpretiere $R^2$, korrigiertes $R^2$ und den Residualstandardfehler. Erkläre danach, weshalb jeder standardisierte Koeffizient der multiplen Regression von seiner bivariaten Korrelation abweichen kann.

### T07-A01-V09: Peer-Feedback und Überarbeitungsqualität

**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel oder das erwartete Muster, das die Berechnung begründet.

Eine konstruierte Studie umfasst 92 Fälle. Die Ergebnisvariable $Y$ trägt die Bezeichnung „Punktwert der Überarbeitungsqualität“; die zugehörige Einheit lautet „Punkte“. $X_1$ ist der Prädiktor „Runden mit Peer-Feedback“ und $X_2$ ist der Prädiktor „Ausgangswert der Schreibqualität“. Der angepasste Achsenabschnitt beträgt 44.000. Die ausgewählte Ausgabe lautet:

| Term | Schätzwert | SE | Standardisiert | Bivariates r |
| --- | --- | --- | --- | --- |
| $X_1$ | 2.100 | 0.507 | 0.391 | 0.480 |
| $X_2$ | 0.300 | 0.104 | 0.271 | 0.400 |

Das Modell berichtet $R^2=0.296$, korrigiertes $R^2=0.280$, Residualstandardfehler $=4.90$ Punkte und residuale Freiheitsgrade von $df=89$.

(a) Schreibe die angepasste Gleichung auf und erkläre, wie sich ein unstandardisierter Schätzwert von einem standardisierten Koeffizienten unterscheidet. (b) Interpretiere beide unstandardisierten Steigungen bedingt. Verwende dabei die Ergebniseinheit und die Formulierung "während der andere Prädiktor festgehalten wird". (c) Berechne jede $t$-Statistik als Schätzwert geteilt durch ihren Standardfehler, bestimme die zweiseitigen $p$-Werte und entscheide bei $\alpha=.05$. (d) Interpretiere $R^2$, korrigiertes $R^2$ und den Residualstandardfehler. Erkläre danach, weshalb jeder standardisierte Koeffizient der multiplen Regression von seiner bivariaten Korrelation abweichen kann.

### T07-A01-V10: Planungssitzungen und Bearbeitungszeit

**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel oder das erwartete Muster, das die Berechnung begründet.

Eine konstruierte Studie umfasst 88 Fälle. Die Ergebnisvariable $Y$ trägt die Bezeichnung „Bearbeitungszeit“; die zugehörige Einheit lautet „Minuten“. $X_1$ ist der Prädiktor „Planungssitzungen“ und $X_2$ ist der Prädiktor „Punktwert der Aufgabenkomplexität“. Der angepasste Achsenabschnitt beträgt 82.000. Die ausgewählte Ausgabe lautet:

| Term | Schätzwert | SE | Standardisiert | Bivariates r |
| --- | --- | --- | --- | --- |
| $X_1$ | -1.900 | 0.384 | -0.430 | -0.450 |
| $X_2$ | 0.850 | 0.185 | 0.398 | 0.420 |

Das Modell berichtet $R^2=0.361$, korrigiertes $R^2=0.346$, Residualstandardfehler $=5.70$ Minuten und residuale Freiheitsgrade von $df=85$.

(a) Schreibe die angepasste Gleichung auf und erkläre, wie sich ein unstandardisierter Schätzwert von einem standardisierten Koeffizienten unterscheidet. (b) Interpretiere beide unstandardisierten Steigungen bedingt. Verwende dabei die Ergebniseinheit und die Formulierung "während der andere Prädiktor festgehalten wird". (c) Berechne jede $t$-Statistik als Schätzwert geteilt durch ihren Standardfehler, bestimme die zweiseitigen $p$-Werte und entscheide bei $\alpha=.05$. (d) Interpretiere $R^2$, korrigiertes $R^2$ und den Residualstandardfehler. Erkläre danach, weshalb jeder standardisierte Koeffizient der multiplen Regression von seiner bivariaten Korrelation abweichen kann.

## A02: Eine vorab festgelegte Folge verschachtelter Modelle vergleichen

### T07-A02-V01: Begleitete Übung und statistisches Denken

**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel oder das erwartete Muster, das die Berechnung begründet.

Drei konstruierte Modelle, die mit der gewöhnlichen Methode der kleinsten Quadrate angepasst wurden, verwenden dieselben $n=70$ Fälle, dieselbe Ergebnisvariable „Punktwert im statistischen Denken“ und einen Achsenabschnitt. Jedes spätere Modell enthält alle Terme des vorherigen Modells. Die gemeinsame totale Quadratsumme ist $SST=1840.0$ und $p$ bezeichnet die Anzahl der Prädiktorkoeffizienten.

| Modell | Prädiktorensatz | p | R-Quadrat |
| --- | --- | --- | --- |
| M1 | Stunden begleiteter Übung | 1 | 0.220 |
| M2 | Stunden begleiteter Übung; Punktwert der vorherigen Vorbereitung | 2 | 0.370 |
| M3 | Stunden begleiteter Übung; Punktwert der vorherigen Vorbereitung; Zahl der Reflexionssitzungen | 3 | 0.390 |

(a) Berechne für jedes Modell die Residuenquadratsumme $SSE=SST(1-R^2)$ und nach M1 bei jedem Schritt die Veränderung in $R^2$. (b) Berechne für alle drei Modelle das korrigierte $R^2=1-(1-R^2)(n-1)/(n-p-1)$. (c) Beschreibe, was das gewöhnliche und das korrigierte $R^2$ über das Hinzufügen des Prädiktors „Zahl der Reflexionssitzungen“ aussagen. (d) Behandle M2 als eingeschränktes und M3 als uneingeschränktes Modell. Schreibe beide Modellgleichungen auf, formuliere die Nullhypothese für den hinzugefügten Koeffizienten und berechne den inkrementellen Test $F=[(R_U^2-R_R^2)/1]/[(1-R_U^2)/(n-3-1)]$ mit 1 und 66 Freiheitsgraden. Bestimme den p-Wert und interpretiere die Entscheidung. (e) Erkläre, weshalb dies eine gültige verschachtelte Folge ist und weshalb weder die Anpassungstabelle noch der inkrementelle Test Kausalität oder Leistung an neuen Daten belegen.

### T07-A02-V02: Arbeitsablauf im Archiv und Suchzeit

**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel oder das erwartete Muster, das die Berechnung begründet.

Drei konstruierte Modelle, die mit der gewöhnlichen Methode der kleinsten Quadrate angepasst wurden, verwenden dieselben $n=80$ Fälle, dieselbe Ergebnisvariable „Suchzeit“ und einen Achsenabschnitt. Jedes spätere Modell enthält alle Terme des vorherigen Modells. Die gemeinsame totale Quadratsumme ist $SST=1320.0$ und $p$ bezeichnet die Anzahl der Prädiktorkoeffizienten.

| Modell | Prädiktorensatz | p | R-Quadrat |
| --- | --- | --- | --- |
| M1 | Übungssitzungen mit Checkliste | 1 | 0.280 |
| M2 | Übungssitzungen mit Checkliste; Monate Archiverfahrung | 2 | 0.350 |
| M3 | Übungssitzungen mit Checkliste; Monate Archiverfahrung; Punktwert zur Katalogvertrautheit | 3 | 0.351 |

(a) Berechne für jedes Modell die Residuenquadratsumme $SSE=SST(1-R^2)$ und nach M1 bei jedem Schritt die Veränderung in $R^2$. (b) Berechne für alle drei Modelle das korrigierte $R^2=1-(1-R^2)(n-1)/(n-p-1)$. (c) Beschreibe, was das gewöhnliche und das korrigierte $R^2$ über das Hinzufügen des Prädiktors „Punktwert zur Katalogvertrautheit“ aussagen. (d) Behandle M2 als eingeschränktes und M3 als uneingeschränktes Modell. Schreibe beide Modellgleichungen auf, formuliere die Nullhypothese für den hinzugefügten Koeffizienten und berechne den inkrementellen Test $F=[(R_U^2-R_R^2)/1]/[(1-R_U^2)/(n-3-1)]$ mit 1 und 76 Freiheitsgraden. Bestimme den p-Wert und interpretiere die Entscheidung. (e) Erkläre, weshalb dies eine gültige verschachtelte Folge ist und weshalb weder die Anpassungstabelle noch der inkrementelle Test Kausalität oder Leistung an neuen Daten belegen.

### T07-A02-V03: Leseroutinen und Textverständnis

**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel oder das erwartete Muster, das die Berechnung begründet.

Drei konstruierte Modelle, die mit der gewöhnlichen Methode der kleinsten Quadrate angepasst wurden, verwenden dieselben $n=60$ Fälle, dieselbe Ergebnisvariable „Punktwert im Textverständnis“ und einen Achsenabschnitt. Jedes spätere Modell enthält alle Terme des vorherigen Modells. Die gemeinsame totale Quadratsumme ist $SST=1560.0$ und $p$ bezeichnet die Anzahl der Prädiktorkoeffizienten.

| Modell | Prädiktorensatz | p | R-Quadrat |
| --- | --- | --- | --- |
| M1 | wöchentliche Lesestunden | 1 | 0.180 |
| M2 | wöchentliche Lesestunden; Ausgangswert des Wortschatzes | 2 | 0.310 |
| M3 | wöchentliche Lesestunden; Ausgangswert des Wortschatzes; Zahl der Annotationssitzungen | 3 | 0.360 |

(a) Berechne für jedes Modell die Residuenquadratsumme $SSE=SST(1-R^2)$ und nach M1 bei jedem Schritt die Veränderung in $R^2$. (b) Berechne für alle drei Modelle das korrigierte $R^2=1-(1-R^2)(n-1)/(n-p-1)$. (c) Beschreibe, was das gewöhnliche und das korrigierte $R^2$ über das Hinzufügen des Prädiktors „Zahl der Annotationssitzungen“ aussagen. (d) Behandle M2 als eingeschränktes und M3 als uneingeschränktes Modell. Schreibe beide Modellgleichungen auf, formuliere die Nullhypothese für den hinzugefügten Koeffizienten und berechne den inkrementellen Test $F=[(R_U^2-R_R^2)/1]/[(1-R_U^2)/(n-3-1)]$ mit 1 und 56 Freiheitsgraden. Bestimme den p-Wert und interpretiere die Entscheidung. (e) Erkläre, weshalb dies eine gültige verschachtelte Folge ist und weshalb weder die Anpassungstabelle noch der inkrementelle Test Kausalität oder Leistung an neuen Daten belegen.

### T07-A02-V04: Streckenübung und Navigationszeit

**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel oder das erwartete Muster, das die Berechnung begründet.

Drei konstruierte Modelle, die mit der gewöhnlichen Methode der kleinsten Quadrate angepasst wurden, verwenden dieselben $n=90$ Fälle, dieselbe Ergebnisvariable „Navigationszeit“ und einen Achsenabschnitt. Jedes spätere Modell enthält alle Terme des vorherigen Modells. Die gemeinsame totale Quadratsumme ist $SST=2100.0$ und $p$ bezeichnet die Anzahl der Prädiktorkoeffizienten.

| Modell | Prädiktorensatz | p | R-Quadrat |
| --- | --- | --- | --- |
| M1 | Versuche zur Streckenübung | 1 | 0.250 |
| M2 | Versuche zur Streckenübung; Punktwert der Streckenkenntnis | 2 | 0.330 |
| M3 | Versuche zur Streckenübung; Punktwert der Streckenkenntnis; Punktwert zur Erinnerung an Orientierungspunkte | 3 | 0.334 |

(a) Berechne für jedes Modell die Residuenquadratsumme $SSE=SST(1-R^2)$ und nach M1 bei jedem Schritt die Veränderung in $R^2$. (b) Berechne für alle drei Modelle das korrigierte $R^2=1-(1-R^2)(n-1)/(n-p-1)$. (c) Beschreibe, was das gewöhnliche und das korrigierte $R^2$ über das Hinzufügen des Prädiktors „Punktwert zur Erinnerung an Orientierungspunkte“ aussagen. (d) Behandle M2 als eingeschränktes und M3 als uneingeschränktes Modell. Schreibe beide Modellgleichungen auf, formuliere die Nullhypothese für den hinzugefügten Koeffizienten und berechne den inkrementellen Test $F=[(R_U^2-R_R^2)/1]/[(1-R_U^2)/(n-3-1)]$ mit 1 und 86 Freiheitsgraden. Bestimme den p-Wert und interpretiere die Entscheidung. (e) Erkläre, weshalb dies eine gültige verschachtelte Folge ist und weshalb weder die Anpassungstabelle noch der inkrementelle Test Kausalität oder Leistung an neuen Daten belegen.

### T07-A02-V05: Suchübung und Kataloggenauigkeit

**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel oder das erwartete Muster, das die Berechnung begründet.

Drei konstruierte Modelle, die mit der gewöhnlichen Methode der kleinsten Quadrate angepasst wurden, verwenden dieselben $n=100$ Fälle, dieselbe Ergebnisvariable „Punktwert der Kataloggenauigkeit“ und einen Achsenabschnitt. Jedes spätere Modell enthält alle Terme des vorherigen Modells. Die gemeinsame totale Quadratsumme ist $SST=1750.0$ und $p$ bezeichnet die Anzahl der Prädiktorkoeffizienten.

| Modell | Prädiktorensatz | p | R-Quadrat |
| --- | --- | --- | --- |
| M1 | Suchübungsblöcke | 1 | 0.300 |
| M2 | Suchübungsblöcke; Punktwert des Katalogvorwissens | 2 | 0.410 |
| M3 | Suchübungsblöcke; Punktwert des Katalogvorwissens; Punktwert der Suchplanung | 3 | 0.440 |

(a) Berechne für jedes Modell die Residuenquadratsumme $SSE=SST(1-R^2)$ und nach M1 bei jedem Schritt die Veränderung in $R^2$. (b) Berechne für alle drei Modelle das korrigierte $R^2=1-(1-R^2)(n-1)/(n-p-1)$. (c) Beschreibe, was das gewöhnliche und das korrigierte $R^2$ über das Hinzufügen des Prädiktors „Punktwert der Suchplanung“ aussagen. (d) Behandle M2 als eingeschränktes und M3 als uneingeschränktes Modell. Schreibe beide Modellgleichungen auf, formuliere die Nullhypothese für den hinzugefügten Koeffizienten und berechne den inkrementellen Test $F=[(R_U^2-R_R^2)/1]/[(1-R_U^2)/(n-3-1)]$ mit 1 und 96 Freiheitsgraden. Bestimme den p-Wert und interpretiere die Entscheidung. (e) Erkläre, weshalb dies eine gültige verschachtelte Folge ist und weshalb weder die Anpassungstabelle noch der inkrementelle Test Kausalität oder Leistung an neuen Daten belegen.

### T07-A02-V06: Workshopteilnahme und Selbstvertrauen

**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel oder das erwartete Muster, das die Berechnung begründet.

Drei konstruierte Modelle, die mit der gewöhnlichen Methode der kleinsten Quadrate angepasst wurden, verwenden dieselben $n=55$ Fälle, dieselbe Ergebnisvariable „Punktwert des Selbstvertrauens“ und einen Achsenabschnitt. Jedes spätere Modell enthält alle Terme des vorherigen Modells. Die gemeinsame totale Quadratsumme ist $SST=980.0$ und $p$ bezeichnet die Anzahl der Prädiktorkoeffizienten.

| Modell | Prädiktorensatz | p | R-Quadrat |
| --- | --- | --- | --- |
| M1 | Workshopsitzungen | 1 | 0.160 |
| M2 | Workshopsitzungen; Ausgangswert des Selbstvertrauens | 2 | 0.290 |
| M3 | Workshopsitzungen; Ausgangswert des Selbstvertrauens; Zahl der Reflexionsprotokolle | 3 | 0.292 |

(a) Berechne für jedes Modell die Residuenquadratsumme $SSE=SST(1-R^2)$ und nach M1 bei jedem Schritt die Veränderung in $R^2$. (b) Berechne für alle drei Modelle das korrigierte $R^2=1-(1-R^2)(n-1)/(n-p-1)$. (c) Beschreibe, was das gewöhnliche und das korrigierte $R^2$ über das Hinzufügen des Prädiktors „Zahl der Reflexionsprotokolle“ aussagen. (d) Behandle M2 als eingeschränktes und M3 als uneingeschränktes Modell. Schreibe beide Modellgleichungen auf, formuliere die Nullhypothese für den hinzugefügten Koeffizienten und berechne den inkrementellen Test $F=[(R_U^2-R_R^2)/1]/[(1-R_U^2)/(n-3-1)]$ mit 1 und 51 Freiheitsgraden. Bestimme den p-Wert und interpretiere die Entscheidung. (e) Erkläre, weshalb dies eine gültige verschachtelte Folge ist und weshalb weder die Anpassungstabelle noch der inkrementelle Test Kausalität oder Leistung an neuen Daten belegen.

### T07-A02-V07: Konzentrationsblöcke und Aufgabengenauigkeit

**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel oder das erwartete Muster, das die Berechnung begründet.

Drei konstruierte Modelle, die mit der gewöhnlichen Methode der kleinsten Quadrate angepasst wurden, verwenden dieselben $n=120$ Fälle, dieselbe Ergebnisvariable „Punktwert der Aufgabengenauigkeit“ und einen Achsenabschnitt. Jedes spätere Modell enthält alle Terme des vorherigen Modells. Die gemeinsame totale Quadratsumme ist $SST=2280.0$ und $p$ bezeichnet die Anzahl der Prädiktorkoeffizienten.

| Modell | Prädiktorensatz | p | R-Quadrat |
| --- | --- | --- | --- |
| M1 | benachrichtigungsfreie Blöcke | 1 | 0.210 |
| M2 | benachrichtigungsfreie Blöcke; Schlafdauer in Stunden | 2 | 0.340 |
| M3 | benachrichtigungsfreie Blöcke; Schlafdauer in Stunden; Zahl der Planungspausen | 3 | 0.370 |

(a) Berechne für jedes Modell die Residuenquadratsumme $SSE=SST(1-R^2)$ und nach M1 bei jedem Schritt die Veränderung in $R^2$. (b) Berechne für alle drei Modelle das korrigierte $R^2=1-(1-R^2)(n-1)/(n-p-1)$. (c) Beschreibe, was das gewöhnliche und das korrigierte $R^2$ über das Hinzufügen des Prädiktors „Zahl der Planungspausen“ aussagen. (d) Behandle M2 als eingeschränktes und M3 als uneingeschränktes Modell. Schreibe beide Modellgleichungen auf, formuliere die Nullhypothese für den hinzugefügten Koeffizienten und berechne den inkrementellen Test $F=[(R_U^2-R_R^2)/1]/[(1-R_U^2)/(n-3-1)]$ mit 1 und 116 Freiheitsgraden. Bestimme den p-Wert und interpretiere die Entscheidung. (e) Erkläre, weshalb dies eine gültige verschachtelte Folge ist und weshalb weder die Anpassungstabelle noch der inkrementelle Test Kausalität oder Leistung an neuen Daten belegen.

### T07-A02-V08: Museumsbesuche und historisches Wissen

**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel oder das erwartete Muster, das die Berechnung begründet.

Drei konstruierte Modelle, die mit der gewöhnlichen Methode der kleinsten Quadrate angepasst wurden, verwenden dieselben $n=75$ Fälle, dieselbe Ergebnisvariable „Punktwert des historischen Wissens“ und einen Achsenabschnitt. Jedes spätere Modell enthält alle Terme des vorherigen Modells. Die gemeinsame totale Quadratsumme ist $SST=1440.0$ und $p$ bezeichnet die Anzahl der Prädiktorkoeffizienten.

| Modell | Prädiktorensatz | p | R-Quadrat |
| --- | --- | --- | --- |
| M1 | Museumsbesuche | 1 | 0.240 |
| M2 | Museumsbesuche; Punktwert des geschichtlichen Vorwissens | 2 | 0.320 |
| M3 | Museumsbesuche; Punktwert des geschichtlichen Vorwissens; Zahl der Ausstellungsnotizen | 3 | 0.321 |

(a) Berechne für jedes Modell die Residuenquadratsumme $SSE=SST(1-R^2)$ und nach M1 bei jedem Schritt die Veränderung in $R^2$. (b) Berechne für alle drei Modelle das korrigierte $R^2=1-(1-R^2)(n-1)/(n-p-1)$. (c) Beschreibe, was das gewöhnliche und das korrigierte $R^2$ über das Hinzufügen des Prädiktors „Zahl der Ausstellungsnotizen“ aussagen. (d) Behandle M2 als eingeschränktes und M3 als uneingeschränktes Modell. Schreibe beide Modellgleichungen auf, formuliere die Nullhypothese für den hinzugefügten Koeffizienten und berechne den inkrementellen Test $F=[(R_U^2-R_R^2)/1]/[(1-R_U^2)/(n-3-1)]$ mit 1 und 71 Freiheitsgraden. Bestimme den p-Wert und interpretiere die Entscheidung. (e) Erkläre, weshalb dies eine gültige verschachtelte Folge ist und weshalb weder die Anpassungstabelle noch der inkrementelle Test Kausalität oder Leistung an neuen Daten belegen.

### T07-A02-V09: Peer-Feedback und Überarbeitungsqualität

**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel oder das erwartete Muster, das die Berechnung begründet.

Drei konstruierte Modelle, die mit der gewöhnlichen Methode der kleinsten Quadrate angepasst wurden, verwenden dieselben $n=65$ Fälle, dieselbe Ergebnisvariable „Punktwert der Überarbeitungsqualität“ und einen Achsenabschnitt. Jedes spätere Modell enthält alle Terme des vorherigen Modells. Die gemeinsame totale Quadratsumme ist $SST=1620.0$ und $p$ bezeichnet die Anzahl der Prädiktorkoeffizienten.

| Modell | Prädiktorensatz | p | R-Quadrat |
| --- | --- | --- | --- |
| M1 | Runden mit Peer-Feedback | 1 | 0.190 |
| M2 | Runden mit Peer-Feedback; Ausgangswert der Schreibqualität | 2 | 0.360 |
| M3 | Runden mit Peer-Feedback; Ausgangswert der Schreibqualität; Punktwert des Überarbeitungsplans | 3 | 0.420 |

(a) Berechne für jedes Modell die Residuenquadratsumme $SSE=SST(1-R^2)$ und nach M1 bei jedem Schritt die Veränderung in $R^2$. (b) Berechne für alle drei Modelle das korrigierte $R^2=1-(1-R^2)(n-1)/(n-p-1)$. (c) Beschreibe, was das gewöhnliche und das korrigierte $R^2$ über das Hinzufügen des Prädiktors „Punktwert des Überarbeitungsplans“ aussagen. (d) Behandle M2 als eingeschränktes und M3 als uneingeschränktes Modell. Schreibe beide Modellgleichungen auf, formuliere die Nullhypothese für den hinzugefügten Koeffizienten und berechne den inkrementellen Test $F=[(R_U^2-R_R^2)/1]/[(1-R_U^2)/(n-3-1)]$ mit 1 und 61 Freiheitsgraden. Bestimme den p-Wert und interpretiere die Entscheidung. (e) Erkläre, weshalb dies eine gültige verschachtelte Folge ist und weshalb weder die Anpassungstabelle noch der inkrementelle Test Kausalität oder Leistung an neuen Daten belegen.

### T07-A02-V10: Planungssitzungen und Bearbeitungszeit

**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel oder das erwartete Muster, das die Berechnung begründet.

Drei konstruierte Modelle, die mit der gewöhnlichen Methode der kleinsten Quadrate angepasst wurden, verwenden dieselben $n=110$ Fälle, dieselbe Ergebnisvariable „Bearbeitungszeit“ und einen Achsenabschnitt. Jedes spätere Modell enthält alle Terme des vorherigen Modells. Die gemeinsame totale Quadratsumme ist $SST=1960.0$ und $p$ bezeichnet die Anzahl der Prädiktorkoeffizienten.

| Modell | Prädiktorensatz | p | R-Quadrat |
| --- | --- | --- | --- |
| M1 | Planungssitzungen | 1 | 0.270 |
| M2 | Planungssitzungen; Punktwert der Aufgabenkomplexität | 2 | 0.390 |
| M3 | Planungssitzungen; Punktwert der Aufgabenkomplexität; Zahl der Fortschrittskontrollen | 3 | 0.395 |

(a) Berechne für jedes Modell die Residuenquadratsumme $SSE=SST(1-R^2)$ und nach M1 bei jedem Schritt die Veränderung in $R^2$. (b) Berechne für alle drei Modelle das korrigierte $R^2=1-(1-R^2)(n-1)/(n-p-1)$. (c) Beschreibe, was das gewöhnliche und das korrigierte $R^2$ über das Hinzufügen des Prädiktors „Zahl der Fortschrittskontrollen“ aussagen. (d) Behandle M2 als eingeschränktes und M3 als uneingeschränktes Modell. Schreibe beide Modellgleichungen auf, formuliere die Nullhypothese für den hinzugefügten Koeffizienten und berechne den inkrementellen Test $F=[(R_U^2-R_R^2)/1]/[(1-R_U^2)/(n-3-1)]$ mit 1 und 106 Freiheitsgraden. Bestimme den p-Wert und interpretiere die Entscheidung. (e) Erkläre, weshalb dies eine gültige verschachtelte Folge ist und weshalb weder die Anpassungstabelle noch der inkrementelle Test Kausalität oder Leistung an neuen Daten belegen.

## A03: Den globalen F-Test von den t-Tests der Koeffizienten unterscheiden

### T07-A03-V01: Begleitete Übung und statistisches Denken

**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel oder das erwartete Muster, das die Berechnung begründet.

Ein konstruiertes Modell mit drei Prädiktoren für die Ergebnisvariable „Punktwert im statistischen Denken“ verwendet $n=50$ und berichtet $R^2=0.220$. $\beta_1$, $\beta_2$ und $\beta_3$ bezeichnen die drei Populationssteigungen. Für $\alpha=.05$ ist der vorgegebene kritische Wert $F_{3,46}=2.80684$. Die Koeffiziententabelle lautet:

| Prädiktor | Schätzwert | SE |
| --- | --- | --- |
| Stunden begleiteter Übung | 1.800 | 0.600 |
| Punktwert der vorherigen Vorbereitung | 0.220 | 0.180 |
| Reflexionssitzungen | 0.120 | 0.160 |

(a) Formuliere die globale Nullhypothese, berechne $F=(R^2/3)/[(1-R^2)/(n-3-1)]$ und triff die globale Entscheidung. (b) Berechne für jeden Prädiktor $t=b/SE$, den zweiseitigen $p$-Wert mit 46 residualen Freiheitsgraden und die Entscheidung bei $\alpha=.05$. (c) Formuliere die Nullhypothese für einen einzelnen Koeffizienten und erkläre, weshalb ein globales Ergebnis nicht zeigt, welche Steigung von null abweicht. (d) Bringe die globalen und individuellen Entscheidungen dieses Modells miteinander in Einklang, ohne eine der beiden Testarten als Beleg für Wichtigkeit, Vorhersage oder Kausalität zu behandeln.

### T07-A03-V02: Arbeitsablauf im Archiv und Suchzeit

**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel oder das erwartete Muster, das die Berechnung begründet.

Ein konstruiertes Modell mit drei Prädiktoren für die Ergebnisvariable „Suchzeit“ verwendet $n=60$ und berichtet $R^2=0.300$. $\beta_1$, $\beta_2$ und $\beta_3$ bezeichnen die drei Populationssteigungen. Für $\alpha=.05$ ist der vorgegebene kritische Wert $F_{3,56}=2.76943$. Die Koeffiziententabelle lautet:

| Prädiktor | Schätzwert | SE |
| --- | --- | --- |
| Übungssitzungen mit Checkliste | -1.400 | 0.450 |
| Monate Archiverfahrung | -0.200 | 0.160 |
| Katalogvertrautheit | 0.300 | 0.120 |

(a) Formuliere die globale Nullhypothese, berechne $F=(R^2/3)/[(1-R^2)/(n-3-1)]$ und triff die globale Entscheidung. (b) Berechne für jeden Prädiktor $t=b/SE$, den zweiseitigen $p$-Wert mit 56 residualen Freiheitsgraden und die Entscheidung bei $\alpha=.05$. (c) Formuliere die Nullhypothese für einen einzelnen Koeffizienten und erkläre, weshalb ein globales Ergebnis nicht zeigt, welche Steigung von null abweicht. (d) Bringe die globalen und individuellen Entscheidungen dieses Modells miteinander in Einklang, ohne eine der beiden Testarten als Beleg für Wichtigkeit, Vorhersage oder Kausalität zu behandeln.

### T07-A03-V03: Leseroutinen und Textverständnis

**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel oder das erwartete Muster, das die Berechnung begründet.

Ein konstruiertes Modell mit drei Prädiktoren für die Ergebnisvariable „Punktwert im Textverständnis“ verwendet $n=70$ und berichtet $R^2=0.100$. $\beta_1$, $\beta_2$ und $\beta_3$ bezeichnen die drei Populationssteigungen. Für $\alpha=.05$ ist der vorgegebene kritische Wert $F_{3,66}=2.74371$. Die Koeffiziententabelle lautet:

| Prädiktor | Schätzwert | SE |
| --- | --- | --- |
| wöchentliche Lesestunden | 1.100 | 0.580 |
| Ausgangswert des Wortschatzes | 0.180 | 0.130 |
| Annotationssitzungen | -0.150 | 0.140 |

(a) Formuliere die globale Nullhypothese, berechne $F=(R^2/3)/[(1-R^2)/(n-3-1)]$ und triff die globale Entscheidung. (b) Berechne für jeden Prädiktor $t=b/SE$, den zweiseitigen $p$-Wert mit 66 residualen Freiheitsgraden und die Entscheidung bei $\alpha=.05$. (c) Formuliere die Nullhypothese für einen einzelnen Koeffizienten und erkläre, weshalb ein globales Ergebnis nicht zeigt, welche Steigung von null abweicht. (d) Bringe die globalen und individuellen Entscheidungen dieses Modells miteinander in Einklang, ohne eine der beiden Testarten als Beleg für Wichtigkeit, Vorhersage oder Kausalität zu behandeln.

### T07-A03-V04: Streckenübung und Navigationszeit

**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel oder das erwartete Muster, das die Berechnung begründet.

Ein konstruiertes Modell mit drei Prädiktoren für die Ergebnisvariable „Navigationszeit“ verwendet $n=80$ und berichtet $R^2=0.250$. $\beta_1$, $\beta_2$ und $\beta_3$ bezeichnen die drei Populationssteigungen. Für $\alpha=.05$ ist der vorgegebene kritische Wert $F_{3,76}=2.72494$. Die Koeffiziententabelle lautet:

| Prädiktor | Schätzwert | SE |
| --- | --- | --- |
| Versuche zur Streckenübung | -1.800 | 0.550 |
| Punktwert der Streckenkenntnis | -0.120 | 0.100 |
| Erinnerung an Orientierungspunkte | 0.280 | 0.110 |

(a) Formuliere die globale Nullhypothese, berechne $F=(R^2/3)/[(1-R^2)/(n-3-1)]$ und triff die globale Entscheidung. (b) Berechne für jeden Prädiktor $t=b/SE$, den zweiseitigen $p$-Wert mit 76 residualen Freiheitsgraden und die Entscheidung bei $\alpha=.05$. (c) Formuliere die Nullhypothese für einen einzelnen Koeffizienten und erkläre, weshalb ein globales Ergebnis nicht zeigt, welche Steigung von null abweicht. (d) Bringe die globalen und individuellen Entscheidungen dieses Modells miteinander in Einklang, ohne eine der beiden Testarten als Beleg für Wichtigkeit, Vorhersage oder Kausalität zu behandeln.

### T07-A03-V05: Suchübung und Kataloggenauigkeit

**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel oder das erwartete Muster, das die Berechnung begründet.

Ein konstruiertes Modell mit drei Prädiktoren für die Ergebnisvariable „Punktwert der Kataloggenauigkeit“ verwendet $n=90$ und berichtet $R^2=0.080$. $\beta_1$, $\beta_2$ und $\beta_3$ bezeichnen die drei Populationssteigungen. Für $\alpha=.05$ ist der vorgegebene kritische Wert $F_{3,86}=2.71065$. Die Koeffiziententabelle lautet:

| Prädiktor | Schätzwert | SE |
| --- | --- | --- |
| Suchübungsblöcke | 1.000 | 0.570 |
| Punktwert des Katalogvorwissens | 0.150 | 0.120 |
| Suchplanung | 0.180 | 0.140 |

(a) Formuliere die globale Nullhypothese, berechne $F=(R^2/3)/[(1-R^2)/(n-3-1)]$ und triff die globale Entscheidung. (b) Berechne für jeden Prädiktor $t=b/SE$, den zweiseitigen $p$-Wert mit 86 residualen Freiheitsgraden und die Entscheidung bei $\alpha=.05$. (c) Formuliere die Nullhypothese für einen einzelnen Koeffizienten und erkläre, weshalb ein globales Ergebnis nicht zeigt, welche Steigung von null abweicht. (d) Bringe die globalen und individuellen Entscheidungen dieses Modells miteinander in Einklang, ohne eine der beiden Testarten als Beleg für Wichtigkeit, Vorhersage oder Kausalität zu behandeln.

### T07-A03-V06: Workshopteilnahme und Selbstvertrauen

**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel oder das erwartete Muster, das die Berechnung begründet.

Ein konstruiertes Modell mit drei Prädiktoren für die Ergebnisvariable „Punktwert des Selbstvertrauens“ verwendet $n=100$ und berichtet $R^2=0.350$. $\beta_1$, $\beta_2$ und $\beta_3$ bezeichnen die drei Populationssteigungen. Für $\alpha=.05$ ist der vorgegebene kritische Wert $F_{3,96}=2.69939$. Die Koeffiziententabelle lautet:

| Prädiktor | Schätzwert | SE |
| --- | --- | --- |
| Workshopsitzungen | 2.100 | 0.500 |
| Ausgangswert des Selbstvertrauens | 0.380 | 0.140 |
| Reflexionsprotokolle | -0.100 | 0.130 |

(a) Formuliere die globale Nullhypothese, berechne $F=(R^2/3)/[(1-R^2)/(n-3-1)]$ und triff die globale Entscheidung. (b) Berechne für jeden Prädiktor $t=b/SE$, den zweiseitigen $p$-Wert mit 96 residualen Freiheitsgraden und die Entscheidung bei $\alpha=.05$. (c) Formuliere die Nullhypothese für einen einzelnen Koeffizienten und erkläre, weshalb ein globales Ergebnis nicht zeigt, welche Steigung von null abweicht. (d) Bringe die globalen und individuellen Entscheidungen dieses Modells miteinander in Einklang, ohne eine der beiden Testarten als Beleg für Wichtigkeit, Vorhersage oder Kausalität zu behandeln.

### T07-A03-V07: Konzentrationsblöcke und Aufgabengenauigkeit

**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel oder das erwartete Muster, das die Berechnung begründet.

Ein konstruiertes Modell mit drei Prädiktoren für die Ergebnisvariable „Punktwert der Aufgabengenauigkeit“ verwendet $n=110$ und berichtet $R^2=0.200$. $\beta_1$, $\beta_2$ und $\beta_3$ bezeichnen die drei Populationssteigungen. Für $\alpha=.05$ ist der vorgegebene kritische Wert $F_{3,106}=2.69030$. Die Koeffiziententabelle lautet:

| Prädiktor | Schätzwert | SE |
| --- | --- | --- |
| benachrichtigungsfreie Blöcke | 1.300 | 0.400 |
| Schlafdauer in Stunden | 0.120 | 0.110 |
| Planungspausen | 0.250 | 0.150 |

(a) Formuliere die globale Nullhypothese, berechne $F=(R^2/3)/[(1-R^2)/(n-3-1)]$ und triff die globale Entscheidung. (b) Berechne für jeden Prädiktor $t=b/SE$, den zweiseitigen $p$-Wert mit 106 residualen Freiheitsgraden und die Entscheidung bei $\alpha=.05$. (c) Formuliere die Nullhypothese für einen einzelnen Koeffizienten und erkläre, weshalb ein globales Ergebnis nicht zeigt, welche Steigung von null abweicht. (d) Bringe die globalen und individuellen Entscheidungen dieses Modells miteinander in Einklang, ohne eine der beiden Testarten als Beleg für Wichtigkeit, Vorhersage oder Kausalität zu behandeln.

### T07-A03-V08: Museumsbesuche und historisches Wissen

**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel oder das erwartete Muster, das die Berechnung begründet.

Ein konstruiertes Modell mit drei Prädiktoren für die Ergebnisvariable „Punktwert des historischen Wissens“ verwendet $n=120$ und berichtet $R^2=0.280$. $\beta_1$, $\beta_2$ und $\beta_3$ bezeichnen die drei Populationssteigungen. Für $\alpha=.05$ ist der vorgegebene kritische Wert $F_{3,116}=2.68281$. Die Koeffiziententabelle lautet:

| Prädiktor | Schätzwert | SE |
| --- | --- | --- |
| Museumsbesuche | 2.000 | 0.480 |
| Punktwert des geschichtlichen Vorwissens | 0.310 | 0.130 |
| Ausstellungsnotizen | 0.080 | 0.120 |

(a) Formuliere die globale Nullhypothese, berechne $F=(R^2/3)/[(1-R^2)/(n-3-1)]$ und triff die globale Entscheidung. (b) Berechne für jeden Prädiktor $t=b/SE$, den zweiseitigen $p$-Wert mit 116 residualen Freiheitsgraden und die Entscheidung bei $\alpha=.05$. (c) Formuliere die Nullhypothese für einen einzelnen Koeffizienten und erkläre, weshalb ein globales Ergebnis nicht zeigt, welche Steigung von null abweicht. (d) Bringe die globalen und individuellen Entscheidungen dieses Modells miteinander in Einklang, ohne eine der beiden Testarten als Beleg für Wichtigkeit, Vorhersage oder Kausalität zu behandeln.

### T07-A03-V09: Peer-Feedback und Überarbeitungsqualität

**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel oder das erwartete Muster, das die Berechnung begründet.

Ein konstruiertes Modell mit drei Prädiktoren für die Ergebnisvariable „Punktwert der Überarbeitungsqualität“ verwendet $n=75$ und berichtet $R^2=0.160$. $\beta_1$, $\beta_2$ und $\beta_3$ bezeichnen die drei Populationssteigungen. Für $\alpha=.05$ ist der vorgegebene kritische Wert $F_{3,71}=2.73365$. Die Koeffiziententabelle lautet:

| Prädiktor | Schätzwert | SE |
| --- | --- | --- |
| Runden mit Peer-Feedback | 1.200 | 0.520 |
| Ausgangswert der Schreibqualität | 0.190 | 0.150 |
| Überarbeitungsplanung | -0.090 | 0.130 |

(a) Formuliere die globale Nullhypothese, berechne $F=(R^2/3)/[(1-R^2)/(n-3-1)]$ und triff die globale Entscheidung. (b) Berechne für jeden Prädiktor $t=b/SE$, den zweiseitigen $p$-Wert mit 71 residualen Freiheitsgraden und die Entscheidung bei $\alpha=.05$. (c) Formuliere die Nullhypothese für einen einzelnen Koeffizienten und erkläre, weshalb ein globales Ergebnis nicht zeigt, welche Steigung von null abweicht. (d) Bringe die globalen und individuellen Entscheidungen dieses Modells miteinander in Einklang, ohne eine der beiden Testarten als Beleg für Wichtigkeit, Vorhersage oder Kausalität zu behandeln.

### T07-A03-V10: Planungssitzungen und Bearbeitungszeit

**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel oder das erwartete Muster, das die Berechnung begründet.

Ein konstruiertes Modell mit drei Prädiktoren für die Ergebnisvariable „Bearbeitungszeit“ verwendet $n=65$ und berichtet $R^2=0.240$. $\beta_1$, $\beta_2$ und $\beta_3$ bezeichnen die drei Populationssteigungen. Für $\alpha=.05$ ist der vorgegebene kritische Wert $F_{3,61}=2.75548$. Die Koeffiziententabelle lautet:

| Prädiktor | Schätzwert | SE |
| --- | --- | --- |
| Planungssitzungen | -1.600 | 0.500 |
| Punktwert der Aufgabenkomplexität | 0.420 | 0.170 |
| Fortschrittskontrollen | 0.160 | 0.140 |

(a) Formuliere die globale Nullhypothese, berechne $F=(R^2/3)/[(1-R^2)/(n-3-1)]$ und triff die globale Entscheidung. (b) Berechne für jeden Prädiktor $t=b/SE$, den zweiseitigen $p$-Wert mit 61 residualen Freiheitsgraden und die Entscheidung bei $\alpha=.05$. (c) Formuliere die Nullhypothese für einen einzelnen Koeffizienten und erkläre, weshalb ein globales Ergebnis nicht zeigt, welche Steigung von null abweicht. (d) Bringe die globalen und individuellen Entscheidungen dieses Modells miteinander in Einklang, ohne eine der beiden Testarten als Beleg für Wichtigkeit, Vorhersage oder Kausalität zu behandeln.

## A04: Semipartielle Korrelation und zusätzliches R-Quadrat

### T07-A04-V01: Begleitete Übung und statistisches Denken

**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel oder das erwartete Muster, das die Berechnung begründet.

Ein konstruiertes aktuelles Modell für die Ergebnisvariable „Punktwert im statistischen Denken“ enthält bereits die Prädiktoren „Stunden begleiteter Übung“ und „Punktwert der vorherigen Vorbereitung“. Es weist $R^2=0.300$ auf. Jeder unten aufgeführte Kandidat wurde separat auf diese aktuellen Prädiktoren regressiert. Das Residuum aus dieser Regression ist der Anteil des Kandidaten, der durch den aktuellen Satz nicht linear vorhergesagt wird. Die Tabelle berichtet die Korrelation zwischen diesem residualisierten Kandidaten und der ursprünglichen, nicht residualisierten Ergebnisvariable. Das Symbol $r_{sp}$ bezeichnet diese semipartielle Korrelation:

| Kandidat | Semipartielles r |
| --- | --- |
| Reflexionssitzungen | 0.240 |
| Treffen mit Lernpartnern | 0.100 |
| Planungskontrollen | -0.180 |

(a) Erkläre, weshalb dies eine semipartielle und keine partielle Korrelation ist. (b) Berechne für jede einzelne Kandidatenaufnahme $\Delta R^2=r_{sp}^2$ und das daraus entstehende $R^2$. (c) Bestimme den gewählten Kandidaten und seinen Zuwachs, wenn ein Vorwärtsschritt den grössten Zuwachs verwendet. (d) Erkläre, was dieser Schritt rechtfertigt und was nicht. Begründe insbesondere, weshalb er weder beweist, dass die gewählte Variable wahr oder kausal ist, noch garantiert, dass sie nach Aufnahme eines weiteren Terms die beste bleibt.

### T07-A04-V02: Arbeitsablauf im Archiv und Suchzeit

**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel oder das erwartete Muster, das die Berechnung begründet.

Ein konstruiertes aktuelles Modell für die Ergebnisvariable „Suchzeit“ enthält bereits die Prädiktoren „Übungssitzungen mit Checkliste“ und „Monate Archiverfahrung“. Es weist $R^2=0.260$ auf. Jeder unten aufgeführte Kandidat wurde separat auf diese aktuellen Prädiktoren regressiert. Das Residuum aus dieser Regression ist der Anteil des Kandidaten, der durch den aktuellen Satz nicht linear vorhergesagt wird. Die Tabelle berichtet die Korrelation zwischen diesem residualisierten Kandidaten und der ursprünglichen, nicht residualisierten Ergebnisvariable. Das Symbol $r_{sp}$ bezeichnet diese semipartielle Korrelation:

| Kandidat | Semipartielles r |
| --- | --- |
| Katalogvertrautheit | -0.120 |
| Nutzung eines Schreibtischplans | -0.270 |
| Beratungen durch Mentoren | 0.080 |

(a) Erkläre, weshalb dies eine semipartielle und keine partielle Korrelation ist. (b) Berechne für jede einzelne Kandidatenaufnahme $\Delta R^2=r_{sp}^2$ und das daraus entstehende $R^2$. (c) Bestimme den gewählten Kandidaten und seinen Zuwachs, wenn ein Vorwärtsschritt den grössten Zuwachs verwendet. (d) Erkläre, was dieser Schritt rechtfertigt und was nicht. Begründe insbesondere, weshalb er weder beweist, dass die gewählte Variable wahr oder kausal ist, noch garantiert, dass sie nach Aufnahme eines weiteren Terms die beste bleibt.

### T07-A04-V03: Leseroutinen und Textverständnis

**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel oder das erwartete Muster, das die Berechnung begründet.

Ein konstruiertes aktuelles Modell für die Ergebnisvariable „Punktwert im Textverständnis“ enthält bereits die Prädiktoren „wöchentliche Lesestunden“ und „Ausgangswert des Wortschatzes“. Es weist $R^2=0.340$ auf. Jeder unten aufgeführte Kandidat wurde separat auf diese aktuellen Prädiktoren regressiert. Das Residuum aus dieser Regression ist der Anteil des Kandidaten, der durch den aktuellen Satz nicht linear vorhergesagt wird. Die Tabelle berichtet die Korrelation zwischen diesem residualisierten Kandidaten und der ursprünglichen, nicht residualisierten Ergebnisvariable. Das Symbol $r_{sp}$ bezeichnet diese semipartielle Korrelation:

| Kandidat | Semipartielles r |
| --- | --- |
| Annotationssitzungen | 0.150 |
| Diskussionsbeiträge | 0.310 |
| Blöcke stillen Lesens | 0.200 |

(a) Erkläre, weshalb dies eine semipartielle und keine partielle Korrelation ist. (b) Berechne für jede einzelne Kandidatenaufnahme $\Delta R^2=r_{sp}^2$ und das daraus entstehende $R^2$. (c) Bestimme den gewählten Kandidaten und seinen Zuwachs, wenn ein Vorwärtsschritt den grössten Zuwachs verwendet. (d) Erkläre, was dieser Schritt rechtfertigt und was nicht. Begründe insbesondere, weshalb er weder beweist, dass die gewählte Variable wahr oder kausal ist, noch garantiert, dass sie nach Aufnahme eines weiteren Terms die beste bleibt.

### T07-A04-V04: Streckenübung und Navigationszeit

**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel oder das erwartete Muster, das die Berechnung begründet.

Ein konstruiertes aktuelles Modell für die Ergebnisvariable „Navigationszeit“ enthält bereits die Prädiktoren „Versuche zur Streckenübung“ und „Punktwert der Streckenkenntnis“. Es weist $R^2=0.290$ auf. Jeder unten aufgeführte Kandidat wurde separat auf diese aktuellen Prädiktoren regressiert. Das Residuum aus dieser Regression ist der Anteil des Kandidaten, der durch den aktuellen Satz nicht linear vorhergesagt wird. Die Tabelle berichtet die Korrelation zwischen diesem residualisierten Kandidaten und der ursprünglichen, nicht residualisierten Ergebnisvariable. Das Symbol $r_{sp}$ bezeichnet diese semipartielle Korrelation:

| Kandidat | Semipartielles r |
| --- | --- |
| Erinnerung an Orientierungspunkte | -0.280 |
| Kartenkontrollen | -0.140 |
| Streckenvorschauen | 0.190 |

(a) Erkläre, weshalb dies eine semipartielle und keine partielle Korrelation ist. (b) Berechne für jede einzelne Kandidatenaufnahme $\Delta R^2=r_{sp}^2$ und das daraus entstehende $R^2$. (c) Bestimme den gewählten Kandidaten und seinen Zuwachs, wenn ein Vorwärtsschritt den grössten Zuwachs verwendet. (d) Erkläre, was dieser Schritt rechtfertigt und was nicht. Begründe insbesondere, weshalb er weder beweist, dass die gewählte Variable wahr oder kausal ist, noch garantiert, dass sie nach Aufnahme eines weiteren Terms die beste bleibt.

### T07-A04-V05: Suchübung und Kataloggenauigkeit

**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel oder das erwartete Muster, das die Berechnung begründet.

Ein konstruiertes aktuelles Modell für die Ergebnisvariable „Punktwert der Kataloggenauigkeit“ enthält bereits die Prädiktoren „Suchübungsblöcke“ und „Punktwert des Katalogvorwissens“. Es weist $R^2=0.370$ auf. Jeder unten aufgeführte Kandidat wurde separat auf diese aktuellen Prädiktoren regressiert. Das Residuum aus dieser Regression ist der Anteil des Kandidaten, der durch den aktuellen Satz nicht linear vorhergesagt wird. Die Tabelle berichtet die Korrelation zwischen diesem residualisierten Kandidaten und der ursprünglichen, nicht residualisierten Ergebnisvariable. Das Symbol $r_{sp}$ bezeichnet diese semipartielle Korrelation:

| Kandidat | Semipartielles r |
| --- | --- |
| Suchplanung | 0.110 |
| Stichwortübungen | 0.220 |
| genutzte Kataloghinweise | 0.290 |

(a) Erkläre, weshalb dies eine semipartielle und keine partielle Korrelation ist. (b) Berechne für jede einzelne Kandidatenaufnahme $\Delta R^2=r_{sp}^2$ und das daraus entstehende $R^2$. (c) Bestimme den gewählten Kandidaten und seinen Zuwachs, wenn ein Vorwärtsschritt den grössten Zuwachs verwendet. (d) Erkläre, was dieser Schritt rechtfertigt und was nicht. Begründe insbesondere, weshalb er weder beweist, dass die gewählte Variable wahr oder kausal ist, noch garantiert, dass sie nach Aufnahme eines weiteren Terms die beste bleibt.

### T07-A04-V06: Workshopteilnahme und Selbstvertrauen

**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel oder das erwartete Muster, das die Berechnung begründet.

Ein konstruiertes aktuelles Modell für die Ergebnisvariable „Punktwert des Selbstvertrauens“ enthält bereits die Prädiktoren „Workshopsitzungen“ und „Ausgangswert des Selbstvertrauens“. Es weist $R^2=0.320$ auf. Jeder unten aufgeführte Kandidat wurde separat auf diese aktuellen Prädiktoren regressiert. Das Residuum aus dieser Regression ist der Anteil des Kandidaten, der durch den aktuellen Satz nicht linear vorhergesagt wird. Die Tabelle berichtet die Korrelation zwischen diesem residualisierten Kandidaten und der ursprünglichen, nicht residualisierten Ergebnisvariable. Das Symbol $r_{sp}$ bezeichnet diese semipartielle Korrelation:

| Kandidat | Semipartielles r |
| --- | --- |
| Reflexionsprotokolle | 0.260 |
| Peer-Treffen | 0.170 |
| praktische Demonstrationen | -0.090 |

(a) Erkläre, weshalb dies eine semipartielle und keine partielle Korrelation ist. (b) Berechne für jede einzelne Kandidatenaufnahme $\Delta R^2=r_{sp}^2$ und das daraus entstehende $R^2$. (c) Bestimme den gewählten Kandidaten und seinen Zuwachs, wenn ein Vorwärtsschritt den grössten Zuwachs verwendet. (d) Erkläre, was dieser Schritt rechtfertigt und was nicht. Begründe insbesondere, weshalb er weder beweist, dass die gewählte Variable wahr oder kausal ist, noch garantiert, dass sie nach Aufnahme eines weiteren Terms die beste bleibt.

### T07-A04-V07: Konzentrationsblöcke und Aufgabengenauigkeit

**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel oder das erwartete Muster, das die Berechnung begründet.

Ein konstruiertes aktuelles Modell für die Ergebnisvariable „Punktwert der Aufgabengenauigkeit“ enthält bereits die Prädiktoren „benachrichtigungsfreie Blöcke“ und „Schlafdauer in Stunden“. Es weist $R^2=0.250$ auf. Jeder unten aufgeführte Kandidat wurde separat auf diese aktuellen Prädiktoren regressiert. Das Residuum aus dieser Regression ist der Anteil des Kandidaten, der durch den aktuellen Satz nicht linear vorhergesagt wird. Die Tabelle berichtet die Korrelation zwischen diesem residualisierten Kandidaten und der ursprünglichen, nicht residualisierten Ergebnisvariable. Das Symbol $r_{sp}$ bezeichnet diese semipartielle Korrelation:

| Kandidat | Semipartielles r |
| --- | --- |
| Planungspausen | 0.130 |
| bildschirmfreie Zeiträume | 0.210 |
| Aufgabenvorschauen | 0.070 |

(a) Erkläre, weshalb dies eine semipartielle und keine partielle Korrelation ist. (b) Berechne für jede einzelne Kandidatenaufnahme $\Delta R^2=r_{sp}^2$ und das daraus entstehende $R^2$. (c) Bestimme den gewählten Kandidaten und seinen Zuwachs, wenn ein Vorwärtsschritt den grössten Zuwachs verwendet. (d) Erkläre, was dieser Schritt rechtfertigt und was nicht. Begründe insbesondere, weshalb er weder beweist, dass die gewählte Variable wahr oder kausal ist, noch garantiert, dass sie nach Aufnahme eines weiteren Terms die beste bleibt.

### T07-A04-V08: Museumsbesuche und historisches Wissen

**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel oder das erwartete Muster, das die Berechnung begründet.

Ein konstruiertes aktuelles Modell für die Ergebnisvariable „Punktwert des historischen Wissens“ enthält bereits die Prädiktoren „Museumsbesuche“ und „Punktwert des geschichtlichen Vorwissens“. Es weist $R^2=0.310$ auf. Jeder unten aufgeführte Kandidat wurde separat auf diese aktuellen Prädiktoren regressiert. Das Residuum aus dieser Regression ist der Anteil des Kandidaten, der durch den aktuellen Satz nicht linear vorhergesagt wird. Die Tabelle berichtet die Korrelation zwischen diesem residualisierten Kandidaten und der ursprünglichen, nicht residualisierten Ergebnisvariable. Das Symbol $r_{sp}$ bezeichnet diese semipartielle Korrelation:

| Kandidat | Semipartielles r |
| --- | --- |
| Ausstellungsnotizen | 0.180 |
| Stationen einer Führung | 0.120 |
| weiterführende Lektüre | 0.250 |

(a) Erkläre, weshalb dies eine semipartielle und keine partielle Korrelation ist. (b) Berechne für jede einzelne Kandidatenaufnahme $\Delta R^2=r_{sp}^2$ und das daraus entstehende $R^2$. (c) Bestimme den gewählten Kandidaten und seinen Zuwachs, wenn ein Vorwärtsschritt den grössten Zuwachs verwendet. (d) Erkläre, was dieser Schritt rechtfertigt und was nicht. Begründe insbesondere, weshalb er weder beweist, dass die gewählte Variable wahr oder kausal ist, noch garantiert, dass sie nach Aufnahme eines weiteren Terms die beste bleibt.

### T07-A04-V09: Peer-Feedback und Überarbeitungsqualität

**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel oder das erwartete Muster, das die Berechnung begründet.

Ein konstruiertes aktuelles Modell für die Ergebnisvariable „Punktwert der Überarbeitungsqualität“ enthält bereits die Prädiktoren „Runden mit Peer-Feedback“ und „Ausgangswert der Schreibqualität“. Es weist $R^2=0.360$ auf. Jeder unten aufgeführte Kandidat wurde separat auf diese aktuellen Prädiktoren regressiert. Das Residuum aus dieser Regression ist der Anteil des Kandidaten, der durch den aktuellen Satz nicht linear vorhergesagt wird. Die Tabelle berichtet die Korrelation zwischen diesem residualisierten Kandidaten und der ursprünglichen, nicht residualisierten Ergebnisvariable. Das Symbol $r_{sp}$ bezeichnet diese semipartielle Korrelation:

| Kandidat | Semipartielles r |
| --- | --- |
| Überarbeitungsplanung | 0.090 |
| genutzte Peer-Kommentare | 0.280 |
| Korrekturdurchgänge | 0.160 |

(a) Erkläre, weshalb dies eine semipartielle und keine partielle Korrelation ist. (b) Berechne für jede einzelne Kandidatenaufnahme $\Delta R^2=r_{sp}^2$ und das daraus entstehende $R^2$. (c) Bestimme den gewählten Kandidaten und seinen Zuwachs, wenn ein Vorwärtsschritt den grössten Zuwachs verwendet. (d) Erkläre, was dieser Schritt rechtfertigt und was nicht. Begründe insbesondere, weshalb er weder beweist, dass die gewählte Variable wahr oder kausal ist, noch garantiert, dass sie nach Aufnahme eines weiteren Terms die beste bleibt.

### T07-A04-V10: Planungssitzungen und Bearbeitungszeit

**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel oder das erwartete Muster, das die Berechnung begründet.

Ein konstruiertes aktuelles Modell für die Ergebnisvariable „Bearbeitungszeit“ enthält bereits die Prädiktoren „Planungssitzungen“ und „Punktwert der Aufgabenkomplexität“. Es weist $R^2=0.280$ auf. Jeder unten aufgeführte Kandidat wurde separat auf diese aktuellen Prädiktoren regressiert. Das Residuum aus dieser Regression ist der Anteil des Kandidaten, der durch den aktuellen Satz nicht linear vorhergesagt wird. Die Tabelle berichtet die Korrelation zwischen diesem residualisierten Kandidaten und der ursprünglichen, nicht residualisierten Ergebnisvariable. Das Symbol $r_{sp}$ bezeichnet diese semipartielle Korrelation:

| Kandidat | Semipartielles r |
| --- | --- |
| Fortschrittskontrollen | -0.230 |
| Kalendererinnerungen | -0.110 |
| Aufgabenvorschauen | 0.200 |

(a) Erkläre, weshalb dies eine semipartielle und keine partielle Korrelation ist. (b) Berechne für jede einzelne Kandidatenaufnahme $\Delta R^2=r_{sp}^2$ und das daraus entstehende $R^2$. (c) Bestimme den gewählten Kandidaten und seinen Zuwachs, wenn ein Vorwärtsschritt den grössten Zuwachs verwendet. (d) Erkläre, was dieser Schritt rechtfertigt und was nicht. Begründe insbesondere, weshalb er weder beweist, dass die gewählte Variable wahr oder kausal ist, noch garantiert, dass sie nach Aufnahme eines weiteren Terms die beste bleibt.

## A05: Vorab festgelegte Kandidatenmodelle mit AIC vergleichen

### T07-A05-V01: Begleitete Übung und statistisches Denken

**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel oder das erwartete Muster, das die Berechnung begründet.

Vier konstruierte, vorab festgelegte Kandidatenmodelle verwenden genau dieselben Fälle und dieselbe Ergebnisvariable „Punktwert im statistischen Denken“. Hier ist $\log(L)$ die vom angepassten Modell berichtete maximierte Log-Likelihood. Nach der angegebenen Konvention zählt $K$ alle geschätzten Parameter, die in die AIC-Berechnung eingehen.

| Modell | Terme | K | Log-Likelihood |
| --- | --- | --- | --- |
| M1 | Stunden begleiteter Übung | 3 | -155.0 |
| M2 | Stunden begleiteter Übung + Punktwert der vorherigen Vorbereitung | 4 | -146.0 |
| M3 | Stunden begleiteter Übung + Punktwert der vorherigen Vorbereitung + Zahl der Reflexionssitzungen | 5 | -142.5 |
| M4 | Stunden begleiteter Übung + Punktwert der vorherigen Vorbereitung + Zahl der Reflexionssitzungen + ein vorab festgelegter Produktterm | 6 | -141.9 |

(a) Berechne für jedes Modell $AIC=-2\log(L)+2K$ und berechne jedes $\Delta AIC=AIC-AIC_{min}$. (b) Führe ausgehend von M1 eine Vorwärtsselektion mit der schrittspezifischen Kandidatentabelle durch. Wähle in jedem Schritt den kleinsten verfügbaren AIC nur dann, wenn er kleiner als beim aktuellen Modell ist. Stoppe andernfalls.

| Vorwärtsschritt | Mögliche Aktion | AIC |
| --- | --- | --- |
| Schritt 1 | Punktwert der vorherigen Vorbereitung hinzufügen | 300.00 |
| Schritt 1 | Zahl der Reflexionssitzungen hinzufügen | 303.20 |
| Schritt 1 | Produktterm hinzufügen | 306.40 |
| Schritt 2 | nach M2 stoppen | 300.00 |
| Schritt 2 | Zahl der Reflexionssitzungen hinzufügen | 295.00 |
| Schritt 2 | Produktterm hinzufügen | 297.80 |
| Schritt 3 | nach M3 stoppen | 295.00 |
| Schritt 3 | Produktterm hinzufügen | 295.80 |

(c) Zeichne den AIC-Pfad der tatsächlich ausgewählten Modelle. Beginne mit M1 bei Schritt 0. (d) Schreibe die endgültige Modellformel auf und interpretiere, was die ausgewählten Terme zum angepassten Zusammenhang beitragen. (e) Erkläre, weshalb der Pfad von früheren Entscheidungen abhängt und weshalb das endgültige Modell dadurch weder als wahr oder kausal bewiesen ist noch nachweislich ausserhalb der Stichprobe vorhersagt.

### T07-A05-V02: Arbeitsablauf im Archiv und Suchzeit

**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel oder das erwartete Muster, das die Berechnung begründet.

Vier konstruierte, vorab festgelegte Kandidatenmodelle verwenden genau dieselben Fälle und dieselbe Ergebnisvariable „Suchzeit“. Hier ist $\log(L)$ die vom angepassten Modell berichtete maximierte Log-Likelihood. Nach der angegebenen Konvention zählt $K$ alle geschätzten Parameter, die in die AIC-Berechnung eingehen.

| Modell | Terme | K | Log-Likelihood |
| --- | --- | --- | --- |
| M1 | Übungssitzungen mit Checkliste | 3 | -142.0 |
| M2 | Übungssitzungen mit Checkliste + Monate Archiverfahrung | 4 | -134.0 |
| M3 | Übungssitzungen mit Checkliste + Monate Archiverfahrung + Punktwert zur Katalogvertrautheit | 5 | -133.4 |
| M4 | Übungssitzungen mit Checkliste + Monate Archiverfahrung + Punktwert zur Katalogvertrautheit + ein vorab festgelegter Produktterm | 6 | -131.8 |

(a) Berechne für jedes Modell $AIC=-2\log(L)+2K$ und berechne jedes $\Delta AIC=AIC-AIC_{min}$. (b) Führe ausgehend von M1 eine Vorwärtsselektion mit der schrittspezifischen Kandidatentabelle durch. Wähle in jedem Schritt den kleinsten verfügbaren AIC nur dann, wenn er kleiner als beim aktuellen Modell ist. Stoppe andernfalls.

| Vorwärtsschritt | Mögliche Aktion | AIC |
| --- | --- | --- |
| Schritt 1 | Monate Archiverfahrung hinzufügen | 276.00 |
| Schritt 1 | Punktwert zur Katalogvertrautheit hinzufügen | 279.20 |
| Schritt 1 | Produktterm hinzufügen | 282.40 |
| Schritt 2 | nach M2 stoppen | 276.00 |
| Schritt 2 | Punktwert zur Katalogvertrautheit hinzufügen | 276.80 |
| Schritt 2 | Produktterm hinzufügen | 279.60 |
| Schritt 3 | nach M3 stoppen | 276.80 |
| Schritt 3 | Produktterm hinzufügen | 275.60 |

(c) Zeichne den AIC-Pfad der tatsächlich ausgewählten Modelle. Beginne mit M1 bei Schritt 0. (d) Schreibe die endgültige Modellformel auf und interpretiere, was die ausgewählten Terme zum angepassten Zusammenhang beitragen. (e) Erkläre, weshalb der Pfad von früheren Entscheidungen abhängt und weshalb das endgültige Modell dadurch weder als wahr oder kausal bewiesen ist noch nachweislich ausserhalb der Stichprobe vorhersagt.

### T07-A05-V03: Leseroutinen und Textverständnis

**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel oder das erwartete Muster, das die Berechnung begründet.

Vier konstruierte, vorab festgelegte Kandidatenmodelle verwenden genau dieselben Fälle und dieselbe Ergebnisvariable „Punktwert im Textverständnis“. Hier ist $\log(L)$ die vom angepassten Modell berichtete maximierte Log-Likelihood. Nach der angegebenen Konvention zählt $K$ alle geschätzten Parameter, die in die AIC-Berechnung eingehen.

| Modell | Terme | K | Log-Likelihood |
| --- | --- | --- | --- |
| M1 | wöchentliche Lesestunden | 3 | -180.0 |
| M2 | wöchentliche Lesestunden + Ausgangswert des Wortschatzes | 4 | -170.0 |
| M3 | wöchentliche Lesestunden + Ausgangswert des Wortschatzes + Zahl der Annotationssitzungen | 5 | -166.0 |
| M4 | wöchentliche Lesestunden + Ausgangswert des Wortschatzes + Zahl der Annotationssitzungen + ein vorab festgelegter Produktterm | 6 | -165.5 |

(a) Berechne für jedes Modell $AIC=-2\log(L)+2K$ und berechne jedes $\Delta AIC=AIC-AIC_{min}$. (b) Führe ausgehend von M1 eine Vorwärtsselektion mit der schrittspezifischen Kandidatentabelle durch. Wähle in jedem Schritt den kleinsten verfügbaren AIC nur dann, wenn er kleiner als beim aktuellen Modell ist. Stoppe andernfalls.

| Vorwärtsschritt | Mögliche Aktion | AIC |
| --- | --- | --- |
| Schritt 1 | Ausgangswert des Wortschatzes hinzufügen | 348.00 |
| Schritt 1 | Zahl der Annotationssitzungen hinzufügen | 351.20 |
| Schritt 1 | Produktterm hinzufügen | 354.40 |
| Schritt 2 | nach M2 stoppen | 348.00 |
| Schritt 2 | Zahl der Annotationssitzungen hinzufügen | 342.00 |
| Schritt 2 | Produktterm hinzufügen | 344.80 |
| Schritt 3 | nach M3 stoppen | 342.00 |
| Schritt 3 | Produktterm hinzufügen | 343.00 |

(c) Zeichne den AIC-Pfad der tatsächlich ausgewählten Modelle. Beginne mit M1 bei Schritt 0. (d) Schreibe die endgültige Modellformel auf und interpretiere, was die ausgewählten Terme zum angepassten Zusammenhang beitragen. (e) Erkläre, weshalb der Pfad von früheren Entscheidungen abhängt und weshalb das endgültige Modell dadurch weder als wahr oder kausal bewiesen ist noch nachweislich ausserhalb der Stichprobe vorhersagt.

### T07-A05-V04: Streckenübung und Navigationszeit

**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel oder das erwartete Muster, das die Berechnung begründet.

Vier konstruierte, vorab festgelegte Kandidatenmodelle verwenden genau dieselben Fälle und dieselbe Ergebnisvariable „Navigationszeit“. Hier ist $\log(L)$ die vom angepassten Modell berichtete maximierte Log-Likelihood. Nach der angegebenen Konvention zählt $K$ alle geschätzten Parameter, die in die AIC-Berechnung eingehen.

| Modell | Terme | K | Log-Likelihood |
| --- | --- | --- | --- |
| M1 | Versuche zur Streckenübung | 3 | -130.0 |
| M2 | Versuche zur Streckenübung + Punktwert der Streckenkenntnis | 4 | -126.0 |
| M3 | Versuche zur Streckenübung + Punktwert der Streckenkenntnis + Punktwert zur Erinnerung an Orientierungspunkte | 5 | -125.5 |
| M4 | Versuche zur Streckenübung + Punktwert der Streckenkenntnis + Punktwert zur Erinnerung an Orientierungspunkte + ein vorab festgelegter Produktterm | 6 | -125.2 |

(a) Berechne für jedes Modell $AIC=-2\log(L)+2K$ und berechne jedes $\Delta AIC=AIC-AIC_{min}$. (b) Führe ausgehend von M1 eine Vorwärtsselektion mit der schrittspezifischen Kandidatentabelle durch. Wähle in jedem Schritt den kleinsten verfügbaren AIC nur dann, wenn er kleiner als beim aktuellen Modell ist. Stoppe andernfalls.

| Vorwärtsschritt | Mögliche Aktion | AIC |
| --- | --- | --- |
| Schritt 1 | Punktwert der Streckenkenntnis hinzufügen | 260.00 |
| Schritt 1 | Punktwert zur Erinnerung an Orientierungspunkte hinzufügen | 263.20 |
| Schritt 1 | Produktterm hinzufügen | 266.40 |
| Schritt 2 | nach M2 stoppen | 260.00 |
| Schritt 2 | Punktwert zur Erinnerung an Orientierungspunkte hinzufügen | 261.00 |
| Schritt 2 | Produktterm hinzufügen | 263.80 |
| Schritt 3 | nach M3 stoppen | 261.00 |
| Schritt 3 | Produktterm hinzufügen | 262.40 |

(c) Zeichne den AIC-Pfad der tatsächlich ausgewählten Modelle. Beginne mit M1 bei Schritt 0. (d) Schreibe die endgültige Modellformel auf und interpretiere, was die ausgewählten Terme zum angepassten Zusammenhang beitragen. (e) Erkläre, weshalb der Pfad von früheren Entscheidungen abhängt und weshalb das endgültige Modell dadurch weder als wahr oder kausal bewiesen ist noch nachweislich ausserhalb der Stichprobe vorhersagt.

### T07-A05-V05: Suchübung und Kataloggenauigkeit

**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel oder das erwartete Muster, das die Berechnung begründet.

Vier konstruierte, vorab festgelegte Kandidatenmodelle verwenden genau dieselben Fälle und dieselbe Ergebnisvariable „Punktwert der Kataloggenauigkeit“. Hier ist $\log(L)$ die vom angepassten Modell berichtete maximierte Log-Likelihood. Nach der angegebenen Konvention zählt $K$ alle geschätzten Parameter, die in die AIC-Berechnung eingehen.

| Modell | Terme | K | Log-Likelihood |
| --- | --- | --- | --- |
| M1 | Suchübungsblöcke | 3 | -200.0 |
| M2 | Suchübungsblöcke + Punktwert des Katalogvorwissens | 4 | -188.0 |
| M3 | Suchübungsblöcke + Punktwert des Katalogvorwissens + Punktwert der Suchplanung | 5 | -183.0 |
| M4 | Suchübungsblöcke + Punktwert des Katalogvorwissens + Punktwert der Suchplanung + ein vorab festgelegter Produktterm | 6 | -180.0 |

(a) Berechne für jedes Modell $AIC=-2\log(L)+2K$ und berechne jedes $\Delta AIC=AIC-AIC_{min}$. (b) Führe ausgehend von M1 eine Vorwärtsselektion mit der schrittspezifischen Kandidatentabelle durch. Wähle in jedem Schritt den kleinsten verfügbaren AIC nur dann, wenn er kleiner als beim aktuellen Modell ist. Stoppe andernfalls.

| Vorwärtsschritt | Mögliche Aktion | AIC |
| --- | --- | --- |
| Schritt 1 | Punktwert des Katalogvorwissens hinzufügen | 384.00 |
| Schritt 1 | Punktwert der Suchplanung hinzufügen | 387.20 |
| Schritt 1 | Produktterm hinzufügen | 390.40 |
| Schritt 2 | nach M2 stoppen | 384.00 |
| Schritt 2 | Punktwert der Suchplanung hinzufügen | 376.00 |
| Schritt 2 | Produktterm hinzufügen | 378.80 |
| Schritt 3 | nach M3 stoppen | 376.00 |
| Schritt 3 | Produktterm hinzufügen | 372.00 |

(c) Zeichne den AIC-Pfad der tatsächlich ausgewählten Modelle. Beginne mit M1 bei Schritt 0. (d) Schreibe die endgültige Modellformel auf und interpretiere, was die ausgewählten Terme zum angepassten Zusammenhang beitragen. (e) Erkläre, weshalb der Pfad von früheren Entscheidungen abhängt und weshalb das endgültige Modell dadurch weder als wahr oder kausal bewiesen ist noch nachweislich ausserhalb der Stichprobe vorhersagt.

### T07-A05-V06: Workshopteilnahme und Selbstvertrauen

**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel oder das erwartete Muster, das die Berechnung begründet.

Vier konstruierte, vorab festgelegte Kandidatenmodelle verwenden genau dieselben Fälle und dieselbe Ergebnisvariable „Punktwert des Selbstvertrauens“. Hier ist $\log(L)$ die vom angepassten Modell berichtete maximierte Log-Likelihood. Nach der angegebenen Konvention zählt $K$ alle geschätzten Parameter, die in die AIC-Berechnung eingehen.

| Modell | Terme | K | Log-Likelihood |
| --- | --- | --- | --- |
| M1 | Workshopsitzungen | 3 | -165.0 |
| M2 | Workshopsitzungen + Ausgangswert des Selbstvertrauens | 4 | -157.0 |
| M3 | Workshopsitzungen + Ausgangswert des Selbstvertrauens + Zahl der Reflexionsprotokolle | 5 | -156.4 |
| M4 | Workshopsitzungen + Ausgangswert des Selbstvertrauens + Zahl der Reflexionsprotokolle + ein vorab festgelegter Produktterm | 6 | -155.8 |

(a) Berechne für jedes Modell $AIC=-2\log(L)+2K$ und berechne jedes $\Delta AIC=AIC-AIC_{min}$. (b) Führe ausgehend von M1 eine Vorwärtsselektion mit der schrittspezifischen Kandidatentabelle durch. Wähle in jedem Schritt den kleinsten verfügbaren AIC nur dann, wenn er kleiner als beim aktuellen Modell ist. Stoppe andernfalls.

| Vorwärtsschritt | Mögliche Aktion | AIC |
| --- | --- | --- |
| Schritt 1 | Ausgangswert des Selbstvertrauens hinzufügen | 322.00 |
| Schritt 1 | Zahl der Reflexionsprotokolle hinzufügen | 325.20 |
| Schritt 1 | Produktterm hinzufügen | 328.40 |
| Schritt 2 | nach M2 stoppen | 322.00 |
| Schritt 2 | Zahl der Reflexionsprotokolle hinzufügen | 322.80 |
| Schritt 2 | Produktterm hinzufügen | 325.60 |
| Schritt 3 | nach M3 stoppen | 322.80 |
| Schritt 3 | Produktterm hinzufügen | 323.60 |

(c) Zeichne den AIC-Pfad der tatsächlich ausgewählten Modelle. Beginne mit M1 bei Schritt 0. (d) Schreibe die endgültige Modellformel auf und interpretiere, was die ausgewählten Terme zum angepassten Zusammenhang beitragen. (e) Erkläre, weshalb der Pfad von früheren Entscheidungen abhängt und weshalb das endgültige Modell dadurch weder als wahr oder kausal bewiesen ist noch nachweislich ausserhalb der Stichprobe vorhersagt.

### T07-A05-V07: Konzentrationsblöcke und Aufgabengenauigkeit

**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel oder das erwartete Muster, das die Berechnung begründet.

Vier konstruierte, vorab festgelegte Kandidatenmodelle verwenden genau dieselben Fälle und dieselbe Ergebnisvariable „Punktwert der Aufgabengenauigkeit“. Hier ist $\log(L)$ die vom angepassten Modell berichtete maximierte Log-Likelihood. Nach der angegebenen Konvention zählt $K$ alle geschätzten Parameter, die in die AIC-Berechnung eingehen.

| Modell | Terme | K | Log-Likelihood |
| --- | --- | --- | --- |
| M1 | benachrichtigungsfreie Blöcke | 3 | -175.0 |
| M2 | benachrichtigungsfreie Blöcke + Schlafdauer in Stunden | 4 | -166.0 |
| M3 | benachrichtigungsfreie Blöcke + Schlafdauer in Stunden + Zahl der Planungspausen | 5 | -162.0 |
| M4 | benachrichtigungsfreie Blöcke + Schlafdauer in Stunden + Zahl der Planungspausen + ein vorab festgelegter Produktterm | 6 | -161.2 |

(a) Berechne für jedes Modell $AIC=-2\log(L)+2K$ und berechne jedes $\Delta AIC=AIC-AIC_{min}$. (b) Führe ausgehend von M1 eine Vorwärtsselektion mit der schrittspezifischen Kandidatentabelle durch. Wähle in jedem Schritt den kleinsten verfügbaren AIC nur dann, wenn er kleiner als beim aktuellen Modell ist. Stoppe andernfalls.

| Vorwärtsschritt | Mögliche Aktion | AIC |
| --- | --- | --- |
| Schritt 1 | Schlafdauer in Stunden hinzufügen | 340.00 |
| Schritt 1 | Zahl der Planungspausen hinzufügen | 343.20 |
| Schritt 1 | Produktterm hinzufügen | 346.40 |
| Schritt 2 | nach M2 stoppen | 340.00 |
| Schritt 2 | Zahl der Planungspausen hinzufügen | 334.00 |
| Schritt 2 | Produktterm hinzufügen | 336.80 |
| Schritt 3 | nach M3 stoppen | 334.00 |
| Schritt 3 | Produktterm hinzufügen | 334.40 |

(c) Zeichne den AIC-Pfad der tatsächlich ausgewählten Modelle. Beginne mit M1 bei Schritt 0. (d) Schreibe die endgültige Modellformel auf und interpretiere, was die ausgewählten Terme zum angepassten Zusammenhang beitragen. (e) Erkläre, weshalb der Pfad von früheren Entscheidungen abhängt und weshalb das endgültige Modell dadurch weder als wahr oder kausal bewiesen ist noch nachweislich ausserhalb der Stichprobe vorhersagt.

### T07-A05-V08: Museumsbesuche und historisches Wissen

**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel oder das erwartete Muster, das die Berechnung begründet.

Vier konstruierte, vorab festgelegte Kandidatenmodelle verwenden genau dieselben Fälle und dieselbe Ergebnisvariable „Punktwert des historischen Wissens“. Hier ist $\log(L)$ die vom angepassten Modell berichtete maximierte Log-Likelihood. Nach der angegebenen Konvention zählt $K$ alle geschätzten Parameter, die in die AIC-Berechnung eingehen.

| Modell | Terme | K | Log-Likelihood |
| --- | --- | --- | --- |
| M1 | Museumsbesuche | 3 | -145.0 |
| M2 | Museumsbesuche + Punktwert des geschichtlichen Vorwissens | 4 | -140.0 |
| M3 | Museumsbesuche + Punktwert des geschichtlichen Vorwissens + Zahl der Ausstellungsnotizen | 5 | -138.0 |
| M4 | Museumsbesuche + Punktwert des geschichtlichen Vorwissens + Zahl der Ausstellungsnotizen + ein vorab festgelegter Produktterm | 6 | -136.4 |

(a) Berechne für jedes Modell $AIC=-2\log(L)+2K$ und berechne jedes $\Delta AIC=AIC-AIC_{min}$. (b) Führe ausgehend von M1 eine Vorwärtsselektion mit der schrittspezifischen Kandidatentabelle durch. Wähle in jedem Schritt den kleinsten verfügbaren AIC nur dann, wenn er kleiner als beim aktuellen Modell ist. Stoppe andernfalls.

| Vorwärtsschritt | Mögliche Aktion | AIC |
| --- | --- | --- |
| Schritt 1 | Punktwert des geschichtlichen Vorwissens hinzufügen | 288.00 |
| Schritt 1 | Zahl der Ausstellungsnotizen hinzufügen | 291.20 |
| Schritt 1 | Produktterm hinzufügen | 294.40 |
| Schritt 2 | nach M2 stoppen | 288.00 |
| Schritt 2 | Zahl der Ausstellungsnotizen hinzufügen | 286.00 |
| Schritt 2 | Produktterm hinzufügen | 288.80 |
| Schritt 3 | nach M3 stoppen | 286.00 |
| Schritt 3 | Produktterm hinzufügen | 284.80 |

(c) Zeichne den AIC-Pfad der tatsächlich ausgewählten Modelle. Beginne mit M1 bei Schritt 0. (d) Schreibe die endgültige Modellformel auf und interpretiere, was die ausgewählten Terme zum angepassten Zusammenhang beitragen. (e) Erkläre, weshalb der Pfad von früheren Entscheidungen abhängt und weshalb das endgültige Modell dadurch weder als wahr oder kausal bewiesen ist noch nachweislich ausserhalb der Stichprobe vorhersagt.

### T07-A05-V09: Peer-Feedback und Überarbeitungsqualität

**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel oder das erwartete Muster, das die Berechnung begründet.

Vier konstruierte, vorab festgelegte Kandidatenmodelle verwenden genau dieselben Fälle und dieselbe Ergebnisvariable „Punktwert der Überarbeitungsqualität“. Hier ist $\log(L)$ die vom angepassten Modell berichtete maximierte Log-Likelihood. Nach der angegebenen Konvention zählt $K$ alle geschätzten Parameter, die in die AIC-Berechnung eingehen.

| Modell | Terme | K | Log-Likelihood |
| --- | --- | --- | --- |
| M1 | Runden mit Peer-Feedback | 3 | -190.0 |
| M2 | Runden mit Peer-Feedback + Ausgangswert der Schreibqualität | 4 | -181.0 |
| M3 | Runden mit Peer-Feedback + Ausgangswert der Schreibqualität + Punktwert des Überarbeitungsplans | 5 | -180.3 |
| M4 | Runden mit Peer-Feedback + Ausgangswert der Schreibqualität + Punktwert des Überarbeitungsplans + ein vorab festgelegter Produktterm | 6 | -179.9 |

(a) Berechne für jedes Modell $AIC=-2\log(L)+2K$ und berechne jedes $\Delta AIC=AIC-AIC_{min}$. (b) Führe ausgehend von M1 eine Vorwärtsselektion mit der schrittspezifischen Kandidatentabelle durch. Wähle in jedem Schritt den kleinsten verfügbaren AIC nur dann, wenn er kleiner als beim aktuellen Modell ist. Stoppe andernfalls.

| Vorwärtsschritt | Mögliche Aktion | AIC |
| --- | --- | --- |
| Schritt 1 | Ausgangswert der Schreibqualität hinzufügen | 370.00 |
| Schritt 1 | Punktwert des Überarbeitungsplans hinzufügen | 373.20 |
| Schritt 1 | Produktterm hinzufügen | 376.40 |
| Schritt 2 | nach M2 stoppen | 370.00 |
| Schritt 2 | Punktwert des Überarbeitungsplans hinzufügen | 370.60 |
| Schritt 2 | Produktterm hinzufügen | 373.40 |
| Schritt 3 | nach M3 stoppen | 370.60 |
| Schritt 3 | Produktterm hinzufügen | 371.80 |

(c) Zeichne den AIC-Pfad der tatsächlich ausgewählten Modelle. Beginne mit M1 bei Schritt 0. (d) Schreibe die endgültige Modellformel auf und interpretiere, was die ausgewählten Terme zum angepassten Zusammenhang beitragen. (e) Erkläre, weshalb der Pfad von früheren Entscheidungen abhängt und weshalb das endgültige Modell dadurch weder als wahr oder kausal bewiesen ist noch nachweislich ausserhalb der Stichprobe vorhersagt.

### T07-A05-V10: Planungssitzungen und Bearbeitungszeit

**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel oder das erwartete Muster, das die Berechnung begründet.

Vier konstruierte, vorab festgelegte Kandidatenmodelle verwenden genau dieselben Fälle und dieselbe Ergebnisvariable „Bearbeitungszeit“. Hier ist $\log(L)$ die vom angepassten Modell berichtete maximierte Log-Likelihood. Nach der angegebenen Konvention zählt $K$ alle geschätzten Parameter, die in die AIC-Berechnung eingehen.

| Modell | Terme | K | Log-Likelihood |
| --- | --- | --- | --- |
| M1 | Planungssitzungen | 3 | -158.0 |
| M2 | Planungssitzungen + Punktwert der Aufgabenkomplexität | 4 | -149.0 |
| M3 | Planungssitzungen + Punktwert der Aufgabenkomplexität + Zahl der Fortschrittskontrollen | 5 | -145.0 |
| M4 | Planungssitzungen + Punktwert der Aufgabenkomplexität + Zahl der Fortschrittskontrollen + ein vorab festgelegter Produktterm | 6 | -144.4 |

(a) Berechne für jedes Modell $AIC=-2\log(L)+2K$ und berechne jedes $\Delta AIC=AIC-AIC_{min}$. (b) Führe ausgehend von M1 eine Vorwärtsselektion mit der schrittspezifischen Kandidatentabelle durch. Wähle in jedem Schritt den kleinsten verfügbaren AIC nur dann, wenn er kleiner als beim aktuellen Modell ist. Stoppe andernfalls.

| Vorwärtsschritt | Mögliche Aktion | AIC |
| --- | --- | --- |
| Schritt 1 | Punktwert der Aufgabenkomplexität hinzufügen | 306.00 |
| Schritt 1 | Zahl der Fortschrittskontrollen hinzufügen | 309.20 |
| Schritt 1 | Produktterm hinzufügen | 312.40 |
| Schritt 2 | nach M2 stoppen | 306.00 |
| Schritt 2 | Zahl der Fortschrittskontrollen hinzufügen | 300.00 |
| Schritt 2 | Produktterm hinzufügen | 302.80 |
| Schritt 3 | nach M3 stoppen | 300.00 |
| Schritt 3 | Produktterm hinzufügen | 300.80 |

(c) Zeichne den AIC-Pfad der tatsächlich ausgewählten Modelle. Beginne mit M1 bei Schritt 0. (d) Schreibe die endgültige Modellformel auf und interpretiere, was die ausgewählten Terme zum angepassten Zusammenhang beitragen. (e) Erkläre, weshalb der Pfad von früheren Entscheidungen abhängt und weshalb das endgültige Modell dadurch weder als wahr oder kausal bewiesen ist noch nachweislich ausserhalb der Stichprobe vorhersagt.

## A07: Ein additives Gruppenmodell interpretieren

### T07-A07-V01: Lernbegleitung und statistisches Denken

**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel oder das erwartete Muster, das die Berechnung begründet.

Ein konstruiertes additives Modell verwendet $G=0$ für die Gruppe „Ohne Lernbegleitung“ und $G=1$ für die Gruppe „Mit Lernbegleitung“: $\hat Y=42.00+(3.00)X+(5.00)G$. Dabei bezeichnet $Y$ die Ergebnisvariable „Punktwert im statistischen Denken“ und $X$ den Prädiktor „Übungsstunden“.

(a) Schreibe die angepasste Gleichung für jede Gruppe auf und interpretiere den Achsenabschnitt bei $X=0$. Weise darauf hin, wenn null lediglich eine mathematische Referenz sein könnte. (b) Interpretiere die gemeinsame $X$-Steigung und den Gruppenkoeffizienten als bedingte Vergleiche. (c) Berechne die angepassten Koordinaten beider Gruppen bei $X=2.0$ und $X=6.0$ und ordne sie in einer Tabelle. (d) Erkläre anhand dieser Koordinaten, weshalb die Linien parallel sind und der Gruppenabstand konstant bleibt. Begründe zudem, weshalb der angepasste Abstand allein keinen kausalen Gruppeneffekt belegt.

### T07-A07-V02: Archiverfahrung und Suche

**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel oder das erwartete Muster, das die Berechnung begründet.

Ein konstruiertes additives Modell verwendet $G=0$ für die Gruppe „Neue Mitarbeitende“ und $G=1$ für die Gruppe „Erfahrene Mitarbeitende“: $\hat Y=36.00+(-1.80)X+(-4.00)G$. Dabei bezeichnet $Y$ die Ergebnisvariable „Suchzeit“ und $X$ den Prädiktor „Übungssitzungen“.

(a) Schreibe die angepasste Gleichung für jede Gruppe auf und interpretiere den Achsenabschnitt bei $X=0$. Weise darauf hin, wenn null lediglich eine mathematische Referenz sein könnte. (b) Interpretiere die gemeinsame $X$-Steigung und den Gruppenkoeffizienten als bedingte Vergleiche. (c) Berechne die angepassten Koordinaten beider Gruppen bei $X=1.0$ und $X=5.0$ und ordne sie in einer Tabelle. (d) Erkläre anhand dieser Koordinaten, weshalb die Linien parallel sind und der Gruppenabstand konstant bleibt. Begründe zudem, weshalb der angepasste Abstand allein keinen kausalen Gruppeneffekt belegt.

### T07-A07-V03: Leseformat und Textverständnis

**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel oder das erwartete Muster, das die Berechnung begründet.

Ein konstruiertes additives Modell verwendet $G=0$ für die Gruppe „Gedruckt“ und $G=1$ für die Gruppe „Digital“: $\hat Y=51.00+(2.20)X+(-2.50)G$. Dabei bezeichnet $Y$ die Ergebnisvariable „Punktwert im Textverständnis“ und $X$ den Prädiktor „Lesestunden“.

(a) Schreibe die angepasste Gleichung für jede Gruppe auf und interpretiere den Achsenabschnitt bei $X=0$. Weise darauf hin, wenn null lediglich eine mathematische Referenz sein könnte. (b) Interpretiere die gemeinsame $X$-Steigung und den Gruppenkoeffizienten als bedingte Vergleiche. (c) Berechne die angepassten Koordinaten beider Gruppen bei $X=2.0$ und $X=7.0$ und ordne sie in einer Tabelle. (d) Erkläre anhand dieser Koordinaten, weshalb die Linien parallel sind und der Gruppenabstand konstant bleibt. Begründe zudem, weshalb der angepasste Abstand allein keinen kausalen Gruppeneffekt belegt.

### T07-A07-V04: Streckenhilfe und Navigation

**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel oder das erwartete Muster, das die Berechnung begründet.

Ein konstruiertes additives Modell verwendet $G=0$ für die Gruppe „Papierkarte“ und $G=1$ für die Gruppe „Karten-App“: $\hat Y=44.00+(-2.00)X+(-3.00)G$. Dabei bezeichnet $Y$ die Ergebnisvariable „Navigationszeit“ und $X$ den Prädiktor „Übungsversuche“.

(a) Schreibe die angepasste Gleichung für jede Gruppe auf und interpretiere den Achsenabschnitt bei $X=0$. Weise darauf hin, wenn null lediglich eine mathematische Referenz sein könnte. (b) Interpretiere die gemeinsame $X$-Steigung und den Gruppenkoeffizienten als bedingte Vergleiche. (c) Berechne die angepassten Koordinaten beider Gruppen bei $X=1.0$ und $X=4.0$ und ordne sie in einer Tabelle. (d) Erkläre anhand dieser Koordinaten, weshalb die Linien parallel sind und der Gruppenabstand konstant bleibt. Begründe zudem, weshalb der angepasste Abstand allein keinen kausalen Gruppeneffekt belegt.

### T07-A07-V05: Suchhilfe und Genauigkeit

**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel oder das erwartete Muster, das die Berechnung begründet.

Ein konstruiertes additives Modell verwendet $G=0$ für die Gruppe „Keine Hilfe“ und $G=1$ für die Gruppe „Checkliste“: $\hat Y=55.00+(2.50)X+(4.00)G$. Dabei bezeichnet $Y$ die Ergebnisvariable „Punktwert der Genauigkeit“ und $X$ den Prädiktor „Übungsblöcke“.

(a) Schreibe die angepasste Gleichung für jede Gruppe auf und interpretiere den Achsenabschnitt bei $X=0$. Weise darauf hin, wenn null lediglich eine mathematische Referenz sein könnte. (b) Interpretiere die gemeinsame $X$-Steigung und den Gruppenkoeffizienten als bedingte Vergleiche. (c) Berechne die angepassten Koordinaten beider Gruppen bei $X=0.0$ und $X=4.0$ und ordne sie in einer Tabelle. (d) Erkläre anhand dieser Koordinaten, weshalb die Linien parallel sind und der Gruppenabstand konstant bleibt. Begründe zudem, weshalb der angepasste Abstand allein keinen kausalen Gruppeneffekt belegt.

### T07-A07-V06: Workshopformat und Selbstvertrauen

**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel oder das erwartete Muster, das die Berechnung begründet.

Ein konstruiertes additives Modell verwendet $G=0$ für die Gruppe „Online“ und $G=1$ für die Gruppe „Vor Ort“: $\hat Y=38.00+(3.20)X+(3.50)G$. Dabei bezeichnet $Y$ die Ergebnisvariable „Punktwert des Selbstvertrauens“ und $X$ den Prädiktor „besuchte Sitzungen“.

(a) Schreibe die angepasste Gleichung für jede Gruppe auf und interpretiere den Achsenabschnitt bei $X=0$. Weise darauf hin, wenn null lediglich eine mathematische Referenz sein könnte. (b) Interpretiere die gemeinsame $X$-Steigung und den Gruppenkoeffizienten als bedingte Vergleiche. (c) Berechne die angepassten Koordinaten beider Gruppen bei $X=1.0$ und $X=5.0$ und ordne sie in einer Tabelle. (d) Erkläre anhand dieser Koordinaten, weshalb die Linien parallel sind und der Gruppenabstand konstant bleibt. Begründe zudem, weshalb der angepasste Abstand allein keinen kausalen Gruppeneffekt belegt.

### T07-A07-V07: Konzentrationsumgebung und Genauigkeit

**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel oder das erwartete Muster, das die Berechnung begründet.

Ein konstruiertes additives Modell verwendet $G=0$ für die Gruppe „Gemeinschaftsraum“ und $G=1$ für die Gruppe „Ruhiger Raum“: $\hat Y=60.00+(1.70)X+(4.50)G$. Dabei bezeichnet $Y$ die Ergebnisvariable „Punktwert der Aufgabengenauigkeit“ und $X$ den Prädiktor „Konzentrationsblöcke“.

(a) Schreibe die angepasste Gleichung für jede Gruppe auf und interpretiere den Achsenabschnitt bei $X=0$. Weise darauf hin, wenn null lediglich eine mathematische Referenz sein könnte. (b) Interpretiere die gemeinsame $X$-Steigung und den Gruppenkoeffizienten als bedingte Vergleiche. (c) Berechne die angepassten Koordinaten beider Gruppen bei $X=2.0$ und $X=8.0$ und ordne sie in einer Tabelle. (d) Erkläre anhand dieser Koordinaten, weshalb die Linien parallel sind und der Gruppenabstand konstant bleibt. Begründe zudem, weshalb der angepasste Abstand allein keinen kausalen Gruppeneffekt belegt.

### T07-A07-V08: Museumsführung und Wissen

**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel oder das erwartete Muster, das die Berechnung begründet.

Ein konstruiertes additives Modell verwendet $G=0$ für die Gruppe „Selbstständig“ und $G=1$ für die Gruppe „Geführt“: $\hat Y=47.00+(4.00)X+(6.00)G$. Dabei bezeichnet $Y$ die Ergebnisvariable „Punktwert des Wissens“ und $X$ den Prädiktor „Besuche“.

(a) Schreibe die angepasste Gleichung für jede Gruppe auf und interpretiere den Achsenabschnitt bei $X=0$. Weise darauf hin, wenn null lediglich eine mathematische Referenz sein könnte. (b) Interpretiere die gemeinsame $X$-Steigung und den Gruppenkoeffizienten als bedingte Vergleiche. (c) Berechne die angepassten Koordinaten beider Gruppen bei $X=0.0$ und $X=3.0$ und ordne sie in einer Tabelle. (d) Erkläre anhand dieser Koordinaten, weshalb die Linien parallel sind und der Gruppenabstand konstant bleibt. Begründe zudem, weshalb der angepasste Abstand allein keinen kausalen Gruppeneffekt belegt.

### T07-A07-V09: Feedbackformat und Überarbeitung

**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel oder das erwartete Muster, das die Berechnung begründet.

Ein konstruiertes additives Modell verwendet $G=0$ für die Gruppe „Schriftlich“ und $G=1$ für die Gruppe „Gespräch“: $\hat Y=52.00+(3.50)X+(2.00)G$. Dabei bezeichnet $Y$ die Ergebnisvariable „Punktwert der Überarbeitung“ und $X$ den Prädiktor „Feedbackrunden“.

(a) Schreibe die angepasste Gleichung für jede Gruppe auf und interpretiere den Achsenabschnitt bei $X=0$. Weise darauf hin, wenn null lediglich eine mathematische Referenz sein könnte. (b) Interpretiere die gemeinsame $X$-Steigung und den Gruppenkoeffizienten als bedingte Vergleiche. (c) Berechne die angepassten Koordinaten beider Gruppen bei $X=1.0$ und $X=4.0$ und ordne sie in einer Tabelle. (d) Erkläre anhand dieser Koordinaten, weshalb die Linien parallel sind und der Gruppenabstand konstant bleibt. Begründe zudem, weshalb der angepasste Abstand allein keinen kausalen Gruppeneffekt belegt.

### T07-A07-V10: Planungsformat und Abschluss

**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel oder das erwartete Muster, das die Berechnung begründet.

Ein konstruiertes additives Modell verwendet $G=0$ für die Gruppe „Papier“ und $G=1$ für die Gruppe „Digital“: $\hat Y=70.00+(-2.40)X+(-3.50)G$. Dabei bezeichnet $Y$ die Ergebnisvariable „Bearbeitungszeit“ und $X$ den Prädiktor „Planungssitzungen“.

(a) Schreibe die angepasste Gleichung für jede Gruppe auf und interpretiere den Achsenabschnitt bei $X=0$. Weise darauf hin, wenn null lediglich eine mathematische Referenz sein könnte. (b) Interpretiere die gemeinsame $X$-Steigung und den Gruppenkoeffizienten als bedingte Vergleiche. (c) Berechne die angepassten Koordinaten beider Gruppen bei $X=1.0$ und $X=6.0$ und ordne sie in einer Tabelle. (d) Erkläre anhand dieser Koordinaten, weshalb die Linien parallel sind und der Gruppenabstand konstant bleibt. Begründe zudem, weshalb der angepasste Abstand allein keinen kausalen Gruppeneffekt belegt.

## A08: Die Referenz wechseln, ohne angepasste Beziehungen zu verändern

### T07-A08-V01: Übungsformat neu referenzieren

**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel oder das erwartete Muster, das die Berechnung begründet.

Ein konstruiertes additives Modell codiert $G=0$ für die Gruppe „Allein“ und $G=1$ für die Gruppe „Zu zweit“: $\hat Y=40.00+(2.80)X+(4.50)G$. Dabei bezeichnet $Y$ die Ergebnisvariable „Punktwert im statistischen Denken“ und $X$ den Prädiktor „Übungsstunden“. Codiere neu mit $H=0$ für „Zu zweit“ und $H=1$ für „Allein“.

(a) Leite den neuen Achsenabschnitt, die neue $X$-Steigung und den Koeffizienten von $H$ her. (b) Schreibe beide Gruppengleichungen unter der neuen Codierung auf und interpretiere den neuen Gruppenkoeffizienten. (c) Berechne bei $X=1.0$ und $X=5.0$ für beide Gruppen die angepassten Werte aus beiden Parametrisierungen und stelle sie nebeneinander. (d) Erkläre anhand der Berechnungen, weshalb das Wechseln der Referenz das Koordinatensystem der Koeffizienten verändert, aber die angepassten Werte, Residuen und gruppenspezifischen angepassten Linien nicht verändern kann.

### T07-A08-V02: Archivrolle neu referenzieren

**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel oder das erwartete Muster, das die Berechnung begründet.

Ein konstruiertes additives Modell codiert $G=0$ für die Gruppe „Assistenz“ und $G=1$ für die Gruppe „Koordination“: $\hat Y=35.00+(-1.60)X+(-5.00)G$. Dabei bezeichnet $Y$ die Ergebnisvariable „Suchzeit“ und $X$ den Prädiktor „Übungssitzungen“. Codiere neu mit $H=0$ für „Koordination“ und $H=1$ für „Assistenz“.

(a) Leite den neuen Achsenabschnitt, die neue $X$-Steigung und den Koeffizienten von $H$ her. (b) Schreibe beide Gruppengleichungen unter der neuen Codierung auf und interpretiere den neuen Gruppenkoeffizienten. (c) Berechne bei $X=0.0$ und $X=4.0$ für beide Gruppen die angepassten Werte aus beiden Parametrisierungen und stelle sie nebeneinander. (d) Erkläre anhand der Berechnungen, weshalb das Wechseln der Referenz das Koordinatensystem der Koeffizienten verändert, aber die angepassten Werte, Residuen und gruppenspezifischen angepassten Linien nicht verändern kann.

### T07-A08-V03: Lesemedium neu referenzieren

**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel oder das erwartete Muster, das die Berechnung begründet.

Ein konstruiertes additives Modell codiert $G=0$ für die Gruppe „Gedruckt“ und $G=1$ für die Gruppe „Audio“: $\hat Y=50.00+(2.00)X+(-3.00)G$. Dabei bezeichnet $Y$ die Ergebnisvariable „Punktwert im Textverständnis“ und $X$ den Prädiktor „Lesestunden“. Codiere neu mit $H=0$ für „Audio“ und $H=1$ für „Gedruckt“.

(a) Leite den neuen Achsenabschnitt, die neue $X$-Steigung und den Koeffizienten von $H$ her. (b) Schreibe beide Gruppengleichungen unter der neuen Codierung auf und interpretiere den neuen Gruppenkoeffizienten. (c) Berechne bei $X=2.0$ und $X=6.0$ für beide Gruppen die angepassten Werte aus beiden Parametrisierungen und stelle sie nebeneinander. (d) Erkläre anhand der Berechnungen, weshalb das Wechseln der Referenz das Koordinatensystem der Koeffizienten verändert, aber die angepassten Werte, Residuen und gruppenspezifischen angepassten Linien nicht verändern kann.

### T07-A08-V04: Navigationsanzeige neu referenzieren

**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel oder das erwartete Muster, das die Berechnung begründet.

Ein konstruiertes additives Modell codiert $G=0$ für die Gruppe „Statisch“ und $G=1$ für die Gruppe „Interaktiv“: $\hat Y=46.00+(-2.20)X+(-4.00)G$. Dabei bezeichnet $Y$ die Ergebnisvariable „Navigationszeit“ und $X$ den Prädiktor „Übungsversuche“. Codiere neu mit $H=0$ für „Interaktiv“ und $H=1$ für „Statisch“.

(a) Leite den neuen Achsenabschnitt, die neue $X$-Steigung und den Koeffizienten von $H$ her. (b) Schreibe beide Gruppengleichungen unter der neuen Codierung auf und interpretiere den neuen Gruppenkoeffizienten. (c) Berechne bei $X=1.0$ und $X=5.0$ für beide Gruppen die angepassten Werte aus beiden Parametrisierungen und stelle sie nebeneinander. (d) Erkläre anhand der Berechnungen, weshalb das Wechseln der Referenz das Koordinatensystem der Koeffizienten verändert, aber die angepassten Werte, Residuen und gruppenspezifischen angepassten Linien nicht verändern kann.

### T07-A08-V05: Kataloghilfe neu referenzieren

**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel oder das erwartete Muster, das die Berechnung begründet.

Ein konstruiertes additives Modell codiert $G=0$ für die Gruppe „Index“ und $G=1$ für die Gruppe „Suchleiste“: $\hat Y=53.00+(2.60)X+(3.00)G$. Dabei bezeichnet $Y$ die Ergebnisvariable „Punktwert der Genauigkeit“ und $X$ den Prädiktor „Übungsblöcke“. Codiere neu mit $H=0$ für „Suchleiste“ und $H=1$ für „Index“.

(a) Leite den neuen Achsenabschnitt, die neue $X$-Steigung und den Koeffizienten von $H$ her. (b) Schreibe beide Gruppengleichungen unter der neuen Codierung auf und interpretiere den neuen Gruppenkoeffizienten. (c) Berechne bei $X=0.0$ und $X=3.0$ für beide Gruppen die angepassten Werte aus beiden Parametrisierungen und stelle sie nebeneinander. (d) Erkläre anhand der Berechnungen, weshalb das Wechseln der Referenz das Koordinatensystem der Koeffizienten verändert, aber die angepassten Werte, Residuen und gruppenspezifischen angepassten Linien nicht verändern kann.

### T07-A08-V06: Workshopumgebung neu referenzieren

**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel oder das erwartete Muster, das die Berechnung begründet.

Ein konstruiertes additives Modell codiert $G=0$ für die Gruppe „Online“ und $G=1$ für die Gruppe „Kursraum“: $\hat Y=37.00+(3.00)X+(5.00)G$. Dabei bezeichnet $Y$ die Ergebnisvariable „Punktwert des Selbstvertrauens“ und $X$ den Prädiktor „Sitzungen“. Codiere neu mit $H=0$ für „Kursraum“ und $H=1$ für „Online“.

(a) Leite den neuen Achsenabschnitt, die neue $X$-Steigung und den Koeffizienten von $H$ her. (b) Schreibe beide Gruppengleichungen unter der neuen Codierung auf und interpretiere den neuen Gruppenkoeffizienten. (c) Berechne bei $X=1.0$ und $X=4.0$ für beide Gruppen die angepassten Werte aus beiden Parametrisierungen und stelle sie nebeneinander. (d) Erkläre anhand der Berechnungen, weshalb das Wechseln der Referenz das Koordinatensystem der Koeffizienten verändert, aber die angepassten Werte, Residuen und gruppenspezifischen angepassten Linien nicht verändern kann.

### T07-A08-V07: Konzentrationsraum neu referenzieren

**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel oder das erwartete Muster, das die Berechnung begründet.

Ein konstruiertes additives Modell codiert $G=0$ für die Gruppe „Offener Raum“ und $G=1$ für die Gruppe „Privater Raum“: $\hat Y=59.00+(1.80)X+(4.00)G$. Dabei bezeichnet $Y$ die Ergebnisvariable „Punktwert der Aufgabengenauigkeit“ und $X$ den Prädiktor „Konzentrationsblöcke“. Codiere neu mit $H=0$ für „Privater Raum“ und $H=1$ für „Offener Raum“.

(a) Leite den neuen Achsenabschnitt, die neue $X$-Steigung und den Koeffizienten von $H$ her. (b) Schreibe beide Gruppengleichungen unter der neuen Codierung auf und interpretiere den neuen Gruppenkoeffizienten. (c) Berechne bei $X=2.0$ und $X=7.0$ für beide Gruppen die angepassten Werte aus beiden Parametrisierungen und stelle sie nebeneinander. (d) Erkläre anhand der Berechnungen, weshalb das Wechseln der Referenz das Koordinatensystem der Koeffizienten verändert, aber die angepassten Werte, Residuen und gruppenspezifischen angepassten Linien nicht verändern kann.

### T07-A08-V08: Museumsroute neu referenzieren

**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel oder das erwartete Muster, das die Berechnung begründet.

Ein konstruiertes additives Modell codiert $G=0$ für die Gruppe „Freie Route“ und $G=1$ für die Gruppe „Zusammengestellte Route“: $\hat Y=45.00+(4.20)X+(6.50)G$. Dabei bezeichnet $Y$ die Ergebnisvariable „Punktwert des Wissens“ und $X$ den Prädiktor „Besuche“. Codiere neu mit $H=0$ für „Zusammengestellte Route“ und $H=1$ für „Freie Route“.

(a) Leite den neuen Achsenabschnitt, die neue $X$-Steigung und den Koeffizienten von $H$ her. (b) Schreibe beide Gruppengleichungen unter der neuen Codierung auf und interpretiere den neuen Gruppenkoeffizienten. (c) Berechne bei $X=0.0$ und $X=3.0$ für beide Gruppen die angepassten Werte aus beiden Parametrisierungen und stelle sie nebeneinander. (d) Erkläre anhand der Berechnungen, weshalb das Wechseln der Referenz das Koordinatensystem der Koeffizienten verändert, aber die angepassten Werte, Residuen und gruppenspezifischen angepassten Linien nicht verändern kann.

### T07-A08-V09: Überarbeitungstreffen neu referenzieren

**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel oder das erwartete Muster, das die Berechnung begründet.

Ein konstruiertes additives Modell codiert $G=0$ für die Gruppe „Asynchron“ und $G=1$ für die Gruppe „Live“: $\hat Y=51.00+(3.40)X+(2.50)G$. Dabei bezeichnet $Y$ die Ergebnisvariable „Punktwert der Überarbeitung“ und $X$ den Prädiktor „Feedbackrunden“. Codiere neu mit $H=0$ für „Live“ und $H=1$ für „Asynchron“.

(a) Leite den neuen Achsenabschnitt, die neue $X$-Steigung und den Koeffizienten von $H$ her. (b) Schreibe beide Gruppengleichungen unter der neuen Codierung auf und interpretiere den neuen Gruppenkoeffizienten. (c) Berechne bei $X=1.0$ und $X=5.0$ für beide Gruppen die angepassten Werte aus beiden Parametrisierungen und stelle sie nebeneinander. (d) Erkläre anhand der Berechnungen, weshalb das Wechseln der Referenz das Koordinatensystem der Koeffizienten verändert, aber die angepassten Werte, Residuen und gruppenspezifischen angepassten Linien nicht verändern kann.

### T07-A08-V10: Planungswerkzeug neu referenzieren

**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel oder das erwartete Muster, das die Berechnung begründet.

Ein konstruiertes additives Modell codiert $G=0$ für die Gruppe „Notizbuch“ und $G=1$ für die Gruppe „Kalender“: $\hat Y=72.00+(-2.50)X+(-4.00)G$. Dabei bezeichnet $Y$ die Ergebnisvariable „Bearbeitungszeit“ und $X$ den Prädiktor „Planungssitzungen“. Codiere neu mit $H=0$ für „Kalender“ und $H=1$ für „Notizbuch“.

(a) Leite den neuen Achsenabschnitt, die neue $X$-Steigung und den Koeffizienten von $H$ her. (b) Schreibe beide Gruppengleichungen unter der neuen Codierung auf und interpretiere den neuen Gruppenkoeffizienten. (c) Berechne bei $X=1.0$ und $X=6.0$ für beide Gruppen die angepassten Werte aus beiden Parametrisierungen und stelle sie nebeneinander. (d) Erkläre anhand der Berechnungen, weshalb das Wechseln der Referenz das Koordinatensystem der Koeffizienten verändert, aber die angepassten Werte, Residuen und gruppenspezifischen angepassten Linien nicht verändern kann.

## A09: Eine Interaktion zwischen Gruppe und quantitativem Prädiktor interpretieren

### T07-A09-V01: Übungsstunden nach Lernbegleitung

**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel oder das erwartete Muster, das die Berechnung begründet.

Ein konstruiertes Interaktionsmodell verwendet $G=0$ für die Gruppe „Ohne Lernbegleitung“, $G=1$ für die Gruppe „Mit Lernbegleitung“ und das Produkt $XG$: $\hat Y=40.00+(2.00)X+(4.00)G+(1.20)XG$. Dabei bezeichnet $Y$ die Ergebnisvariable „Punktwert im statistischen Denken“ und $X$ den Prädiktor „Übungsstunden“.

(a) Erstelle für beide Gruppen Zeilen bei $X=1.0$ und $X=5.0$ und zeige darin $G$ und $XG$. (b) Leite den bedingten Achsenabschnitt und die bedingte Steigung jeder Gruppe her. (c) Berechne die vier angepassten Koordinaten und ordne alle Grössen in einer Tabelle. (d) Zeichne aus diesen Koordinaten die beiden angepassten Geraden in ein beschriftetes Diagramm und markiere bei beiden dargestellten $X$-Werten den angepassten Gruppenabstand. (e) Interpretiere $b_1$, $b_2$ und $b_3$ bei ihren richtigen Referenzbedingungen. Erkläre, wie $b_3$ den Gruppenabstand entlang von $X$ verändert, und begründe, weshalb eine Interaktion selbst kein Kausalitätsbeleg ist.

### T07-A09-V02: Übungssitzungen nach Archivrolle

**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel oder das erwartete Muster, das die Berechnung begründet.

Ein konstruiertes Interaktionsmodell verwendet $G=0$ für die Gruppe „Neue Mitarbeitende“, $G=1$ für die Gruppe „Erfahrene Mitarbeitende“ und das Produkt $XG$: $\hat Y=38.00+(-1.20)X+(-3.00)G+(-0.80)XG$. Dabei bezeichnet $Y$ die Ergebnisvariable „Suchzeit“ und $X$ den Prädiktor „Übungssitzungen“.

(a) Erstelle für beide Gruppen Zeilen bei $X=0.0$ und $X=4.0$ und zeige darin $G$ und $XG$. (b) Leite den bedingten Achsenabschnitt und die bedingte Steigung jeder Gruppe her. (c) Berechne die vier angepassten Koordinaten und ordne alle Grössen in einer Tabelle. (d) Zeichne aus diesen Koordinaten die beiden angepassten Geraden in ein beschriftetes Diagramm und markiere bei beiden dargestellten $X$-Werten den angepassten Gruppenabstand. (e) Interpretiere $b_1$, $b_2$ und $b_3$ bei ihren richtigen Referenzbedingungen. Erkläre, wie $b_3$ den Gruppenabstand entlang von $X$ verändert, und begründe, weshalb eine Interaktion selbst kein Kausalitätsbeleg ist.

### T07-A09-V03: Lesestunden nach Medium

**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel oder das erwartete Muster, das die Berechnung begründet.

Ein konstruiertes Interaktionsmodell verwendet $G=0$ für die Gruppe „Gedruckt“, $G=1$ für die Gruppe „Audio“ und das Produkt $XG$: $\hat Y=49.00+(2.60)X+(2.00)G+(-1.00)XG$. Dabei bezeichnet $Y$ die Ergebnisvariable „Punktwert im Textverständnis“ und $X$ den Prädiktor „Lesestunden“.

(a) Erstelle für beide Gruppen Zeilen bei $X=2.0$ und $X=6.0$ und zeige darin $G$ und $XG$. (b) Leite den bedingten Achsenabschnitt und die bedingte Steigung jeder Gruppe her. (c) Berechne die vier angepassten Koordinaten und ordne alle Grössen in einer Tabelle. (d) Zeichne aus diesen Koordinaten die beiden angepassten Geraden in ein beschriftetes Diagramm und markiere bei beiden dargestellten $X$-Werten den angepassten Gruppenabstand. (e) Interpretiere $b_1$, $b_2$ und $b_3$ bei ihren richtigen Referenzbedingungen. Erkläre, wie $b_3$ den Gruppenabstand entlang von $X$ verändert, und begründe, weshalb eine Interaktion selbst kein Kausalitätsbeleg ist.

### T07-A09-V04: Streckenübung nach Navigationsanzeige

**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel oder das erwartete Muster, das die Berechnung begründet.

Ein konstruiertes Interaktionsmodell verwendet $G=0$ für die Gruppe „Statisch“, $G=1$ für die Gruppe „Interaktiv“ und das Produkt $XG$: $\hat Y=48.00+(-1.50)X+(-2.00)G+(-0.90)XG$. Dabei bezeichnet $Y$ die Ergebnisvariable „Navigationszeit“ und $X$ den Prädiktor „Übungsversuche“.

(a) Erstelle für beide Gruppen Zeilen bei $X=1.0$ und $X=5.0$ und zeige darin $G$ und $XG$. (b) Leite den bedingten Achsenabschnitt und die bedingte Steigung jeder Gruppe her. (c) Berechne die vier angepassten Koordinaten und ordne alle Grössen in einer Tabelle. (d) Zeichne aus diesen Koordinaten die beiden angepassten Geraden in ein beschriftetes Diagramm und markiere bei beiden dargestellten $X$-Werten den angepassten Gruppenabstand. (e) Interpretiere $b_1$, $b_2$ und $b_3$ bei ihren richtigen Referenzbedingungen. Erkläre, wie $b_3$ den Gruppenabstand entlang von $X$ verändert, und begründe, weshalb eine Interaktion selbst kein Kausalitätsbeleg ist.

### T07-A09-V05: Übungsblöcke nach Kataloghilfe

**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel oder das erwartete Muster, das die Berechnung begründet.

Ein konstruiertes Interaktionsmodell verwendet $G=0$ für die Gruppe „Index“, $G=1$ für die Gruppe „Suchleiste“ und das Produkt $XG$: $\hat Y=52.00+(2.00)X+(3.00)G+(0.70)XG$. Dabei bezeichnet $Y$ die Ergebnisvariable „Punktwert der Genauigkeit“ und $X$ den Prädiktor „Übungsblöcke“.

(a) Erstelle für beide Gruppen Zeilen bei $X=0.0$ und $X=4.0$ und zeige darin $G$ und $XG$. (b) Leite den bedingten Achsenabschnitt und die bedingte Steigung jeder Gruppe her. (c) Berechne die vier angepassten Koordinaten und ordne alle Grössen in einer Tabelle. (d) Zeichne aus diesen Koordinaten die beiden angepassten Geraden in ein beschriftetes Diagramm und markiere bei beiden dargestellten $X$-Werten den angepassten Gruppenabstand. (e) Interpretiere $b_1$, $b_2$ und $b_3$ bei ihren richtigen Referenzbedingungen. Erkläre, wie $b_3$ den Gruppenabstand entlang von $X$ verändert, und begründe, weshalb eine Interaktion selbst kein Kausalitätsbeleg ist.

### T07-A09-V06: Sitzungen nach Workshopumgebung

**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel oder das erwartete Muster, das die Berechnung begründet.

Ein konstruiertes Interaktionsmodell verwendet $G=0$ für die Gruppe „Online“, $G=1$ für die Gruppe „Kursraum“ und das Produkt $XG$: $\hat Y=36.00+(2.40)X+(5.00)G+(0.80)XG$. Dabei bezeichnet $Y$ die Ergebnisvariable „Punktwert des Selbstvertrauens“ und $X$ den Prädiktor „Sitzungen“.

(a) Erstelle für beide Gruppen Zeilen bei $X=1.0$ und $X=5.0$ und zeige darin $G$ und $XG$. (b) Leite den bedingten Achsenabschnitt und die bedingte Steigung jeder Gruppe her. (c) Berechne die vier angepassten Koordinaten und ordne alle Grössen in einer Tabelle. (d) Zeichne aus diesen Koordinaten die beiden angepassten Geraden in ein beschriftetes Diagramm und markiere bei beiden dargestellten $X$-Werten den angepassten Gruppenabstand. (e) Interpretiere $b_1$, $b_2$ und $b_3$ bei ihren richtigen Referenzbedingungen. Erkläre, wie $b_3$ den Gruppenabstand entlang von $X$ verändert, und begründe, weshalb eine Interaktion selbst kein Kausalitätsbeleg ist.

### T07-A09-V07: Konzentrationsblöcke nach Raumart

**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel oder das erwartete Muster, das die Berechnung begründet.

Ein konstruiertes Interaktionsmodell verwendet $G=0$ für die Gruppe „Offener Raum“, $G=1$ für die Gruppe „Privater Raum“ und das Produkt $XG$: $\hat Y=58.00+(2.10)X+(4.00)G+(-0.60)XG$. Dabei bezeichnet $Y$ die Ergebnisvariable „Punktwert der Aufgabengenauigkeit“ und $X$ den Prädiktor „Konzentrationsblöcke“.

(a) Erstelle für beide Gruppen Zeilen bei $X=2.0$ und $X=7.0$ und zeige darin $G$ und $XG$. (b) Leite den bedingten Achsenabschnitt und die bedingte Steigung jeder Gruppe her. (c) Berechne die vier angepassten Koordinaten und ordne alle Grössen in einer Tabelle. (d) Zeichne aus diesen Koordinaten die beiden angepassten Geraden in ein beschriftetes Diagramm und markiere bei beiden dargestellten $X$-Werten den angepassten Gruppenabstand. (e) Interpretiere $b_1$, $b_2$ und $b_3$ bei ihren richtigen Referenzbedingungen. Erkläre, wie $b_3$ den Gruppenabstand entlang von $X$ verändert, und begründe, weshalb eine Interaktion selbst kein Kausalitätsbeleg ist.

### T07-A09-V08: Besuche nach Museumsroute

**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel oder das erwartete Muster, das die Berechnung begründet.

Ein konstruiertes Interaktionsmodell verwendet $G=0$ für die Gruppe „Freie Route“, $G=1$ für die Gruppe „Zusammengestellte Route“ und das Produkt $XG$: $\hat Y=44.00+(3.50)X+(3.00)G+(1.50)XG$. Dabei bezeichnet $Y$ die Ergebnisvariable „Punktwert des Wissens“ und $X$ den Prädiktor „Besuche“.

(a) Erstelle für beide Gruppen Zeilen bei $X=0.0$ und $X=3.0$ und zeige darin $G$ und $XG$. (b) Leite den bedingten Achsenabschnitt und die bedingte Steigung jeder Gruppe her. (c) Berechne die vier angepassten Koordinaten und ordne alle Grössen in einer Tabelle. (d) Zeichne aus diesen Koordinaten die beiden angepassten Geraden in ein beschriftetes Diagramm und markiere bei beiden dargestellten $X$-Werten den angepassten Gruppenabstand. (e) Interpretiere $b_1$, $b_2$ und $b_3$ bei ihren richtigen Referenzbedingungen. Erkläre, wie $b_3$ den Gruppenabstand entlang von $X$ verändert, und begründe, weshalb eine Interaktion selbst kein Kausalitätsbeleg ist.

### T07-A09-V09: Feedbackrunden nach Sitzungsform

**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel oder das erwartete Muster, das die Berechnung begründet.

Ein konstruiertes Interaktionsmodell verwendet $G=0$ für die Gruppe „Asynchron“, $G=1$ für die Gruppe „Live“ und das Produkt $XG$: $\hat Y=50.00+(2.80)X+(4.00)G+(-0.50)XG$. Dabei bezeichnet $Y$ die Ergebnisvariable „Punktwert der Überarbeitung“ und $X$ den Prädiktor „Feedbackrunden“.

(a) Erstelle für beide Gruppen Zeilen bei $X=1.0$ und $X=5.0$ und zeige darin $G$ und $XG$. (b) Leite den bedingten Achsenabschnitt und die bedingte Steigung jeder Gruppe her. (c) Berechne die vier angepassten Koordinaten und ordne alle Grössen in einer Tabelle. (d) Zeichne aus diesen Koordinaten die beiden angepassten Geraden in ein beschriftetes Diagramm und markiere bei beiden dargestellten $X$-Werten den angepassten Gruppenabstand. (e) Interpretiere $b_1$, $b_2$ und $b_3$ bei ihren richtigen Referenzbedingungen. Erkläre, wie $b_3$ den Gruppenabstand entlang von $X$ verändert, und begründe, weshalb eine Interaktion selbst kein Kausalitätsbeleg ist.

### T07-A09-V10: Planung nach Werkzeugart

**Überlege zuerst.** Nenne vor dem Rechnen den Zusammenhang, die Regel oder das erwartete Muster, das die Berechnung begründet.

Ein konstruiertes Interaktionsmodell verwendet $G=0$ für die Gruppe „Notizbuch“, $G=1$ für die Gruppe „Kalender“ und das Produkt $XG$: $\hat Y=74.00+(-1.80)X+(-2.00)G+(-0.90)XG$. Dabei bezeichnet $Y$ die Ergebnisvariable „Bearbeitungszeit“ und $X$ den Prädiktor „Planungssitzungen“.

(a) Erstelle für beide Gruppen Zeilen bei $X=1.0$ und $X=6.0$ und zeige darin $G$ und $XG$. (b) Leite den bedingten Achsenabschnitt und die bedingte Steigung jeder Gruppe her. (c) Berechne die vier angepassten Koordinaten und ordne alle Grössen in einer Tabelle. (d) Zeichne aus diesen Koordinaten die beiden angepassten Geraden in ein beschriftetes Diagramm und markiere bei beiden dargestellten $X$-Werten den angepassten Gruppenabstand. (e) Interpretiere $b_1$, $b_2$ und $b_3$ bei ihren richtigen Referenzbedingungen. Erkläre, wie $b_3$ den Gruppenabstand entlang von $X$ verändert, und begründe, weshalb eine Interaktion selbst kein Kausalitätsbeleg ist.
