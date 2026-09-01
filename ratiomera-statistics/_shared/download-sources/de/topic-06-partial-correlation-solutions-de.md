---
title: "Vollständige Lösungen"
subtitle: "Partielle Korrelation"
document-id: "topic-06-partial-correlation-solutions-de"
topic-id: "topic-06-partial-correlation"
topic-number: "06"
topic-slug: "partial-correlation"
document-type: "solutions"
locale: "de"
paired-document-id: "topic-06-partial-correlation-exercises-de"
---

Diese vollständigen Lösungen verwenden dieselben Kennungen und dieselbe Reihenfolge wie das Übungsblatt. Zwischenwerte werden bis zum angegebenen Rundungsschritt beibehalten. Kleine Abweichungen durch früheres Runden sind deshalb dort zulässig, wo dies vermerkt ist. Alle Kontexte, Werte, Daten und Softwareausgaben sind eigens erstelltes Lehrmaterial; sie sind keine empirischen Befunde.

# Teil I: Theorie

## A02: Bivariate und partielle Korrelation vergleichen

### T06-A02-V01: Übungszeit, Vorwissen und statistisches Denken

**Fragestellung bestimmen**

Ein plausibles Diagramm lautet **Z → X, Z → Y und X ↔ Y**.

Es verbindet die Variable **«Vorwissen»** sowohl mit **«wöchentliche Übungszeit»** als auch mit **«Punktwert im statistischen Denken»**; die separate $X$-$Y$-Verbindung bleibt ein eigener Zusammenhang.

Eine mögliche inhaltliche Erklärung lautet: Vorwissen kann sowohl mit der wöchentlichen Übungszeit als auch mit dem statistischen Denken positiv zusammenhängen.

Deshalb kann ein Teil des bivariaten Zusammenhangs auf diesen beiden Verbindungen beruhen.

Der Koeffizient verändert sich von 0.68 zu 0.34.

**Evidenz schrittweise beurteilen**

Sein Betrag ist nach der Bereinigung kleiner.

Bei der Residualisierung wird zuerst die Variable **«wöchentliche Übungszeit»** aus **«Vorwissen»** vorhergesagt und danach die Variable **«Punktwert im statistischen Denken»** aus **«Vorwissen»**.

Die partielle Korrelation ist die Korrelation zwischen den Abweichungen, die in diesen beiden Residualspalten verbleiben.

Ein kleinerer Betrag deutet darauf hin, dass die Kontrollvariable einen Teil des bivariaten Musters beschreibt.

Ein grösserer Betrag deutet auf Suppression hin: Die Bereinigung macht dann einen zuvor teilweise verdeckten Zusammenhang sichtbar.

**Schluss und Grenzen festhalten**

Keines der Ergebnisse stellt die zeitliche Reihenfolge her, schliesst nicht gemessene Variablen aus, behebt Messfehler oder ersetzt experimentelle Kontrolle.

Die Begründung von **«Vorwissen»** als Kontrollvariable braucht fachliche und forschungsplanerische Argumente, darunter eine plausible zeitliche Reihenfolge und eine klare Rolle der Variable.

Die Koeffizienten allein liefern diese Begründung nicht.

Eine lineare Bereinigung entfernt nur den angepassten linearen Anteil im angegebenen Modell.

Nichtlineare Strukturen, Messprobleme und relevante nicht gemessene Variablen können bestehen bleiben.

### T06-A02-V02: Suchzeit, Archiverfahrung und Genauigkeit

**Fragestellung bestimmen**

Ein plausibles Diagramm lautet **Z → X, Z → Y und X ↔ Y**.

Es verbindet die Variable **«Archiverfahrung»** sowohl mit **«Suchzeit»** als auch mit **«Genauigkeit»**; die separate $X$-$Y$-Verbindung bleibt ein eigener Zusammenhang.

Eine mögliche inhaltliche Erklärung lautet: Mehr Archiverfahrung kann die Suchzeit verkürzen und zugleich die Genauigkeit erhöhen.

Dadurch kann ein Teil des negativen bivariaten Zusammenhangs entstehen.

Der Koeffizient verändert sich von -0.57 zu -0.26.

**Evidenz schrittweise beurteilen**

Sein Betrag ist nach der Bereinigung kleiner.

Bei der Residualisierung wird zuerst die Variable **«Suchzeit»** aus **«Archiverfahrung»** vorhergesagt und danach die Variable **«Genauigkeit»** aus **«Archiverfahrung»**.

Die partielle Korrelation ist die Korrelation zwischen den Abweichungen, die in diesen beiden Residualspalten verbleiben.

Ein kleinerer Betrag deutet darauf hin, dass die Kontrollvariable einen Teil des bivariaten Musters beschreibt.

Ein grösserer Betrag deutet auf Suppression hin: Die Bereinigung macht dann einen zuvor teilweise verdeckten Zusammenhang sichtbar.

**Schluss und Grenzen festhalten**

Keines der Ergebnisse stellt die zeitliche Reihenfolge her, schliesst nicht gemessene Variablen aus, behebt Messfehler oder ersetzt experimentelle Kontrolle.

Die Begründung von **«Archiverfahrung»** als Kontrollvariable braucht fachliche und forschungsplanerische Argumente, darunter eine plausible zeitliche Reihenfolge und eine klare Rolle der Variable.

Die Koeffizienten allein liefern diese Begründung nicht.

Eine lineare Bereinigung entfernt nur den angepassten linearen Anteil im angegebenen Modell.

Nichtlineare Strukturen, Messprobleme und relevante nicht gemessene Variablen können bestehen bleiben.

### T06-A02-V03: Lesezeit, Kursarbeitslast und Textverständnis

**Fragestellung bestimmen**

Ein plausibles Diagramm lautet **Z → X, Z → Y und X ↔ Y**.

Es verbindet die Variable **«Arbeitslast im Kurs»** sowohl mit **«Lesezeit»** als auch mit **«Textverständnis»**; die separate $X$-$Y$-Verbindung bleibt ein eigener Zusammenhang.

Eine mögliche inhaltliche Erklärung lautet: Eine hohe Arbeitslast im Kurs kann mit mehr Lesezeit, aber geringerem Textverständnis einhergehen.

Dadurch kann sie einen Teil des positiven bereinigten Zusammenhangs verdecken.

Der Koeffizient verändert sich von 0.18 zu 0.41.

**Evidenz schrittweise beurteilen**

Sein Betrag ist nach der Bereinigung grösser.

Bei der Residualisierung wird zuerst die Variable **«Lesezeit»** aus **«Arbeitslast im Kurs»** vorhergesagt und danach die Variable **«Textverständnis»** aus **«Arbeitslast im Kurs»**.

Die partielle Korrelation ist die Korrelation zwischen den Abweichungen, die in diesen beiden Residualspalten verbleiben.

Ein kleinerer Betrag deutet darauf hin, dass die Kontrollvariable einen Teil des bivariaten Musters beschreibt.

Ein grösserer Betrag deutet auf Suppression hin: Die Bereinigung macht dann einen zuvor teilweise verdeckten Zusammenhang sichtbar.

**Schluss und Grenzen festhalten**

Keines der Ergebnisse stellt die zeitliche Reihenfolge her, schliesst nicht gemessene Variablen aus, behebt Messfehler oder ersetzt experimentelle Kontrolle.

Die Begründung von **«Arbeitslast im Kurs»** als Kontrollvariable braucht fachliche und forschungsplanerische Argumente, darunter eine plausible zeitliche Reihenfolge und eine klare Rolle der Variable.

Die Koeffizienten allein liefern diese Begründung nicht.

Eine lineare Bereinigung entfernt nur den angepassten linearen Anteil im angegebenen Modell.

Nichtlineare Strukturen, Messprobleme und relevante nicht gemessene Variablen können bestehen bleiben.

### T06-A02-V04: Benachrichtigungen, Aufgabenlast und Konzentration

**Fragestellung bestimmen**

Ein plausibles Diagramm lautet **Z → X, Z → Y und X ↔ Y**.

Es verbindet die Variable **«Aufgabenlast»** sowohl mit **«Anzahl der Benachrichtigungen»** als auch mit **«Konzentration»**; die separate $X$-$Y$-Verbindung bleibt ein eigener Zusammenhang.

Eine mögliche inhaltliche Erklärung lautet: Eine höhere Aufgabenlast kann die Zahl der Benachrichtigungen erhöhen und die Konzentration senken.

Dadurch kann ein Teil des rohen negativen Zusammenhangs entstehen.

Der Koeffizient verändert sich von -0.49 zu -0.20.

**Evidenz schrittweise beurteilen**

Sein Betrag ist nach der Bereinigung kleiner.

Bei der Residualisierung wird zuerst die Variable **«Anzahl der Benachrichtigungen»** aus **«Aufgabenlast»** vorhergesagt und danach die Variable **«Konzentration»** aus **«Aufgabenlast»**.

Die partielle Korrelation ist die Korrelation zwischen den Abweichungen, die in diesen beiden Residualspalten verbleiben.

Ein kleinerer Betrag deutet darauf hin, dass die Kontrollvariable einen Teil des bivariaten Musters beschreibt.

Ein grösserer Betrag deutet auf Suppression hin: Die Bereinigung macht dann einen zuvor teilweise verdeckten Zusammenhang sichtbar.

**Schluss und Grenzen festhalten**

Keines der Ergebnisse stellt die zeitliche Reihenfolge her, schliesst nicht gemessene Variablen aus, behebt Messfehler oder ersetzt experimentelle Kontrolle.

Die Begründung von **«Aufgabenlast»** als Kontrollvariable braucht fachliche und forschungsplanerische Argumente, darunter eine plausible zeitliche Reihenfolge und eine klare Rolle der Variable.

Die Koeffizienten allein liefern diese Begründung nicht.

Eine lineare Bereinigung entfernt nur den angepassten linearen Anteil im angegebenen Modell.

Nichtlineare Strukturen, Messprobleme und relevante nicht gemessene Variablen können bestehen bleiben.

### T06-A02-V05: Museumsbesuche, Bildungsstand und historisches Wissen

**Fragestellung bestimmen**

Ein plausibles Diagramm lautet **Z → X, Z → Y und X ↔ Y**.

Es verbindet die Variable **«Bildungsstand»** sowohl mit **«Museumsbesuche»** als auch mit **«historisches Wissen»**; die separate $X$-$Y$-Verbindung bleibt ein eigener Zusammenhang.

Eine mögliche inhaltliche Erklärung lautet: Ein höherer Bildungsstand kann Museumsbesuche fördern und historisches Wissen unterstützen.

Deshalb kann der rohe Zusammenhang teilweise auf diesen beiden Verbindungen beruhen.

Der Koeffizient verändert sich von 0.54 zu 0.29.

**Evidenz schrittweise beurteilen**

Sein Betrag ist nach der Bereinigung kleiner.

Bei der Residualisierung wird zuerst die Variable **«Museumsbesuche»** aus **«Bildungsstand»** vorhergesagt und danach die Variable **«historisches Wissen»** aus **«Bildungsstand»**.

Die partielle Korrelation ist die Korrelation zwischen den Abweichungen, die in diesen beiden Residualspalten verbleiben.

Ein kleinerer Betrag deutet darauf hin, dass die Kontrollvariable einen Teil des bivariaten Musters beschreibt.

Ein grösserer Betrag deutet auf Suppression hin: Die Bereinigung macht dann einen zuvor teilweise verdeckten Zusammenhang sichtbar.

**Schluss und Grenzen festhalten**

Keines der Ergebnisse stellt die zeitliche Reihenfolge her, schliesst nicht gemessene Variablen aus, behebt Messfehler oder ersetzt experimentelle Kontrolle.

Die Begründung von **«Bildungsstand»** als Kontrollvariable braucht fachliche und forschungsplanerische Argumente, darunter eine plausible zeitliche Reihenfolge und eine klare Rolle der Variable.

Die Koeffizienten allein liefern diese Begründung nicht.

Eine lineare Bereinigung entfernt nur den angepassten linearen Anteil im angegebenen Modell.

Nichtlineare Strukturen, Messprobleme und relevante nicht gemessene Variablen können bestehen bleiben.

### T06-A02-V06: Streckenkenntnis, Streckenlänge und Reisezeit

**Fragestellung bestimmen**

Ein plausibles Diagramm lautet **Z → X, Z → Y und X ↔ Y**.

Es verbindet die Variable **«Streckenlänge»** sowohl mit **«Streckenkenntnis»** als auch mit **«Reisezeit»**; die separate $X$-$Y$-Verbindung bleibt ein eigener Zusammenhang.

Eine mögliche inhaltliche Erklärung lautet: Längere Strecken können vertrauter sein und trotzdem mehr Reisezeit beanspruchen.

Dadurch kann ein Teil des negativen Zusammenhangs zwischen Streckenkenntnis und Reisezeit verdeckt werden.

Der Koeffizient verändert sich von -0.21 zu -0.48.

**Evidenz schrittweise beurteilen**

Sein Betrag ist nach der Bereinigung grösser.

Bei der Residualisierung wird zuerst die Variable **«Streckenkenntnis»** aus **«Streckenlänge»** vorhergesagt und danach die Variable **«Reisezeit»** aus **«Streckenlänge»**.

Die partielle Korrelation ist die Korrelation zwischen den Abweichungen, die in diesen beiden Residualspalten verbleiben.

Ein kleinerer Betrag deutet darauf hin, dass die Kontrollvariable einen Teil des bivariaten Musters beschreibt.

Ein grösserer Betrag deutet auf Suppression hin: Die Bereinigung macht dann einen zuvor teilweise verdeckten Zusammenhang sichtbar.

**Schluss und Grenzen festhalten**

Keines der Ergebnisse stellt die zeitliche Reihenfolge her, schliesst nicht gemessene Variablen aus, behebt Messfehler oder ersetzt experimentelle Kontrolle.

Die Begründung von **«Streckenlänge»** als Kontrollvariable braucht fachliche und forschungsplanerische Argumente, darunter eine plausible zeitliche Reihenfolge und eine klare Rolle der Variable.

Die Koeffizienten allein liefern diese Begründung nicht.

Eine lineare Bereinigung entfernt nur den angepassten linearen Anteil im angegebenen Modell.

Nichtlineare Strukturen, Messprobleme und relevante nicht gemessene Variablen können bestehen bleiben.

### T06-A02-V07: Workshopteilnahme sowie anfängliches und abschliessendes Selbstvertrauen

**Fragestellung bestimmen**

Ein plausibles Diagramm lautet **Z → X, Z → Y und X ↔ Y**.

Es verbindet die Variable **«anfängliches Selbstvertrauen»** sowohl mit **«Workshopteilnahme»** als auch mit **«abschliessendes Selbstvertrauen»**; die separate $X$-$Y$-Verbindung bleibt ein eigener Zusammenhang.

Eine mögliche inhaltliche Erklärung lautet: Lernende mit höherem anfänglichem Selbstvertrauen können häufiger an Workshops teilnehmen und auch mit höherem Selbstvertrauen abschliessen.

Der Koeffizient verändert sich von 0.61 zu 0.25.

**Evidenz schrittweise beurteilen**

Sein Betrag ist nach der Bereinigung kleiner.

Bei der Residualisierung wird zuerst die Variable **«Workshopteilnahme»** aus **«anfängliches Selbstvertrauen»** vorhergesagt und danach die Variable **«abschliessendes Selbstvertrauen»** aus **«anfängliches Selbstvertrauen»**.

Die partielle Korrelation ist die Korrelation zwischen den Abweichungen, die in diesen beiden Residualspalten verbleiben.

Ein kleinerer Betrag deutet darauf hin, dass die Kontrollvariable einen Teil des bivariaten Musters beschreibt.

Ein grösserer Betrag deutet auf Suppression hin: Die Bereinigung macht dann einen zuvor teilweise verdeckten Zusammenhang sichtbar.

**Schluss und Grenzen festhalten**

Keines der Ergebnisse stellt die zeitliche Reihenfolge her, schliesst nicht gemessene Variablen aus, behebt Messfehler oder ersetzt experimentelle Kontrolle.

Die Begründung von **«anfängliches Selbstvertrauen»** als Kontrollvariable braucht fachliche und forschungsplanerische Argumente, darunter eine plausible zeitliche Reihenfolge und eine klare Rolle der Variable.

Die Koeffizienten allein liefern diese Begründung nicht.

Eine lineare Bereinigung entfernt nur den angepassten linearen Anteil im angegebenen Modell.

Nichtlineare Strukturen, Messprobleme und relevante nicht gemessene Variablen können bestehen bleiben.

### T06-A02-V08: Aufgabenwechsel, Arbeitslast und Aufgabenerledigung

**Fragestellung bestimmen**

Ein plausibles Diagramm lautet **Z → X, Z → Y und X ↔ Y**.

Es verbindet die Variable **«Arbeitslast»** sowohl mit **«Häufigkeit des Aufgabenwechsels»** als auch mit **«Punktwert für die Aufgabenerledigung»**; die separate $X$-$Y$-Verbindung bleibt ein eigener Zusammenhang.

Eine mögliche inhaltliche Erklärung lautet: Eine hohe Arbeitslast kann häufigere Aufgabenwechsel begünstigen und den Punktwert für die Aufgabenerledigung senken.

Dadurch kann ein Teil des rohen negativen Zusammenhangs entstehen.

Der Koeffizient verändert sich von -0.52 zu -0.28.

**Evidenz schrittweise beurteilen**

Sein Betrag ist nach der Bereinigung kleiner.

Bei der Residualisierung wird zuerst die Variable **«Häufigkeit des Aufgabenwechsels»** aus **«Arbeitslast»** vorhergesagt und danach die Variable **«Punktwert für die Aufgabenerledigung»** aus **«Arbeitslast»**.

Die partielle Korrelation ist die Korrelation zwischen den Abweichungen, die in diesen beiden Residualspalten verbleiben.

Ein kleinerer Betrag deutet darauf hin, dass die Kontrollvariable einen Teil des bivariaten Musters beschreibt.

Ein grösserer Betrag deutet auf Suppression hin: Die Bereinigung macht dann einen zuvor teilweise verdeckten Zusammenhang sichtbar.

**Schluss und Grenzen festhalten**

Keines der Ergebnisse stellt die zeitliche Reihenfolge her, schliesst nicht gemessene Variablen aus, behebt Messfehler oder ersetzt experimentelle Kontrolle.

Die Begründung von **«Arbeitslast»** als Kontrollvariable braucht fachliche und forschungsplanerische Argumente, darunter eine plausible zeitliche Reihenfolge und eine klare Rolle der Variable.

Die Koeffizienten allein liefern diese Begründung nicht.

Eine lineare Bereinigung entfernt nur den angepassten linearen Anteil im angegebenen Modell.

Nichtlineare Strukturen, Messprobleme und relevante nicht gemessene Variablen können bestehen bleiben.

### T06-A02-V09: Diskussionsbeiträge, Engagement und statistisches Denken

**Fragestellung bestimmen**

Ein plausibles Diagramm lautet **Z → X, Z → Y und X ↔ Y**.

Es verbindet die Variable **«allgemeines Engagement»** sowohl mit **«Anzahl der Diskussionsbeiträge»** als auch mit **«Punktwert im statistischen Denken»**; die separate $X$-$Y$-Verbindung bleibt ein eigener Zusammenhang.

Eine mögliche inhaltliche Erklärung lautet: Ein höheres allgemeines Engagement kann sowohl zu mehr Diskussionsbeiträgen als auch zu höheren Punktwerten im statistischen Denken führen.

Der Koeffizient verändert sich von 0.59 zu 0.19.

**Evidenz schrittweise beurteilen**

Sein Betrag ist nach der Bereinigung kleiner.

Bei der Residualisierung wird zuerst die Variable **«Anzahl der Diskussionsbeiträge»** aus **«allgemeines Engagement»** vorhergesagt und danach die Variable **«Punktwert im statistischen Denken»** aus **«allgemeines Engagement»**.

Die partielle Korrelation ist die Korrelation zwischen den Abweichungen, die in diesen beiden Residualspalten verbleiben.

Ein kleinerer Betrag deutet darauf hin, dass die Kontrollvariable einen Teil des bivariaten Musters beschreibt.

Ein grösserer Betrag deutet auf Suppression hin: Die Bereinigung macht dann einen zuvor teilweise verdeckten Zusammenhang sichtbar.

**Schluss und Grenzen festhalten**

Keines der Ergebnisse stellt die zeitliche Reihenfolge her, schliesst nicht gemessene Variablen aus, behebt Messfehler oder ersetzt experimentelle Kontrolle.

Die Begründung von **«allgemeines Engagement»** als Kontrollvariable braucht fachliche und forschungsplanerische Argumente, darunter eine plausible zeitliche Reihenfolge und eine klare Rolle der Variable.

Die Koeffizienten allein liefern diese Begründung nicht.

Eine lineare Bereinigung entfernt nur den angepassten linearen Anteil im angegebenen Modell.

Nichtlineare Strukturen, Messprobleme und relevante nicht gemessene Variablen können bestehen bleiben.

### T06-A02-V10: Regelmässigkeit, gesamte Lernzeit und Behaltensleistung

**Fragestellung bestimmen**

Ein plausibles Diagramm lautet **Z → X, Z → Y und X ↔ Y**.

Es verbindet die Variable **«gesamte Lernzeit»** sowohl mit **«Regelmässigkeit des Übens»** als auch mit **«Behaltensleistung»**; die separate $X$-$Y$-Verbindung bleibt ein eigener Zusammenhang.

Eine mögliche inhaltliche Erklärung lautet: Die gesamte Lernzeit kann mit beiden Variablen positiv zusammenhängen und dabei den eigenständigen Zusammenhang zwischen regelmässigem Üben und der Behaltensleistung im bivariaten Koeffizienten teilweise verdecken.

Der Koeffizient verändert sich von 0.33 zu 0.47.

**Evidenz schrittweise beurteilen**

Sein Betrag ist nach der Bereinigung grösser.

Bei der Residualisierung wird zuerst die Variable **«Regelmässigkeit des Übens»** aus **«gesamte Lernzeit»** vorhergesagt und danach die Variable **«Behaltensleistung»** aus **«gesamte Lernzeit»**.

Die partielle Korrelation ist die Korrelation zwischen den Abweichungen, die in diesen beiden Residualspalten verbleiben.

Ein kleinerer Betrag deutet darauf hin, dass die Kontrollvariable einen Teil des bivariaten Musters beschreibt.

Ein grösserer Betrag deutet auf Suppression hin: Die Bereinigung macht dann einen zuvor teilweise verdeckten Zusammenhang sichtbar.

**Schluss und Grenzen festhalten**

Keines der Ergebnisse stellt die zeitliche Reihenfolge her, schliesst nicht gemessene Variablen aus, behebt Messfehler oder ersetzt experimentelle Kontrolle.

Die Begründung von **«gesamte Lernzeit»** als Kontrollvariable braucht fachliche und forschungsplanerische Argumente, darunter eine plausible zeitliche Reihenfolge und eine klare Rolle der Variable.

Die Koeffizienten allein liefern diese Begründung nicht.

Eine lineare Bereinigung entfernt nur den angepassten linearen Anteil im angegebenen Modell.

Nichtlineare Strukturen, Messprobleme und relevante nicht gemessene Variablen können bestehen bleiben.

# Teil II: Rechnerpraxis

## A01: Partielle Korrelation mit Residualisierung und direkter Formel

### T06-A01-V01: Übungszeit und statistisches Denken nach Bereinigung um den Ausgangswert

**Berechnung einrichten**

Abgesehen von der dargestellten Rundung haben beide Residualspalten den Mittelwert null.

Ihre Kreuzproduktsumme beträgt $\sum e_Xe_Y=15.4000$, während $\sum e_X^2=28.0000$ und $\sum e_Y^2=12.1171$ gelten.

**Berechnung durchführen**

Somit ist $r(e_X,e_Y)=15.4000/\sqrt{28.0000(12.1171)}=0.8361$.

Die direkte Formel ergibt $[0.8761-(0.5200)(0.4800)]/\sqrt{[1-(0.5200)^2][1-(0.4800)^2]}=0.8361$.

Kleine Unterschiede können entstehen, wenn die dargestellten Korrelationen vor dem Einsetzen in die Formel gerundet werden.

**Ergebnis interpretieren und prüfen**

Jedes Residuum ist die Differenz zwischen dem beobachteten Wert und dem Wert derselben Variable, der aus $Z$ linear vorhergesagt wurde.

Die Korrelation der beiden Residualspalten beschreibt, wie sich diese verbleibenden Abweichungen gemeinsam bewegen.

Sie bleibt ein bereinigter Zusammenhang und ist nicht automatisch ein kausaler Effekt.

### T06-A01-V02: Suchzeit und Genauigkeit nach Bereinigung um die Archiverfahrung

**Berechnung einrichten**

Abgesehen von der dargestellten Rundung haben beide Residualspalten den Mittelwert null.

Ihre Kreuzproduktsumme beträgt $\sum e_Xe_Y=-12.1000$, während $\sum e_X^2=28.0000$ und $\sum e_Y^2=9.6200$ gelten.

**Berechnung durchführen**

Somit ist $r(e_X,e_Y)=-12.1000/\sqrt{28.0000(9.6200)}=-0.7373$.

Die direkte Formel ergibt $[-0.7997-(-0.4600)(0.5500)]/\sqrt{[1-(-0.4600)^2][1-(0.5500)^2]}=-0.7373$.

Kleine Unterschiede können entstehen, wenn die dargestellten Korrelationen vor dem Einsetzen in die Formel gerundet werden.

**Ergebnis interpretieren und prüfen**

Jedes Residuum ist die Differenz zwischen dem beobachteten Wert und dem Wert derselben Variable, der aus $Z$ linear vorhergesagt wurde.

Die Korrelation der beiden Residualspalten beschreibt, wie sich diese verbleibenden Abweichungen gemeinsam bewegen.

Sie bleibt ein bereinigter Zusammenhang und ist nicht automatisch ein kausaler Effekt.

### T06-A01-V03: Lesezeit und Textverständnis nach Bereinigung um das Vorwissen

**Berechnung einrichten**

Abgesehen von der dargestellten Rundung haben beide Residualspalten den Mittelwert null.

Ihre Kreuzproduktsumme beträgt $\sum e_Xe_Y=13.8000$, während $\sum e_X^2=42.0000$ und $\sum e_Y^2=8.6971$ gelten.

**Berechnung durchführen**

Somit ist $r(e_X,e_Y)=13.8000/\sqrt{42.0000(8.6971)}=0.7220$.

Die direkte Formel ergibt $[0.7834-(0.5800)(0.4400)]/\sqrt{[1-(0.5800)^2][1-(0.4400)^2]}=0.7220$.

Kleine Unterschiede können entstehen, wenn die dargestellten Korrelationen vor dem Einsetzen in die Formel gerundet werden.

**Ergebnis interpretieren und prüfen**

Jedes Residuum ist die Differenz zwischen dem beobachteten Wert und dem Wert derselben Variable, der aus $Z$ linear vorhergesagt wurde.

Die Korrelation der beiden Residualspalten beschreibt, wie sich diese verbleibenden Abweichungen gemeinsam bewegen.

Sie bleibt ein bereinigter Zusammenhang und ist nicht automatisch ein kausaler Effekt.

### T06-A01-V04: Benachrichtigungen und Konzentration nach Bereinigung um die Arbeitslast

**Berechnung einrichten**

Abgesehen von der dargestellten Rundung haben beide Residualspalten den Mittelwert null.

Ihre Kreuzproduktsumme beträgt $\sum e_Xe_Y=-9.9000$, während $\sum e_X^2=28.0000$ und $\sum e_Y^2=7.4800$ gelten.

**Berechnung durchführen**

Somit ist $r(e_X,e_Y)=-9.9000/\sqrt{28.0000(7.4800)}=-0.6841$.

Die direkte Formel ergibt $[-0.7628-(-0.5100)(0.4900)]/\sqrt{[1-(-0.5100)^2][1-(0.4900)^2]}=-0.6841$.

Kleine Unterschiede können entstehen, wenn die dargestellten Korrelationen vor dem Einsetzen in die Formel gerundet werden.

**Ergebnis interpretieren und prüfen**

Jedes Residuum ist die Differenz zwischen dem beobachteten Wert und dem Wert derselben Variable, der aus $Z$ linear vorhergesagt wurde.

Die Korrelation der beiden Residualspalten beschreibt, wie sich diese verbleibenden Abweichungen gemeinsam bewegen.

Sie bleibt ein bereinigter Zusammenhang und ist nicht automatisch ein kausaler Effekt.

### T06-A01-V05: Museumsbesuche und Wissen nach Bereinigung um den Bildungsstand

**Berechnung einrichten**

Abgesehen von der dargestellten Rundung haben beide Residualspalten den Mittelwert null.

Ihre Kreuzproduktsumme beträgt $\sum e_Xe_Y=9.2000$, während $\sum e_X^2=42.0000$ und $\sum e_Y^2=5.3743$ gelten.

**Berechnung durchführen**

Somit ist $r(e_X,e_Y)=9.2000/\sqrt{42.0000(5.3743)}=0.6124$.

Die direkte Formel ergibt $[0.7074-(0.4700)(0.5300)]/\sqrt{[1-(0.4700)^2][1-(0.5300)^2]}=0.6124$.

Kleine Unterschiede können entstehen, wenn die dargestellten Korrelationen vor dem Einsetzen in die Formel gerundet werden.

**Ergebnis interpretieren und prüfen**

Jedes Residuum ist die Differenz zwischen dem beobachteten Wert und dem Wert derselben Variable, der aus $Z$ linear vorhergesagt wurde.

Die Korrelation der beiden Residualspalten beschreibt, wie sich diese verbleibenden Abweichungen gemeinsam bewegen.

Sie bleibt ein bereinigter Zusammenhang und ist nicht automatisch ein kausaler Effekt.

### T06-A01-V06: Streckenkenntnis und Reisezeit nach Bereinigung um die Streckenlänge

**Berechnung einrichten**

Abgesehen von der dargestellten Rundung haben beide Residualspalten den Mittelwert null.

Ihre Kreuzproduktsumme beträgt $\sum e_Xe_Y=-11.6000$, während $\sum e_X^2=28.0000$ und $\sum e_Y^2=7.8400$ gelten.

**Berechnung durchführen**

Somit ist $r(e_X,e_Y)=-11.6000/\sqrt{28.0000(7.8400)}=-0.7829$.

Die direkte Formel ergibt $[-0.8235-(-0.4300)(0.6000)]/\sqrt{[1-(-0.4300)^2][1-(0.6000)^2]}=-0.7829$.

Kleine Unterschiede können entstehen, wenn die dargestellten Korrelationen vor dem Einsetzen in die Formel gerundet werden.

**Ergebnis interpretieren und prüfen**

Jedes Residuum ist die Differenz zwischen dem beobachteten Wert und dem Wert derselben Variable, der aus $Z$ linear vorhergesagt wurde.

Die Korrelation der beiden Residualspalten beschreibt, wie sich diese verbleibenden Abweichungen gemeinsam bewegen.

Sie bleibt ein bereinigter Zusammenhang und ist nicht automatisch ein kausaler Effekt.

### T06-A01-V07: Workshopteilnahme und Selbstvertrauen nach Bereinigung um den Ausgangswert

**Berechnung einrichten**

Abgesehen von der dargestellten Rundung haben beide Residualspalten den Mittelwert null.

Ihre Kreuzproduktsumme beträgt $\sum e_Xe_Y=15.0000$, während $\sum e_X^2=42.0000$ und $\sum e_Y^2=8.1771$ gelten.

**Berechnung durchführen**

Somit ist $r(e_X,e_Y)=15.0000/\sqrt{42.0000(8.1771)}=0.8094$.

Die direkte Formel ergibt $[0.8300-(0.6200)(0.4000)]/\sqrt{[1-(0.6200)^2][1-(0.4000)^2]}=0.8094$.

Kleine Unterschiede können entstehen, wenn die dargestellten Korrelationen vor dem Einsetzen in die Formel gerundet werden.

**Ergebnis interpretieren und prüfen**

Jedes Residuum ist die Differenz zwischen dem beobachteten Wert und dem Wert derselben Variable, der aus $Z$ linear vorhergesagt wurde.

Die Korrelation der beiden Residualspalten beschreibt, wie sich diese verbleibenden Abweichungen gemeinsam bewegen.

Sie bleibt ein bereinigter Zusammenhang und ist nicht automatisch ein kausaler Effekt.

### T06-A01-V08: Aufgabenwechsel und Aufgabenerledigung nach Bereinigung um die Aufgabenlast

**Berechnung einrichten**

Abgesehen von der dargestellten Rundung haben beide Residualspalten den Mittelwert null.

Ihre Kreuzproduktsumme beträgt $\sum e_Xe_Y=-9.5000$, während $\sum e_X^2=28.0000$ und $\sum e_Y^2=6.7800$ gelten.

**Berechnung durchführen**

Somit ist $r(e_X,e_Y)=-9.5000/\sqrt{28.0000(6.7800)}=-0.6895$.

Die direkte Formel ergibt $[-0.7617-(-0.5500)(0.4500)]/\sqrt{[1-(-0.5500)^2][1-(0.4500)^2]}=-0.6895$.

Kleine Unterschiede können entstehen, wenn die dargestellten Korrelationen vor dem Einsetzen in die Formel gerundet werden.

**Ergebnis interpretieren und prüfen**

Jedes Residuum ist die Differenz zwischen dem beobachteten Wert und dem Wert derselben Variable, der aus $Z$ linear vorhergesagt wurde.

Die Korrelation der beiden Residualspalten beschreibt, wie sich diese verbleibenden Abweichungen gemeinsam bewegen.

Sie bleibt ein bereinigter Zusammenhang und ist nicht automatisch ein kausaler Effekt.

### T06-A01-V09: Diskussionsbeiträge und statistisches Denken nach Bereinigung um das Engagement

**Berechnung einrichten**

Abgesehen von der dargestellten Rundung haben beide Residualspalten den Mittelwert null.

Ihre Kreuzproduktsumme beträgt $\sum e_Xe_Y=13.2000$, während $\sum e_X^2=42.0000$ und $\sum e_Y^2=6.6743$ gelten.

**Berechnung durchführen**

Somit ist $r(e_X,e_Y)=13.2000/\sqrt{42.0000(6.6743)}=0.7884$.

Die direkte Formel ergibt $[0.8460-(0.5000)(0.5700)]/\sqrt{[1-(0.5000)^2][1-(0.5700)^2]}=0.7884$.

Kleine Unterschiede können entstehen, wenn die dargestellten Korrelationen vor dem Einsetzen in die Formel gerundet werden.

**Ergebnis interpretieren und prüfen**

Jedes Residuum ist die Differenz zwischen dem beobachteten Wert und dem Wert derselben Variable, der aus $Z$ linear vorhergesagt wurde.

Die Korrelation der beiden Residualspalten beschreibt, wie sich diese verbleibenden Abweichungen gemeinsam bewegen.

Sie bleibt ein bereinigter Zusammenhang und ist nicht automatisch ein kausaler Effekt.

### T06-A01-V10: Regelmässigkeit des Übens und Behaltensleistung nach Bereinigung um die Lernzeit

**Berechnung einrichten**

Abgesehen von der dargestellten Rundung haben beide Residualspalten den Mittelwert null.

Ihre Kreuzproduktsumme beträgt $\sum e_Xe_Y=9.4000$, während $\sum e_X^2=28.0000$ und $\sum e_Y^2=6.6686$ gelten.

**Berechnung durchführen**

Somit ist $r(e_X,e_Y)=9.4000/\sqrt{28.0000(6.6686)}=0.6879$.

Die direkte Formel ergibt $[0.7637-(0.5600)(0.4600)]/\sqrt{[1-(0.5600)^2][1-(0.4600)^2]}=0.6879$.

Kleine Unterschiede können entstehen, wenn die dargestellten Korrelationen vor dem Einsetzen in die Formel gerundet werden.

**Ergebnis interpretieren und prüfen**

Jedes Residuum ist die Differenz zwischen dem beobachteten Wert und dem Wert derselben Variable, der aus $Z$ linear vorhergesagt wurde.

Die Korrelation der beiden Residualspalten beschreibt, wie sich diese verbleibenden Abweichungen gemeinsam bewegen.

Sie bleibt ein bereinigter Zusammenhang und ist nicht automatisch ein kausaler Effekt.
