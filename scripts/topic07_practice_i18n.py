#!/usr/bin/env python3
"""Natural de-CH and informal standard-Albanian text for Topic 7 practice.

The canonical generator supplies every calculation, formula, numeric token,
task identifier, and table shape. This module supplies only localized learner
language and context labels, then checks the rendered multilingual contract.
"""

from __future__ import annotations

import math
import re
from types import ModuleType

from intro_stats_practice_support import group_heading, number, student_t_two_sided_p, task, task_id


CONTEXTS = {
    "de": [
        {
            "title": "Begleitete Übung und statistisches Denken",
            "outcome": "Punktwert im statistischen Denken",
            "outcome_unit": "Punkte",
            "x1": "Stunden begleiteter Übung",
            "x2": "Punktwert der vorherigen Vorbereitung",
            "x3": "Zahl der Reflexionssitzungen",
        },
        {
            "title": "Arbeitsablauf im Archiv und Suchzeit",
            "outcome": "Suchzeit",
            "outcome_unit": "Minuten",
            "x1": "Übungssitzungen mit Checkliste",
            "x2": "Monate Archiverfahrung",
            "x3": "Punktwert zur Katalogvertrautheit",
        },
        {
            "title": "Leseroutinen und Textverständnis",
            "outcome": "Punktwert im Textverständnis",
            "outcome_unit": "Punkte",
            "x1": "wöchentliche Lesestunden",
            "x2": "Ausgangswert des Wortschatzes",
            "x3": "Zahl der Annotationssitzungen",
        },
        {
            "title": "Streckenübung und Navigationszeit",
            "outcome": "Navigationszeit",
            "outcome_unit": "Minuten",
            "x1": "Versuche zur Streckenübung",
            "x2": "Punktwert der Streckenkenntnis",
            "x3": "Punktwert zur Erinnerung an Orientierungspunkte",
        },
        {
            "title": "Suchübung und Kataloggenauigkeit",
            "outcome": "Punktwert der Kataloggenauigkeit",
            "outcome_unit": "Punkte",
            "x1": "Suchübungsblöcke",
            "x2": "Punktwert des Katalogvorwissens",
            "x3": "Punktwert der Suchplanung",
        },
        {
            "title": "Workshopteilnahme und Selbstvertrauen",
            "outcome": "Punktwert des Selbstvertrauens",
            "outcome_unit": "Punkte",
            "x1": "Workshopsitzungen",
            "x2": "Ausgangswert des Selbstvertrauens",
            "x3": "Zahl der Reflexionsprotokolle",
        },
        {
            "title": "Konzentrationsblöcke und Aufgabengenauigkeit",
            "outcome": "Punktwert der Aufgabengenauigkeit",
            "outcome_unit": "Punkte",
            "x1": "benachrichtigungsfreie Blöcke",
            "x2": "Schlafdauer in Stunden",
            "x3": "Zahl der Planungspausen",
        },
        {
            "title": "Museumsbesuche und historisches Wissen",
            "outcome": "Punktwert des historischen Wissens",
            "outcome_unit": "Punkte",
            "x1": "Museumsbesuche",
            "x2": "Punktwert des geschichtlichen Vorwissens",
            "x3": "Zahl der Ausstellungsnotizen",
        },
        {
            "title": "Peer-Feedback und Überarbeitungsqualität",
            "outcome": "Punktwert der Überarbeitungsqualität",
            "outcome_unit": "Punkte",
            "x1": "Runden mit Peer-Feedback",
            "x2": "Ausgangswert der Schreibqualität",
            "x3": "Punktwert des Überarbeitungsplans",
        },
        {
            "title": "Planungssitzungen und Bearbeitungszeit",
            "outcome": "Bearbeitungszeit",
            "outcome_unit": "Minuten",
            "x1": "Planungssitzungen",
            "x2": "Punktwert der Aufgabenkomplexität",
            "x3": "Zahl der Fortschrittskontrollen",
        },
    ],
    "sq": [
        {
            "title": "Praktika e udhëhequr dhe arsyetimi",
            "outcome": "pikët e arsyetimit",
            "outcome_unit": "pikë",
            "x1": "orët e praktikës së udhëhequr",
            "x2": "pikët e përgatitjes paraprake",
            "x3": "numri i seancave të reflektimit",
        },
        {
            "title": "Rrjedha e punës në arkiv dhe koha e gjetjes",
            "outcome": "koha e gjetjes",
            "outcome_unit": "minuta",
            "x1": "seancat e praktikës me listë kontrolli",
            "x2": "muajt e përvojës në arkiv",
            "x3": "pikët e njohjes së katalogut",
        },
        {
            "title": "Rutinat e leximit dhe të kuptuarit",
            "outcome": "pikët e të kuptuarit",
            "outcome_unit": "pikë",
            "x1": "orët javore të leximit",
            "x2": "pikët fillestare të fjalorit",
            "x3": "numri i seancave të shënimeve",
        },
        {
            "title": "Ushtrimi i rrugës dhe koha e navigimit",
            "outcome": "koha e navigimit",
            "outcome_unit": "minuta",
            "x1": "përpjekjet për ta ushtruar rrugën",
            "x2": "pikët e njohjes së rrugës",
            "x3": "pikët e kujtimit të pikave orientuese",
        },
        {
            "title": "Praktika e kërkimit dhe saktësia në katalog",
            "outcome": "pikët e saktësisë në katalog",
            "outcome_unit": "pikë",
            "x1": "grupet e ushtrimeve të kërkimit",
            "x2": "pikët e njohurive paraprake të katalogut",
            "x3": "pikët e planifikimit të kërkimit",
        },
        {
            "title": "Pjesëmarrja në seminar dhe vetëbesimi",
            "outcome": "pikët e vetëbesimit",
            "outcome_unit": "pikë",
            "x1": "seancat e seminarit",
            "x2": "pikët fillestare të vetëbesimit",
            "x3": "numri i ditarëve të reflektimit",
        },
        {
            "title": "Blloqet e përqendrimit dhe saktësia e detyrës",
            "outcome": "pikët e saktësisë së detyrës",
            "outcome_unit": "pikë",
            "x1": "blloqet pa njoftime",
            "x2": "kohëzgjatja e gjumit në orë",
            "x3": "numri i pushimeve për planifikim",
        },
        {
            "title": "Vizitat në muze dhe njohuritë historike",
            "outcome": "pikët e njohurive historike",
            "outcome_unit": "pikë",
            "x1": "vizitat në muze",
            "x2": "pikët e njohurive paraprake të historisë",
            "x3": "numri i shënimeve për ekspozitat",
        },
        {
            "title": "Vlerësimi nga bashkëmoshatarët dhe cilësia e rishikimit",
            "outcome": "pikët e cilësisë së rishikimit",
            "outcome_unit": "pikë",
            "x1": "raundet e vlerësimit nga bashkëmoshatarët",
            "x2": "pikët fillestare të shkrimit",
            "x3": "pikët e planit të rishikimit",
        },
        {
            "title": "Seancat e planifikimit dhe koha e përfundimit",
            "outcome": "koha e përfundimit",
            "outcome_unit": "minuta",
            "x1": "seancat e planifikimit",
            "x2": "pikët e ndërlikimit të detyrës",
            "x3": "numri i kontrolleve të përparimit",
        },
    ],
}


CANDIDATE_NAMES = {
    "de": [
        ("Reflexionssitzungen", "Treffen mit Lernpartnern", "Planungskontrollen"),
        ("Katalogvertrautheit", "Nutzung eines Schreibtischplans", "Beratungen durch Mentoren"),
        ("Annotationssitzungen", "Diskussionsbeiträge", "Blöcke stillen Lesens"),
        ("Erinnerung an Orientierungspunkte", "Kartenkontrollen", "Streckenvorschauen"),
        ("Suchplanung", "Stichwortübungen", "genutzte Kataloghinweise"),
        ("Reflexionsprotokolle", "Peer-Treffen", "praktische Demonstrationen"),
        ("Planungspausen", "bildschirmfreie Zeiträume", "Aufgabenvorschauen"),
        ("Ausstellungsnotizen", "Stationen einer Führung", "weiterführende Lektüre"),
        ("Überarbeitungsplanung", "genutzte Peer-Kommentare", "Korrekturdurchgänge"),
        ("Fortschrittskontrollen", "Kalendererinnerungen", "Aufgabenvorschauen"),
    ],
    "sq": [
        ("seancat e reflektimit", "takimet me partnerin e studimit", "kontrollet e planifikimit"),
        ("njohja e katalogut", "përdorimi i hartës së tavolinës", "këshillimet nga mentori"),
        ("seancat e shënimeve", "postimet në diskutim", "blloqet e leximit në qetësi"),
        ("kujtimi i pikave orientuese", "kontrollet e hartës", "shikimet paraprake të rrugës"),
        ("planifikimi i kërkimit", "ushtrimet me fjalë kyçe", "udhëzimet e katalogut të përdorura"),
        ("ditarët e reflektimit", "takimet me bashkëmoshatarët", "demonstrimet praktike"),
        ("pushimet për planifikim", "intervalet pa ekran", "shikimet paraprake të detyrës"),
        ("shënimet për ekspozitat", "ndalesat e vizitës së udhëhequr", "leximet vijuese"),
        ("planifikimi i rishikimit", "komentet e përdorura nga bashkëmoshatarët", "kalimet e redaktimit"),
        ("kontrollet e përparimit", "përkujtuesit e kalendarit", "shikimet paraprake të detyrës"),
    ],
}


GROUP_TITLES = {
    "de": (
        "Eine Gleichung und Ausgabe der multiplen Regression lesen",
        "Eine vorab festgelegte Folge verschachtelter Modelle vergleichen",
        "Den globalen F-Test von den t-Tests der Koeffizienten unterscheiden",
        "Semipartielle Korrelation und zusätzliches R-Quadrat",
        "Vorab festgelegte Kandidatenmodelle mit AIC vergleichen",
        "Dummy-Variablen bilden und die Referenzkategorie bestimmen",
        "Ein additives Gruppenmodell interpretieren",
        "Die Referenz wechseln, ohne angepasste Beziehungen zu verändern",
        "Eine Interaktion zwischen Gruppe und quantitativem Prädiktor interpretieren",
    ),
    "sq": (
        "Leximi i ekuacionit dhe rezultatit të regresionit të shumëfishtë",
        "Krahasimi i një vargu të paracaktuar modelesh të ndërfutura",
        "Dallimi i testit global F nga testet t të koeficienteve",
        "Korrelacioni gjysmëpartial dhe rritja e R-katrorit",
        "Krahasimi i modeleve kandidate të paracaktuara me AIC",
        "Ndërtimi i treguesve dhe gjetja e kategorisë referuese",
        "Interpretimi i një modeli grupor aditiv",
        "Ndërrimi i referencës pa ndryshuar marrëdhëniet e përshtatura",
        "Interpretimi i ndërveprimit mes grupit dhe ndryshores parashikuese sasiore",
    ),
}


def _localized_cases(canonical: list[tuple], text: list[tuple[str, ...]], text_fields: int) -> list[tuple]:
    if len(canonical) != len(text):
        raise ValueError("localized Topic 7 case labels must match the canonical rows")
    return [(*labels, *case[text_fields:]) for case, labels in zip(canonical, text)]


A06_TEXT = {
    "de": [
        ("Tutorialformat", "Punktwert im statistischen Denken", ("Text", "Video", "Interaktiv")),
        ("Lernort", "Konzentrationswert", ("Zu Hause", "Bibliothek", "Lernraum", "Draussen")),
        ("Feedbackkanal", "Punktwert der Überarbeitung", ("Schriftlich", "Audio", "Video")),
        ("Methode der Notizerfassung", "Erinnerungswert", ("Papier", "Tablet", "Laptop", "Gemischt")),
        ("Workshopzeit", "Punktwert des Selbstvertrauens", ("Morgen", "Nachmittag", "Abend")),
        ("Archivhilfe", "Punktwert der Suche", ("Checkliste", "Karte", "Mentor", "Suchwerkzeug")),
        ("Überarbeitungsstrategie", "Qualitätswert", ("Selbstkontrolle", "Peer-Review", "Beurteilung durch Lehrperson")),
        ("Museumsroute", "Punktwert des Wissens", ("Chronologisch", "Thematisch", "Freie Wahl", "Geführt", "Hybrid")),
        ("Lernplan", "Punktwert des Behaltens", ("Täglich", "Zweimal wöchentlich", "Wöchentlich")),
        ("Aufgabenoberfläche", "Punktwert des Abschlusses", ("Liste", "Tafel", "Kalender", "Zeitachse")),
    ],
    "sq": [
        ("Formati i tutorialit", "pikët e arsyetimit", ("Tekst", "Video", "Ndërveprues")),
        ("Vendi i studimit", "pikët e përqendrimit", ("Shtëpi", "Bibliotekë", "Dhomë studimi", "Jashtë")),
        ("Kanali i vlerësimit", "pikët e rishikimit", ("Me shkrim", "Audio", "Video")),
        ("Mënyra e mbajtjes së shënimeve", "pikët e kujtesës", ("Letër", "Tablet", "Laptop", "E përzier")),
        ("Orari i seminarit", "pikët e vetëbesimit", ("Mëngjes", "Pasdite", "Mbrëmje")),
        ("Udhëzuesi i arkivit", "pikët e gjetjes", ("Listë kontrolli", "Hartë", "Mentor", "Mjet kërkimi")),
        ("Strategjia e rishikimit", "pikët e cilësisë", ("Vetërishikim", "Rishikim nga bashkëmoshatarët", "Rishikim nga mësimdhënësi")),
        ("Rruga në muze", "pikët e njohurive", ("Kronologjike", "Tematike", "Zgjedhje e lirë", "E udhëhequr", "Hibride")),
        ("Plani i studimit", "pikët e kujtesës", ("Çdo ditë", "Dy herë në javë", "Çdo javë")),
        ("Ndërfaqja e detyrës", "pikët e përfundimit", ("Listë", "Tabelë", "Kalendar", "Vijë kohore")),
    ],
}


A07_TEXT = {
    "de": [
        ("Lernbegleitung und statistisches Denken", "Punktwert im statistischen Denken", "Übungsstunden", "Ohne Lernbegleitung", "Mit Lernbegleitung"),
        ("Archiverfahrung und Suche", "Suchzeit", "Übungssitzungen", "Neue Mitarbeitende", "Erfahrene Mitarbeitende"),
        ("Leseformat und Textverständnis", "Punktwert im Textverständnis", "Lesestunden", "Gedruckt", "Digital"),
        ("Streckenhilfe und Navigation", "Navigationszeit", "Übungsversuche", "Papierkarte", "Karten-App"),
        ("Suchhilfe und Genauigkeit", "Punktwert der Genauigkeit", "Übungsblöcke", "Keine Hilfe", "Checkliste"),
        ("Workshopformat und Selbstvertrauen", "Punktwert des Selbstvertrauens", "besuchte Sitzungen", "Online", "Vor Ort"),
        ("Konzentrationsumgebung und Genauigkeit", "Punktwert der Aufgabengenauigkeit", "Konzentrationsblöcke", "Gemeinschaftsraum", "Ruhiger Raum"),
        ("Museumsführung und Wissen", "Punktwert des Wissens", "Besuche", "Selbstständig", "Geführt"),
        ("Feedbackformat und Überarbeitung", "Punktwert der Überarbeitung", "Feedbackrunden", "Schriftlich", "Gespräch"),
        ("Planungsformat und Abschluss", "Bearbeitungszeit", "Planungssitzungen", "Papier", "Digital"),
    ],
    "sq": [
        ("Mbështetja nga tutoriali dhe arsyetimi", "pikët e arsyetimit", "orët e praktikës", "Pa udhëheqje", "Me tutor"),
        ("Përvoja në arkiv dhe gjetja", "koha e gjetjes", "seancat e praktikës", "Staf i ri", "Staf me përvojë"),
        ("Formati i leximit dhe të kuptuarit", "pikët e të kuptuarit", "orët e leximit", "Material i shtypur", "Digjital"),
        ("Ndihma për rrugën dhe navigimi", "koha e navigimit", "përpjekjet e ushtrimit", "Hartë në letër", "Hartë në aplikacion"),
        ("Udhëzuesi i kërkimit dhe saktësia", "pikët e saktësisë", "grupet e ushtrimeve", "Pa udhëzues", "Listë kontrolli"),
        ("Mënyra e seminarit dhe vetëbesimi", "pikët e vetëbesimit", "seancat e ndjekura", "Online", "Në klasë"),
        ("Mjedisi i përqendrimit dhe saktësia", "pikët e saktësisë së detyrës", "blloqet e përqendrimit", "Dhomë e përbashkët", "Dhomë e qetë"),
        ("Udhëzuesi i muzeut dhe njohuritë", "pikët e njohurive", "vizitat", "Pa udhëheqje", "E udhëhequr"),
        ("Mënyra e vlerësimit dhe rishikimi", "pikët e rishikimit", "raundet e vlerësimit", "Me shkrim", "Bisedë"),
        ("Formati i planifikimit dhe përfundimi", "koha e përfundimit", "seancat e planifikimit", "Letër", "Digjital"),
    ],
}


A08_TEXT = {
    "de": [
        ("Übungsformat neu referenzieren", "Punktwert im statistischen Denken", "Übungsstunden", "Allein", "Zu zweit"),
        ("Archivrolle neu referenzieren", "Suchzeit", "Übungssitzungen", "Assistenz", "Koordination"),
        ("Lesemedium neu referenzieren", "Punktwert im Textverständnis", "Lesestunden", "Gedruckt", "Audio"),
        ("Navigationsanzeige neu referenzieren", "Navigationszeit", "Übungsversuche", "Statisch", "Interaktiv"),
        ("Kataloghilfe neu referenzieren", "Punktwert der Genauigkeit", "Übungsblöcke", "Index", "Suchleiste"),
        ("Workshopumgebung neu referenzieren", "Punktwert des Selbstvertrauens", "Sitzungen", "Online", "Kursraum"),
        ("Konzentrationsraum neu referenzieren", "Punktwert der Aufgabengenauigkeit", "Konzentrationsblöcke", "Offener Raum", "Privater Raum"),
        ("Museumsroute neu referenzieren", "Punktwert des Wissens", "Besuche", "Freie Route", "Zusammengestellte Route"),
        ("Überarbeitungstreffen neu referenzieren", "Punktwert der Überarbeitung", "Feedbackrunden", "Asynchron", "Live"),
        ("Planungswerkzeug neu referenzieren", "Bearbeitungszeit", "Planungssitzungen", "Notizbuch", "Kalender"),
    ],
    "sq": [
        ("Ndërrimi i referencës së formatit të praktikës", "pikët e arsyetimit", "orët e praktikës", "Në mënyrë të pavarur", "Me partner"),
        ("Ndërrimi i referencës së rolit në arkiv", "koha e gjetjes", "seancat e praktikës", "Asistent", "Koordinator"),
        ("Ndërrimi i referencës së mjetit të leximit", "pikët e të kuptuarit", "orët e leximit", "Material i shtypur", "Audio"),
        ("Ndërrimi i referencës së ekranit të navigimit", "koha e navigimit", "përpjekjet e ushtrimit", "Statik", "Ndërveprues"),
        ("Ndërrimi i referencës së ndihmës së katalogut", "pikët e saktësisë", "grupet e ushtrimeve", "Indeks", "Shirit kërkimi"),
        ("Ndërrimi i referencës së mjedisit të seminarit", "pikët e vetëbesimit", "seancat", "Online", "Klasë"),
        ("Ndërrimi i referencës së dhomës së përqendrimit", "pikët e saktësisë së detyrës", "blloqet e përqendrimit", "Dhomë e hapur", "Dhomë private"),
        ("Ndërrimi i referencës së rrugës në muze", "pikët e njohurive", "vizitat", "Rrugë e lirë", "Rrugë e përzgjedhur"),
        ("Ndërrimi i referencës së takimit për rishikim", "pikët e rishikimit", "raundet e vlerësimit", "Asinkron", "Drejtpërdrejt"),
        ("Ndërrimi i referencës së mjetit të planifikimit", "koha e përfundimit", "seancat e planifikimit", "Fletore", "Kalendar"),
    ],
}


A09_TEXT = {
    "de": [
        ("Übungsstunden nach Lernbegleitung", "Punktwert im statistischen Denken", "Übungsstunden", "Ohne Lernbegleitung", "Mit Lernbegleitung"),
        ("Übungssitzungen nach Archivrolle", "Suchzeit", "Übungssitzungen", "Neue Mitarbeitende", "Erfahrene Mitarbeitende"),
        ("Lesestunden nach Medium", "Punktwert im Textverständnis", "Lesestunden", "Gedruckt", "Audio"),
        ("Streckenübung nach Navigationsanzeige", "Navigationszeit", "Übungsversuche", "Statisch", "Interaktiv"),
        ("Übungsblöcke nach Kataloghilfe", "Punktwert der Genauigkeit", "Übungsblöcke", "Index", "Suchleiste"),
        ("Sitzungen nach Workshopumgebung", "Punktwert des Selbstvertrauens", "Sitzungen", "Online", "Kursraum"),
        ("Konzentrationsblöcke nach Raumart", "Punktwert der Aufgabengenauigkeit", "Konzentrationsblöcke", "Offener Raum", "Privater Raum"),
        ("Besuche nach Museumsroute", "Punktwert des Wissens", "Besuche", "Freie Route", "Zusammengestellte Route"),
        ("Feedbackrunden nach Sitzungsform", "Punktwert der Überarbeitung", "Feedbackrunden", "Asynchron", "Live"),
        ("Planung nach Werkzeugart", "Bearbeitungszeit", "Planungssitzungen", "Notizbuch", "Kalender"),
    ],
    "sq": [
        ("Orët e praktikës sipas mbështetjes nga tutoriali", "pikët e arsyetimit", "orët e praktikës", "Pa udhëheqje", "Me tutor"),
        ("Seancat e praktikës sipas rolit në arkiv", "koha e gjetjes", "seancat e praktikës", "Staf i ri", "Staf me përvojë"),
        ("Orët e leximit sipas mjetit", "pikët e të kuptuarit", "orët e leximit", "Material i shtypur", "Audio"),
        ("Ushtrimi sipas ekranit të navigimit", "koha e navigimit", "përpjekjet e ushtrimit", "Statik", "Ndërveprues"),
        ("Grupet e ushtrimeve sipas ndihmës së katalogut", "pikët e saktësisë", "grupet e ushtrimeve", "Indeks", "Shirit kërkimi"),
        ("Seancat sipas mjedisit të seminarit", "pikët e vetëbesimit", "seancat", "Online", "Klasë"),
        ("Blloqet e përqendrimit sipas llojit të dhomës", "pikët e saktësisë së detyrës", "blloqet e përqendrimit", "Dhomë e hapur", "Dhomë private"),
        ("Vizitat sipas rrugës në muze", "pikët e njohurive", "vizitat", "Rrugë e lirë", "Rrugë e përzgjedhur"),
        ("Raundet e vlerësimit sipas mënyrës së takimit", "pikët e rishikimit", "raundet e vlerësimit", "Asinkron", "Drejtpërdrejt"),
        ("Planifikimi sipas llojit të mjetit", "koha e përfundimit", "seancat e planifikimit", "Fletore", "Kalendar"),
    ],
}


def _decision(locale: str, p_value: float) -> str:
    rejected = p_value < 0.05
    if locale == "de":
        return (
            "wird die Nullhypothese für den Koeffizienten verworfen"
            if rejected
            else "wird die Nullhypothese für den Koeffizienten nicht verworfen"
        )
    return (
        "hipoteza zero për koeficientin hidhet poshtë"
        if rejected
        else "hipoteza zero për koeficientin nuk hidhet poshtë"
    )


def _sq_unit_after_prej(unit: str) -> str:
    """Return the Albanian unit form required after ``prej``."""

    forms = {"pikë": "pikësh", "minuta": "minutash"}
    try:
        return forms[unit]
    except KeyError as exc:
        raise ValueError(f"missing Albanian unit inflection for {unit!r}") from exc


def _render_a01(locale: str, c: ModuleType) -> tuple[str, str]:
    contexts = CONTEXTS[locale]
    exercise_group = [group_heading(1, GROUP_TITLES[locale][0])]
    solution_group = [group_heading(1, GROUP_TITLES[locale][0])]
    for variant, (context, case) in enumerate(zip(contexts, c.A01_CASES), 1):
        n, b0, b1, b2, r_y1, r_y2, r_12, rse = case
        beta1, beta2, r2, se1, se2 = c.two_predictor_output(
            n, b1, b2, r_y1, r_y2, r_12
        )
        adjusted = c.adjusted_r_squared(r2, n, 2)
        df = n - 3
        t1, t2 = b1 / se1, b2 / se2
        p1, p2 = student_t_two_sided_p(t1, df), student_t_two_sided_p(t2, df)
        if locale == "de":
            output = c.markdown_table(
                ("Term", "Schätzwert", "SE", "Standardisiert", "Bivariates r"),
                [
                    ("$X_1$", number(b1, 3), number(se1, 3), number(beta1, 3), number(r_y1, 3)),
                    ("$X_2$", number(b2, 3), number(se2, 3), number(beta2, 3), number(r_y2, 3)),
                ],
            )
            prompt = rf"""Eine konstruierte Studie umfasst {n} Fälle. Die Ergebnisvariable $Y$ trägt die Bezeichnung „{context["outcome"]}“; die zugehörige Einheit lautet „{context["outcome_unit"]}“. $X_1$ ist der Prädiktor „{context["x1"]}“ und $X_2$ ist der Prädiktor „{context["x2"]}“. Der angepasste Achsenabschnitt beträgt {number(b0, 3)}. Die ausgewählte Ausgabe lautet:

{output}

Das Modell berichtet $R^2={number(r2, 3)}$, korrigiertes $R^2={number(adjusted, 3)}$, Residualstandardfehler $={number(rse, 2)}$ {context["outcome_unit"]} und residuale Freiheitsgrade von $df={df}$.

(a) Schreibe die angepasste Gleichung auf und erkläre, wie sich ein unstandardisierter Schätzwert von einem standardisierten Koeffizienten unterscheidet. (b) Interpretiere beide unstandardisierten Steigungen bedingt. Verwende dabei die Ergebniseinheit und die Formulierung "während der andere Prädiktor festgehalten wird". (c) Berechne jede $t$-Statistik als Schätzwert geteilt durch ihren Standardfehler, bestimme die zweiseitigen $p$-Werte und entscheide bei $\alpha=.05$. (d) Interpretiere $R^2$, korrigiertes $R^2$ und den Residualstandardfehler. Erkläre danach, weshalb jeder standardisierte Koeffizient der multiplen Regression von seiner bivariaten Korrelation abweichen kann."""
            first_decision = "verworfen" if p1 < 0.05 else "nicht verworfen"
            second_decision = "verworfen" if p2 < 0.05 else "nicht verworfen"
            solution = rf"""(a) Die angepasste Gleichung lautet $\hat Y={number(b0, 3)}+({number(b1, 3)})X_1+({number(b2, 3)})X_2$. Eine unstandardisierte Steigung verwendet die ursprünglichen Messeinheiten. Ein standardisierter Koeffizient beschreibt dagegen die angepasste Veränderung in Standardabweichungen der Ergebnisvariable bei einer Zunahme des Prädiktors um eine Standardabweichung, bedingt auf den anderen Prädiktor.

(b) Wenn der Prädiktor „{context["x2"]}“ festgehalten wird, geht eine Zunahme des Prädiktors „{context["x1"]}“ um eine Einheit mit einer angepassten Veränderung der Ergebnisvariable „{context["outcome"]}“ um {number(b1, 3)} {context["outcome_unit"]} einher. Wenn der Prädiktor „{context["x1"]}“ festgehalten wird, geht eine Zunahme des Prädiktors „{context["x2"]}“ um eine Einheit mit einer angepassten Veränderung der Ergebnisvariable um {number(b2, 3)} {context["outcome_unit"]} einher. Dies sind bedingte Zusammenhänge und nicht automatisch kausale Effekte.

(c) Für $X_1$ gilt $t={number(b1, 3)}/{number(se1, 3)}={number(t1, 3)}$ mit {df} Freiheitsgraden und damit $p {c.p_text(p1)}$; folglich wird die Nullhypothese für den Koeffizienten bei $\alpha=.05$ {first_decision}. Für $X_2$ gilt $t={number(b2, 3)}/{number(se2, 3)}={number(t2, 3)}$ und damit $p {c.p_text(p2)}$; folglich wird die Nullhypothese für den Koeffizienten {second_decision}. Jeder Test betrifft diesen einen Populationskoeffizienten, bedingt auf genau den anderen Term in diesem Modell.

(d) $R^2={number(r2, 3)}$ bedeutet, dass das angepasste Modell mit zwei Prädiktoren {number(100*r2, 1)}% der Stichprobenvariation der Ergebnisvariable „{context["outcome"]}“ darstellt. Das korrigierte $R^2={number(adjusted, 3)}$ berücksichtigt innerhalb der Stichprobe, dass zwei Steigungen geschätzt wurden. Es ist kein Test an neuen Daten. Der Residualstandardfehler besagt, dass die beobachteten Ergebnisse unter dem Modell typischerweise noch ungefähr {number(rse, 2)} {context["outcome_unit"]} von ihren angepassten Werten abweichen. Die standardisierten Steigungen {number(beta1, 3)} und {number(beta2, 3)} unterscheiden sich von den bivariaten Korrelationen {number(r_y1, 3)} und {number(r_y2, 3)}, weil jede Steigung den bedingten Zusammenhang eines Prädiktors von der mit dem anderen Prädiktor geteilten Variation trennt."""
        else:
            output = c.markdown_table(
                ("Termi", "Vlerësimi", "SE", "I standardizuar", "r bivariat"),
                [
                    ("$X_1$", number(b1, 3), number(se1, 3), number(beta1, 3), number(r_y1, 3)),
                    ("$X_2$", number(b2, 3), number(se2, 3), number(beta2, 3), number(r_y2, 3)),
                ],
            )
            prompt = rf"""Një studim i ndërtuar përdor {n} raste. Ndryshorja e rezultatit $Y$ quhet «{context["outcome"]}» dhe matet me njësinë «{context["outcome_unit"]}»; $X_1$ është ndryshorja parashikuese «{context["x1"]}», ndërsa $X_2$ është ndryshorja parashikuese «{context["x2"]}». Prerja e përshtatur është {number(b0, 3)}. Rezultati i përzgjedhur është:

{output}

Modeli raporton $R^2={number(r2, 3)}$, R-katrorin e përshtatur $R^2={number(adjusted, 3)}$, gabimin standard të rezidualeve $={number(rse, 2)}$ {context["outcome_unit"]} dhe shkallët e lirisë reziduale $df={df}$.

(a) Shkruaje ekuacionin e përshtatur dhe shpjego si ndryshon një vlerësim i pastandardizuar nga një koeficient i standardizuar. (b) Interpretoji me kusht të dyja pjerrësitë e pastandardizuara. Përdor njësinë e rezultatit dhe shprehjen "duke e mbajtur të pandryshuar ndryshoren tjetër parashikuese". (c) Llogarite secilën statistikë $t$ si vlerësimi i pjesëtuar me gabimin e vet standard, gjeji vlerat e dyanshme $p$ dhe merr vendimin në $\alpha=.05$. (d) Interpreto $R^2$, $R^2$ të përshtatur dhe gabimin standard të rezidualeve. Pastaj shpjego pse secili koeficient i standardizuar i regresionit të shumëfishtë mund të ndryshojë nga korrelacioni i vet bivariat."""
            solution = rf"""(a) Ekuacioni i përshtatur është $\hat Y={number(b0, 3)}+({number(b1, 3)})X_1+({number(b2, 3)})X_2$. Një pjerrësi e pastandardizuar përdor njësitë fillestare të matjes. Një koeficient i standardizuar përshkruan ndryshimin e përshtatur në devijime standarde të rezultatit kur ndryshorja parashikuese rritet me një devijim standard, duke u kushtëzuar nga ndryshorja tjetër parashikuese.

(b) Duke e mbajtur të pandryshuar ndryshoren parashikuese «{context["x2"]}», një rritje me një njësi e ndryshores parashikuese «{context["x1"]}» lidhet me një ndryshim të përshtatur prej {number(b1, 3)} {_sq_unit_after_prej(context["outcome_unit"])} në ndryshoren e rezultatit «{context["outcome"]}». Duke e mbajtur të pandryshuar ndryshoren parashikuese «{context["x1"]}», një rritje me një njësi e ndryshores parashikuese «{context["x2"]}» lidhet me një ndryshim të përshtatur prej {number(b2, 3)} {_sq_unit_after_prej(context["outcome_unit"])}. Këto janë lidhje të kushtëzuara, jo automatikisht efekte shkakësore.

(c) Për $X_1$, $t={number(b1, 3)}/{number(se1, 3)}={number(t1, 3)}$ me {df} shkallë lirie, që jep $p {c.p_text(p1)}$; prandaj {_decision(locale, p1)} në $\alpha=.05$. Për $X_2$, $t={number(b2, 3)}/{number(se2, 3)}={number(t2, 3)}$, që jep $p {c.p_text(p2)}$; prandaj {_decision(locale, p2)}. Secili test ka të bëjë me atë koeficient të vetëm të popullatës, duke u kushtëzuar nga pikërisht termi tjetër në këtë model.

(d) $R^2={number(r2, 3)}$ do të thotë se modeli i përshtatur me dy ndryshore parashikuese paraqet {number(100*r2, 1)}% të ndryshueshmërisë në kampion të ndryshores së rezultatit «{context["outcome"]}». R-katrori i përshtatur $R^2={number(adjusted, 3)}$ vendos një dënim brenda kampionit për vlerësimin e dy pjerrësive. Nuk është test me të dhëna të reja. Gabimi standard i rezidualeve tregon se, sipas modelit, rezultatet e vëzhguara zakonisht largohen me rreth {number(rse, 2)} {context["outcome_unit"]} nga vlerat e tyre të përshtatura. Pjerrësitë e standardizuara {number(beta1, 3)} dhe {number(beta2, 3)} ndryshojnë nga korrelacionet bivariate {number(r_y1, 3)} dhe {number(r_y2, 3)}, sepse secila pjerrësi e ndan marrëdhënien e kushtëzuar të një ndryshoreje parashikuese nga ndryshueshmëria që ajo ndan me ndryshoren tjetër parashikuese."""
        exercise_group.append(task(7, 1, variant, context["title"], prompt))
        solution_group.append(task(7, 1, variant, context["title"], solution))
    return "".join(exercise_group), "".join(solution_group)


def _render_a02(locale: str, c: ModuleType) -> tuple[str, str]:
    contexts = CONTEXTS[locale]
    exercise_group = [group_heading(2, GROUP_TITLES[locale][1])]
    solution_group = [group_heading(2, GROUP_TITLES[locale][1])]
    for variant, (context, case) in enumerate(zip(contexts, c.A02_CASES), 1):
        n, sst, r1, r2, r3 = case
        r_values = (r1, r2, r3)
        adjusted = tuple(c.adjusted_r_squared(r, n, p) for p, r in enumerate(r_values, 1))
        sse = tuple(sst * (1.0 - r) for r in r_values)
        changes = (r1, r2 - r1, r3 - r2)
        change_df = 1
        error_df = n - 3 - 1
        change_f = (changes[2] / change_df) / ((1.0 - r3) / error_df)
        change_p = c.student_t_two_sided_p(math.sqrt(change_f), error_df)
        model_rows = [
            ("M1", context["x1"], "1", number(r1, 3)),
            ("M2", f'{context["x1"]}; {context["x2"]}', "2", number(r2, 3)),
            ("M3", f'{context["x1"]}; {context["x2"]}; {context["x3"]}', "3", number(r3, 3)),
        ]
        direction_de = "steigt" if adjusted[2] > adjusted[1] else "sinkt"
        direction_sq = "rritet" if adjusted[2] > adjusted[1] else "zvogëlohet"
        if locale == "de":
            prompt = rf"""Drei konstruierte Modelle, die mit der gewöhnlichen Methode der kleinsten Quadrate angepasst wurden, verwenden dieselben $n={n}$ Fälle, dieselbe Ergebnisvariable „{context["outcome"]}“ und einen Achsenabschnitt. Jedes spätere Modell enthält alle Terme des vorherigen Modells. Die gemeinsame totale Quadratsumme ist $SST={number(sst, 1)}$ und $p$ bezeichnet die Anzahl der Prädiktorkoeffizienten.

{c.markdown_table(("Modell", "Prädiktorensatz", "p", "R-Quadrat"), model_rows)}

(a) Berechne für jedes Modell die Residuenquadratsumme $SSE=SST(1-R^2)$ und nach M1 bei jedem Schritt die Veränderung in $R^2$. (b) Berechne für alle drei Modelle das korrigierte $R^2=1-(1-R^2)(n-1)/(n-p-1)$. (c) Beschreibe, was das gewöhnliche und das korrigierte $R^2$ über das Hinzufügen des Prädiktors „{context["x3"]}“ aussagen. (d) Behandle M2 als eingeschränktes und M3 als uneingeschränktes Modell. Schreibe beide Modellgleichungen auf, formuliere die Nullhypothese für den hinzugefügten Koeffizienten und berechne den inkrementellen Test $F=[(R_U^2-R_R^2)/1]/[(1-R_U^2)/(n-3-1)]$ mit 1 und {error_df} Freiheitsgraden. Bestimme den p-Wert und interpretiere die Entscheidung. (e) Erkläre, weshalb dies eine gültige verschachtelte Folge ist und weshalb weder die Anpassungstabelle noch der inkrementelle Test Kausalität oder Leistung an neuen Daten belegen."""
            solution_rows = [
                ("M1", number(sse[0], 2), "kein späterer Schritt", number(adjusted[0], 4)),
                ("M2", number(sse[1], 2), number(changes[1], 3), number(adjusted[1], 4)),
                ("M3", number(sse[2], 2), number(changes[2], 3), number(adjusted[2], 4)),
            ]
            solution = rf"""(a) Wende $SSE={number(sst, 1)}(1-R^2)$ an und subtrahiere aufeinanderfolgende $R^2$-Werte. (b) Setze für jedes Modell seine eigene Prädiktorenzahl in die korrigierte Formel ein:

{c.markdown_table(("Modell", "SSE", "Veränderung in R-Quadrat", "Korrigiertes R-Quadrat"), solution_rows)}

(c) Das gewöhnliche $R^2$ steigt von {number(r2, 3)} auf {number(r3, 3)}, wenn der Prädiktor „{context["x3"]}“ hinzugefügt wird. Der Zuwachs beträgt {number(changes[2], 3)}, also {number(100*changes[2], 1)} Prozentpunkte der Stichprobenvariation. Das gewöhnliche $R^2$ kann nicht sinken, wenn diesem Modell mit denselben Fällen und demselben Achsenabschnitt ein Prädiktor hinzugefügt wird. Das korrigierte $R^2$ {direction_de} von {number(adjusted[1], 4)} auf {number(adjusted[2], 4)}, weil es den Anpassungsgewinn gegen die zusätzlich geschätzte Steigung abwägt. Diese Korrektur ist deskriptiv und gilt innerhalb der Stichprobe.

(d) Die eingeschränkte Gleichung lautet $Y=\beta_0+\beta_1X_1+\beta_2X_2+\varepsilon$. Die uneingeschränkte Gleichung ergänzt den Prädiktor „{context["x3"]}“: $Y=\beta_0+\beta_1X_1+\beta_2X_2+\beta_3X_3+\varepsilon$. Die Nullhypothese lautet $H_0:\beta_3=0$, bedingt auf die bereits in M2 enthaltenen Terme. Die inkrementelle Statistik beträgt $F=[({number(r3,3)}-{number(r2,3)})/1]/[(1-{number(r3,3)})/({n}-3-1)]={number(change_f,4)}$ mit 1 und {error_df} Freiheitsgraden. Der p-Wert beträgt {number(change_p,4)}. Der hinzugefügte Term {'erfüllt' if change_p < 0.05 else 'erfüllt nicht'} das 5%-Kriterium.

(e) M1 ist in M2 enthalten und M2 ist in M3 enthalten: Wird jeder neu hinzugefügte Koeffizient auf null gesetzt, entsteht wieder das vorherige Modell. Die Ergebnisvariable, die Fälle und der Achsenabschnitt bleiben ebenfalls gleich. Deshalb lassen sich die Anpassungsänderungen als verschachtelte Schritte vergleichen. Die Folge randomisiert keine Prädiktoren, schliesst ausgelassene Variablen nicht aus, beweist keinen Mechanismus und misst die Vorhersage für neue Fälle nicht. Diese Fragen erfordern Angaben zum Design und eine getrennte Validierung."""
        else:
            prompt = rf"""Tri modele të ndërtuara, të përshtatura me metodën e zakonshme të katrorëve më të vegjël, përdorin të njëjtat $n={n}$ raste, të njëjtën ndryshore rezultati «{context["outcome"]}» dhe një prerje. Secili model vijues i përmban të gjithë termat e modelit të mëparshëm. Shuma totale e përbashkët e katrorëve është $SST={number(sst, 1)}$, ndërsa $p$ shënon numrin e koeficienteve parashikues.

{c.markdown_table(("Modeli", "Grupi i ndryshoreve parashikuese", "p", "R-katrori"), model_rows)}

(a) Llogarite shumën e katrorëve të rezidualeve $SSE=SST(1-R^2)$ për secilin model dhe ndryshimin në $R^2$ në secilin hap pas M1. (b) Llogarite vlerën e përshtatur $R^2=1-(1-R^2)(n-1)/(n-p-1)$ për të tria modelet. (c) Përshkruaj çfarë tregojnë $R^2$ i zakonshëm dhe ai i përshtatur për shtimin e ndryshores parashikuese «{context["x3"]}». (d) Trajtoje M2 si modelin e kufizuar dhe M3 si modelin e pakufizuar. Shkruaji të dy ekuacionet e modeleve, formuloje hipotezën zero për koeficientin e shtuar dhe llogarite testin e rritjes $F=[(R_U^2-R_R^2)/1]/[(1-R_U^2)/(n-3-1)]$ me 1 dhe {error_df} shkallë lirie. Gjeje vlerën p dhe interpretoje vendimin. (e) Shpjego pse ky është një varg i vlefshëm modelesh të ndërfutura dhe pse as tabela e përshtatjes, as testi i rritjes nuk vërteton shkakësi ose performancë me të dhëna të reja."""
            solution_rows = [
                ("M1", number(sse[0], 2), "nuk është hap vijues", number(adjusted[0], 4)),
                ("M2", number(sse[1], 2), number(changes[1], 3), number(adjusted[1], 4)),
                ("M3", number(sse[2], 2), number(changes[2], 3), number(adjusted[2], 4)),
            ]
            solution = rf"""(a) Zbato $SSE={number(sst, 1)}(1-R^2)$ dhe zbrit vlerat e njëpasnjëshme të $R^2$. (b) Zëvendësoje numrin e ndryshoreve parashikuese të secilit model në formulën e përshtatur:

{c.markdown_table(("Modeli", "SSE", "Ndryshimi në R-katror", "R-katrori i përshtatur"), solution_rows)}

(c) $R^2$ i zakonshëm rritet nga {number(r2, 3)} në {number(r3, 3)} kur shtohet ndryshorja parashikuese «{context["x3"]}». Rritja është {number(changes[2], 3)}, ose {number(100*changes[2], 1)} pikë përqindjeje të ndryshueshmërisë në kampion. $R^2$ i zakonshëm nuk mund të zvogëlohet kur këtij modeli me të njëjtat raste dhe të njëjtën prerje i shtohet një ndryshore parashikuese. $R^2$ i përshtatur {direction_sq} nga {number(adjusted[1], 4)} në {number(adjusted[2], 4)}, sepse e peshon përshtatjen shtesë kundrejt pjerrësisë shtesë të vlerësuar. Kjo masë e përshtatur është përshkruese dhe vlen vetëm brenda kampionit.

(d) Ekuacioni i kufizuar është $Y=\beta_0+\beta_1X_1+\beta_2X_2+\varepsilon$. Ekuacioni i pakufizuar shton ndryshoren parashikuese «{context["x3"]}»: $Y=\beta_0+\beta_1X_1+\beta_2X_2+\beta_3X_3+\varepsilon$. Hipoteza zero është $H_0:\beta_3=0$, duke u kushtëzuar nga termat që gjenden tashmë në M2. Statistika e rritjes është $F=[({number(r3,3)}-{number(r2,3)})/1]/[(1-{number(r3,3)})/({n}-3-1)]={number(change_f,4)}$ me 1 dhe {error_df} shkallë lirie. Vlera p është {number(change_p,4)}, prandaj termi i shtuar {'e plotëson' if change_p < 0.05 else 'nuk e plotëson'} kriterin 5%.

(e) M1 përfshihet në M2 dhe M2 përfshihet në M3: vendosja në zero e secilit koeficient të saposhtuar e rikrijon modelin e mëparshëm. Edhe ndryshorja e rezultatit, rastet dhe prerja mbeten të njëjta, prandaj ndryshimet e përshtatjes mund të krahasohen si hapa të ndërfutur. Ky varg nuk i cakton rastësisht ndryshoret parashikuese, nuk i përjashton ndryshoret e lëna jashtë, nuk vërteton mekanizëm dhe nuk mat parashikimin për raste të reja. Këto pyetje kërkojnë informacion për dizajnin dhe vlerësim të veçantë."""
        exercise_group.append(task(7, 2, variant, context["title"], prompt))
        solution_group.append(task(7, 2, variant, context["title"], solution))
    return "".join(exercise_group), "".join(solution_group)


def _render_a03(locale: str, c: ModuleType) -> tuple[str, str]:
    contexts = CONTEXTS[locale]
    names_by_context = CANDIDATE_NAMES[locale]
    exercise_group = [group_heading(3, GROUP_TITLES[locale][2])]
    solution_group = [group_heading(3, GROUP_TITLES[locale][2])]
    for variant, (context, case, candidate_names) in enumerate(zip(contexts, c.A03_CASES, names_by_context), 1):
        n, r2, critical, coefficients = case
        names = (context["x1"], context["x2"], candidate_names[0])
        df2 = n - 4
        f_value = c.global_f(r2, n, 3)
        coefficient_rows = [
            (name, number(estimate, 3), number(se, 3))
            for name, (estimate, se) in zip(names, coefficients)
        ]
        significant_count = sum(
            student_t_two_sided_p(estimate / se, df2) < 0.05
            for estimate, se in coefficients
        )
        if locale == "de":
            prompt = rf"""Ein konstruiertes Modell mit drei Prädiktoren für die Ergebnisvariable „{context["outcome"]}“ verwendet $n={n}$ und berichtet $R^2={number(r2, 3)}$. $\beta_1$, $\beta_2$ und $\beta_3$ bezeichnen die drei Populationssteigungen. Für $\alpha=.05$ ist der vorgegebene kritische Wert $F_{{3,{df2}}}={number(critical, 5)}$. Die Koeffiziententabelle lautet:

{c.markdown_table(("Prädiktor", "Schätzwert", "SE"), coefficient_rows)}

(a) Formuliere die globale Nullhypothese, berechne $F=(R^2/3)/[(1-R^2)/(n-3-1)]$ und triff die globale Entscheidung. (b) Berechne für jeden Prädiktor $t=b/SE$, den zweiseitigen $p$-Wert mit {df2} residualen Freiheitsgraden und die Entscheidung bei $\alpha=.05$. (c) Formuliere die Nullhypothese für einen einzelnen Koeffizienten und erkläre, weshalb ein globales Ergebnis nicht zeigt, welche Steigung von null abweicht. (d) Bringe die globalen und individuellen Entscheidungen dieses Modells miteinander in Einklang, ohne eine der beiden Testarten als Beleg für Wichtigkeit, Vorhersage oder Kausalität zu behandeln."""
            details = []
            for name, (estimate, se) in zip(names, coefficients):
                t_value = estimate / se
                p_value = student_t_two_sided_p(t_value, df2)
                details.append(
                    f"{name}: $t={number(estimate, 3)}/{number(se, 3)}={number(t_value, 3)}$, "
                    f"$p {c.p_text(p_value)}$, somit {_decision(locale, p_value)}"
                )
            global_decision = "verworfen" if f_value > critical else "nicht verworfen"
            comparison = "grösser als" if f_value > critical else "nicht grösser als"
            solution = rf"""(a) Die globale Nullhypothese lautet $H_0:\beta_1=\beta_2=\beta_3=0$. Die Statistik ist $F=({number(r2, 3)}/3)/[(1-{number(r2, 3)})/{df2}]={number(f_value, 3)}$. Weil {number(f_value, 3)} {comparison} {number(critical, 5)} ist, wird die globale Nullhypothese bei $\alpha=.05$ {global_decision}.

(b) Die Berechnungen für die Koeffizienten lauten: {"; ".join(details)}. In {significant_count} von drei gezeigten Tests wird die individuelle Nullhypothese auf dem angegebenen Niveau verworfen.

(c) Für Prädiktor $X_j$ lautet die individuelle Nullhypothese $H_0:\beta_j=0$, bedingt auf jeden anderen Term in genau diesem Modell. Der globale Test stellt eine gemeinsame Frage zu allen drei Steigungen. Wird die globale Nullhypothese verworfen, unterscheidet sich unter dem Modell mindestens eine Populationssteigung ausser dem Achsenabschnitt von null. Die globale Statistik nennt jedoch keinen Prädiktor. Wird sie nicht verworfen, beweist dies umgekehrt nicht, dass jede Populationssteigung null ist.

(d) Die beiden Entscheidungsarten können sich unterscheiden, weil der globale Test die Prädiktoren gemeinsam beurteilt, während jeder $t$-Test einen einzelnen bedingten Koeffizienten und seine Unsicherheit isoliert. Geteilte Prädiktorvariation kann individuelle Standardfehler vergrössern, obwohl der Prädiktorensatz gemeinsam Erklärungswert besitzt. Umgekehrt kann Stichprobenvariation in einem Modell, dessen globaler Test nicht verworfen wird, zu einem kleinen individuellen p-Wert führen. Ein p-Wert misst weder Effektgrösse noch praktische Bedeutung, künftige Vorhersage oder Kausalität."""
        else:
            prompt = rf"""Një model i ndërtuar me tri ndryshore parashikuese për ndryshoren e rezultatit «{context["outcome"]}» përdor $n={n}$ dhe raporton $R^2={number(r2, 3)}$. Le të shënojnë $\beta_1$, $\beta_2$ dhe $\beta_3$ tri pjerrësitë e popullatës. Për $\alpha=.05$, vlera kritike e dhënë është $F_{{3,{df2}}}={number(critical, 5)}$. Tabela e koeficienteve është:

{c.markdown_table(("Ndryshorja parashikuese", "Vlerësimi", "SE"), coefficient_rows)}

(a) Shënoje hipotezën zero globale, llogarite $F=(R^2/3)/[(1-R^2)/(n-3-1)]$ dhe merr vendimin global. (b) Për secilën ndryshore parashikuese, llogarite $t=b/SE$, vlerën e saj të dyanshme $p$ me {df2} shkallë lirie reziduale dhe vendimin në $\alpha=.05$. (c) Shënoje hipotezën zero për koeficientin individual dhe shpjego pse rezultati global nuk tregon se cila pjerrësi ndryshon nga zeroja. (d) Pajtoji vendimet globale dhe individuale të këtij modeli pa e trajtuar asnjërin lloj testi si provë për rëndësi, parashikim ose shkakësi."""
            details = []
            for name, (estimate, se) in zip(names, coefficients):
                t_value = estimate / se
                p_value = student_t_two_sided_p(t_value, df2)
                details.append(
                    f"{name}: $t={number(estimate, 3)}/{number(se, 3)}={number(t_value, 3)}$, "
                    f"$p {c.p_text(p_value)}$, prandaj {_decision(locale, p_value)}"
                )
            global_decision = (
                "hipoteza zero globale hidhet poshtë"
                if f_value > critical
                else "hipoteza zero globale nuk hidhet poshtë"
            )
            comparison = "më e madhe se" if f_value > critical else "jo më e madhe se"
            solution = rf"""(a) Hipoteza zero globale është $H_0:\beta_1=\beta_2=\beta_3=0$. Statistika është $F=({number(r2, 3)}/3)/[(1-{number(r2, 3)})/{df2}]={number(f_value, 3)}$. Meqë {number(f_value, 3)} është {comparison} {number(critical, 5)}, {global_decision} në $\alpha=.05$.

(b) Llogaritjet e koeficienteve janë: {"; ".join(details)}. Në {significant_count} nga tri testet e paraqitura, hipoteza zero individuale hidhet poshtë në nivelin e shënuar.

(c) Për ndryshoren parashikuese $X_j$, hipoteza zero individuale është $H_0:\beta_j=0$, duke u kushtëzuar nga çdo term tjetër pikërisht në këtë model. Testi global bën një pyetje të përbashkët për të tria pjerrësitë. Hedhja poshtë e saj tregon se, sipas modelit, të paktën një pjerrësi e popullatës përveç prerjes ndryshon nga zeroja, por statistika globale nuk e emërton ndryshoren parashikuese. Moshedhja poshtë nuk është provë se çdo pjerrësi e popullatës është zero.

(d) Dy llojet e vendimeve mund të ndryshojnë sepse testi global i vlerëson ndryshoret parashikuese së bashku, ndërsa secili test $t$ izolon një koeficient të kushtëzuar dhe pasigurinë e tij. Ndryshueshmëria e përbashkët e ndryshoreve parashikuese mund t'i zmadhojë gabimet standarde individuale edhe kur grupi parashikues ka vlerë shpjeguese së bashku. Anasjelltas, ndryshueshmëria e kampionit mund të japë një vlerë të vogël individuale p në një model, testi global i të cilit nuk hidhet poshtë. Vlera p nuk mat madhësinë e efektit, vlerën praktike, parashikimin e ardhshëm ose shkakësinë."""
        exercise_group.append(task(7, 3, variant, context["title"], prompt))
        solution_group.append(task(7, 3, variant, context["title"], solution))
    return "".join(exercise_group), "".join(solution_group)


def _render_a04(locale: str, c: ModuleType) -> tuple[str, str]:
    contexts = CONTEXTS[locale]
    names_by_context = CANDIDATE_NAMES[locale]
    exercise_group = [group_heading(4, GROUP_TITLES[locale][3])]
    solution_group = [group_heading(4, GROUP_TITLES[locale][3])]
    for variant, (context, case, names) in enumerate(zip(contexts, c.A04_CASES, names_by_context), 1):
        base_r2, semipartials = case
        candidate_rows = [
            (name, number(value, 3)) for name, value in zip(names, semipartials)
        ]
        increments = tuple(value * value for value in semipartials)
        new_r2 = tuple(base_r2 + increment for increment in increments)
        winner = max(range(3), key=lambda index: increments[index])
        if locale == "de":
            prompt = rf"""Ein konstruiertes aktuelles Modell für die Ergebnisvariable „{context["outcome"]}“ enthält bereits die Prädiktoren „{context["x1"]}“ und „{context["x2"]}“. Es weist $R^2={number(base_r2, 3)}$ auf. Jeder unten aufgeführte Kandidat wurde separat auf diese aktuellen Prädiktoren regressiert. Das Residuum aus dieser Regression ist der Anteil des Kandidaten, der durch den aktuellen Satz nicht linear vorhergesagt wird. Die Tabelle berichtet die Korrelation zwischen diesem residualisierten Kandidaten und der ursprünglichen, nicht residualisierten Ergebnisvariable. Das Symbol $r_{{sp}}$ bezeichnet diese semipartielle Korrelation:

{c.markdown_table(("Kandidat", "Semipartielles r"), candidate_rows)}

(a) Erkläre, weshalb dies eine semipartielle und keine partielle Korrelation ist. (b) Berechne für jede einzelne Kandidatenaufnahme $\Delta R^2=r_{{sp}}^2$ und das daraus entstehende $R^2$. (c) Bestimme den gewählten Kandidaten und seinen Zuwachs, wenn ein Vorwärtsschritt den grössten Zuwachs verwendet. (d) Erkläre, was dieser Schritt rechtfertigt und was nicht. Begründe insbesondere, weshalb er weder beweist, dass die gewählte Variable wahr oder kausal ist, noch garantiert, dass sie nach Aufnahme eines weiteren Terms die beste bleibt."""
            result_rows = [
                (name, number(value, 3), number(increment, 4), number(result, 4))
                for name, value, increment, result in zip(names, semipartials, increments, new_r2)
            ]
            solution = rf"""(a) Jeder Kandidat wird um die aktuellen Prädiktoren residualisiert, während die Ergebnisvariable in ihrer ursprünglichen Form bleibt. Diese einseitige Residualisierung definiert eine semipartielle Korrelation. Bei einer partiellen Korrelation würden sowohl der Kandidat als auch die Ergebnisvariable um den aktuellen Prädiktorensatz residualisiert.

(b) Das Quadrieren jeder semipartiellen Korrelation ergibt den Zuwachs durch einen Prädiktor:

{c.markdown_table(("Kandidat", "Semipartielles r", "Zuwachs in R-Quadrat", "Neues R-Quadrat"), result_rows)}

(c) Die grösste quadrierte semipartielle Korrelation beträgt {number(increments[winner], 4)} und gehört zu {names[winner]}. Eine Vorwärtsregel, die nur auf den gezeigten Kandidaten beruht, würde diesen Prädiktor zuerst aufnehmen und das Stichproben-$R^2$ von {number(base_r2, 3)} auf {number(new_r2[winner], 4)} erhöhen.

(d) Der Schritt ordnet diese drei Kandidaten danach, wie viel zusätzliche Stichprobenvariation jeder nach den aktuellen Prädiktoren erklärt. Durch das Quadrieren verschwindet das Vorzeichen. Das Vorzeichen von $r_{{sp}}$ bleibt jedoch für die Richtung des Zusammenhangs wichtig, auch wenn es $\Delta R^2$ nicht beeinflusst. Die Rangfolge gilt bedingt auf das gegenwärtige Modell, die Kandidaten und die Stichprobe. Nach Aufnahme eines weiteren Prädiktors verändert die geteilte Variation, was in jedem anderen Kandidaten übrig bleibt. Die Auswahl beweist weder Wahrheit noch kausale Wirkung, inhaltliche Bedeutung oder Leistung an neuen Daten."""
        else:
            prompt = rf"""Një model aktual i ndërtuar për ndryshoren e rezultatit «{context["outcome"]}» tashmë përmban ndryshoret parashikuese «{context["x1"]}» dhe «{context["x2"]}». Ai ka $R^2={number(base_r2, 3)}$. Secila ndryshore kandidate më poshtë është regresuar veçmas mbi këto ndryshore parashikuese aktuale. Reziduali nga ai regresion është pjesa e ndryshores kandidate që nuk parashikohet në mënyrë lineare nga grupi aktual. Tabela raporton korrelacionin mes asaj ndryshoreje kandidate të kthyer në rezidual dhe rezultatit fillestar, jo të kthyer në rezidual. Simboli $r_{{sp}}$ shënon këtë korrelacion gjysmëpartial:

{c.markdown_table(("Ndryshorja kandidate", "r gjysmëpartial"), candidate_rows)}

(a) Shpjego pse ky është korrelacion gjysmëpartial dhe jo korrelacion i pjesshëm. (b) Për secilën shtesë me një ndryshore kandidate, llogarite $\Delta R^2=r_{{sp}}^2$ dhe $R^2$ që rezulton. (c) Nëse një hap përpara përdor rritjen më të madhe, gjeje ndryshoren kandidate të zgjedhur dhe përcaktoje rritjen e saj. (d) Shpjego çfarë arsyeton dhe çfarë nuk arsyeton ky hap, duke përfshirë pse ai as nuk vërteton se ndryshorja e zgjedhur është e vërtetë ose shkakësore, as nuk garanton se do të mbetet më e mira pasi të hyjë një term tjetër."""
            result_rows = [
                (name, number(value, 3), number(increment, 4), number(result, 4))
                for name, value, increment, result in zip(names, semipartials, increments, new_r2)
            ]
            solution = rf"""(a) Secila ndryshore kandidate kthehet në rezidual kundrejt ndryshoreve parashikuese aktuale, por rezultati mbetet në formën e tij fillestare. Ky kthim në rezidual vetëm nga njëra anë përkufizon korrelacionin gjysmëpartial. Korrelacioni i pjesshëm do t'i kthente në reziduale si ndryshoren kandidate, ashtu edhe rezultatin kundrejt grupit aktual të ndryshoreve parashikuese.

(b) Katrori i secilit korrelacion gjysmëpartial jep rritjen nga një ndryshore parashikuese:

{c.markdown_table(("Ndryshorja kandidate", "r gjysmëpartial", "Rritja në R-katror", "R-katrori i ri"), result_rows)}

(c) Korrelacioni gjysmëpartial më i madh në katror është {number(increments[winner], 4)}, për {names[winner]}. Një rregull përpara i bazuar vetëm në ndryshoret kandidate të paraqitura do ta shtonte së pari atë ndryshore parashikuese, duke e rritur $R^2$ e kampionit nga {number(base_r2, 3)} në {number(new_r2[winner], 4)}.

(d) Hapi i rendit këto tri ndryshore kandidate sipas ndryshueshmërisë shtesë në kampion që shpjegon secila pas ndryshoreve parashikuese aktuale. Katrori e heq shenjën, prandaj shenja e $r_{{sp}}$ mbetet e rëndësishme për drejtimin e lidhjes edhe pse nuk ndikon në $\Delta R^2$. Renditja kushtëzohet nga modeli, ndryshoret kandidate dhe kampioni aktual. Pasi hyn një ndryshore tjetër parashikuese, ndryshueshmëria e përbashkët e ndryshon atë që mbetet në secilën ndryshore tjetër kandidate. Përzgjedhja nuk vërteton të vërtetën, efektin shkakësor, rëndësinë përmbajtësore ose performancën me të dhëna të reja."""
        exercise_group.append(task(7, 4, variant, context["title"], prompt))
        solution_group.append(task(7, 4, variant, context["title"], solution))
    return "".join(exercise_group), "".join(solution_group)


def _render_a05(locale: str, c: ModuleType) -> tuple[str, str]:
    contexts = CONTEXTS[locale]
    exercise_group = [group_heading(5, GROUP_TITLES[locale][4])]
    solution_group = [group_heading(5, GROUP_TITLES[locale][4])]
    k_values = (3, 4, 5, 6)
    for variant, (context, log_likelihoods) in enumerate(zip(contexts, c.A05_CASES), 1):
        product_term = "ein vorab festgelegter Produktterm" if locale == "de" else "një term prodhimi i paracaktuar"
        formulas = (
            context["x1"],
            f'{context["x1"]} + {context["x2"]}',
            f'{context["x1"]} + {context["x2"]} + {context["x3"]}',
            f'{context["x1"]} + {context["x2"]} + {context["x3"]} + {product_term}',
        )
        input_rows = [
            (f"M{index}", formula, k, number(ll, 1))
            for index, (formula, k, ll) in enumerate(zip(formulas, k_values, log_likelihoods), 1)
        ]
        aics = tuple(-2.0 * ll + 2.0 * k for ll, k in zip(log_likelihoods, k_values))
        minimum = min(aics)
        deltas = tuple(aic - minimum for aic in aics)
        winner = aics.index(minimum)
        forward_rows_de = [
            ("Schritt 1", f'{context["x2"]} hinzufügen', number(aics[1], 2)),
            ("Schritt 1", f'{context["x3"]} hinzufügen', number(aics[1] + 3.20, 2)),
            ("Schritt 1", "Produktterm hinzufügen", number(aics[1] + 6.40, 2)),
            ("Schritt 2", "nach M2 stoppen", number(aics[1], 2)),
            ("Schritt 2", f'{context["x3"]} hinzufügen', number(aics[2], 2)),
            ("Schritt 2", "Produktterm hinzufügen", number(aics[2] + 2.80, 2)),
            ("Schritt 3", "nach M3 stoppen", number(aics[2], 2)),
            ("Schritt 3", "Produktterm hinzufügen", number(aics[3], 2)),
        ]
        forward_rows_sq = [
            ("Hapi 1", f'shto «{context["x2"]}»', number(aics[1], 2)),
            ("Hapi 1", f'shto «{context["x3"]}»', number(aics[1] + 3.20, 2)),
            ("Hapi 1", "shto termin e prodhimit", number(aics[1] + 6.40, 2)),
            ("Hapi 2", "ndalo pas M2", number(aics[1], 2)),
            ("Hapi 2", f'shto «{context["x3"]}»', number(aics[2], 2)),
            ("Hapi 2", "shto termin e prodhimit", number(aics[2] + 2.80, 2)),
            ("Hapi 3", "ndalo pas M3", number(aics[2], 2)),
            ("Hapi 3", "shto termin e prodhimit", number(aics[3], 2)),
        ]
        selected_models = [0, 1]
        if aics[2] < aics[1]:
            selected_models.append(2)
            if aics[3] < aics[2]:
                selected_models.append(3)
        final_index = selected_models[-1]
        path_coordinates = ", ".join(
            f"({step}, {number(aics[model],2)})"
            for step, model in enumerate(selected_models)
        )
        final_terms = formulas[final_index]
        result_rows = [
            (f"M{index}", number(aic, 2), number(delta, 2))
            for index, (aic, delta) in enumerate(zip(aics, deltas), 1)
        ]
        ranking = ", ".join(
            f"M{index + 1}" for index in sorted(range(4), key=lambda item: aics[item])
        )
        if locale == "de":
            prompt = rf"""Vier konstruierte, vorab festgelegte Kandidatenmodelle verwenden genau dieselben Fälle und dieselbe Ergebnisvariable „{context["outcome"]}“. Hier ist $\log(L)$ die vom angepassten Modell berichtete maximierte Log-Likelihood. Nach der angegebenen Konvention zählt $K$ alle geschätzten Parameter, die in die AIC-Berechnung eingehen.

{c.markdown_table(("Modell", "Terme", "K", "Log-Likelihood"), input_rows)}

(a) Berechne für jedes Modell $AIC=-2\log(L)+2K$ und berechne jedes $\Delta AIC=AIC-AIC_{{min}}$. (b) Führe ausgehend von M1 eine Vorwärtsselektion mit der schrittspezifischen Kandidatentabelle durch. Wähle in jedem Schritt den kleinsten verfügbaren AIC nur dann, wenn er kleiner als beim aktuellen Modell ist. Stoppe andernfalls.

{c.markdown_table(("Vorwärtsschritt", "Mögliche Aktion", "AIC"), forward_rows_de)}

(c) Zeichne den AIC-Pfad der tatsächlich ausgewählten Modelle. Beginne mit M1 bei Schritt 0. (d) Schreibe die endgültige Modellformel auf und interpretiere, was die ausgewählten Terme zum angepassten Zusammenhang beitragen. (e) Erkläre, weshalb der Pfad von früheren Entscheidungen abhängt und weshalb das endgültige Modell dadurch weder als wahr oder kausal bewiesen ist noch nachweislich ausserhalb der Stichprobe vorhersagt."""
            solution = rf"""(a) Für M1 ergibt sich zum Beispiel $-2({number(log_likelihoods[0], 1)})+2({k_values[0]})={number(aics[0], 2)}$. Dieselbe Regel ergibt für alle vier Modelle:

{c.markdown_table(("Modell", "AIC", "Delta AIC"), result_rows)}

(b) In Schritt 1 wird M2 ausgewählt, weil {number(aics[1],2)} kleiner als die anderen angezeigten Werte von Schritt 1 und kleiner als der Wert {number(aics[0],2)} von M1 ist. {'In Schritt 2 wird M3 ausgewählt, weil sein AIC kleiner als der aktuelle Wert von M2 ist.' if 2 in selected_models else 'In Schritt 2 wird gestoppt, weil keine Ergänzung einen AIC unter dem aktuellen Wert von M2 besitzt.'} {'In Schritt 3 wird danach M4 ausgewählt, weil sein AIC unter demjenigen von M3 liegt.' if 3 in selected_models else 'Auf diesem Vorwärtspfad wird später kein Produktterm ausgewählt.'}

(c) Die Koordinaten des ausgewählten Pfads lauten {path_coordinates}. Trage den Schritt auf der horizontalen Achse und den AIC auf der vertikalen Achse ab. Verbinde nur aufeinanderfolgende ausgewählte Modelle und ende dort, wo die Regel stoppt. Die fallenden Abschnitte zeigen Verbesserungen des relativen Gleichgewichts zwischen Anpassung und Komplexität entlang dieses bestimmten Pfads.

(d) Die endgültige ausgewählte Formel lautet `{context["outcome"]} ~ {final_terms}`. Ihre Terme beschreiben bedingte angepasste Zusammenhänge für diese Ergebnisvariable und diese Fälle. Sie identifizieren für sich allein keine Ursachen.

(e) Bei einem Vorwärtspfad wird die Wahl nach jedem ausgewählten Term neu berechnet. Eine Ergänzung, die in einem Schritt nützlich erscheint, kann deshalb in einem späteren Schritt redundant werden. Der Pfad kann zudem stoppen, bevor er den global kleinsten AIC unter Kombinationen erreicht, die durch seine früheren Entscheidungen nie verfügbar wurden. AIC belohnt Anpassung und fügt eine Komplexitätsstrafe hinzu. Das Kriterium belegt weder, dass ein ausgewähltes Modell die Wahrheit der Datenerzeugung darstellt, noch dass seine Vorhersagen generalisieren. Die Leistung an neuen Daten erfordert eine getrennte Validierung. AIC-Werte für unterschiedliche Ergebnisvariablen oder Fallmengen gehören nicht zu einer gemeinsam vergleichbaren Kandidatenfamilie."""
        else:
            prompt = rf"""Katër modele kandidate të ndërtuara dhe të paracaktuara përdorin pikërisht të njëjtat raste dhe të njëjtën ndryshore rezultati «{context["outcome"]}». Këtu $\log(L)$ është log-likelihood-u i maksimizuar që raporton modeli i përshtatur. Sipas marrëveshjes së shënuar, $K$ numëron të gjithë parametrat e vlerësuar që përdoren në llogaritjen e AIC-së.

{c.markdown_table(("Modeli", "Termat", "K", "Log-likelihood-u"), input_rows)}

(a) Llogarite $AIC=-2\log(L)+2K$ për secilin model dhe llogarite secilën $\Delta AIC=AIC-AIC_{{min}}$. (b) Duke nisur nga M1, kryeje përzgjedhjen përpara me tabelën e kandidatëve për secilin hap. Në çdo hap zgjidhe AIC-në më të ulët të disponueshme vetëm nëse është më e ulët se AIC-ja e modelit aktual. Përndryshe, ndalo.

{c.markdown_table(("Hapi përpara", "Veprimi i mundshëm", "AIC"), forward_rows_sq)}

(c) Vizatoje rrugën e AIC-së për modelet që u përzgjodhën vërtet, duke nisur me M1 në hapin 0. (d) Shkruaje formulën e modelit përfundimtar dhe interpreto çfarë u shtojnë termat e përzgjedhur lidhjeve të përshtatura. (e) Shpjego pse rruga varet nga zgjedhjet e mëparshme dhe pse modeli përfundimtar nuk vërtetohet në këtë mënyrë si i vërtetë, shkakësor ose parashikues jashtë kampionit."""
            solution = rf"""(a) Për shembull, M1 jep $-2({number(log_likelihoods[0], 1)})+2({k_values[0]})={number(aics[0], 2)}$. Zbatimi i të njëjtit rregull për të katër modelet jep:

{c.markdown_table(("Modeli", "AIC", "Delta AIC"), result_rows)}

(b) Në hapin 1 përzgjidhet M2, sepse {number(aics[1],2)} është më e ulët se vlerat e tjera të paraqitura në hapin 1 dhe më e ulët se vlera {number(aics[0],2)} e M1. {'Në hapin 2 përzgjidhet M3, sepse AIC-ja e tij është më e ulët se vlera aktuale e M2.' if 2 in selected_models else 'Në hapin 2 ndalohet, sepse asnjë shtesë nuk ka AIC më të ulët se vlera aktuale e M2.'} {'Më pas, në hapin 3 përzgjidhet M4, sepse AIC-ja e tij është më e ulët se ajo e M3.' if 3 in selected_models else 'Në këtë rrugë përpara nuk përzgjidhet më vonë asnjë term prodhimi.'}

(c) Koordinatat e rrugës së përzgjedhur janë {path_coordinates}. Vendose hapin në boshtin horizontal dhe AIC-në në boshtin vertikal. Lidhi vetëm modelet e njëpasnjëshme që u përzgjodhën dhe përfundo aty ku ndalon rregulli. Segmentet zbritëse tregojnë përmirësime të baraspeshës relative mes përshtatjes dhe ndërlikimit përgjatë pikërisht kësaj rruge.

(d) Formula përfundimtare e përzgjedhur është `{context["outcome"]} ~ {final_terms}`. Termat e saj përshkruajnë lidhje të kushtëzuara të përshtatura për këtë ndryshore rezultati dhe këto raste. Vetëm ata nuk përcaktojnë shkaqe.

(e) Në një rrugë përpara, zgjedhja rillogaritet pas çdo termi të përzgjedhur. Prandaj, një shtesë që duket e dobishme në një hap mund të bëhet e tepërt në një hap të mëvonshëm. Rruga mund të ndalojë edhe para se të arrijë AIC-në më të ulët në tërësi mes kombinimeve që zgjedhjet e mëparshme nuk i bënë kurrë të arritshme. AIC-ja shpërblen përshtatjen, por shton një dënim për ndërlikimin. Nuk vërteton se modeli i përzgjedhur është e vërteta që ka prodhuar të dhënat ose se parashikimet e tij do të përgjithësohen. Performanca me të dhëna të reja kërkon vlerësim të veçantë. Vlerat AIC për ndryshore të ndryshme rezultati ose grupe të ndryshme rastesh nuk përbëjnë një familje të përbashkët modelesh kandidate për krahasim."""
        exercise_group.append(task(7, 5, variant, context["title"], prompt))
        solution_group.append(task(7, 5, variant, context["title"], solution))
    return "".join(exercise_group), "".join(solution_group)


def _render_a06(locale: str, c: ModuleType) -> tuple[str, str]:
    cases = _localized_cases(c.A06_CASES, A06_TEXT[locale], 3)
    exercise_group = [group_heading(6, GROUP_TITLES[locale][5])]
    solution_group = [group_heading(6, GROUP_TITLES[locale][5])]
    for variant, (setting, outcome, categories, b0, effects) in enumerate(cases, 1):
        k = len(categories)
        reference = categories[0]
        formula_terms = " ".join(
            f"{'+' if effect >= 0 else '-'} {number(abs(effect), 2)}D_{index}"
            for index, effect in enumerate(effects, 1)
        )
        coding_rows = []
        fitted_rows = []
        for category_index, category in enumerate(categories):
            codes = tuple(int(category_index == indicator_index) for indicator_index in range(1, k))
            coding_rows.append((category, *codes))
            fit_value = b0 if category_index == 0 else b0 + effects[category_index - 1]
            fitted_rows.append((category, number(fit_value, 2)))
        if locale == "de":
            prompt = rf"""In einem konstruierten Modell hat der kategoriale Prädiktor „{setting}“ $k={k}$ Kategorien: {", ".join(categories)}. Verwende „{reference}“ als Referenzkategorie und behalte einen Achsenabschnitt bei. $D_1$ bis $D_{k-1}$ kennzeichnen die Nichtreferenzkategorien in der aufgeführten Reihenfolge. Das angepasste Modell für die Ergebnisvariable „{outcome}“ lautet $\hat Y={number(b0, 2)} {formula_terms}$.

(a) Gib an, wie viele Dummy-Variablen benötigt werden, und erkläre weshalb. (b) Erstelle für jede Kategorie die vollständige Codierungstabelle mit Nullen und Einsen. (c) Bestimme die Referenzzeile, berechne den angepassten Wert jeder Kategorie und interpretiere den Koeffizienten von $D_1$ als Vergleich mit der Referenz. (d) Erkläre, weshalb eine eigene Dummy-Variable für alle $k$ Kategorien bei beibehaltenem Achsenabschnitt eine exakte Redundanz erzeugt. Beschreibe zudem, was sich bei einer anderen Referenz ändern und was gleich bleiben würde."""
            headers = ("Kategorie",) + tuple(
                f"$D_{index}$ ({categories[index]})" for index in range(1, k)
            )
            direction = "höher" if effects[0] > 0 else "tiefer"
            solution = rf"""(a) Mit einem Achsenabschnitt werden $k-1={k-1}$ Dummy-Variablen benötigt. Die ausgelassene Kategorie wird durch den Achsenabschnitt dargestellt und bildet die Vergleichsbasis.

(b) Die vollständige Codierung lautet:

{c.markdown_table(headers, coding_rows)}

(c) Die Kategorie „{reference}“ ist die Referenz, weil in dieser Zeile jede Dummy-Variable null ist. Die angepassten Werte der Kategorien lauten:

{c.markdown_table(("Kategorie", f"Angepasster Wert der Ergebnisvariable „{outcome}“"), fitted_rows)}

Der Koeffizient von $D_1$ ist {number(effects[0], 2)}. Somit liegt der angepasste Wert der Ergebnisvariable „{outcome}“ für die Kategorie „{categories[1]}“ um {number(abs(effects[0]), 2)} Punkte {direction} als für die Referenzkategorie „{reference}“. Der Achsenabschnitt {number(b0, 2)} ist der angepasste Wert für „{reference}“.

(d) Für jeden Fall würden sich die $k$ Kategorieindikatoren genau zu eins summieren. Diese Eins ist bereits die Achsenabschnittsspalte. Werden alle Indikatoren zusammen mit dem Achsenabschnitt aufgenommen, ist eine Spalte eine exakte Kombination der anderen und die Koeffizienten sind nicht eindeutig bestimmt. Eine andere Referenz verändert den angezeigten Achsenabschnitt und die Kategoriekontraste, aber nicht den angepassten Wert einer Kategorie."""
        else:
            prompt = rf"""Në një model të ndërtuar, ndryshorja parashikuese kategorike «{setting}» ka $k={k}$ kategori: {", ".join(categories)}. Përdor «{reference}» si kategori referuese dhe mbaje prerjen. Përdor $D_1$ deri te $D_{k-1}$ për të identifikuar kategoritë joreferuese sipas rendit të dhënë. Modeli i përshtatur për ndryshoren e rezultatit «{outcome}» është $\hat Y={number(b0, 2)} {formula_terms}$.

(a) Shëno sa tregues nevojiten dhe shpjego pse. (b) Ndërtoje tabelën e plotë të kodimit me zero dhe një për secilën kategori. (c) Gjeje rreshtin referues, llogarite vlerën e përshtatur të secilës kategori dhe interpretoje koeficientin e $D_1$ si krahasim me referencën. (d) Shpjego pse shtimi i një treguesi të veçantë për të gjitha $k$ kategoritë, duke e mbajtur prerjen, krijon varësi lineare të saktë. Përshkruaj çfarë do të ndryshonte dhe çfarë do të mbetej e pandryshuar po të zgjidhej një referencë tjetër."""
            headers = ("Kategoria",) + tuple(
                f"$D_{index}$ ({categories[index]})" for index in range(1, k)
            )
            direction = "më e lartë" if effects[0] > 0 else "më e ulët"
            solution = rf"""(a) Me një prerje nevojiten $k-1={k-1}$ tregues. Kategoria e lënë jashtë përfaqësohet nga prerja dhe bëhet baza e krahasimit.

(b) Kodimi i plotë është:

{c.markdown_table(headers, coding_rows)}

(c) Kategoria «{reference}» është referenca sepse çdo tregues është zero në atë rresht. Vlerat e përshtatura të kategorive janë:

{c.markdown_table(("Kategoria", f"Vlera e përshtatur e ndryshores «{outcome}»"), fitted_rows)}

Koeficienti i $D_1$ është {number(effects[0], 2)}. Prandaj, vlera e përshtatur e ndryshores së rezultatit «{outcome}» për kategorinë «{categories[1]}» është {number(abs(effects[0]), 2)} pikë {direction} se për kategorinë referuese «{reference}». Prerja {number(b0, 2)} është vlera e përshtatur për «{reference}».

(d) Për secilin rast, $k$ treguesit e kategorive do të jepnin shumën saktësisht një, e cila tashmë është kolona e prerjes. Përfshirja e të gjithë treguesve bashkë me prerjen e bën njërën kolonë kombinim të saktë të kolonave të tjera, prandaj koeficientët nuk mund të përcaktohen në mënyrë unike. Zgjedhja e një reference tjetër e ndryshon prerjen dhe kontrastet e kategorive që paraqiten, por nuk e ndryshon vlerën e përshtatur të asnjë kategorie."""
        exercise_group.append(task(7, 6, variant, setting, prompt))
        solution_group.append(task(7, 6, variant, setting, solution))
    return "".join(exercise_group), "".join(solution_group)


def _render_a07(locale: str, c: ModuleType) -> tuple[str, str]:
    cases = _localized_cases(c.A07_CASES, A07_TEXT[locale], 5)
    exercise_group = [group_heading(7, GROUP_TITLES[locale][6])]
    solution_group = [group_heading(7, GROUP_TITLES[locale][6])]
    for variant, case in enumerate(cases, 1):
        title, outcome, x_name, reference, comparison, b0, b1, b2, x_low, x_high = case
        rows = []
        for group_name, group in ((reference, 0), (comparison, 1)):
            for x_value in (x_low, x_high):
                rows.append(
                    (
                        group_name,
                        number(x_value, 1),
                        number(c.fitted(b0, b1, b2, 0.0, x_value, group), 2),
                    )
                )
        if locale == "de":
            prompt = rf"""Ein konstruiertes additives Modell verwendet $G=0$ für die Gruppe „{reference}“ und $G=1$ für die Gruppe „{comparison}“: $\hat Y={number(b0, 2)}+({number(b1, 2)})X+({number(b2, 2)})G$. Dabei bezeichnet $Y$ die Ergebnisvariable „{outcome}“ und $X$ den Prädiktor „{x_name}“.

(a) Schreibe die angepasste Gleichung für jede Gruppe auf und interpretiere den Achsenabschnitt bei $X=0$. Weise darauf hin, wenn null lediglich eine mathematische Referenz sein könnte. (b) Interpretiere die gemeinsame $X$-Steigung und den Gruppenkoeffizienten als bedingte Vergleiche. (c) Berechne die angepassten Koordinaten beider Gruppen bei $X={number(x_low, 1)}$ und $X={number(x_high, 1)}$ und ordne sie in einer Tabelle. (d) Erkläre anhand dieser Koordinaten, weshalb die Linien parallel sind und der Gruppenabstand konstant bleibt. Begründe zudem, weshalb der angepasste Abstand allein keinen kausalen Gruppeneffekt belegt."""
            direction = "höher" if b2 > 0 else "tiefer"
            solution = rf"""(a) Setze für die Gruppe „{reference}“ $G=0$: $\hat Y={number(b0, 2)}+({number(b1, 2)})X$. Setze für die Gruppe „{comparison}“ $G=1$: $\hat Y={number(b0+b2, 2)}+({number(b1, 2)})X$. Der Achsenabschnitt {number(b0, 2)} ist der angepasste Wert der Ergebnisvariable „{outcome}“ in der Gruppe „{reference}“, wenn der Prädiktor „{x_name}“ null ist. Er kann mathematisch notwendig, aber inhaltlich wenig hilfreich sein, wenn null ausserhalb des sinnvollen Bereichs liegt.

(b) Innerhalb jeder Gruppe geht eine Zunahme des Prädiktors „{x_name}“ um eine Einheit mit einer angepassten Veränderung der Ergebnisvariable „{outcome}“ um {number(b1, 2)} Einheiten einher. Beim selben Wert des Prädiktors liegt der angepasste Wert für die Gruppe „{comparison}“ um {number(abs(b2), 2)} Einheiten {direction} als für „{reference}“. "Beim selben Wert" bezeichnet den bedingten Modellvergleich und keinen Eingriff.

(c) Einsetzen ergibt:

{c.markdown_table(("Gruppe", "X", f"Angepasster Wert der Ergebnisvariable „{outcome}“"), rows)}

(d) Beide Gleichungen haben die Steigung {number(b1, 2)}. Gleiche horizontale Veränderungen erzeugen deshalb gleiche angepasste vertikale Veränderungen. Ihre Achsenabschnitte unterscheiden sich um {number(b2, 2)}. Werden die beiden angepassten Werte an einem der gezeigten $X$-Werte voneinander subtrahiert, entsteht derselbe konstante Abstand. Das Modell enthält keinen $XG$-Produktterm und erzwingt daher parallele angepasste Linien. Der Abstand ist ein bereinigter Zusammenhang. Ohne ein geeignetes Design und geeignete Annahmen beweist er nicht, dass eine Veränderung der Gruppenzugehörigkeit die Ergebnisvariable verändern würde."""
        else:
            prompt = rf"""Një model aditiv i ndërtuar përdor $G=0$ për grupin «{reference}» dhe $G=1$ për grupin «{comparison}»: $\hat Y={number(b0, 2)}+({number(b1, 2)})X+({number(b2, 2)})G$. Këtu $Y$ shënon ndryshoren e rezultatit «{outcome}», ndërsa $X$ shënon ndryshoren parashikuese «{x_name}».

(a) Shkruaje ekuacionin e përshtatur për secilin grup dhe interpretoje prerjen në $X=0$, duke vënë në dukje kur zeroja mund të jetë vetëm referencë matematikore. (b) Interpretoji pjerrësinë e përbashkët të $X$ dhe koeficientin e grupit si krahasime të kushtëzuara. (c) Llogariti koordinatat e përshtatura për të dyja grupet në $X={number(x_low, 1)}$ dhe $X={number(x_high, 1)}$ dhe organizoji në tabelë. (d) Shpjego si tregojnë këto koordinata vija paralele dhe një largësi të pandryshueshme mes grupeve. Gjithashtu shëno pse largësia e përshtatur nuk vërteton vetvetiu efekt shkakësor të grupit."""
            direction = "më lart" if b2 > 0 else "më poshtë"
            solution = rf"""(a) Për grupin «{reference}», vendos $G=0$: $\hat Y={number(b0, 2)}+({number(b1, 2)})X$. Për grupin «{comparison}», vendos $G=1$: $\hat Y={number(b0+b2, 2)}+({number(b1, 2)})X$. Prerja {number(b0, 2)} është vlera e përshtatur e ndryshores së rezultatit «{outcome}» për grupin «{reference}», kur ndryshorja parashikuese «{x_name}» është zero. Mund të jetë e nevojshme matematikisht, por e padobishme nga ana përmbajtësore nëse zeroja gjendet jashtë intervalit kuptimplotë.

(b) Brenda cilitdo grup, një rritje me një njësi e ndryshores parashikuese «{x_name}» lidhet me një ndryshim të përshtatur prej {number(b1, 2)} njësish në ndryshoren e rezultatit «{outcome}». Kur ndryshorja parashikuese ka të njëjtën vlerë, vlera e përshtatur për grupin «{comparison}» është {number(abs(b2), 2)} njësi {direction} se për grupin «{reference}». Shprehja "në të njëjtën vlerë" tregon krahasimin e kushtëzuar të modelit, jo një ndërhyrje.

(c) Zëvendësimi jep:

{c.markdown_table(("Grupi", "X", f"Vlera e përshtatur e ndryshores «{outcome}»"), rows)}

(d) Të dy ekuacionet kanë pjerrësi {number(b1, 2)}, prandaj ndryshime të barabarta horizontale prodhojnë ndryshime të barabarta vertikale të përshtatura. Prerjet e tyre ndryshojnë me {number(b2, 2)} dhe zbritja e dy vlerave të përshtatura në cilëndo $X$ të paraqitur jep po atë largësi të pandryshueshme. Modeli nuk përmban term prodhimi $XG$, prandaj imponon vija të përshtatura paralele. Largësia është lidhje e përshtatur. Pa dizajn dhe supozime të përshtatshme, nuk vërteton se ndryshimi i përkatësisë në grup do ta ndryshonte rezultatin."""
        exercise_group.append(task(7, 7, variant, title, prompt))
        solution_group.append(task(7, 7, variant, title, solution))
    return "".join(exercise_group), "".join(solution_group)


def _render_a08(locale: str, c: ModuleType) -> tuple[str, str]:
    cases = _localized_cases(c.A08_CASES, A08_TEXT[locale], 5)
    exercise_group = [group_heading(8, GROUP_TITLES[locale][7])]
    solution_group = [group_heading(8, GROUP_TITLES[locale][7])]
    for variant, case in enumerate(cases, 1):
        title, outcome, x_name, old_reference, new_reference, b0, b1, b2, x_low, x_high = case
        new_b0, new_b1, new_b2 = b0 + b2, b1, -b2
        comparison_rows = []
        for group_name, old_g, new_h in (
            (old_reference, 0, 1),
            (new_reference, 1, 0),
        ):
            for x_value in (x_low, x_high):
                old_fit = b0 + b1 * x_value + b2 * old_g
                new_fit = new_b0 + new_b1 * x_value + new_b2 * new_h
                comparison_rows.append(
                    (
                        group_name,
                        number(x_value, 1),
                        number(old_fit, 2),
                        number(new_fit, 2),
                    )
                )
        if locale == "de":
            prompt = rf"""Ein konstruiertes additives Modell codiert $G=0$ für die Gruppe „{old_reference}“ und $G=1$ für die Gruppe „{new_reference}“: $\hat Y={number(b0, 2)}+({number(b1, 2)})X+({number(b2, 2)})G$. Dabei bezeichnet $Y$ die Ergebnisvariable „{outcome}“ und $X$ den Prädiktor „{x_name}“. Codiere neu mit $H=0$ für „{new_reference}“ und $H=1$ für „{old_reference}“.

(a) Leite den neuen Achsenabschnitt, die neue $X$-Steigung und den Koeffizienten von $H$ her. (b) Schreibe beide Gruppengleichungen unter der neuen Codierung auf und interpretiere den neuen Gruppenkoeffizienten. (c) Berechne bei $X={number(x_low, 1)}$ und $X={number(x_high, 1)}$ für beide Gruppen die angepassten Werte aus beiden Parametrisierungen und stelle sie nebeneinander. (d) Erkläre anhand der Berechnungen, weshalb das Wechseln der Referenz das Koordinatensystem der Koeffizienten verändert, aber die angepassten Werte, Residuen und gruppenspezifischen angepassten Linien nicht verändern kann."""
            direction = "höher" if new_b2 > 0 else "tiefer"
            solution = rf"""(a) Die neue Referenz ist die alte Gruppe mit $G=1$. Ihr alter Achsenabschnitt wird daher zum neuen Achsenabschnitt: $b'_0={number(b0, 2)}+({number(b2, 2)})={number(new_b0, 2)}$. Die gemeinsame Steigung bleibt $b'_1={number(new_b1, 2)}$. Der Kontrast kehrt seine Richtung um, somit gilt $b'_2=-({number(b2, 2)})={number(new_b2, 2)}$.

(b) Für die Gruppe „{new_reference}“ ist $H=0$, woraus $\hat Y={number(new_b0, 2)}+({number(new_b1, 2)})X$ folgt. Für die Gruppe „{old_reference}“ ist $H=1$, woraus $\hat Y={number(new_b0, 2)}+({number(new_b1, 2)})X+({number(new_b2, 2)})={number(b0, 2)}+({number(b1, 2)})X$ folgt. Beim selben $X$ liegt der angepasste Wert für „{old_reference}“ um {number(abs(new_b2), 2)} Einheiten {direction} als für „{new_reference}“.

(c) Beide Codierungen ergeben:

{c.markdown_table(("Gruppe", "X", "Anpassung aus alter Codierung", "Anpassung aus neuer Codierung"), comparison_rows)}

(d) In jeder Zeile sind die angepassten Werte unter beiden Codierungen identisch. Das Wechseln der Referenz verändert, welche Gruppe der Achsenabschnitt darstellt, und kehrt den angezeigten Gruppenkontrast um. Es beschreibt jedoch dieselben zwei Linien. Weil jeder Fall denselben angepassten Wert behält, bleibt auch jedes Residuum unverändert, wenn der angepasste Wert von der beobachteten Ergebnisvariable subtrahiert wird. Die Referenzwahl verändert die Darstellung, nicht die Modellanpassung oder die zugrunde liegenden angepassten Beziehungen."""
        else:
            prompt = rf"""Një model aditiv i ndërtuar kodon $G=0$ për grupin «{old_reference}» dhe $G=1$ për grupin «{new_reference}»: $\hat Y={number(b0, 2)}+({number(b1, 2)})X+({number(b2, 2)})G$. Këtu $Y$ shënon ndryshoren e rezultatit «{outcome}», ndërsa $X$ shënon ndryshoren parashikuese «{x_name}». Rikodoje me $H=0$ për «{new_reference}» dhe $H=1$ për «{old_reference}».

(a) Nxirre prerjen e re, pjerrësinë e re të $X$ dhe koeficientin e $H$. (b) Shkruaji të dy ekuacionet e grupeve me kodimin e ri dhe interpretoje koeficientin e ri të grupit. (c) Në $X={number(x_low, 1)}$ dhe $X={number(x_high, 1)}$, llogariti vlerat e përshtatura nga të dy parametrizimet për të dyja grupet dhe vendosi krah për krah. (d) Përdori llogaritjet për të shpjeguar pse ndërrimi i referencës e ndryshon sistemin koordinativ të koeficienteve, por nuk mund t'i ndryshojë vlerat e përshtatura, rezidualet ose vijat e përshtatura të grupeve."""
            direction = "më lart" if new_b2 > 0 else "më poshtë"
            solution = rf"""(a) Referenca e re është grupi i vjetër $G=1$, prandaj prerja e tij e vjetër bëhet prerja e re: $b'_0={number(b0, 2)}+({number(b2, 2)})={number(new_b0, 2)}$. Pjerrësia e përbashkët mbetet $b'_1={number(new_b1, 2)}$. Kontrasti e ndërron drejtimin, prandaj $b'_2=-({number(b2, 2)})={number(new_b2, 2)}$.

(b) Për grupin «{new_reference}», $H=0$, që jep $\hat Y={number(new_b0, 2)}+({number(new_b1, 2)})X$. Për grupin «{old_reference}», $H=1$, që jep $\hat Y={number(new_b0, 2)}+({number(new_b1, 2)})X+({number(new_b2, 2)})={number(b0, 2)}+({number(b1, 2)})X$. Në të njëjtin $X$, vlera e përshtatur për grupin «{old_reference}» është {number(abs(new_b2), 2)} njësi {direction} se për grupin «{new_reference}».

(c) Të dy kodimet japin:

{c.markdown_table(("Grupi", "X", "Përshtatja nga kodimi i vjetër", "Përshtatja nga kodimi i ri"), comparison_rows)}

(d) Çdo rresht ka vlera të përshtatura identike në të dy kodimet. Ndërrimi i referencës e ndryshon grupin që përfaqëson prerja dhe e përmbys kontrastin e paraqitur mes grupeve, por përshkruan të njëjtat dy vija. Meqë secili rast e mban të njëjtën vlerë të përshtatur, zbritja e saj nga rezultati i vëzhguar e lë të pandryshuar edhe secilin rezidual. Zgjedhja e referencës e ndryshon paraqitjen, jo përshtatjen e modelit ose marrëdhëniet e përshtatura."""
        exercise_group.append(task(7, 8, variant, title, prompt))
        solution_group.append(task(7, 8, variant, title, solution))
    return "".join(exercise_group), "".join(solution_group)


def _render_a09(locale: str, c: ModuleType) -> tuple[str, str]:
    cases = _localized_cases(c.A09_CASES, A09_TEXT[locale], 5)
    exercise_group = [group_heading(9, GROUP_TITLES[locale][8])]
    solution_group = [group_heading(9, GROUP_TITLES[locale][8])]
    for variant, case in enumerate(cases, 1):
        title, outcome, x_name, reference, comparison, b0, b1, b2, b3, x_low, x_high = case
        rows = []
        for group_name, group in ((reference, 0), (comparison, 1)):
            for x_value in (x_low, x_high):
                rows.append(
                    (
                        group_name,
                        str(group),
                        number(x_value, 1),
                        number(x_value * group, 1),
                        number(c.fitted(b0, b1, b2, b3, x_value, group), 2),
                    )
                )
        gap_low = b2 + b3 * x_low
        gap_high = b2 + b3 * x_high
        if locale == "de":
            prompt = rf"""Ein konstruiertes Interaktionsmodell verwendet $G=0$ für die Gruppe „{reference}“, $G=1$ für die Gruppe „{comparison}“ und das Produkt $XG$: $\hat Y={number(b0, 2)}+({number(b1, 2)})X+({number(b2, 2)})G+({number(b3, 2)})XG$. Dabei bezeichnet $Y$ die Ergebnisvariable „{outcome}“ und $X$ den Prädiktor „{x_name}“.

(a) Erstelle für beide Gruppen Zeilen bei $X={number(x_low, 1)}$ und $X={number(x_high, 1)}$ und zeige darin $G$ und $XG$. (b) Leite den bedingten Achsenabschnitt und die bedingte Steigung jeder Gruppe her. (c) Berechne die vier angepassten Koordinaten und ordne alle Grössen in einer Tabelle. (d) Zeichne aus diesen Koordinaten die beiden angepassten Geraden in ein beschriftetes Diagramm und markiere bei beiden dargestellten $X$-Werten den angepassten Gruppenabstand. (e) Interpretiere $b_1$, $b_2$ und $b_3$ bei ihren richtigen Referenzbedingungen. Erkläre, wie $b_3$ den Gruppenabstand entlang von $X$ verändert, und begründe, weshalb eine Interaktion selbst kein Kausalitätsbeleg ist."""
            solution = rf"""(a) Wenn $G=0$ ist, ist das Produkt $XG$ für jedes $X$ null. Wenn $G=1$ ist, gilt $XG=X$. (b) Einsetzen ergibt für die Gruppe „{reference}“: $\hat Y={number(b0, 2)}+({number(b1, 2)})X$, mit der Steigung {number(b1, 2)}. Für die Gruppe „{comparison}“ ergibt sich: $\hat Y={number(b0+b2, 2)}+({number(b1+b3, 2)})X$, mit der Steigung $b_1+b_3={number(b1, 2)}+({number(b3, 2)})={number(b1+b3, 2)}$.

(c) Die Produktterme und angepassten Koordinaten lauten:

{c.markdown_table(("Gruppe", "G", "X", "XG", f"Angepasster Wert der Ergebnisvariable „{outcome}“"), rows)}

(d) Trage den Prädiktor „{x_name}“ auf der horizontalen Achse und den angepassten Wert der Ergebnisvariable „{outcome}“ auf der vertikalen Achse ab. Verbinde für die Gruppe „{reference}“ ihre beiden Koordinaten aus der Tabelle. Verbinde für die Gruppe „{comparison}“ ihre beiden Koordinaten zu einer zweiten beschrifteten Geraden. Zeichne bei $X={number(x_low,1)}$ und $X={number(x_high,1)}$ vertikale Strecken zwischen den Geraden und beschrifte ihre Längen mit {number(gap_low,2)} und {number(gap_high,2)}. Die nicht parallelen Steigungen machen den sich verändernden Abstand sichtbar.

(e) $b_1={number(b1, 2)}$ ist die Steigung des Prädiktors „{x_name}“ in der Referenzgruppe. $b_2={number(b2, 2)}$ ist die angepasste Differenz „{comparison}“ minus „{reference}“, und zwar genau bei $X=0$. Der Koeffizient bleibt dort interpretierbar, auch wenn null inhaltlich nicht zentral ist. $b_3={number(b3, 2)}$ ist die Differenz zwischen den beiden Gruppensteigungen. Der angepasste Gruppenabstand lautet daher $b_2+b_3X$: Er beträgt {number(gap_low, 2)} bei $X={number(x_low, 1)}$ und {number(gap_high, 2)} bei $X={number(x_high, 1)}$. Die Interaktion beschreibt, wie sich ein bedingter Zusammenhang zwischen Gruppen unterscheidet. Sie belegt nicht, dass die Gruppe oder $X$ die Ergebnisvariable verursacht."""
        else:
            prompt = rf"""Një model ndërveprimi i ndërtuar përdor $G=0$ për grupin «{reference}», $G=1$ për grupin «{comparison}» dhe prodhimin $XG$: $\hat Y={number(b0, 2)}+({number(b1, 2)})X+({number(b2, 2)})G+({number(b3, 2)})XG$. Këtu $Y$ shënon ndryshoren e rezultatit «{outcome}», ndërsa $X$ shënon ndryshoren parashikuese «{x_name}».

(a) Ndërtoji rreshtat për të dyja grupet në $X={number(x_low, 1)}$ dhe $X={number(x_high, 1)}$, duke paraqitur $G$ dhe $XG$. (b) Nxirre prerjen dhe pjerrësinë e kushtëzuar të secilit grup. (c) Llogariti katër koordinatat e përshtatura dhe organizoji të gjitha madhësitë në një tabelë. (d) Vizatoji dy vijat e përshtatura nga këto koordinata në një grafik të vetëm të emërtuar dhe shënoje largësinë e përshtatur mes grupeve në të dyja vlerat e paraqitura të $X$. (e) Interpretoji $b_1$, $b_2$ dhe $b_3$ në kushtet e tyre të duhura referuese, shpjego si e ndryshon $b_3$ largësinë mes grupeve përgjatë $X$ dhe shëno pse një ndërveprim nuk është vetvetiu provë shkakësore."""
            solution = rf"""(a) Kur $G=0$, prodhimi $XG$ është zero për çdo $X$. Kur $G=1$, $XG=X$. (b) Zëvendësimi jep për grupin «{reference}»: $\hat Y={number(b0, 2)}+({number(b1, 2)})X$, me pjerrësi {number(b1, 2)}. Për grupin «{comparison}»: $\hat Y={number(b0+b2, 2)}+({number(b1+b3, 2)})X$, me pjerrësi $b_1+b_3={number(b1, 2)}+({number(b3, 2)})={number(b1+b3, 2)}$.

(c) Termat e prodhimit dhe koordinatat e përshtatura janë:

{c.markdown_table(("Grupi", "G", "X", "XG", f"Vlera e përshtatur e ndryshores «{outcome}»"), rows)}

(d) Vendose ndryshoren parashikuese «{x_name}» në boshtin horizontal dhe vlerën e përshtatur të ndryshores së rezultatit «{outcome}» në boshtin vertikal. Për grupin «{reference}», lidhi dy koordinatat e tij nga tabela. Për grupin «{comparison}», lidhi dy koordinatat e tij në një vijë të dytë të emërtuar. Vizato segmente vertikale mes vijave në $X={number(x_low,1)}$ dhe $X={number(x_high,1)}$ dhe emërtoji gjatësitë e tyre me {number(gap_low,2)} dhe {number(gap_high,2)}. Pjerrësitë joparalele e bëjnë të dukshme largësinë që ndryshon.

(e) $b_1={number(b1, 2)}$ është pjerrësia e ndryshores parashikuese «{x_name}» në grupin referues. $b_2={number(b2, 2)}$ është diferenca e përshtatur «{comparison}» minus «{reference}», pikërisht në $X=0$. Mbetet e interpretueshme aty, megjithëse zeroja mund të mos jetë qendrore nga ana përmbajtësore. $b_3={number(b3, 2)}$ është diferenca mes dy pjerrësive të grupeve. Prandaj, largësia e përshtatur mes grupeve është $b_2+b_3X$: ajo është {number(gap_low, 2)} në $X={number(x_low, 1)}$ dhe {number(gap_high, 2)} në $X={number(x_high, 1)}$. Ndërveprimi përshkruan si ndryshon një lidhje e kushtëzuar sipas grupit. Nuk vërteton se grupi ose $X$ e shkakton rezultatin."""
        exercise_group.append(task(7, 9, variant, title, prompt))
        solution_group.append(task(7, 9, variant, title, solution))
    return "".join(exercise_group), "".join(solution_group)


def _task_bodies(text: str) -> dict[str, str]:
    pattern = re.compile(r"^## (T07-A\d{2}-V\d{2}): [^\n]+\n\n", re.MULTILINE)
    matches = list(pattern.finditer(text))
    return {
        match.group(1): text[
            match.end() : matches[index + 1].start() if index + 1 < len(matches) else len(text)
        ]
        for index, match in enumerate(matches)
    }


def _math_spans(text: str) -> tuple[str, ...]:
    pattern = re.compile(r"\$\$(.*?)\$\$|(?<!\$)\$(?!\$)(.*?)(?<!\$)\$(?!\$)", re.DOTALL)
    return tuple(next(group for group in match.groups() if group is not None) for match in pattern.finditer(text))


def _canonical_math_reference(identifier: str, label: str, text: str) -> str:
    """Repair one legacy delimiter only in memory before formula comparison.

    Canonical English A09 exercise prose is intentionally regenerated byte for
    byte in this pass. Its second displayed X coordinate lacks one closing
    dollar sign. Localized sources use balanced delimiters, so this function
    supplies the intended English formula boundary only to the validator.
    """

    if label == "exercise" and identifier.startswith("T07-A09-"):
        return re.sub(
            r"(\$X=[^$\n]+), showing \$G\$",
            r"\1$, showing $G$",
            text,
            count=1,
        )
    return text


def _table_geometry(text: str) -> tuple[tuple[int, ...], ...]:
    tables: list[tuple[int, ...]] = []
    current: list[int] = []
    for line in text.splitlines():
        if line.startswith("|"):
            current.append(line.count("|"))
        elif current:
            tables.append(tuple(current))
            current = []
    if current:
        tables.append(tuple(current))
    return tuple(tables)


def _validate_localized(
    locale: str,
    exercises: list[str],
    solutions: list[str],
    canonical_exercises: list[str],
    canonical_solutions: list[str],
) -> None:
    if len(exercises) != 9 or len(solutions) != 9:
        raise AssertionError("Topic 7 needs nine localized practice groups")
    expected = [
        task_id(7, group, variant)
        for group in range(1, 10)
        for variant in range(1, 11)
    ]
    heading_pattern = re.compile(r"^## (T07-A\d{2}-V\d{2}): ([^\n]+)\n\n", re.MULTILINE)
    localized_texts = ("".join(exercises), "".join(solutions))
    canonical_texts = ("".join(canonical_exercises), "".join(canonical_solutions))
    for label, localized, canonical in zip(("exercise", "solution"), localized_texts, canonical_texts):
        matches = list(heading_pattern.finditer(localized))
        if [match.group(1) for match in matches] != expected:
            raise AssertionError(f"localized {label} IDs are incomplete or out of order")
        if "\u2014" in localized:
            raise AssertionError(f"localized {label} text contains an em dash")
        if locale == "de" and "\u00df" in localized:
            raise AssertionError(f"localized {label} text contains German sharp-s")
        formal_sq = ("j" + "u", "j" + "uaj", "t" + "uaj", "s" + "uaj", "j" + "ush")
        formal_sq_pattern = r"\b(?:" + "|".join(formal_sq) + r")\b"
        if locale == "sq" and re.search(formal_sq_pattern, localized, re.IGNORECASE):
            raise AssertionError(f"localized {label} text contains formal Albanian address")
        localized_bodies = _task_bodies(localized)
        canonical_bodies = _task_bodies(canonical)
        if tuple(localized_bodies) != tuple(canonical_bodies):
            raise AssertionError(f"localized {label} task order differs from canonical English")
        for identifier in expected:
            localized_body = localized_bodies[identifier]
            canonical_body = canonical_bodies[identifier]
            for letter in "abcd":
                if localized_body.count(f"({letter})") != 1:
                    raise AssertionError(f"{identifier} {label} needs exactly one ({letter}) response")
            canonical_math_body = _canonical_math_reference(
                identifier, label, canonical_body
            )
            if _math_spans(localized_body) != _math_spans(canonical_math_body):
                raise AssertionError(f"{identifier} {label} math spans differ from canonical English")
            if _table_geometry(localized_body) != _table_geometry(canonical_body):
                raise AssertionError(f"{identifier} {label} table geometry differs from canonical English")
    exercise_titles = [match.group(2) for match in heading_pattern.finditer(localized_texts[0])]
    solution_titles = [match.group(2) for match in heading_pattern.finditer(localized_texts[1])]
    if exercise_titles != solution_titles:
        raise AssertionError("localized exercise and solution titles differ")


def render_localized(locale: str, canonical: ModuleType) -> tuple[list[str], list[str]]:
    """Render one complete localized pair from canonical Topic 7 calculations."""

    if locale not in ("de", "sq"):
        raise ValueError("Topic 7 localization is available only for de and sq")
    canonical._validate_case_data()
    rendered = [
        _render_a01(locale, canonical),
        _render_a02(locale, canonical),
        _render_a03(locale, canonical),
        _render_a04(locale, canonical),
        _render_a05(locale, canonical),
        _render_a06(locale, canonical),
        _render_a07(locale, canonical),
        _render_a08(locale, canonical),
        _render_a09(locale, canonical),
    ]
    exercises = [pair[0] for pair in rendered]
    solutions = [pair[1] for pair in rendered]
    canonical_exercises, canonical_solutions = canonical.render_english()
    _validate_localized(
        locale,
        exercises,
        solutions,
        canonical_exercises,
        canonical_solutions,
    )
    return exercises, solutions
