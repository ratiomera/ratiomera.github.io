"""Natural de-CH and Albanian language data for Topic 2 practice.

The numerical values and statistical structure live in
``generate_topic02_materials.py``.  This module contains only translated,
language-dependent wording aligned row-for-row with the canonical English
data.  Keeping the two concerns separate lets the generator prove that every
locale uses the same IDs, formulas, numbers, and table geometry.
"""

from __future__ import annotations


DE_STAGE_CONTEXTS = [
    ("Eine Archivsuche abschliessen", "den Katalogeintrag finden", "die Archivschachtel anfordern", "den relevanten Brief bestimmen"),
    ("Eine dreistufige Sprachprüfung bestehen", "den Wortschatzteil bestehen", "den Hörverständnisteil bestehen", "das Gespräch bestehen"),
    ("Eine digitale Anmeldung abschliessen", "die E-Mail-Adresse bestätigen", "das Profil vervollständigen", "die Einwilligungserklärung absenden"),
    ("Eine Feldarbeitsabfolge lösen", "den Stichprobenpunkt finden", "eine gültige Messung erfassen", "den Datensatz korrekt hochladen"),
    ("Eine Bibliotheksrecherche abschliessen", "die Datenbank finden", "einen geeigneten Artikel abrufen", "dessen Methoden korrekt beurteilen"),
    ("In einem Musikvorspiel weiterkommen", "den Rhythmustest bestehen", "das vorbereitete Stück bestehen", "die Aufgabe zum Blattspiel bestehen"),
    ("Ein Laborprotokoll abschliessen", "die Probe vorbereiten", "einen brauchbaren Messwert erhalten", "das Ergebnis korrekt beschriften"),
    ("Einen Onlinekurs zur Sicherheit abschliessen", "das erste Modul abschliessen", "das Szenarioquiz bestehen", "die abschliessende Reflexion einreichen"),
    ("Eine Kartenleseaufgabe abschliessen", "die richtige Route auswählen", "den Kontrollpunkt erreichen", "die letzte Landmarke erkennen"),
    ("Eine Dateneingabeprüfung bestehen", "das erste Formular korrekt eingeben", "die Validierungswarnung beheben", "den bereinigten Datensatz absenden"),
]

SQ_STAGE_CONTEXTS = [
    ("Përfundimi i një kërkimi në arkiv", "të gjesh regjistrimin në katalog", "të kërkosh kutinë e arkivit", "të përcaktosh letrën përkatëse"),
    ("Kalimi i një vlerësimi gjuhësor me tri etapa", "të kalosh pjesën e fjalorit", "të kalosh pjesën e dëgjimit", "të kalosh intervistën"),
    ("Përfundimi i një regjistrimi digjital", "të verifikosh adresën e emailit", "të plotësosh profilin", "të dërgosh formularin e pëlqimit"),
    ("Përfundimi i një vargu hapash në terren", "të gjesh pikën e kampionimit", "të regjistrosh një matje të vlefshme", "ta ngarkosh regjistrimin saktë"),
    ("Përfundimi i një kërkimi bibliotekar", "të gjesh bazën e të dhënave", "të marrësh një artikull të përshtatshëm", "t'i vlerësosh saktë metodat e tij"),
    ("Kalimi i etapave të një audicioni muzikor", "të kalosh provën e ritmit", "të kalosh pjesën e përgatitur", "të kalosh provën e leximit të notave në çast"),
    ("Përfundimi i një protokolli laboratorik", "të përgatitësh mostrën", "të marrësh një lexim të përdorshëm", "ta etiketosh rezultatin saktë"),
    ("Përfundimi i një kursi në internet për sigurinë", "të përfundosh modulin e parë", "të kalosh kuizin me situata", "të dorëzosh reflektimin përfundimtar"),
    ("Përfundimi i një sfide për leximin e hartës", "të zgjedhësh rrugën e saktë", "të arrish pikën e kontrollit", "të dallosh pikën e fundit orientuese"),
    ("Kalimi i një kontrolli të futjes së të dhënave", "ta plotësosh saktë formularin e parë", "ta zgjidhësh paralajmërimin e validimit", "ta dorëzosh regjistrimin e pastruar"),
]


DE_INDEPENDENT_CONTEXTS = [
    ("Zwei unabhängige Qualitätsprüfungen", "eine gescannte Seite die Bildprüfung besteht", "dieselbe Seite die Metadatenprüfung besteht"),
    ("Unabhängige Teilnahme an Workshops", "eine Einwohnerin oder ein Einwohner die Morgensitzung besucht", "dieselbe Person die Abendsitzung besucht"),
    ("Zwei unabhängige Sensoralarme", "der Temperatursensor auslöst", "der Vibrationssensor auslöst"),
    ("Unabhängige Merkmale ausgewählter Bücher", "ein ausgewähltes Buch eine Übersetzung ist", "es einen festen Einband hat"),
    ("Unabhängige Ereignisse in einer Befragung", "eine Antwort am Montag eingeht", "sie mit einem Mobilgerät abgeschickt wird"),
    ("Zwei unabhängige Verkehrsereignisse", "ein Bus innerhalb von fünf Minuten ankommt", "in einem Anschlusszug ein Sitzplatz frei ist"),
    ("Unabhängige Codierungsprüfungen", "ein Datensatz ein gültiges Datum enthält", "er einen gültigen Kategoriecode enthält"),
    ("Zwei unabhängige Ziehungen", "ein ausgewählter Spielstein blau ist", "bei einer zweiten Ziehung mit Zurücklegen ein Dreieck gezogen wird"),
    ("Unabhängige Studienereignisse", "eine teilnehmende Person das Tagebuch abschliesst", "die Labordatei erfolgreich hochgeladen wird"),
    ("Unabhängige Katalogmerkmale", "ein Objekt digitalisiert ist", "sein Feld zur Urheberschaft vollständig ist"),
]

SQ_INDEPENDENT_CONTEXTS = [
    ("Dy kontrolle të pavarura të cilësisë", "një faqe e skanuar e kalon kontrollin e figurës", "e njëjta faqe e kalon kontrollin e metadatave"),
    ("Pjesëmarrje e pavarur në punëtori", "një banor merr pjesë në seancën e mëngjesit", "i njëjti banor merr pjesë në seancën e mbrëmjes"),
    ("Dy sinjale të pavarura sensorësh", "aktivizohet sensori i temperaturës", "aktivizohet sensori i dridhjeve"),
    ("Veçori të pavarura të librave të zgjedhur", "një libër i zgjedhur është përkthim", "ai ka kopertinë të fortë"),
    ("Ngjarje të pavarura në një anketë", "një përgjigje arrin të hënën", "ajo dërgohet nga një pajisje celulare"),
    ("Dy ngjarje të pavarura udhëtimi", "një autobus arrin brenda pesë minutash", "një tren lidhës ka vend të lirë"),
    ("Kontrolle të pavarura të kodimit", "një regjistrim ka datë të vlefshme", "ai ka kod të vlefshëm kategorie"),
    ("Dy zgjedhje të pavarura", "një pullë e zgjedhur është blu", "në një zgjedhje të dytë me rikthim del një trekëndësh"),
    ("Ngjarje të pavarura studimi", "një pjesëmarrës e plotëson ditarin", "skedari i laboratorit ngarkohet me sukses"),
    ("Veçori të pavarura të katalogut", "një objekt është digjitalizuar", "fusha e krijuesit të tij është e plotë"),
]


DE_TABLE_CONTEXTS = [
    ("Leseformat und Kursabschluss", "Audio", "Text", "Abgeschlossen", "Nicht abgeschlossen"),
    ("Museumsmitgliedschaft und Veranstaltungsbesuch", "Mitglied", "Nichtmitglied", "Teilgenommen", "Nicht teilgenommen"),
    ("Lernort und Einhaltung der Frist", "Bibliothek", "Zuhause", "Fristgerecht", "Verspätet"),
    ("Untertitel und Quizabschluss", "Untertitel", "Keine Untertitel", "Abgeschlossen", "Nicht abgeschlossen"),
    ("Verkehrsabonnement und Campusbesuche", "Abonnement", "Kein Abonnement", "Häufig", "Selten"),
    ("Erinnerung und Antwort", "Erinnerung", "Keine Erinnerung", "Geantwortet", "Nicht geantwortet"),
    ("Workshop-Schwerpunkt und Zertifizierung", "Methoden", "Schreiben", "Zertifiziert", "Nicht zertifiziert"),
    ("Gerätetyp und Formularabschluss", "Tablet", "Laptop", "Vollständig", "Unvollständig"),
    ("Freiwilligenrolle und erneuter Besuch", "Führung", "Archiv", "Zurückgekehrt", "Nicht zurückgekehrt"),
    ("Tutorialformat und Abgabe der Übung", "Live", "Aufgezeichnet", "Eingereicht", "Nicht eingereicht"),
]

SQ_TABLE_CONTEXTS = [
    ("Formati i leximit dhe përfundimi i kursit", "Audio", "Tekst", "Përfunduar", "Papërfunduar"),
    ("Anëtarësia në muze dhe pjesëmarrja në aktivitet", "Anëtar", "Joanëtar", "Mori pjesë", "Nuk mori pjesë"),
    ("Vendi i studimit dhe respektimi i afatit", "Bibliotekë", "Shtëpi", "Në kohë", "Me vonesë"),
    ("Përdorimi i titrave dhe përfundimi i kuizit", "Me titra", "Pa titra", "Përfunduar", "Papërfunduar"),
    ("Abonimi i transportit dhe vizitat në kampus", "Me abonim", "Pa abonim", "Të shpeshta", "Të rralla"),
    ("Kujtesa dhe përgjigjja", "Me kujtesë", "Pa kujtesë", "U përgjigj", "Nuk u përgjigj"),
    ("Drejtimi i punëtorisë dhe certifikimi", "Metoda", "Shkrim", "Certifikuar", "Pacertifikuar"),
    ("Lloji i pajisjes dhe plotësimi i formularit", "Tablet", "Laptop", "I plotë", "I paplotë"),
    ("Roli vullnetar dhe vizita e përsëritur", "Ciceron", "Arkiv", "U kthye", "Nuk u kthye"),
    ("Formati i tutorialit dhe dorëzimi i ushtrimit", "Drejtpërdrejt", "I regjistruar", "Dorëzuar", "Padorëzuar"),
]


DE_BAYES_CONTEXTS = [
    ("Screening auf Unterstützungsbedarf bei Barrierefreiheit", "einen Unterstützungsbedarf im Bereich Barrierefreiheit"),
    ("Erkennung seltener Transkriptionsfehler", "einen Transkriptionsfehler"),
    ("Screening auf Konservierungsrisiken", "ein konservatorisch gefährdetes Objekt"),
    ("Erkennung doppelter Datensätze", "einen doppelten Datensatz"),
    ("Screening auf Sprachunterstützungsbedarf", "einen Bedarf an Sprachunterstützung"),
    ("Erkennung beschädigter Bilder", "ein beschädigtes Bild"),
    ("Screening zur Forschungsintegrität", "eine Einreichung, die auf Forschungsintegrität geprüft werden sollte"),
    ("Warnung vor Geräteausfall", "einen bevorstehenden Geräteausfall"),
    ("Erkennung von Katalogisierungsanomalien", "einen Datensatz mit einer Katalogisierungsanomalie"),
    ("Klassifikation nach Unterstützungspriorität", "einen Fall mit tatsächlich hoher Unterstützungspriorität"),
]

SQ_BAYES_CONTEXTS = [
    ("Depistimi i nevojave për mbështetje në qasshmëri", "një nevojë për mbështetje në qasshmëri"),
    ("Zbulimi i gabimeve të rralla të transkriptimit", "një gabim transkriptimi"),
    ("Depistimi i rrezikut të konservimit", "një objekt në rrezik konservimi"),
    ("Zbulimi i regjistrimeve të dyfishta", "një regjistrim të dyfishtë"),
    ("Depistimi i nevojës për mbështetje gjuhësore", "një nevojë për mbështetje gjuhësore"),
    ("Zbulimi i figurave të dëmtuara", "një figurë të dëmtuar"),
    ("Depistimi i integritetit kërkimor", "një dorëzim që kërkon shqyrtim të integritetit"),
    ("Paralajmërimi për defekt të pajisjes", "një defekt të afërt të pajisjes"),
    ("Zbulimi i anomalive të katalogimit", "një regjistrim me anomali katalogimi"),
    ("Klasifikimi sipas përparësisë së mbështetjes", "një rast që ka vërtet përparësi të lartë mbështetjeje"),
]


DE_DISCRETE_TITLES = [
    "Anzahl der Anschlussfragen", "Tägliche Archivanfragen", "Abgeschlossene Übungsserien",
    "Gemeldete Routenänderungen", "Wöchentliche Gemeinschaftstreffen", "Erfolgreiche Dateiwiederherstellungen",
    "Besuchte Museumsräume", "Abgeschlossene optionale Lektüren", "Verifizierte Abschnitte mündlicher Überlieferungen",
    "Warnungen zur Datenqualität",
]

SQ_DISCRETE_TITLES = [
    "Numri i pyetjeve pasuese", "Kërkesat ditore në arkiv", "Seritë e përfunduara të ushtrimeve",
    "Ndryshimet e raportuara të rrugës", "Takimet javore të komunitetit", "Rikuperimet e suksesshme të skedarëve",
    "Dhomat e vizituara të muzeut", "Leximet plotësuese të përfunduara", "Segmentet e verifikuara të historisë gojore",
    "Paralajmërimet për cilësinë e të dhënave",
]


DE_BINOMIAL_EXACT = [
    ("Abgeschlossene Einwilligungsprüfungen", "Einwilligungsprüfungen", "abgeschlossen ist"),
    ("Korrekt klassifizierte Bilder", "Bilder", "korrekt klassifiziert ist"),
    ("Zurückgesandte Tagebuchaufforderungen", "Tagebuchaufforderungen", "zurückgesandt wird"),
    ("Erfolgreiche Archivsuche", "Archivsuchvorgänge", "erfolgreich ist"),
    ("Brauchbare Sensormesswerte", "Sensormesswerte", "brauchbar ist"),
    ("Fristgerechte Tutorialabgaben", "Tutorialabgaben", "fristgerecht eingeht"),
    ("Verifizierte Katalogeinträge", "Katalogeinträge", "verifiziert ist"),
    ("Wahrgenommene Interviewtermine", "Interviewtermine", "wahrgenommen wird"),
    ("Richtige Routenwahlen", "Routenwahlen", "richtig ist"),
    ("Erfolgreiche Audiotranskriptionen", "Audiotranskriptionen", "erfolgreich ist"),
]

SQ_BINOMIAL_EXACT = [
    ("Kontrollet e përfunduara të pëlqimit", "kontrolle pëlqimi", "përfundohet"),
    ("Figurat e klasifikuara saktë", "figura", "klasifikohet saktë"),
    ("Kërkesat e kthyera të ditarit", "kërkesa ditari", "kthehet"),
    ("Kërkimet e suksesshme në arkiv", "kërkime në arkiv", "ka sukses"),
    ("Leximet e përdorshme të sensorit", "lexime sensori", "është i përdorshëm"),
    ("Dorëzimet në kohë të tutorialit", "dorëzime tutoriali", "arrin në kohë"),
    ("Regjistrimet e verifikuara të katalogut", "regjistrime katalogu", "verifikohet"),
    ("Takimet e përfunduara të intervistës", "takime interviste", "përfundohet"),
    ("Zgjedhjet e sakta të rrugës", "zgjedhje rruge", "është e saktë"),
    ("Transkriptimet e suksesshme të audios", "transkriptime audioje", "ka sukses"),
]


DE_BINOMIAL_TAIL = [
    ("Datensätze mit manueller Prüfung", "Datensätzen", "eine manuelle Prüfung benötigt"),
    ("Museumsbesuchende mit Audioguide", "Museumsbesuchenden", "einen Audioguide verlangt"),
    ("ungültige Umfragelinks", "Umfragelinks", "als ungültig zurückkommt"),
    ("Objekte mit Konservierungsbedarf", "Objekten", "Konservierungsarbeit benötigt"),
    ("Teilnehmende mit verpasster Erinnerung", "Teilnehmenden", "eine Erinnerung verpasst"),
    ("Uploads mit einem zweiten Versuch", "Uploads", "einen zweiten Versuch benötigt"),
    ("ausgewählte Seiten mit Anmerkungen", "ausgewählten Seiten", "Anmerkungen enthält"),
    ("Interviews mit neuem Termin", "Interviews", "neu angesetzt werden muss"),
    ("Routenbeobachtungen mit Verspätung", "Routenbeobachtungen", "eine Verspätung zeigt"),
    ("Formulare mit optionalem Kommentar", "Formularen", "einen optionalen Kommentar enthält"),
]

SQ_BINOMIAL_TAIL = [
    ("Regjistrime që kërkojnë shqyrtim manual", "regjistrime", "kërkon shqyrtim manual"),
    ("Vizitorë që kërkojnë audiociceron", "vizitorë muzeu", "kërkon audiociceron"),
    ("Lidhje të pavlefshme të anketës", "lidhje ankete", "kthehet si e pavlefshme"),
    ("Objekte që kërkojnë konservim", "objekte", "kërkon punë konservimi"),
    ("Pjesëmarrës që humbin një kujtesë", "pjesëmarrës", "humb një kujtesë"),
    ("Ngarkime që kërkojnë një përpjekje të dytë", "ngarkime", "kërkon një përpjekje të dytë"),
    ("Faqe të zgjedhura që përmbajnë shënime", "faqe të zgjedhura", "përmban shënime"),
    ("Intervista që kërkojnë ricaktim", "intervista", "kërkon ricaktim"),
    ("Vëzhgime të rrugës që tregojnë vonesë", "vëzhgime rruge", "tregon vonesë"),
    ("Formularë që përmbajnë koment fakultativ", "formularë", "përmban një koment fakultativ"),
]


DE_PMF_DENSITY = [
    ("die Anzahl besuchter Ausstellungen", "die in einem Museum verbrachte Zeit"),
    ("die Anzahl empfangener Nachrichten", "die Wartezeit bis zur nächsten Nachricht"),
    ("die Anzahl der Transkriptionsfehler", "die Dauer eines Audioabschnitts"),
    ("die Anzahl ausgeliehener Bücher", "die Masse eines zurückgesandten Pakets"),
    ("die Anzahl der Umfrageerinnerungen", "die Bearbeitungszeit einer antwortenden Person"),
    ("die Anzahl der Routenänderungen", "die zurückgelegte Distanz"),
    ("die Anzahl fehlender Felder", "das präzise gemessene Alter einer teilnehmenden Person"),
    ("die Anzahl der Workshopsitzungen", "der Schallpegel im Raum"),
    ("die Anzahl konservierter Fotografien", "die Temperatur im Archiv"),
    ("die Anzahl erfolgreicher Prüfungen", "die genaue Reaktionszeit bei einer Aufgabe"),
]

SQ_PMF_DENSITY = [
    ("numri i ekspozitave të vizituara", "koha e kaluar në muze"),
    ("numri i mesazheve të marra", "vonesa deri te mesazhi tjetër"),
    ("numri i gabimeve të transkriptimit", "kohëzgjatja e një segmenti audio"),
    ("numri i librave të huazuar", "masa e një pakoje të kthyer"),
    ("numri i kujtesave të anketës", "koha e plotësimit nga një person që përgjigjet"),
    ("numri i ndryshimeve të rrugës", "largësia e përshkuar"),
    ("numri i fushave që mungojnë", "mosha e një pjesëmarrësi e matur me saktësi"),
    ("numri i seancave të punëtorisë", "niveli i zërit në dhomë"),
    ("numri i fotografive të konservuara", "temperatura e arkivit"),
    ("numri i kontrolleve të suksesshme", "koha e saktë e reagimit në një detyrë"),
]


DE_GENERAL_NORMAL = [
    ("Leseflüssigkeitswert", "Wertpunkte"), ("Bearbeitungszeit im Archiv", "Minuten"),
    ("Wohlbefindenswert", "Wertpunkte"), ("Dauer des Museumsbesuchs", "Minuten"),
    ("Gedächtniswert", "Wertpunkte"), ("Schallpegelindex", "Indexpunkte"),
    ("Zuversichtswert im Kurs", "Wertpunkte"), ("Reaktionszeit", "Millisekunden"),
    ("Vertrauenswert in der Gemeinschaft", "Wertpunkte"), ("Genauigkeitswert der Katalogisierung", "Wertpunkte"),
]

SQ_GENERAL_NORMAL = [
    ("rezultatin e rrjedhshmërisë në lexim", "pikë"), ("kohën e përpunimit në arkiv", "minuta"),
    ("rezultatin e mirëqenies", "pikë"), ("kohëzgjatjen e vizitës në muze", "minuta"),
    ("rezultatin e kujtesës", "pikë"), ("indeksin e nivelit të zërit", "pikë indeksi"),
    ("rezultatin e sigurisë në kurs", "pikë"), ("kohën e reagimit", "milisekonda"),
    ("rezultatin e besimit në komunitet", "pikë"), ("rezultatin e saktësisë së katalogimit", "pikë"),
]

SQ_GENERAL_NORMAL_TITLES = [
    "Rezultati i rrjedhshmërisë në lexim", "Koha e përpunimit në arkiv",
    "Rezultati i mirëqenies", "Kohëzgjatja e vizitës në muze",
    "Rezultati i kujtesës", "Indeksi i nivelit të zërit",
    "Rezultati i sigurisë në kurs", "Koha e reagimit",
    "Rezultati i besimit në komunitet", "Rezultati i saktësisë së katalogimit",
]


DE_SAMPLING = [
    ("Lesewert", "Wertpunkte"), ("Bearbeitungszeit", "Minuten"),
    ("Wohlbefindensindex", "Indexpunkte"), ("Gedächtniswert", "Wertpunkte"),
    ("Vertrauensbewertung", "Bewertungspunkte"), ("Reaktionszeit", "Millisekunden"),
    ("Zuversichtswert", "Wertpunkte"), ("Besuchsdauer", "Minuten"),
    ("Genauigkeitswert", "Wertpunkte"), ("Schallindex", "Indexpunkte"),
]

SQ_SAMPLING = [
    ("rezultatin e leximit", "pikë"), ("kohën e përpunimit", "minuta"),
    ("indeksin e mirëqenies", "pikë indeksi"), ("rezultatin e kujtesës", "pikë"),
    ("vlerësimin e besimit", "pikë vlerësimi"), ("kohën e reagimit", "milisekonda"),
    ("rezultatin e sigurisë", "pikë"), ("kohëzgjatjen e vizitës", "minuta"),
    ("rezultatin e saktësisë", "pikë"), ("indeksin e zërit", "pikë indeksi"),
]


DE_NORMAL_INTERVALS = [
    ("Fokuswert", "Wertpunkte"), ("Lesewert", "Wertpunkte"),
    ("Besuchsdauer", "Minuten"), ("Gedächtniswert", "Wertpunkte"),
    ("Vertrauensindex", "Indexpunkte"), ("Reaktionszeit", "Millisekunden"),
    ("Wohlbefindenswert", "Wertpunkte"), ("Katalogisierungswert", "Wertpunkte"),
    ("Schallpegel", "Dezibel"), ("Zuversichtsbewertung", "Bewertungspunkte"),
]

SQ_NORMAL_INTERVALS = [
    ("rezultatin e përqendrimit", "pikë"), ("rezultatin e leximit", "pikë"),
    ("kohëzgjatjen e vizitës", "minuta"), ("rezultatin e kujtesës", "pikë"),
    ("indeksin e besimit", "pikë indeksi"), ("kohën e reagimit", "milisekonda"),
    ("rezultatin e mirëqenies", "pikë"), ("rezultatin e katalogimit", "pikë"),
    ("nivelin e zërit", "decibel"), ("vlerësimin e sigurisë", "pikë vlerësimi"),
]


DE_SAMPLING_BIAS = [
    (
        "QR-Befragung zur Parknutzung",
        "Eine Stadt schätzt die wöchentliche Parknutzung anhand einer Befragung von 640 Personen, die einen QR-Code im grössten zentralen Park der Stadt scannen.",
        "alle Einwohnerinnen und Einwohner der Stadt",
        "Personen, die während des Aushangs den grössten zentralen Park betreten, den Code bemerken und ihn scannen können",
        "die 640 Parkbesuchenden, die den Code scannten und die Befragung abschickten",
        "der Anteil aller Einwohnerinnen und Einwohner der Stadt, die wöchentlich irgendeinen Park nutzen",
        "der Anteil der 640 Antwortenden, die eine wöchentliche Parknutzung angeben",
        "Personen, die Parks häufig nutzen, betreten diesen Park eher. Ausserdem können sich Personen, die einen Code bemerken und scannen, hinsichtlich Interesse oder digitalem Zugang von anderen unterscheiden.",
        "Aus einem Register der Stadtbevölkerung eine Wahrscheinlichkeitsstichprobe ziehen und ausgewählte Nichtantwortende über mehrere Kontaktwege erneut anfragen.",
    ),
    (
        "Pendlerbefragung unter Inhabenden von Parkbewilligungen",
        "Eine Universität schätzt die mittlere Pendelzeit der Studierenden anhand von 820 Antworten auf eine E-Mail, die nur an Personen mit Parkbewilligung verschickt wurde.",
        "alle eingeschriebenen Studierenden",
        "die Liste der Universität mit Studierenden, die eine Parkbewilligung besitzen",
        "die 820 Inhabenden einer Parkbewilligung, die antworteten",
        "die mittlere Pendelzeit aller eingeschriebenen Studierenden",
        "die mittlere Pendelzeit der 820 Antwortenden",
        "Der Auswahlrahmen lässt Studierende aus, die zu Fuss gehen, mit dem Fahrrad oder öffentlichen Verkehrsmitteln fahren oder keine Bewilligung besitzen. Die Antwortbereitschaft kann zudem von der Pendelbelastung abhängen.",
        "Aus dem vollständigen Einschreiberegister ziehen, bei Bedarf nach wahrscheinlichem Verkehrsmittel schichten und bei den ausgewählten Studierenden nachfassen.",
    ),
    (
        "Zufriedenheit nach einer ausverkauften Ausstellung",
        "Ein Museum schätzt die Zufriedenheit während der ganzen Saison anhand von 510 Antworten, die am Ausgang einer einzigen ausverkauften Abendausstellung erhoben wurden.",
        "alle Museumsbesuchenden während der Zielsaison",
        "Besuchende beim Verlassen der ausverkauften Abendausstellung, denen die Ausgangsbefragung angeboten wurde",
        "die 510 Anwesenden, die diese Ausgangsbefragung abschlossen",
        "der mittlere Zufriedenheitswert aller Besuchenden in der Zielsaison",
        "der mittlere Zufriedenheitswert der 510 Antwortenden",
        "Ein aussergewöhnlich beliebter Abend muss andere Daten oder Ausstellungen nicht repräsentieren. Ob jemand die Befragung abschliesst, kann zudem von einer besonders guten oder schlechten Erfahrung abhängen.",
        "Besuche über verschiedene Ausstellungen, Tage und Zeiten auswählen, anschliessend eine Wahrscheinlichkeitsstichprobe der hinausgehenden Besuchenden einladen und Nichtantwort dokumentieren.",
    ),
    (
        "Befragung zum digitalen Zugang innerhalb einer App",
        "Eine Bibliothek schätzt den Bedarf an digitalem Zugang anhand von 430 Antworten auf eine Befragung, die nur in ihrer Smartphone-App beworben wurde.",
        "alle Bibliotheksnutzenden",
        "Bibliotheksnutzende, die die Smartphone-App verwenden und den Hinweis zur Befragung sehen konnten",
        "die 430 App-Nutzenden, die freiwillig antworteten",
        "der Anteil aller Bibliotheksnutzenden, die einen besseren digitalen Zugang benötigen",
        "der Anteil der 430 Antwortenden, die diesen Bedarf melden",
        "Nutzende ohne geeignetes Gerät oder App-Zugang können nicht in den Auswahlrahmen gelangen. Freiwillige Antworten auf eine Befragung zum Zugang können zudem von besonders starkem Bedarf oder Engagement geprägt sein.",
        "Aus dem vollständigen Nutzendenregister ziehen und zugängliche Antwortwege über Web, Telefon, Papier und persönliche Befragung anbieten.",
    ),
    (
        "Freiwilligenstunden aus Listen grosser Hilfsorganisationen",
        "Eine Region schätzt die mittleren wöchentlichen Freiwilligenstunden anhand von Datensätzen zu 760 Mitgliedern, die von grossen registrierten Hilfsorganisationen aufgelistet werden.",
        "alle Freiwilligen in der Region",
        "Mitgliederlisten, die von grossen registrierten Hilfsorganisationen bereitgestellt wurden",
        "die 760 aufgeführten Mitglieder, deren Datensätze verwendet wurden",
        "die mittleren wöchentlichen Freiwilligenstunden aller Freiwilligen in der Region",
        "die mittleren aufgezeichneten Wochenstunden dieser 760 aufgeführten Mitglieder",
        "Die Listen lassen informell tätige Freiwillige sowie Mitglieder kleiner oder nicht registrierter Gruppen aus. Formelle Mitgliederdaten können regelmässig und langfristig tätige Personen überrepräsentieren.",
        "Einen breiteren Auswahlrahmen aus verschiedenen Organisationstypen und Gemeinschaftsquellen aufbauen und innerhalb definierter Freiwilligenschichten zufällig auswählen.",
    ),
    (
        "Befragung zur Kursbelastung nach der Notenvergabe",
        "Eine Hochschule schätzt die wahrgenommene Kursbelastung anhand von 390 Studierenden, die nach der Veröffentlichung der Abschlussnoten auf der Lernplattform noch aktiv waren.",
        "alle in den Kurs eingeschriebenen Studierenden",
        "eingeschriebene Studierende, deren Plattformkonten nach der Notenvergabe aktiv blieben",
        "die 390 weiterhin aktiven Studierenden, die Angaben zur Belastung machten",
        "die mittlere wahrgenommene Belastung aller eingeschriebenen Studierenden",
        "die von den 390 Antwortenden gemeldete mittlere Belastung",
        "Studierende, die sich zurückzogen, den Kurs abbrachen oder die Plattform nicht mehr nutzten, fehlen. Die Antwortbereitschaft nach der Benotung kann mit der Belastung oder dem Kursergebnis zusammenhängen.",
        "Aus der ursprünglichen Kursliste auswählen, die Studierenden unabhängig von ihrer späteren Plattformaktivität kontaktieren und bei Nichtantwort nachfassen.",
    ),
    (
        "Verkehrsverspätungen aus Kommentaren mit Hashtag",
        "Ein Verkehrsunternehmen schätzt den Anteil als verspätet erlebter Fahrten anhand von 1 240 Kommentaren in sozialen Medien, die den Kampagnen-Hashtag enthalten.",
        "alle Fahrten von Passagieren während des Zielzeitraums",
        "öffentlich abrufbare Kommentare in sozialen Medien, die den Kampagnen-Hashtag verwenden",
        "die 1 240 abgerufenen Kommentare mit Hashtag",
        "der Anteil aller Fahrten, die als verspätet erlebt wurden",
        "der Anteil der 1 240 Kommentare, die eine Verspätung beschreiben",
        "Personen mit extremen Erfahrungen posten eher, eine Person kann mehrere Kommentare beitragen, und beobachtet werden Kommentare statt Fahrten.",
        "Fahrten aus Betriebsdaten auswählen und zu jeder ausgewählten Fahrt eine Antwort erheben, wobei die Fahrt die Analyseeinheit bleibt.",
    ),
    (
        "Formulare zum Quartierinteresse nach Vorstellungen",
        "Ein Kulturzentrum schätzt das Interesse im Quartier anhand von 570 ausgefüllten Formularen, die nur nach Veranstaltungen mit Eintrittskarte verteilt wurden.",
        "alle Einwohnerinnen und Einwohner des umliegenden Quartiers",
        "Personen mit Eintrittskarte, die die ausgewählten Vorstellungen verliessen und ein Formular angeboten bekamen",
        "die 570 Personen, die blieben und ein Formular ausfüllten",
        "der Anteil der Quartierbevölkerung mit Interesse an künftigen Programmen",
        "der Anteil der 570 Antwortenden, die Interesse äusserten",
        "Personen, die nicht bereits Veranstaltungen mit Eintrittskarte besuchen, fehlen im Auswahlrahmen. Das Bleiben zum Ausfüllen kann mit der Begeisterung für das Zentrum zusammenhängen.",
        "Einen Adressrahmen des Quartiers verwenden, Einwohnerinnen und Einwohner unabhängig vom Besuch auswählen und mehrere Antwortwege anbieten.",
    ),
    (
        "Schlafdaten von ganzjährig aktiven Wearable-Nutzenden",
        "Ein Forschungsteam schätzt die mittlere nächtliche Schlafdauer anhand von 680 Personen, die ein Wearable ein ganzes Jahr lang aktiv hielten.",
        "alle Nutzenden in der beabsichtigten Wearable-Population während des Jahres",
        "Nutzende mit zu Beginn des Beobachtungszeitraums aktivierten Konten",
        "die 680 ein Jahr lang verbliebenen Nutzenden mit vollständigen Schlafdaten",
        "die mittlere nächtliche Schlafdauer in der Population",
        "die mittlere aufgezeichnete nächtliche Schlafdauer der verbliebenen Nutzenden",
        "Die Bedingung einer einjährigen Nutzung schliesst unregelmässige oder früh ausgestiegene Personen aus. Verbleib und vollständiges Tragen können von Schlafgewohnheiten, Gesundheit oder Zufriedenheit mit dem Gerät abhängen.",
        "Nutzende beim Eintritt auswählen, Teilaufzeichnungen nach einem vorab festgelegten Plan für fehlende Daten behalten und verbliebene mit verlorenen Teilnehmenden vergleichen.",
    ),
    (
        "Archivfeedback erst nach einem Download",
        "Ein Archiv schätzt den Anteil erfolgreicher Suchversuche anhand von 450 Feedbackformularen, die erst erschienen, nachdem eine Person mindestens einen Datensatz heruntergeladen hatte.",
        "alle Suchversuche im Archiv während des Zielzeitraums",
        "Suchversuche, die mindestens einen Download erreichten und deshalb die Feedbackaufforderung erhielten",
        "die 450 eingereichten Feedbackformulare aus diesem eingeschränkten Auswahlrahmen",
        "der Anteil aller Suchversuche, die mit einem erfolgreichen Abruf endeten",
        "der Anteil der 450 Formulare, deren Absendende einen Erfolg melden",
        "Die Aufforderung erscheint erst nach einem erfolgreichen Ereignis. Fehlgeschlagene Suchen haben daher keinen Weg in den Auswahlrahmen, und unter den Personen mit Download kann zusätzliche Selbstselektion auftreten.",
        "Suchversuche beim Start auswählen, unabhängig von einem Download um Feedback bitten und jedem ausgewählten Versuch genau eine Antwortmöglichkeit zuordnen.",
    ),
]


DE_COVERAGE_CLAIMS = [
    (
        "Bildungsabschlüsse unter Fussballfans",
        "Eine berufliche Netzwerkplattform berichtet, dass 64% der Profile, die Northport FC als Lieblingsverein nennen, auch einen Hochschulabschluss angeben. Eine Schlagzeile macht daraus die Behauptung, 64% aller Fans von Northport FC hätten einen Hochschulabschluss.",
        "alle Personen, die Northport FC unterstützen",
        "Plattformmitglieder, die Northport FC in einem sichtbaren Profil nennen und Bildungsangaben machen",
        "Fans, die die berufliche Plattform nicht nutzen, den Verein nicht angeben oder keine Bildungsangabe machen, haben keinen Weg in die Prozentzahl. Die Plattformmitgliedschaft hängt zudem mit Bildung und Erwerbstätigkeit zusammen.",
        "Unter den analysierten Plattformprofilen, die Northport FC nannten und Bildungsangaben enthielten, meldeten 64% einen Hochschulabschluss.",
        "den Fanstatus zuerst definieren, Fans über einen nicht an die berufliche Plattform gebundenen Auswahlrahmen ziehen und ausgewählte Nichtantwortende erneut kontaktieren",
    ),
    (
        "Lesegewohnheiten aus einer E-Reader-Gemeinschaft",
        "Ein E-Reader-Forum stellt fest, dass 71% von 2 400 antwortenden Mitgliedern mindestens zwei Bücher pro Monat beenden. Ein Beitrag beschreibt 71% als Anteil aller Erwachsenen des Landes.",
        "alle Erwachsenen des Landes",
        "Mitglieder des E-Reader-Forums, die die Einladung sahen und freiwillig antworteten",
        "Erwachsene ohne E-Reader oder ohne Forum fehlen. Besonders engagierte Lesende treten dem Forum eher bei und antworten häufiger.",
        "Unter den antwortenden Mitgliedern dieses E-Reader-Forums gaben 71% an, mindestens zwei Bücher pro Monat zu beenden.",
        "aus einem populationsbasierten Auswahlrahmen für Erwachsene eine Wahrscheinlichkeitsstichprobe ziehen und mehrere Antwortwege anbieten",
    ),
    (
        "Fahrradnutzung aus einer Routenplanungs-App",
        "Eine Fahrrad-App berichtet, dass 58% der aktiven Nutzenden mindestens drei Fahrten pro Woche aufzeichnen. Das Ergebnis wird als Anteil der Stadtbevölkerung dargestellt, der so häufig Fahrrad fährt.",
        "alle Einwohnerinnen und Einwohner der Stadt",
        "aktive Nutzende der Fahrrad-App, die das Aufzeichnen von Fahrten erlauben",
        "Personen ohne Fahrradnutzung, ohne App oder mit deaktivierter Aufzeichnung fehlen. Häufig Fahrende bleiben eher aktive Nutzende.",
        "Unter aktiven App-Nutzenden mit eingeschalteter Fahrtenaufzeichnung verzeichneten 58% mindestens drei Fahrten pro Woche.",
        "Personen aus einem Stadtregister ziehen und ihre Fahrradnutzung unabhängig von der App-Nutzung messen",
    ),
    (
        "Museumsinteresse unter Newsletter-Abonnierenden",
        "Eine Befragung im Museumsnewsletter ergibt, dass 82% der Antwortenden eine neue Ausstellung besuchen möchten. Das Museum beschreibt dies als Interesse aller Einwohnerinnen und Einwohner der Region.",
        "alle Einwohnerinnen und Einwohner der Region",
        "Newsletter-Abonnierende des Museums, die die Nachricht öffneten und die Befragung abschlossen",
        "Bereits am Museum interessierte Personen abonnieren, öffnen und beantworten den Newsletter eher.",
        "Unter den Newsletter-Abonnierenden, die antworteten, sagten 82%, dass sie die Ausstellung besuchen möchten.",
        "die Regionalbevölkerung unabhängig vom Newsletter-Abonnement ziehen und Nichtantwort dokumentieren",
    ),
    (
        "Präferenz für Fernarbeit auf einer Coworking-Plattform",
        "Eine Coworking-Plattform berichtet, dass 76% der antwortenden Kontoinhabenden an den meisten Wochentagen Fernarbeit bevorzugen. Ein Nachrichtenbeitrag schreibt diese Präferenz allen erwerbstätigen Erwachsenen zu.",
        "alle erwerbstätigen Erwachsenen der Zielregion",
        "Kontoinhabende der Coworking-Plattform, die die Umfrage erhielten und beantworteten",
        "Die Plattform überrepräsentiert Personen mit Berufen, die Fernarbeit erlauben. Freiwillige mit starken Präferenzen antworten möglicherweise häufiger.",
        "Unter den antwortenden Kontoinhabenden dieser Coworking-Plattform bevorzugten 76% an den meisten Wochentagen Fernarbeit.",
        "erwerbstätige Erwachsene über Berufe und Arbeitsformen hinweg aus einem geeigneten Arbeitskräfte-Auswahlrahmen ziehen",
    ),
    (
        "Sprachgebrauch aus öffentlichen Profilfeldern",
        "Eine soziale Plattform zählt die Sprachen in 50 000 öffentlichen Profilen und schliesst daraus, dass 43% der Landesbevölkerung täglich drei Sprachen verwenden.",
        "alle Einwohnerinnen und Einwohner des Landes",
        "Plattformmitglieder mit öffentlichen Profilen, die mindestens eine Sprache aufführten",
        "Plattformzugang und öffentliche Profilangaben unterscheiden sich in der Bevölkerung. Eine aufgeführte Sprache belegt zudem keine tägliche Verwendung.",
        "Von den öffentlichen Profilen mit Sprachfeld in den analysierten Plattformdaten führten 43% mindestens drei Sprachen auf.",
        "aus einem Auswahlrahmen der Bevölkerung ziehen und eine klar definierte Frage zum alltäglichen Sprachgebrauch stellen",
    ),
    (
        "Wohlbefinden von Studierenden aus einer Lernplanungs-App",
        "Eine Lernplanungs-App stellt fest, dass 61% ihrer Antwortenden hohe akademische Belastung melden, und behandelt dies als Schätzung für alle Studierenden.",
        "alle eingeschriebenen Studierenden an den interessierenden Universitäten",
        "Nutzende der Lernplanungs-App, die die Frage zum Wohlbefinden bemerkten und beantworteten",
        "Studierende mit einer Planungs-App können sich hinsichtlich Belastung oder Organisation unterscheiden. Die Antwortbereitschaft kann mit der aktuellen Belastung zusammenhängen.",
        "Unter den App-Nutzenden, die antworteten, meldeten 61% hohe akademische Belastung.",
        "aus vollständigen Einschreibelisten ziehen und die ausgewählten Studierenden über mehrere Wege kontaktieren",
    ),
    (
        "Konzertbesuch aus Profilen von Ticketkonten",
        "Ein Ticketunternehmen beobachtet, dass 67% der Konten im letzten Jahr mindestens einer Konzertseite folgten, und schliesst daraus, dass 67% aller Einwohnerinnen und Einwohner ein Konzert besucht hätten.",
        "alle Personen der Zielbevölkerung",
        "registrierte Ticketkonten mit beobachtbarer Aktivität beim Folgen von Seiten",
        "Personen ohne Konto fehlen, eine Person kann mehrere Konten besitzen, und das Folgen einer Seite ist nicht dasselbe wie ein Konzertbesuch.",
        "Unter den beobachteten Ticketkonten folgten 67% im letzten Jahr mindestens einer Konzertseite.",
        "Personen statt Konten ziehen und ein klar definiertes Besuchsergebnis erfragen oder überprüfen",
    ),
    (
        "Zufriedenheit mit öffentlichen Verkehrsmitteln aus einer Mobile-Ticket-Stichprobe",
        "Ein Verkehrsunternehmen findet unter Nutzenden von Mobile-Tickets eine Zufriedenheit von 74% und stellt sie als Zufriedenheit aller Fahrgäste dar.",
        "alle Fahrgäste des Verkehrssystems im Zielzeitraum",
        "Fahrgäste, die ein Mobile-Ticket kauften und die Frage in der App erhielten",
        "Nutzende von Bargeld, Papiertickets, Abonnementen oder Zugänglichkeitsdiensten können nicht in den Auswahlrahmen gelangen. Die Zufriedenheit kann zudem die Antwortbereitschaft beeinflussen.",
        "Unter den Mobile-Ticket-Nutzenden, die auf die Frage in der App antworteten, meldeten 74% Zufriedenheit.",
        "Fahrten über Ticketarten, Routen und Zeiten hinweg auswählen und die ausgewählten Fahrgäste über zugängliche Antwortwege einladen",
    ),
    (
        "Freiwilligenarbeit aus Webseiten von Organisationen",
        "Profile auf den Webseiten grosser Hilfsorganisationen zeigen, dass 69% der aufgeführten Freiwilligen jeden Monat mitarbeiten. Der Wert wird als Anteil aller Freiwilligen in der Region berichtet.",
        "alle formell und informell tätigen Freiwilligen der Region",
        "Freiwillige, die von den in der Websuche enthaltenen grossen Hilfsorganisationen öffentlich aufgeführt werden",
        "Informelle Freiwillige, kleine Organisationen und Personen ohne öffentliches Profil fehlen. Regelmässig Mitwirkende werden zudem eher vorgestellt.",
        "Unter den von den einbezogenen grossen Hilfsorganisationen öffentlich aufgeführten Freiwilligen wurden 69% als monatlich mitwirkend beschrieben.",
        "einen breiteren Auswahlrahmen über verschiedene Organisationsgrössen und informelle Gemeinschaftsarbeit aufbauen und daraus Freiwillige ziehen",
    ),
]


DE_SURVIVOR_SELECTION = [
    (
        "Schadensmuster bei zurückgekehrten Lieferdrohnen",
        "Ingenieurinnen und Ingenieure untersuchen nur Lieferdrohnen, die zur Basis zurückgekehrt sind. Dabei zeigen sich viele Spuren an der Aussenhülle, aber wenige beim Navigationsmodul. Das Team muss entscheiden, welcher Bereich zusätzlichen Schutz benötigt.",
        "Drohnen, die trotz Beschädigung zurückkehrten und untersucht werden konnten",
        "Drohnen, die nicht zurückkehrten, darunter möglicherweise solche mit kritischen Schäden am Navigationsmodul",
        "Ein Schaden am Navigationsmodul kann die Rückkehr verhindern. Die dort beobachtete geringe Zahl von Spuren kann deshalb starke Selektion statt Sicherheit anzeigen.",
        "Protokolle gescheiterter Flüge und geborgene, nicht zurückgekehrte Drohnen untersuchen, bevor über die wertvollste Verstärkung entschieden wird",
    ),
    (
        "Lerngewohnheiten unter Personen mit Kursabschluss",
        "Ein Kursteam befragt nur Studierende, die einen schwierigen Onlinekurs abgeschlossen haben, und stellt fest, dass die meisten Wochenpläne verwendeten. Es schliesst daraus auf die Gewohnheiten aller Eingeschriebenen.",
        "Eingeschriebene, die bis zum Abschluss blieben und einem Interview zustimmten",
        "Studierende, die sich zurückzogen, sich nicht mehr anmeldeten oder dem Interview nicht zustimmten",
        "Planungsgewohnheiten können mit dem Durchhalten zusammenhängen. Die Auswahl nach Kursabschluss kann die beobachtete Gewohnheit deshalb ungewöhnlich häufig erscheinen lassen.",
        "die ursprüngliche Gruppe der Eingeschriebenen weiterverfolgen und vergleichbare Angaben von Personen mit und ohne Abschluss sammeln",
    ),
    (
        "Zuverlässigkeit noch eingesetzter Geräte",
        "Ein Labor untersucht Sensoren, die nach zwei Jahren noch im Einsatz sind, und findet kaum Korrosion. Es schliesst daraus, dass das ursprüngliche Sensormodell selten korrodiert.",
        "Sensoren, die zwei Jahre im Einsatz überstanden und für eine Untersuchung verfügbar blieben",
        "früher entfernte, entsorgte oder ersetzte Sensoren, möglicherweise weil Korrosion einen Ausfall verursachte",
        "Das interessierende Ergebnis kann bestimmen, ob ein Sensor beobachtbar bleibt. Dadurch verbleiben die am wenigsten beschädigten Einheiten in der untersuchten Gruppe.",
        "Wartungs- und Ersatzaufzeichnungen für die vollständige ursprüngliche Sensorkohorte einschliesslich ausgefallener Einheiten verwenden",
    ),
    (
        "Zufriedenheit unter wiederkehrenden Museumsbesuchenden",
        "Ein Museum befragt Personen bei ihrem fünften Besuch und findet eine sehr hohe Zufriedenheit. Es verwendet das Ergebnis zur Beschreibung aller Personen, die das Museum je besucht haben.",
        "Besuchende, die zufrieden oder motiviert genug waren, mindestens viermal zurückzukehren und erneut zu kommen",
        "Personen mit nur einem Besuch und Personen, die nicht zurückkehrten",
        "Frühere Zufriedenheit kann die Rückkehr beeinflussen. Eine Auswahl bei einem späteren Besuch filtert daher viele weniger zufriedene Erfahrungen heraus.",
        "Erstbesuche auswählen und diese Personen unabhängig von einer späteren Rückkehr weiterverfolgen",
    ),
    (
        "Arbeitsbelastung aus Berichten verbliebener Mitarbeitender",
        "Ein Unternehmen fragt Mitarbeitende, die fünf Jahre geblieben sind, nach ihrer Arbeitsbelastung im ersten Jahr und behauptet, die Antworten repräsentierten alle damals eingestellten Personen.",
        "Personen der Einstellungskohorte, die fünf Jahre blieben und antworteten",
        "Personen, die kündigten, entlassen wurden oder nach dem Austritt nicht erreichbar waren",
        "Die Belastung im ersten Jahr kann das Verlassen beeinflussen. Verbliebene Mitarbeitende können daher systematisch andere Erfahrungen berichten.",
        "Belastungsdaten vorausschauend für die vollständige Einstellungskohorte erheben und Austrittsinformationen aufbewahren",
    ),
    (
        "Genesung unter Personen mit abschliessender Nachkontrolle",
        "Eine Klinik schätzt den Behandlungserfolg anhand von Patientinnen und Patienten, die zum letzten Nachkontrolltermin zurückkehrten. Die meisten Anwesenden waren genesen.",
        "behandelte Personen, die die letzte Nachkontrolle besuchten und ein Ergebnis lieferten",
        "Personen, die wegen Verschlechterung, Genesung an einem anderen Ort, Umzug oder Rückzug nicht zur Nachkontrolle kamen",
        "Die Teilnahme an der Nachkontrolle kann vom Genesungsverlauf abhängen. Der beobachtete Anteil muss daher nicht alle behandelten Personen repräsentieren.",
        "die vollständige Gruppe behandelter Personen verfolgen und mehrere geeignete Wege zur Erhebung der Ergebnisse bei versäumten Terminen verwenden",
    ),
    (
        "Haltbarkeit überlebender Archivdateien",
        "Ein Archiv prüft digitale Dateien, die nach zehn Jahren noch geöffnet werden können, und stellt fest, dass fast alle intakte Metadaten besitzen. Es schliesst daraus auf eine gute Metadatenerhaltung in der ursprünglichen Sammlung.",
        "Dateien, die überlebten, auffindbar blieben und noch geöffnet werden konnten",
        "verlorene, beschädigte oder nicht auffindbare Dateien, deren Metadaten möglicherweise zu ihrem Verschwinden beitrugen",
        "Die Bedingung, dass eine Datei auffindbar und zu öffnen sein muss, kann genau die Ausfälle entfernen, die für die Beurteilung der Erhaltung nötig sind.",
        "das ursprüngliche Dateiinventar prüfen und fehlende sowie beschädigte Dateien als Ergebnisse zählen statt sie auszuschliessen",
    ),
    (
        "Zuversicht unter Finalistinnen und Finalisten",
        "Forschende fragen nur Personen im Finale eines Redewettbewerbs nach ihrer Zuversicht vor der ersten Runde und leiten daraus die Zuversicht aller Teilnehmenden ab.",
        "Personen, die jede frühere Runde überstanden und das Finale erreichten",
        "Personen, die früher ausschieden oder sich zurückzogen",
        "Anfängliche Zuversicht kann Leistung und Rückzug beeinflussen. Finalistinnen und Finalisten bilden daher eine ausgewählte Teilgruppe.",
        "die Zuversicht aller Teilnehmenden vor der ersten Runde messen und ihren späteren Wettbewerbsstatus festhalten",
    ),
    (
        "Fahrzeiten aus abgeschlossenen App-Routen",
        "Eine Navigations-App berechnet die mittlere Fahrzeit nur aus als abgeschlossen markierten Fahrten. Fahrten, bei denen die App vor der Ankunft geschlossen wurde, werden ausgeschlossen.",
        "aufgezeichnete Fahrten, die aktiv blieben, bis die App den Abschluss registrierte",
        "unterbrochene, abgebrochene oder aussergewöhnlich verzögerte Fahrten, deren App-Sitzung früh endete",
        "Lange oder problematische Fahrten werden möglicherweise eher früh geschlossen. Dadurch können abgeschlossene Routen schneller erscheinen.",
        "jede begonnene Fahrt als Teil der Kohorte definieren und unvollständige Routendaten untersuchen statt sie stillschweigend zu verwerfen",
    ),
    (
        "Lesefortschritt unter aktiven Abonnierenden",
        "Ein E-Book-Dienst untersucht den Lesefortschritt nur bei Personen, deren Abonnement nach einem Jahr noch aktiv war, und berichtet das Ergebnis für alle ursprünglichen Abonnierenden.",
        "Abonnierende, die das ganze Jahr aktiv blieben und auswertbare Fortschrittsdaten hatten",
        "Personen, die kündigten oder deren Konto während des Jahres inaktiv wurde",
        "Das Leseengagement kann die Kündigung beeinflussen. Aktive Abonnierende können deshalb ungewöhnlich hohe Fortschritte zeigen.",
        "die ursprüngliche Abonnierendenkohorte in der Analyse behalten und den Fortschritt bis zur Kündigung erfassen oder ehemalige Abonnierende nachverfolgen",
    ),
]


SQ_SAMPLING_BIAS = [
    (
        "Anketa me kod QR për përdorimin e parkut",
        "Një qytet vlerëson përdorimin javor të parqeve duke anketuar 640 persona që skanojnë një kod QR të vendosur brenda parkut të tij më të madh qendror.",
        "të gjithë banorët e qytetit",
        "personat që hyjnë në parkun më të madh qendror gjatë periudhës së afishimit, e vërejnë kodin dhe mund ta skanojnë",
        "640 vizitorët e parkut që skanuan kodin dhe e dorëzuan anketën",
        "përpjesëtimi i të gjithë banorëve të qytetit që përdorin cilindo park çdo javë",
        "përpjesëtimi i 640 të anketuarve që raportojnë përdorim javor të parkut",
        "Përdoruesit e shpeshtë të parqeve kanë më shumë gjasa të hyjnë në këtë park. Personat që vërejnë dhe skanojnë një kod mund të dallojnë nga të tjerët për nga interesi ose qasja digjitale.",
        "Të merret një kampion probabilitar nga një kornizë e banorëve të qytetit dhe të kontaktohen përsëri të përzgjedhurit që nuk përgjigjen përmes më shumë se një mënyre kontakti.",
    ),
    (
        "Anketa e udhëtimit mes mbajtësve të lejeve të parkimit",
        "Një universitet vlerëson kohën mesatare të udhëtimit të studentëve nga 820 përgjigje ndaj një emaili të dërguar vetëm te mbajtësit e lejeve të parkimit.",
        "të gjithë studentët e regjistruar",
        "lista e universitetit me studentët që kanë leje parkimi",
        "820 mbajtësit e lejeve të parkimit që u përgjigjën",
        "koha mesatare e udhëtimit për të gjithë studentët e regjistruar",
        "koha mesatare e udhëtimit për 820 personat që u përgjigjën",
        "Korniza lë jashtë studentët që ecin, përdorin biçikletën ose transportin publik, si dhe ata pa leje parkimi. Gatishmëria për t'u përgjigjur mund të varet edhe nga vështirësia e udhëtimit.",
        "Të merret kampion nga regjistri i plotë i studentëve, të shtresëzohet sipas mënyrës së mundshme të udhëtimit kur kjo ndihmon dhe të kontaktohen përsëri studentët e përzgjedhur.",
    ),
    (
        "Kënaqësia pas një ekspozite me të gjitha biletat e shitura",
        "Një muze vlerëson kënaqësinë gjatë gjithë sezonit nga 510 përgjigje të mbledhura në dalje të një ekspozite të vetme në mbrëmje me të gjitha biletat e shitura.",
        "të gjithë vizitorët e muzeut gjatë sezonit të synuar",
        "vizitorët që dolën nga ekspozita e mbrëmjes dhe të cilëve iu ofrua anketa në dalje",
        "510 të pranishmit që e plotësuan atë anketë në dalje",
        "rezultati mesatar i kënaqësisë mes të gjithë vizitorëve në sezonin e synuar",
        "rezultati mesatar i kënaqësisë mes 510 personave që u përgjigjën",
        "Një mbrëmje jashtëzakonisht e pëlqyer mund të mos përfaqësojë data ose ekspozita të tjera. Plotësimi i anketës mund të varet edhe nga një përvojë veçanërisht e mirë ose e keqe.",
        "Të përzgjidhen vizita në ekspozita, ditë dhe orare të ndryshme, pastaj të ftohet një kampion probabilitar i vizitorëve në dalje dhe të dokumentohet mospërgjigjja.",
    ),
    (
        "Anketa e qasjes digjitale brenda një aplikacioni",
        "Një bibliotekë vlerëson nevojat për qasje digjitale nga 430 përgjigje ndaj një ankete të reklamuar vetëm në aplikacionin e saj për telefon të mençur.",
        "të gjithë përdoruesit e bibliotekës",
        "përdoruesit e bibliotekës që përdorin aplikacionin dhe mund ta shihnin njoftimin e anketës",
        "430 përdoruesit e aplikacionit që dhanë përgjigje vullnetarisht",
        "përpjesëtimi i të gjithë përdoruesve të bibliotekës që kanë nevojë për qasje më të mirë digjitale",
        "përpjesëtimi i 430 të anketuarve që raportojnë këtë nevojë",
        "Përdoruesit pa pajisje të përshtatshme ose pa qasje në aplikacion nuk mund të hyjnë në kornizë. Personat që i përgjigjen vullnetarisht një ankete për qasjen mund të kenë nevoja ose angazhim jashtëzakonisht të madh.",
        "Të merret kampion nga regjistri i plotë i përdoruesve dhe të ofrohen mënyra të qasshme përgjigjeje në internet, me telefon, në letër dhe ballë për ballë.",
    ),
    (
        "Orët vullnetare nga listat e organizatave të mëdha bamirëse",
        "Një rajon vlerëson orët mesatare javore të punës vullnetare nga regjistrimet e 760 anëtarëve të listuar nga organizata të mëdha bamirëse të regjistruara.",
        "të gjithë vullnetarët në rajon",
        "listat e anëtarëve të dhëna nga organizata të mëdha bamirëse të regjistruara",
        "760 anëtarët e listuar, regjistrimet e të cilëve u përdorën",
        "orët mesatare javore të punës vullnetare mes të gjithë vullnetarëve në rajon",
        "orët mesatare javore të regjistruara për këta 760 anëtarë të listuar",
        "Listat lënë jashtë vullnetarët joformalë dhe anëtarët e grupeve të vogla ose të paregjistruara. Regjistrimet e anëtarësisë formale mund të mbipërfaqësojnë vullnetarët e rregullt dhe afatgjatë.",
        "Të ndërtohet një kornizë më e gjerë nga lloje të ndryshme organizatash dhe burime komunitare, pastaj të bëhet përzgjedhje probabilitare brenda shtresave të përcaktuara të vullnetarëve.",
    ),
    (
        "Anketa e ngarkesës së kursit pas notave",
        "Një kolegj vlerëson ngarkesën e perceptuar të kursit nga 390 studentë që ishin ende aktivë në platformën mësimore pasi u publikuan notat përfundimtare.",
        "të gjithë studentët e regjistruar në kurs",
        "studentët e regjistruar, llogaritë e të cilëve mbetën aktive në platformë pas publikimit të notave",
        "390 studentët ende aktivë që dhanë të dhëna për ngarkesën",
        "ngarkesa mesatare e perceptuar mes të gjithë studentëve të regjistruar",
        "ngarkesa mesatare e raportuar nga 390 personat që u përgjigjën",
        "Studentët që u shkëputën, u çregjistruan ose ndaluan së përdoruri platformën mungojnë. Gatishmëria për t'u përgjigjur pas vlerësimit mund të lidhet me ngarkesën ose rezultatet e kursit.",
        "Të përzgjidhet nga lista fillestare e kursit, studentët të kontaktohen pavarësisht aktivitetit të mëvonshëm në platformë dhe të ndiqen rastet e mospërgjigjes.",
    ),
    (
        "Vonesat e transportit nga komentet me hashtag",
        "Një agjenci transporti vlerëson përpjesëtimin e udhëtimeve të përjetuara si të vonuara nga 1 240 komente në media sociale që përmbajnë hashtagun e fushatës së saj.",
        "të gjitha udhëtimet e pasagjerëve gjatë periudhës së synuar",
        "komentet publike në media sociale që mund të merren dhe që përdorin hashtagun e fushatës",
        "1 240 komentet e marra me hashtag",
        "përpjesëtimi i të gjitha udhëtimeve të përjetuara si të vonuara",
        "përpjesëtimi i 1 240 komenteve që përshkruajnë një vonesë",
        "Personat me përvoja skajore kanë më shumë gjasa të postojnë, një person mund të japë disa komente, dhe njësitë e vëzhguara janë komentet në vend të udhëtimeve.",
        "Të përzgjidhen udhëtime nga regjistrimet operative dhe të merret një përgjigje për secilin udhëtim të zgjedhur, duke e mbajtur udhëtimin si njësi analize.",
    ),
    (
        "Formularët e interesit të lagjes pas shfaqjeve",
        "Një qendër kulturore vlerëson interesin e lagjes nga 570 formularë të plotësuar, të shpërndarë vetëm pas shfaqjeve me bileta.",
        "të gjithë banorët e lagjes përreth",
        "mbajtësit e biletave që dolën nga shfaqjet e zgjedhura dhe të cilëve iu ofrua një formular",
        "570 mbajtësit e biletave që qëndruan dhe plotësuan formularin",
        "përpjesëtimi i banorëve të lagjes që interesohen për programe të ardhshme",
        "përpjesëtimi i 570 të anketuarve që shprehën interes",
        "Banorët që nuk marrin tashmë pjesë në aktivitete me bileta mungojnë në kornizë. Qëndrimi për të plotësuar formularin mund të lidhet me entuziazmin për qendrën.",
        "Të përdoret një kornizë adresash të lagjes, banorët të përzgjidhen pavarësisht pjesëmarrjes dhe të ofrohen disa mënyra përgjigjeje.",
    ),
    (
        "Regjistrimet e gjumit nga përdoruesit vjetorë të pajisjeve që vishen",
        "Një ekip kërkimor vlerëson kohëzgjatjen mesatare të gjumit gjatë natës nga 680 persona që e mbajtën aktive një pajisje që vishet për një vit të plotë.",
        "të gjithë përdoruesit në popullatën e synuar të pajisjes gjatë vitit",
        "përdoruesit e pajisjes me llogari të aktivizuara në fillim të periudhës së vëzhgimit",
        "680 përdoruesit që qëndruan një vit të plotë me regjistrime të plota gjumi",
        "kohëzgjatja mesatare e gjumit gjatë natës në popullatë",
        "kohëzgjatja mesatare e regjistruar e gjumit te përdoruesit që qëndruan",
        "Qëndrimi për një vit lë jashtë përdoruesit e ndërprerë ose ata që hoqën dorë. Qëndrimi ose përdorimi i plotë i pajisjes mund të varet nga zakonet e gjumit, shëndeti ose kënaqësia me pajisjen.",
        "Përdoruesit të përzgjidhen në regjistrim, të ruhen të dhënat e pjesshme sipas një plani të paracaktuar për të dhënat që mungojnë dhe të krahasohen pjesëmarrësit e mbetur me ata të humbur.",
    ),
    (
        "Komentet për arkivin të shfaqura vetëm pas shkarkimit",
        "Një arkiv vlerëson përpjesëtimin e kërkimeve që përfundojnë me gjetje të suksesshme nga 450 formularë komentesh të shfaqur vetëm pasi përdoruesi shkarkoi të paktën një regjistrim.",
        "të gjitha përpjekjet e kërkimit në arkiv gjatë periudhës së synuar",
        "përpjekjet e kërkimit që arritën të paktën një shkarkim dhe prandaj morën kërkesën për koment",
        "450 formularët e dorëzuar të komenteve nga kjo kornizë e kufizuar",
        "përpjesëtimi i të gjitha kërkimeve që përfundojnë me gjetje të suksesshme",
        "përpjesëtimi i 450 formularëve, dërguesit e të cilëve raportojnë sukses",
        "Kërkesa shfaqet vetëm pas një rezultati të suksesshëm, kështu që kërkimet e dështuara nuk kanë rrugë për të hyrë në kornizë. Mes personave që shkarkojnë mund të ketë edhe vetëpërzgjedhje.",
        "Të përzgjidhen kërkimet në fillim, të kërkohet koment pavarësisht nëse ndodh shkarkimi dhe çdo kërkimi të përzgjedhur t'i lidhet një mundësi e vetme përgjigjeje.",
    ),
]


SQ_COVERAGE_CLAIMS = [
    (
        "Nivelet e arsimit mes përkrahësve të futbollit",
        "Një platformë rrjetëzimi profesional raporton se 64% e profileve që e shënojnë Northport FC si klub të parapëlqyer raportojnë edhe një diplomë universitare. Një titull lajmi e kthen këtë në pretendimin se 64% e të gjithë përkrahësve të Northport FC kanë diplomë universitare.",
        "të gjithë personat që përkrahin Northport FC",
        "anëtarët e platformës që e shënojnë Northport FC në një profil të dukshëm dhe japin të dhëna për arsimin",
        "Përkrahësit që nuk e përdorin platformën profesionale, nuk shënojnë klub ose nuk japin arsimimin nuk mund të hyjnë në përqindje. Anëtarësia në platformë lidhet edhe me arsimin dhe punësimin.",
        "Mes profileve të analizuara që shënonin Northport FC dhe përmbanin të dhëna për arsimin, 64% raportonin diplomë universitare.",
        "të përcaktohet fillimisht statusi i përkrahësit, të merret kampion përmes një kornize që nuk lidhet me anëtarësinë në platformën profesionale dhe të kontaktohen përsëri të përzgjedhurit që nuk përgjigjen",
    ),
    (
        "Zakonet e leximit nga një komunitet lexuesish elektronikë",
        "Një forum për lexues elektronikë gjen se 71% e 2 400 anëtarëve që u përgjigjën përfundojnë të paktën dy libra në muaj. Një postim e paraqet 71% si normë për të gjithë të rriturit në vend.",
        "të gjithë të rriturit në vend",
        "anëtarët e forumit që e panë ftesën dhe zgjodhën të përgjigjen",
        "Të rriturit që nuk përdorin lexues elektronik ose forum mungojnë. Lexuesit shumë aktivë kanë veçanërisht shumë gjasa të anëtarësohen dhe të përgjigjen.",
        "Mes anëtarëve të këtij forumi që u përgjigjën, 71% raportuan se përfundojnë të paktën dy libra në muaj.",
        "të merret një kampion probabilitar nga një kornizë popullate e të rriturve dhe të ofrohen disa mënyra përgjigjeje",
    ),
    (
        "Shpeshtësia e çiklizmit nga një aplikacion për planifikimin e rrugës",
        "Një aplikacion çiklizmi raporton se 58% e përdoruesve aktivë regjistrojnë të paktën tri udhëtime në javë. Rezultati paraqitet si pjesa e banorëve të qytetit që ngasin biçikletën kaq shpesh.",
        "të gjithë banorët e qytetit",
        "përdoruesit aktivë të aplikacionit që lejojnë regjistrimin e udhëtimeve",
        "Banorët që nuk përdorin biçikletë ose aplikacion, si dhe ata që e çaktivizojnë regjistrimin, mungojnë. Çiklistët e shpeshtë kanë më shumë gjasa të mbeten përdorues aktivë.",
        "Mes përdoruesve aktivë me regjistrimin e udhëtimeve të aktivizuar, 58% regjistruan të paktën tri udhëtime në javë.",
        "të merret kampion nga regjistri i qytetit dhe të matet shpeshtësia e çiklizmit pavarësisht përdorimit të aplikacionit",
    ),
    (
        "Interesi për muzeun nga abonentët e buletinit",
        "Një anketë e buletinit të muzeut gjen se 82% e personave që u përgjigjën planifikojnë të vizitojnë një ekspozitë të re. Muzeu e përshkruan këtë si nivelin e interesit mes të gjithë banorëve të rajonit.",
        "të gjithë banorët e rajonit",
        "abonentët e buletinit që e hapën mesazhin dhe e plotësuan anketën",
        "Personat që tashmë interesohen për muzeun kanë më shumë gjasa të abonohen, ta hapin mesazhin dhe t'i përgjigjen anketës.",
        "Mes abonentëve të buletinit që u përgjigjën, 82% thanë se planifikonin ta vizitonin ekspozitën.",
        "të merret kampion i banorëve të rajonit pavarësisht abonimit në buletin dhe të regjistrohet mospërgjigjja",
    ),
    (
        "Parapëlqimi për punën nga larg në një platformë bashkëpunimi",
        "Një platformë bashkëpunimi raporton se 76% e mbajtësve të llogarive që u përgjigjën parapëlqejnë punën nga larg në shumicën e ditëve të javës. Një lajm ia atribuon këtë parapëlqim të gjithë të rriturve të punësuar.",
        "të gjithë të rriturit e punësuar në rajonin e synuar",
        "mbajtësit e llogarive në platformë që morën dhe plotësuan pyetësorin",
        "Platforma mbipërfaqëson personat me punë që mund të bëhen nga larg. Vullnetarët me parapëlqime të forta mund të përgjigjen më shpesh.",
        "Mes mbajtësve të llogarive në këtë platformë që u përgjigjën, 76% parapëlqenin punën nga larg në shumicën e ditëve të javës.",
        "të merret kampion i të rriturve të punësuar në profesione dhe forma pune të ndryshme nga një kornizë e përshtatshme e fuqisë punëtore",
    ),
    (
        "Përdorimi i gjuhëve nga fushat e profileve publike",
        "Një platformë sociale numëron gjuhët e listuara në 50 000 profile publike dhe përfundon se 43% e popullatës së vendit përdor tri gjuhë çdo ditë.",
        "të gjithë banorët e vendit",
        "anëtarët e platformës me profile publike që zgjodhën të listojnë të paktën një gjuhë",
        "Qasja në platformë dhe zgjedhjet për profilin publik ndryshojnë mes banorëve. Listimi i një gjuhe nuk vërteton përdorim të përditshëm.",
        "Nga profilet publike me fushë gjuhësh në të dhënat e analizuara, 43% listonin të paktën tri gjuhë.",
        "të merret kampion nga një kornizë e popullatës dhe të bëhet një pyetje e përcaktuar qartë për përdorimin e përditshëm të gjuhëve",
    ),
    (
        "Mirëqenia e studentëve nga një aplikacion planifikimi",
        "Një aplikacion planifikimi studimi gjen se 61% e personave që u përgjigjën raportojnë stres të lartë akademik dhe e trajton këtë si vlerësim për çdo student universitar.",
        "të gjithë studentët e regjistruar në universitetet me interes",
        "përdoruesit e aplikacionit që e vunë re dhe iu përgjigjën pyetjes për mirëqenien",
        "Studentët që përdorin një aplikacion planifikimi mund të dallojnë në ngarkesë ose organizim. Gatishmëria për t'u përgjigjur mund të lidhet me stresin aktual.",
        "Mes përdoruesve të aplikacionit që u përgjigjën, 61% raportuan stres të lartë akademik.",
        "të merret kampion nga listat e plota të regjistrimit dhe studentët e përzgjedhur të kontaktohen në më shumë se një mënyrë",
    ),
    (
        "Pjesëmarrja në koncerte nga profilet e llogarive të biletave",
        "Një kompani biletash vëren se 67% e llogarive ndoqën të paktën një faqe koncerti vitin e kaluar dhe përfundon se 67% e të gjithë banorëve morën pjesë në koncert.",
        "të gjithë banorët në popullatën e synuar",
        "llogaritë e regjistruara me aktivitet të dukshëm në ndjekjen e faqeve",
        "Banorët pa llogari mungojnë, një person mund të ketë disa llogari, dhe ndjekja e një faqeje nuk është i njëjti rezultat si pjesëmarrja në koncert.",
        "Mes llogarive të vëzhguara, 67% ndoqën të paktën një faqe koncerti vitin e kaluar.",
        "të përzgjidhen persona në vend të llogarive dhe të pyetet ose verifikohet një rezultat pjesëmarrjeje i përcaktuar qartë",
    ),
    (
        "Kënaqësia me transportin publik nga një kampion biletash celulare",
        "Një operator transporti gjen 74% kënaqësi mes përdoruesve që blenë bileta celulare dhe e paraqet këtë si kënaqësi mes të gjithë pasagjerëve.",
        "të gjithë pasagjerët që përdorin sistemin e transportit gjatë periudhës së synuar",
        "pasagjerët që blenë biletë celulare dhe morën pyetjen në aplikacion",
        "Përdoruesit e parave të gatshme, biletave në letër, aboneve dhe shërbimeve të qasshmërisë nuk mund të hyjnë në kornizë. Kënaqësia mund të ndikojë edhe në përgjigjen ndaj pyetjes.",
        "Mes përdoruesve të biletave celulare që iu përgjigjën pyetjes në aplikacion, 74% raportuan kënaqësi.",
        "të përzgjidhen udhëtime në lloje biletash, rrugë dhe orare të ndryshme, pastaj pasagjerët e zgjedhur të ftohen përmes mënyrave të qasshme të përgjigjes",
    ),
    (
        "Pjesëmarrja vullnetare nga faqet e organizatave",
        "Profilet në faqet e organizatave të mëdha bamirëse tregojnë se 69% e vullnetarëve të listuar kontribuojnë çdo muaj. Shifra raportohet si normë për të gjithë vullnetarët e rajonit.",
        "të gjithë vullnetarët formalë dhe joformalë në rajon",
        "vullnetarët e listuar publikisht nga organizatat e mëdha bamirëse të përfshira në kërkimin në internet",
        "Mungojnë vullnetarët joformalë, organizatat e vogla dhe vullnetarët pa profile publike. Personat që kontribuojnë rregullisht kanë më shumë gjasa të paraqiten në faqe.",
        "Mes vullnetarëve të listuar publikisht nga organizatat e mëdha bamirëse të përfshira, 69% përshkruheshin si kontribues të përmuajshëm.",
        "të ndërtohet një kornizë më e gjerë me organizata të madhësive të ndryshme dhe punë joformale në komunitet, pastaj të merret kampion vullnetarësh brenda saj",
    ),
]


SQ_SURVIVOR_SELECTION = [
    (
        "Modelet e dëmtimit te dronët e kthyer të dërgesave",
        "Inxhinierët shqyrtojnë vetëm dronët e dërgesave që u kthyen në bazë. Ata vërejnë shumë shenja në mbështjellësin e jashtëm, por pak pranë njësisë së navigimit, dhe duhet të vendosin se cila zonë ka më shumë nevojë për mbrojtje shtesë.",
        "dronët që u dëmtuan, por megjithatë u kthyen dhe mund të shqyrtoheshin",
        "dronët që nuk u kthyen, përfshirë ata që mund të kenë pësuar dëmtim kritik të njësisë së navigimit",
        "Dëmtimi i njësisë së navigimit mund ta pengojë kthimin. Prandaj numri i ulët i shenjave të vëzhguara aty mund të tregojë përzgjedhje të fortë, jo siguri.",
        "të shqyrtohen regjistrimet e fluturimeve të dështuara dhe dronët e pakthyer që janë gjetur para se të vendoset se ku ka më shumë vlerë përforcimi",
    ),
    (
        "Zakonet e studimit mes personave që përfunduan kursin",
        "Një ekip kursi interviston vetëm studentët që përfunduan një kurs të vështirë në internet dhe gjen se shumica përdorën plane javore. Ekipi përfundon se këto janë zakonet e të gjithë personave që u regjistruan.",
        "personat e regjistruar që qëndruan deri në përfundim dhe pranuan të intervistoheshin",
        "studentët që u çregjistruan, ndaluan së hyrë në platformë ose nuk pranuan intervistën",
        "Zakonet e planifikimit mund të lidhen me këmbënguljen. Përzgjedhja sipas përfundimit mund ta bëjë zakonin e vëzhguar të duket jashtëzakonisht i shpeshtë.",
        "të ndiqet grupi fillestar i të regjistruarve dhe të mblidhen të dhëna të krahasueshme nga ata që e përfunduan dhe ata që nuk e përfunduan kursin",
    ),
    (
        "Besueshmëria mes pajisjeve ende në përdorim",
        "Një laborator shqyrton sensorët që mbeten në përdorim pas dy vjetësh dhe gjen shumë pak korrozion. Laboratori përfundon se modeli fillestar i sensorit rrallë gërryhet.",
        "sensorët që mbijetuan në përdorim për dy vjet dhe ishin ende të disponueshëm për shqyrtim",
        "sensorët e hequr, hedhur ose zëvendësuar më herët, ndoshta sepse korrozioni shkaktoi defekt",
        "Rezultati me interes mund të përcaktojë nëse sensori mbetet i vëzhgueshëm, duke lënë në grupin e shqyrtuar njësitë më pak të dëmtuara.",
        "të përdoren regjistrimet e mirëmbajtjes dhe zëvendësimit për të gjithë grupin fillestar të sensorëve, përfshirë njësitë që dështuan",
    ),
    (
        "Kënaqësia mes vizitorëve që kthehen në muze",
        "Një muze anketon njerëzit në vizitën e pestë dhe gjen kënaqësi shumë të lartë. Muzeu e përdor rezultatin për të përshkruar këdo që e ka vizituar ndonjëherë.",
        "vizitorët që ishin mjaft të kënaqur ose të motivuar për t'u kthyer të paktën katër herë dhe për të ardhur përsëri",
        "vizitorët që erdhën vetëm një herë dhe personat që vendosën të mos kthehen",
        "Kënaqësia e mëparshme mund të ndikojë në kthim. Përzgjedhja në një vizitë të mëvonshme filtron shumë përvoja më pak të kënaqshme.",
        "të merret kampion në vizitën e parë dhe këta vizitorë të ndiqen pavarësisht nëse kthehen",
    ),
    (
        "Raportet e ngarkesës nga punonjësit që qëndruan",
        "Një kompani pyet punonjësit që kanë qëndruar pesë vjet për ngarkesën në vitin e parë dhe përfundon se përgjigjet përfaqësojnë çdo person të punësuar atë vit.",
        "punonjësit nga grupi i të punësuarve që qëndruan pesë vjet dhe u përgjigjën",
        "punonjësit që dhanë dorëheqje, u larguan nga puna ose nuk mund të kontaktoheshin pasi u larguan",
        "Ngarkesa e vitit të parë mund të ndikojë në largim. Punonjësit që qëndruan mund të raportojnë përvoja sistematikisht të ndryshme.",
        "të mblidhen të dhëna për ngarkesën në mënyrë prospektive nga i gjithë grupi fillestar dhe të ruhen të dhënat e largimit",
    ),
    (
        "Shërimi mes pacientëve që erdhën në kontrollin përfundimtar",
        "Një klinikë vlerëson shërimin pas trajtimit nga pacientët që u kthyen për takimin e fundit të kontrollit. Shumica e atyre që erdhën ishin shëruar.",
        "pacientët e trajtuar që erdhën në kontrollin përfundimtar dhe dhanë rezultat",
        "pacientët që munguan sepse gjendja u përkeqësua, u shëruan diku tjetër, u zhvendosën ose u shkëputën",
        "Pjesëmarrja në kontroll mund të varet nga shërimi. Prandaj përqindja e vëzhguar nuk ka pse t'i përfaqësojë të gjithë pacientët e trajtuar.",
        "të gjurmohet i gjithë grupi i trajtuar dhe të përdoren disa mënyra të përshtatshme për të marrë rezultatet e personave që mungojnë në kontroll",
    ),
    (
        "Qëndrueshmëria mes skedarëve të mbijetuar të arkivit",
        "Një arkiv kontrollon skedarët digjitalë që mund të hapen ende pas dhjetë vjetësh dhe gjen se pothuajse të gjithë kanë metadata të paprekura. Arkivi përfundon se koleksioni fillestar i ruajti mirë metadatat.",
        "skedarët që mbijetuan, mbetën të gjetshëm dhe mund të hapeshin ende",
        "skedarët e humbur, dëmtuar ose të pagjetshëm, metadatat e të cilëve mund të kenë ndikuar në zhdukjen e tyre",
        "Kushti që një skedar duhet të gjendet dhe të hapet mund të heqë pikërisht dështimet që nevojiten për të vlerësuar ruajtjen.",
        "të auditohet inventari fillestar dhe skedarët që mungojnë ose janë dëmtuar të numërohen si rezultate në vend që të përjashtohen",
    ),
    (
        "Siguria mes finalistëve të një gare",
        "Studiuesit pyesin vetëm finalistët e një gare të të folurit publik për sigurinë para raundit të parë dhe nxjerrin përfundim për nivelin e sigurisë së çdo garuesi.",
        "garuesit që kaluan çdo raund të mëparshëm dhe arritën në finale",
        "garuesit që u eliminuan në raunde të mëparshme ose u tërhoqën",
        "Siguria fillestare mund të ndikojë në paraqitje dhe tërheqje. Finalistët përbëjnë kështu një nëngrup të përzgjedhur.",
        "të matet siguria e të gjithë garuesve para raundit të parë dhe të ruhet statusi i tyre i mëvonshëm në garë",
    ),
    (
        "Kohët e udhëtimit nga rrugët e përfunduara në aplikacion",
        "Një aplikacion navigimi llogarit kohën mesatare të udhëtimit duke përdorur vetëm udhëtimet e shënuara si të përfunduara. Ai përjashton udhëtimet e personave që e mbyllën aplikacionin para mbërritjes.",
        "udhëtimet e regjistruara që mbetën aktive derisa aplikacioni regjistroi përfundimin",
        "udhëtimet e ndërprera, braktisura ose jashtëzakonisht të vonuara, seancat e të cilave përfunduan herët",
        "Udhëtimet e gjata ose problematike mund të mbyllen më shpesh para kohe, duke i bërë rrugët e përfunduara të duken më të shpejta.",
        "çdo udhëtim i nisur të përcaktohet si pjesë e grupit dhe të shqyrtohen regjistrimet e paplota në vend që të hiqen pa shpjegim",
    ),
    (
        "Përparimi në lexim mes abonentëve aktivë",
        "Një shërbim librash elektronikë studion përparimin në lexim vetëm mes personave, abonimi i të cilëve ishte ende aktiv pas një viti, dhe e raporton rezultatin për të gjithë abonentët fillestarë.",
        "abonentët që mbetën aktivë gjatë gjithë vitit dhe kishin të dhëna të lexueshme për përparimin",
        "personat që e anuluan abonimin ose llogaritë e të cilëve u bënë joaktive gjatë vitit",
        "Angazhimi në lexim mund të ndikojë në anulim. Abonentët aktivë mund të shfaqin përparim jashtëzakonisht të lartë.",
        "grupi fillestar i abonentëve të mbahet në analizë dhe përparimi të regjistrohet deri në anulim ose të ndiqen ish-abonentët",
    ),
]
