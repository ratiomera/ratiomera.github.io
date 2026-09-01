#!/usr/bin/env python3
"""Generate Ratiomera's authored Topic 2 learner documents.

The source worksheets define learning objectives only. Every context, value,
question, calculation, and explanation below is new Ratiomera material. Run one
locale at a time so the canonical English document can be reviewed before the
German and Albanian adaptations are generated.
"""

from __future__ import annotations

import argparse
import math
import re

import topic02_practice_i18n as i18n
from intro_stats_practice_support import write_pair


def probability_normal(z: float) -> float:
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))


def number(value: float, digits: int = 4) -> str:
    return f"{value:.{digits}f}"


def probability_binomial(n: int, p: float, x: int) -> float:
    return math.comb(n, x) * p**x * (1 - p) ** (n - x)


def heading(group: int, title: str) -> str:
    return f"# A{group:02d}: {title}\n\n"


def task(topic: int, group: int, variant: int, title: str, body: str) -> str:
    return f"## T{topic:02d}-A{group:02d}-V{variant:02d}: {title}\n\n{body.strip()}\n\n"


STAGE_CONTEXTS = [
    ("Completing an archive search", "locate the catalog record", "request the box", "identify the relevant letter"),
    ("Passing a three-stage language assessment", "pass the vocabulary section", "pass the listening section", "pass the interview"),
    ("Finishing a digital registration", "verify the email address", "complete the profile", "submit the consent form"),
    ("Solving a fieldwork sequence", "find the sampling point", "record a valid measurement", "upload the record correctly"),
    ("Completing a library research task", "find the database", "retrieve a suitable article", "evaluate its methods accurately"),
    ("Advancing through a music audition", "pass the rhythm screen", "pass the prepared piece", "pass the sight-reading task"),
    ("Completing a laboratory protocol", "prepare the sample", "obtain a usable reading", "label the result correctly"),
    ("Finishing an online safety course", "complete the first module", "pass the scenario quiz", "submit the final reflection"),
    ("Completing a map-reading challenge", "select the correct route", "reach the checkpoint", "identify the final landmark"),
    ("Passing a data-entry check", "enter the first form correctly", "resolve the validation warning", "submit the clean record"),
]
STAGE_PROBABILITIES = [
    (0.62, 0.81, 0.74), (0.68, 0.77, 0.84), (0.73, 0.86, 0.79),
    (0.57, 0.83, 0.91), (0.66, 0.72, 0.88), (0.71, 0.69, 0.82),
    (0.64, 0.87, 0.76), (0.78, 0.75, 0.89), (0.59, 0.82, 0.85),
    (0.69, 0.84, 0.73),
]

INDEPENDENT_CONTEXTS = [
    ("Two independent quality checks", "a scanned page passes the image check", "the same page passes the metadata check"),
    ("Independent workshop attendance", "a resident attends the morning session", "the resident attends the evening session"),
    ("Two independent sensor alerts", "the temperature sensor triggers", "the vibration sensor triggers"),
    ("Independent item selections", "a selected book is a translation", "it has a hard cover"),
    ("Independent survey events", "a response arrives on Monday", "it is submitted from a mobile device"),
    ("Two independent route events", "a bus arrives within five minutes", "a connecting train has an available seat"),
    ("Independent coding checks", "a record has a valid date", "it has a valid category code"),
    ("Two independent draws", "a selected token is blue", "a second, replaced draw is triangular"),
    ("Independent study events", "a participant completes the diary", "the laboratory file uploads successfully"),
    ("Independent catalog features", "an item is digitized", "its creator field is complete"),
]
INDEPENDENT_PROBABILITIES = [
    (0.78, 0.64), (0.55, 0.72), (0.18, 0.27), (0.36, 0.41), (0.22, 0.63),
    (0.74, 0.58), (0.83, 0.69), (0.45, 0.32), (0.67, 0.88), (0.39, 0.76),
]

TABLE_CONTEXTS = [
    ("Reading format and course completion", "Audio", "Text", "Completed", "Not completed", 12, 18, 28, 42),
    ("Museum membership and event attendance", "Member", "Nonmember", "Attended", "Did not attend", 24, 16, 18, 42),
    ("Study location and deadline success", "Library", "Home", "On time", "Late", 21, 14, 27, 18),
    ("Caption use and quiz completion", "Captions", "No captions", "Completed", "Not completed", 30, 20, 18, 12),
    ("Transit pass and campus visits", "Pass", "No pass", "Frequent", "Infrequent", 16, 24, 14, 46),
    ("Reminder choice and response", "Reminder", "No reminder", "Responded", "No response", 27, 13, 33, 27),
    ("Workshop track and certification", "Methods", "Writing", "Certified", "Not certified", 18, 12, 24, 36),
    ("Device type and form completion", "Tablet", "Laptop", "Complete", "Incomplete", 14, 21, 30, 15),
    ("Volunteer role and return visit", "Guide", "Archive", "Returned", "Did not return", 22, 18, 11, 29),
    ("Tutorial format and practice submission", "Live", "Recorded", "Submitted", "Not submitted", 26, 14, 39, 21),
]

BAYES_CONTEXTS = [
    ("Accessibility-needs screening", "an accessibility support need", 0.72, 0.91, 0.02, 0.11),
    ("Rare transcription-error detection", "a transcription error", 0.84, 0.93, 0.01, 0.08),
    ("Conservation-risk screening", "an object that is at conservation risk", 0.79, 0.88, 0.04, 0.16),
    ("Duplicate-record detection", "a record that is a duplicate", 0.90, 0.86, 0.03, 0.14),
    ("Language-support screening", "a need for language support", 0.76, 0.94, 0.05, 0.19),
    ("Damaged-image detection", "an image that is damaged", 0.88, 0.90, 0.02, 0.12),
    ("Research-integrity screening", "a submission that warrants integrity review", 0.81, 0.96, 0.01, 0.07),
    ("Equipment-failure warning", "an impending equipment failure", 0.85, 0.89, 0.06, 0.21),
    ("Cataloging-anomaly detection", "a record that contains a cataloging anomaly", 0.74, 0.92, 0.03, 0.15),
    ("Support-priority classification", "a case that genuinely has high support priority", 0.87, 0.95, 0.04, 0.18),
]

DISCRETE_DISTRIBUTIONS = [
    ("Number of follow-up questions", [0, 1, 3, 5], [0.20, 0.35, 0.30, 0.15]),
    ("Daily archive requests", [1, 2, 4, 6], [0.25, 0.40, 0.20, 0.15]),
    ("Completed practice sets", [0, 2, 3, 7], [0.10, 0.30, 0.45, 0.15]),
    ("Reported route changes", [0, 1, 2, 4], [0.45, 0.25, 0.20, 0.10]),
    ("Weekly community meetings", [1, 3, 4, 8], [0.30, 0.25, 0.35, 0.10]),
    ("Successful file recoveries", [0, 2, 5, 6], [0.15, 0.25, 0.40, 0.20]),
    ("Museum rooms visited", [2, 4, 5, 9], [0.20, 0.30, 0.35, 0.15]),
    ("Optional readings completed", [0, 1, 4, 6], [0.25, 0.30, 0.25, 0.20]),
    ("Verified oral-history segments", [1, 2, 3, 5], [0.15, 0.35, 0.30, 0.20]),
    ("Data-quality warnings", [0, 2, 4, 7], [0.40, 0.25, 0.20, 0.15]),
]

BINOMIAL_EXACT = [
    ("Completed consent checks", "consent checks", "is completed", 8, 0.62, 5, 7),
    ("Correctly classified images", "images", "is classified correctly", 9, 0.74, 6, 8),
    ("Returned diary prompts", "diary prompts", "is returned", 7, 0.58, 3, 5),
    ("Successful archive searches", "archive searches", "succeeds", 10, 0.43, 4, 6),
    ("Usable sensor readings", "sensor readings", "is usable", 6, 0.81, 4, 6),
    ("On-time tutorial submissions", "tutorial submissions", "arrives on time", 12, 0.67, 8, 10),
    ("Verified catalog entries", "catalog entries", "is verified", 9, 0.52, 4, 7),
    ("Completed interview appointments", "interview appointments", "is completed", 11, 0.76, 8, 9),
    ("Correct route choices", "route choices", "is correct", 8, 0.35, 2, 4),
    ("Successful audio transcriptions", "audio transcriptions", "is successful", 10, 0.69, 6, 8),
]

BINOMIAL_TAIL = [
    ("Records requiring manual review", "records", "requires manual review", 40, 0.04, 3),
    ("Visitors requesting audio guides", "museum visitors", "requests an audio guide", 25, 0.12, 5),
    ("Invalid survey links", "survey links", "is returned as invalid", 30, 0.06, 4),
    ("Items needing preservation work", "items", "needs preservation work", 35, 0.09, 6),
    ("Participants missing a reminder", "participants", "misses a reminder", 28, 0.08, 4),
    ("Uploads needing a second attempt", "uploads", "needs a second attempt", 32, 0.07, 5),
    ("Sampled pages containing annotations", "sampled pages", "contains annotations", 20, 0.15, 5),
    ("Interviews requiring rescheduling", "interviews", "requires rescheduling", 24, 0.11, 4),
    ("Route observations showing delay", "route observations", "shows a delay", 36, 0.05, 3),
    ("Forms containing an optional comment", "forms", "contains an optional comment", 18, 0.18, 5),
]

PMF_DENSITY_CONTEXTS = [
    ("the number of exhibitions visited", "the time spent in a museum"),
    ("the number of messages received", "the delay until the next message"),
    ("the count of transcription errors", "the duration of an audio segment"),
    ("the number of books borrowed", "the mass of a returned parcel"),
    ("the count of survey reminders", "a respondent's completion time"),
    ("the number of route changes", "the distance traveled"),
    ("the count of missing fields", "a participant's age measured precisely"),
    ("the number of workshop sessions", "the sound level in the room"),
    ("the count of preserved photographs", "the temperature of the archive"),
    ("the number of successful checks", "the exact reaction time on a task"),
]

STANDARD_NORMAL = [
    (-0.45, 1.36, -0.80, 0.95), (-1.12, 0.84, -0.35, 1.42),
    (0.28, 1.74, -1.05, 0.62), (-0.93, 1.18, -0.44, 1.27),
    (0.67, 2.05, -1.33, 0.71), (-1.48, 0.56, -0.92, 1.08),
    (0.14, 1.51, -0.68, 1.19), (-0.76, 1.89, -1.21, 0.37),
    (0.91, 1.24, -0.57, 1.63), (-0.22, 2.17, -1.46, 0.88),
]

GENERAL_NORMAL = [
    ("reading fluency score", "score points", 72, 100, 79, 68),
    ("archive processing time", "minutes", 45, 64, 51, 39),
    ("wellbeing score", "score points", 58, 81, 64, 52),
    ("museum visit duration", "minutes", 90, 225, 105, 78),
    ("memory score", "score points", 110, 144, 124, 103),
    ("sound-level index", "index points", 38, 49, 42, 33),
    ("course confidence score", "score points", 66, 121, 75, 59),
    ("response time", "milliseconds", 520, 3600, 575, 485),
    ("community trust score", "score points", 48, 64, 54, 43),
    ("cataloging accuracy score", "score points", 84, 36, 88, 79),
]

QUANTILES = [
    (0.70, 0.92), (0.15, 0.88), (0.80, 0.96), (0.28, 0.90), (0.50, 0.94),
    (0.75, 0.97), (0.32, 0.68), (0.82, 0.95), (0.11, 0.62), (0.78, 0.93),
]

SAMPLING = [
    ("reading score", "score points", 64, 196, 49, 100, 121),
    ("processing time", "minutes", 52, 225, 36, 144, 100),
    ("wellbeing index", "index points", 71, 144, 64, 256, 81),
    ("memory score", "score points", 105, 324, 81, 225, 144),
    ("trust rating", "rating points", 48, 100, 25, 169, 64),
    ("reaction time", "milliseconds", 480, 2500, 100, 1600, 400),
    ("confidence score", "score points", 59, 121, 49, 196, 100),
    ("visit duration", "minutes", 82, 400, 64, 256, 144),
    ("accuracy score", "score points", 88, 81, 36, 144, 49),
    ("sound index", "index points", 42, 169, 25, 100, 64),
]

NORMAL_INTERVALS = [
    ("focus score", "score points", 50, 81, 50, 59, 43, 61),
    ("reading score", "score points", 70, 100, 65, 82, 58, 76),
    ("visit duration", "minutes", 80, 225, 80, 95, 62, 101),
    ("memory score", "score points", 105, 144, 96, 117, 88, 122),
    ("trust index", "index points", 44, 64, 40, 52, 33, 49),
    ("response time", "milliseconds", 500, 2500, 475, 560, 410, 535),
    ("wellbeing score", "score points", 62, 121, 62, 74, 48, 69),
    ("cataloging score", "score points", 86, 49, 81, 93, 74, 90),
    ("sound level", "decibels", 36, 36, 36, 42, 27, 39),
    ("confidence rating", "rating points", 55, 64, 51, 63, 43, 59),
]

SAMPLING_BIAS = [
    (
        "Park-use QR survey",
        "A city estimates weekly park use by surveying 640 people who scan a code posted inside its largest central park.",
        "all city residents whose weekly use of any park is of interest",
        "people entering the largest central park during the posting period who notice the code",
        "the 640 park visitors who scanned the code and submitted the survey",
        "the proportion of all city residents who use any park weekly",
        "the proportion of the 640 respondents who report weekly park use",
        "Frequent park users are more likely to enter this park, and people who notice and scan a code may differ in interest or digital access from those who do not.",
        "Draw a probability sample from a city-resident frame and follow up selected nonrespondents through more than one contact mode.",
    ),
    (
        "Commuting survey of parking-permit holders",
        "A university estimates students' mean commuting time from 820 replies to an email sent only to parking-permit holders.",
        "all enrolled students",
        "the university's list of students holding parking permits",
        "the 820 parking-permit holders who replied",
        "the mean commuting time among all enrolled students",
        "the mean commuting time among the 820 respondents",
        "The frame omits students who walk, cycle, use transit, or do not hold a permit, and reply behavior may depend on commuting burden.",
        "Sample from the full enrollment register, stratify by likely travel mode if useful, and pursue responses from the selected students.",
    ),
    (
        "Satisfaction after one sold-out exhibition",
        "A museum estimates season-wide visitor satisfaction from 510 responses collected at the exit of one sold-out evening exhibition.",
        "all museum visitors during the target season",
        "visitors leaving the sold-out evening exhibition who were offered the exit survey",
        "the 510 attendees who completed that exit survey",
        "the mean satisfaction score among all visitors in the target season",
        "the mean satisfaction score among the 510 respondents",
        "One unusually popular evening may not represent other dates or exhibitions, and survey completion may depend on whether an attendee had a notably good or bad experience.",
        "Select visits across exhibitions, days, and times, then invite a probability sample of exiting visitors and document nonresponse.",
    ),
    (
        "Digital-access survey inside an app",
        "A library estimates digital-access needs from 430 answers to a survey advertised only through its smartphone app.",
        "all library users",
        "library users who use the smartphone app and were exposed to the survey notice",
        "the 430 app users who volunteered an answer",
        "the proportion of all library users who need better digital access",
        "the proportion of the 430 respondents reporting that need",
        "Users without suitable devices or app access cannot enter the frame, and volunteers who answer an access survey may have unusually strong needs or engagement.",
        "Sample from the full user register and offer accessible web, telephone, paper, and in-person response routes.",
    ),
    (
        "Volunteer hours from large-charity lists",
        "A region estimates mean weekly volunteer hours from records for 760 members listed by large registered charities.",
        "all volunteers in the region",
        "membership lists supplied by large registered charities",
        "the 760 listed charity members whose records were used",
        "the mean weekly volunteer hours among all regional volunteers",
        "the mean weekly hours recorded for those 760 listed members",
        "The lists exclude informal volunteers and members of small or unregistered groups, and formal membership records may overrepresent regular, long-term volunteers.",
        "Build a broader frame from multiple organization types and community sources, then use probability selection within defined volunteer strata.",
    ),
    (
        "Course-workload survey after grades",
        "A college estimates perceived course workload from 390 students still active on the learning platform after final grades were released.",
        "all students enrolled in the course",
        "enrolled students whose accounts remained active on the platform after grades were released",
        "the 390 still-active students who supplied workload information",
        "the mean perceived workload among all enrolled students",
        "the mean workload reported by the 390 respondents",
        "Students who disengaged, withdrew, or stopped using the platform are excluded, and willingness to answer after grading may be related to workload or course outcomes.",
        "Select from the original course roster, contact students independently of later platform activity, and follow up nonrespondents.",
    ),
    (
        "Transit delays inferred from hashtagged comments",
        "A transit agency estimates the proportion of rider trips experienced as delayed from 1 240 social-media comments containing its campaign hashtag.",
        "all rider trips during the target period",
        "publicly retrievable social-media comments that use the campaign hashtag",
        "the 1 240 retrieved hashtagged comments",
        "the proportion of all rider trips experienced as delayed",
        "the proportion of the 1 240 comments that describe a delay",
        "People with extreme experiences are more likely to post, one person can contribute several comments, and comments rather than rider trips are the observed units.",
        "Sample rider trips from operational records and obtain a response tied to each selected trip, while keeping the trip as the unit of analysis.",
    ),
    (
        "Neighborhood-interest forms after performances",
        "A cultural center estimates neighborhood interest from 570 completed forms distributed only after ticketed performances.",
        "all residents in the surrounding neighborhood",
        "ticket holders leaving the selected performances who were offered a form",
        "the 570 ticket holders who stayed and completed a form",
        "the proportion of neighborhood residents interested in future programs",
        "the proportion of the 570 respondents expressing interest",
        "Residents who do not already attend ticketed events are absent from the frame, and staying to complete a form may be related to enthusiasm for the center.",
        "Use a neighborhood address frame, select residents independently of attendance, and offer several response modes.",
    ),
    (
        "Sleep records from year-long wearable users",
        "A research team estimates users' mean nightly sleep duration from 680 people who kept a wearable device active for a full year.",
        "all users in the intended wearable-user population during the year",
        "device users with accounts activated at the beginning of the observation period",
        "the 680 users retained for a full year with complete sleep records",
        "the population mean nightly sleep duration",
        "the retained users' mean recorded nightly duration",
        "Year-long retention excludes intermittent or discontinued users, and retention or complete wear may depend on sleep habits, health, or satisfaction with the device.",
        "Select users at enrollment, retain partial records under a prespecified missing-data plan, and compare retained with lost participants.",
    ),
    (
        "Archive feedback shown only after a download",
        "An archive estimates the proportion of search attempts ending in successful retrieval from 450 feedback forms shown only after a user downloaded at least one record.",
        "all archive search attempts during the target period",
        "search attempts that reached at least one download and therefore received the feedback prompt",
        "the 450 submitted feedback forms from that restricted frame",
        "the proportion of all search attempts ending in successful retrieval",
        "the proportion of the 450 sampled forms whose submitters report success",
        "The prompt appears only after a post-search success event, so failed searches have no route into the frame; response among downloaders can add further self-selection.",
        "Sample search attempts at initiation, invite feedback whether or not a download occurs, and link one response opportunity to each selected attempt.",
    ),
]


COVERAGE_CLAIMS = [
    (
        "Education levels among football supporters",
        "A professional-networking platform reports that 64% of the profiles that name Northport FC as a favorite club also report a university degree. A headline turns this into the claim that 64% of all Northport FC supporters have a university degree.",
        "all people who support Northport FC",
        "platform members who name Northport FC on a visible profile and report education information",
        "Supporters who do not use the professional platform, do not name a club, or omit education have no route into the percentage. Platform membership is also related to education and employment.",
        "Among the analyzed platform profiles that named Northport FC and reported education, 64% reported a university degree.",
        "define supporter status first, sample supporters through a frame that is not tied to professional-platform membership, and follow up selected nonrespondents",
    ),
    (
        "Reading habits from an e-reader community",
        "An e-reader forum finds that 71% of 2 400 responding members finish at least two books per month. A post describes 71% as the rate for all adults in the country.",
        "all adults in the country",
        "members of the e-reader forum who saw the invitation and chose to respond",
        "Adults who do not use e-readers or the forum are absent, and highly engaged readers are especially likely to join and answer.",
        "Among responding members of this e-reader forum, 71% reported finishing at least two books per month.",
        "draw a probability sample from a population-based adult frame and offer several response modes",
    ),
    (
        "Cycling frequency from a route-planning app",
        "A cycling app reports that 58% of active users record at least three rides per week. The result is presented as the share of city residents who cycle that often.",
        "all residents of the city",
        "active users of the cycling app who allow ride recording",
        "Residents who do not cycle, do not use the app, or disable recording are missing, while frequent cyclists are more likely to remain active users.",
        "Among active app users with ride recording enabled, 58% recorded at least three rides per week.",
        "sample residents from a city register and measure cycling frequency whether or not they use an app",
    ),
    (
        "Museum interest from newsletter subscribers",
        "A museum newsletter survey finds that 82% of respondents plan to visit a new exhibition. The museum describes this as the level of interest among all regional residents.",
        "all residents of the region",
        "museum newsletter subscribers who opened the message and completed the survey",
        "People already interested in the museum are more likely to subscribe, open the message, and answer the survey.",
        "Among newsletter subscribers who answered, 82% said that they planned to visit the exhibition.",
        "sample regional residents independently of newsletter subscription and record nonresponse",
    ),
    (
        "Remote-work preference from a coworking platform",
        "A coworking platform reports that 76% of responding account holders prefer remote work on most weekdays. A news item attributes that preference to all employed adults.",
        "all employed adults in the target region",
        "account holders on the coworking platform who received and answered its poll",
        "The platform overrepresents people whose jobs can be done remotely, and volunteers with strong preferences may answer more often.",
        "Among responding account holders on this coworking platform, 76% preferred remote work on most weekdays.",
        "sample employed adults across occupations and work arrangements from a suitable labor-force frame",
    ),
    (
        "Language use from public profile fields",
        "A social platform counts the languages listed on 50 000 public profiles and concludes that 43% of the country's population uses three languages every day.",
        "all residents of the country",
        "platform members with public profiles who chose to list at least one language",
        "Platform access and public-profile choices differ across residents, and listing a language does not establish daily use.",
        "Of the public profiles with a language field in the analyzed platform data, 43% listed at least three languages.",
        "sample residents through a population frame and ask a clearly defined question about everyday language use",
    ),
    (
        "Student wellbeing from a study-planner app",
        "A study-planner app finds that 61% of its respondents report high academic stress and treats this as an estimate for every university student.",
        "all students enrolled at the universities of interest",
        "users of the study-planner app who noticed and answered the wellbeing prompt",
        "Students who use a planning app may differ in workload or organization, and willingness to answer may be connected with current stress.",
        "Among app users who answered the prompt, 61% reported high academic stress.",
        "sample from complete enrollment lists and contact the selected students through more than one mode",
    ),
    (
        "Concert attendance from ticket-account profiles",
        "A ticketing company observes that 67% of accounts followed at least one concert page last year and concludes that 67% of all residents attended a concert.",
        "all residents in the target population",
        "registered ticketing accounts with observable page-following activity",
        "Residents without accounts are absent, one person can hold several accounts, and following a page is not the same outcome as attending a concert.",
        "Among the observed ticketing accounts, 67% followed at least one concert page last year.",
        "sample people rather than accounts and ask or verify a clearly defined attendance outcome",
    ),
    (
        "Public-transport satisfaction from a mobile-ticket sample",
        "A transport operator finds 74% satisfaction among users who bought mobile tickets and presents it as satisfaction among all passengers.",
        "all passengers using the transport system in the target period",
        "passengers who purchased a mobile ticket and received the in-app question",
        "Cash, paper-ticket, pass, and accessibility-service users cannot enter the frame, and satisfaction may influence whether the prompt is answered.",
        "Among mobile-ticket users who answered the in-app question, 74% reported being satisfied.",
        "sample trips across ticket types, routes, and times, then invite the selected passengers through accessible response routes",
    ),
    (
        "Volunteer participation from organization websites",
        "Profiles on the websites of large charities show that 69% of listed volunteers contribute every month. The figure is reported as the rate for all volunteers in the region.",
        "all formal and informal volunteers in the region",
        "volunteers publicly listed by the large charities included in the web search",
        "Informal volunteers, small organizations, and volunteers without public profiles are missing, while regular contributors are more likely to be featured.",
        "Among volunteers publicly listed by the included large charities, 69% were described as contributing every month.",
        "construct a broader frame across organization sizes and informal community work, then sample volunteers within it",
    ),
]


SURVIVOR_SELECTION = [
    (
        "Damage patterns on returned delivery drones",
        "Engineers inspect only delivery drones that returned to base and notice many marks on the outer casing but few near the navigation unit. They must decide which area most needs added protection.",
        "drones that were damaged yet still returned and could be inspected",
        "drones that failed to return, including any whose navigation units were critically damaged",
        "Damage to a navigation unit may prevent return, so the low observed mark count there can signal severe selection rather than safety.",
        "investigate failed-flight logs and recovered nonreturning drones before deciding where reinforcement is most valuable",
    ),
    (
        "Study habits among course completers",
        "A course team interviews only students who completed a difficult online course and finds that most used weekly planning sheets. It concludes that planning sheets describe the habits of everyone who enrolled.",
        "enrollees who remained through completion and agreed to be interviewed",
        "students who withdrew, stopped logging in, or did not agree to the interview",
        "Planning habits can be connected with persistence, so conditioning on completion can make the observed habit unusually common.",
        "follow the original enrollment cohort and collect comparable information from completers and noncompleters",
    ),
    (
        "Reliability among devices still in service",
        "A laboratory examines sensors that remain in service after two years and finds very little corrosion. It concludes that the original sensor model rarely corrodes.",
        "sensors that survived in service for two years and were still available for inspection",
        "sensors removed, discarded, or replaced earlier, possibly because corrosion caused failure",
        "The outcome of interest can determine whether a sensor remains observable, leaving the least damaged units in the inspected group.",
        "use maintenance and replacement records for the full original sensor cohort, including failed units",
    ),
    (
        "Satisfaction among returning museum visitors",
        "A museum surveys people on their fifth visit and finds very high satisfaction. It uses the result to describe everyone who ever visited the museum.",
        "visitors who were satisfied or motivated enough to return at least four times and attend again",
        "one-time visitors and people who decided not to return",
        "Past satisfaction can influence return, so selecting on a later visit filters out many less satisfied experiences.",
        "sample first-time visits and follow those visitors whether or not they return",
    ),
    (
        "Workload reports from retained employees",
        "A company asks employees who have stayed for five years about their first-year workload and concludes that the answers represent every person hired in that year.",
        "employees from the hiring cohort who remained for five years and responded",
        "employees who resigned, were dismissed, or could not be contacted after leaving",
        "First-year workload can affect leaving, so the retained employees may systematically report different experiences.",
        "collect workload information prospectively from the full hiring cohort and retain exit information",
    ),
    (
        "Recovery among follow-up clinic attendees",
        "A clinic estimates treatment recovery from patients who returned for the final follow-up appointment. Most of those attendees had recovered.",
        "treated patients who attended the final follow-up and supplied an outcome",
        "patients who missed follow-up because they worsened, recovered elsewhere, moved, or disengaged",
        "Follow-up attendance may depend on recovery, so the observed percentage need not represent all treated patients.",
        "trace the full treated cohort and use several appropriate ways to obtain outcomes from missed appointments",
    ),
    (
        "Durability among surviving archive files",
        "An archive checks digital files that can still be opened after ten years and finds that nearly all have intact metadata. It concludes that the original collection preserved metadata well.",
        "files that survived, remained discoverable, and could still be opened",
        "lost, corrupted, or undiscoverable files whose metadata may have contributed to their disappearance",
        "Requiring a file to be findable and open can remove precisely the failures needed to assess preservation.",
        "audit the original file inventory and count missing and corrupted files as outcomes rather than excluding them",
    ),
    (
        "Confidence among competition finalists",
        "Researchers ask only finalists in a public-speaking competition about confidence before the first round and infer the confidence level of every entrant.",
        "entrants who advanced through every earlier round and reached the final",
        "entrants eliminated in earlier rounds or who withdrew",
        "Initial confidence can influence performance and withdrawal, so finalists form a selected subset of entrants.",
        "measure confidence for all entrants before the first round and retain their later competition status",
    ),
    (
        "Travel times from completed app routes",
        "A navigation app calculates average travel time using only trips marked complete. It excludes trips whose users closed the app before arrival.",
        "recorded trips that remained active until the app registered completion",
        "interrupted, abandoned, or exceptionally delayed trips whose app sessions ended early",
        "Long or problematic trips may be more likely to be closed early, which can make completed routes look faster.",
        "define every started trip as part of the cohort and investigate incomplete route records instead of silently dropping them",
    ),
    (
        "Reading progress among active subscribers",
        "An e-book service studies reading progress only among people whose subscription was still active after one year and reports the result for all original subscribers.",
        "subscribers who remained active for the full year and had readable progress data",
        "people who canceled or whose accounts became inactive during the year",
        "Reading engagement can affect cancellation, so active subscribers may display unusually high progress.",
        "retain the original subscriber cohort in the analysis and record progress up to cancellation or follow up former subscribers",
    ),
]


def _part_list(parts: list[str]) -> str:
    return "; ".join(f"({chr(97 + index)}) {part}" for index, part in enumerate(parts))


def varied_exercise(
    variant: int,
    setup: str,
    parts: list[str],
    reasoning: str,
) -> str:
    """Give parallel tasks genuinely different prose and information flow."""

    labeled = _part_list(parts)
    setup = setup.strip()
    separator = "\n\n" if "\n" in setup else " "
    styles = (
        f"{setup}{separator}Work through these requests: {labeled}. {reasoning}",
        f"{reasoning} Use this setting for the calculations:\n\n{setup}{separator}Report the following: {labeled}.",
        f"Consider the following information. {setup}{separator}Prepare a structured response that contains: {labeled}. {reasoning}",
        f"Use the setting below to build the analysis step by step. {setup}{separator}Begin with (a) {parts[0]}; then "
        + "; then ".join(f"({chr(98 + j)}) {part}" for j, part in enumerate(parts[1:]))
        + f". {reasoning}",
        f"Your goal is to connect the numerical work to its meaning. {setup}{separator}Address these items: {labeled}. {reasoning}",
        f"Start by reading the assumptions in this scenario. {setup}{separator}Without skipping intermediate reasoning, provide the following: {labeled}. {reasoning}",
        f"This problem has {len(parts)} linked parts. {setup}{separator}The required work is: {labeled}. Finish by doing the following: {reasoning}",
        f"Treat the stated model as the working model. {setup}{separator}Separate your answer into these parts: {labeled}. {reasoning}",
        f"Before calculating, note what is given and what is conditional or model-based. {setup}{separator}Now answer: {labeled}. {reasoning}",
        f"{setup}{separator}Write a concise analysis with the following components:\n\n"
        + "\n".join(f"- ({chr(97 + j)}) {part}" for j, part in enumerate(parts))
        + f"\n\n{reasoning}",
    )
    craft_notes = (
        "Place each rule next to the result it supports.",
        "Make clear which information is given and which quantity is derived.",
        "Use complete explanatory sentences around the notation.",
        "Check every step against the assumptions stated in the scenario.",
        "Interpret the result rather than merely repeating its numerical value.",
        "Show enough working that another learner could reproduce the argument.",
        "End with a brief check that the result answers the original question.",
        "Distinguish model assumptions from conclusions produced by the model.",
        "State relevant event definitions or measurement units explicitly.",
        "Keep the subpart labels aligned with the requested outputs.",
    )
    return f"{styles[variant - 1]} {craft_notes[variant - 1]}"


def varied_exercise_localized(
    locale: str,
    variant: int,
    setup: str,
    parts: list[str],
    reasoning: str,
) -> str:
    """Apply parallel but natural task framing without changing task data."""

    if locale not in ("de", "sq"):
        raise ValueError(f"unsupported localized exercise locale: {locale}")
    labeled = "; ".join(
        f"({chr(97 + index)}) {part}" for index, part in enumerate(parts)
    )
    setup = setup.strip()
    separator = "\n\n" if "\n" in setup else " "
    if locale == "de":
        styles = (
            f"{setup}{separator}Bearbeite diese Aufträge: {labeled}. {reasoning}",
            f"{reasoning} Verwende für die Berechnungen folgende Situation:\n\n{setup}{separator}Berichte: {labeled}.",
            f"Betrachte die folgenden Angaben. {setup}{separator}Erstelle eine gegliederte Antwort mit diesen Bestandteilen: {labeled}. {reasoning}",
            f"Baue die Analyse mit der folgenden Situation Schritt für Schritt auf. {setup}{separator}Beginne mit (a) {parts[0]}; danach "
            + "; danach ".join(
                f"({chr(98 + index)}) {part}"
                for index, part in enumerate(parts[1:])
            )
            + f". {reasoning}",
            f"Verbinde die Rechnung mit ihrer Bedeutung. {setup}{separator}Bearbeite: {labeled}. {reasoning}",
            f"Lies zuerst die Annahmen der Situation. {setup}{separator}Zeige ohne ausgelassene Zwischenschritte: {labeled}. {reasoning}",
            f"Diese Aufgabe besitzt {len(parts)} zusammenhängende Teile. {setup}{separator}Gefordert sind: {labeled}. Schliesse mit Folgendem ab: {reasoning}",
            f"Verwende das angegebene Modell als Arbeitsmodell. {setup}{separator}Gliedere deine Antwort in: {labeled}. {reasoning}",
            f"Halte vor dem Rechnen fest, was gegeben, bedingt oder modellbasiert ist. {setup}{separator}Beantworte nun: {labeled}. {reasoning}",
            f"{setup}{separator}Schreibe eine kurze Analyse mit folgenden Bestandteilen:\n\n"
            + "\n".join(
                f"- ({chr(97 + index)}) {part}"
                for index, part in enumerate(parts)
            )
            + f"\n\n{reasoning}",
        )
        craft_notes = (
            "Setze jede Regel unmittelbar neben das Ergebnis, das sie begründet.",
            "Zeige klar, welche Angaben gegeben und welche Grössen daraus hergeleitet sind.",
            "Ergänze die Notation mit vollständigen erklärenden Sätzen.",
            "Prüfe jeden Schritt anhand der Annahmen in der Situation.",
            "Interpretiere das Ergebnis, statt nur seinen Zahlenwert zu wiederholen.",
            "Zeige genug Rechenweg, damit eine andere lernende Person die Argumentation nachvollziehen kann.",
            "Prüfe am Schluss kurz, ob das Ergebnis die ursprüngliche Frage beantwortet.",
            "Unterscheide Modellannahmen von Schlussfolgerungen, die das Modell liefert.",
            "Nenne die relevanten Ereignisdefinitionen oder Messeinheiten ausdrücklich.",
            "Halte die Kennzeichnungen der Teilaufgaben und der verlangten Ergebnisse deckungsgleich.",
        )
    else:
        styles = (
            f"{setup}{separator}Puno me këto kërkesa: {labeled}. {reasoning}",
            f"{reasoning} Përdor këtë situatë për llogaritjet:\n\n{setup}{separator}Raporto: {labeled}.",
            f"Shqyrto të dhënat vijuese. {setup}{separator}Përgatit një përgjigje të strukturuar që përmban: {labeled}. {reasoning}",
            f"Ndërtoje analizën hap pas hapi nga situata e mëposhtme. {setup}{separator}Fillo me (a) {parts[0]}; pastaj "
            + "; pastaj ".join(
                f"({chr(98 + index)}) {part}"
                for index, part in enumerate(parts[1:])
            )
            + f". {reasoning}",
            f"Lidhe llogaritjen me kuptimin e saj. {setup}{separator}Trajto këto pika: {labeled}. {reasoning}",
            f"Lexo fillimisht supozimet e situatës. {setup}{separator}Pa kapërcyer arsyetimin ndërmjetës, jep: {labeled}. {reasoning}",
            f"Kjo detyrë ka {len(parts)} pjesë të lidhura. {setup}{separator}Kërkohet: {labeled}. Në fund bëj edhe këtë: {reasoning}",
            f"Përdore modelin e dhënë si model pune. {setup}{separator}Ndaje përgjigjen në këto pjesë: {labeled}. {reasoning}",
            f"Para llogaritjes, dallo çfarë është dhënë dhe çfarë është e kushtëzuar ose e bazuar në model. {setup}{separator}Tani përgjigju: {labeled}. {reasoning}",
            f"{setup}{separator}Shkruaj një analizë të shkurtër me këto pjesë:\n\n"
            + "\n".join(
                f"- ({chr(97 + index)}) {part}"
                for index, part in enumerate(parts)
            )
            + f"\n\n{reasoning}",
        )
        craft_notes = (
            "Vendose çdo rregull pranë rezultatit që ai mbështet.",
            "Dallo qartë cilat të dhëna jepen dhe cila madhësi nxirret prej tyre.",
            "Shoqëroje simbolikën me fjali të plota shpjeguese.",
            "Kontrolloje çdo hap kundrejt supozimeve të situatës.",
            "Interpretoje rezultatin, mos përsërit vetëm vlerën numerike.",
            "Trego aq punë sa një student tjetër ta riprodhojë arsyetimin.",
            "Në fund kontrollo shkurt nëse rezultati i përgjigjet pyetjes fillestare.",
            "Dallo supozimet e modelit nga përfundimet që jep modeli.",
            "Përcakto shprehimisht ngjarjet ose njësitë matëse përkatëse.",
            "Mbaji etiketat e nënpjesëve në të njëjtin rend si rezultatet e kërkuara.",
        )
    return f"{styles[variant - 1]} {craft_notes[variant - 1]}"


def quantile_sign(probability: float) -> str:
    if probability < 0.5:
        return "negative"
    if probability > 0.5:
        return "positive"
    return "zero"


def document_header(document_type: str) -> str:
    title = "Exercise Sheet" if document_type == "exercises" else "Complete Solutions"
    pair = "solutions" if document_type == "exercises" else "exercises"
    return f'''---
title: "{title}"
subtitle: "Probability"
document-id: "topic-02-probability-{document_type}-en"
topic-id: "topic-02-probability"
topic-number: "02"
topic-slug: "probability"
document-type: "{document_type}"
locale: "en"
paired-document-id: "topic-02-probability-{pair}-en"
---

'''


def render_english() -> tuple[str, str]:
    exercises = [document_header("exercises")]
    solutions = [document_header("solutions")]
    exercises.append(
        "This sheet contains 160 exercises organized into 16 learning-objective groups. Work through each exercise before consulting its matching complete solution. Show the probability rule, substituted values, relevant units, and a short interpretation.\n\n"
    )
    solutions.append(
        "These solutions follow the Exercise Sheet identifiers exactly. Probabilities are rounded to four decimal places; small differences caused by retaining more intermediate digits are acceptable.\n\n"
    )

    # A01: sequential conditional probability
    exercises.append(heading(1, "Sequential Conditional Probability"))
    solutions.append(heading(1, "Sequential Conditional Probability"))
    for i, ((title, first, second, third), (p1, p2, p3)) in enumerate(zip(STAGE_CONTEXTS, STAGE_PROBABILITIES), 1):
        setup = (
            f"Success requires three ordered stages: first, {first}; second, {second}; and third, {third}. "
            f"The first-stage success probability is {number(p1, 2)}. Among those who clear stage one, "
            f"the second-stage success probability is {number(p2, 2)}. Among those who clear both, the "
            f"third-stage success probability is {number(p3, 2)}."
        )
        prompt = varied_exercise(
            i,
            setup,
            [
                "find the probability of completing stages one and two",
                "find the probability of completing the full three-stage sequence",
                "find the probability of completing the first two stages but failing the third",
            ],
            "Define events for the stages and explain why the multiplication uses conditional rather than unrelated marginal probabilities.",
        )
        exercises.append(task(2, 1, i, title, prompt))
        p12, p123, p12not3 = p1*p2, p1*p2*p3, p1*p2*(1-p3)
        solutions.append(task(2, 1, i, title, f"Let $A$, $B$, and $C$ denote success at the three stages in order. (a) By the chain rule, $P(A\\cap B)=P(A)P(B\\mid A)={number(p1,2)}\\times {number(p2,2)}={number(p12)}$. (b) $P(A\\cap B\\cap C)=P(A)P(B\\mid A)P(C\\mid A\\cap B)={number(p1,2)}\\times {number(p2,2)}\\times {number(p3,2)}={number(p123)}$. Thus the model says that a proportion {number(p123)} will complete the entire sequence ending with “{third}.” (c) Conditional on the first two successes, failure at the third stage has probability $1-{number(p3,2)}={number(1-p3,2)}$. Therefore $P(A\\cap B\\cap C')={number(p1,2)}\\times {number(p2,2)}\\times {number(1-p3,2)}={number(p12not3)}$, the modeled proportion who reach the third stage but do not complete it. The later-stage probabilities refer to groups already restricted by earlier success, so replacing them with unrelated marginal probabilities would discard the conditions in the scenario."))

    # A02: independence
    exercises.append(heading(2, "Independent Joint Events"))
    solutions.append(heading(2, "Independent Joint Events"))
    for i, ((title, a, b), (pa, pb)) in enumerate(zip(INDEPENDENT_CONTEXTS, INDEPENDENT_PROBABILITIES), 1):
        setup = (
            f"Let event $A$ be that {a}, with $P(A)={number(pa,2)}$. Let event $B$ be that {b}, "
            f"with $P(B)={number(pb,2)}$. Assume $A$ and $B$ are independent."
        )
        prompt = varied_exercise(
            i,
            setup,
            [
                "calculate the probability that both events occur",
                "calculate the probability that at least one event occurs",
                "calculate the probability that $A$ occurs while $B$ does not",
            ],
            "Name the rule used in each part and identify exactly which product calculations depend on independence.",
        )
        exercises.append(task(2, 2, i, title, prompt))
        both = pa*pb
        union = pa+pb-both
        only_a = pa*(1-pb)
        solutions.append(task(2, 2, i, title, f"Independence permits $P(A\\cap B)=P(A)P(B)={number(pa,2)}\\times {number(pb,2)}={number(both)}$. This is the modeled probability that {a} and {b}. For (b), the general addition rule gives $P(A\\cup B)={number(pa,2)}+{number(pb,2)}-{number(both)}={number(union)}$, the probability that at least one of those events occurs. For (c), independence of $A$ and $B$ also gives independence of $A$ and $B'$, so $P(A\\cap B')={number(pa,2)}(1-{number(pb,2)})={number(only_a)}$. Independence is used to replace joint probabilities with products; the addition rule itself is valid whether or not the events are independent."))

    # A03: contingency tables
    exercises.append(heading(3, "Contingency Tables and Event Relationships"))
    solutions.append(heading(3, "Contingency Tables and Event Relationships"))
    for i, (title, g1, g2, yes, no, a, b, c, d) in enumerate(TABLE_CONTEXTS, 1):
        n = a+b+c+d
        setup = f"""The observed sample is summarized below.

| Group | {yes} | {no} | Total |
|---|---:|---:|---:|
| {g1} | {a} | {b} | {a+b} |
| {g2} | {c} | {d} | {c+d} |
| Total | {a+c} | {b+d} | {n} |

Let $G$ denote membership in the {g1} row and let $Y$ denote the {yes} outcome. The {g2} row is $G^c$."""
        prompt = varied_exercise(
            i,
            setup,
            [
                "find $P(Y\\mid G)$ and $P(Y\\mid G^c)$, then decide whether the variables are independent in the empirical distribution",
                "find the joint probability $P(G\\cap Y)$",
                "decide whether $G$ and $Y$ are disjoint events",
            ],
            "Explain why an exact relationship in these sample counts is not, by itself, a conclusion about an unsampled population.",
        )
        exercises.append(task(2, 3, i, title, prompt))
        p1, p2, joint = a/(a+b), c/(c+d), a/n
        independent = abs(p1-p2) < 1e-12
        decision = "equal, so the variables are independent in this empirical table" if independent else "different, so the variables are not independent in this empirical table"
        solutions.append(task(2, 3, i, title, f"(a) $P(Y\\mid G)={a}/{a+b}={number(p1)}$ for the {g1} row, while $P(Y\\mid G^c)={c}/{c+d}={number(p2)}$ for the {g2} row. These conditional proportions are {decision}. This is a descriptive statement about the displayed empirical distribution, not proof that the same relationship holds in a wider population. (b) The intersection of {g1} and {yes} contains {a} of the {n} observations, so $P(G\\cap Y)={a}/{n}={number(joint)}$. (c) $G$ and $Y$ are not disjoint because that intersection is nonempty. Disjoint events would have an intersection count of zero."))

    # A04: Bayes and base rates
    exercises.append(heading(4, "Bayes' Theorem and Base Rates"))
    solutions.append(heading(4, "Bayes' Theorem and Base Rates"))
    for i, (title, condition, sens, spec, prev1, prev2) in enumerate(BAYES_CONTEXTS, 1):
        setup = (
            f"A hypothetical screening tool is used to detect {condition}. Its sensitivity is {number(sens,2)}, "
            f"and its specificity is {number(spec,2)}. Let $D$ mean that the condition is truly present and $+$ mean a positive result."
        )
        prompt = varied_exercise(
            i,
            setup,
            [
                f"calculate $P(D\\mid +)$ when prevalence is {number(prev1*100,0)}%",
                f"recalculate $P(D\\mid +)$ when prevalence is {number(prev2*100,0)}%",
                "compare the posterior probabilities and explain the base-rate effect",
            ],
            "For each prevalence, show the true-positive and false-positive paths, and explain why sensitivity alone is not the requested posterior probability.",
        )
        exercises.append(task(2, 4, i, title, prompt))
        vals=[]
        for prev in (prev1,prev2):
            tp=sens*prev; fp=(1-spec)*(1-prev); vals.append((tp,fp,tp/(tp+fp)))
        solutions.append(task(2, 4, i, title, f"The false-positive probability is $1-{number(spec,2)}={number(1-spec,2)}$. (a) At prevalence {number(prev1,2)}, the positive-result paths are $P(+\\cap D)={number(sens,2)}\\times {number(prev1,2)}={number(vals[0][0])}$ and $P(+\\cap D')={number(1-spec,2)}\\times {number(1-prev1,2)}={number(vals[0][1])}$. Thus $P(D\\mid +)={number(vals[0][0])}/({number(vals[0][0])}+{number(vals[0][1])})={number(vals[0][2])}$. (b) At prevalence {number(prev2,2)}, the corresponding paths are {number(vals[1][0])} and {number(vals[1][1])}, giving $P(D\\mid +)={number(vals[1][0])}/({number(vals[1][0])}+{number(vals[1][1])})={number(vals[1][2])}$. This posterior is the chance that the condition described as “{condition}” is truly present after a positive result. Sensitivity instead conditions on the condition already being present. The higher base rate raises the share of positive results that are true positives."))

    # A05: discrete distributions
    exercises.append(heading(5, "Discrete Expectation, Variance, PMF, and CDF"))
    solutions.append(heading(5, "Discrete Expectation, Variance, PMF, and CDF"))
    for i, (title, xs, ps) in enumerate(DISCRETE_DISTRIBUTIONS, 1):
        cells = " | ".join(str(x) for x in xs)
        probs = " | ".join(number(p,2) for p in ps)
        description = title[0].lower() + title[1:]
        setup = f"""Let $X$ represent the count described as “{description}.” Its proposed distribution is:

| $x$ | {cells} |
|---|---:|---:|---:|---:|
| $P(X=x)$ | {probs} |"""
        prompt = varied_exercise(
            i,
            setup,
            [
                "verify that the table is a valid probability mass function",
                "calculate $E(X)$ and $\\operatorname{Var}(X)$, using $E(X^2)-[E(X)]^2$ for the variance",
                "give $F(x)$ at every support point",
            ],
            "Describe how the PMF and CDF plots differ, and interpret the expectation in the context named above.",
        )
        exercises.append(task(2, 5, i, title, prompt))
        mean=sum(x*p for x,p in zip(xs,ps)); ex2=sum(x*x*p for x,p in zip(xs,ps)); var=ex2-mean*mean
        cdf=[]; running=0.0
        for x,p in zip(xs,ps): running+=p; cdf.append(f"$F({x})={number(running,2)}$")
        mean_terms="+".join(f"{x}({number(p,2)})" for x,p in zip(xs,ps))
        ex2_terms="+".join(f"{x}^2({number(p,2)})" for x,p in zip(xs,ps))
        solutions.append(task(2, 5, i, title, f"(a) All masses are nonnegative and their sum is {'+'.join(number(p,2) for p in ps)}={number(sum(ps),2)}, so the table is a valid PMF. (b) $E(X)=\\sum xP(X=x)={mean_terms}={number(mean)}$. Across many comparable observations, the long-run average {description} would approach {number(mean)}. Next, $E(X^2)={ex2_terms}={number(ex2)}$, so $\\operatorname{{Var}}(X)={number(ex2)}-{number(mean)}^2={number(var)}$; this variance is expressed in squared count units. (c) The cumulative values are {', '.join(cdf)}. A PMF plot places a separate bar or point mass at each support value. A CDF is instead a nondecreasing, right-continuous step function that accumulates those masses and ends at 1."))

    # A06: exact binomial probabilities
    exercises.append(heading(6, "Exact Binomial Probabilities"))
    solutions.append(heading(6, "Exact Binomial Probabilities"))
    for i, (title, units, success, n, p, k1, k2) in enumerate(BINOMIAL_EXACT,1):
        setup = (
            f"Consider {n} {units}. Treat them as independent trials, and suppose the probability that any one "
            f"{success} is constant at $\\pi={number(p,2)}$. Let $X$ count how many satisfy that success definition."
        )
        prompt = varied_exercise(
            i,
            setup,
            [
                f"calculate $P(X={k1})$",
                f"calculate $P(X={k2})$",
                "find $E(X)$ and $\\operatorname{Var}(X)$",
                "state the fixed-trial, binary-outcome, constant-probability, and independence assumptions in this setting",
            ],
            "Show the binomial coefficient and every substituted model value before rounding.",
        )
        exercises.append(task(2,6,i,title,prompt))
        q1=probability_binomial(n,p,k1);q2=probability_binomial(n,p,k2);ev=n*p;var=n*p*(1-p)
        solutions.append(task(2,6,i,title,f"The model is $X\\sim B({n},{number(p,2)})$. (a) $P(X={k1})=\\binom{{{n}}}{{{k1}}}{number(p,2)}^{{{k1}}}(1-{number(p,2)})^{{{n-k1}}}={number(q1)}$. This is the modeled probability that exactly {k1} of the {n} {units} meet the success definition. (b) $P(X={k2})=\\binom{{{n}}}{{{k2}}}{number(p,2)}^{{{k2}}}(1-{number(p,2)})^{{{n-k2}}}={number(q2)}$, the corresponding probability for exactly {k2}. (c) $E(X)=n\\pi={n}({number(p,2)})={number(ev)}$ and $\\operatorname{{Var}}(X)=n\\pi(1-\\pi)={n}({number(p,2)})({number(1-p,2)})={number(var)}$. Across repeated groups of {n}, the mean count would approach {number(ev)}. (d) The setting must keep the number of {units} fixed at {n}; classify each one only as success or failure according to whether it {success}; keep the success probability at {number(p,2)}; and make the trial outcomes independent. If any condition fails, this binomial calculation is not justified."))

    # A07: binomial complements
    exercises.append(heading(7, "Binomial Tail Probabilities by Complement"))
    solutions.append(heading(7, "Binomial Tail Probabilities by Complement"))
    for i,(label,units,success,n,p,k) in enumerate(BINOMIAL_TAIL,1):
        title=f"More than {k} {label[0].lower() + label[1:]}"
        setup = (
            f"Among {n} {units}, model the cases independently. For each one, the event that it {success} has "
            f"constant probability $\\pi={number(p,2)}$. Let $X$ be the total number of such events."
        )
        prompt = varied_exercise(
            i,
            setup,
            [
                f"identify the binomial model and the complement of $X>{k}$",
                f"use that complement to evaluate $P(X>{k})$, displaying every lower-tail term",
                "interpret the tail probability and compare the number of terms with a direct upper-tail sum",
            ],
            "Retain unrounded component probabilities until the final reported result.",
        )
        exercises.append(task(2,7,i,title,prompt))
        terms=[probability_binomial(n,p,x) for x in range(k+1)];cdf=sum(terms);tail=1-cdf
        symbolic="+".join(f"P(X={x})" for x in range(k+1))
        numeric="+".join(number(v) for v in terms)
        solutions.append(task(2,7,i,title,f"(a) Here $X\\sim B({n},{number(p,2)})$, and the complement of $X>{k}$ is $X\\leq {k}$. (b) Therefore $P(X>{k})=1-[{symbolic}]=1-[{numeric}]\\approx 1-{number(cdf)}={number(tail)}$. The approximation sign is necessary because the displayed component terms are rounded; the value {number(cdf)} was calculated from unrounded terms. (c) The model assigns probability {number(tail)} to seeing more than {k} successes among the {n} {units}, where one success means that one unit {success}. The complement uses {k+1} lower-tail terms, whereas a direct sum would require the values {k+1} through {n}."))

    # A08: PMF versus density
    exercises.append(heading(8, "Probability Mass Functions and Densities"))
    solutions.append(heading(8, "Probability Mass Functions and Densities"))
    for i,(discrete,continuous) in enumerate(PMF_DENSITY_CONTEXTS,1):
        title=f"From {discrete} to {continuous}"
        setup = (
            f"Define $X$ as {discrete}, a count, and define $Y$ as {continuous}, measured on a continuous scale. "
            "The two variables therefore require different probability representations."
        )
        prompt = varied_exercise(
            i,
            setup,
            [
                "identify which variable uses a PMF and which uses a density",
                "explain the point probability $P(X=x)$ and contrast it with $P(Y=y)$",
                "show how each variable obtains probability over an interval",
                "explain what a CDF records for both variables",
            ],
            "Use the geometry of mass, area, jumps, and accumulation rather than relying only on definitions.",
        )
        exercises.append(task(2,8,i,title,prompt))
        solutions.append(task(2,8,i,title,f"(a) Because $X$ records {discrete}, it has countable support and a PMF can assign mass $P(X=x)$ to each possible count. Because $Y$ is {continuous}, an ideal continuous model represents it with a density $f_Y(y)$. (b) $P(X=x)$ may be positive for one count, while $P(Y=y)=0$ at every exact point even when nearby values are plausible. (c) For $X$, an interval probability is the sum of its included masses. For $Y$, it is density area, for example $P(a<Y\\leq b)=\\int_a^b f_Y(y)\\,dy$. (d) In either case, a CDF records accumulated probability: $F_X(x)=P(X\\leq x)$ jumps at supported counts, whereas $F_Y(y)=P(Y\\leq y)$ accumulates area continuously under the density."))

    # A09: standard normal
    exercises.append(heading(9, "Standard-Normal Probabilities"))
    solutions.append(heading(9, "Standard-Normal Probabilities"))
    for i,(a,b,c,d) in enumerate(STANDARD_NORMAL,1):
        title=f"Standard-normal regions, set {i}"
        setup = "Let $Z\\sim N(0,1)$ and write $\\Phi(z)=P(Z\\leq z)$."
        prompt = varied_exercise(
            i,
            setup,
            [
                f"evaluate $P(Z\\leq {number(a,2)})$",
                f"evaluate $P(Z>{number(b,2)})$",
                f"evaluate $P({number(c,2)}<Z\\leq {number(d,2)})$",
            ],
            "For each probability, state which region of the normal curve would be shaded and name the complement or CDF-subtraction rule used.",
        )
        exercises.append(task(2,9,i,title,prompt))
        pa=probability_normal(a);pb=1-probability_normal(b);pc=probability_normal(d)-probability_normal(c)
        solutions.append(task(2,9,i,title,f"Write $\\Phi(z)=P(Z\\leq z)$. (a) $P(Z\\leq {number(a,2)})=\\Phi({number(a,2)})={number(pa)}$. Shade left of {number(a,2)}. (b) $P(Z>{number(b,2)})=1-\\Phi({number(b,2)})={number(pb)}$. Shade the right tail. (c) $P({number(c,2)}<Z\\leq {number(d,2)})=\\Phi({number(d,2)})-\\Phi({number(c,2)})={number(pc)}$. Shade between the two cutoffs. Boundary inclusions do not change probabilities for a continuous distribution."))

    # A10: general normal
    exercises.append(heading(10, "Probabilities for a General Normal Distribution"))
    solutions.append(heading(10, "Probabilities for a General Normal Distribution"))
    for i,(context,unit,mu,var,x1,x2) in enumerate(GENERAL_NORMAL,1):
        sd=math.sqrt(var); title=f"Modeling {context}"
        setup = (
            f"Suppose $X$ measures {context} in {unit} and follows $N({mu},{var})$, where the second "
            "parameter is the variance."
        )
        prompt = varied_exercise(
            i,
            setup,
            [
                f"standardize {x1} and find $P(X\\leq {x1})$",
                f"standardize {x2} and find $P(X>{x2})$",
                "identify each shaded region and interpret both probabilities in context",
            ],
            "Keep the unrounded z-scores for the probability calculations and round only the reported results.",
        )
        exercises.append(task(2,10,i,title,prompt))
        z1=(x1-mu)/sd;z2=(x2-mu)/sd;p1=probability_normal(z1);p2=1-probability_normal(z2)
        solutions.append(task(2,10,i,title,f"The standard deviation is $\\sigma=\\sqrt{{{var}}}={number(sd,2)}$. (a) $z=({x1}-{mu})/{number(sd,2)}\\approx {number(z1)}$. Retaining the unrounded quotient gives $P(X\\leq {x1})=\\Phi(({x1}-{mu})/{number(sd,2)})={number(p1)}$. Thus the model places proportion {number(p1)} of {context} values at or below {x1} {unit}; shade the left side of that cutoff. (b) $z=({x2}-{mu})/{number(sd,2)}\\approx {number(z2)}$, and $P(X>{x2})=1-\\Phi(({x2}-{mu})/{number(sd,2)})={number(p2)}$. This is the modeled proportion above {x2} {unit}, represented by the right tail. Both interpretations depend on the stated normal model."))

    # A11: inverse normal
    exercises.append(heading(11, "Inverse Standard-Normal Quantiles"))
    solutions.append(heading(11, "Inverse Standard-Normal Quantiles"))
    for i,(q1,q2) in enumerate(QUANTILES,1):
        title=f"Finding the {number(q1*100,0)}% and {number(q2*100,0)}% z-quantiles"
        setup = (
            f"For $Z\\sim N(0,1)$, one cumulative area is {number(q1,2)} and the other is {number(q2,2)}. "
            "The unknown quantities are the z-axis cutoffs, not the probabilities."
        )
        prompt = varied_exercise(
            i,
            setup,
            [
                f"find $z_{{{number(q1*100,0)}\\%}}$ such that $P(Z\\leq z)={number(q1,2)}$",
                f"find $z_{{{number(q2*100,0)}\\%}}$ such that $P(Z\\leq z)={number(q2,2)}$",
            ],
            "Predict each cutoff's sign from its position relative to 0.50, then explain why this is an inverse rather than a forward CDF calculation.",
        )
        exercises.append(task(2,11,i,title,prompt))
        # Python's standard library has no inverse CDF; use a stable bisection.
        def inv(q):
            lo,hi=-8.0,8.0
            for _ in range(100):
                mid=(lo+hi)/2
                if probability_normal(mid)<q: lo=mid
                else: hi=mid
            return (lo+hi)/2
        z1,z2=inv(q1),inv(q2)
        if abs(z1) < 0.00005:
            z1 = 0.0
        if abs(z2) < 0.00005:
            z2 = 0.0
        sign1=quantile_sign(q1); sign2=quantile_sign(q2)
        solutions.append(task(2,11,i,title,f"A quantile begins with cumulative probability $q$ and solves $\\Phi(z)=q$ for a location. (a) $\\Phi(z)={number(q1,2)}$ gives $z_{{{number(q1*100,0)}\\%}}={number(z1)}$. Because {number(q1,2)} is {'below' if q1 < 0.5 else 'above' if q1 > 0.5 else 'equal to'} 0.50, this cutoff is {sign1}. (b) $\\Phi(z)={number(q2,2)}$ gives $z_{{{number(q2*100,0)}\\%}}={number(z2)}$; its expected sign is {sign2}. The inputs are areas and the outputs are positions on the z-axis, which reverses an ordinary forward CDF calculation."))

    # A12: sampling distributions
    exercises.append(heading(12, "Sampling Distribution of the Mean"))
    solutions.append(heading(12, "Sampling Distribution of the Mean"))
    for i,(context,unit,mu,var,n,newvar,newn) in enumerate(SAMPLING,1):
        title=f"Precision of a sample mean for {context}"
        sd=math.sqrt(var);se=sd/math.sqrt(n);sevar=math.sqrt(newvar)/math.sqrt(n);sen=sd/math.sqrt(newn)
        setup = (
            f"A population variable measuring {context} in {unit} has mean $\\mu={mu}$ and variance "
            f"$\\sigma^2={var}$. Consider samples containing $n={n}$ independent observations from this population."
        )
        prompt = varied_exercise(
            i,
            setup,
            [
                "find $E(\\bar X)$ and $\\operatorname{SD}(\\bar X)$",
                f"find the standard error if the population variance changes to {newvar} while $n={n}$",
                f"find the standard error if variance remains {var} but sample size changes to $n={newn}$",
            ],
            "Explain separately how population variability and sample size change the precision of the sample mean.",
        )
        exercises.append(task(2,12,i,title,prompt))
        variance_direction = "larger" if newvar > var else "smaller"
        variance_effect = "increases" if sevar > se else "decreases"
        sample_direction = "larger" if newn > n else "smaller"
        sample_effect = "decreases" if sen < se else "increases"
        solutions.append(task(2,12,i,title,f"For an unbiased sample mean, $E(\\bar X)=\\mu={mu}$. Independence gives $\\operatorname{{SD}}(\\bar X)=\\sigma/\\sqrt n$. (a) $\\sigma=\\sqrt{{{var}}}={number(sd,2)}$, so $\\operatorname{{SE}}={number(sd,2)}/\\sqrt{{{n}}}={number(se)}$ {unit}. Across repeated samples, their means are centered at {mu} {unit} with standard deviation {number(se)} {unit}. (b) With variance {newvar}, $\\operatorname{{SE}}=\\sqrt{{{newvar}}}/\\sqrt{{{n}}}={number(sevar)}$ {unit}. The {variance_direction} population variance {variance_effect} the SE relative to part (a). (c) With $n={newn}$, $\\operatorname{{SE}}=\\sqrt{{{var}}}/\\sqrt{{{newn}}}={number(sen)}$ {unit}. The {sample_direction} sample size {sample_effect} the SE through the square root of $n$. A smaller SE means that repeated sample means cluster more tightly around the population mean."))

    # A13: normal intervals
    exercises.append(heading(13, "Intervals under a Normal Model"))
    solutions.append(heading(13, "Intervals under a Normal Model"))
    for i,(context,unit,mu,var,a,b,c,d) in enumerate(NORMAL_INTERVALS,1):
        title=f"Interval probabilities for {context}"
        sd=math.sqrt(var);za=(a-mu)/sd;zb=(b-mu)/sd;zc=(c-mu)/sd;zd=(d-mu)/sd
        p1=probability_normal(zb)-probability_normal(za);p2=probability_normal(zd)-probability_normal(zc)
        setup = (
            f"Suppose $X$ measures {context} in {unit} and follows $N({mu},{var})$, where the second "
            "parameter is the variance."
        )
        prompt = varied_exercise(
            i,
            setup,
            [
                f"calculate $P({a}<X\\leq {b})$",
                f"calculate $P({c}<X\\leq {d})$",
            ],
            "For both intervals, standardize each endpoint, subtract CDF values in the correct order, and interpret the result as a modeled proportion.",
        )
        exercises.append(task(2,13,i,title,prompt))
        solutions.append(task(2,13,i,title,f"The standard deviation is $\\sigma=\\sqrt{{{var}}}={number(sd,2)}$. (a) The endpoints are $z_a=({a}-{mu})/{number(sd,2)}\\approx {number(za)}$ and $z_b=({b}-{mu})/{number(sd,2)}\\approx {number(zb)}$. Using the unrounded z-scores, $P({a}<X\\leq {b})=\\Phi(({b}-{mu})/{number(sd,2)})-\\Phi(({a}-{mu})/{number(sd,2)})={number(p1)}$. The model therefore places proportion {number(p1)} of {context} values between {a} and {b} {unit}. (b) $z_c=({c}-{mu})/{number(sd,2)}\\approx {number(zc)}$ and $z_d=({d}-{mu})/{number(sd,2)}\\approx {number(zd)}$, giving $P({c}<X\\leq {d})=\\Phi(({d}-{mu})/{number(sd,2)})-\\Phi(({c}-{mu})/{number(sd,2)})={number(p2)}$. This is the modeled proportion between {c} and {d} {unit}. Endpoint inclusion does not affect a continuous-model probability."))

    # A14: sampling bias
    exercises.append(heading(14, "Population, Sample, and Selection Bias"))
    solutions.append(heading(14, "Population, Sample, and Selection Bias"))
    for i,(title,scenario,pop,frame,sample,param,stat,biases,design) in enumerate(SAMPLING_BIAS,1):
        prompt = varied_exercise(
            i,
            scenario,
            [
                "identify the target population",
                "distinguish the operational sampling frame from the achieved sample",
                "state a population parameter that matches the research claim",
                "state the corresponding sample statistic and its observational unit",
            ],
            "Explain at least two scenario-specific coverage, selection, or nonresponse mechanisms; state what a larger sample would and would not repair; and propose a more defensible design.",
        )
        exercises.append(task(2,14,i,title,prompt))
        solutions.append(task(2,14,i,title,f"(a) The target population is {pop}. (b) The operational sampling frame is {frame}. The achieved sample is {sample}. Keeping these separate matters because the frame describes who or what had a route to selection, whereas the sample contains the units actually observed. (c) A matching population parameter is {param}. (d) The sample statistic is {stat}. The main threats are specific to this design: {biases} A larger sample obtained through the same mechanism would reduce random sampling variability around that mechanism's frame-specific value, but it would not repair the systematic coverage or selection mechanisms just identified. A more defensible approach is to {design[0].lower() + design[1:]}"))

    # A15: coverage error in claims based on restricted profiles or platforms
    exercises.append(heading(15, "Coverage Error and the Population Behind a Percentage"))
    solutions.append(heading(15, "Coverage Error and the Population Behind a Percentage"))
    for i,(title,claim,target,observed,coverage,honest,design) in enumerate(COVERAGE_CLAIMS,1):
        prompt = varied_exercise(
            i,
            claim,
            [
                "state the population named in the broad claim",
                "identify the units that actually had a route into the reported percentage",
                "explain why the observed frame does not cover the named population",
                "rewrite the result so that it describes only the observed data",
            ],
            "Then propose a sampling design that would match the broad population more closely, and explain why simply collecting more observations through the same restricted frame would not solve the problem.",
        )
        exercises.append(task(2,15,i,title,prompt))
        solutions.append(task(2,15,i,title,f"(a) The broad claim names {target}. (b) The units with a route into the calculation are {observed}. (c) This creates coverage error because {coverage[0].lower() + coverage[1:]} The percentage can be calculated correctly for the observed records and still fail to estimate the percentage in the broader population. (d) An honest descriptive statement is: \"{honest}\" A more defensible study would {design}. Increasing the number of records drawn through the same restricted route would make the restricted-frame percentage more precise, but would not add the kinds of people who never entered that frame."))

    # A16: survivorship and selection on continued observability
    exercises.append(heading(16, "Survivorship Bias and Missing Outcomes"))
    solutions.append(heading(16, "Survivorship Bias and Missing Outcomes"))
    for i,(title,scenario,observed,missing,distortion,action) in enumerate(SURVIVOR_SELECTION,1):
        prompt = varied_exercise(
            i,
            scenario,
            [
                "identify the cases that remain observable",
                "identify the relevant cases missing from the observed group",
                "explain how the outcome itself may influence whether a case is observed",
                "state why an analysis of the observed cases alone can point toward the wrong conclusion",
            ],
            "Finish by describing the additional evidence or follow-up needed before making the intended population claim.",
        )
        exercises.append(task(2,16,i,title,prompt))
        solutions.append(task(2,16,i,title,f"(a) The observed group contains {observed}. (b) Missing from that group are {missing}. (c) The selection process is tied to the outcome: {distortion} This is survivorship bias, meaning that continued availability is required for observation even though failure to remain available can itself carry important information. (d) Looking only at the observed cases conditions the analysis on survival, completion, return, or retention. It can therefore hide failures and reverse the practical lesson. The next step is to {action}. The goal is not to guess the missing results, but to redesign collection so both continuing and noncontinuing cases contribute evidence."))

    return "".join(exercises).rstrip()+"\n", "".join(solutions).rstrip()+"\n"


def render_localized(locale: str) -> tuple[list[str], list[str]]:
    """Render de-CH or Albanian from the canonical English task structure."""

    if locale not in ("de", "sq"):
        raise ValueError(f"unsupported localized locale: {locale}")
    is_de = locale == "de"
    exercises: list[str] = []
    solutions: list[str] = []

    if is_de:
        stage_contexts = i18n.DE_STAGE_CONTEXTS
        independent_contexts = i18n.DE_INDEPENDENT_CONTEXTS
        table_contexts = i18n.DE_TABLE_CONTEXTS
        bayes_contexts = i18n.DE_BAYES_CONTEXTS
    else:
        stage_contexts = i18n.SQ_STAGE_CONTEXTS
        independent_contexts = i18n.SQ_INDEPENDENT_CONTEXTS
        table_contexts = i18n.SQ_TABLE_CONTEXTS
        bayes_contexts = i18n.SQ_BAYES_CONTEXTS

    # A01: sequential conditional probability
    heading_text = (
        "Sequenzielle bedingte Wahrscheinlichkeit"
        if is_de
        else "Probabiliteti i kushtëzuar në një varg etapash"
    )
    exercises.append(heading(1, heading_text))
    solutions.append(heading(1, heading_text))
    for variant, ((title, first, second, third), (p1, p2, p3)) in enumerate(
        zip(stage_contexts, STAGE_PROBABILITIES), 1
    ):
        if is_de:
            setup = (
                f"Der Erfolg erfordert drei geordnete Schritte: zuerst {first}, danach {second} und schliesslich {third}. "
                f"Die Erfolgswahrscheinlichkeit des ersten Schritts ist {number(p1, 2)}. Unter den Personen, die Schritt eins schaffen, "
                f"beträgt die Erfolgswahrscheinlichkeit des zweiten Schritts {number(p2, 2)}. Unter den Personen, die beide schaffen, "
                f"beträgt die Erfolgswahrscheinlichkeit des dritten Schritts {number(p3, 2)}."
            )
            parts = [
                "berechne die Wahrscheinlichkeit, die Schritte eins und zwei abzuschliessen",
                "berechne die Wahrscheinlichkeit, die vollständige dreistufige Abfolge abzuschliessen",
                "berechne die Wahrscheinlichkeit, die ersten beiden Schritte zu schaffen, aber am dritten zu scheitern",
            ]
            reasoning = (
                "Definiere Ereignisse für die drei Schritte und erkläre, weshalb die Multiplikation bedingte Wahrscheinlichkeiten und nicht unverbundene Randwahrscheinlichkeiten verwendet."
            )
        else:
            setup = (
                f"Suksesi kërkon tri etapa me radhë: së pari {first}; së dyti {second}; dhe së treti {third}. "
                f"Probabiliteti i suksesit në etapën e parë është {number(p1, 2)}. Mes atyre që e kalojnë etapën e parë, "
                f"probabiliteti i suksesit në etapën e dytë është {number(p2, 2)}. Mes atyre që i kalojnë të dyja, "
                f"probabiliteti i suksesit në etapën e tretë është {number(p3, 2)}."
            )
            parts = [
                "gjej probabilitetin e përfundimit të etapës së parë dhe të dytë",
                "gjej probabilitetin e përfundimit të të tria etapave",
                "gjej probabilitetin e përfundimit të dy etapave të para dhe dështimit në të tretën",
            ]
            reasoning = (
                "Përcakto ngjarjet e etapave dhe shpjego pse shumëzimi përdor probabilitete të kushtëzuara, jo probabilitete margjinale të palidhura."
            )
        prompt = varied_exercise_localized(
            locale, variant, setup, parts, reasoning
        )
        exercises.append(task(2, 1, variant, title, prompt))
        p12, p123, p12not3 = p1 * p2, p1 * p2 * p3, p1 * p2 * (1 - p3)
        if is_de:
            solution = (
                f"$A$, $B$ und $C$ bezeichnen der Reihe nach den Erfolg in den drei Schritten. (a) Nach der Kettenregel gilt "
                f"$P(A\\cap B)=P(A)P(B\\mid A)={number(p1,2)}\\times {number(p2,2)}={number(p12)}$. "
                f"(b) $P(A\\cap B\\cap C)=P(A)P(B\\mid A)P(C\\mid A\\cap B)={number(p1,2)}\\times {number(p2,2)}\\times {number(p3,2)}={number(p123)}$. "
                f"Das Modell sagt somit, dass der Anteil {number(p123)} die ganze Abfolge bis zum Schritt «{third}» abschliesst. "
                f"(c) Nach den ersten beiden Erfolgen beträgt die bedingte Wahrscheinlichkeit eines Misserfolgs im dritten Schritt $1-{number(p3,2)}={number(1-p3,2)}$. "
                f"Daher ist $P(A\\cap B\\cap C')={number(p1,2)}\\times {number(p2,2)}\\times {number(1-p3,2)}={number(p12not3)}$. "
                "Dies ist der modellierte Anteil, der den dritten Schritt erreicht, ihn aber nicht abschliesst. Die Wahrscheinlichkeiten späterer Schritte beziehen sich bereits auf durch frühere Erfolge eingeschränkte Gruppen. Unbedingte Randwahrscheinlichkeiten würden diese Bedingungen verwerfen."
            )
        else:
            solution = (
                f"$A$, $B$ dhe $C$ tregojnë me radhë suksesin në tri etapat. (a) Sipas rregullit të vargut, "
                f"$P(A\\cap B)=P(A)P(B\\mid A)={number(p1,2)}\\times {number(p2,2)}={number(p12)}$. "
                f"(b) $P(A\\cap B\\cap C)=P(A)P(B\\mid A)P(C\\mid A\\cap B)={number(p1,2)}\\times {number(p2,2)}\\times {number(p3,2)}={number(p123)}$. "
                f"Pra modeli thotë se përpjesëtimi {number(p123)} e përfundon gjithë vargun deri te etapa «{third}». "
                f"(c) Pas dy sukseseve të para, probabiliteti i kushtëzuar i dështimit në etapën e tretë është $1-{number(p3,2)}={number(1-p3,2)}$. "
                f"Prandaj $P(A\\cap B\\cap C')={number(p1,2)}\\times {number(p2,2)}\\times {number(1-p3,2)}={number(p12not3)}$. "
                "Ky është përpjesëtimi i modeluar që arrin në etapën e tretë, por nuk e përfundon. Probabilitetet e etapave të mëvonshme i referohen grupeve tashmë të kufizuara nga sukseset e mëparshme. Zëvendësimi i tyre me probabilitete margjinale do t'i humbte kushtet e situatës."
            )
        solutions.append(task(2, 1, variant, title, solution))

    # A02: independence
    heading_text = (
        "Gemeinsame unabhängige Ereignisse"
        if is_de
        else "Ngjarje të përbashkëta të pavarura"
    )
    exercises.append(heading(2, heading_text))
    solutions.append(heading(2, heading_text))
    for variant, ((title, event_a, event_b), (pa, pb)) in enumerate(
        zip(independent_contexts, INDEPENDENT_PROBABILITIES), 1
    ):
        if is_de:
            setup = (
                f"Ereignis $A$ bedeutet, dass {event_a}, mit $P(A)={number(pa,2)}$. Ereignis $B$ bedeutet, dass {event_b}, "
                f"mit $P(B)={number(pb,2)}$. Nimm an, dass $A$ und $B$ unabhängig sind."
            )
            parts = [
                "berechne die Wahrscheinlichkeit, dass beide Ereignisse eintreten",
                "berechne die Wahrscheinlichkeit, dass mindestens eines der Ereignisse eintritt",
                "berechne die Wahrscheinlichkeit, dass $A$ eintritt und $B$ nicht eintritt",
            ]
            reasoning = (
                "Nenne in jedem Teil die verwendete Regel und zeige genau, welche Produktrechnungen von der Unabhängigkeit abhängen."
            )
        else:
            setup = (
                f"Ngjarja $A$ do të thotë se {event_a}, me $P(A)={number(pa,2)}$. Ngjarja $B$ do të thotë se {event_b}, "
                f"me $P(B)={number(pb,2)}$. Supozo se $A$ dhe $B$ janë të pavarura."
            )
            parts = [
                "llogarit probabilitetin që të ndodhin të dyja ngjarjet",
                "llogarit probabilitetin që të ndodhë të paktën njëra ngjarje",
                "llogarit probabilitetin që të ndodhë $A$, por jo $B$",
            ]
            reasoning = (
                "Emërto rregullin e përdorur në secilën pjesë dhe trego saktësisht cilat prodhime varen nga pavarësia."
            )
        prompt = varied_exercise_localized(
            locale, variant, setup, parts, reasoning
        )
        exercises.append(task(2, 2, variant, title, prompt))
        both = pa * pb
        union = pa + pb - both
        only_a = pa * (1 - pb)
        if is_de:
            solution = (
                f"Wegen der Unabhängigkeit ist $P(A\\cap B)=P(A)P(B)={number(pa,2)}\\times {number(pb,2)}={number(both)}$. "
                f"Dies ist die modellierte Wahrscheinlichkeit, dass {event_a} und {event_b}. Für (b) ergibt die allgemeine Additionsregel "
                f"$P(A\\cup B)={number(pa,2)}+{number(pb,2)}-{number(both)}={number(union)}$. Das ist die Wahrscheinlichkeit, dass mindestens eines der beiden Ereignisse eintritt. "
                f"Für (c) folgt aus der Unabhängigkeit von $A$ und $B$ auch die Unabhängigkeit von $A$ und $B'$. Deshalb gilt "
                f"$P(A\\cap B')={number(pa,2)}(1-{number(pb,2)})={number(only_a)}$. Unabhängigkeit erlaubt, gemeinsame Wahrscheinlichkeiten durch Produkte zu ersetzen. Die Additionsregel selbst gilt mit und ohne Unabhängigkeit."
            )
        else:
            solution = (
                f"Pavarësia lejon $P(A\\cap B)=P(A)P(B)={number(pa,2)}\\times {number(pb,2)}={number(both)}$. "
                f"Ky është probabiliteti i modeluar që {event_a} dhe {event_b}. Për (b), rregulla e përgjithshme e mbledhjes jep "
                f"$P(A\\cup B)={number(pa,2)}+{number(pb,2)}-{number(both)}={number(union)}$. Ky është probabiliteti që të ndodhë të paktën njëra nga dy ngjarjet. "
                f"Për (c), nga pavarësia e $A$ dhe $B$ rrjedh edhe pavarësia e $A$ dhe $B'$. Prandaj "
                f"$P(A\\cap B')={number(pa,2)}(1-{number(pb,2)})={number(only_a)}$. Pavarësia përdoret për të zëvendësuar probabilitetet e përbashkëta me prodhime. Rregulla e mbledhjes vlen pavarësisht nëse ngjarjet janë të pavarura."
            )
        solutions.append(task(2, 2, variant, title, solution))

    # A03: contingency tables
    heading_text = (
        "Kontingenztafeln und Beziehungen zwischen Ereignissen"
        if is_de
        else "Tabelat e kontingjencës dhe marrëdhëniet mes ngjarjeve"
    )
    exercises.append(heading(3, heading_text))
    solutions.append(heading(3, heading_text))
    for variant, (localized, canonical) in enumerate(
        zip(table_contexts, TABLE_CONTEXTS), 1
    ):
        title, group_1, group_2, yes, no = localized
        _title, _g1, _g2, _yes, _no, a, b, c, d = canonical
        total = a + b + c + d
        if is_de:
            setup = f"""Die beobachtete Stichprobe ist unten zusammengefasst.

| Gruppe | {yes} | {no} | Gesamt |
|---|---:|---:|---:|
| {group_1} | {a} | {b} | {a+b} |
| {group_2} | {c} | {d} | {c+d} |
| Gesamt | {a+c} | {b+d} | {total} |

$G$ bezeichnet die Zugehörigkeit zur Zeile {group_1}, und $Y$ bezeichnet das Ergebnis {yes}. Die Zeile {group_2} ist $G^c$."""
            parts = [
                "bestimme $P(Y\\mid G)$ und $P(Y\\mid G^c)$ und entscheide danach, ob die Variablen in der empirischen Verteilung unabhängig sind",
                "bestimme die gemeinsame Wahrscheinlichkeit $P(G\\cap Y)$",
                "entscheide, ob $G$ und $Y$ disjunkte Ereignisse sind",
            ]
            reasoning = (
                "Erkläre, weshalb eine exakte Beziehung in diesen Stichprobenhäufigkeiten allein noch keine Schlussfolgerung über eine nicht erhobene Grundgesamtheit erlaubt."
            )
        else:
            setup = f"""Kampioni i vëzhguar përmblidhet më poshtë.

| Grupi | {yes} | {no} | Gjithsej |
|---|---:|---:|---:|
| {group_1} | {a} | {b} | {a+b} |
| {group_2} | {c} | {d} | {c+d} |
| Gjithsej | {a+c} | {b+d} | {total} |

$G$ tregon përkatësinë në rreshtin {group_1}, ndërsa $Y$ tregon rezultatin {yes}. Rreshti {group_2} është $G^c$."""
            parts = [
                "gjej $P(Y\\mid G)$ dhe $P(Y\\mid G^c)$, pastaj vendos nëse ndryshoret janë të pavarura në shpërndarjen empirike",
                "gjej probabilitetin e përbashkët $P(G\\cap Y)$",
                "vendos nëse $G$ dhe $Y$ janë ngjarje që përjashtojnë njëra-tjetrën",
            ]
            reasoning = (
                "Shpjego pse një marrëdhënie e saktë në këto numërime të kampionit nuk është vetvetiu përfundim për një popullatë që nuk është kampionuar."
            )
        prompt = varied_exercise_localized(
            locale, variant, setup, parts, reasoning
        )
        exercises.append(task(2, 3, variant, title, prompt))
        p1, p2, joint = a / (a + b), c / (c + d), a / total
        independent = abs(p1 - p2) < 1e-12
        if is_de:
            decision = (
                "gleich, daher sind die Variablen in dieser empirischen Tabelle unabhängig"
                if independent
                else "verschieden, daher sind die Variablen in dieser empirischen Tabelle nicht unabhängig"
            )
            solution = (
                f"(a) Für die Zeile {group_1} ist $P(Y\\mid G)={a}/{a+b}={number(p1)}$, für die Zeile {group_2} ist "
                f"$P(Y\\mid G^c)={c}/{c+d}={number(p2)}$. Diese bedingten Anteile sind {decision}. Dies beschreibt die gezeigte empirische Verteilung und beweist nicht dieselbe Beziehung in einer grösseren Grundgesamtheit. "
                f"(b) Der Schnitt von {group_1} und {yes} enthält {a} der {total} Beobachtungen. Somit ist $P(G\\cap Y)={a}/{total}={number(joint)}$. "
                "(c) $G$ und $Y$ sind nicht disjunkt, weil dieser Schnitt nicht leer ist. Bei disjunkten Ereignissen wäre die Häufigkeit im Schnitt null."
            )
        else:
            decision = (
                "të barabarta, prandaj ndryshoret janë të pavarura në këtë tabelë empirike"
                if independent
                else "të ndryshme, prandaj ndryshoret nuk janë të pavarura në këtë tabelë empirike"
            )
            solution = (
                f"(a) Për rreshtin {group_1}, $P(Y\\mid G)={a}/{a+b}={number(p1)}$, ndërsa për rreshtin {group_2}, "
                f"$P(Y\\mid G^c)={c}/{c+d}={number(p2)}$. Këto përpjesëtime të kushtëzuara janë {decision}. Ky është përshkrim i shpërndarjes empirike të paraqitur, jo provë se e njëjta marrëdhënie vlen në një popullatë më të gjerë. "
                f"(b) Prerja e {group_1} dhe {yes} përmban {a} nga {total} vëzhgimet, prandaj $P(G\\cap Y)={a}/{total}={number(joint)}$. "
                "(c) $G$ dhe $Y$ nuk e përjashtojnë njëra-tjetrën, sepse kjo prerje nuk është bosh. Ngjarjet që përjashtojnë njëra-tjetrën do të kishin numërim zero në prerje."
            )
        solutions.append(task(2, 3, variant, title, solution))

    # A04: Bayes and base rates
    heading_text = (
        "Satz von Bayes und Basisraten"
        if is_de
        else "Teorema e Bayes-it dhe normat bazë"
    )
    exercises.append(heading(4, heading_text))
    solutions.append(heading(4, heading_text))
    for variant, (localized, canonical) in enumerate(
        zip(bayes_contexts, BAYES_CONTEXTS), 1
    ):
        title, condition = localized
        _title, _condition, sensitivity, specificity, prevalence_1, prevalence_2 = canonical
        if is_de:
            setup = (
                f"Ein hypothetisches Screening-Instrument soll {condition} erkennen. Seine Sensitivität beträgt {number(sensitivity,2)}, "
                f"seine Spezifität {number(specificity,2)}. $D$ bedeutet, dass das Merkmal tatsächlich vorliegt, und $+$ bedeutet ein positives Ergebnis."
            )
            parts = [
                f"berechne $P(D\\mid +)$ bei einer Prävalenz von {number(prevalence_1*100,0)}%",
                f"berechne $P(D\\mid +)$ erneut bei einer Prävalenz von {number(prevalence_2*100,0)}%",
                "vergleiche die posterioren Wahrscheinlichkeiten und erkläre den Basisrateneffekt",
            ]
            reasoning = (
                "Zeige für beide Prävalenzen den richtig-positiven und den falsch-positiven Pfad. Erkläre zudem, weshalb die Sensitivität allein nicht die gesuchte posteriore Wahrscheinlichkeit ist."
            )
        else:
            setup = (
                f"Një instrument hipotetik depistimi përdoret për të zbuluar {condition}. Ndjeshmëria e tij është {number(sensitivity,2)}, "
                f"ndërsa specifiteti është {number(specificity,2)}. $D$ do të thotë se gjendja është vërtet e pranishme, kurse $+$ tregon rezultat pozitiv."
            )
            parts = [
                f"llogarit $P(D\\mid +)$ kur prevalenca është {number(prevalence_1*100,0)}%",
                f"llogarit përsëri $P(D\\mid +)$ kur prevalenca është {number(prevalence_2*100,0)}%",
                "krahaso probabilitetet pasuese dhe shpjego ndikimin e normës bazë",
            ]
            reasoning = (
                "Për secilën prevalencë, trego rrugën e rezultateve vërtet pozitive dhe gabimisht pozitive. Shpjego pse vetëm ndjeshmëria nuk është probabiliteti pasues që kërkohet."
            )
        prompt = varied_exercise_localized(
            locale, variant, setup, parts, reasoning
        )
        exercises.append(task(2, 4, variant, title, prompt))
        values = []
        for prevalence in (prevalence_1, prevalence_2):
            true_positive = sensitivity * prevalence
            false_positive = (1 - specificity) * (1 - prevalence)
            values.append(
                (
                    true_positive,
                    false_positive,
                    true_positive / (true_positive + false_positive),
                )
            )
        if is_de:
            solution = (
                f"Die falsch-positive Wahrscheinlichkeit ist $1-{number(specificity,2)}={number(1-specificity,2)}$. "
                f"(a) Bei Prävalenz {number(prevalence_1,2)} sind die Pfade zu einem positiven Ergebnis "
                f"$P(+\\cap D)={number(sensitivity,2)}\\times {number(prevalence_1,2)}={number(values[0][0])}$ und "
                f"$P(+\\cap D')={number(1-specificity,2)}\\times {number(1-prevalence_1,2)}={number(values[0][1])}$. Somit ist "
                f"$P(D\\mid +)={number(values[0][0])}/({number(values[0][0])}+{number(values[0][1])})={number(values[0][2])}$. "
                f"(b) Bei Prävalenz {number(prevalence_2,2)} lauten die entsprechenden Pfade {number(values[1][0])} und {number(values[1][1])}. Daraus folgt "
                f"$P(D\\mid +)={number(values[1][0])}/({number(values[1][0])}+{number(values[1][1])})={number(values[1][2])}$. "
                "Diese posteriore Wahrscheinlichkeit beschreibt nach einem positiven Ergebnis die Chance, dass das untersuchte Merkmal tatsächlich vorliegt. Die Sensitivität setzt hingegen bereits voraus, dass das Merkmal vorliegt. Eine höhere Basisrate erhöht den Anteil der positiven Ergebnisse, die richtig positiv sind."
            )
        else:
            solution = (
                f"Probabiliteti i rezultatit gabimisht pozitiv është $1-{number(specificity,2)}={number(1-specificity,2)}$. "
                f"(a) Kur prevalenca është {number(prevalence_1,2)}, rrugët drejt rezultatit pozitiv janë "
                f"$P(+\\cap D)={number(sensitivity,2)}\\times {number(prevalence_1,2)}={number(values[0][0])}$ dhe "
                f"$P(+\\cap D')={number(1-specificity,2)}\\times {number(1-prevalence_1,2)}={number(values[0][1])}$. Prandaj "
                f"$P(D\\mid +)={number(values[0][0])}/({number(values[0][0])}+{number(values[0][1])})={number(values[0][2])}$. "
                f"(b) Kur prevalenca është {number(prevalence_2,2)}, rrugët përkatëse janë {number(values[1][0])} dhe {number(values[1][1])}, duke dhënë "
                f"$P(D\\mid +)={number(values[1][0])}/({number(values[1][0])}+{number(values[1][1])})={number(values[1][2])}$. "
                f"Ky probabilitet pasues tregon mundësinë që «{condition}» të jetë vërtet e pranishme pas një rezultati pozitiv. Ndjeshmëria kushtëzohet mbi praninë e gjendjes që në fillim. Norma bazë më e lartë e rrit pjesën e rezultateve pozitive që janë vërtet pozitive."
            )
        solutions.append(task(2, 4, variant, title, solution))

    # A05: discrete distributions
    localized_discrete_titles = (
        i18n.DE_DISCRETE_TITLES if is_de else i18n.SQ_DISCRETE_TITLES
    )
    heading_text = (
        "Diskreter Erwartungswert, Varianz, PMF und CDF"
        if is_de
        else "Vlera e pritur, varianca, PMF-ja dhe CDF-ja për ndryshore diskrete"
    )
    exercises.append(heading(5, heading_text))
    solutions.append(heading(5, heading_text))
    for variant, (title, canonical) in enumerate(
        zip(localized_discrete_titles, DISCRETE_DISTRIBUTIONS), 1
    ):
        _title, values, probabilities = canonical
        cells = " | ".join(str(value) for value in values)
        masses = " | ".join(number(probability, 2) for probability in probabilities)
        description = title if is_de else title[0].lower() + title[1:]
        if is_de:
            setup = f"""$X$ bezeichnet die Grösse «{description}». Die vorgeschlagene Verteilung lautet:

| $x$ | {cells} |
|---|---:|---:|---:|---:|
| $P(X=x)$ | {masses} |"""
            parts = [
                "prüfe, ob die Tabelle eine gültige Wahrscheinlichkeitsfunktion ist",
                "berechne $E(X)$ und $\\operatorname{Var}(X)$, wobei du für die Varianz $E(X^2)-[E(X)]^2$ verwendest",
                "gib $F(x)$ an jeder Stelle des Trägers an",
            ]
            reasoning = (
                "Beschreibe den Unterschied zwischen den Grafiken der PMF und der CDF und interpretiere den Erwartungswert im oben genannten Kontext."
            )
        else:
            setup = f"""$X$ përfaqëson numërimin e përshkruar si «{description}». Shpërndarja e propozuar është:

| $x$ | {cells} |
|---|---:|---:|---:|---:|
| $P(X=x)$ | {masses} |"""
            parts = [
                "verifiko nëse tabela është funksion i vlefshëm i masës së probabilitetit",
                "llogarit $E(X)$ dhe $\\operatorname{Var}(X)$ duke përdorur $E(X^2)-[E(X)]^2$ për variancën",
                "jep $F(x)$ në secilën vlerë të bashkësisë mbështetëse",
            ]
            reasoning = (
                "Përshkruaj si dallojnë grafiku i PMF-së dhe ai i CDF-së, pastaj interpreto vlerën e pritur në kontekstin e mësipërm."
            )
        prompt = varied_exercise_localized(
            locale, variant, setup, parts, reasoning
        )
        exercises.append(task(2, 5, variant, title, prompt))
        mean = sum(x * p for x, p in zip(values, probabilities))
        expected_square = sum(
            x * x * p for x, p in zip(values, probabilities)
        )
        variance = expected_square - mean * mean
        cumulative = []
        running = 0.0
        for value, probability in zip(values, probabilities):
            running += probability
            cumulative.append(f"$F({value})={number(running,2)}$")
        mean_terms = "+".join(
            f"{value}({number(probability,2)})"
            for value, probability in zip(values, probabilities)
        )
        square_terms = "+".join(
            f"{value}^2({number(probability,2)})"
            for value, probability in zip(values, probabilities)
        )
        if is_de:
            solution = (
                f"(a) Alle Massen sind nichtnegativ, und ihre Summe ist {'+'.join(number(p,2) for p in probabilities)}={number(sum(probabilities),2)}. Die Tabelle ist daher eine gültige PMF. "
                f"(b) $E(X)=\\sum xP(X=x)={mean_terms}={number(mean)}$. Über viele vergleichbare Beobachtungen nähert sich der langfristige Mittelwert der Grösse «{description}» dem Wert {number(mean)}. "
                f"Weiter ist $E(X^2)={square_terms}={number(expected_square)}$. Somit gilt $\\operatorname{{Var}}(X)={number(expected_square)}-{number(mean)}^2={number(variance)}$; die Varianz besitzt quadrierte Zähleinheiten. "
                f"(c) Die kumulierten Werte sind {', '.join(cumulative)}. Eine PMF-Grafik setzt bei jedem möglichen Wert einen eigenen Balken oder eine Punktmasse. Eine CDF ist dagegen eine nicht fallende, rechtsstetige Treppenfunktion, welche die Massen ansammelt und bei 1 endet."
            )
        else:
            solution = (
                f"(a) Të gjitha masat janë jonegative dhe shuma e tyre është {'+'.join(number(p,2) for p in probabilities)}={number(sum(probabilities),2)}, prandaj tabela është PMF e vlefshme. "
                f"(b) $E(X)=\\sum xP(X=x)={mean_terms}={number(mean)}$. Në shumë vëzhgime të krahasueshme, mesatarja afatgjatë e madhësisë së emërtuar më sipër do t'i afrohej {number(mean)}. "
                f"Më pas, $E(X^2)={square_terms}={number(expected_square)}$, kështu që $\\operatorname{{Var}}(X)={number(expected_square)}-{number(mean)}^2={number(variance)}$; kjo variancë shprehet në njësi numërimi në katror. "
                f"(c) Vlerat kumulative janë {', '.join(cumulative)}. Grafiku i PMF-së vendos një shtyllë ose masë të veçantë në secilën vlerë mbështetëse. CDF-ja është funksion shkallëzues jozbritës, i vazhdueshëm nga e djathta, që i grumbullon masat dhe përfundon në 1."
            )
        solutions.append(task(2, 5, variant, title, solution))

    # A06: exact binomial probabilities
    localized_binomial_exact = (
        i18n.DE_BINOMIAL_EXACT if is_de else i18n.SQ_BINOMIAL_EXACT
    )
    heading_text = (
        "Exakte Binomialwahrscheinlichkeiten"
        if is_de
        else "Probabilitetet e sakta binomiale"
    )
    exercises.append(heading(6, heading_text))
    solutions.append(heading(6, heading_text))
    for variant, (localized, canonical) in enumerate(
        zip(localized_binomial_exact, BINOMIAL_EXACT), 1
    ):
        title, units, success = localized
        _title, _units, _success, n, probability, first_count, second_count = canonical
        if is_de:
            setup = (
                f"Betrachte {n} {units}. Behandle sie als unabhängige Versuche und nimm an, dass die Wahrscheinlichkeit, dass eine Einheit {success}, "
                f"konstant $\\pi={number(probability,2)}$ ist. $X$ zählt, wie viele Einheiten diese Erfolgsdefinition erfüllen."
            )
            parts = [
                f"berechne $P(X={first_count})$",
                f"berechne $P(X={second_count})$",
                "bestimme $E(X)$ und $\\operatorname{Var}(X)$",
                "formuliere für diese Situation die Annahmen einer festen Versuchszahl, zweier möglicher Ergebnisse, einer konstanten Wahrscheinlichkeit und unabhängiger Versuche",
            ]
            reasoning = (
                "Zeige vor dem Runden den Binomialkoeffizienten und jeden eingesetzten Modellwert."
            )
        else:
            setup = (
                f"Shqyrto {n} {units}. Trajtoji si prova të pavarura dhe supozo se probabiliteti që secila njësi {success} "
                f"është konstant, $\\pi={number(probability,2)}$. $X$ numëron sa njësi e plotësojnë këtë përkufizim të suksesit."
            )
            parts = [
                f"llogarit $P(X={first_count})$",
                f"llogarit $P(X={second_count})$",
                "gjej $E(X)$ dhe $\\operatorname{Var}(X)$",
                "për këtë situatë, thuaj supozimet për numrin fiks të provave, dy rezultatet, probabilitetin konstant dhe pavarësinë",
            ]
            reasoning = (
                "Trego koeficientin binomial dhe çdo vlerë të zëvendësuar të modelit para rrumbullakimit."
            )
        prompt = varied_exercise_localized(
            locale, variant, setup, parts, reasoning
        )
        exercises.append(task(2, 6, variant, title, prompt))
        first_probability = probability_binomial(
            n, probability, first_count
        )
        second_probability = probability_binomial(
            n, probability, second_count
        )
        expected = n * probability
        variance = n * probability * (1 - probability)
        if is_de:
            solution = (
                f"Das Modell lautet $X\\sim B({n},{number(probability,2)})$. (a) "
                f"$P(X={first_count})=\\binom{{{n}}}{{{first_count}}}{number(probability,2)}^{{{first_count}}}(1-{number(probability,2)})^{{{n-first_count}}}={number(first_probability)}$. "
                f"Dies ist die modellierte Wahrscheinlichkeit, dass genau {first_count} der {n} {units} die Erfolgsdefinition erfüllen. (b) "
                f"$P(X={second_count})=\\binom{{{n}}}{{{second_count}}}{number(probability,2)}^{{{second_count}}}(1-{number(probability,2)})^{{{n-second_count}}}={number(second_probability)}$. Dies ist die entsprechende Wahrscheinlichkeit für genau {second_count}. "
                f"(c) $E(X)=n\\pi={n}({number(probability,2)})={number(expected)}$ und $\\operatorname{{Var}}(X)=n\\pi(1-\\pi)={n}({number(probability,2)})({number(1-probability,2)})={number(variance)}$. "
                f"Über wiederholte Gruppen der Grösse {n} nähert sich die mittlere Anzahl dem Wert {number(expected)}. (d) Die Zahl der {units} muss fest bei {n} bleiben. Jede Einheit wird nur als Erfolg oder Misserfolg danach eingeteilt, ob sie {success}. "
                f"Die Erfolgswahrscheinlichkeit muss {number(probability,2)} bleiben, und die Ergebnisse der Versuche müssen unabhängig sein. Wenn eine Bedingung nicht gilt, ist diese Binomialrechnung nicht begründet."
            )
        else:
            solution = (
                f"Modeli është $X\\sim B({n},{number(probability,2)})$. (a) "
                f"$P(X={first_count})=\\binom{{{n}}}{{{first_count}}}{number(probability,2)}^{{{first_count}}}(1-{number(probability,2)})^{{{n-first_count}}}={number(first_probability)}$. "
                f"Ky është probabiliteti i modeluar që saktësisht {first_count} nga {n} {units} ta plotësojnë përkufizimin e suksesit. (b) "
                f"$P(X={second_count})=\\binom{{{n}}}{{{second_count}}}{number(probability,2)}^{{{second_count}}}(1-{number(probability,2)})^{{{n-second_count}}}={number(second_probability)}$. Ky është probabiliteti përkatës për saktësisht {second_count}. "
                f"(c) $E(X)=n\\pi={n}({number(probability,2)})={number(expected)}$ dhe $\\operatorname{{Var}}(X)=n\\pi(1-\\pi)={n}({number(probability,2)})({number(1-probability,2)})={number(variance)}$. "
                f"Në grupe të përsëritura me {n} njësi, numri mesatar do t'i afrohej {number(expected)}. (d) Numri i provave duhet të mbetet fiks në {n}. Secila njësi klasifikohet vetëm si sukses ose dështim sipas asaj nëse {success}. "
                f"Probabiliteti i suksesit duhet të mbetet {number(probability,2)}, ndërsa rezultatet e provave duhet të jenë të pavarura. Nëse ndonjë kusht dështon, kjo llogaritje binomiale nuk arsyetohet."
            )
        solutions.append(task(2, 6, variant, title, solution))

    # A07: binomial complements
    localized_binomial_tail = (
        i18n.DE_BINOMIAL_TAIL if is_de else i18n.SQ_BINOMIAL_TAIL
    )
    heading_text = (
        "Binomiale Randwahrscheinlichkeiten mit dem Komplement"
        if is_de
        else "Probabilitetet e skajit binomial përmes komplementit"
    )
    exercises.append(heading(7, heading_text))
    solutions.append(heading(7, heading_text))
    for variant, (localized, canonical) in enumerate(
        zip(localized_binomial_tail, BINOMIAL_TAIL), 1
    ):
        label, units, success = localized
        _label, _units, _success, n, probability, cutoff = canonical
        title = (
            f"Mehr als {cutoff} {label}"
            if is_de
            else f"Më shumë se {cutoff} {label[0].lower() + label[1:]}"
        )
        if is_de:
            setup = (
                f"Modelliere die {n} betrachteten Einheiten als unabhängige Fälle. Für jede Einheit besitzt das Ereignis, dass sie {success}, "
                f"die konstante Wahrscheinlichkeit $\\pi={number(probability,2)}$. $X$ ist die Gesamtzahl dieser Ereignisse."
            )
            parts = [
                f"bestimme das Binomialmodell und das Komplement von $X>{cutoff}$",
                f"verwende dieses Komplement, um $P(X>{cutoff})$ zu berechnen, und zeige jeden Term des unteren Randes",
                "interpretiere die Randwahrscheinlichkeit und vergleiche die Anzahl der Terme mit einer direkten Summe des oberen Randes",
            ]
            reasoning = (
                "Behalte die ungerundeten Einzelwahrscheinlichkeiten bis zum abschliessend berichteten Ergebnis bei."
            )
        else:
            setup = (
                f"Modeloji {n} njësitë e shqyrtuara si raste të pavarura. Për secilën njësi, ngjarja që ajo {success} "
                f"ka probabilitet konstant $\\pi={number(probability,2)}$. $X$ është numri i përgjithshëm i këtyre ngjarjeve."
            )
            parts = [
                f"përcakto modelin binomial dhe komplementin e $X>{cutoff}$",
                f"përdore këtë komplement për të llogaritur $P(X>{cutoff})$, duke treguar çdo term të skajit të poshtëm",
                "interpreto probabilitetin e skajit dhe krahaso numrin e termave me një shumë të drejtpërdrejtë të skajit të sipërm",
            ]
            reasoning = (
                "Ruaji probabilitetet e parrumbullakosura të përbërësve deri te rezultati përfundimtar që raporton."
            )
        prompt = varied_exercise_localized(
            locale, variant, setup, parts, reasoning
        )
        exercises.append(task(2, 7, variant, title, prompt))
        terms = [
            probability_binomial(n, probability, count)
            for count in range(cutoff + 1)
        ]
        cumulative = sum(terms)
        tail = 1 - cumulative
        symbolic = "+".join(
            f"P(X={count})" for count in range(cutoff + 1)
        )
        numeric = "+".join(number(value) for value in terms)
        if is_de:
            solution = (
                f"(a) Hier ist $X\\sim B({n},{number(probability,2)})$, und das Komplement von $X>{cutoff}$ ist $X\\leq {cutoff}$. "
                f"(b) Daher gilt $P(X>{cutoff})=1-[{symbolic}]=1-[{numeric}]\\approx 1-{number(cumulative)}={number(tail)}$. "
                f"Das Näherungszeichen ist nötig, weil die gezeigten Einzelterme gerundet sind. Der Wert {number(cumulative)} wurde mit ungerundeten Termen berechnet. "
                f"(c) Das Modell weist die Wahrscheinlichkeit {number(tail)} dem Ereignis zu, bei dem mehr als {cutoff} Erfolge in einer Gruppe von {n} betrachteten Einheiten auftreten. Ein Erfolg bedeutet hier, dass eine Einheit {success}. "
                f"Das Komplement benötigt {cutoff+1} Terme des unteren Randes. Eine direkte Summe würde dagegen die Werte {cutoff+1} bis {n} benötigen."
            )
        else:
            solution = (
                f"(a) Këtu $X\\sim B({n},{number(probability,2)})$, ndërsa komplementi i $X>{cutoff}$ është $X\\leq {cutoff}$. "
                f"(b) Prandaj $P(X>{cutoff})=1-[{symbolic}]=1-[{numeric}]\\approx 1-{number(cumulative)}={number(tail)}$. "
                f"Shenja e përafrimit nevojitet sepse termat e paraqitur janë rrumbullakosur. Vlera {number(cumulative)} u llogarit nga termat e parrumbullakosur. "
                f"(c) Modeli i cakton probabilitetin {number(tail)} rastit me më shumë se {cutoff} suksese mes {n} njësive të shqyrtuara. Këtu një sukses do të thotë se një njësi {success}. "
                f"Komplementi përdor {cutoff+1} terma të skajit të poshtëm, ndërsa një shumë e drejtpërdrejtë do të kërkonte vlerat {cutoff+1} deri në {n}."
            )
        solutions.append(task(2, 7, variant, title, solution))

    # A08: PMF versus density
    localized_pmf_density = (
        i18n.DE_PMF_DENSITY if is_de else i18n.SQ_PMF_DENSITY
    )
    heading_text = (
        "Wahrscheinlichkeitsfunktionen und Dichten"
        if is_de
        else "Funksionet e masës së probabilitetit dhe dendësitë"
    )
    exercises.append(heading(8, heading_text))
    solutions.append(heading(8, heading_text))
    for variant, (discrete, continuous) in enumerate(
        localized_pmf_density, 1
    ):
        title = (
            f"{discrete[0].upper() + discrete[1:]} und {continuous}"
            if is_de
            else f"Nga {discrete} te {continuous}"
        )
        if is_de:
            setup = (
                f"Definiere $X$ als {discrete}, also als Anzahl, und $Y$ als {continuous}, gemessen auf einer stetigen Skala. "
                "Die beiden Variablen benötigen daher unterschiedliche Wahrscheinlichkeitsdarstellungen."
            )
            parts = [
                "bestimme, welche Variable eine PMF und welche eine Dichte verwendet",
                "erkläre die Punktwahrscheinlichkeit $P(X=x)$ und stelle ihr $P(Y=y)$ gegenüber",
                "zeige, wie jede Variable Wahrscheinlichkeit über einem Intervall erhält",
                "erkläre, was eine CDF für beide Variablen aufzeichnet",
            ]
            reasoning = (
                "Verwende die Geometrie von Masse, Fläche, Sprüngen und Ansammlung, statt dich nur auf Definitionen zu stützen."
            )
            solution = (
                f"(a) Weil $X$ {discrete} erfasst, besitzt die Variable einen abzählbaren Träger. Eine PMF kann jedem möglichen Zählwert die Masse $P(X=x)$ zuweisen. "
                f"Weil $Y$ {continuous} ist, wird die Variable in einem idealen stetigen Modell durch eine Dichte $f_Y(y)$ dargestellt. "
                "(b) $P(X=x)$ kann für einen einzelnen Zählwert positiv sein, während $P(Y=y)=0$ an jedem einzelnen Punkt gilt, auch wenn Werte in seiner Nähe plausibel sind. "
                "(c) Bei $X$ ist eine Intervallwahrscheinlichkeit die Summe der darin enthaltenen Massen. Bei $Y$ ist sie eine Fläche unter der Dichte, zum Beispiel $P(a<Y\\leq b)=\\int_a^b f_Y(y)\\,dy$. "
                "(d) In beiden Fällen zeichnet eine CDF die angesammelte Wahrscheinlichkeit auf: $F_X(x)=P(X\\leq x)$ springt bei den möglichen Zählwerten, während $F_Y(y)=P(Y\\leq y)$ die Fläche unter der Dichte stetig ansammelt."
            )
        else:
            setup = (
                f"Përcakto ndryshoren diskrete si $X$ = **{discrete}** dhe ndryshoren e vazhdueshme si $Y$ = **{continuous}**. "
                "Prandaj dy ndryshoret kërkojnë paraqitje të ndryshme të probabilitetit."
            )
            parts = [
                "përcakto cila ndryshore përdor PMF dhe cila përdor dendësi",
                "shpjego probabilitetin në një pikë $P(X=x)$ dhe krahasoje me $P(Y=y)$",
                "trego si merret probabiliteti në një interval për secilën ndryshore",
                "shpjego çfarë regjistron CDF-ja për të dyja ndryshoret",
            ]
            reasoning = (
                "Përdor gjeometrinë e masës, sipërfaqes, kërcimeve dhe grumbullimit, jo vetëm përkufizimet."
            )
            solution = (
                f"(a) Ndryshorja $X$ = **{discrete}** ka bashkësi mbështetëse të numërueshme dhe PMF-ja mund t'i caktojë masën $P(X=x)$ secilit numërim të mundshëm. "
                f"Ndryshorja $Y$ = **{continuous}** matet në një shkallë të vazhdueshme, prandaj një model ideal i vazhdueshëm e paraqet atë me dendësinë $f_Y(y)$. "
                "(b) $P(X=x)$ mund të jetë pozitiv për një numërim të vetëm, ndërsa $P(Y=y)=0$ në çdo pikë të saktë edhe kur vlerat pranë saj janë të besueshme. "
                "(c) Për $X$, probabiliteti i intervalit është shuma e masave të përfshira. Për $Y$, ai është sipërfaqe nën dendësi, për shembull $P(a<Y\\leq b)=\\int_a^b f_Y(y)\\,dy$. "
                "(d) Në të dyja rastet, CDF-ja regjistron probabilitetin e grumbulluar: $F_X(x)=P(X\\leq x)$ kërcen në numërimet e mbështetura, ndërsa $F_Y(y)=P(Y\\leq y)$ e grumbullon vazhdimisht sipërfaqen nën dendësi."
            )
        prompt = varied_exercise_localized(
            locale, variant, setup, parts, reasoning
        )
        exercises.append(task(2, 8, variant, title, prompt))
        solutions.append(task(2, 8, variant, title, solution))

    # A09: standard normal
    heading_text = (
        "Wahrscheinlichkeiten der Standardnormalverteilung"
        if is_de
        else "Probabilitetet e shpërndarjes normale standarde"
    )
    exercises.append(heading(9, heading_text))
    solutions.append(heading(9, heading_text))
    for variant, (a, b, c, d) in enumerate(STANDARD_NORMAL, 1):
        title = (
            f"Bereiche der Standardnormalverteilung, Satz {variant}"
            if is_de
            else f"Zonat e shpërndarjes normale standarde, grupi {variant}"
        )
        setup = (
            "Es gilt $Z\\sim N(0,1)$ und $\\Phi(z)=P(Z\\leq z)$."
            if is_de
            else "Le të jetë $Z\\sim N(0,1)$ dhe $\\Phi(z)=P(Z\\leq z)$."
        )
        if is_de:
            parts = [
                f"berechne $P(Z\\leq {number(a,2)})$",
                f"berechne $P(Z>{number(b,2)})$",
                f"berechne $P({number(c,2)}<Z\\leq {number(d,2)})$",
            ]
            reasoning = (
                "Beschreibe bei jeder Wahrscheinlichkeit den schattierten Bereich der Normalkurve und nenne die verwendete Komplement- oder CDF-Differenzregel."
            )
        else:
            parts = [
                f"llogarit $P(Z\\leq {number(a,2)})$",
                f"llogarit $P(Z>{number(b,2)})$",
                f"llogarit $P({number(c,2)}<Z\\leq {number(d,2)})$",
            ]
            reasoning = (
                "Për secilin probabilitet, thuaj cila zonë e lakores normale do të ngjyrosej dhe emërto rregullin e komplementit ose të zbritjes së CDF-ve."
            )
        prompt = varied_exercise_localized(
            locale, variant, setup, parts, reasoning
        )
        exercises.append(task(2, 9, variant, title, prompt))
        left = probability_normal(a)
        right = 1 - probability_normal(b)
        middle = probability_normal(d) - probability_normal(c)
        if is_de:
            solution = (
                f"Schreibe $\\Phi(z)=P(Z\\leq z)$. (a) $P(Z\\leq {number(a,2)})=\\Phi({number(a,2)})={number(left)}$. Schattiere links von {number(a,2)}. "
                f"(b) $P(Z>{number(b,2)})=1-\\Phi({number(b,2)})={number(right)}$. Schattiere den rechten Rand. "
                f"(c) $P({number(c,2)}<Z\\leq {number(d,2)})=\\Phi({number(d,2)})-\\Phi({number(c,2)})={number(middle)}$. Schattiere zwischen den beiden Grenzen. Bei einer stetigen Verteilung verändert die Einbeziehung einer Grenze die Wahrscheinlichkeit nicht."
            )
        else:
            solution = (
                f"Shkruaj $\\Phi(z)=P(Z\\leq z)$. (a) $P(Z\\leq {number(a,2)})=\\Phi({number(a,2)})={number(left)}$. Ngjyrose zonën majtas nga {number(a,2)}. "
                f"(b) $P(Z>{number(b,2)})=1-\\Phi({number(b,2)})={number(right)}$. Ngjyrose skajin e djathtë. "
                f"(c) $P({number(c,2)}<Z\\leq {number(d,2)})=\\Phi({number(d,2)})-\\Phi({number(c,2)})={number(middle)}$. Ngjyrose zonën mes dy kufijve. Për një shpërndarje të vazhdueshme, përfshirja e kufirit nuk e ndryshon probabilitetin."
            )
        solutions.append(task(2, 9, variant, title, solution))

    # A10: general normal
    localized_general_normal = (
        i18n.DE_GENERAL_NORMAL if is_de else i18n.SQ_GENERAL_NORMAL
    )
    heading_text = (
        "Wahrscheinlichkeiten einer allgemeinen Normalverteilung"
        if is_de
        else "Probabilitetet për një shpërndarje normale të përgjithshme"
    )
    exercises.append(heading(10, heading_text))
    solutions.append(heading(10, heading_text))
    for variant, (localized, canonical) in enumerate(
        zip(localized_general_normal, GENERAL_NORMAL), 1
    ):
        context, unit = localized
        _context, _unit, mean, variance, first_value, second_value = canonical
        standard_deviation = math.sqrt(variance)
        title = (
            f"Normalmodell: {context}"
            if is_de
            else f"Modeli normal: {i18n.SQ_GENERAL_NORMAL_TITLES[variant - 1]}"
        )
        if is_de:
            setup = (
                f"$X$ bezeichnet **{context}** (Einheit: **{unit}**) und folgt $N({mean},{variance})$, wobei der zweite Parameter die Varianz ist."
            )
            parts = [
                f"standardisiere {first_value} und bestimme $P(X\\leq {first_value})$",
                f"standardisiere {second_value} und bestimme $P(X>{second_value})$",
                "bestimme die beiden schattierten Bereiche und interpretiere beide Wahrscheinlichkeiten im Kontext",
            ]
            reasoning = (
                "Behalte für die Wahrscheinlichkeitsrechnung die ungerundeten z-Werte bei und runde erst die berichteten Ergebnisse."
            )
        else:
            setup = (
                f"Supozo se $X$ mat {context} në {unit} dhe ndjek $N({mean},{variance})$, ku parametri i dytë është varianca."
            )
            parts = [
                f"standardizo {first_value} dhe gjej $P(X\\leq {first_value})$",
                f"standardizo {second_value} dhe gjej $P(X>{second_value})$",
                "përcakto secilën zonë të ngjyrosur dhe interpreto të dy probabilitetet në kontekst",
            ]
            reasoning = (
                "Ruaji vlerat z të parrumbullakosura për llogaritjet e probabilitetit dhe rrumbullakos vetëm rezultatet që raporton."
            )
        prompt = varied_exercise_localized(
            locale, variant, setup, parts, reasoning
        )
        exercises.append(task(2, 10, variant, title, prompt))
        first_z = (first_value - mean) / standard_deviation
        second_z = (second_value - mean) / standard_deviation
        first_probability = probability_normal(first_z)
        second_probability = 1 - probability_normal(second_z)
        if is_de:
            solution = (
                f"Die Standardabweichung ist $\\sigma=\\sqrt{{{variance}}}={number(standard_deviation,2)}$. "
                f"(a) $z=({first_value}-{mean})/{number(standard_deviation,2)}\\approx {number(first_z)}$. Mit dem ungerundeten Quotienten ergibt sich "
                f"$P(X\\leq {first_value})=\\Phi(({first_value}-{mean})/{number(standard_deviation,2)})={number(first_probability)}$. Nach diesem Modell beträgt der entsprechende Anteil {number(first_probability)}. Er umfasst Werte bis einschliesslich {first_value} {unit}. Schattiere die linke Seite dieser Grenze. "
                f"(b) $z=({second_value}-{mean})/{number(standard_deviation,2)}\\approx {number(second_z)}$ und $P(X>{second_value})=1-\\Phi(({second_value}-{mean})/{number(standard_deviation,2)})={number(second_probability)}$. "
                f"Dies ist der modellierte Anteil über {second_value} {unit}, dargestellt durch den rechten Rand. Beide Interpretationen hängen vom angegebenen Normalmodell ab."
            )
        else:
            solution = (
                f"Devijimi standard është $\\sigma=\\sqrt{{{variance}}}={number(standard_deviation,2)}$. "
                f"(a) $z=({first_value}-{mean})/{number(standard_deviation,2)}\\approx {number(first_z)}$. Duke ruajtur herësin e parrumbullakosur merret "
                f"$P(X\\leq {first_value})=\\Phi(({first_value}-{mean})/{number(standard_deviation,2)})={number(first_probability)}$. Pra modeli vendos përpjesëtimin {number(first_probability)} të vlerave të ndryshores në ose nën {first_value} {unit}. Ngjyrose anën e majtë të këtij kufiri. "
                f"(b) $z=({second_value}-{mean})/{number(standard_deviation,2)}\\approx {number(second_z)}$ dhe $P(X>{second_value})=1-\\Phi(({second_value}-{mean})/{number(standard_deviation,2)})={number(second_probability)}$. "
                f"Ky është përpjesëtimi i modeluar mbi {second_value} {unit}, i paraqitur nga skaji i djathtë. Të dy interpretimet varen nga modeli normal i dhënë."
            )
        solutions.append(task(2, 10, variant, title, solution))

    # A11: inverse normal
    heading_text = (
        "Inverse Quantile der Standardnormalverteilung"
        if is_de
        else "Kuantilet e anasjella të shpërndarjes normale standarde"
    )
    exercises.append(heading(11, heading_text))
    solutions.append(heading(11, heading_text))
    for variant, (first_area, second_area) in enumerate(QUANTILES, 1):
        title = (
            f"Bestimmung der z-Quantile zu {number(first_area*100,0)}% und {number(second_area*100,0)}%"
            if is_de
            else f"Gjetja e kuantileve z për {number(first_area*100,0)}% dhe {number(second_area*100,0)}%"
        )
        if is_de:
            setup = (
                f"Für $Z\\sim N(0,1)$ beträgt eine kumulierte Fläche {number(first_area,2)}, die andere {number(second_area,2)}. Gesucht sind die Grenzen auf der z-Achse, nicht die Wahrscheinlichkeiten."
            )
            parts = [
                f"bestimme $z_{{{number(first_area*100,0)}\\%}}$ mit $P(Z\\leq z)={number(first_area,2)}$",
                f"bestimme $z_{{{number(second_area*100,0)}\\%}}$ mit $P(Z\\leq z)={number(second_area,2)}$",
            ]
            reasoning = (
                "Sage anhand der Lage zu 0.50 das Vorzeichen jeder Grenze voraus und erkläre danach, weshalb dies eine inverse und keine vorwärts gerichtete CDF-Rechnung ist."
            )
        else:
            setup = (
                f"Për $Z\\sim N(0,1)$, një sipërfaqe kumulative është {number(first_area,2)}, ndërsa tjetra është {number(second_area,2)}. Të panjohurat janë kufijtë në boshtin z, jo probabilitetet."
            )
            parts = [
                f"gjej $z_{{{number(first_area*100,0)}\\%}}$ të tillë që $P(Z\\leq z)={number(first_area,2)}$",
                f"gjej $z_{{{number(second_area*100,0)}\\%}}$ të tillë që $P(Z\\leq z)={number(second_area,2)}$",
            ]
            reasoning = (
                "Parashiko shenjën e secilit kufi nga pozita ndaj 0.50, pastaj shpjego pse kjo është llogaritje e anasjellë dhe jo llogaritje e drejtpërdrejtë e CDF-së."
            )
        prompt = varied_exercise_localized(
            locale, variant, setup, parts, reasoning
        )
        exercises.append(task(2, 11, variant, title, prompt))

        def inverse_normal(area: float) -> float:
            lower, upper = -8.0, 8.0
            for _ in range(100):
                midpoint = (lower + upper) / 2
                if probability_normal(midpoint) < area:
                    lower = midpoint
                else:
                    upper = midpoint
            return (lower + upper) / 2

        first_z = inverse_normal(first_area)
        second_z = inverse_normal(second_area)
        if abs(first_z) < 0.00005:
            first_z = 0.0
        if abs(second_z) < 0.00005:
            second_z = 0.0
        first_sign_en = quantile_sign(first_area)
        second_sign_en = quantile_sign(second_area)
        if is_de:
            sign_words = {
                "negative": "negativ",
                "positive": "positiv",
                "zero": "null",
            }
            relation = (
                "kleiner als"
                if first_area < 0.5
                else "grösser als"
                if first_area > 0.5
                else "gleich"
            )
            solution = (
                f"Ein Quantil beginnt mit der kumulierten Wahrscheinlichkeit $q$ und löst $\\Phi(z)=q$ nach einer Position auf. "
                f"(a) Aus $\\Phi(z)={number(first_area,2)}$ folgt $z_{{{number(first_area*100,0)}\\%}}={number(first_z)}$. Weil {number(first_area,2)} {relation} 0.50 ist, ist diese Grenze {sign_words[first_sign_en]}. "
                f"(b) Aus $\\Phi(z)={number(second_area,2)}$ folgt $z_{{{number(second_area*100,0)}\\%}}={number(second_z)}$; das erwartete Vorzeichen ist {sign_words[second_sign_en]}. "
                "Die Eingaben sind Flächen, und die Ausgaben sind Positionen auf der z-Achse. Damit wird die Richtung einer gewöhnlichen CDF-Rechnung umgekehrt."
            )
        else:
            sign_words = {
                "negative": "negativ",
                "positive": "pozitiv",
                "zero": "zero",
            }
            relation = (
                "më e vogël se"
                if first_area < 0.5
                else "më e madhe se"
                if first_area > 0.5
                else "e barabartë me"
            )
            solution = (
                f"Një kuantil fillon me probabilitetin kumulativ $q$ dhe zgjidh $\\Phi(z)=q$ për një pozitë. "
                f"(a) $\\Phi(z)={number(first_area,2)}$ jep $z_{{{number(first_area*100,0)}\\%}}={number(first_z)}$. Meqë {number(first_area,2)} është {relation} 0.50, ky kufi është {sign_words[first_sign_en]}. "
                f"(b) $\\Phi(z)={number(second_area,2)}$ jep $z_{{{number(second_area*100,0)}\\%}}={number(second_z)}$; kufiri i dytë pritet të jetë {sign_words[second_sign_en]}. "
                "Hyrjet janë sipërfaqe, ndërsa daljet janë pozita në boshtin z. Kjo e përmbys drejtimin e një llogaritjeje të zakonshme të CDF-së."
            )
        solutions.append(task(2, 11, variant, title, solution))

    # A12: sampling distributions
    localized_sampling = (
        i18n.DE_SAMPLING if is_de else i18n.SQ_SAMPLING
    )
    heading_text = (
        "Stichprobenverteilung des Mittelwerts"
        if is_de
        else "Shpërndarja e kampionimit e mesatares"
    )
    exercises.append(heading(12, heading_text))
    solutions.append(heading(12, heading_text))
    for variant, (localized, canonical) in enumerate(
        zip(localized_sampling, SAMPLING), 1
    ):
        context, unit = localized
        _context, _unit, mean, variance, sample_size, new_variance, new_sample_size = canonical
        standard_deviation = math.sqrt(variance)
        standard_error = standard_deviation / math.sqrt(sample_size)
        variance_standard_error = math.sqrt(new_variance) / math.sqrt(sample_size)
        size_standard_error = standard_deviation / math.sqrt(new_sample_size)
        title = (
            f"Präzision eines Stichprobenmittelwerts: {context}"
            if is_de
            else f"Saktësia e mesatares së kampionit për {context}"
        )
        if is_de:
            setup = (
                f"Eine Populationsvariable für **{context}** (Einheit: **{unit}**) besitzt den Mittelwert $\\mu={mean}$ und die Varianz "
                f"$\\sigma^2={variance}$. Betrachte Stichproben mit $n={sample_size}$ unabhängigen Beobachtungen aus dieser Grundgesamtheit."
            )
            parts = [
                "bestimme $E(\\bar X)$ und $\\operatorname{SD}(\\bar X)$",
                f"bestimme den Standardfehler, wenn sich die Populationsvarianz auf {new_variance} ändert und $n={sample_size}$ bleibt",
                f"bestimme den Standardfehler, wenn die Varianz {variance} bleibt und die Stichprobengrösse sich auf $n={new_sample_size}$ ändert",
            ]
            reasoning = (
                "Erkläre getrennt, wie die Streuung der Grundgesamtheit und die Stichprobengrösse die Präzision des Stichprobenmittelwerts verändern."
            )
        else:
            setup = (
                f"Një ndryshore e popullatës që mat {context} në {unit} ka mesatare $\\mu={mean}$ dhe variancë "
                f"$\\sigma^2={variance}$. Shqyrto kampione me $n={sample_size}$ vëzhgime të pavarura nga kjo popullatë."
            )
            parts = [
                "gjej $E(\\bar X)$ dhe $\\operatorname{SD}(\\bar X)$",
                f"gjej gabimin standard nëse varianca e popullatës ndryshon në {new_variance}, ndërsa $n={sample_size}$",
                f"gjej gabimin standard nëse varianca mbetet {variance}, por madhësia e kampionit ndryshon në $n={new_sample_size}$",
            ]
            reasoning = (
                "Shpjego veçmas si e ndryshojnë ndryshueshmëria e popullatës dhe madhësia e kampionit saktësinë e mesatares së kampionit."
            )
        prompt = varied_exercise_localized(
            locale, variant, setup, parts, reasoning
        )
        exercises.append(task(2, 12, variant, title, prompt))
        if is_de:
            variance_direction = (
                "grössere" if new_variance > variance else "kleinere"
            )
            variance_effect = (
                "erhöht" if variance_standard_error > standard_error else "verringert"
            )
            sample_direction = (
                "grössere" if new_sample_size > sample_size else "kleinere"
            )
            sample_effect = (
                "verringert" if size_standard_error < standard_error else "erhöht"
            )
            solution = (
                f"Für einen erwartungstreuen Stichprobenmittelwert gilt $E(\\bar X)=\\mu={mean}$. Aus der Unabhängigkeit folgt $\\operatorname{{SD}}(\\bar X)=\\sigma/\\sqrt n$. "
                f"(a) $\\sigma=\\sqrt{{{variance}}}={number(standard_deviation,2)}$. Daher ist $\\operatorname{{SE}}={number(standard_deviation,2)}/\\sqrt{{{sample_size}}}={number(standard_error)}$ {unit}. "
                f"Über wiederholte Stichproben beträgt der Mittelwert ihrer Mittelwerte {mean} {unit}; ihre Standardabweichung beträgt {number(standard_error)} {unit}. "
                f"(b) Bei Varianz {new_variance} ist $\\operatorname{{SE}}=\\sqrt{{{new_variance}}}/\\sqrt{{{sample_size}}}={number(variance_standard_error)}$ {unit}. Die {variance_direction} Populationsvarianz {variance_effect} den SE gegenüber Teil (a). "
                f"(c) Bei $n={new_sample_size}$ ist $\\operatorname{{SE}}=\\sqrt{{{variance}}}/\\sqrt{{{new_sample_size}}}={number(size_standard_error)}$ {unit}. Die {sample_direction} Stichprobe {sample_effect} den SE über die Quadratwurzel aus $n$. "
                "Ein kleinerer SE bedeutet, dass die Mittelwerte wiederholter Stichproben dichter um den Populationsmittelwert liegen."
            )
        else:
            variance_direction = (
                "më e madhe" if new_variance > variance else "më e vogël"
            )
            variance_effect = (
                "e rrit" if variance_standard_error > standard_error else "e zvogëlon"
            )
            sample_direction = (
                "më e madhe" if new_sample_size > sample_size else "më e vogël"
            )
            sample_effect = (
                "e zvogëlon" if size_standard_error < standard_error else "e rrit"
            )
            solution = (
                f"Për një mesatare të paanshme të kampionit, $E(\\bar X)=\\mu={mean}$. Pavarësia jep $\\operatorname{{SD}}(\\bar X)=\\sigma/\\sqrt n$. "
                f"(a) $\\sigma=\\sqrt{{{variance}}}={number(standard_deviation,2)}$, prandaj $\\operatorname{{SE}}={number(standard_deviation,2)}/\\sqrt{{{sample_size}}}={number(standard_error)}$ {unit}. "
                f"Në kampione të përsëritura, mesataret përqendrohen te {mean} {unit} me devijim standard {number(standard_error)} {unit}. "
                f"(b) Me variancë {new_variance}, $\\operatorname{{SE}}=\\sqrt{{{new_variance}}}/\\sqrt{{{sample_size}}}={number(variance_standard_error)}$ {unit}. Varianca {variance_direction} e popullatës {variance_effect} SE-në kundrejt pjesës (a). "
                f"(c) Me $n={new_sample_size}$, $\\operatorname{{SE}}=\\sqrt{{{variance}}}/\\sqrt{{{new_sample_size}}}={number(size_standard_error)}$ {unit}. Madhësia {sample_direction} e kampionit {sample_effect} SE-në përmes rrënjës katrore të $n$. "
                "SE më e vogël do të thotë se mesataret e kampioneve të përsëritura grumbullohen më afër mesatares së popullatës."
            )
        solutions.append(task(2, 12, variant, title, solution))

    # A13: normal intervals
    localized_intervals = (
        i18n.DE_NORMAL_INTERVALS if is_de else i18n.SQ_NORMAL_INTERVALS
    )
    heading_text = (
        "Intervalle unter einem Normalmodell"
        if is_de
        else "Intervalet nën një model normal"
    )
    exercises.append(heading(13, heading_text))
    solutions.append(heading(13, heading_text))
    for variant, (localized, canonical) in enumerate(
        zip(localized_intervals, NORMAL_INTERVALS), 1
    ):
        context, unit = localized
        _context, _unit, mean, variance, a, b, c, d = canonical
        standard_deviation = math.sqrt(variance)
        z_a = (a - mean) / standard_deviation
        z_b = (b - mean) / standard_deviation
        z_c = (c - mean) / standard_deviation
        z_d = (d - mean) / standard_deviation
        first_probability = probability_normal(z_b) - probability_normal(z_a)
        second_probability = probability_normal(z_d) - probability_normal(z_c)
        title = (
            f"Intervallwahrscheinlichkeiten: {context}"
            if is_de
            else f"Probabilitetet e intervaleve për {context}"
        )
        if is_de:
            setup = (
                f"$X$ bezeichnet **{context}** (Einheit: **{unit}**) und folgt $N({mean},{variance})$, wobei der zweite Parameter die Varianz ist."
            )
            parts = [
                f"berechne $P({a}<X\\leq {b})$",
                f"berechne $P({c}<X\\leq {d})$",
            ]
            reasoning = (
                "Standardisiere bei beiden Intervallen jede Grenze, subtrahiere die CDF-Werte in der richtigen Reihenfolge und interpretiere das Ergebnis als modellierten Anteil."
            )
        else:
            setup = (
                f"Supozo se $X$ mat {context} në {unit} dhe ndjek $N({mean},{variance})$, ku parametri i dytë është varianca."
            )
            parts = [
                f"llogarit $P({a}<X\\leq {b})$",
                f"llogarit $P({c}<X\\leq {d})$",
            ]
            reasoning = (
                "Për të dy intervalet, standardizo secilin kufi, zbrit vlerat e CDF-së në rendin e duhur dhe interpretoje rezultatin si përpjesëtim të modeluar."
            )
        prompt = varied_exercise_localized(
            locale, variant, setup, parts, reasoning
        )
        exercises.append(task(2, 13, variant, title, prompt))
        if is_de:
            solution = (
                f"Die Standardabweichung ist $\\sigma=\\sqrt{{{variance}}}={number(standard_deviation,2)}$. "
                f"(a) Die Grenzen lauten $z_a=({a}-{mean})/{number(standard_deviation,2)}\\approx {number(z_a)}$ und $z_b=({b}-{mean})/{number(standard_deviation,2)}\\approx {number(z_b)}$. "
                f"Mit den ungerundeten z-Werten gilt $P({a}<X\\leq {b})=\\Phi(({b}-{mean})/{number(standard_deviation,2)})-\\Phi(({a}-{mean})/{number(standard_deviation,2)})={number(first_probability)}$. "
                f"Der modellierte Anteil beträgt somit {number(first_probability)} für den Wertebereich **{a} bis {b} {unit}**. "
                f"(b) $z_c=({c}-{mean})/{number(standard_deviation,2)}\\approx {number(z_c)}$ und $z_d=({d}-{mean})/{number(standard_deviation,2)}\\approx {number(z_d)}$. Daher ist "
                f"$P({c}<X\\leq {d})=\\Phi(({d}-{mean})/{number(standard_deviation,2)})-\\Phi(({c}-{mean})/{number(standard_deviation,2)})={number(second_probability)}$. "
                f"Dies ist der modellierte Anteil für den Wertebereich **{c} bis {d} {unit}**. Bei einem stetigen Modell verändert die Einbeziehung einer Grenze die Wahrscheinlichkeit nicht."
            )
        else:
            solution = (
                f"Devijimi standard është $\\sigma=\\sqrt{{{variance}}}={number(standard_deviation,2)}$. "
                f"(a) Kufijtë janë $z_a=({a}-{mean})/{number(standard_deviation,2)}\\approx {number(z_a)}$ dhe $z_b=({b}-{mean})/{number(standard_deviation,2)}\\approx {number(z_b)}$. "
                f"Duke përdorur vlerat z të parrumbullakosura, $P({a}<X\\leq {b})=\\Phi(({b}-{mean})/{number(standard_deviation,2)})-\\Phi(({a}-{mean})/{number(standard_deviation,2)})={number(first_probability)}$. "
                f"Prandaj modeli vendos përpjesëtimin {number(first_probability)} të vlerave të ndryshores nga {a} deri në {b} {unit}. "
                f"(b) $z_c=({c}-{mean})/{number(standard_deviation,2)}\\approx {number(z_c)}$ dhe $z_d=({d}-{mean})/{number(standard_deviation,2)}\\approx {number(z_d)}$, duke dhënë "
                f"$P({c}<X\\leq {d})=\\Phi(({d}-{mean})/{number(standard_deviation,2)})-\\Phi(({c}-{mean})/{number(standard_deviation,2)})={number(second_probability)}$. "
                f"Ky është përpjesëtimi i modeluar nga {c} deri në {d} {unit}. Përfshirja e kufirit nuk e ndryshon probabilitetin e një modeli të vazhdueshëm."
            )
        solutions.append(task(2, 13, variant, title, solution))

    # A14: sampling bias
    localized_sampling_bias = (
        i18n.DE_SAMPLING_BIAS if is_de else i18n.SQ_SAMPLING_BIAS
    )
    heading_text = (
        "Grundgesamtheit, Stichprobe und Auswahlverzerrung"
        if is_de
        else "Popullata, kampioni dhe anshmëria e përzgjedhjes"
    )
    exercises.append(heading(14, heading_text))
    solutions.append(heading(14, heading_text))
    for variant, (
        title,
        scenario,
        population,
        frame,
        sample,
        parameter,
        statistic,
        biases,
        design,
    ) in enumerate(localized_sampling_bias, 1):
        if is_de:
            parts = [
                "bestimme die Zielpopulation",
                "unterscheide den operativen Auswahlrahmen von der tatsächlich erreichten Stichprobe",
                "formuliere einen Populationsparameter, der zur Forschungsbehauptung passt",
                "formuliere die entsprechende Stichprobenstatistik und ihre Beobachtungseinheit",
            ]
            reasoning = (
                "Erkläre mindestens zwei zur Situation passende Mechanismen der Unterabdeckung, Auswahl oder Nichtantwort. Sage, was eine grössere Stichprobe reparieren würde und was nicht, und schlage ein besser begründetes Design vor."
            )
        else:
            parts = [
                "përcakto popullatën e synuar",
                "dallo kornizën operative të kampionimit nga kampioni i arritur",
                "jep një parametër të popullatës që përputhet me pretendimin kërkimor",
                "jep statistikën përkatëse të kampionit dhe njësinë e saj të vëzhgimit",
            ]
            reasoning = (
                "Shpjego të paktën dy mekanizma të mbulimit, përzgjedhjes ose mospërgjigjes që lidhen me situatën. Thuaj çfarë do të rregullonte një kampion më i madh dhe çfarë nuk do të rregullonte, pastaj propozo një dizajn më të mbrojtshëm."
            )
        prompt = varied_exercise_localized(
            locale, variant, scenario, parts, reasoning
        )
        exercises.append(task(2, 14, variant, title, prompt))
        if is_de:
            solution = (
                f"(a) Zielpopulation: {population}. (b) Der operative Auswahlrahmen umfasst {frame}. Die erreichte Stichprobe umfasst {sample}. "
                "Diese Trennung ist wichtig: Der Rahmen beschreibt, wer oder was einen Weg zur Auswahl besass, während die Stichprobe die tatsächlich beobachteten Einheiten enthält. "
                f"(c) Passender Populationsparameter: {parameter}. (d) Stichprobenstatistik: {statistic}. Die wichtigsten Gefahren sind designspezifisch: {biases} "
                "Eine grössere Stichprobe aus demselben Mechanismus würde die zufällige Stichprobenvariation um den rahmenspezifischen Wert dieses Mechanismus verringern. Diese grössere Stichprobe würde die identifizierten systematischen Abdeckungs- oder Auswahlmechanismen aber nicht reparieren. "
                f"Ein besser begründeter Ansatz ist: {design}"
            )
        else:
            solution = (
                f"(a) Popullata e synuar: {population}. (b) Korniza operative e kampionimit: {frame}. Kampioni i arritur: {sample}. "
                "Kjo ndarje ka rëndësi: korniza përshkruan kush ose çfarë kishte rrugë për t'u përzgjedhur, ndërsa kampioni përmban njësitë që u vëzhguan vërtet. "
                f"(c) Parametri përkatës i popullatës: {parameter}. (d) Statistika e kampionit: {statistic}. Kërcënimet kryesore lidhen me këtë dizajn: {biases} "
                "Një kampion më i madh nga i njëjti mekanizëm do ta zvogëlonte ndryshueshmërinë e rastësishme të kampionimit rreth vlerës së kornizës së këtij mekanizmi, por nuk do t'i rregullonte mekanizmat sistematikë të mbulimit ose përzgjedhjes. "
                f"Një qasje më e mbrojtshme është: {design[0].lower() + design[1:]}"
            )
        solutions.append(task(2, 14, variant, title, solution))

    # A15: worksheet-2 case-2 sampling-frame and profile coverage objective
    localized_coverage = (
        i18n.DE_COVERAGE_CLAIMS if is_de else i18n.SQ_COVERAGE_CLAIMS
    )
    heading_text = (
        "Abdeckungsfehler und die Population hinter einer Prozentzahl"
        if is_de
        else "Gabimi i mbulimit dhe popullata pas një përqindjeje"
    )
    exercises.append(heading(15, heading_text))
    solutions.append(heading(15, heading_text))
    for variant, (
        title,
        claim,
        target,
        observed,
        coverage,
        honest,
        design,
    ) in enumerate(localized_coverage, 1):
        if is_de:
            parts = [
                "nenne die in der breiten Behauptung bezeichnete Population",
                "bestimme die Einheiten, die tatsächlich einen Weg in die berichtete Prozentzahl hatten",
                "erkläre, weshalb der beobachtete Auswahlrahmen die genannte Population nicht abdeckt",
                "formuliere das Ergebnis so um, dass es nur die beobachteten Daten beschreibt",
            ]
            reasoning = (
                "Schlage danach ein Stichprobendesign vor, das besser zur breiten Population passt. Erkläre zudem, weshalb mehr Beobachtungen aus demselben eingeschränkten Rahmen das Problem nicht lösen."
            )
        else:
            parts = [
                "thuaj popullatën e emërtuar në pretendimin e gjerë",
                "përcakto njësitë që kishin vërtet një rrugë për të hyrë në përqindjen e raportuar",
                "shpjego pse korniza e vëzhguar nuk e mbulon popullatën e emërtuar",
                "rishkruaje rezultatin në mënyrë që të përshkruajë vetëm të dhënat e vëzhguara",
            ]
            reasoning = (
                "Pastaj propozo një dizajn kampionimi që përputhet më mirë me popullatën e gjerë. Shpjego pse mbledhja e më shumë vëzhgimeve përmes së njëjtës kornizë të kufizuar nuk e zgjidh problemin."
            )
        prompt = varied_exercise_localized(
            locale, variant, claim, parts, reasoning
        )
        exercises.append(task(2, 15, variant, title, prompt))
        if is_de:
            solution = (
                f"(a) Die breite Behauptung nennt {target}. (b) Einen Weg in die Berechnung hatten {observed}. "
                f"(c) Der Abdeckungsfehler entsteht aus folgendem Grund: {coverage} Die Prozentzahl kann für die beobachteten Datensätze korrekt berechnet sein und dennoch den Anteil in der breiteren Population nicht schätzen. "
                f"(d) Eine ehrliche deskriptive Aussage lautet: «{honest}» Eine besser begründete Studie würde {design}. "
                "Mehr Datensätze über denselben eingeschränkten Weg würden die Prozentzahl für diesen Rahmen präziser machen, aber keine Personengruppen hinzufügen, die nie in den Rahmen gelangen konnten."
            )
        else:
            solution = (
                f"(a) Pretendimi i gjerë emërton {target}. (b) Njësitë me rrugë për të hyrë në llogaritje janë {observed}. "
                f"(c) Gabimi i mbulimit lind për këtë arsye: {coverage} Përqindja mund të llogaritet saktë për regjistrimet e vëzhguara dhe prapëseprapë të mos e vlerësojë përqindjen në popullatën më të gjerë. "
                f"(d) Një pohim i sinqertë përshkrues është: «{honest}» Një studim më i mbrojtshëm do të ndiqte këtë plan: {design}. "
                "Rritja e numrit të regjistrimeve nga e njëjta rrugë e kufizuar do ta bënte më të saktë përqindjen për atë kornizë, por nuk do të shtonte llojet e njerëzve që nuk hynë kurrë në të."
            )
        solutions.append(task(2, 15, variant, title, solution))

    # A16: worksheet-2 survivorship-selection objective
    localized_survivorship = (
        i18n.DE_SURVIVOR_SELECTION
        if is_de
        else i18n.SQ_SURVIVOR_SELECTION
    )
    heading_text = (
        "Survivorship-Bias und fehlende Ergebnisse"
        if is_de
        else "Anshmëria e mbijetesës dhe rezultatet që mungojnë"
    )
    exercises.append(heading(16, heading_text))
    solutions.append(heading(16, heading_text))
    for variant, (
        title,
        scenario,
        observed,
        missing,
        distortion,
        action,
    ) in enumerate(localized_survivorship, 1):
        if is_de:
            parts = [
                "bestimme die Fälle, die beobachtbar bleiben",
                "bestimme die relevanten Fälle, die in der beobachteten Gruppe fehlen",
                "erkläre, wie das Ergebnis selbst beeinflussen kann, ob ein Fall beobachtet wird",
                "erkläre, weshalb eine Analyse nur der beobachteten Fälle zur falschen Schlussfolgerung führen kann",
            ]
            reasoning = (
                "Beschreibe abschliessend, welche zusätzliche Evidenz oder Nachverfolgung vor der beabsichtigten Populationsaussage nötig ist."
            )
        else:
            parts = [
                "përcakto rastet që mbeten të vëzhgueshme",
                "përcakto rastet përkatëse që mungojnë nga grupi i vëzhguar",
                "shpjego si mund të ndikojë vetë rezultati në vëzhgimin e rastit",
                "thuaj pse analiza vetëm e rasteve të vëzhguara mund të çojë drejt përfundimit të gabuar",
            ]
            reasoning = (
                "Në fund përshkruaj çfarë prove ose ndjekjeje shtesë nevojitet para se të bëhet pretendimi i synuar për popullatën."
            )
        prompt = varied_exercise_localized(
            locale, variant, scenario, parts, reasoning
        )
        exercises.append(task(2, 16, variant, title, prompt))
        if is_de:
            solution = (
                f"(a) Die beobachtete Gruppe enthält {observed}. (b) In dieser Gruppe fehlen {missing}. "
                f"(c) Der Auswahlprozess hängt mit dem Ergebnis zusammen: {distortion} Dies ist Survivorship-Bias. Damit ist gemeint, dass ein Fall für die Beobachtung verfügbar bleiben muss, obwohl gerade das Verschwinden wichtige Information tragen kann. "
                "(d) Wer nur die beobachteten Fälle untersucht, bedingt die Analyse auf Überleben, Abschluss, Rückkehr oder Verbleib. Dadurch können Misserfolge verborgen bleiben und die praktische Lehre kann sich umkehren. "
                f"Der nächste Schritt ist: {action}. Das Ziel besteht nicht darin, fehlende Ergebnisse zu erraten. Die Erhebung soll vielmehr so gestaltet werden, dass fortbestehende und nicht fortbestehende Fälle Evidenz beitragen."
            )
        else:
            solution = (
                f"(a) Grupi i vëzhguar përmban {observed}. (b) Nga ky grup mungojnë {missing}. "
                f"(c) Procesi i përzgjedhjes lidhet me rezultatin: {distortion} Kjo është anshmëri e mbijetesës. Një rast duhet të mbetet i disponueshëm që të vëzhgohet, edhe pse pikërisht mungesa e tij nga të dhënat mund të mbartë informacion të rëndësishëm. "
                "(d) Vëzhgimi vetëm i rasteve të dukshme e kushtëzon analizën mbi mbijetesën, përfundimin, kthimin ose qëndrimin. Kjo mund t'i fshehë dështimet dhe ta përmbysë mësimin praktik. "
                f"Hapi tjetër është: {action[0].lower() + action[1:]}. Qëllimi nuk është të hamendësohen rezultatet që mungojnë, por të ridizajnohet mbledhja që rastet që vazhdojnë dhe ato që nuk vazhdojnë të japin prova."
            )
        solutions.append(task(2, 16, variant, title, solution))

    def collapse_groups(fragments: list[str]) -> list[str]:
        sections: list[str] = []
        current: list[str] = []
        for fragment in fragments:
            if fragment.startswith("# A") and current:
                sections.append("".join(current).rstrip() + "\n\n")
                current = []
            current.append(fragment)
        if current:
            sections.append("".join(current).rstrip() + "\n\n")
        if len(sections) != 16:
            raise ValueError("localized render must contain exactly 16 groups")
        return sections

    return collapse_groups(exercises), collapse_groups(solutions)


def _sections_from_english_render(text: str) -> list[str]:
    """Extract the canonical English A01-A16 sections for shared pair writing."""

    sections = re.findall(
        r"(?ms)^# A\d{2}:.*?(?=^# A\d{2}:|\Z)", text
    )
    if len(sections) != 16:
        raise ValueError("canonical English render must contain exactly 16 groups")
    return [section.rstrip() + "\n\n" for section in sections]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--locale", choices=("en", "de", "sq"), default="en")
    args = parser.parse_args()
    if args.locale == "en":
        exercise_text, solution_text = render_english()
        exercise_sections = _sections_from_english_render(exercise_text)
        solution_sections = _sections_from_english_render(solution_text)
    else:
        exercise_sections, solution_sections = render_localized(args.locale)
    exercise_path, solution_path = write_pair(
        2,
        args.locale,
        16,
        exercise_sections,
        solution_sections,
    )
    print(
        f"Generated and source-validated Topic 2 {args.locale} sources: "
        f"{exercise_path.name}, {solution_path.name}."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
