---
title: "Vollständige Lösungen"
subtitle: "Wahrscheinlichkeit"
document-id: "topic-02-probability-solutions-de"
topic-id: "topic-02-probability"
topic-number: "02"
topic-slug: "probability"
document-type: "solutions"
locale: "de"
paired-document-id: "topic-02-probability-exercises-de"
---

Diese vollständigen Lösungen verwenden dieselben Kennungen und dieselbe Reihenfolge wie das Übungsblatt. Zwischenwerte werden bis zum angegebenen Rundungsschritt beibehalten. Kleine Abweichungen durch früheres Runden sind deshalb dort zulässig, wo dies vermerkt ist. Alle Kontexte, Werte, Daten und Softwareausgaben sind eigens erstelltes Lehrmaterial; sie sind keine empirischen Befunde.

# Teil I: Theorie

## A08: Wahrscheinlichkeitsfunktionen und Dichten

### T02-A08-V01: Die Anzahl besuchter Ausstellungen und die in einem Museum verbrachte Zeit

**Fragestellung bestimmen, Teil (a)**

Weil $X$ die Anzahl besuchter Ausstellungen erfasst, besitzt die Variable einen abzählbaren Träger. Eine PMF kann jedem möglichen Zählwert die Masse $P(X=x)$ zuweisen. Weil $Y$ die in einem Museum verbrachte Zeit ist, wird die Variable in einem idealen stetigen Modell durch eine Dichte $f_Y(y)$ dargestellt.

**Evidenz schrittweise beurteilen, Teil (b)**

$P(X=x)$ kann für einen einzelnen Zählwert positiv sein, während $P(Y=y)=0$ an jedem einzelnen Punkt gilt, auch wenn Werte in seiner Nähe plausibel sind.

**Evidenz schrittweise beurteilen, Teil (c)**

Bei $X$ ist eine Intervallwahrscheinlichkeit die Summe der darin enthaltenen Massen. Bei $Y$ ist sie eine Fläche unter der Dichte, zum Beispiel $P(a<Y\leq b)=\int_a^b f_Y(y)\,dy$.

**Schluss und Grenzen festhalten, Teil (d)**

In beiden Fällen zeichnet eine CDF die angesammelte Wahrscheinlichkeit auf: $F_X(x)=P(X\leq x)$ springt bei den möglichen Zählwerten, während $F_Y(y)=P(Y\leq y)$ die Fläche unter der Dichte stetig ansammelt.

### T02-A08-V02: Die Anzahl empfangener Nachrichten und die Wartezeit bis zur nächsten Nachricht

**Fragestellung bestimmen, Teil (a)**

Weil $X$ die Anzahl empfangener Nachrichten erfasst, besitzt die Variable einen abzählbaren Träger. Eine PMF kann jedem möglichen Zählwert die Masse $P(X=x)$ zuweisen. Weil $Y$ die Wartezeit bis zur nächsten Nachricht ist, wird die Variable in einem idealen stetigen Modell durch eine Dichte $f_Y(y)$ dargestellt.

**Evidenz schrittweise beurteilen, Teil (b)**

$P(X=x)$ kann für einen einzelnen Zählwert positiv sein, während $P(Y=y)=0$ an jedem einzelnen Punkt gilt, auch wenn Werte in seiner Nähe plausibel sind.

**Evidenz schrittweise beurteilen, Teil (c)**

Bei $X$ ist eine Intervallwahrscheinlichkeit die Summe der darin enthaltenen Massen. Bei $Y$ ist sie eine Fläche unter der Dichte, zum Beispiel $P(a<Y\leq b)=\int_a^b f_Y(y)\,dy$.

**Schluss und Grenzen festhalten, Teil (d)**

In beiden Fällen zeichnet eine CDF die angesammelte Wahrscheinlichkeit auf: $F_X(x)=P(X\leq x)$ springt bei den möglichen Zählwerten, während $F_Y(y)=P(Y\leq y)$ die Fläche unter der Dichte stetig ansammelt.

### T02-A08-V03: Die Anzahl der Transkriptionsfehler und die Dauer eines Audioabschnitts

**Fragestellung bestimmen, Teil (a)**

Weil $X$ die Anzahl der Transkriptionsfehler erfasst, besitzt die Variable einen abzählbaren Träger. Eine PMF kann jedem möglichen Zählwert die Masse $P(X=x)$ zuweisen. Weil $Y$ die Dauer eines Audioabschnitts ist, wird die Variable in einem idealen stetigen Modell durch eine Dichte $f_Y(y)$ dargestellt.

**Evidenz schrittweise beurteilen, Teil (b)**

$P(X=x)$ kann für einen einzelnen Zählwert positiv sein, während $P(Y=y)=0$ an jedem einzelnen Punkt gilt, auch wenn Werte in seiner Nähe plausibel sind.

**Evidenz schrittweise beurteilen, Teil (c)**

Bei $X$ ist eine Intervallwahrscheinlichkeit die Summe der darin enthaltenen Massen. Bei $Y$ ist sie eine Fläche unter der Dichte, zum Beispiel $P(a<Y\leq b)=\int_a^b f_Y(y)\,dy$.

**Schluss und Grenzen festhalten, Teil (d)**

In beiden Fällen zeichnet eine CDF die angesammelte Wahrscheinlichkeit auf: $F_X(x)=P(X\leq x)$ springt bei den möglichen Zählwerten, während $F_Y(y)=P(Y\leq y)$ die Fläche unter der Dichte stetig ansammelt.

### T02-A08-V04: Die Anzahl ausgeliehener Bücher und die Masse eines zurückgesandten Pakets

**Fragestellung bestimmen, Teil (a)**

Weil $X$ die Anzahl ausgeliehener Bücher erfasst, besitzt die Variable einen abzählbaren Träger. Eine PMF kann jedem möglichen Zählwert die Masse $P(X=x)$ zuweisen. Weil $Y$ die Masse eines zurückgesandten Pakets ist, wird die Variable in einem idealen stetigen Modell durch eine Dichte $f_Y(y)$ dargestellt.

**Evidenz schrittweise beurteilen, Teil (b)**

$P(X=x)$ kann für einen einzelnen Zählwert positiv sein, während $P(Y=y)=0$ an jedem einzelnen Punkt gilt, auch wenn Werte in seiner Nähe plausibel sind.

**Evidenz schrittweise beurteilen, Teil (c)**

Bei $X$ ist eine Intervallwahrscheinlichkeit die Summe der darin enthaltenen Massen. Bei $Y$ ist sie eine Fläche unter der Dichte, zum Beispiel $P(a<Y\leq b)=\int_a^b f_Y(y)\,dy$.

**Schluss und Grenzen festhalten, Teil (d)**

In beiden Fällen zeichnet eine CDF die angesammelte Wahrscheinlichkeit auf: $F_X(x)=P(X\leq x)$ springt bei den möglichen Zählwerten, während $F_Y(y)=P(Y\leq y)$ die Fläche unter der Dichte stetig ansammelt.

### T02-A08-V05: Die Anzahl der Umfrageerinnerungen und die Bearbeitungszeit einer antwortenden Person

**Fragestellung bestimmen, Teil (a)**

Weil $X$ die Anzahl der Umfrageerinnerungen erfasst, besitzt die Variable einen abzählbaren Träger. Eine PMF kann jedem möglichen Zählwert die Masse $P(X=x)$ zuweisen. Weil $Y$ die Bearbeitungszeit einer antwortenden Person ist, wird die Variable in einem idealen stetigen Modell durch eine Dichte $f_Y(y)$ dargestellt.

**Evidenz schrittweise beurteilen, Teil (b)**

$P(X=x)$ kann für einen einzelnen Zählwert positiv sein, während $P(Y=y)=0$ an jedem einzelnen Punkt gilt, auch wenn Werte in seiner Nähe plausibel sind.

**Evidenz schrittweise beurteilen, Teil (c)**

Bei $X$ ist eine Intervallwahrscheinlichkeit die Summe der darin enthaltenen Massen. Bei $Y$ ist sie eine Fläche unter der Dichte, zum Beispiel $P(a<Y\leq b)=\int_a^b f_Y(y)\,dy$.

**Schluss und Grenzen festhalten, Teil (d)**

In beiden Fällen zeichnet eine CDF die angesammelte Wahrscheinlichkeit auf: $F_X(x)=P(X\leq x)$ springt bei den möglichen Zählwerten, während $F_Y(y)=P(Y\leq y)$ die Fläche unter der Dichte stetig ansammelt.

### T02-A08-V06: Die Anzahl der Routenänderungen und die zurückgelegte Distanz

**Fragestellung bestimmen, Teil (a)**

Weil $X$ die Anzahl der Routenänderungen erfasst, besitzt die Variable einen abzählbaren Träger. Eine PMF kann jedem möglichen Zählwert die Masse $P(X=x)$ zuweisen. Weil $Y$ die zurückgelegte Distanz ist, wird die Variable in einem idealen stetigen Modell durch eine Dichte $f_Y(y)$ dargestellt.

**Evidenz schrittweise beurteilen, Teil (b)**

$P(X=x)$ kann für einen einzelnen Zählwert positiv sein, während $P(Y=y)=0$ an jedem einzelnen Punkt gilt, auch wenn Werte in seiner Nähe plausibel sind.

**Evidenz schrittweise beurteilen, Teil (c)**

Bei $X$ ist eine Intervallwahrscheinlichkeit die Summe der darin enthaltenen Massen. Bei $Y$ ist sie eine Fläche unter der Dichte, zum Beispiel $P(a<Y\leq b)=\int_a^b f_Y(y)\,dy$.

**Schluss und Grenzen festhalten, Teil (d)**

In beiden Fällen zeichnet eine CDF die angesammelte Wahrscheinlichkeit auf: $F_X(x)=P(X\leq x)$ springt bei den möglichen Zählwerten, während $F_Y(y)=P(Y\leq y)$ die Fläche unter der Dichte stetig ansammelt.

### T02-A08-V07: Die Anzahl fehlender Felder und das präzise gemessene Alter einer teilnehmenden Person

**Fragestellung bestimmen, Teil (a)**

Weil $X$ die Anzahl fehlender Felder erfasst, besitzt die Variable einen abzählbaren Träger. Eine PMF kann jedem möglichen Zählwert die Masse $P(X=x)$ zuweisen. Weil $Y$ das präzise gemessene Alter einer teilnehmenden Person ist, wird die Variable in einem idealen stetigen Modell durch eine Dichte $f_Y(y)$ dargestellt.

**Evidenz schrittweise beurteilen, Teil (b)**

$P(X=x)$ kann für einen einzelnen Zählwert positiv sein, während $P(Y=y)=0$ an jedem einzelnen Punkt gilt, auch wenn Werte in seiner Nähe plausibel sind.

**Evidenz schrittweise beurteilen, Teil (c)**

Bei $X$ ist eine Intervallwahrscheinlichkeit die Summe der darin enthaltenen Massen. Bei $Y$ ist sie eine Fläche unter der Dichte, zum Beispiel $P(a<Y\leq b)=\int_a^b f_Y(y)\,dy$.

**Schluss und Grenzen festhalten, Teil (d)**

In beiden Fällen zeichnet eine CDF die angesammelte Wahrscheinlichkeit auf: $F_X(x)=P(X\leq x)$ springt bei den möglichen Zählwerten, während $F_Y(y)=P(Y\leq y)$ die Fläche unter der Dichte stetig ansammelt.

### T02-A08-V08: Die Anzahl der Workshopsitzungen und der Schallpegel im Raum

**Fragestellung bestimmen, Teil (a)**

Weil $X$ die Anzahl der Workshopsitzungen erfasst, besitzt die Variable einen abzählbaren Träger. Eine PMF kann jedem möglichen Zählwert die Masse $P(X=x)$ zuweisen. Weil $Y$ der Schallpegel im Raum ist, wird die Variable in einem idealen stetigen Modell durch eine Dichte $f_Y(y)$ dargestellt.

**Evidenz schrittweise beurteilen, Teil (b)**

$P(X=x)$ kann für einen einzelnen Zählwert positiv sein, während $P(Y=y)=0$ an jedem einzelnen Punkt gilt, auch wenn Werte in seiner Nähe plausibel sind.

**Evidenz schrittweise beurteilen, Teil (c)**

Bei $X$ ist eine Intervallwahrscheinlichkeit die Summe der darin enthaltenen Massen. Bei $Y$ ist sie eine Fläche unter der Dichte, zum Beispiel $P(a<Y\leq b)=\int_a^b f_Y(y)\,dy$.

**Schluss und Grenzen festhalten, Teil (d)**

In beiden Fällen zeichnet eine CDF die angesammelte Wahrscheinlichkeit auf: $F_X(x)=P(X\leq x)$ springt bei den möglichen Zählwerten, während $F_Y(y)=P(Y\leq y)$ die Fläche unter der Dichte stetig ansammelt.

### T02-A08-V09: Die Anzahl konservierter Fotografien und die Temperatur im Archiv

**Fragestellung bestimmen, Teil (a)**

Weil $X$ die Anzahl konservierter Fotografien erfasst, besitzt die Variable einen abzählbaren Träger. Eine PMF kann jedem möglichen Zählwert die Masse $P(X=x)$ zuweisen. Weil $Y$ die Temperatur im Archiv ist, wird die Variable in einem idealen stetigen Modell durch eine Dichte $f_Y(y)$ dargestellt.

**Evidenz schrittweise beurteilen, Teil (b)**

$P(X=x)$ kann für einen einzelnen Zählwert positiv sein, während $P(Y=y)=0$ an jedem einzelnen Punkt gilt, auch wenn Werte in seiner Nähe plausibel sind.

**Evidenz schrittweise beurteilen, Teil (c)**

Bei $X$ ist eine Intervallwahrscheinlichkeit die Summe der darin enthaltenen Massen. Bei $Y$ ist sie eine Fläche unter der Dichte, zum Beispiel $P(a<Y\leq b)=\int_a^b f_Y(y)\,dy$.

**Schluss und Grenzen festhalten, Teil (d)**

In beiden Fällen zeichnet eine CDF die angesammelte Wahrscheinlichkeit auf: $F_X(x)=P(X\leq x)$ springt bei den möglichen Zählwerten, während $F_Y(y)=P(Y\leq y)$ die Fläche unter der Dichte stetig ansammelt.

### T02-A08-V10: Die Anzahl erfolgreicher Prüfungen und die genaue Reaktionszeit bei einer Aufgabe

**Fragestellung bestimmen, Teil (a)**

Weil $X$ die Anzahl erfolgreicher Prüfungen erfasst, besitzt die Variable einen abzählbaren Träger. Eine PMF kann jedem möglichen Zählwert die Masse $P(X=x)$ zuweisen. Weil $Y$ die genaue Reaktionszeit bei einer Aufgabe ist, wird die Variable in einem idealen stetigen Modell durch eine Dichte $f_Y(y)$ dargestellt.

**Evidenz schrittweise beurteilen, Teil (b)**

$P(X=x)$ kann für einen einzelnen Zählwert positiv sein, während $P(Y=y)=0$ an jedem einzelnen Punkt gilt, auch wenn Werte in seiner Nähe plausibel sind.

**Evidenz schrittweise beurteilen, Teil (c)**

Bei $X$ ist eine Intervallwahrscheinlichkeit die Summe der darin enthaltenen Massen. Bei $Y$ ist sie eine Fläche unter der Dichte, zum Beispiel $P(a<Y\leq b)=\int_a^b f_Y(y)\,dy$.

**Schluss und Grenzen festhalten, Teil (d)**

In beiden Fällen zeichnet eine CDF die angesammelte Wahrscheinlichkeit auf: $F_X(x)=P(X\leq x)$ springt bei den möglichen Zählwerten, während $F_Y(y)=P(Y\leq y)$ die Fläche unter der Dichte stetig ansammelt.

## A14: Grundgesamtheit, Stichprobe und Auswahlverzerrung

### T02-A14-V01: QR-Befragung zur Parknutzung

**Fragestellung bestimmen, Teil (a)**

Zielpopulation: alle Einwohnerinnen und Einwohner der Stadt.

**Evidenz schrittweise beurteilen, Teil (b)**

Der operative Auswahlrahmen umfasst Personen, die während des Aushangs den grössten zentralen Park betreten, den Code bemerken und ihn scannen können. Die erreichte Stichprobe umfasst die 640 Parkbesuchenden, die den Code scannten und die Befragung abschickten. Diese Trennung ist wichtig: Der Rahmen beschreibt, wer oder was einen Weg zur Auswahl besass, während die Stichprobe die tatsächlich beobachteten Einheiten enthält.

**Evidenz schrittweise beurteilen, Teil (c)**

Passender Populationsparameter: der Anteil aller Einwohnerinnen und Einwohner der Stadt, die wöchentlich irgendeinen Park nutzen.

**Schluss und Grenzen festhalten, Teil (d)**

Stichprobenstatistik: der Anteil der 640 Antwortenden, die eine wöchentliche Parknutzung angeben. Die wichtigsten Gefahren sind designspezifisch: Personen, die Parks häufig nutzen, betreten diesen Park eher. Ausserdem können sich Personen, die einen Code bemerken und scannen, hinsichtlich Interesse oder digitalem Zugang von anderen unterscheiden. Eine grössere Stichprobe aus demselben Mechanismus würde die zufällige Stichprobenvariation um den rahmenspezifischen Wert dieses Mechanismus verringern. Diese grössere Stichprobe würde die identifizierten systematischen Abdeckungs- oder Auswahlmechanismen aber nicht reparieren. Ein besser begründeter Ansatz ist: Aus einem Register der Stadtbevölkerung eine Wahrscheinlichkeitsstichprobe ziehen und ausgewählte Nichtantwortende über mehrere Kontaktwege erneut anfragen.

### T02-A14-V02: Pendlerbefragung unter Inhabenden von Parkbewilligungen

**Fragestellung bestimmen, Teil (a)**

Zielpopulation: alle eingeschriebenen Studierenden.

**Evidenz schrittweise beurteilen, Teil (b)**

Der operative Auswahlrahmen umfasst die Liste der Universität mit Studierenden, die eine Parkbewilligung besitzen. Die erreichte Stichprobe umfasst die 820 Inhabenden einer Parkbewilligung, die antworteten. Diese Trennung ist wichtig: Der Rahmen beschreibt, wer oder was einen Weg zur Auswahl besass, während die Stichprobe die tatsächlich beobachteten Einheiten enthält.

**Evidenz schrittweise beurteilen, Teil (c)**

Passender Populationsparameter: die mittlere Pendelzeit aller eingeschriebenen Studierenden.

**Schluss und Grenzen festhalten, Teil (d)**

Stichprobenstatistik: die mittlere Pendelzeit der 820 Antwortenden. Die wichtigsten Gefahren sind designspezifisch: Der Auswahlrahmen lässt Studierende aus, die zu Fuss gehen, mit dem Fahrrad oder öffentlichen Verkehrsmitteln fahren oder keine Bewilligung besitzen. Die Antwortbereitschaft kann zudem von der Pendelbelastung abhängen. Eine grössere Stichprobe aus demselben Mechanismus würde die zufällige Stichprobenvariation um den rahmenspezifischen Wert dieses Mechanismus verringern. Diese grössere Stichprobe würde die identifizierten systematischen Abdeckungs- oder Auswahlmechanismen aber nicht reparieren. Ein besser begründeter Ansatz ist: Aus dem vollständigen Einschreiberegister ziehen, bei Bedarf nach wahrscheinlichem Verkehrsmittel schichten und bei den ausgewählten Studierenden nachfassen.

### T02-A14-V03: Zufriedenheit nach einer ausverkauften Ausstellung

**Fragestellung bestimmen, Teil (a)**

Zielpopulation: alle Museumsbesuchenden während der Zielsaison.

**Evidenz schrittweise beurteilen, Teil (b)**

Der operative Auswahlrahmen umfasst Besuchende beim Verlassen der ausverkauften Abendausstellung, denen die Ausgangsbefragung angeboten wurde. Die erreichte Stichprobe umfasst die 510 Anwesenden, die diese Ausgangsbefragung abschlossen. Diese Trennung ist wichtig: Der Rahmen beschreibt, wer oder was einen Weg zur Auswahl besass, während die Stichprobe die tatsächlich beobachteten Einheiten enthält.

**Evidenz schrittweise beurteilen, Teil (c)**

Passender Populationsparameter: der mittlere Zufriedenheitswert aller Besuchenden in der Zielsaison.

**Schluss und Grenzen festhalten, Teil (d)**

Stichprobenstatistik: der mittlere Zufriedenheitswert der 510 Antwortenden. Die wichtigsten Gefahren sind designspezifisch: Ein aussergewöhnlich beliebter Abend muss andere Daten oder Ausstellungen nicht repräsentieren. Ob jemand die Befragung abschliesst, kann zudem von einer besonders guten oder schlechten Erfahrung abhängen. Eine grössere Stichprobe aus demselben Mechanismus würde die zufällige Stichprobenvariation um den rahmenspezifischen Wert dieses Mechanismus verringern. Diese grössere Stichprobe würde die identifizierten systematischen Abdeckungs- oder Auswahlmechanismen aber nicht reparieren. Ein besser begründeter Ansatz ist: Besuche über verschiedene Ausstellungen, Tage und Zeiten auswählen, anschliessend eine Wahrscheinlichkeitsstichprobe der hinausgehenden Besuchenden einladen und Nichtantwort dokumentieren.

### T02-A14-V04: Befragung zum digitalen Zugang innerhalb einer App

**Fragestellung bestimmen, Teil (a)**

Zielpopulation: alle Bibliotheksnutzenden.

**Evidenz schrittweise beurteilen, Teil (b)**

Der operative Auswahlrahmen umfasst Bibliotheksnutzende, die die Smartphone-App verwenden und den Hinweis zur Befragung sehen konnten. Die erreichte Stichprobe umfasst die 430 App-Nutzenden, die freiwillig antworteten. Diese Trennung ist wichtig: Der Rahmen beschreibt, wer oder was einen Weg zur Auswahl besass, während die Stichprobe die tatsächlich beobachteten Einheiten enthält.

**Evidenz schrittweise beurteilen, Teil (c)**

Passender Populationsparameter: der Anteil aller Bibliotheksnutzenden, die einen besseren digitalen Zugang benötigen.

**Schluss und Grenzen festhalten, Teil (d)**

Stichprobenstatistik: der Anteil der 430 Antwortenden, die diesen Bedarf melden. Die wichtigsten Gefahren sind designspezifisch: Nutzende ohne geeignetes Gerät oder App-Zugang können nicht in den Auswahlrahmen gelangen. Freiwillige Antworten auf eine Befragung zum Zugang können zudem von besonders starkem Bedarf oder Engagement geprägt sein. Eine grössere Stichprobe aus demselben Mechanismus würde die zufällige Stichprobenvariation um den rahmenspezifischen Wert dieses Mechanismus verringern. Diese grössere Stichprobe würde die identifizierten systematischen Abdeckungs- oder Auswahlmechanismen aber nicht reparieren. Ein besser begründeter Ansatz ist: Aus dem vollständigen Nutzendenregister ziehen und zugängliche Antwortwege über Web, Telefon, Papier und persönliche Befragung anbieten.

### T02-A14-V05: Freiwilligenstunden aus Listen grosser Hilfsorganisationen

**Fragestellung bestimmen, Teil (a)**

Zielpopulation: alle Freiwilligen in der Region.

**Evidenz schrittweise beurteilen, Teil (b)**

Der operative Auswahlrahmen umfasst Mitgliederlisten, die von grossen registrierten Hilfsorganisationen bereitgestellt wurden. Die erreichte Stichprobe umfasst die 760 aufgeführten Mitglieder, deren Datensätze verwendet wurden. Diese Trennung ist wichtig: Der Rahmen beschreibt, wer oder was einen Weg zur Auswahl besass, während die Stichprobe die tatsächlich beobachteten Einheiten enthält.

**Evidenz schrittweise beurteilen, Teil (c)**

Passender Populationsparameter: die mittleren wöchentlichen Freiwilligenstunden aller Freiwilligen in der Region.

**Schluss und Grenzen festhalten, Teil (d)**

Stichprobenstatistik: die mittleren aufgezeichneten Wochenstunden dieser 760 aufgeführten Mitglieder. Die wichtigsten Gefahren sind designspezifisch: Die Listen lassen informell tätige Freiwillige sowie Mitglieder kleiner oder nicht registrierter Gruppen aus. Formelle Mitgliederdaten können regelmässig und langfristig tätige Personen überrepräsentieren. Eine grössere Stichprobe aus demselben Mechanismus würde die zufällige Stichprobenvariation um den rahmenspezifischen Wert dieses Mechanismus verringern. Diese grössere Stichprobe würde die identifizierten systematischen Abdeckungs- oder Auswahlmechanismen aber nicht reparieren. Ein besser begründeter Ansatz ist: Einen breiteren Auswahlrahmen aus verschiedenen Organisationstypen und Gemeinschaftsquellen aufbauen und innerhalb definierter Freiwilligenschichten zufällig auswählen.

### T02-A14-V06: Befragung zur Kursbelastung nach der Notenvergabe

**Fragestellung bestimmen, Teil (a)**

Zielpopulation: alle in den Kurs eingeschriebenen Studierenden.

**Evidenz schrittweise beurteilen, Teil (b)**

Der operative Auswahlrahmen umfasst eingeschriebene Studierende, deren Plattformkonten nach der Notenvergabe aktiv blieben. Die erreichte Stichprobe umfasst die 390 weiterhin aktiven Studierenden, die Angaben zur Belastung machten. Diese Trennung ist wichtig: Der Rahmen beschreibt, wer oder was einen Weg zur Auswahl besass, während die Stichprobe die tatsächlich beobachteten Einheiten enthält.

**Evidenz schrittweise beurteilen, Teil (c)**

Passender Populationsparameter: die mittlere wahrgenommene Belastung aller eingeschriebenen Studierenden.

**Schluss und Grenzen festhalten, Teil (d)**

Stichprobenstatistik: die von den 390 Antwortenden gemeldete mittlere Belastung. Die wichtigsten Gefahren sind designspezifisch: Studierende, die sich zurückzogen, den Kurs abbrachen oder die Plattform nicht mehr nutzten, fehlen. Die Antwortbereitschaft nach der Benotung kann mit der Belastung oder dem Kursergebnis zusammenhängen. Eine grössere Stichprobe aus demselben Mechanismus würde die zufällige Stichprobenvariation um den rahmenspezifischen Wert dieses Mechanismus verringern. Diese grössere Stichprobe würde die identifizierten systematischen Abdeckungs- oder Auswahlmechanismen aber nicht reparieren. Ein besser begründeter Ansatz ist: Aus der ursprünglichen Kursliste auswählen, die Studierenden unabhängig von ihrer späteren Plattformaktivität kontaktieren und bei Nichtantwort nachfassen.

### T02-A14-V07: Verkehrsverspätungen aus Kommentaren mit Hashtag

**Fragestellung bestimmen, Teil (a)**

Zielpopulation: alle Fahrten von Passagieren während des Zielzeitraums.

**Evidenz schrittweise beurteilen, Teil (b)**

Der operative Auswahlrahmen umfasst öffentlich abrufbare Kommentare in sozialen Medien, die den Kampagnen-Hashtag verwenden. Die erreichte Stichprobe umfasst die 1 240 abgerufenen Kommentare mit Hashtag. Diese Trennung ist wichtig: Der Rahmen beschreibt, wer oder was einen Weg zur Auswahl besass, während die Stichprobe die tatsächlich beobachteten Einheiten enthält.

**Evidenz schrittweise beurteilen, Teil (c)**

Passender Populationsparameter: der Anteil aller Fahrten, die als verspätet erlebt wurden.

**Schluss und Grenzen festhalten, Teil (d)**

Stichprobenstatistik: der Anteil der 1 240 Kommentare, die eine Verspätung beschreiben. Die wichtigsten Gefahren sind designspezifisch: Personen mit extremen Erfahrungen posten eher, eine Person kann mehrere Kommentare beitragen, und beobachtet werden Kommentare statt Fahrten. Eine grössere Stichprobe aus demselben Mechanismus würde die zufällige Stichprobenvariation um den rahmenspezifischen Wert dieses Mechanismus verringern. Diese grössere Stichprobe würde die identifizierten systematischen Abdeckungs- oder Auswahlmechanismen aber nicht reparieren. Ein besser begründeter Ansatz ist: Fahrten aus Betriebsdaten auswählen und zu jeder ausgewählten Fahrt eine Antwort erheben, wobei die Fahrt die Analyseeinheit bleibt.

### T02-A14-V08: Formulare zum Quartierinteresse nach Vorstellungen

**Fragestellung bestimmen, Teil (a)**

Zielpopulation: alle Einwohnerinnen und Einwohner des umliegenden Quartiers.

**Evidenz schrittweise beurteilen, Teil (b)**

Der operative Auswahlrahmen umfasst Personen mit Eintrittskarte, die die ausgewählten Vorstellungen verliessen und ein Formular angeboten bekamen. Die erreichte Stichprobe umfasst die 570 Personen, die blieben und ein Formular ausfüllten. Diese Trennung ist wichtig: Der Rahmen beschreibt, wer oder was einen Weg zur Auswahl besass, während die Stichprobe die tatsächlich beobachteten Einheiten enthält.

**Evidenz schrittweise beurteilen, Teil (c)**

Passender Populationsparameter: der Anteil der Quartierbevölkerung mit Interesse an künftigen Programmen.

**Schluss und Grenzen festhalten, Teil (d)**

Stichprobenstatistik: der Anteil der 570 Antwortenden, die Interesse äusserten. Die wichtigsten Gefahren sind designspezifisch: Personen, die nicht bereits Veranstaltungen mit Eintrittskarte besuchen, fehlen im Auswahlrahmen. Das Bleiben zum Ausfüllen kann mit der Begeisterung für das Zentrum zusammenhängen. Eine grössere Stichprobe aus demselben Mechanismus würde die zufällige Stichprobenvariation um den rahmenspezifischen Wert dieses Mechanismus verringern. Diese grössere Stichprobe würde die identifizierten systematischen Abdeckungs- oder Auswahlmechanismen aber nicht reparieren. Ein besser begründeter Ansatz ist: Einen Adressrahmen des Quartiers verwenden, Einwohnerinnen und Einwohner unabhängig vom Besuch auswählen und mehrere Antwortwege anbieten.

### T02-A14-V09: Schlafdaten von ganzjährig aktiven Wearable-Nutzenden

**Fragestellung bestimmen, Teil (a)**

Zielpopulation: alle Nutzenden in der beabsichtigten Wearable-Population während des Jahres.

**Evidenz schrittweise beurteilen, Teil (b)**

Der operative Auswahlrahmen umfasst Nutzende mit zu Beginn des Beobachtungszeitraums aktivierten Konten. Die erreichte Stichprobe umfasst die 680 ein Jahr lang verbliebenen Nutzenden mit vollständigen Schlafdaten. Diese Trennung ist wichtig: Der Rahmen beschreibt, wer oder was einen Weg zur Auswahl besass, während die Stichprobe die tatsächlich beobachteten Einheiten enthält.

**Evidenz schrittweise beurteilen, Teil (c)**

Passender Populationsparameter: die mittlere nächtliche Schlafdauer in der Population.

**Schluss und Grenzen festhalten, Teil (d)**

Stichprobenstatistik: die mittlere aufgezeichnete nächtliche Schlafdauer der verbliebenen Nutzenden. Die wichtigsten Gefahren sind designspezifisch: Die Bedingung einer einjährigen Nutzung schliesst unregelmässige oder früh ausgestiegene Personen aus. Verbleib und vollständiges Tragen können von Schlafgewohnheiten, Gesundheit oder Zufriedenheit mit dem Gerät abhängen. Eine grössere Stichprobe aus demselben Mechanismus würde die zufällige Stichprobenvariation um den rahmenspezifischen Wert dieses Mechanismus verringern. Diese grössere Stichprobe würde die identifizierten systematischen Abdeckungs- oder Auswahlmechanismen aber nicht reparieren. Ein besser begründeter Ansatz ist: Nutzende beim Eintritt auswählen, Teilaufzeichnungen nach einem vorab festgelegten Plan für fehlende Daten behalten und verbliebene mit verlorenen Teilnehmenden vergleichen.

### T02-A14-V10: Archivfeedback erst nach einem Download

**Fragestellung bestimmen, Teil (a)**

Zielpopulation: alle Suchversuche im Archiv während des Zielzeitraums.

**Evidenz schrittweise beurteilen, Teil (b)**

Der operative Auswahlrahmen umfasst Suchversuche, die mindestens einen Download erreichten und deshalb die Feedbackaufforderung erhielten. Die erreichte Stichprobe umfasst die 450 eingereichten Feedbackformulare aus diesem eingeschränkten Auswahlrahmen. Diese Trennung ist wichtig: Der Rahmen beschreibt, wer oder was einen Weg zur Auswahl besass, während die Stichprobe die tatsächlich beobachteten Einheiten enthält.

**Evidenz schrittweise beurteilen, Teil (c)**

Passender Populationsparameter: der Anteil aller Suchversuche, die mit einem erfolgreichen Abruf endeten.

**Schluss und Grenzen festhalten, Teil (d)**

Stichprobenstatistik: der Anteil der 450 Formulare, deren Absendende einen Erfolg melden. Die wichtigsten Gefahren sind designspezifisch: Die Aufforderung erscheint erst nach einem erfolgreichen Ereignis. Fehlgeschlagene Suchen haben daher keinen Weg in den Auswahlrahmen, und unter den Personen mit Download kann zusätzliche Selbstselektion auftreten. Eine grössere Stichprobe aus demselben Mechanismus würde die zufällige Stichprobenvariation um den rahmenspezifischen Wert dieses Mechanismus verringern. Diese grössere Stichprobe würde die identifizierten systematischen Abdeckungs- oder Auswahlmechanismen aber nicht reparieren. Ein besser begründeter Ansatz ist: Suchversuche beim Start auswählen, unabhängig von einem Download um Feedback bitten und jedem ausgewählten Versuch genau eine Antwortmöglichkeit zuordnen.

## A15: Abdeckungsfehler und die Population hinter einer Prozentzahl

### T02-A15-V01: Bildungsabschlüsse unter Fussballfans

**Fragestellung bestimmen, Teil (a)**

Die breite Behauptung nennt alle Personen, die Northport FC unterstützen.

**Evidenz schrittweise beurteilen, Teil (b)**

Einen Weg in die Berechnung hatten Plattformmitglieder, die Northport FC in einem sichtbaren Profil nennen und Bildungsangaben machen.

**Evidenz schrittweise beurteilen, Teil (c)**

Der Abdeckungsfehler entsteht aus folgendem Grund: Fans, die die berufliche Plattform nicht nutzen, den Verein nicht angeben oder keine Bildungsangabe machen, haben keinen Weg in die Prozentzahl. Die Plattformmitgliedschaft hängt zudem mit Bildung und Erwerbstätigkeit zusammen. Die Prozentzahl kann für die beobachteten Datensätze korrekt berechnet sein und dennoch den Anteil in der breiteren Population nicht schätzen.

**Schluss und Grenzen festhalten, Teil (d)**

Eine ehrliche deskriptive Aussage lautet: «Unter den analysierten Plattformprofilen, die Northport FC nannten und Bildungsangaben enthielten, meldeten 64% einen Hochschulabschluss.» Eine besser begründete Studie würde den Fanstatus zuerst definieren, Fans über einen nicht an die berufliche Plattform gebundenen Auswahlrahmen ziehen und ausgewählte Nichtantwortende erneut kontaktieren. Mehr Datensätze über denselben eingeschränkten Weg würden die Prozentzahl für diesen Rahmen präziser machen, aber keine Personengruppen hinzufügen, die nie in den Rahmen gelangen konnten.

### T02-A15-V02: Lesegewohnheiten aus einer E-Reader-Gemeinschaft

**Fragestellung bestimmen, Teil (a)**

Die breite Behauptung nennt alle Erwachsenen des Landes.

**Evidenz schrittweise beurteilen, Teil (b)**

Einen Weg in die Berechnung hatten Mitglieder des E-Reader-Forums, die die Einladung sahen und freiwillig antworteten.

**Evidenz schrittweise beurteilen, Teil (c)**

Der Abdeckungsfehler entsteht aus folgendem Grund: Erwachsene ohne E-Reader oder ohne Forum fehlen. Besonders engagierte Lesende treten dem Forum eher bei und antworten häufiger. Die Prozentzahl kann für die beobachteten Datensätze korrekt berechnet sein und dennoch den Anteil in der breiteren Population nicht schätzen.

**Schluss und Grenzen festhalten, Teil (d)**

Eine ehrliche deskriptive Aussage lautet: «Unter den antwortenden Mitgliedern dieses E-Reader-Forums gaben 71% an, mindestens zwei Bücher pro Monat zu beenden.» Eine besser begründete Studie würde aus einem populationsbasierten Auswahlrahmen für Erwachsene eine Wahrscheinlichkeitsstichprobe ziehen und mehrere Antwortwege anbieten. Mehr Datensätze über denselben eingeschränkten Weg würden die Prozentzahl für diesen Rahmen präziser machen, aber keine Personengruppen hinzufügen, die nie in den Rahmen gelangen konnten.

### T02-A15-V03: Fahrradnutzung aus einer Routenplanungs-App

**Fragestellung bestimmen, Teil (a)**

Die breite Behauptung nennt alle Einwohnerinnen und Einwohner der Stadt.

**Evidenz schrittweise beurteilen, Teil (b)**

Einen Weg in die Berechnung hatten aktive Nutzende der Fahrrad-App, die das Aufzeichnen von Fahrten erlauben.

**Evidenz schrittweise beurteilen, Teil (c)**

Der Abdeckungsfehler entsteht aus folgendem Grund: Personen ohne Fahrradnutzung, ohne App oder mit deaktivierter Aufzeichnung fehlen. Häufig Fahrende bleiben eher aktive Nutzende. Die Prozentzahl kann für die beobachteten Datensätze korrekt berechnet sein und dennoch den Anteil in der breiteren Population nicht schätzen.

**Schluss und Grenzen festhalten, Teil (d)**

Eine ehrliche deskriptive Aussage lautet: «Unter aktiven App-Nutzenden mit eingeschalteter Fahrtenaufzeichnung verzeichneten 58% mindestens drei Fahrten pro Woche.» Eine besser begründete Studie würde Personen aus einem Stadtregister ziehen und ihre Fahrradnutzung unabhängig von der App-Nutzung messen. Mehr Datensätze über denselben eingeschränkten Weg würden die Prozentzahl für diesen Rahmen präziser machen, aber keine Personengruppen hinzufügen, die nie in den Rahmen gelangen konnten.

### T02-A15-V04: Museumsinteresse unter Newsletter-Abonnierenden

**Fragestellung bestimmen, Teil (a)**

Die breite Behauptung nennt alle Einwohnerinnen und Einwohner der Region.

**Evidenz schrittweise beurteilen, Teil (b)**

Einen Weg in die Berechnung hatten Newsletter-Abonnierende des Museums, die die Nachricht öffneten und die Befragung abschlossen.

**Evidenz schrittweise beurteilen, Teil (c)**

Der Abdeckungsfehler entsteht aus folgendem Grund: Bereits am Museum interessierte Personen abonnieren, öffnen und beantworten den Newsletter eher. Die Prozentzahl kann für die beobachteten Datensätze korrekt berechnet sein und dennoch den Anteil in der breiteren Population nicht schätzen.

**Schluss und Grenzen festhalten, Teil (d)**

Eine ehrliche deskriptive Aussage lautet: «Unter den Newsletter-Abonnierenden, die antworteten, sagten 82%, dass sie die Ausstellung besuchen möchten.» Eine besser begründete Studie würde die Regionalbevölkerung unabhängig vom Newsletter-Abonnement ziehen und Nichtantwort dokumentieren. Mehr Datensätze über denselben eingeschränkten Weg würden die Prozentzahl für diesen Rahmen präziser machen, aber keine Personengruppen hinzufügen, die nie in den Rahmen gelangen konnten.

### T02-A15-V05: Präferenz für Fernarbeit auf einer Coworking-Plattform

**Fragestellung bestimmen, Teil (a)**

Die breite Behauptung nennt alle erwerbstätigen Erwachsenen der Zielregion.

**Evidenz schrittweise beurteilen, Teil (b)**

Einen Weg in die Berechnung hatten Kontoinhabende der Coworking-Plattform, die die Umfrage erhielten und beantworteten.

**Evidenz schrittweise beurteilen, Teil (c)**

Der Abdeckungsfehler entsteht aus folgendem Grund: Die Plattform überrepräsentiert Personen mit Berufen, die Fernarbeit erlauben. Freiwillige mit starken Präferenzen antworten möglicherweise häufiger. Die Prozentzahl kann für die beobachteten Datensätze korrekt berechnet sein und dennoch den Anteil in der breiteren Population nicht schätzen.

**Schluss und Grenzen festhalten, Teil (d)**

Eine ehrliche deskriptive Aussage lautet: «Unter den antwortenden Kontoinhabenden dieser Coworking-Plattform bevorzugten 76% an den meisten Wochentagen Fernarbeit.» Eine besser begründete Studie würde erwerbstätige Erwachsene über Berufe und Arbeitsformen hinweg aus einem geeigneten Arbeitskräfte-Auswahlrahmen ziehen. Mehr Datensätze über denselben eingeschränkten Weg würden die Prozentzahl für diesen Rahmen präziser machen, aber keine Personengruppen hinzufügen, die nie in den Rahmen gelangen konnten.

### T02-A15-V06: Sprachgebrauch aus öffentlichen Profilfeldern

**Fragestellung bestimmen, Teil (a)**

Die breite Behauptung nennt alle Einwohnerinnen und Einwohner des Landes.

**Evidenz schrittweise beurteilen, Teil (b)**

Einen Weg in die Berechnung hatten Plattformmitglieder mit öffentlichen Profilen, die mindestens eine Sprache aufführten.

**Evidenz schrittweise beurteilen, Teil (c)**

Der Abdeckungsfehler entsteht aus folgendem Grund: Plattformzugang und öffentliche Profilangaben unterscheiden sich in der Bevölkerung. Eine aufgeführte Sprache belegt zudem keine tägliche Verwendung. Die Prozentzahl kann für die beobachteten Datensätze korrekt berechnet sein und dennoch den Anteil in der breiteren Population nicht schätzen.

**Schluss und Grenzen festhalten, Teil (d)**

Eine ehrliche deskriptive Aussage lautet: «Von den öffentlichen Profilen mit Sprachfeld in den analysierten Plattformdaten führten 43% mindestens drei Sprachen auf.» Eine besser begründete Studie würde aus einem Auswahlrahmen der Bevölkerung ziehen und eine klar definierte Frage zum alltäglichen Sprachgebrauch stellen. Mehr Datensätze über denselben eingeschränkten Weg würden die Prozentzahl für diesen Rahmen präziser machen, aber keine Personengruppen hinzufügen, die nie in den Rahmen gelangen konnten.

### T02-A15-V07: Wohlbefinden von Studierenden aus einer Lernplanungs-App

**Fragestellung bestimmen, Teil (a)**

Die breite Behauptung nennt alle eingeschriebenen Studierenden an den interessierenden Universitäten.

**Evidenz schrittweise beurteilen, Teil (b)**

Einen Weg in die Berechnung hatten Nutzende der Lernplanungs-App, die die Frage zum Wohlbefinden bemerkten und beantworteten.

**Evidenz schrittweise beurteilen, Teil (c)**

Der Abdeckungsfehler entsteht aus folgendem Grund: Studierende mit einer Planungs-App können sich hinsichtlich Belastung oder Organisation unterscheiden. Die Antwortbereitschaft kann mit der aktuellen Belastung zusammenhängen. Die Prozentzahl kann für die beobachteten Datensätze korrekt berechnet sein und dennoch den Anteil in der breiteren Population nicht schätzen.

**Schluss und Grenzen festhalten, Teil (d)**

Eine ehrliche deskriptive Aussage lautet: «Unter den App-Nutzenden, die antworteten, meldeten 61% hohe akademische Belastung.» Eine besser begründete Studie würde aus vollständigen Einschreibelisten ziehen und die ausgewählten Studierenden über mehrere Wege kontaktieren. Mehr Datensätze über denselben eingeschränkten Weg würden die Prozentzahl für diesen Rahmen präziser machen, aber keine Personengruppen hinzufügen, die nie in den Rahmen gelangen konnten.

### T02-A15-V08: Konzertbesuch aus Profilen von Ticketkonten

**Fragestellung bestimmen, Teil (a)**

Die breite Behauptung nennt alle Personen der Zielbevölkerung.

**Evidenz schrittweise beurteilen, Teil (b)**

Einen Weg in die Berechnung hatten registrierte Ticketkonten mit beobachtbarer Aktivität beim Folgen von Seiten.

**Evidenz schrittweise beurteilen, Teil (c)**

Der Abdeckungsfehler entsteht aus folgendem Grund: Personen ohne Konto fehlen, eine Person kann mehrere Konten besitzen, und das Folgen einer Seite ist nicht dasselbe wie ein Konzertbesuch. Die Prozentzahl kann für die beobachteten Datensätze korrekt berechnet sein und dennoch den Anteil in der breiteren Population nicht schätzen.

**Schluss und Grenzen festhalten, Teil (d)**

Eine ehrliche deskriptive Aussage lautet: «Unter den beobachteten Ticketkonten folgten 67% im letzten Jahr mindestens einer Konzertseite.» Eine besser begründete Studie würde Personen statt Konten ziehen und ein klar definiertes Besuchsergebnis erfragen oder überprüfen. Mehr Datensätze über denselben eingeschränkten Weg würden die Prozentzahl für diesen Rahmen präziser machen, aber keine Personengruppen hinzufügen, die nie in den Rahmen gelangen konnten.

### T02-A15-V09: Zufriedenheit mit öffentlichen Verkehrsmitteln aus einer Mobile-Ticket-Stichprobe

**Fragestellung bestimmen, Teil (a)**

Die breite Behauptung nennt alle Fahrgäste des Verkehrssystems im Zielzeitraum.

**Evidenz schrittweise beurteilen, Teil (b)**

Einen Weg in die Berechnung hatten Fahrgäste, die ein Mobile-Ticket kauften und die Frage in der App erhielten.

**Evidenz schrittweise beurteilen, Teil (c)**

Der Abdeckungsfehler entsteht aus folgendem Grund: Nutzende von Bargeld, Papiertickets, Abonnementen oder Zugänglichkeitsdiensten können nicht in den Auswahlrahmen gelangen. Die Zufriedenheit kann zudem die Antwortbereitschaft beeinflussen. Die Prozentzahl kann für die beobachteten Datensätze korrekt berechnet sein und dennoch den Anteil in der breiteren Population nicht schätzen.

**Schluss und Grenzen festhalten, Teil (d)**

Eine ehrliche deskriptive Aussage lautet: «Unter den Mobile-Ticket-Nutzenden, die auf die Frage in der App antworteten, meldeten 74% Zufriedenheit.» Eine besser begründete Studie würde Fahrten über Ticketarten, Routen und Zeiten hinweg auswählen und die ausgewählten Fahrgäste über zugängliche Antwortwege einladen. Mehr Datensätze über denselben eingeschränkten Weg würden die Prozentzahl für diesen Rahmen präziser machen, aber keine Personengruppen hinzufügen, die nie in den Rahmen gelangen konnten.

### T02-A15-V10: Freiwilligenarbeit aus Webseiten von Organisationen

**Fragestellung bestimmen, Teil (a)**

Die breite Behauptung nennt alle formell und informell tätigen Freiwilligen der Region.

**Evidenz schrittweise beurteilen, Teil (b)**

Einen Weg in die Berechnung hatten Freiwillige, die von den in der Websuche enthaltenen grossen Hilfsorganisationen öffentlich aufgeführt werden.

**Evidenz schrittweise beurteilen, Teil (c)**

Der Abdeckungsfehler entsteht aus folgendem Grund: Informelle Freiwillige, kleine Organisationen und Personen ohne öffentliches Profil fehlen. Regelmässig Mitwirkende werden zudem eher vorgestellt. Die Prozentzahl kann für die beobachteten Datensätze korrekt berechnet sein und dennoch den Anteil in der breiteren Population nicht schätzen.

**Schluss und Grenzen festhalten, Teil (d)**

Eine ehrliche deskriptive Aussage lautet: «Unter den von den einbezogenen grossen Hilfsorganisationen öffentlich aufgeführten Freiwilligen wurden 69% als monatlich mitwirkend beschrieben.» Eine besser begründete Studie würde einen breiteren Auswahlrahmen über verschiedene Organisationsgrössen und informelle Gemeinschaftsarbeit aufbauen und daraus Freiwillige ziehen. Mehr Datensätze über denselben eingeschränkten Weg würden die Prozentzahl für diesen Rahmen präziser machen, aber keine Personengruppen hinzufügen, die nie in den Rahmen gelangen konnten.

## A16: Survivorship-Bias und fehlende Ergebnisse

### T02-A16-V01: Schadensmuster bei zurückgekehrten Lieferdrohnen

**Fragestellung bestimmen, Teil (a)**

Die beobachtete Gruppe enthält Drohnen, die trotz Beschädigung zurückkehrten und untersucht werden konnten.

**Evidenz schrittweise beurteilen, Teil (b)**

In dieser Gruppe fehlen Drohnen, die nicht zurückkehrten, darunter möglicherweise solche mit kritischen Schäden am Navigationsmodul.

**Evidenz schrittweise beurteilen, Teil (c)**

Der Auswahlprozess hängt mit dem Ergebnis zusammen: Ein Schaden am Navigationsmodul kann die Rückkehr verhindern. Die dort beobachtete geringe Zahl von Spuren kann deshalb starke Selektion statt Sicherheit anzeigen. Dies ist Survivorship-Bias. Damit ist gemeint, dass ein Fall für die Beobachtung verfügbar bleiben muss, obwohl gerade das Verschwinden wichtige Information tragen kann.

**Schluss und Grenzen festhalten, Teil (d)**

Wer nur die beobachteten Fälle untersucht, bedingt die Analyse auf Überleben, Abschluss, Rückkehr oder Verbleib. Dadurch können Misserfolge verborgen bleiben und die praktische Lehre kann sich umkehren. Der nächste Schritt ist: Protokolle gescheiterter Flüge und geborgene, nicht zurückgekehrte Drohnen untersuchen, bevor über die wertvollste Verstärkung entschieden wird. Das Ziel besteht nicht darin, fehlende Ergebnisse zu erraten. Die Erhebung soll vielmehr so gestaltet werden, dass fortbestehende und nicht fortbestehende Fälle Evidenz beitragen.

### T02-A16-V02: Lerngewohnheiten unter Personen mit Kursabschluss

**Fragestellung bestimmen, Teil (a)**

Die beobachtete Gruppe enthält Eingeschriebene, die bis zum Abschluss blieben und einem Interview zustimmten.

**Evidenz schrittweise beurteilen, Teil (b)**

In dieser Gruppe fehlen Studierende, die sich zurückzogen, sich nicht mehr anmeldeten oder dem Interview nicht zustimmten.

**Evidenz schrittweise beurteilen, Teil (c)**

Der Auswahlprozess hängt mit dem Ergebnis zusammen: Planungsgewohnheiten können mit dem Durchhalten zusammenhängen. Die Auswahl nach Kursabschluss kann die beobachtete Gewohnheit deshalb ungewöhnlich häufig erscheinen lassen. Dies ist Survivorship-Bias. Damit ist gemeint, dass ein Fall für die Beobachtung verfügbar bleiben muss, obwohl gerade das Verschwinden wichtige Information tragen kann.

**Schluss und Grenzen festhalten, Teil (d)**

Wer nur die beobachteten Fälle untersucht, bedingt die Analyse auf Überleben, Abschluss, Rückkehr oder Verbleib. Dadurch können Misserfolge verborgen bleiben und die praktische Lehre kann sich umkehren. Der nächste Schritt ist: die ursprüngliche Gruppe der Eingeschriebenen weiterverfolgen und vergleichbare Angaben von Personen mit und ohne Abschluss sammeln. Das Ziel besteht nicht darin, fehlende Ergebnisse zu erraten. Die Erhebung soll vielmehr so gestaltet werden, dass fortbestehende und nicht fortbestehende Fälle Evidenz beitragen.

### T02-A16-V03: Zuverlässigkeit noch eingesetzter Geräte

**Fragestellung bestimmen, Teil (a)**

Die beobachtete Gruppe enthält Sensoren, die zwei Jahre im Einsatz überstanden und für eine Untersuchung verfügbar blieben.

**Evidenz schrittweise beurteilen, Teil (b)**

In dieser Gruppe fehlen früher entfernte, entsorgte oder ersetzte Sensoren, möglicherweise weil Korrosion einen Ausfall verursachte.

**Evidenz schrittweise beurteilen, Teil (c)**

Der Auswahlprozess hängt mit dem Ergebnis zusammen: Das interessierende Ergebnis kann bestimmen, ob ein Sensor beobachtbar bleibt. Dadurch verbleiben die am wenigsten beschädigten Einheiten in der untersuchten Gruppe. Dies ist Survivorship-Bias. Damit ist gemeint, dass ein Fall für die Beobachtung verfügbar bleiben muss, obwohl gerade das Verschwinden wichtige Information tragen kann.

**Schluss und Grenzen festhalten, Teil (d)**

Wer nur die beobachteten Fälle untersucht, bedingt die Analyse auf Überleben, Abschluss, Rückkehr oder Verbleib. Dadurch können Misserfolge verborgen bleiben und die praktische Lehre kann sich umkehren. Der nächste Schritt ist: Wartungs- und Ersatzaufzeichnungen für die vollständige ursprüngliche Sensorkohorte einschliesslich ausgefallener Einheiten verwenden. Das Ziel besteht nicht darin, fehlende Ergebnisse zu erraten. Die Erhebung soll vielmehr so gestaltet werden, dass fortbestehende und nicht fortbestehende Fälle Evidenz beitragen.

### T02-A16-V04: Zufriedenheit unter wiederkehrenden Museumsbesuchenden

**Fragestellung bestimmen, Teil (a)**

Die beobachtete Gruppe enthält Besuchende, die zufrieden oder motiviert genug waren, mindestens viermal zurückzukehren und erneut zu kommen.

**Evidenz schrittweise beurteilen, Teil (b)**

In dieser Gruppe fehlen Personen mit nur einem Besuch und Personen, die nicht zurückkehrten.

**Evidenz schrittweise beurteilen, Teil (c)**

Der Auswahlprozess hängt mit dem Ergebnis zusammen: Frühere Zufriedenheit kann die Rückkehr beeinflussen. Eine Auswahl bei einem späteren Besuch filtert daher viele weniger zufriedene Erfahrungen heraus. Dies ist Survivorship-Bias. Damit ist gemeint, dass ein Fall für die Beobachtung verfügbar bleiben muss, obwohl gerade das Verschwinden wichtige Information tragen kann.

**Schluss und Grenzen festhalten, Teil (d)**

Wer nur die beobachteten Fälle untersucht, bedingt die Analyse auf Überleben, Abschluss, Rückkehr oder Verbleib. Dadurch können Misserfolge verborgen bleiben und die praktische Lehre kann sich umkehren. Der nächste Schritt ist: Erstbesuche auswählen und diese Personen unabhängig von einer späteren Rückkehr weiterverfolgen. Das Ziel besteht nicht darin, fehlende Ergebnisse zu erraten. Die Erhebung soll vielmehr so gestaltet werden, dass fortbestehende und nicht fortbestehende Fälle Evidenz beitragen.

### T02-A16-V05: Arbeitsbelastung aus Berichten verbliebener Mitarbeitender

**Fragestellung bestimmen, Teil (a)**

Die beobachtete Gruppe enthält Personen der Einstellungskohorte, die fünf Jahre blieben und antworteten.

**Evidenz schrittweise beurteilen, Teil (b)**

In dieser Gruppe fehlen Personen, die kündigten, entlassen wurden oder nach dem Austritt nicht erreichbar waren.

**Evidenz schrittweise beurteilen, Teil (c)**

Der Auswahlprozess hängt mit dem Ergebnis zusammen: Die Belastung im ersten Jahr kann das Verlassen beeinflussen. Verbliebene Mitarbeitende können daher systematisch andere Erfahrungen berichten. Dies ist Survivorship-Bias. Damit ist gemeint, dass ein Fall für die Beobachtung verfügbar bleiben muss, obwohl gerade das Verschwinden wichtige Information tragen kann.

**Schluss und Grenzen festhalten, Teil (d)**

Wer nur die beobachteten Fälle untersucht, bedingt die Analyse auf Überleben, Abschluss, Rückkehr oder Verbleib. Dadurch können Misserfolge verborgen bleiben und die praktische Lehre kann sich umkehren. Der nächste Schritt ist: Belastungsdaten vorausschauend für die vollständige Einstellungskohorte erheben und Austrittsinformationen aufbewahren. Das Ziel besteht nicht darin, fehlende Ergebnisse zu erraten. Die Erhebung soll vielmehr so gestaltet werden, dass fortbestehende und nicht fortbestehende Fälle Evidenz beitragen.

### T02-A16-V06: Genesung unter Personen mit abschliessender Nachkontrolle

**Fragestellung bestimmen, Teil (a)**

Die beobachtete Gruppe enthält behandelte Personen, die die letzte Nachkontrolle besuchten und ein Ergebnis lieferten.

**Evidenz schrittweise beurteilen, Teil (b)**

In dieser Gruppe fehlen Personen, die wegen Verschlechterung, Genesung an einem anderen Ort, Umzug oder Rückzug nicht zur Nachkontrolle kamen.

**Evidenz schrittweise beurteilen, Teil (c)**

Der Auswahlprozess hängt mit dem Ergebnis zusammen: Die Teilnahme an der Nachkontrolle kann vom Genesungsverlauf abhängen. Der beobachtete Anteil muss daher nicht alle behandelten Personen repräsentieren. Dies ist Survivorship-Bias. Damit ist gemeint, dass ein Fall für die Beobachtung verfügbar bleiben muss, obwohl gerade das Verschwinden wichtige Information tragen kann.

**Schluss und Grenzen festhalten, Teil (d)**

Wer nur die beobachteten Fälle untersucht, bedingt die Analyse auf Überleben, Abschluss, Rückkehr oder Verbleib. Dadurch können Misserfolge verborgen bleiben und die praktische Lehre kann sich umkehren. Der nächste Schritt ist: die vollständige Gruppe behandelter Personen verfolgen und mehrere geeignete Wege zur Erhebung der Ergebnisse bei versäumten Terminen verwenden. Das Ziel besteht nicht darin, fehlende Ergebnisse zu erraten. Die Erhebung soll vielmehr so gestaltet werden, dass fortbestehende und nicht fortbestehende Fälle Evidenz beitragen.

### T02-A16-V07: Haltbarkeit überlebender Archivdateien

**Fragestellung bestimmen, Teil (a)**

Die beobachtete Gruppe enthält Dateien, die überlebten, auffindbar blieben und noch geöffnet werden konnten.

**Evidenz schrittweise beurteilen, Teil (b)**

In dieser Gruppe fehlen verlorene, beschädigte oder nicht auffindbare Dateien, deren Metadaten möglicherweise zu ihrem Verschwinden beitrugen.

**Evidenz schrittweise beurteilen, Teil (c)**

Der Auswahlprozess hängt mit dem Ergebnis zusammen: Die Bedingung, dass eine Datei auffindbar und zu öffnen sein muss, kann genau die Ausfälle entfernen, die für die Beurteilung der Erhaltung nötig sind. Dies ist Survivorship-Bias. Damit ist gemeint, dass ein Fall für die Beobachtung verfügbar bleiben muss, obwohl gerade das Verschwinden wichtige Information tragen kann.

**Schluss und Grenzen festhalten, Teil (d)**

Wer nur die beobachteten Fälle untersucht, bedingt die Analyse auf Überleben, Abschluss, Rückkehr oder Verbleib. Dadurch können Misserfolge verborgen bleiben und die praktische Lehre kann sich umkehren. Der nächste Schritt ist: das ursprüngliche Dateiinventar prüfen und fehlende sowie beschädigte Dateien als Ergebnisse zählen statt sie auszuschliessen. Das Ziel besteht nicht darin, fehlende Ergebnisse zu erraten. Die Erhebung soll vielmehr so gestaltet werden, dass fortbestehende und nicht fortbestehende Fälle Evidenz beitragen.

### T02-A16-V08: Zuversicht unter Finalistinnen und Finalisten

**Fragestellung bestimmen, Teil (a)**

Die beobachtete Gruppe enthält Personen, die jede frühere Runde überstanden und das Finale erreichten.

**Evidenz schrittweise beurteilen, Teil (b)**

In dieser Gruppe fehlen Personen, die früher ausschieden oder sich zurückzogen.

**Evidenz schrittweise beurteilen, Teil (c)**

Der Auswahlprozess hängt mit dem Ergebnis zusammen: Anfängliche Zuversicht kann Leistung und Rückzug beeinflussen. Finalistinnen und Finalisten bilden daher eine ausgewählte Teilgruppe. Dies ist Survivorship-Bias. Damit ist gemeint, dass ein Fall für die Beobachtung verfügbar bleiben muss, obwohl gerade das Verschwinden wichtige Information tragen kann.

**Schluss und Grenzen festhalten, Teil (d)**

Wer nur die beobachteten Fälle untersucht, bedingt die Analyse auf Überleben, Abschluss, Rückkehr oder Verbleib. Dadurch können Misserfolge verborgen bleiben und die praktische Lehre kann sich umkehren. Der nächste Schritt ist: die Zuversicht aller Teilnehmenden vor der ersten Runde messen und ihren späteren Wettbewerbsstatus festhalten. Das Ziel besteht nicht darin, fehlende Ergebnisse zu erraten. Die Erhebung soll vielmehr so gestaltet werden, dass fortbestehende und nicht fortbestehende Fälle Evidenz beitragen.

### T02-A16-V09: Fahrzeiten aus abgeschlossenen App-Routen

**Fragestellung bestimmen, Teil (a)**

Die beobachtete Gruppe enthält aufgezeichnete Fahrten, die aktiv blieben, bis die App den Abschluss registrierte.

**Evidenz schrittweise beurteilen, Teil (b)**

In dieser Gruppe fehlen unterbrochene, abgebrochene oder aussergewöhnlich verzögerte Fahrten, deren App-Sitzung früh endete.

**Evidenz schrittweise beurteilen, Teil (c)**

Der Auswahlprozess hängt mit dem Ergebnis zusammen: Lange oder problematische Fahrten werden möglicherweise eher früh geschlossen. Dadurch können abgeschlossene Routen schneller erscheinen. Dies ist Survivorship-Bias. Damit ist gemeint, dass ein Fall für die Beobachtung verfügbar bleiben muss, obwohl gerade das Verschwinden wichtige Information tragen kann.

**Schluss und Grenzen festhalten, Teil (d)**

Wer nur die beobachteten Fälle untersucht, bedingt die Analyse auf Überleben, Abschluss, Rückkehr oder Verbleib. Dadurch können Misserfolge verborgen bleiben und die praktische Lehre kann sich umkehren. Der nächste Schritt ist: jede begonnene Fahrt als Teil der Kohorte definieren und unvollständige Routendaten untersuchen statt sie stillschweigend zu verwerfen. Das Ziel besteht nicht darin, fehlende Ergebnisse zu erraten. Die Erhebung soll vielmehr so gestaltet werden, dass fortbestehende und nicht fortbestehende Fälle Evidenz beitragen.

### T02-A16-V10: Lesefortschritt unter aktiven Abonnierenden

**Fragestellung bestimmen, Teil (a)**

Die beobachtete Gruppe enthält Abonnierende, die das ganze Jahr aktiv blieben und auswertbare Fortschrittsdaten hatten.

**Evidenz schrittweise beurteilen, Teil (b)**

In dieser Gruppe fehlen Personen, die kündigten oder deren Konto während des Jahres inaktiv wurde.

**Evidenz schrittweise beurteilen, Teil (c)**

Der Auswahlprozess hängt mit dem Ergebnis zusammen: Das Leseengagement kann die Kündigung beeinflussen. Aktive Abonnierende können deshalb ungewöhnlich hohe Fortschritte zeigen. Dies ist Survivorship-Bias. Damit ist gemeint, dass ein Fall für die Beobachtung verfügbar bleiben muss, obwohl gerade das Verschwinden wichtige Information tragen kann.

**Schluss und Grenzen festhalten, Teil (d)**

Wer nur die beobachteten Fälle untersucht, bedingt die Analyse auf Überleben, Abschluss, Rückkehr oder Verbleib. Dadurch können Misserfolge verborgen bleiben und die praktische Lehre kann sich umkehren. Der nächste Schritt ist: die ursprüngliche Abonnierendenkohorte in der Analyse behalten und den Fortschritt bis zur Kündigung erfassen oder ehemalige Abonnierende nachverfolgen. Das Ziel besteht nicht darin, fehlende Ergebnisse zu erraten. Die Erhebung soll vielmehr so gestaltet werden, dass fortbestehende und nicht fortbestehende Fälle Evidenz beitragen.

# Teil II: Rechnerpraxis

## A01: Sequenzielle bedingte Wahrscheinlichkeit

### T02-A01-V01: Eine Archivsuche abschliessen

**Berechnung einrichten, Teil (a)**

$A$, $B$ und $C$ bezeichnen der Reihe nach den Erfolg in den drei Schritten.

Nach der Kettenregel gilt $P(A\cap B)=P(A)P(B\mid A)=0.62\times 0.81=0.5022$.

**Berechnung durchführen, Teil (b)**

$P(A\cap B\cap C)=P(A)P(B\mid A)P(C\mid A\cap B)=0.62\times 0.81\times 0.74=0.3716$. Das Modell sagt somit, dass der Anteil 0.3716 die ganze Abfolge bis zum Schritt «den relevanten Brief bestimmen» abschliesst.

**Ergebnis interpretieren und prüfen, Teil (c)**

Nach den ersten beiden Erfolgen beträgt die bedingte Wahrscheinlichkeit eines Misserfolgs im dritten Schritt $1-0.74=0.26$. Daher ist $P(A\cap B\cap C')=0.62\times 0.81\times 0.26=0.1306$. Dies ist der modellierte Anteil, der den dritten Schritt erreicht, ihn aber nicht abschliesst. Die Wahrscheinlichkeiten späterer Schritte beziehen sich bereits auf durch frühere Erfolge eingeschränkte Gruppen. Unbedingte Randwahrscheinlichkeiten würden diese Bedingungen verwerfen.

### T02-A01-V02: Eine dreistufige Sprachprüfung bestehen

**Berechnung einrichten, Teil (a)**

$A$, $B$ und $C$ bezeichnen der Reihe nach den Erfolg in den drei Schritten.

Nach der Kettenregel gilt $P(A\cap B)=P(A)P(B\mid A)=0.68\times 0.77=0.5236$.

**Berechnung durchführen, Teil (b)**

$P(A\cap B\cap C)=P(A)P(B\mid A)P(C\mid A\cap B)=0.68\times 0.77\times 0.84=0.4398$. Das Modell sagt somit, dass der Anteil 0.4398 die ganze Abfolge bis zum Schritt «das Gespräch bestehen» abschliesst.

**Ergebnis interpretieren und prüfen, Teil (c)**

Nach den ersten beiden Erfolgen beträgt die bedingte Wahrscheinlichkeit eines Misserfolgs im dritten Schritt $1-0.84=0.16$. Daher ist $P(A\cap B\cap C')=0.68\times 0.77\times 0.16=0.0838$. Dies ist der modellierte Anteil, der den dritten Schritt erreicht, ihn aber nicht abschliesst. Die Wahrscheinlichkeiten späterer Schritte beziehen sich bereits auf durch frühere Erfolge eingeschränkte Gruppen. Unbedingte Randwahrscheinlichkeiten würden diese Bedingungen verwerfen.

### T02-A01-V03: Eine digitale Anmeldung abschliessen

**Berechnung einrichten, Teil (a)**

$A$, $B$ und $C$ bezeichnen der Reihe nach den Erfolg in den drei Schritten.

Nach der Kettenregel gilt $P(A\cap B)=P(A)P(B\mid A)=0.73\times 0.86=0.6278$.

**Berechnung durchführen, Teil (b)**

$P(A\cap B\cap C)=P(A)P(B\mid A)P(C\mid A\cap B)=0.73\times 0.86\times 0.79=0.4960$. Das Modell sagt somit, dass der Anteil 0.4960 die ganze Abfolge bis zum Schritt «die Einwilligungserklärung absenden» abschliesst.

**Ergebnis interpretieren und prüfen, Teil (c)**

Nach den ersten beiden Erfolgen beträgt die bedingte Wahrscheinlichkeit eines Misserfolgs im dritten Schritt $1-0.79=0.21$. Daher ist $P(A\cap B\cap C')=0.73\times 0.86\times 0.21=0.1318$. Dies ist der modellierte Anteil, der den dritten Schritt erreicht, ihn aber nicht abschliesst. Die Wahrscheinlichkeiten späterer Schritte beziehen sich bereits auf durch frühere Erfolge eingeschränkte Gruppen. Unbedingte Randwahrscheinlichkeiten würden diese Bedingungen verwerfen.

### T02-A01-V04: Eine Feldarbeitsabfolge lösen

**Berechnung einrichten, Teil (a)**

$A$, $B$ und $C$ bezeichnen der Reihe nach den Erfolg in den drei Schritten.

Nach der Kettenregel gilt $P(A\cap B)=P(A)P(B\mid A)=0.57\times 0.83=0.4731$.

**Berechnung durchführen, Teil (b)**

$P(A\cap B\cap C)=P(A)P(B\mid A)P(C\mid A\cap B)=0.57\times 0.83\times 0.91=0.4305$. Das Modell sagt somit, dass der Anteil 0.4305 die ganze Abfolge bis zum Schritt «den Datensatz korrekt hochladen» abschliesst.

**Ergebnis interpretieren und prüfen, Teil (c)**

Nach den ersten beiden Erfolgen beträgt die bedingte Wahrscheinlichkeit eines Misserfolgs im dritten Schritt $1-0.91=0.09$. Daher ist $P(A\cap B\cap C')=0.57\times 0.83\times 0.09=0.0426$. Dies ist der modellierte Anteil, der den dritten Schritt erreicht, ihn aber nicht abschliesst. Die Wahrscheinlichkeiten späterer Schritte beziehen sich bereits auf durch frühere Erfolge eingeschränkte Gruppen. Unbedingte Randwahrscheinlichkeiten würden diese Bedingungen verwerfen.

### T02-A01-V05: Eine Bibliotheksrecherche abschliessen

**Berechnung einrichten, Teil (a)**

$A$, $B$ und $C$ bezeichnen der Reihe nach den Erfolg in den drei Schritten.

Nach der Kettenregel gilt $P(A\cap B)=P(A)P(B\mid A)=0.66\times 0.72=0.4752$.

**Berechnung durchführen, Teil (b)**

$P(A\cap B\cap C)=P(A)P(B\mid A)P(C\mid A\cap B)=0.66\times 0.72\times 0.88=0.4182$. Das Modell sagt somit, dass der Anteil 0.4182 die ganze Abfolge bis zum Schritt «dessen Methoden korrekt beurteilen» abschliesst.

**Ergebnis interpretieren und prüfen, Teil (c)**

Nach den ersten beiden Erfolgen beträgt die bedingte Wahrscheinlichkeit eines Misserfolgs im dritten Schritt $1-0.88=0.12$. Daher ist $P(A\cap B\cap C')=0.66\times 0.72\times 0.12=0.0570$. Dies ist der modellierte Anteil, der den dritten Schritt erreicht, ihn aber nicht abschliesst. Die Wahrscheinlichkeiten späterer Schritte beziehen sich bereits auf durch frühere Erfolge eingeschränkte Gruppen. Unbedingte Randwahrscheinlichkeiten würden diese Bedingungen verwerfen.

### T02-A01-V06: In einem Musikvorspiel weiterkommen

**Berechnung einrichten, Teil (a)**

$A$, $B$ und $C$ bezeichnen der Reihe nach den Erfolg in den drei Schritten.

Nach der Kettenregel gilt $P(A\cap B)=P(A)P(B\mid A)=0.71\times 0.69=0.4899$.

**Berechnung durchführen, Teil (b)**

$P(A\cap B\cap C)=P(A)P(B\mid A)P(C\mid A\cap B)=0.71\times 0.69\times 0.82=0.4017$. Das Modell sagt somit, dass der Anteil 0.4017 die ganze Abfolge bis zum Schritt «die Aufgabe zum Blattspiel bestehen» abschliesst.

**Ergebnis interpretieren und prüfen, Teil (c)**

Nach den ersten beiden Erfolgen beträgt die bedingte Wahrscheinlichkeit eines Misserfolgs im dritten Schritt $1-0.82=0.18$. Daher ist $P(A\cap B\cap C')=0.71\times 0.69\times 0.18=0.0882$. Dies ist der modellierte Anteil, der den dritten Schritt erreicht, ihn aber nicht abschliesst. Die Wahrscheinlichkeiten späterer Schritte beziehen sich bereits auf durch frühere Erfolge eingeschränkte Gruppen. Unbedingte Randwahrscheinlichkeiten würden diese Bedingungen verwerfen.

### T02-A01-V07: Ein Laborprotokoll abschliessen

**Berechnung einrichten, Teil (a)**

$A$, $B$ und $C$ bezeichnen der Reihe nach den Erfolg in den drei Schritten.

Nach der Kettenregel gilt $P(A\cap B)=P(A)P(B\mid A)=0.64\times 0.87=0.5568$.

**Berechnung durchführen, Teil (b)**

$P(A\cap B\cap C)=P(A)P(B\mid A)P(C\mid A\cap B)=0.64\times 0.87\times 0.76=0.4232$. Das Modell sagt somit, dass der Anteil 0.4232 die ganze Abfolge bis zum Schritt «das Ergebnis korrekt beschriften» abschliesst.

**Ergebnis interpretieren und prüfen, Teil (c)**

Nach den ersten beiden Erfolgen beträgt die bedingte Wahrscheinlichkeit eines Misserfolgs im dritten Schritt $1-0.76=0.24$. Daher ist $P(A\cap B\cap C')=0.64\times 0.87\times 0.24=0.1336$. Dies ist der modellierte Anteil, der den dritten Schritt erreicht, ihn aber nicht abschliesst. Die Wahrscheinlichkeiten späterer Schritte beziehen sich bereits auf durch frühere Erfolge eingeschränkte Gruppen. Unbedingte Randwahrscheinlichkeiten würden diese Bedingungen verwerfen.

### T02-A01-V08: Einen Onlinekurs zur Sicherheit abschliessen

**Berechnung einrichten, Teil (a)**

$A$, $B$ und $C$ bezeichnen der Reihe nach den Erfolg in den drei Schritten.

Nach der Kettenregel gilt $P(A\cap B)=P(A)P(B\mid A)=0.78\times 0.75=0.5850$.

**Berechnung durchführen, Teil (b)**

$P(A\cap B\cap C)=P(A)P(B\mid A)P(C\mid A\cap B)=0.78\times 0.75\times 0.89=0.5206$. Das Modell sagt somit, dass der Anteil 0.5206 die ganze Abfolge bis zum Schritt «die abschliessende Reflexion einreichen» abschliesst.

**Ergebnis interpretieren und prüfen, Teil (c)**

Nach den ersten beiden Erfolgen beträgt die bedingte Wahrscheinlichkeit eines Misserfolgs im dritten Schritt $1-0.89=0.11$. Daher ist $P(A\cap B\cap C')=0.78\times 0.75\times 0.11=0.0643$. Dies ist der modellierte Anteil, der den dritten Schritt erreicht, ihn aber nicht abschliesst. Die Wahrscheinlichkeiten späterer Schritte beziehen sich bereits auf durch frühere Erfolge eingeschränkte Gruppen. Unbedingte Randwahrscheinlichkeiten würden diese Bedingungen verwerfen.

### T02-A01-V09: Eine Kartenleseaufgabe abschliessen

**Berechnung einrichten, Teil (a)**

$A$, $B$ und $C$ bezeichnen der Reihe nach den Erfolg in den drei Schritten.

Nach der Kettenregel gilt $P(A\cap B)=P(A)P(B\mid A)=0.59\times 0.82=0.4838$.

**Berechnung durchführen, Teil (b)**

$P(A\cap B\cap C)=P(A)P(B\mid A)P(C\mid A\cap B)=0.59\times 0.82\times 0.85=0.4112$. Das Modell sagt somit, dass der Anteil 0.4112 die ganze Abfolge bis zum Schritt «die letzte Landmarke erkennen» abschliesst.

**Ergebnis interpretieren und prüfen, Teil (c)**

Nach den ersten beiden Erfolgen beträgt die bedingte Wahrscheinlichkeit eines Misserfolgs im dritten Schritt $1-0.85=0.15$. Daher ist $P(A\cap B\cap C')=0.59\times 0.82\times 0.15=0.0726$. Dies ist der modellierte Anteil, der den dritten Schritt erreicht, ihn aber nicht abschliesst. Die Wahrscheinlichkeiten späterer Schritte beziehen sich bereits auf durch frühere Erfolge eingeschränkte Gruppen. Unbedingte Randwahrscheinlichkeiten würden diese Bedingungen verwerfen.

### T02-A01-V10: Eine Dateneingabeprüfung bestehen

**Berechnung einrichten, Teil (a)**

$A$, $B$ und $C$ bezeichnen der Reihe nach den Erfolg in den drei Schritten.

Nach der Kettenregel gilt $P(A\cap B)=P(A)P(B\mid A)=0.69\times 0.84=0.5796$.

**Berechnung durchführen, Teil (b)**

$P(A\cap B\cap C)=P(A)P(B\mid A)P(C\mid A\cap B)=0.69\times 0.84\times 0.73=0.4231$. Das Modell sagt somit, dass der Anteil 0.4231 die ganze Abfolge bis zum Schritt «den bereinigten Datensatz absenden» abschliesst.

**Ergebnis interpretieren und prüfen, Teil (c)**

Nach den ersten beiden Erfolgen beträgt die bedingte Wahrscheinlichkeit eines Misserfolgs im dritten Schritt $1-0.73=0.27$. Daher ist $P(A\cap B\cap C')=0.69\times 0.84\times 0.27=0.1565$. Dies ist der modellierte Anteil, der den dritten Schritt erreicht, ihn aber nicht abschliesst. Die Wahrscheinlichkeiten späterer Schritte beziehen sich bereits auf durch frühere Erfolge eingeschränkte Gruppen. Unbedingte Randwahrscheinlichkeiten würden diese Bedingungen verwerfen.

## A02: Gemeinsame unabhängige Ereignisse

### T02-A02-V01: Zwei unabhängige Qualitätsprüfungen

**Berechnung einrichten, Teil (b)**

Wegen der Unabhängigkeit ist $P(A\cap B)=P(A)P(B)=0.78\times 0.64=0.4992$. Dies ist die modellierte Wahrscheinlichkeit, dass eine gescannte Seite die Bildprüfung besteht und dieselbe Seite die Metadatenprüfung besteht. Für

ergibt die allgemeine Additionsregel $P(A\cup B)=0.78+0.64-0.4992=0.9208$. Das ist die Wahrscheinlichkeit, dass mindestens eines der beiden Ereignisse eintritt. Für

**Ergebnis interpretieren und prüfen, Teil (c)**

folgt aus der Unabhängigkeit von $A$ und $B$ auch die Unabhängigkeit von $A$ und $B'$. Deshalb gilt $P(A\cap B')=0.78(1-0.64)=0.2808$. Unabhängigkeit erlaubt, gemeinsame Wahrscheinlichkeiten durch Produkte zu ersetzen. Die Additionsregel selbst gilt mit und ohne Unabhängigkeit.

### T02-A02-V02: Unabhängige Teilnahme an Workshops

**Berechnung einrichten, Teil (b)**

Wegen der Unabhängigkeit ist $P(A\cap B)=P(A)P(B)=0.55\times 0.72=0.3960$. Dies ist die modellierte Wahrscheinlichkeit, dass eine Einwohnerin oder ein Einwohner die Morgensitzung besucht und dieselbe Person die Abendsitzung besucht. Für

ergibt die allgemeine Additionsregel $P(A\cup B)=0.55+0.72-0.3960=0.8740$. Das ist die Wahrscheinlichkeit, dass mindestens eines der beiden Ereignisse eintritt. Für

**Ergebnis interpretieren und prüfen, Teil (c)**

folgt aus der Unabhängigkeit von $A$ und $B$ auch die Unabhängigkeit von $A$ und $B'$. Deshalb gilt $P(A\cap B')=0.55(1-0.72)=0.1540$. Unabhängigkeit erlaubt, gemeinsame Wahrscheinlichkeiten durch Produkte zu ersetzen. Die Additionsregel selbst gilt mit und ohne Unabhängigkeit.

### T02-A02-V03: Zwei unabhängige Sensoralarme

**Berechnung einrichten, Teil (b)**

Wegen der Unabhängigkeit ist $P(A\cap B)=P(A)P(B)=0.18\times 0.27=0.0486$. Dies ist die modellierte Wahrscheinlichkeit, dass der Temperatursensor auslöst und der Vibrationssensor auslöst. Für

ergibt die allgemeine Additionsregel $P(A\cup B)=0.18+0.27-0.0486=0.4014$. Das ist die Wahrscheinlichkeit, dass mindestens eines der beiden Ereignisse eintritt. Für

**Ergebnis interpretieren und prüfen, Teil (c)**

folgt aus der Unabhängigkeit von $A$ und $B$ auch die Unabhängigkeit von $A$ und $B'$. Deshalb gilt $P(A\cap B')=0.18(1-0.27)=0.1314$. Unabhängigkeit erlaubt, gemeinsame Wahrscheinlichkeiten durch Produkte zu ersetzen. Die Additionsregel selbst gilt mit und ohne Unabhängigkeit.

### T02-A02-V04: Unabhängige Merkmale ausgewählter Bücher

**Berechnung einrichten, Teil (b)**

Wegen der Unabhängigkeit ist $P(A\cap B)=P(A)P(B)=0.36\times 0.41=0.1476$. Dies ist die modellierte Wahrscheinlichkeit, dass ein ausgewähltes Buch eine Übersetzung ist und es einen festen Einband hat. Für

ergibt die allgemeine Additionsregel $P(A\cup B)=0.36+0.41-0.1476=0.6224$. Das ist die Wahrscheinlichkeit, dass mindestens eines der beiden Ereignisse eintritt. Für

**Ergebnis interpretieren und prüfen, Teil (c)**

folgt aus der Unabhängigkeit von $A$ und $B$ auch die Unabhängigkeit von $A$ und $B'$. Deshalb gilt $P(A\cap B')=0.36(1-0.41)=0.2124$. Unabhängigkeit erlaubt, gemeinsame Wahrscheinlichkeiten durch Produkte zu ersetzen. Die Additionsregel selbst gilt mit und ohne Unabhängigkeit.

### T02-A02-V05: Unabhängige Ereignisse in einer Befragung

**Berechnung einrichten, Teil (b)**

Wegen der Unabhängigkeit ist $P(A\cap B)=P(A)P(B)=0.22\times 0.63=0.1386$. Dies ist die modellierte Wahrscheinlichkeit, dass eine Antwort am Montag eingeht und sie mit einem Mobilgerät abgeschickt wird. Für

ergibt die allgemeine Additionsregel $P(A\cup B)=0.22+0.63-0.1386=0.7114$. Das ist die Wahrscheinlichkeit, dass mindestens eines der beiden Ereignisse eintritt. Für

**Ergebnis interpretieren und prüfen, Teil (c)**

folgt aus der Unabhängigkeit von $A$ und $B$ auch die Unabhängigkeit von $A$ und $B'$. Deshalb gilt $P(A\cap B')=0.22(1-0.63)=0.0814$. Unabhängigkeit erlaubt, gemeinsame Wahrscheinlichkeiten durch Produkte zu ersetzen. Die Additionsregel selbst gilt mit und ohne Unabhängigkeit.

### T02-A02-V06: Zwei unabhängige Verkehrsereignisse

**Berechnung einrichten, Teil (b)**

Wegen der Unabhängigkeit ist $P(A\cap B)=P(A)P(B)=0.74\times 0.58=0.4292$. Dies ist die modellierte Wahrscheinlichkeit, dass ein Bus innerhalb von fünf Minuten ankommt und in einem Anschlusszug ein Sitzplatz frei ist. Für

ergibt die allgemeine Additionsregel $P(A\cup B)=0.74+0.58-0.4292=0.8908$. Das ist die Wahrscheinlichkeit, dass mindestens eines der beiden Ereignisse eintritt. Für

**Ergebnis interpretieren und prüfen, Teil (c)**

folgt aus der Unabhängigkeit von $A$ und $B$ auch die Unabhängigkeit von $A$ und $B'$. Deshalb gilt $P(A\cap B')=0.74(1-0.58)=0.3108$. Unabhängigkeit erlaubt, gemeinsame Wahrscheinlichkeiten durch Produkte zu ersetzen. Die Additionsregel selbst gilt mit und ohne Unabhängigkeit.

### T02-A02-V07: Unabhängige Codierungsprüfungen

**Berechnung einrichten, Teil (b)**

Wegen der Unabhängigkeit ist $P(A\cap B)=P(A)P(B)=0.83\times 0.69=0.5727$. Dies ist die modellierte Wahrscheinlichkeit, dass ein Datensatz ein gültiges Datum enthält und er einen gültigen Kategoriecode enthält. Für

ergibt die allgemeine Additionsregel $P(A\cup B)=0.83+0.69-0.5727=0.9473$. Das ist die Wahrscheinlichkeit, dass mindestens eines der beiden Ereignisse eintritt. Für

**Ergebnis interpretieren und prüfen, Teil (c)**

folgt aus der Unabhängigkeit von $A$ und $B$ auch die Unabhängigkeit von $A$ und $B'$. Deshalb gilt $P(A\cap B')=0.83(1-0.69)=0.2573$. Unabhängigkeit erlaubt, gemeinsame Wahrscheinlichkeiten durch Produkte zu ersetzen. Die Additionsregel selbst gilt mit und ohne Unabhängigkeit.

### T02-A02-V08: Zwei unabhängige Ziehungen

**Berechnung einrichten, Teil (b)**

Wegen der Unabhängigkeit ist $P(A\cap B)=P(A)P(B)=0.45\times 0.32=0.1440$. Dies ist die modellierte Wahrscheinlichkeit, dass ein ausgewählter Spielstein blau ist und bei einer zweiten Ziehung mit Zurücklegen ein Dreieck gezogen wird. Für

ergibt die allgemeine Additionsregel $P(A\cup B)=0.45+0.32-0.1440=0.6260$. Das ist die Wahrscheinlichkeit, dass mindestens eines der beiden Ereignisse eintritt. Für

**Ergebnis interpretieren und prüfen, Teil (c)**

folgt aus der Unabhängigkeit von $A$ und $B$ auch die Unabhängigkeit von $A$ und $B'$. Deshalb gilt $P(A\cap B')=0.45(1-0.32)=0.3060$. Unabhängigkeit erlaubt, gemeinsame Wahrscheinlichkeiten durch Produkte zu ersetzen. Die Additionsregel selbst gilt mit und ohne Unabhängigkeit.

### T02-A02-V09: Unabhängige Studienereignisse

**Berechnung einrichten, Teil (b)**

Wegen der Unabhängigkeit ist $P(A\cap B)=P(A)P(B)=0.67\times 0.88=0.5896$. Dies ist die modellierte Wahrscheinlichkeit, dass eine teilnehmende Person das Tagebuch abschliesst und die Labordatei erfolgreich hochgeladen wird. Für

ergibt die allgemeine Additionsregel $P(A\cup B)=0.67+0.88-0.5896=0.9604$. Das ist die Wahrscheinlichkeit, dass mindestens eines der beiden Ereignisse eintritt. Für

**Ergebnis interpretieren und prüfen, Teil (c)**

folgt aus der Unabhängigkeit von $A$ und $B$ auch die Unabhängigkeit von $A$ und $B'$. Deshalb gilt $P(A\cap B')=0.67(1-0.88)=0.0804$. Unabhängigkeit erlaubt, gemeinsame Wahrscheinlichkeiten durch Produkte zu ersetzen. Die Additionsregel selbst gilt mit und ohne Unabhängigkeit.

### T02-A02-V10: Unabhängige Katalogmerkmale

**Berechnung einrichten, Teil (b)**

Wegen der Unabhängigkeit ist $P(A\cap B)=P(A)P(B)=0.39\times 0.76=0.2964$. Dies ist die modellierte Wahrscheinlichkeit, dass ein Objekt digitalisiert ist und sein Feld zur Urheberschaft vollständig ist. Für

ergibt die allgemeine Additionsregel $P(A\cup B)=0.39+0.76-0.2964=0.8536$. Das ist die Wahrscheinlichkeit, dass mindestens eines der beiden Ereignisse eintritt. Für

**Ergebnis interpretieren und prüfen, Teil (c)**

folgt aus der Unabhängigkeit von $A$ und $B$ auch die Unabhängigkeit von $A$ und $B'$. Deshalb gilt $P(A\cap B')=0.39(1-0.76)=0.0936$. Unabhängigkeit erlaubt, gemeinsame Wahrscheinlichkeiten durch Produkte zu ersetzen. Die Additionsregel selbst gilt mit und ohne Unabhängigkeit.

## A03: Kontingenztafeln und Beziehungen zwischen Ereignissen

### T02-A03-V01: Leseformat und Kursabschluss

**Vor dem Rechnen begründen, Teil (a)**

Für die Zeile Audio ist $P(Y\mid G)=12/30=0.4000$, für die Zeile Text ist $P(Y\mid G^c)=28/70=0.4000$. Diese bedingten Anteile sind gleich, daher sind die Variablen in dieser empirischen Tabelle unabhängig. Dies beschreibt die gezeigte empirische Verteilung und beweist nicht dieselbe Beziehung in einer grösseren Grundgesamtheit.

**Berechnung durchführen, Teil (b)**

Der Schnitt von Audio und Abgeschlossen enthält 12 der 100 Beobachtungen. Somit ist $P(G\cap Y)=12/100=0.1200$.

**Ergebnis interpretieren und prüfen, Teil (c)**

$G$ und $Y$ sind nicht disjunkt, weil dieser Schnitt nicht leer ist. Bei disjunkten Ereignissen wäre die Häufigkeit im Schnitt null.

### T02-A03-V02: Museumsmitgliedschaft und Veranstaltungsbesuch

**Vor dem Rechnen begründen, Teil (a)**

Für die Zeile Mitglied ist $P(Y\mid G)=24/40=0.6000$, für die Zeile Nichtmitglied ist $P(Y\mid G^c)=18/60=0.3000$. Diese bedingten Anteile sind verschieden, daher sind die Variablen in dieser empirischen Tabelle nicht unabhängig. Dies beschreibt die gezeigte empirische Verteilung und beweist nicht dieselbe Beziehung in einer grösseren Grundgesamtheit.

**Berechnung durchführen, Teil (b)**

Der Schnitt von Mitglied und Teilgenommen enthält 24 der 100 Beobachtungen. Somit ist $P(G\cap Y)=24/100=0.2400$.

**Ergebnis interpretieren und prüfen, Teil (c)**

$G$ und $Y$ sind nicht disjunkt, weil dieser Schnitt nicht leer ist. Bei disjunkten Ereignissen wäre die Häufigkeit im Schnitt null.

### T02-A03-V03: Lernort und Einhaltung der Frist

**Vor dem Rechnen begründen, Teil (a)**

Für die Zeile Bibliothek ist $P(Y\mid G)=21/35=0.6000$, für die Zeile Zuhause ist $P(Y\mid G^c)=27/45=0.6000$. Diese bedingten Anteile sind gleich, daher sind die Variablen in dieser empirischen Tabelle unabhängig. Dies beschreibt die gezeigte empirische Verteilung und beweist nicht dieselbe Beziehung in einer grösseren Grundgesamtheit.

**Berechnung durchführen, Teil (b)**

Der Schnitt von Bibliothek und Fristgerecht enthält 21 der 80 Beobachtungen. Somit ist $P(G\cap Y)=21/80=0.2625$.

**Ergebnis interpretieren und prüfen, Teil (c)**

$G$ und $Y$ sind nicht disjunkt, weil dieser Schnitt nicht leer ist. Bei disjunkten Ereignissen wäre die Häufigkeit im Schnitt null.

### T02-A03-V04: Untertitel und Quizabschluss

**Vor dem Rechnen begründen, Teil (a)**

Für die Zeile Untertitel ist $P(Y\mid G)=30/50=0.6000$, für die Zeile Keine Untertitel ist $P(Y\mid G^c)=18/30=0.6000$. Diese bedingten Anteile sind gleich, daher sind die Variablen in dieser empirischen Tabelle unabhängig. Dies beschreibt die gezeigte empirische Verteilung und beweist nicht dieselbe Beziehung in einer grösseren Grundgesamtheit.

**Berechnung durchführen, Teil (b)**

Der Schnitt von Untertitel und Abgeschlossen enthält 30 der 80 Beobachtungen. Somit ist $P(G\cap Y)=30/80=0.3750$.

**Ergebnis interpretieren und prüfen, Teil (c)**

$G$ und $Y$ sind nicht disjunkt, weil dieser Schnitt nicht leer ist. Bei disjunkten Ereignissen wäre die Häufigkeit im Schnitt null.

### T02-A03-V05: Verkehrsabonnement und Campusbesuche

**Vor dem Rechnen begründen, Teil (a)**

Für die Zeile Abonnement ist $P(Y\mid G)=16/40=0.4000$, für die Zeile Kein Abonnement ist $P(Y\mid G^c)=14/60=0.2333$. Diese bedingten Anteile sind verschieden, daher sind die Variablen in dieser empirischen Tabelle nicht unabhängig. Dies beschreibt die gezeigte empirische Verteilung und beweist nicht dieselbe Beziehung in einer grösseren Grundgesamtheit.

**Berechnung durchführen, Teil (b)**

Der Schnitt von Abonnement und Häufig enthält 16 der 100 Beobachtungen. Somit ist $P(G\cap Y)=16/100=0.1600$.

**Ergebnis interpretieren und prüfen, Teil (c)**

$G$ und $Y$ sind nicht disjunkt, weil dieser Schnitt nicht leer ist. Bei disjunkten Ereignissen wäre die Häufigkeit im Schnitt null.

### T02-A03-V06: Erinnerung und Antwort

**Vor dem Rechnen begründen, Teil (a)**

Für die Zeile Erinnerung ist $P(Y\mid G)=27/40=0.6750$, für die Zeile Keine Erinnerung ist $P(Y\mid G^c)=33/60=0.5500$. Diese bedingten Anteile sind verschieden, daher sind die Variablen in dieser empirischen Tabelle nicht unabhängig. Dies beschreibt die gezeigte empirische Verteilung und beweist nicht dieselbe Beziehung in einer grösseren Grundgesamtheit.

**Berechnung durchführen, Teil (b)**

Der Schnitt von Erinnerung und Geantwortet enthält 27 der 100 Beobachtungen. Somit ist $P(G\cap Y)=27/100=0.2700$.

**Ergebnis interpretieren und prüfen, Teil (c)**

$G$ und $Y$ sind nicht disjunkt, weil dieser Schnitt nicht leer ist. Bei disjunkten Ereignissen wäre die Häufigkeit im Schnitt null.

### T02-A03-V07: Workshop-Schwerpunkt und Zertifizierung

**Vor dem Rechnen begründen, Teil (a)**

Für die Zeile Methoden ist $P(Y\mid G)=18/30=0.6000$, für die Zeile Schreiben ist $P(Y\mid G^c)=24/60=0.4000$. Diese bedingten Anteile sind verschieden, daher sind die Variablen in dieser empirischen Tabelle nicht unabhängig. Dies beschreibt die gezeigte empirische Verteilung und beweist nicht dieselbe Beziehung in einer grösseren Grundgesamtheit.

**Berechnung durchführen, Teil (b)**

Der Schnitt von Methoden und Zertifiziert enthält 18 der 90 Beobachtungen. Somit ist $P(G\cap Y)=18/90=0.2000$.

**Ergebnis interpretieren und prüfen, Teil (c)**

$G$ und $Y$ sind nicht disjunkt, weil dieser Schnitt nicht leer ist. Bei disjunkten Ereignissen wäre die Häufigkeit im Schnitt null.

### T02-A03-V08: Gerätetyp und Formularabschluss

**Vor dem Rechnen begründen, Teil (a)**

Für die Zeile Tablet ist $P(Y\mid G)=14/35=0.4000$, für die Zeile Laptop ist $P(Y\mid G^c)=30/45=0.6667$. Diese bedingten Anteile sind verschieden, daher sind die Variablen in dieser empirischen Tabelle nicht unabhängig. Dies beschreibt die gezeigte empirische Verteilung und beweist nicht dieselbe Beziehung in einer grösseren Grundgesamtheit.

**Berechnung durchführen, Teil (b)**

Der Schnitt von Tablet und Vollständig enthält 14 der 80 Beobachtungen. Somit ist $P(G\cap Y)=14/80=0.1750$.

**Ergebnis interpretieren und prüfen, Teil (c)**

$G$ und $Y$ sind nicht disjunkt, weil dieser Schnitt nicht leer ist. Bei disjunkten Ereignissen wäre die Häufigkeit im Schnitt null.

### T02-A03-V09: Freiwilligenrolle und erneuter Besuch

**Vor dem Rechnen begründen, Teil (a)**

Für die Zeile Führung ist $P(Y\mid G)=22/40=0.5500$, für die Zeile Archiv ist $P(Y\mid G^c)=11/40=0.2750$. Diese bedingten Anteile sind verschieden, daher sind die Variablen in dieser empirischen Tabelle nicht unabhängig. Dies beschreibt die gezeigte empirische Verteilung und beweist nicht dieselbe Beziehung in einer grösseren Grundgesamtheit.

**Berechnung durchführen, Teil (b)**

Der Schnitt von Führung und Zurückgekehrt enthält 22 der 80 Beobachtungen. Somit ist $P(G\cap Y)=22/80=0.2750$.

**Ergebnis interpretieren und prüfen, Teil (c)**

$G$ und $Y$ sind nicht disjunkt, weil dieser Schnitt nicht leer ist. Bei disjunkten Ereignissen wäre die Häufigkeit im Schnitt null.

### T02-A03-V10: Tutorialformat und Abgabe der Übung

**Vor dem Rechnen begründen, Teil (a)**

Für die Zeile Live ist $P(Y\mid G)=26/40=0.6500$, für die Zeile Aufgezeichnet ist $P(Y\mid G^c)=39/60=0.6500$. Diese bedingten Anteile sind gleich, daher sind die Variablen in dieser empirischen Tabelle unabhängig. Dies beschreibt die gezeigte empirische Verteilung und beweist nicht dieselbe Beziehung in einer grösseren Grundgesamtheit.

**Berechnung durchführen, Teil (b)**

Der Schnitt von Live und Eingereicht enthält 26 der 100 Beobachtungen. Somit ist $P(G\cap Y)=26/100=0.2600$.

**Ergebnis interpretieren und prüfen, Teil (c)**

$G$ und $Y$ sind nicht disjunkt, weil dieser Schnitt nicht leer ist. Bei disjunkten Ereignissen wäre die Häufigkeit im Schnitt null.

## A04: Satz von Bayes und Basisraten

### T02-A04-V01: Screening auf Unterstützungsbedarf bei Barrierefreiheit

**Vor dem Rechnen begründen, Teil (a)**

Die falsch-positive Wahrscheinlichkeit ist $1-0.91=0.09$.

Bei Prävalenz 0.02 sind die Pfade zu einem positiven Ergebnis $P(+\cap D)=0.72\times 0.02=0.0144$ und $P(+\cap D')=0.09\times 0.98=0.0882$. Somit ist $P(D\mid +)=0.0144/(0.0144+0.0882)=0.1404$.

**Ergebnis interpretieren und prüfen, Teil (b)**

Bei Prävalenz 0.11 lauten die entsprechenden Pfade 0.0792 und 0.0801. Daraus folgt $P(D\mid +)=0.0792/(0.0792+0.0801)=0.4972$. Diese posteriore Wahrscheinlichkeit beschreibt nach einem positiven Ergebnis die Chance, dass das untersuchte Merkmal tatsächlich vorliegt. Die Sensitivität setzt hingegen bereits voraus, dass das Merkmal vorliegt. Eine höhere Basisrate erhöht den Anteil der positiven Ergebnisse, die richtig positiv sind.

### T02-A04-V02: Erkennung seltener Transkriptionsfehler

**Vor dem Rechnen begründen, Teil (a)**

Die falsch-positive Wahrscheinlichkeit ist $1-0.93=0.07$.

Bei Prävalenz 0.01 sind die Pfade zu einem positiven Ergebnis $P(+\cap D)=0.84\times 0.01=0.0084$ und $P(+\cap D')=0.07\times 0.99=0.0693$. Somit ist $P(D\mid +)=0.0084/(0.0084+0.0693)=0.1081$.

**Ergebnis interpretieren und prüfen, Teil (b)**

Bei Prävalenz 0.08 lauten die entsprechenden Pfade 0.0672 und 0.0644. Daraus folgt $P(D\mid +)=0.0672/(0.0672+0.0644)=0.5106$. Diese posteriore Wahrscheinlichkeit beschreibt nach einem positiven Ergebnis die Chance, dass das untersuchte Merkmal tatsächlich vorliegt. Die Sensitivität setzt hingegen bereits voraus, dass das Merkmal vorliegt. Eine höhere Basisrate erhöht den Anteil der positiven Ergebnisse, die richtig positiv sind.

### T02-A04-V03: Screening auf Konservierungsrisiken

**Vor dem Rechnen begründen, Teil (a)**

Die falsch-positive Wahrscheinlichkeit ist $1-0.88=0.12$.

Bei Prävalenz 0.04 sind die Pfade zu einem positiven Ergebnis $P(+\cap D)=0.79\times 0.04=0.0316$ und $P(+\cap D')=0.12\times 0.96=0.1152$. Somit ist $P(D\mid +)=0.0316/(0.0316+0.1152)=0.2153$.

**Ergebnis interpretieren und prüfen, Teil (b)**

Bei Prävalenz 0.16 lauten die entsprechenden Pfade 0.1264 und 0.1008. Daraus folgt $P(D\mid +)=0.1264/(0.1264+0.1008)=0.5563$. Diese posteriore Wahrscheinlichkeit beschreibt nach einem positiven Ergebnis die Chance, dass das untersuchte Merkmal tatsächlich vorliegt. Die Sensitivität setzt hingegen bereits voraus, dass das Merkmal vorliegt. Eine höhere Basisrate erhöht den Anteil der positiven Ergebnisse, die richtig positiv sind.

### T02-A04-V04: Erkennung doppelter Datensätze

**Vor dem Rechnen begründen, Teil (a)**

Die falsch-positive Wahrscheinlichkeit ist $1-0.86=0.14$.

Bei Prävalenz 0.03 sind die Pfade zu einem positiven Ergebnis $P(+\cap D)=0.90\times 0.03=0.0270$ und $P(+\cap D')=0.14\times 0.97=0.1358$. Somit ist $P(D\mid +)=0.0270/(0.0270+0.1358)=0.1658$.

**Ergebnis interpretieren und prüfen, Teil (b)**

Bei Prävalenz 0.14 lauten die entsprechenden Pfade 0.1260 und 0.1204. Daraus folgt $P(D\mid +)=0.1260/(0.1260+0.1204)=0.5114$. Diese posteriore Wahrscheinlichkeit beschreibt nach einem positiven Ergebnis die Chance, dass das untersuchte Merkmal tatsächlich vorliegt. Die Sensitivität setzt hingegen bereits voraus, dass das Merkmal vorliegt. Eine höhere Basisrate erhöht den Anteil der positiven Ergebnisse, die richtig positiv sind.

### T02-A04-V05: Screening auf Sprachunterstützungsbedarf

**Vor dem Rechnen begründen, Teil (a)**

Die falsch-positive Wahrscheinlichkeit ist $1-0.94=0.06$.

Bei Prävalenz 0.05 sind die Pfade zu einem positiven Ergebnis $P(+\cap D)=0.76\times 0.05=0.0380$ und $P(+\cap D')=0.06\times 0.95=0.0570$. Somit ist $P(D\mid +)=0.0380/(0.0380+0.0570)=0.4000$.

**Ergebnis interpretieren und prüfen, Teil (b)**

Bei Prävalenz 0.19 lauten die entsprechenden Pfade 0.1444 und 0.0486. Daraus folgt $P(D\mid +)=0.1444/(0.1444+0.0486)=0.7482$. Diese posteriore Wahrscheinlichkeit beschreibt nach einem positiven Ergebnis die Chance, dass das untersuchte Merkmal tatsächlich vorliegt. Die Sensitivität setzt hingegen bereits voraus, dass das Merkmal vorliegt. Eine höhere Basisrate erhöht den Anteil der positiven Ergebnisse, die richtig positiv sind.

### T02-A04-V06: Erkennung beschädigter Bilder

**Vor dem Rechnen begründen, Teil (a)**

Die falsch-positive Wahrscheinlichkeit ist $1-0.90=0.10$.

Bei Prävalenz 0.02 sind die Pfade zu einem positiven Ergebnis $P(+\cap D)=0.88\times 0.02=0.0176$ und $P(+\cap D')=0.10\times 0.98=0.0980$. Somit ist $P(D\mid +)=0.0176/(0.0176+0.0980)=0.1522$.

**Ergebnis interpretieren und prüfen, Teil (b)**

Bei Prävalenz 0.12 lauten die entsprechenden Pfade 0.1056 und 0.0880. Daraus folgt $P(D\mid +)=0.1056/(0.1056+0.0880)=0.5455$. Diese posteriore Wahrscheinlichkeit beschreibt nach einem positiven Ergebnis die Chance, dass das untersuchte Merkmal tatsächlich vorliegt. Die Sensitivität setzt hingegen bereits voraus, dass das Merkmal vorliegt. Eine höhere Basisrate erhöht den Anteil der positiven Ergebnisse, die richtig positiv sind.

### T02-A04-V07: Screening zur Forschungsintegrität

**Vor dem Rechnen begründen, Teil (a)**

Die falsch-positive Wahrscheinlichkeit ist $1-0.96=0.04$.

Bei Prävalenz 0.01 sind die Pfade zu einem positiven Ergebnis $P(+\cap D)=0.81\times 0.01=0.0081$ und $P(+\cap D')=0.04\times 0.99=0.0396$. Somit ist $P(D\mid +)=0.0081/(0.0081+0.0396)=0.1698$.

**Ergebnis interpretieren und prüfen, Teil (b)**

Bei Prävalenz 0.07 lauten die entsprechenden Pfade 0.0567 und 0.0372. Daraus folgt $P(D\mid +)=0.0567/(0.0567+0.0372)=0.6038$. Diese posteriore Wahrscheinlichkeit beschreibt nach einem positiven Ergebnis die Chance, dass das untersuchte Merkmal tatsächlich vorliegt. Die Sensitivität setzt hingegen bereits voraus, dass das Merkmal vorliegt. Eine höhere Basisrate erhöht den Anteil der positiven Ergebnisse, die richtig positiv sind.

### T02-A04-V08: Warnung vor Geräteausfall

**Vor dem Rechnen begründen, Teil (a)**

Die falsch-positive Wahrscheinlichkeit ist $1-0.89=0.11$.

Bei Prävalenz 0.06 sind die Pfade zu einem positiven Ergebnis $P(+\cap D)=0.85\times 0.06=0.0510$ und $P(+\cap D')=0.11\times 0.94=0.1034$. Somit ist $P(D\mid +)=0.0510/(0.0510+0.1034)=0.3303$.

**Ergebnis interpretieren und prüfen, Teil (b)**

Bei Prävalenz 0.21 lauten die entsprechenden Pfade 0.1785 und 0.0869. Daraus folgt $P(D\mid +)=0.1785/(0.1785+0.0869)=0.6726$. Diese posteriore Wahrscheinlichkeit beschreibt nach einem positiven Ergebnis die Chance, dass das untersuchte Merkmal tatsächlich vorliegt. Die Sensitivität setzt hingegen bereits voraus, dass das Merkmal vorliegt. Eine höhere Basisrate erhöht den Anteil der positiven Ergebnisse, die richtig positiv sind.

### T02-A04-V09: Erkennung von Katalogisierungsanomalien

**Vor dem Rechnen begründen, Teil (a)**

Die falsch-positive Wahrscheinlichkeit ist $1-0.92=0.08$.

Bei Prävalenz 0.03 sind die Pfade zu einem positiven Ergebnis $P(+\cap D)=0.74\times 0.03=0.0222$ und $P(+\cap D')=0.08\times 0.97=0.0776$. Somit ist $P(D\mid +)=0.0222/(0.0222+0.0776)=0.2224$.

**Ergebnis interpretieren und prüfen, Teil (b)**

Bei Prävalenz 0.15 lauten die entsprechenden Pfade 0.1110 und 0.0680. Daraus folgt $P(D\mid +)=0.1110/(0.1110+0.0680)=0.6201$. Diese posteriore Wahrscheinlichkeit beschreibt nach einem positiven Ergebnis die Chance, dass das untersuchte Merkmal tatsächlich vorliegt. Die Sensitivität setzt hingegen bereits voraus, dass das Merkmal vorliegt. Eine höhere Basisrate erhöht den Anteil der positiven Ergebnisse, die richtig positiv sind.

### T02-A04-V10: Klassifikation nach Unterstützungspriorität

**Vor dem Rechnen begründen, Teil (a)**

Die falsch-positive Wahrscheinlichkeit ist $1-0.95=0.05$.

Bei Prävalenz 0.04 sind die Pfade zu einem positiven Ergebnis $P(+\cap D)=0.87\times 0.04=0.0348$ und $P(+\cap D')=0.05\times 0.96=0.0480$. Somit ist $P(D\mid +)=0.0348/(0.0348+0.0480)=0.4203$.

**Ergebnis interpretieren und prüfen, Teil (b)**

Bei Prävalenz 0.18 lauten die entsprechenden Pfade 0.1566 und 0.0410. Daraus folgt $P(D\mid +)=0.1566/(0.1566+0.0410)=0.7925$. Diese posteriore Wahrscheinlichkeit beschreibt nach einem positiven Ergebnis die Chance, dass das untersuchte Merkmal tatsächlich vorliegt. Die Sensitivität setzt hingegen bereits voraus, dass das Merkmal vorliegt. Eine höhere Basisrate erhöht den Anteil der positiven Ergebnisse, die richtig positiv sind.

## A05: Diskreter Erwartungswert, Varianz, PMF und CDF

### T02-A05-V01: Anzahl der Anschlussfragen

**Berechnung einrichten, Teil (a)**

Alle Massen sind nichtnegativ, und ihre Summe ist 0.20+0.35+0.30+0.15=1.00. Die Tabelle ist daher eine gültige PMF.

**Berechnung durchführen, Teil (b)**

$E(X)=\sum xP(X=x)=0(0.20)+1(0.35)+3(0.30)+5(0.15)=2.0000$. Über viele vergleichbare Beobachtungen nähert sich der langfristige Mittelwert der Grösse «Anzahl der Anschlussfragen» dem Wert 2.0000. Weiter ist $E(X^2)=0^2(0.20)+1^2(0.35)+3^2(0.30)+5^2(0.15)=6.8000$. Somit gilt $\operatorname{Var}(X)=6.8000-2.0000^2=2.8000$; die Varianz besitzt quadrierte Zähleinheiten.

**Ergebnis interpretieren und prüfen, Teil (c)**

Die kumulierten Werte sind $F(0)=0.20$, $F(1)=0.55$, $F(3)=0.85$, $F(5)=1.00$. Eine PMF-Grafik setzt bei jedem möglichen Wert einen eigenen Balken oder eine Punktmasse. Eine CDF ist dagegen eine nicht fallende, rechtsstetige Treppenfunktion, welche die Massen ansammelt und bei 1 endet.

### T02-A05-V02: Tägliche Archivanfragen

**Berechnung einrichten, Teil (a)**

Alle Massen sind nichtnegativ, und ihre Summe ist 0.25+0.40+0.20+0.15=1.00. Die Tabelle ist daher eine gültige PMF.

**Berechnung durchführen, Teil (b)**

$E(X)=\sum xP(X=x)=1(0.25)+2(0.40)+4(0.20)+6(0.15)=2.7500$. Über viele vergleichbare Beobachtungen nähert sich der langfristige Mittelwert der Grösse «Tägliche Archivanfragen» dem Wert 2.7500. Weiter ist $E(X^2)=1^2(0.25)+2^2(0.40)+4^2(0.20)+6^2(0.15)=10.4500$. Somit gilt $\operatorname{Var}(X)=10.4500-2.7500^2=2.8875$; die Varianz besitzt quadrierte Zähleinheiten.

**Ergebnis interpretieren und prüfen, Teil (c)**

Die kumulierten Werte sind $F(1)=0.25$, $F(2)=0.65$, $F(4)=0.85$, $F(6)=1.00$. Eine PMF-Grafik setzt bei jedem möglichen Wert einen eigenen Balken oder eine Punktmasse. Eine CDF ist dagegen eine nicht fallende, rechtsstetige Treppenfunktion, welche die Massen ansammelt und bei 1 endet.

### T02-A05-V03: Abgeschlossene Übungsserien

**Berechnung einrichten, Teil (a)**

Alle Massen sind nichtnegativ, und ihre Summe ist 0.10+0.30+0.45+0.15=1.00. Die Tabelle ist daher eine gültige PMF.

**Berechnung durchführen, Teil (b)**

$E(X)=\sum xP(X=x)=0(0.10)+2(0.30)+3(0.45)+7(0.15)=3.0000$. Über viele vergleichbare Beobachtungen nähert sich der langfristige Mittelwert der Grösse «Abgeschlossene Übungsserien» dem Wert 3.0000. Weiter ist $E(X^2)=0^2(0.10)+2^2(0.30)+3^2(0.45)+7^2(0.15)=12.6000$. Somit gilt $\operatorname{Var}(X)=12.6000-3.0000^2=3.6000$; die Varianz besitzt quadrierte Zähleinheiten.

**Ergebnis interpretieren und prüfen, Teil (c)**

Die kumulierten Werte sind $F(0)=0.10$, $F(2)=0.40$, $F(3)=0.85$, $F(7)=1.00$. Eine PMF-Grafik setzt bei jedem möglichen Wert einen eigenen Balken oder eine Punktmasse. Eine CDF ist dagegen eine nicht fallende, rechtsstetige Treppenfunktion, welche die Massen ansammelt und bei 1 endet.

### T02-A05-V04: Gemeldete Routenänderungen

**Berechnung einrichten, Teil (a)**

Alle Massen sind nichtnegativ, und ihre Summe ist 0.45+0.25+0.20+0.10=1.00. Die Tabelle ist daher eine gültige PMF.

**Berechnung durchführen, Teil (b)**

$E(X)=\sum xP(X=x)=0(0.45)+1(0.25)+2(0.20)+4(0.10)=1.0500$. Über viele vergleichbare Beobachtungen nähert sich der langfristige Mittelwert der Grösse «Gemeldete Routenänderungen» dem Wert 1.0500. Weiter ist $E(X^2)=0^2(0.45)+1^2(0.25)+2^2(0.20)+4^2(0.10)=2.6500$. Somit gilt $\operatorname{Var}(X)=2.6500-1.0500^2=1.5475$; die Varianz besitzt quadrierte Zähleinheiten.

**Ergebnis interpretieren und prüfen, Teil (c)**

Die kumulierten Werte sind $F(0)=0.45$, $F(1)=0.70$, $F(2)=0.90$, $F(4)=1.00$. Eine PMF-Grafik setzt bei jedem möglichen Wert einen eigenen Balken oder eine Punktmasse. Eine CDF ist dagegen eine nicht fallende, rechtsstetige Treppenfunktion, welche die Massen ansammelt und bei 1 endet.

### T02-A05-V05: Wöchentliche Gemeinschaftstreffen

**Berechnung einrichten, Teil (a)**

Alle Massen sind nichtnegativ, und ihre Summe ist 0.30+0.25+0.35+0.10=1.00. Die Tabelle ist daher eine gültige PMF.

**Berechnung durchführen, Teil (b)**

$E(X)=\sum xP(X=x)=1(0.30)+3(0.25)+4(0.35)+8(0.10)=3.2500$. Über viele vergleichbare Beobachtungen nähert sich der langfristige Mittelwert der Grösse «Wöchentliche Gemeinschaftstreffen» dem Wert 3.2500. Weiter ist $E(X^2)=1^2(0.30)+3^2(0.25)+4^2(0.35)+8^2(0.10)=14.5500$. Somit gilt $\operatorname{Var}(X)=14.5500-3.2500^2=3.9875$; die Varianz besitzt quadrierte Zähleinheiten.

**Ergebnis interpretieren und prüfen, Teil (c)**

Die kumulierten Werte sind $F(1)=0.30$, $F(3)=0.55$, $F(4)=0.90$, $F(8)=1.00$. Eine PMF-Grafik setzt bei jedem möglichen Wert einen eigenen Balken oder eine Punktmasse. Eine CDF ist dagegen eine nicht fallende, rechtsstetige Treppenfunktion, welche die Massen ansammelt und bei 1 endet.

### T02-A05-V06: Erfolgreiche Dateiwiederherstellungen

**Berechnung einrichten, Teil (a)**

Alle Massen sind nichtnegativ, und ihre Summe ist 0.15+0.25+0.40+0.20=1.00. Die Tabelle ist daher eine gültige PMF.

**Berechnung durchführen, Teil (b)**

$E(X)=\sum xP(X=x)=0(0.15)+2(0.25)+5(0.40)+6(0.20)=3.7000$. Über viele vergleichbare Beobachtungen nähert sich der langfristige Mittelwert der Grösse «Erfolgreiche Dateiwiederherstellungen» dem Wert 3.7000. Weiter ist $E(X^2)=0^2(0.15)+2^2(0.25)+5^2(0.40)+6^2(0.20)=18.2000$. Somit gilt $\operatorname{Var}(X)=18.2000-3.7000^2=4.5100$; die Varianz besitzt quadrierte Zähleinheiten.

**Ergebnis interpretieren und prüfen, Teil (c)**

Die kumulierten Werte sind $F(0)=0.15$, $F(2)=0.40$, $F(5)=0.80$, $F(6)=1.00$. Eine PMF-Grafik setzt bei jedem möglichen Wert einen eigenen Balken oder eine Punktmasse. Eine CDF ist dagegen eine nicht fallende, rechtsstetige Treppenfunktion, welche die Massen ansammelt und bei 1 endet.

### T02-A05-V07: Besuchte Museumsräume

**Berechnung einrichten, Teil (a)**

Alle Massen sind nichtnegativ, und ihre Summe ist 0.20+0.30+0.35+0.15=1.00. Die Tabelle ist daher eine gültige PMF.

**Berechnung durchführen, Teil (b)**

$E(X)=\sum xP(X=x)=2(0.20)+4(0.30)+5(0.35)+9(0.15)=4.7000$. Über viele vergleichbare Beobachtungen nähert sich der langfristige Mittelwert der Grösse «Besuchte Museumsräume» dem Wert 4.7000. Weiter ist $E(X^2)=2^2(0.20)+4^2(0.30)+5^2(0.35)+9^2(0.15)=26.5000$. Somit gilt $\operatorname{Var}(X)=26.5000-4.7000^2=4.4100$; die Varianz besitzt quadrierte Zähleinheiten.

**Ergebnis interpretieren und prüfen, Teil (c)**

Die kumulierten Werte sind $F(2)=0.20$, $F(4)=0.50$, $F(5)=0.85$, $F(9)=1.00$. Eine PMF-Grafik setzt bei jedem möglichen Wert einen eigenen Balken oder eine Punktmasse. Eine CDF ist dagegen eine nicht fallende, rechtsstetige Treppenfunktion, welche die Massen ansammelt und bei 1 endet.

### T02-A05-V08: Abgeschlossene optionale Lektüren

**Berechnung einrichten, Teil (a)**

Alle Massen sind nichtnegativ, und ihre Summe ist 0.25+0.30+0.25+0.20=1.00. Die Tabelle ist daher eine gültige PMF.

**Berechnung durchführen, Teil (b)**

$E(X)=\sum xP(X=x)=0(0.25)+1(0.30)+4(0.25)+6(0.20)=2.5000$. Über viele vergleichbare Beobachtungen nähert sich der langfristige Mittelwert der Grösse «Abgeschlossene optionale Lektüren» dem Wert 2.5000. Weiter ist $E(X^2)=0^2(0.25)+1^2(0.30)+4^2(0.25)+6^2(0.20)=11.5000$. Somit gilt $\operatorname{Var}(X)=11.5000-2.5000^2=5.2500$; die Varianz besitzt quadrierte Zähleinheiten.

**Ergebnis interpretieren und prüfen, Teil (c)**

Die kumulierten Werte sind $F(0)=0.25$, $F(1)=0.55$, $F(4)=0.80$, $F(6)=1.00$. Eine PMF-Grafik setzt bei jedem möglichen Wert einen eigenen Balken oder eine Punktmasse. Eine CDF ist dagegen eine nicht fallende, rechtsstetige Treppenfunktion, welche die Massen ansammelt und bei 1 endet.

### T02-A05-V09: Verifizierte Abschnitte mündlicher Überlieferungen

**Berechnung einrichten, Teil (a)**

Alle Massen sind nichtnegativ, und ihre Summe ist 0.15+0.35+0.30+0.20=1.00. Die Tabelle ist daher eine gültige PMF.

**Berechnung durchführen, Teil (b)**

$E(X)=\sum xP(X=x)=1(0.15)+2(0.35)+3(0.30)+5(0.20)=2.7500$. Über viele vergleichbare Beobachtungen nähert sich der langfristige Mittelwert der Grösse «Verifizierte Abschnitte mündlicher Überlieferungen» dem Wert 2.7500. Weiter ist $E(X^2)=1^2(0.15)+2^2(0.35)+3^2(0.30)+5^2(0.20)=9.2500$. Somit gilt $\operatorname{Var}(X)=9.2500-2.7500^2=1.6875$; die Varianz besitzt quadrierte Zähleinheiten.

**Ergebnis interpretieren und prüfen, Teil (c)**

Die kumulierten Werte sind $F(1)=0.15$, $F(2)=0.50$, $F(3)=0.80$, $F(5)=1.00$. Eine PMF-Grafik setzt bei jedem möglichen Wert einen eigenen Balken oder eine Punktmasse. Eine CDF ist dagegen eine nicht fallende, rechtsstetige Treppenfunktion, welche die Massen ansammelt und bei 1 endet.

### T02-A05-V10: Warnungen zur Datenqualität

**Berechnung einrichten, Teil (a)**

Alle Massen sind nichtnegativ, und ihre Summe ist 0.40+0.25+0.20+0.15=1.00. Die Tabelle ist daher eine gültige PMF.

**Berechnung durchführen, Teil (b)**

$E(X)=\sum xP(X=x)=0(0.40)+2(0.25)+4(0.20)+7(0.15)=2.3500$. Über viele vergleichbare Beobachtungen nähert sich der langfristige Mittelwert der Grösse «Warnungen zur Datenqualität» dem Wert 2.3500. Weiter ist $E(X^2)=0^2(0.40)+2^2(0.25)+4^2(0.20)+7^2(0.15)=11.5500$. Somit gilt $\operatorname{Var}(X)=11.5500-2.3500^2=6.0275$; die Varianz besitzt quadrierte Zähleinheiten.

**Ergebnis interpretieren und prüfen, Teil (c)**

Die kumulierten Werte sind $F(0)=0.40$, $F(2)=0.65$, $F(4)=0.85$, $F(7)=1.00$. Eine PMF-Grafik setzt bei jedem möglichen Wert einen eigenen Balken oder eine Punktmasse. Eine CDF ist dagegen eine nicht fallende, rechtsstetige Treppenfunktion, welche die Massen ansammelt und bei 1 endet.

## A06: Exakte Binomialwahrscheinlichkeiten

### T02-A06-V01: Abgeschlossene Einwilligungsprüfungen

**Berechnung einrichten, Teil (a)**

Das Modell lautet $X\sim B(8,0.62)$.

$P(X=5)=\binom{8}{5}0.62^{5}(1-0.62)^{3}=0.2815$. Dies ist die modellierte Wahrscheinlichkeit, dass genau 5 der 8 Einwilligungsprüfungen die Erfolgsdefinition erfüllen.

**Berechnung durchführen, Teil (b)**

$P(X=7)=\binom{8}{7}0.62^{7}(1-0.62)^{1}=0.1071$. Dies ist die entsprechende Wahrscheinlichkeit für genau 7.

**Berechnung durchführen, Teil (c)**

$E(X)=n\pi=8(0.62)=4.9600$ und $\operatorname{Var}(X)=n\pi(1-\pi)=8(0.62)(0.38)=1.8848$. Über wiederholte Gruppen der Grösse 8 nähert sich die mittlere Anzahl dem Wert 4.9600.

**Ergebnis interpretieren und prüfen, Teil (d)**

Die Zahl der Einwilligungsprüfungen muss fest bei 8 bleiben. Jede Einheit wird nur als Erfolg oder Misserfolg danach eingeteilt, ob sie abgeschlossen ist. Die Erfolgswahrscheinlichkeit muss 0.62 bleiben, und die Ergebnisse der Versuche müssen unabhängig sein. Wenn eine Bedingung nicht gilt, ist diese Binomialrechnung nicht begründet.

### T02-A06-V02: Korrekt klassifizierte Bilder

**Berechnung einrichten, Teil (a)**

Das Modell lautet $X\sim B(9,0.74)$.

$P(X=6)=\binom{9}{6}0.74^{6}(1-0.74)^{3}=0.2424$. Dies ist die modellierte Wahrscheinlichkeit, dass genau 6 der 9 Bilder die Erfolgsdefinition erfüllen.

**Berechnung durchführen, Teil (b)**

$P(X=8)=\binom{9}{8}0.74^{8}(1-0.74)^{1}=0.2104$. Dies ist die entsprechende Wahrscheinlichkeit für genau 8.

**Berechnung durchführen, Teil (c)**

$E(X)=n\pi=9(0.74)=6.6600$ und $\operatorname{Var}(X)=n\pi(1-\pi)=9(0.74)(0.26)=1.7316$. Über wiederholte Gruppen der Grösse 9 nähert sich die mittlere Anzahl dem Wert 6.6600.

**Ergebnis interpretieren und prüfen, Teil (d)**

Die Zahl der Bilder muss fest bei 9 bleiben. Jede Einheit wird nur als Erfolg oder Misserfolg danach eingeteilt, ob sie korrekt klassifiziert ist. Die Erfolgswahrscheinlichkeit muss 0.74 bleiben, und die Ergebnisse der Versuche müssen unabhängig sein. Wenn eine Bedingung nicht gilt, ist diese Binomialrechnung nicht begründet.

### T02-A06-V03: Zurückgesandte Tagebuchaufforderungen

**Berechnung einrichten, Teil (a)**

Das Modell lautet $X\sim B(7,0.58)$.

$P(X=3)=\binom{7}{3}0.58^{3}(1-0.58)^{4}=0.2125$. Dies ist die modellierte Wahrscheinlichkeit, dass genau 3 der 7 Tagebuchaufforderungen die Erfolgsdefinition erfüllen.

**Berechnung durchführen, Teil (b)**

$P(X=5)=\binom{7}{5}0.58^{5}(1-0.58)^{2}=0.2431$. Dies ist die entsprechende Wahrscheinlichkeit für genau 5.

**Berechnung durchführen, Teil (c)**

$E(X)=n\pi=7(0.58)=4.0600$ und $\operatorname{Var}(X)=n\pi(1-\pi)=7(0.58)(0.42)=1.7052$. Über wiederholte Gruppen der Grösse 7 nähert sich die mittlere Anzahl dem Wert 4.0600.

**Ergebnis interpretieren und prüfen, Teil (d)**

Die Zahl der Tagebuchaufforderungen muss fest bei 7 bleiben. Jede Einheit wird nur als Erfolg oder Misserfolg danach eingeteilt, ob sie zurückgesandt wird. Die Erfolgswahrscheinlichkeit muss 0.58 bleiben, und die Ergebnisse der Versuche müssen unabhängig sein. Wenn eine Bedingung nicht gilt, ist diese Binomialrechnung nicht begründet.

### T02-A06-V04: Erfolgreiche Archivsuche

**Berechnung einrichten, Teil (a)**

Das Modell lautet $X\sim B(10,0.43)$.

$P(X=4)=\binom{10}{4}0.43^{4}(1-0.43)^{6}=0.2462$. Dies ist die modellierte Wahrscheinlichkeit, dass genau 4 der 10 Archivsuchvorgänge die Erfolgsdefinition erfüllen.

**Berechnung durchführen, Teil (b)**

$P(X=6)=\binom{10}{6}0.43^{6}(1-0.43)^{4}=0.1401$. Dies ist die entsprechende Wahrscheinlichkeit für genau 6.

**Berechnung durchführen, Teil (c)**

$E(X)=n\pi=10(0.43)=4.3000$ und $\operatorname{Var}(X)=n\pi(1-\pi)=10(0.43)(0.57)=2.4510$. Über wiederholte Gruppen der Grösse 10 nähert sich die mittlere Anzahl dem Wert 4.3000.

**Ergebnis interpretieren und prüfen, Teil (d)**

Die Zahl der Archivsuchvorgänge muss fest bei 10 bleiben. Jede Einheit wird nur als Erfolg oder Misserfolg danach eingeteilt, ob sie erfolgreich ist. Die Erfolgswahrscheinlichkeit muss 0.43 bleiben, und die Ergebnisse der Versuche müssen unabhängig sein. Wenn eine Bedingung nicht gilt, ist diese Binomialrechnung nicht begründet.

### T02-A06-V05: Brauchbare Sensormesswerte

**Berechnung einrichten, Teil (a)**

Das Modell lautet $X\sim B(6,0.81)$.

$P(X=4)=\binom{6}{4}0.81^{4}(1-0.81)^{2}=0.2331$. Dies ist die modellierte Wahrscheinlichkeit, dass genau 4 der 6 Sensormesswerte die Erfolgsdefinition erfüllen.

**Berechnung durchführen, Teil (b)**

$P(X=6)=\binom{6}{6}0.81^{6}(1-0.81)^{0}=0.2824$. Dies ist die entsprechende Wahrscheinlichkeit für genau 6.

**Berechnung durchführen, Teil (c)**

$E(X)=n\pi=6(0.81)=4.8600$ und $\operatorname{Var}(X)=n\pi(1-\pi)=6(0.81)(0.19)=0.9234$. Über wiederholte Gruppen der Grösse 6 nähert sich die mittlere Anzahl dem Wert 4.8600.

**Ergebnis interpretieren und prüfen, Teil (d)**

Die Zahl der Sensormesswerte muss fest bei 6 bleiben. Jede Einheit wird nur als Erfolg oder Misserfolg danach eingeteilt, ob sie brauchbar ist. Die Erfolgswahrscheinlichkeit muss 0.81 bleiben, und die Ergebnisse der Versuche müssen unabhängig sein. Wenn eine Bedingung nicht gilt, ist diese Binomialrechnung nicht begründet.

### T02-A06-V06: Fristgerechte Tutorialabgaben

**Berechnung einrichten, Teil (a)**

Das Modell lautet $X\sim B(12,0.67)$.

$P(X=8)=\binom{12}{8}0.67^{8}(1-0.67)^{4}=0.2384$. Dies ist die modellierte Wahrscheinlichkeit, dass genau 8 der 12 Tutorialabgaben die Erfolgsdefinition erfüllen.

**Berechnung durchführen, Teil (b)**

$P(X=10)=\binom{12}{10}0.67^{10}(1-0.67)^{2}=0.1310$. Dies ist die entsprechende Wahrscheinlichkeit für genau 10.

**Berechnung durchführen, Teil (c)**

$E(X)=n\pi=12(0.67)=8.0400$ und $\operatorname{Var}(X)=n\pi(1-\pi)=12(0.67)(0.33)=2.6532$. Über wiederholte Gruppen der Grösse 12 nähert sich die mittlere Anzahl dem Wert 8.0400.

**Ergebnis interpretieren und prüfen, Teil (d)**

Die Zahl der Tutorialabgaben muss fest bei 12 bleiben. Jede Einheit wird nur als Erfolg oder Misserfolg danach eingeteilt, ob sie fristgerecht eingeht. Die Erfolgswahrscheinlichkeit muss 0.67 bleiben, und die Ergebnisse der Versuche müssen unabhängig sein. Wenn eine Bedingung nicht gilt, ist diese Binomialrechnung nicht begründet.

### T02-A06-V07: Verifizierte Katalogeinträge

**Berechnung einrichten, Teil (a)**

Das Modell lautet $X\sim B(9,0.52)$.

$P(X=4)=\binom{9}{4}0.52^{4}(1-0.52)^{5}=0.2347$. Dies ist die modellierte Wahrscheinlichkeit, dass genau 4 der 9 Katalogeinträge die Erfolgsdefinition erfüllen.

**Berechnung durchführen, Teil (b)**

$P(X=7)=\binom{9}{7}0.52^{7}(1-0.52)^{2}=0.0853$. Dies ist die entsprechende Wahrscheinlichkeit für genau 7.

**Berechnung durchführen, Teil (c)**

$E(X)=n\pi=9(0.52)=4.6800$ und $\operatorname{Var}(X)=n\pi(1-\pi)=9(0.52)(0.48)=2.2464$. Über wiederholte Gruppen der Grösse 9 nähert sich die mittlere Anzahl dem Wert 4.6800.

**Ergebnis interpretieren und prüfen, Teil (d)**

Die Zahl der Katalogeinträge muss fest bei 9 bleiben. Jede Einheit wird nur als Erfolg oder Misserfolg danach eingeteilt, ob sie verifiziert ist. Die Erfolgswahrscheinlichkeit muss 0.52 bleiben, und die Ergebnisse der Versuche müssen unabhängig sein. Wenn eine Bedingung nicht gilt, ist diese Binomialrechnung nicht begründet.

### T02-A06-V08: Wahrgenommene Interviewtermine

**Berechnung einrichten, Teil (a)**

Das Modell lautet $X\sim B(11,0.76)$.

$P(X=8)=\binom{11}{8}0.76^{8}(1-0.76)^{3}=0.2539$. Dies ist die modellierte Wahrscheinlichkeit, dass genau 8 der 11 Interviewtermine die Erfolgsdefinition erfüllen.

**Berechnung durchführen, Teil (b)**

$P(X=9)=\binom{11}{9}0.76^{9}(1-0.76)^{2}=0.2680$. Dies ist die entsprechende Wahrscheinlichkeit für genau 9.

**Berechnung durchführen, Teil (c)**

$E(X)=n\pi=11(0.76)=8.3600$ und $\operatorname{Var}(X)=n\pi(1-\pi)=11(0.76)(0.24)=2.0064$. Über wiederholte Gruppen der Grösse 11 nähert sich die mittlere Anzahl dem Wert 8.3600.

**Ergebnis interpretieren und prüfen, Teil (d)**

Die Zahl der Interviewtermine muss fest bei 11 bleiben. Jede Einheit wird nur als Erfolg oder Misserfolg danach eingeteilt, ob sie wahrgenommen wird. Die Erfolgswahrscheinlichkeit muss 0.76 bleiben, und die Ergebnisse der Versuche müssen unabhängig sein. Wenn eine Bedingung nicht gilt, ist diese Binomialrechnung nicht begründet.

### T02-A06-V09: Richtige Routenwahlen

**Berechnung einrichten, Teil (a)**

Das Modell lautet $X\sim B(8,0.35)$.

$P(X=2)=\binom{8}{2}0.35^{2}(1-0.35)^{6}=0.2587$. Dies ist die modellierte Wahrscheinlichkeit, dass genau 2 der 8 Routenwahlen die Erfolgsdefinition erfüllen.

**Berechnung durchführen, Teil (b)**

$P(X=4)=\binom{8}{4}0.35^{4}(1-0.35)^{4}=0.1875$. Dies ist die entsprechende Wahrscheinlichkeit für genau 4.

**Berechnung durchführen, Teil (c)**

$E(X)=n\pi=8(0.35)=2.8000$ und $\operatorname{Var}(X)=n\pi(1-\pi)=8(0.35)(0.65)=1.8200$. Über wiederholte Gruppen der Grösse 8 nähert sich die mittlere Anzahl dem Wert 2.8000.

**Ergebnis interpretieren und prüfen, Teil (d)**

Die Zahl der Routenwahlen muss fest bei 8 bleiben. Jede Einheit wird nur als Erfolg oder Misserfolg danach eingeteilt, ob sie richtig ist. Die Erfolgswahrscheinlichkeit muss 0.35 bleiben, und die Ergebnisse der Versuche müssen unabhängig sein. Wenn eine Bedingung nicht gilt, ist diese Binomialrechnung nicht begründet.

### T02-A06-V10: Erfolgreiche Audiotranskriptionen

**Berechnung einrichten, Teil (a)**

Das Modell lautet $X\sim B(10,0.69)$.

$P(X=6)=\binom{10}{6}0.69^{6}(1-0.69)^{4}=0.2093$. Dies ist die modellierte Wahrscheinlichkeit, dass genau 6 der 10 Audiotranskriptionen die Erfolgsdefinition erfüllen.

**Berechnung durchführen, Teil (b)**

$P(X=8)=\binom{10}{8}0.69^{8}(1-0.69)^{2}=0.2222$. Dies ist die entsprechende Wahrscheinlichkeit für genau 8.

**Berechnung durchführen, Teil (c)**

$E(X)=n\pi=10(0.69)=6.9000$ und $\operatorname{Var}(X)=n\pi(1-\pi)=10(0.69)(0.31)=2.1390$. Über wiederholte Gruppen der Grösse 10 nähert sich die mittlere Anzahl dem Wert 6.9000.

**Ergebnis interpretieren und prüfen, Teil (d)**

Die Zahl der Audiotranskriptionen muss fest bei 10 bleiben. Jede Einheit wird nur als Erfolg oder Misserfolg danach eingeteilt, ob sie erfolgreich ist. Die Erfolgswahrscheinlichkeit muss 0.69 bleiben, und die Ergebnisse der Versuche müssen unabhängig sein. Wenn eine Bedingung nicht gilt, ist diese Binomialrechnung nicht begründet.

## A07: Binomiale Randwahrscheinlichkeiten mit dem Komplement

### T02-A07-V01: Mehr als 3 Datensätze mit manueller Prüfung

**Berechnung einrichten, Teil (a)**

Hier ist $X\sim B(40,0.04)$, und das Komplement von $X>3$ ist $X\leq 3$.

**Berechnung durchführen, Teil (b)**

Daher gilt $P(X>3)=1-[P(X=0)+P(X=1)+P(X=2)+P(X=3)]=1-[0.1954+0.3256+0.2646+0.1396]\approx 1-0.9252=0.0748$. Das Näherungszeichen ist nötig, weil die gezeigten Einzelterme gerundet sind. Der Wert 0.9252 wurde mit ungerundeten Termen berechnet.

**Ergebnis interpretieren und prüfen, Teil (c)**

Das Modell weist die Wahrscheinlichkeit 0.0748 dem Ereignis zu, bei dem mehr als 3 Erfolge in einer Gruppe von 40 betrachteten Einheiten auftreten. Ein Erfolg bedeutet hier, dass eine Einheit eine manuelle Prüfung benötigt. Das Komplement benötigt 4 Terme des unteren Randes. Eine direkte Summe würde dagegen die Werte 4 bis 40 benötigen.

### T02-A07-V02: Mehr als 5 Museumsbesuchende mit Audioguide

**Berechnung einrichten, Teil (a)**

Hier ist $X\sim B(25,0.12)$, und das Komplement von $X>5$ ist $X\leq 5$.

**Berechnung durchführen, Teil (b)**

Daher gilt $P(X>5)=1-[P(X=0)+P(X=1)+P(X=2)+P(X=3)+P(X=4)+P(X=5)]=1-[0.0409+0.1395+0.2283+0.2387+0.1790+0.1025]\approx 1-0.9291=0.0709$. Das Näherungszeichen ist nötig, weil die gezeigten Einzelterme gerundet sind. Der Wert 0.9291 wurde mit ungerundeten Termen berechnet.

**Ergebnis interpretieren und prüfen, Teil (c)**

Das Modell weist die Wahrscheinlichkeit 0.0709 dem Ereignis zu, bei dem mehr als 5 Erfolge in einer Gruppe von 25 betrachteten Einheiten auftreten. Ein Erfolg bedeutet hier, dass eine Einheit einen Audioguide verlangt. Das Komplement benötigt 6 Terme des unteren Randes. Eine direkte Summe würde dagegen die Werte 6 bis 25 benötigen.

### T02-A07-V03: Mehr als 4 ungültige Umfragelinks

**Berechnung einrichten, Teil (a)**

Hier ist $X\sim B(30,0.06)$, und das Komplement von $X>4$ ist $X\leq 4$.

**Berechnung durchführen, Teil (b)**

Daher gilt $P(X>4)=1-[P(X=0)+P(X=1)+P(X=2)+P(X=3)+P(X=4)]=1-[0.1563+0.2992+0.2769+0.1650+0.0711]\approx 1-0.9685=0.0315$. Das Näherungszeichen ist nötig, weil die gezeigten Einzelterme gerundet sind. Der Wert 0.9685 wurde mit ungerundeten Termen berechnet.

**Ergebnis interpretieren und prüfen, Teil (c)**

Das Modell weist die Wahrscheinlichkeit 0.0315 dem Ereignis zu, bei dem mehr als 4 Erfolge in einer Gruppe von 30 betrachteten Einheiten auftreten. Ein Erfolg bedeutet hier, dass eine Einheit als ungültig zurückkommt. Das Komplement benötigt 5 Terme des unteren Randes. Eine direkte Summe würde dagegen die Werte 5 bis 30 benötigen.

### T02-A07-V04: Mehr als 6 Objekte mit Konservierungsbedarf

**Berechnung einrichten, Teil (a)**

Hier ist $X\sim B(35,0.09)$, und das Komplement von $X>6$ ist $X\leq 6$.

**Berechnung durchführen, Teil (b)**

Daher gilt $P(X>6)=1-[P(X=0)+P(X=1)+P(X=2)+P(X=3)+P(X=4)+P(X=5)+P(X=6)]=1-[0.0369+0.1276+0.2145+0.2333+0.1846+0.1132+0.0560]\approx 1-0.9660=0.0340$. Das Näherungszeichen ist nötig, weil die gezeigten Einzelterme gerundet sind. Der Wert 0.9660 wurde mit ungerundeten Termen berechnet.

**Ergebnis interpretieren und prüfen, Teil (c)**

Das Modell weist die Wahrscheinlichkeit 0.0340 dem Ereignis zu, bei dem mehr als 6 Erfolge in einer Gruppe von 35 betrachteten Einheiten auftreten. Ein Erfolg bedeutet hier, dass eine Einheit Konservierungsarbeit benötigt. Das Komplement benötigt 7 Terme des unteren Randes. Eine direkte Summe würde dagegen die Werte 7 bis 35 benötigen.

### T02-A07-V05: Mehr als 4 Teilnehmende mit verpasster Erinnerung

**Berechnung einrichten, Teil (a)**

Hier ist $X\sim B(28,0.08)$, und das Komplement von $X>4$ ist $X\leq 4$.

**Berechnung durchführen, Teil (b)**

Daher gilt $P(X>4)=1-[P(X=0)+P(X=1)+P(X=2)+P(X=3)+P(X=4)]=1-[0.0968+0.2358+0.2768+0.2086+0.1134]\approx 1-0.9314=0.0686$. Das Näherungszeichen ist nötig, weil die gezeigten Einzelterme gerundet sind. Der Wert 0.9314 wurde mit ungerundeten Termen berechnet.

**Ergebnis interpretieren und prüfen, Teil (c)**

Das Modell weist die Wahrscheinlichkeit 0.0686 dem Ereignis zu, bei dem mehr als 4 Erfolge in einer Gruppe von 28 betrachteten Einheiten auftreten. Ein Erfolg bedeutet hier, dass eine Einheit eine Erinnerung verpasst. Das Komplement benötigt 5 Terme des unteren Randes. Eine direkte Summe würde dagegen die Werte 5 bis 28 benötigen.

### T02-A07-V06: Mehr als 5 Uploads mit einem zweiten Versuch

**Berechnung einrichten, Teil (a)**

Hier ist $X\sim B(32,0.07)$, und das Komplement von $X>5$ ist $X\leq 5$.

**Berechnung durchführen, Teil (b)**

Daher gilt $P(X>5)=1-[P(X=0)+P(X=1)+P(X=2)+P(X=3)+P(X=4)+P(X=5)]=1-[0.0981+0.2362+0.2755+0.2074+0.1132+0.0477]\approx 1-0.9780=0.0220$. Das Näherungszeichen ist nötig, weil die gezeigten Einzelterme gerundet sind. Der Wert 0.9780 wurde mit ungerundeten Termen berechnet.

**Ergebnis interpretieren und prüfen, Teil (c)**

Das Modell weist die Wahrscheinlichkeit 0.0220 dem Ereignis zu, bei dem mehr als 5 Erfolge in einer Gruppe von 32 betrachteten Einheiten auftreten. Ein Erfolg bedeutet hier, dass eine Einheit einen zweiten Versuch benötigt. Das Komplement benötigt 6 Terme des unteren Randes. Eine direkte Summe würde dagegen die Werte 6 bis 32 benötigen.

### T02-A07-V07: Mehr als 5 ausgewählte Seiten mit Anmerkungen

**Berechnung einrichten, Teil (a)**

Hier ist $X\sim B(20,0.15)$, und das Komplement von $X>5$ ist $X\leq 5$.

**Berechnung durchführen, Teil (b)**

Daher gilt $P(X>5)=1-[P(X=0)+P(X=1)+P(X=2)+P(X=3)+P(X=4)+P(X=5)]=1-[0.0388+0.1368+0.2293+0.2428+0.1821+0.1028]\approx 1-0.9327=0.0673$. Das Näherungszeichen ist nötig, weil die gezeigten Einzelterme gerundet sind. Der Wert 0.9327 wurde mit ungerundeten Termen berechnet.

**Ergebnis interpretieren und prüfen, Teil (c)**

Das Modell weist die Wahrscheinlichkeit 0.0673 dem Ereignis zu, bei dem mehr als 5 Erfolge in einer Gruppe von 20 betrachteten Einheiten auftreten. Ein Erfolg bedeutet hier, dass eine Einheit Anmerkungen enthält. Das Komplement benötigt 6 Terme des unteren Randes. Eine direkte Summe würde dagegen die Werte 6 bis 20 benötigen.

### T02-A07-V08: Mehr als 4 Interviews mit neuem Termin

**Berechnung einrichten, Teil (a)**

Hier ist $X\sim B(24,0.11)$, und das Komplement von $X>4$ ist $X\leq 4$.

**Berechnung durchführen, Teil (b)**

Daher gilt $P(X>4)=1-[P(X=0)+P(X=1)+P(X=2)+P(X=3)+P(X=4)]=1-[0.0610+0.1810+0.2572+0.2331+0.1513]\approx 1-0.8835=0.1165$. Das Näherungszeichen ist nötig, weil die gezeigten Einzelterme gerundet sind. Der Wert 0.8835 wurde mit ungerundeten Termen berechnet.

**Ergebnis interpretieren und prüfen, Teil (c)**

Das Modell weist die Wahrscheinlichkeit 0.1165 dem Ereignis zu, bei dem mehr als 4 Erfolge in einer Gruppe von 24 betrachteten Einheiten auftreten. Ein Erfolg bedeutet hier, dass eine Einheit neu angesetzt werden muss. Das Komplement benötigt 5 Terme des unteren Randes. Eine direkte Summe würde dagegen die Werte 5 bis 24 benötigen.

### T02-A07-V09: Mehr als 3 Routenbeobachtungen mit Verspätung

**Berechnung einrichten, Teil (a)**

Hier ist $X\sim B(36,0.05)$, und das Komplement von $X>3$ ist $X\leq 3$.

**Berechnung durchführen, Teil (b)**

Daher gilt $P(X>3)=1-[P(X=0)+P(X=1)+P(X=2)+P(X=3)]=1-[0.1578+0.2990+0.2753+0.1642]\approx 1-0.8963=0.1037$. Das Näherungszeichen ist nötig, weil die gezeigten Einzelterme gerundet sind. Der Wert 0.8963 wurde mit ungerundeten Termen berechnet.

**Ergebnis interpretieren und prüfen, Teil (c)**

Das Modell weist die Wahrscheinlichkeit 0.1037 dem Ereignis zu, bei dem mehr als 3 Erfolge in einer Gruppe von 36 betrachteten Einheiten auftreten. Ein Erfolg bedeutet hier, dass eine Einheit eine Verspätung zeigt. Das Komplement benötigt 4 Terme des unteren Randes. Eine direkte Summe würde dagegen die Werte 4 bis 36 benötigen.

### T02-A07-V10: Mehr als 5 Formulare mit optionalem Kommentar

**Berechnung einrichten, Teil (a)**

Hier ist $X\sim B(18,0.18)$, und das Komplement von $X>5$ ist $X\leq 5$.

**Berechnung durchführen, Teil (b)**

Daher gilt $P(X>5)=1-[P(X=0)+P(X=1)+P(X=2)+P(X=3)+P(X=4)+P(X=5)]=1-[0.0281+0.1110+0.2071+0.2425+0.1996+0.1227]\approx 1-0.9111=0.0889$. Das Näherungszeichen ist nötig, weil die gezeigten Einzelterme gerundet sind. Der Wert 0.9111 wurde mit ungerundeten Termen berechnet.

**Ergebnis interpretieren und prüfen, Teil (c)**

Das Modell weist die Wahrscheinlichkeit 0.0889 dem Ereignis zu, bei dem mehr als 5 Erfolge in einer Gruppe von 18 betrachteten Einheiten auftreten. Ein Erfolg bedeutet hier, dass eine Einheit einen optionalen Kommentar enthält. Das Komplement benötigt 6 Terme des unteren Randes. Eine direkte Summe würde dagegen die Werte 6 bis 18 benötigen.

## A09: Wahrscheinlichkeiten der Standardnormalverteilung

### T02-A09-V01: Bereiche der Standardnormalverteilung, Satz 1

**Berechnung einrichten, Teil (a)**

Schreibe $\Phi(z)=P(Z\leq z)$.

$P(Z\leq -0.45)=\Phi(-0.45)=0.3264$. Schattiere links von -0.45.

**Berechnung durchführen, Teil (b)**

$P(Z>1.36)=1-\Phi(1.36)=0.0869$. Schattiere den rechten Rand.

**Ergebnis interpretieren und prüfen, Teil (c)**

$P(-0.80<Z\leq 0.95)=\Phi(0.95)-\Phi(-0.80)=0.6171$. Schattiere zwischen den beiden Grenzen. Bei einer stetigen Verteilung verändert die Einbeziehung einer Grenze die Wahrscheinlichkeit nicht.

### T02-A09-V02: Bereiche der Standardnormalverteilung, Satz 2

**Berechnung einrichten, Teil (a)**

Schreibe $\Phi(z)=P(Z\leq z)$.

$P(Z\leq -1.12)=\Phi(-1.12)=0.1314$. Schattiere links von -1.12.

**Berechnung durchführen, Teil (b)**

$P(Z>0.84)=1-\Phi(0.84)=0.2005$. Schattiere den rechten Rand.

**Ergebnis interpretieren und prüfen, Teil (c)**

$P(-0.35<Z\leq 1.42)=\Phi(1.42)-\Phi(-0.35)=0.5590$. Schattiere zwischen den beiden Grenzen. Bei einer stetigen Verteilung verändert die Einbeziehung einer Grenze die Wahrscheinlichkeit nicht.

### T02-A09-V03: Bereiche der Standardnormalverteilung, Satz 3

**Berechnung einrichten, Teil (a)**

Schreibe $\Phi(z)=P(Z\leq z)$.

$P(Z\leq 0.28)=\Phi(0.28)=0.6103$. Schattiere links von 0.28.

**Berechnung durchführen, Teil (b)**

$P(Z>1.74)=1-\Phi(1.74)=0.0409$. Schattiere den rechten Rand.

**Ergebnis interpretieren und prüfen, Teil (c)**

$P(-1.05<Z\leq 0.62)=\Phi(0.62)-\Phi(-1.05)=0.5855$. Schattiere zwischen den beiden Grenzen. Bei einer stetigen Verteilung verändert die Einbeziehung einer Grenze die Wahrscheinlichkeit nicht.

### T02-A09-V04: Bereiche der Standardnormalverteilung, Satz 4

**Berechnung einrichten, Teil (a)**

Schreibe $\Phi(z)=P(Z\leq z)$.

$P(Z\leq -0.93)=\Phi(-0.93)=0.1762$. Schattiere links von -0.93.

**Berechnung durchführen, Teil (b)**

$P(Z>1.18)=1-\Phi(1.18)=0.1190$. Schattiere den rechten Rand.

**Ergebnis interpretieren und prüfen, Teil (c)**

$P(-0.44<Z\leq 1.27)=\Phi(1.27)-\Phi(-0.44)=0.5680$. Schattiere zwischen den beiden Grenzen. Bei einer stetigen Verteilung verändert die Einbeziehung einer Grenze die Wahrscheinlichkeit nicht.

### T02-A09-V05: Bereiche der Standardnormalverteilung, Satz 5

**Berechnung einrichten, Teil (a)**

Schreibe $\Phi(z)=P(Z\leq z)$.

$P(Z\leq 0.67)=\Phi(0.67)=0.7486$. Schattiere links von 0.67.

**Berechnung durchführen, Teil (b)**

$P(Z>2.05)=1-\Phi(2.05)=0.0202$. Schattiere den rechten Rand.

**Ergebnis interpretieren und prüfen, Teil (c)**

$P(-1.33<Z\leq 0.71)=\Phi(0.71)-\Phi(-1.33)=0.6694$. Schattiere zwischen den beiden Grenzen. Bei einer stetigen Verteilung verändert die Einbeziehung einer Grenze die Wahrscheinlichkeit nicht.

### T02-A09-V06: Bereiche der Standardnormalverteilung, Satz 6

**Berechnung einrichten, Teil (a)**

Schreibe $\Phi(z)=P(Z\leq z)$.

$P(Z\leq -1.48)=\Phi(-1.48)=0.0694$. Schattiere links von -1.48.

**Berechnung durchführen, Teil (b)**

$P(Z>0.56)=1-\Phi(0.56)=0.2877$. Schattiere den rechten Rand.

**Ergebnis interpretieren und prüfen, Teil (c)**

$P(-0.92<Z\leq 1.08)=\Phi(1.08)-\Phi(-0.92)=0.6811$. Schattiere zwischen den beiden Grenzen. Bei einer stetigen Verteilung verändert die Einbeziehung einer Grenze die Wahrscheinlichkeit nicht.

### T02-A09-V07: Bereiche der Standardnormalverteilung, Satz 7

**Berechnung einrichten, Teil (a)**

Schreibe $\Phi(z)=P(Z\leq z)$.

$P(Z\leq 0.14)=\Phi(0.14)=0.5557$. Schattiere links von 0.14.

**Berechnung durchführen, Teil (b)**

$P(Z>1.51)=1-\Phi(1.51)=0.0655$. Schattiere den rechten Rand.

**Ergebnis interpretieren und prüfen, Teil (c)**

$P(-0.68<Z\leq 1.19)=\Phi(1.19)-\Phi(-0.68)=0.6347$. Schattiere zwischen den beiden Grenzen. Bei einer stetigen Verteilung verändert die Einbeziehung einer Grenze die Wahrscheinlichkeit nicht.

### T02-A09-V08: Bereiche der Standardnormalverteilung, Satz 8

**Berechnung einrichten, Teil (a)**

Schreibe $\Phi(z)=P(Z\leq z)$.

$P(Z\leq -0.76)=\Phi(-0.76)=0.2236$. Schattiere links von -0.76.

**Berechnung durchführen, Teil (b)**

$P(Z>1.89)=1-\Phi(1.89)=0.0294$. Schattiere den rechten Rand.

**Ergebnis interpretieren und prüfen, Teil (c)**

$P(-1.21<Z\leq 0.37)=\Phi(0.37)-\Phi(-1.21)=0.5312$. Schattiere zwischen den beiden Grenzen. Bei einer stetigen Verteilung verändert die Einbeziehung einer Grenze die Wahrscheinlichkeit nicht.

### T02-A09-V09: Bereiche der Standardnormalverteilung, Satz 9

**Berechnung einrichten, Teil (a)**

Schreibe $\Phi(z)=P(Z\leq z)$.

$P(Z\leq 0.91)=\Phi(0.91)=0.8186$. Schattiere links von 0.91.

**Berechnung durchführen, Teil (b)**

$P(Z>1.24)=1-\Phi(1.24)=0.1075$. Schattiere den rechten Rand.

**Ergebnis interpretieren und prüfen, Teil (c)**

$P(-0.57<Z\leq 1.63)=\Phi(1.63)-\Phi(-0.57)=0.6641$. Schattiere zwischen den beiden Grenzen. Bei einer stetigen Verteilung verändert die Einbeziehung einer Grenze die Wahrscheinlichkeit nicht.

### T02-A09-V10: Bereiche der Standardnormalverteilung, Satz 10

**Berechnung einrichten, Teil (a)**

Schreibe $\Phi(z)=P(Z\leq z)$.

$P(Z\leq -0.22)=\Phi(-0.22)=0.4129$. Schattiere links von -0.22.

**Berechnung durchführen, Teil (b)**

$P(Z>2.17)=1-\Phi(2.17)=0.0150$. Schattiere den rechten Rand.

**Ergebnis interpretieren und prüfen, Teil (c)**

$P(-1.46<Z\leq 0.88)=\Phi(0.88)-\Phi(-1.46)=0.7384$. Schattiere zwischen den beiden Grenzen. Bei einer stetigen Verteilung verändert die Einbeziehung einer Grenze die Wahrscheinlichkeit nicht.

## A10: Wahrscheinlichkeiten einer allgemeinen Normalverteilung

### T02-A10-V01: Normalmodell: Leseflüssigkeitswert

**Berechnung einrichten, Teil (a)**

Die Standardabweichung ist $\sigma=\sqrt{100}=10.00$.

$z=(79-72)/10.00\approx 0.7000$. Mit dem ungerundeten Quotienten ergibt sich $P(X\leq 79)=\Phi((79-72)/10.00)=0.7580$. Nach diesem Modell beträgt der entsprechende Anteil 0.7580. Er umfasst Werte bis einschliesslich 79 Wertpunkte. Schattiere die linke Seite dieser Grenze.

**Ergebnis interpretieren und prüfen, Teil (b)**

$z=(68-72)/10.00\approx -0.4000$ und $P(X>68)=1-\Phi((68-72)/10.00)=0.6554$. Dies ist der modellierte Anteil über 68 Wertpunkte, dargestellt durch den rechten Rand. Beide Interpretationen hängen vom angegebenen Normalmodell ab.

### T02-A10-V02: Normalmodell: Bearbeitungszeit im Archiv

**Berechnung einrichten, Teil (a)**

Die Standardabweichung ist $\sigma=\sqrt{64}=8.00$.

$z=(51-45)/8.00\approx 0.7500$. Mit dem ungerundeten Quotienten ergibt sich $P(X\leq 51)=\Phi((51-45)/8.00)=0.7734$. Nach diesem Modell beträgt der entsprechende Anteil 0.7734. Er umfasst Werte bis einschliesslich 51 Minuten. Schattiere die linke Seite dieser Grenze.

**Ergebnis interpretieren und prüfen, Teil (b)**

$z=(39-45)/8.00\approx -0.7500$ und $P(X>39)=1-\Phi((39-45)/8.00)=0.7734$. Dies ist der modellierte Anteil über 39 Minuten, dargestellt durch den rechten Rand. Beide Interpretationen hängen vom angegebenen Normalmodell ab.

### T02-A10-V03: Normalmodell: Wohlbefindenswert

**Berechnung einrichten, Teil (a)**

Die Standardabweichung ist $\sigma=\sqrt{81}=9.00$.

$z=(64-58)/9.00\approx 0.6667$. Mit dem ungerundeten Quotienten ergibt sich $P(X\leq 64)=\Phi((64-58)/9.00)=0.7475$. Nach diesem Modell beträgt der entsprechende Anteil 0.7475. Er umfasst Werte bis einschliesslich 64 Wertpunkte. Schattiere die linke Seite dieser Grenze.

**Ergebnis interpretieren und prüfen, Teil (b)**

$z=(52-58)/9.00\approx -0.6667$ und $P(X>52)=1-\Phi((52-58)/9.00)=0.7475$. Dies ist der modellierte Anteil über 52 Wertpunkte, dargestellt durch den rechten Rand. Beide Interpretationen hängen vom angegebenen Normalmodell ab.

### T02-A10-V04: Normalmodell: Dauer des Museumsbesuchs

**Berechnung einrichten, Teil (a)**

Die Standardabweichung ist $\sigma=\sqrt{225}=15.00$.

$z=(105-90)/15.00\approx 1.0000$. Mit dem ungerundeten Quotienten ergibt sich $P(X\leq 105)=\Phi((105-90)/15.00)=0.8413$. Nach diesem Modell beträgt der entsprechende Anteil 0.8413. Er umfasst Werte bis einschliesslich 105 Minuten. Schattiere die linke Seite dieser Grenze.

**Ergebnis interpretieren und prüfen, Teil (b)**

$z=(78-90)/15.00\approx -0.8000$ und $P(X>78)=1-\Phi((78-90)/15.00)=0.7881$. Dies ist der modellierte Anteil über 78 Minuten, dargestellt durch den rechten Rand. Beide Interpretationen hängen vom angegebenen Normalmodell ab.

### T02-A10-V05: Normalmodell: Gedächtniswert

**Berechnung einrichten, Teil (a)**

Die Standardabweichung ist $\sigma=\sqrt{144}=12.00$.

$z=(124-110)/12.00\approx 1.1667$. Mit dem ungerundeten Quotienten ergibt sich $P(X\leq 124)=\Phi((124-110)/12.00)=0.8783$. Nach diesem Modell beträgt der entsprechende Anteil 0.8783. Er umfasst Werte bis einschliesslich 124 Wertpunkte. Schattiere die linke Seite dieser Grenze.

**Ergebnis interpretieren und prüfen, Teil (b)**

$z=(103-110)/12.00\approx -0.5833$ und $P(X>103)=1-\Phi((103-110)/12.00)=0.7202$. Dies ist der modellierte Anteil über 103 Wertpunkte, dargestellt durch den rechten Rand. Beide Interpretationen hängen vom angegebenen Normalmodell ab.

### T02-A10-V06: Normalmodell: Schallpegelindex

**Berechnung einrichten, Teil (a)**

Die Standardabweichung ist $\sigma=\sqrt{49}=7.00$.

$z=(42-38)/7.00\approx 0.5714$. Mit dem ungerundeten Quotienten ergibt sich $P(X\leq 42)=\Phi((42-38)/7.00)=0.7161$. Nach diesem Modell beträgt der entsprechende Anteil 0.7161. Er umfasst Werte bis einschliesslich 42 Indexpunkte. Schattiere die linke Seite dieser Grenze.

**Ergebnis interpretieren und prüfen, Teil (b)**

$z=(33-38)/7.00\approx -0.7143$ und $P(X>33)=1-\Phi((33-38)/7.00)=0.7625$. Dies ist der modellierte Anteil über 33 Indexpunkte, dargestellt durch den rechten Rand. Beide Interpretationen hängen vom angegebenen Normalmodell ab.

### T02-A10-V07: Normalmodell: Zuversichtswert im Kurs

**Berechnung einrichten, Teil (a)**

Die Standardabweichung ist $\sigma=\sqrt{121}=11.00$.

$z=(75-66)/11.00\approx 0.8182$. Mit dem ungerundeten Quotienten ergibt sich $P(X\leq 75)=\Phi((75-66)/11.00)=0.7934$. Nach diesem Modell beträgt der entsprechende Anteil 0.7934. Er umfasst Werte bis einschliesslich 75 Wertpunkte. Schattiere die linke Seite dieser Grenze.

**Ergebnis interpretieren und prüfen, Teil (b)**

$z=(59-66)/11.00\approx -0.6364$ und $P(X>59)=1-\Phi((59-66)/11.00)=0.7377$. Dies ist der modellierte Anteil über 59 Wertpunkte, dargestellt durch den rechten Rand. Beide Interpretationen hängen vom angegebenen Normalmodell ab.

### T02-A10-V08: Normalmodell: Reaktionszeit

**Berechnung einrichten, Teil (a)**

Die Standardabweichung ist $\sigma=\sqrt{3600}=60.00$.

$z=(575-520)/60.00\approx 0.9167$. Mit dem ungerundeten Quotienten ergibt sich $P(X\leq 575)=\Phi((575-520)/60.00)=0.8203$. Nach diesem Modell beträgt der entsprechende Anteil 0.8203. Er umfasst Werte bis einschliesslich 575 Millisekunden. Schattiere die linke Seite dieser Grenze.

**Ergebnis interpretieren und prüfen, Teil (b)**

$z=(485-520)/60.00\approx -0.5833$ und $P(X>485)=1-\Phi((485-520)/60.00)=0.7202$. Dies ist der modellierte Anteil über 485 Millisekunden, dargestellt durch den rechten Rand. Beide Interpretationen hängen vom angegebenen Normalmodell ab.

### T02-A10-V09: Normalmodell: Vertrauenswert in der Gemeinschaft

**Berechnung einrichten, Teil (a)**

Die Standardabweichung ist $\sigma=\sqrt{64}=8.00$.

$z=(54-48)/8.00\approx 0.7500$. Mit dem ungerundeten Quotienten ergibt sich $P(X\leq 54)=\Phi((54-48)/8.00)=0.7734$. Nach diesem Modell beträgt der entsprechende Anteil 0.7734. Er umfasst Werte bis einschliesslich 54 Wertpunkte. Schattiere die linke Seite dieser Grenze.

**Ergebnis interpretieren und prüfen, Teil (b)**

$z=(43-48)/8.00\approx -0.6250$ und $P(X>43)=1-\Phi((43-48)/8.00)=0.7340$. Dies ist der modellierte Anteil über 43 Wertpunkte, dargestellt durch den rechten Rand. Beide Interpretationen hängen vom angegebenen Normalmodell ab.

### T02-A10-V10: Normalmodell: Genauigkeitswert der Katalogisierung

**Berechnung einrichten, Teil (a)**

Die Standardabweichung ist $\sigma=\sqrt{36}=6.00$.

$z=(88-84)/6.00\approx 0.6667$. Mit dem ungerundeten Quotienten ergibt sich $P(X\leq 88)=\Phi((88-84)/6.00)=0.7475$. Nach diesem Modell beträgt der entsprechende Anteil 0.7475. Er umfasst Werte bis einschliesslich 88 Wertpunkte. Schattiere die linke Seite dieser Grenze.

**Ergebnis interpretieren und prüfen, Teil (b)**

$z=(79-84)/6.00\approx -0.8333$ und $P(X>79)=1-\Phi((79-84)/6.00)=0.7977$. Dies ist der modellierte Anteil über 79 Wertpunkte, dargestellt durch den rechten Rand. Beide Interpretationen hängen vom angegebenen Normalmodell ab.

## A11: Inverse Quantile der Standardnormalverteilung

### T02-A11-V01: Bestimmung der z-Quantile zu 70% und 92%

**Berechnung einrichten, Teil (a)**

Ein Quantil beginnt mit der kumulierten Wahrscheinlichkeit $q$ und löst $\Phi(z)=q$ nach einer Position auf.

Aus $\Phi(z)=0.70$ folgt $z_{70\%}=0.5244$. Weil 0.70 grösser als 0.50 ist, ist diese Grenze positiv.

**Ergebnis interpretieren und prüfen, Teil (b)**

Aus $\Phi(z)=0.92$ folgt $z_{92\%}=1.4051$; das erwartete Vorzeichen ist positiv. Die Eingaben sind Flächen, und die Ausgaben sind Positionen auf der z-Achse. Damit wird die Richtung einer gewöhnlichen CDF-Rechnung umgekehrt.

### T02-A11-V02: Bestimmung der z-Quantile zu 15% und 88%

**Berechnung einrichten, Teil (a)**

Ein Quantil beginnt mit der kumulierten Wahrscheinlichkeit $q$ und löst $\Phi(z)=q$ nach einer Position auf.

Aus $\Phi(z)=0.15$ folgt $z_{15\%}=-1.0364$. Weil 0.15 kleiner als 0.50 ist, ist diese Grenze negativ.

**Ergebnis interpretieren und prüfen, Teil (b)**

Aus $\Phi(z)=0.88$ folgt $z_{88\%}=1.1750$; das erwartete Vorzeichen ist positiv. Die Eingaben sind Flächen, und die Ausgaben sind Positionen auf der z-Achse. Damit wird die Richtung einer gewöhnlichen CDF-Rechnung umgekehrt.

### T02-A11-V03: Bestimmung der z-Quantile zu 80% und 96%

**Berechnung einrichten, Teil (a)**

Ein Quantil beginnt mit der kumulierten Wahrscheinlichkeit $q$ und löst $\Phi(z)=q$ nach einer Position auf.

Aus $\Phi(z)=0.80$ folgt $z_{80\%}=0.8416$. Weil 0.80 grösser als 0.50 ist, ist diese Grenze positiv.

**Ergebnis interpretieren und prüfen, Teil (b)**

Aus $\Phi(z)=0.96$ folgt $z_{96\%}=1.7507$; das erwartete Vorzeichen ist positiv. Die Eingaben sind Flächen, und die Ausgaben sind Positionen auf der z-Achse. Damit wird die Richtung einer gewöhnlichen CDF-Rechnung umgekehrt.

### T02-A11-V04: Bestimmung der z-Quantile zu 28% und 90%

**Berechnung einrichten, Teil (a)**

Ein Quantil beginnt mit der kumulierten Wahrscheinlichkeit $q$ und löst $\Phi(z)=q$ nach einer Position auf.

Aus $\Phi(z)=0.28$ folgt $z_{28\%}=-0.5828$. Weil 0.28 kleiner als 0.50 ist, ist diese Grenze negativ.

**Ergebnis interpretieren und prüfen, Teil (b)**

Aus $\Phi(z)=0.90$ folgt $z_{90\%}=1.2816$; das erwartete Vorzeichen ist positiv. Die Eingaben sind Flächen, und die Ausgaben sind Positionen auf der z-Achse. Damit wird die Richtung einer gewöhnlichen CDF-Rechnung umgekehrt.

### T02-A11-V05: Bestimmung der z-Quantile zu 50% und 94%

**Berechnung einrichten, Teil (a)**

Ein Quantil beginnt mit der kumulierten Wahrscheinlichkeit $q$ und löst $\Phi(z)=q$ nach einer Position auf.

Aus $\Phi(z)=0.50$ folgt $z_{50\%}=0.0000$. Weil 0.50 gleich 0.50 ist, ist diese Grenze null.

**Ergebnis interpretieren und prüfen, Teil (b)**

Aus $\Phi(z)=0.94$ folgt $z_{94\%}=1.5548$; das erwartete Vorzeichen ist positiv. Die Eingaben sind Flächen, und die Ausgaben sind Positionen auf der z-Achse. Damit wird die Richtung einer gewöhnlichen CDF-Rechnung umgekehrt.

### T02-A11-V06: Bestimmung der z-Quantile zu 75% und 97%

**Berechnung einrichten, Teil (a)**

Ein Quantil beginnt mit der kumulierten Wahrscheinlichkeit $q$ und löst $\Phi(z)=q$ nach einer Position auf.

Aus $\Phi(z)=0.75$ folgt $z_{75\%}=0.6745$. Weil 0.75 grösser als 0.50 ist, ist diese Grenze positiv.

**Ergebnis interpretieren und prüfen, Teil (b)**

Aus $\Phi(z)=0.97$ folgt $z_{97\%}=1.8808$; das erwartete Vorzeichen ist positiv. Die Eingaben sind Flächen, und die Ausgaben sind Positionen auf der z-Achse. Damit wird die Richtung einer gewöhnlichen CDF-Rechnung umgekehrt.

### T02-A11-V07: Bestimmung der z-Quantile zu 32% und 68%

**Berechnung einrichten, Teil (a)**

Ein Quantil beginnt mit der kumulierten Wahrscheinlichkeit $q$ und löst $\Phi(z)=q$ nach einer Position auf.

Aus $\Phi(z)=0.32$ folgt $z_{32\%}=-0.4677$. Weil 0.32 kleiner als 0.50 ist, ist diese Grenze negativ.

**Ergebnis interpretieren und prüfen, Teil (b)**

Aus $\Phi(z)=0.68$ folgt $z_{68\%}=0.4677$; das erwartete Vorzeichen ist positiv. Die Eingaben sind Flächen, und die Ausgaben sind Positionen auf der z-Achse. Damit wird die Richtung einer gewöhnlichen CDF-Rechnung umgekehrt.

### T02-A11-V08: Bestimmung der z-Quantile zu 82% und 95%

**Berechnung einrichten, Teil (a)**

Ein Quantil beginnt mit der kumulierten Wahrscheinlichkeit $q$ und löst $\Phi(z)=q$ nach einer Position auf.

Aus $\Phi(z)=0.82$ folgt $z_{82\%}=0.9154$. Weil 0.82 grösser als 0.50 ist, ist diese Grenze positiv.

**Ergebnis interpretieren und prüfen, Teil (b)**

Aus $\Phi(z)=0.95$ folgt $z_{95\%}=1.6449$; das erwartete Vorzeichen ist positiv. Die Eingaben sind Flächen, und die Ausgaben sind Positionen auf der z-Achse. Damit wird die Richtung einer gewöhnlichen CDF-Rechnung umgekehrt.

### T02-A11-V09: Bestimmung der z-Quantile zu 11% und 62%

**Berechnung einrichten, Teil (a)**

Ein Quantil beginnt mit der kumulierten Wahrscheinlichkeit $q$ und löst $\Phi(z)=q$ nach einer Position auf.

Aus $\Phi(z)=0.11$ folgt $z_{11\%}=-1.2265$. Weil 0.11 kleiner als 0.50 ist, ist diese Grenze negativ.

**Ergebnis interpretieren und prüfen, Teil (b)**

Aus $\Phi(z)=0.62$ folgt $z_{62\%}=0.3055$; das erwartete Vorzeichen ist positiv. Die Eingaben sind Flächen, und die Ausgaben sind Positionen auf der z-Achse. Damit wird die Richtung einer gewöhnlichen CDF-Rechnung umgekehrt.

### T02-A11-V10: Bestimmung der z-Quantile zu 78% und 93%

**Berechnung einrichten, Teil (a)**

Ein Quantil beginnt mit der kumulierten Wahrscheinlichkeit $q$ und löst $\Phi(z)=q$ nach einer Position auf.

Aus $\Phi(z)=0.78$ folgt $z_{78\%}=0.7722$. Weil 0.78 grösser als 0.50 ist, ist diese Grenze positiv.

**Ergebnis interpretieren und prüfen, Teil (b)**

Aus $\Phi(z)=0.93$ folgt $z_{93\%}=1.4758$; das erwartete Vorzeichen ist positiv. Die Eingaben sind Flächen, und die Ausgaben sind Positionen auf der z-Achse. Damit wird die Richtung einer gewöhnlichen CDF-Rechnung umgekehrt.

## A12: Stichprobenverteilung des Mittelwerts

### T02-A12-V01: Präzision eines Stichprobenmittelwerts: Lesewert

**Vor dem Rechnen begründen, Teil (a)**

Für einen erwartungstreuen Stichprobenmittelwert gilt $E(\bar X)=\mu=64$. Aus der Unabhängigkeit folgt $\operatorname{SD}(\bar X)=\sigma/\sqrt n$.

$\sigma=\sqrt{196}=14.00$. Daher ist $\operatorname{SE}=14.00/\sqrt{49}=2.0000$ Wertpunkte. Über wiederholte Stichproben beträgt der Mittelwert ihrer Mittelwerte 64 Wertpunkte; ihre Standardabweichung beträgt 2.0000 Wertpunkte.

**Berechnung durchführen, Teil (b)**

Bei Varianz 100 ist $\operatorname{SE}=\sqrt{100}/\sqrt{49}=1.4286$ Wertpunkte. Die kleinere Populationsvarianz verringert den SE gegenüber Teil

**Berechnung durchführen, Teil (a)**

.

**Ergebnis interpretieren und prüfen, Teil (c)**

Bei $n=121$ ist $\operatorname{SE}=\sqrt{196}/\sqrt{121}=1.2727$ Wertpunkte. Die grössere Stichprobe verringert den SE über die Quadratwurzel aus $n$. Ein kleinerer SE bedeutet, dass die Mittelwerte wiederholter Stichproben dichter um den Populationsmittelwert liegen.

### T02-A12-V02: Präzision eines Stichprobenmittelwerts: Bearbeitungszeit

**Vor dem Rechnen begründen, Teil (a)**

Für einen erwartungstreuen Stichprobenmittelwert gilt $E(\bar X)=\mu=52$. Aus der Unabhängigkeit folgt $\operatorname{SD}(\bar X)=\sigma/\sqrt n$.

$\sigma=\sqrt{225}=15.00$. Daher ist $\operatorname{SE}=15.00/\sqrt{36}=2.5000$ Minuten. Über wiederholte Stichproben beträgt der Mittelwert ihrer Mittelwerte 52 Minuten; ihre Standardabweichung beträgt 2.5000 Minuten.

**Berechnung durchführen, Teil (b)**

Bei Varianz 144 ist $\operatorname{SE}=\sqrt{144}/\sqrt{36}=2.0000$ Minuten. Die kleinere Populationsvarianz verringert den SE gegenüber Teil

**Berechnung durchführen, Teil (a)**

.

**Ergebnis interpretieren und prüfen, Teil (c)**

Bei $n=100$ ist $\operatorname{SE}=\sqrt{225}/\sqrt{100}=1.5000$ Minuten. Die grössere Stichprobe verringert den SE über die Quadratwurzel aus $n$. Ein kleinerer SE bedeutet, dass die Mittelwerte wiederholter Stichproben dichter um den Populationsmittelwert liegen.

### T02-A12-V03: Präzision eines Stichprobenmittelwerts: Wohlbefindensindex

**Vor dem Rechnen begründen, Teil (a)**

Für einen erwartungstreuen Stichprobenmittelwert gilt $E(\bar X)=\mu=71$. Aus der Unabhängigkeit folgt $\operatorname{SD}(\bar X)=\sigma/\sqrt n$.

$\sigma=\sqrt{144}=12.00$. Daher ist $\operatorname{SE}=12.00/\sqrt{64}=1.5000$ Indexpunkte. Über wiederholte Stichproben beträgt der Mittelwert ihrer Mittelwerte 71 Indexpunkte; ihre Standardabweichung beträgt 1.5000 Indexpunkte.

**Berechnung durchführen, Teil (b)**

Bei Varianz 256 ist $\operatorname{SE}=\sqrt{256}/\sqrt{64}=2.0000$ Indexpunkte. Die grössere Populationsvarianz erhöht den SE gegenüber Teil

**Berechnung durchführen, Teil (a)**

.

**Ergebnis interpretieren und prüfen, Teil (c)**

Bei $n=81$ ist $\operatorname{SE}=\sqrt{144}/\sqrt{81}=1.3333$ Indexpunkte. Die grössere Stichprobe verringert den SE über die Quadratwurzel aus $n$. Ein kleinerer SE bedeutet, dass die Mittelwerte wiederholter Stichproben dichter um den Populationsmittelwert liegen.

### T02-A12-V04: Präzision eines Stichprobenmittelwerts: Gedächtniswert

**Vor dem Rechnen begründen, Teil (a)**

Für einen erwartungstreuen Stichprobenmittelwert gilt $E(\bar X)=\mu=105$. Aus der Unabhängigkeit folgt $\operatorname{SD}(\bar X)=\sigma/\sqrt n$.

$\sigma=\sqrt{324}=18.00$. Daher ist $\operatorname{SE}=18.00/\sqrt{81}=2.0000$ Wertpunkte. Über wiederholte Stichproben beträgt der Mittelwert ihrer Mittelwerte 105 Wertpunkte; ihre Standardabweichung beträgt 2.0000 Wertpunkte.

**Berechnung durchführen, Teil (b)**

Bei Varianz 225 ist $\operatorname{SE}=\sqrt{225}/\sqrt{81}=1.6667$ Wertpunkte. Die kleinere Populationsvarianz verringert den SE gegenüber Teil

**Berechnung durchführen, Teil (a)**

.

**Ergebnis interpretieren und prüfen, Teil (c)**

Bei $n=144$ ist $\operatorname{SE}=\sqrt{324}/\sqrt{144}=1.5000$ Wertpunkte. Die grössere Stichprobe verringert den SE über die Quadratwurzel aus $n$. Ein kleinerer SE bedeutet, dass die Mittelwerte wiederholter Stichproben dichter um den Populationsmittelwert liegen.

### T02-A12-V05: Präzision eines Stichprobenmittelwerts: Vertrauensbewertung

**Vor dem Rechnen begründen, Teil (a)**

Für einen erwartungstreuen Stichprobenmittelwert gilt $E(\bar X)=\mu=48$. Aus der Unabhängigkeit folgt $\operatorname{SD}(\bar X)=\sigma/\sqrt n$.

$\sigma=\sqrt{100}=10.00$. Daher ist $\operatorname{SE}=10.00/\sqrt{25}=2.0000$ Bewertungspunkte. Über wiederholte Stichproben beträgt der Mittelwert ihrer Mittelwerte 48 Bewertungspunkte; ihre Standardabweichung beträgt 2.0000 Bewertungspunkte.

**Berechnung durchführen, Teil (b)**

Bei Varianz 169 ist $\operatorname{SE}=\sqrt{169}/\sqrt{25}=2.6000$ Bewertungspunkte. Die grössere Populationsvarianz erhöht den SE gegenüber Teil

**Berechnung durchführen, Teil (a)**

.

**Ergebnis interpretieren und prüfen, Teil (c)**

Bei $n=64$ ist $\operatorname{SE}=\sqrt{100}/\sqrt{64}=1.2500$ Bewertungspunkte. Die grössere Stichprobe verringert den SE über die Quadratwurzel aus $n$. Ein kleinerer SE bedeutet, dass die Mittelwerte wiederholter Stichproben dichter um den Populationsmittelwert liegen.

### T02-A12-V06: Präzision eines Stichprobenmittelwerts: Reaktionszeit

**Vor dem Rechnen begründen, Teil (a)**

Für einen erwartungstreuen Stichprobenmittelwert gilt $E(\bar X)=\mu=480$. Aus der Unabhängigkeit folgt $\operatorname{SD}(\bar X)=\sigma/\sqrt n$.

$\sigma=\sqrt{2500}=50.00$. Daher ist $\operatorname{SE}=50.00/\sqrt{100}=5.0000$ Millisekunden. Über wiederholte Stichproben beträgt der Mittelwert ihrer Mittelwerte 480 Millisekunden; ihre Standardabweichung beträgt 5.0000 Millisekunden.

**Berechnung durchführen, Teil (b)**

Bei Varianz 1600 ist $\operatorname{SE}=\sqrt{1600}/\sqrt{100}=4.0000$ Millisekunden. Die kleinere Populationsvarianz verringert den SE gegenüber Teil

**Berechnung durchführen, Teil (a)**

.

**Ergebnis interpretieren und prüfen, Teil (c)**

Bei $n=400$ ist $\operatorname{SE}=\sqrt{2500}/\sqrt{400}=2.5000$ Millisekunden. Die grössere Stichprobe verringert den SE über die Quadratwurzel aus $n$. Ein kleinerer SE bedeutet, dass die Mittelwerte wiederholter Stichproben dichter um den Populationsmittelwert liegen.

### T02-A12-V07: Präzision eines Stichprobenmittelwerts: Zuversichtswert

**Vor dem Rechnen begründen, Teil (a)**

Für einen erwartungstreuen Stichprobenmittelwert gilt $E(\bar X)=\mu=59$. Aus der Unabhängigkeit folgt $\operatorname{SD}(\bar X)=\sigma/\sqrt n$.

$\sigma=\sqrt{121}=11.00$. Daher ist $\operatorname{SE}=11.00/\sqrt{49}=1.5714$ Wertpunkte. Über wiederholte Stichproben beträgt der Mittelwert ihrer Mittelwerte 59 Wertpunkte; ihre Standardabweichung beträgt 1.5714 Wertpunkte.

**Berechnung durchführen, Teil (b)**

Bei Varianz 196 ist $\operatorname{SE}=\sqrt{196}/\sqrt{49}=2.0000$ Wertpunkte. Die grössere Populationsvarianz erhöht den SE gegenüber Teil

**Berechnung durchführen, Teil (a)**

.

**Ergebnis interpretieren und prüfen, Teil (c)**

Bei $n=100$ ist $\operatorname{SE}=\sqrt{121}/\sqrt{100}=1.1000$ Wertpunkte. Die grössere Stichprobe verringert den SE über die Quadratwurzel aus $n$. Ein kleinerer SE bedeutet, dass die Mittelwerte wiederholter Stichproben dichter um den Populationsmittelwert liegen.

### T02-A12-V08: Präzision eines Stichprobenmittelwerts: Besuchsdauer

**Vor dem Rechnen begründen, Teil (a)**

Für einen erwartungstreuen Stichprobenmittelwert gilt $E(\bar X)=\mu=82$. Aus der Unabhängigkeit folgt $\operatorname{SD}(\bar X)=\sigma/\sqrt n$.

$\sigma=\sqrt{400}=20.00$. Daher ist $\operatorname{SE}=20.00/\sqrt{64}=2.5000$ Minuten. Über wiederholte Stichproben beträgt der Mittelwert ihrer Mittelwerte 82 Minuten; ihre Standardabweichung beträgt 2.5000 Minuten.

**Berechnung durchführen, Teil (b)**

Bei Varianz 256 ist $\operatorname{SE}=\sqrt{256}/\sqrt{64}=2.0000$ Minuten. Die kleinere Populationsvarianz verringert den SE gegenüber Teil

**Berechnung durchführen, Teil (a)**

.

**Ergebnis interpretieren und prüfen, Teil (c)**

Bei $n=144$ ist $\operatorname{SE}=\sqrt{400}/\sqrt{144}=1.6667$ Minuten. Die grössere Stichprobe verringert den SE über die Quadratwurzel aus $n$. Ein kleinerer SE bedeutet, dass die Mittelwerte wiederholter Stichproben dichter um den Populationsmittelwert liegen.

### T02-A12-V09: Präzision eines Stichprobenmittelwerts: Genauigkeitswert

**Vor dem Rechnen begründen, Teil (a)**

Für einen erwartungstreuen Stichprobenmittelwert gilt $E(\bar X)=\mu=88$. Aus der Unabhängigkeit folgt $\operatorname{SD}(\bar X)=\sigma/\sqrt n$.

$\sigma=\sqrt{81}=9.00$. Daher ist $\operatorname{SE}=9.00/\sqrt{36}=1.5000$ Wertpunkte. Über wiederholte Stichproben beträgt der Mittelwert ihrer Mittelwerte 88 Wertpunkte; ihre Standardabweichung beträgt 1.5000 Wertpunkte.

**Berechnung durchführen, Teil (b)**

Bei Varianz 144 ist $\operatorname{SE}=\sqrt{144}/\sqrt{36}=2.0000$ Wertpunkte. Die grössere Populationsvarianz erhöht den SE gegenüber Teil

**Berechnung durchführen, Teil (a)**

.

**Ergebnis interpretieren und prüfen, Teil (c)**

Bei $n=49$ ist $\operatorname{SE}=\sqrt{81}/\sqrt{49}=1.2857$ Wertpunkte. Die grössere Stichprobe verringert den SE über die Quadratwurzel aus $n$. Ein kleinerer SE bedeutet, dass die Mittelwerte wiederholter Stichproben dichter um den Populationsmittelwert liegen.

### T02-A12-V10: Präzision eines Stichprobenmittelwerts: Schallindex

**Vor dem Rechnen begründen, Teil (a)**

Für einen erwartungstreuen Stichprobenmittelwert gilt $E(\bar X)=\mu=42$. Aus der Unabhängigkeit folgt $\operatorname{SD}(\bar X)=\sigma/\sqrt n$.

$\sigma=\sqrt{169}=13.00$. Daher ist $\operatorname{SE}=13.00/\sqrt{25}=2.6000$ Indexpunkte. Über wiederholte Stichproben beträgt der Mittelwert ihrer Mittelwerte 42 Indexpunkte; ihre Standardabweichung beträgt 2.6000 Indexpunkte.

**Berechnung durchführen, Teil (b)**

Bei Varianz 100 ist $\operatorname{SE}=\sqrt{100}/\sqrt{25}=2.0000$ Indexpunkte. Die kleinere Populationsvarianz verringert den SE gegenüber Teil

**Berechnung durchführen, Teil (a)**

.

**Ergebnis interpretieren und prüfen, Teil (c)**

Bei $n=64$ ist $\operatorname{SE}=\sqrt{169}/\sqrt{64}=1.6250$ Indexpunkte. Die grössere Stichprobe verringert den SE über die Quadratwurzel aus $n$. Ein kleinerer SE bedeutet, dass die Mittelwerte wiederholter Stichproben dichter um den Populationsmittelwert liegen.

## A13: Intervalle unter einem Normalmodell

### T02-A13-V01: Intervallwahrscheinlichkeiten: Fokuswert

**Berechnung einrichten, Teil (a)**

Die Standardabweichung ist $\sigma=\sqrt{81}=9.00$.

Die Grenzen lauten $z_a=(50-50)/9.00\approx 0.0000$ und $z_b=(59-50)/9.00\approx 1.0000$. Mit den ungerundeten z-Werten gilt $P(50<X\leq 59)=\Phi((59-50)/9.00)-\Phi((50-50)/9.00)=0.3413$. Der modellierte Anteil beträgt somit 0.3413 für den Wertebereich **50 bis 59 Wertpunkte**.

**Ergebnis interpretieren und prüfen, Teil (b)**

$z_c=(43-50)/9.00\approx -0.7778$ und $z_d=(61-50)/9.00\approx 1.2222$. Daher ist $P(43<X\leq 61)=\Phi((61-50)/9.00)-\Phi((43-50)/9.00)=0.6708$. Dies ist der modellierte Anteil für den Wertebereich **43 bis 61 Wertpunkte**. Bei einem stetigen Modell verändert die Einbeziehung einer Grenze die Wahrscheinlichkeit nicht.

### T02-A13-V02: Intervallwahrscheinlichkeiten: Lesewert

**Berechnung einrichten, Teil (a)**

Die Standardabweichung ist $\sigma=\sqrt{100}=10.00$.

Die Grenzen lauten $z_a=(65-70)/10.00\approx -0.5000$ und $z_b=(82-70)/10.00\approx 1.2000$. Mit den ungerundeten z-Werten gilt $P(65<X\leq 82)=\Phi((82-70)/10.00)-\Phi((65-70)/10.00)=0.5764$. Der modellierte Anteil beträgt somit 0.5764 für den Wertebereich **65 bis 82 Wertpunkte**.

**Ergebnis interpretieren und prüfen, Teil (b)**

$z_c=(58-70)/10.00\approx -1.2000$ und $z_d=(76-70)/10.00\approx 0.6000$. Daher ist $P(58<X\leq 76)=\Phi((76-70)/10.00)-\Phi((58-70)/10.00)=0.6107$. Dies ist der modellierte Anteil für den Wertebereich **58 bis 76 Wertpunkte**. Bei einem stetigen Modell verändert die Einbeziehung einer Grenze die Wahrscheinlichkeit nicht.

### T02-A13-V03: Intervallwahrscheinlichkeiten: Besuchsdauer

**Berechnung einrichten, Teil (a)**

Die Standardabweichung ist $\sigma=\sqrt{225}=15.00$.

Die Grenzen lauten $z_a=(80-80)/15.00\approx 0.0000$ und $z_b=(95-80)/15.00\approx 1.0000$. Mit den ungerundeten z-Werten gilt $P(80<X\leq 95)=\Phi((95-80)/15.00)-\Phi((80-80)/15.00)=0.3413$. Der modellierte Anteil beträgt somit 0.3413 für den Wertebereich **80 bis 95 Minuten**.

**Ergebnis interpretieren und prüfen, Teil (b)**

$z_c=(62-80)/15.00\approx -1.2000$ und $z_d=(101-80)/15.00\approx 1.4000$. Daher ist $P(62<X\leq 101)=\Phi((101-80)/15.00)-\Phi((62-80)/15.00)=0.8042$. Dies ist der modellierte Anteil für den Wertebereich **62 bis 101 Minuten**. Bei einem stetigen Modell verändert die Einbeziehung einer Grenze die Wahrscheinlichkeit nicht.

### T02-A13-V04: Intervallwahrscheinlichkeiten: Gedächtniswert

**Berechnung einrichten, Teil (a)**

Die Standardabweichung ist $\sigma=\sqrt{144}=12.00$.

Die Grenzen lauten $z_a=(96-105)/12.00\approx -0.7500$ und $z_b=(117-105)/12.00\approx 1.0000$. Mit den ungerundeten z-Werten gilt $P(96<X\leq 117)=\Phi((117-105)/12.00)-\Phi((96-105)/12.00)=0.6147$. Der modellierte Anteil beträgt somit 0.6147 für den Wertebereich **96 bis 117 Wertpunkte**.

**Ergebnis interpretieren und prüfen, Teil (b)**

$z_c=(88-105)/12.00\approx -1.4167$ und $z_d=(122-105)/12.00\approx 1.4167$. Daher ist $P(88<X\leq 122)=\Phi((122-105)/12.00)-\Phi((88-105)/12.00)=0.8434$. Dies ist der modellierte Anteil für den Wertebereich **88 bis 122 Wertpunkte**. Bei einem stetigen Modell verändert die Einbeziehung einer Grenze die Wahrscheinlichkeit nicht.

### T02-A13-V05: Intervallwahrscheinlichkeiten: Vertrauensindex

**Berechnung einrichten, Teil (a)**

Die Standardabweichung ist $\sigma=\sqrt{64}=8.00$.

Die Grenzen lauten $z_a=(40-44)/8.00\approx -0.5000$ und $z_b=(52-44)/8.00\approx 1.0000$. Mit den ungerundeten z-Werten gilt $P(40<X\leq 52)=\Phi((52-44)/8.00)-\Phi((40-44)/8.00)=0.5328$. Der modellierte Anteil beträgt somit 0.5328 für den Wertebereich **40 bis 52 Indexpunkte**.

**Ergebnis interpretieren und prüfen, Teil (b)**

$z_c=(33-44)/8.00\approx -1.3750$ und $z_d=(49-44)/8.00\approx 0.6250$. Daher ist $P(33<X\leq 49)=\Phi((49-44)/8.00)-\Phi((33-44)/8.00)=0.6494$. Dies ist der modellierte Anteil für den Wertebereich **33 bis 49 Indexpunkte**. Bei einem stetigen Modell verändert die Einbeziehung einer Grenze die Wahrscheinlichkeit nicht.

### T02-A13-V06: Intervallwahrscheinlichkeiten: Reaktionszeit

**Berechnung einrichten, Teil (a)**

Die Standardabweichung ist $\sigma=\sqrt{2500}=50.00$.

Die Grenzen lauten $z_a=(475-500)/50.00\approx -0.5000$ und $z_b=(560-500)/50.00\approx 1.2000$. Mit den ungerundeten z-Werten gilt $P(475<X\leq 560)=\Phi((560-500)/50.00)-\Phi((475-500)/50.00)=0.5764$. Der modellierte Anteil beträgt somit 0.5764 für den Wertebereich **475 bis 560 Millisekunden**.

**Ergebnis interpretieren und prüfen, Teil (b)**

$z_c=(410-500)/50.00\approx -1.8000$ und $z_d=(535-500)/50.00\approx 0.7000$. Daher ist $P(410<X\leq 535)=\Phi((535-500)/50.00)-\Phi((410-500)/50.00)=0.7221$. Dies ist der modellierte Anteil für den Wertebereich **410 bis 535 Millisekunden**. Bei einem stetigen Modell verändert die Einbeziehung einer Grenze die Wahrscheinlichkeit nicht.

### T02-A13-V07: Intervallwahrscheinlichkeiten: Wohlbefindenswert

**Berechnung einrichten, Teil (a)**

Die Standardabweichung ist $\sigma=\sqrt{121}=11.00$.

Die Grenzen lauten $z_a=(62-62)/11.00\approx 0.0000$ und $z_b=(74-62)/11.00\approx 1.0909$. Mit den ungerundeten z-Werten gilt $P(62<X\leq 74)=\Phi((74-62)/11.00)-\Phi((62-62)/11.00)=0.3623$. Der modellierte Anteil beträgt somit 0.3623 für den Wertebereich **62 bis 74 Wertpunkte**.

**Ergebnis interpretieren und prüfen, Teil (b)**

$z_c=(48-62)/11.00\approx -1.2727$ und $z_d=(69-62)/11.00\approx 0.6364$. Daher ist $P(48<X\leq 69)=\Phi((69-62)/11.00)-\Phi((48-62)/11.00)=0.6362$. Dies ist der modellierte Anteil für den Wertebereich **48 bis 69 Wertpunkte**. Bei einem stetigen Modell verändert die Einbeziehung einer Grenze die Wahrscheinlichkeit nicht.

### T02-A13-V08: Intervallwahrscheinlichkeiten: Katalogisierungswert

**Berechnung einrichten, Teil (a)**

Die Standardabweichung ist $\sigma=\sqrt{49}=7.00$.

Die Grenzen lauten $z_a=(81-86)/7.00\approx -0.7143$ und $z_b=(93-86)/7.00\approx 1.0000$. Mit den ungerundeten z-Werten gilt $P(81<X\leq 93)=\Phi((93-86)/7.00)-\Phi((81-86)/7.00)=0.6038$. Der modellierte Anteil beträgt somit 0.6038 für den Wertebereich **81 bis 93 Wertpunkte**.

**Ergebnis interpretieren und prüfen, Teil (b)**

$z_c=(74-86)/7.00\approx -1.7143$ und $z_d=(90-86)/7.00\approx 0.5714$. Daher ist $P(74<X\leq 90)=\Phi((90-86)/7.00)-\Phi((74-86)/7.00)=0.6729$. Dies ist der modellierte Anteil für den Wertebereich **74 bis 90 Wertpunkte**. Bei einem stetigen Modell verändert die Einbeziehung einer Grenze die Wahrscheinlichkeit nicht.

### T02-A13-V09: Intervallwahrscheinlichkeiten: Schallpegel

**Berechnung einrichten, Teil (a)**

Die Standardabweichung ist $\sigma=\sqrt{36}=6.00$.

Die Grenzen lauten $z_a=(36-36)/6.00\approx 0.0000$ und $z_b=(42-36)/6.00\approx 1.0000$. Mit den ungerundeten z-Werten gilt $P(36<X\leq 42)=\Phi((42-36)/6.00)-\Phi((36-36)/6.00)=0.3413$. Der modellierte Anteil beträgt somit 0.3413 für den Wertebereich **36 bis 42 Dezibel**.

**Ergebnis interpretieren und prüfen, Teil (b)**

$z_c=(27-36)/6.00\approx -1.5000$ und $z_d=(39-36)/6.00\approx 0.5000$. Daher ist $P(27<X\leq 39)=\Phi((39-36)/6.00)-\Phi((27-36)/6.00)=0.6247$. Dies ist der modellierte Anteil für den Wertebereich **27 bis 39 Dezibel**. Bei einem stetigen Modell verändert die Einbeziehung einer Grenze die Wahrscheinlichkeit nicht.

### T02-A13-V10: Intervallwahrscheinlichkeiten: Zuversichtsbewertung

**Berechnung einrichten, Teil (a)**

Die Standardabweichung ist $\sigma=\sqrt{64}=8.00$.

Die Grenzen lauten $z_a=(51-55)/8.00\approx -0.5000$ und $z_b=(63-55)/8.00\approx 1.0000$. Mit den ungerundeten z-Werten gilt $P(51<X\leq 63)=\Phi((63-55)/8.00)-\Phi((51-55)/8.00)=0.5328$. Der modellierte Anteil beträgt somit 0.5328 für den Wertebereich **51 bis 63 Bewertungspunkte**.

**Ergebnis interpretieren und prüfen, Teil (b)**

$z_c=(43-55)/8.00\approx -1.5000$ und $z_d=(59-55)/8.00\approx 0.5000$. Daher ist $P(43<X\leq 59)=\Phi((59-55)/8.00)-\Phi((43-55)/8.00)=0.6247$. Dies ist der modellierte Anteil für den Wertebereich **43 bis 59 Bewertungspunkte**. Bei einem stetigen Modell verändert die Einbeziehung einer Grenze die Wahrscheinlichkeit nicht.
