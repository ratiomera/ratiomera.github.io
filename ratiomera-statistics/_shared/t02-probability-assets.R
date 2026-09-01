# Shared theory figures for Probability, Topic 2.
# Each language page sets `topic_locale` before sourcing this file. Data,
# formulas, seeds, scales, and geometry remain identical across locales.

if (!exists("topic_locale", inherits = FALSE)) topic_locale <- "en"
if (!topic_locale %in% c("en", "de", "sq")) {
  stop("Unsupported Topic 2 locale: ", topic_locale, call. = FALSE)
}

if (!exists("ratiomera_prepare_plotly_widget", mode = "function")) {
  plotly_helper_candidates <- c(
    "../../_shared/plotly-helpers.R",
    "ratiomera-statistics/_shared/plotly-helpers.R"
  )
  plotly_helper_path <- plotly_helper_candidates[
    file.exists(plotly_helper_candidates)
  ][[1]]
  source(plotly_helper_path, local = TRUE)
}

required_topic2_packages <- c(
  "dplyr", "tibble", "tidyr", "ggplot2", "DT", "plotly", "htmlwidgets", "knitr"
)
missing_topic2_packages <- required_topic2_packages[
  !vapply(required_topic2_packages, requireNamespace, logical(1), quietly = TRUE)
]
if (length(missing_topic2_packages)) {
  stop(
    "Topic 2 requires these R packages: ",
    paste(missing_topic2_packages, collapse = ", "),
    call. = FALSE
  )
}

suppressPackageStartupMessages({
  library(dplyr)
  library(tibble)
  library(tidyr)
  library(ggplot2)
  library(DT)
  library(plotly)
  library(knitr)
})

topic2_labels <- list(
  en = list(
    event_title = "Events as Sets of Outcomes",
    event_subtitle = "Overlap is the intersection; both circles together form the union",
    event_a = "Event A",
    event_b = "Event B",
    intersection = "A and B",
    operations_title = "Four Event Operations on One Sample Space",
    operations_subtitle = "The highlighted tiles show which outcomes belong to the named event",
    operation_union = "Union: A or D or both",
    operation_intersection = "Intersection: both A and D",
    operation_complement = "Complement: not A",
    operation_disjoint = "Disjoint events: A and B never overlap",
    operation_union_result = "A or D: {1, 2, 3, 7}",
    operation_intersection_result = "A and D: {2, 3}",
    operation_complement_result = "Not A: {4, 5, 6, 7, 8, 9, 10}",
    operation_disjoint_result = "A and B: no shared outcomes",
    sample_space_short = "Sample space",
    chain_title = "A Three-Stage Conditional Probability Chain",
    chain_subtitle = "Each later probability is conditional on all earlier successes",
    chain_start = "Start",
    chain_stage_1 = "Record located",
    chain_stage_2 = "Usable scan",
    chain_stage_3 = "Metadata verified",
    bayes_title = "Why the Starting Proportion Changes What a Positive Result Means",
    bayes_subtitle = "Expected positive results among 10 000 hypothetical people with the stated rates",
    bayes_status = "Condition status",
    bayes_count = "Expected positive results",
    bayes_present = "Present: true positives",
    bayes_absent = "Absent: false positives",
    pmf_cdf_title = "One Discrete Distribution, Two Views",
    pmf_cdf_subtitle = "The PMF shows separate probabilities; the CDF adds them from left to right",
    pmf = "Probability mass function",
    cdf = "Cumulative distribution function",
    requests = "Follow-up requests",
    value = "Value",
    probability = "Probability",
    density_title = "Probability Is Area under a Density",
    density_subtitle = "The shaded interval has positive probability; one exact point has probability zero",
    standard_value = "Standardized value",
    density = "Density",
    binomial_title = "Binomial Shape Depends on the Success Probability",
    binomial_subtitle = "Every panel uses n = 12 independent trials",
    successes = "Number of successes",
    normal_title = "Four Normal-Distribution Question Types",
    normal_subtitle = "Direction and boundaries determine which area or cutoff is required",
    below = "Below a cutoff",
    above = "Above a cutoff",
    between = "Between two cutoffs",
    inverse = "Cutoff for 99% below",
    sampling_title = "How Sample Size Changes Sampling Distributions",
    sampling_subtitle = "1 500 simulated means per panel from standardized source populations",
    normal_source = "Normal source",
    uniform_source = "Uniform source",
    skewed_source = "Right-skewed source",
    sample_mean = "Sample mean",
    simulation_density = "Simulation density",
    sample_size = "Sample size",
    sampling_process_title = "From a Population to a Sampling Distribution",
    sampling_process_subtitle = "Repeated random samples produce different sample means",
    process_stage = "Stage",
    process_population = "Population\nall possible units",
    process_samples = "Many random samples\nof size n",
    process_means = "One mean from\neach sample",
    process_distribution = "Sampling distribution\nof the sample mean",
    process_draw = "draw",
    process_calculate = "calculate",
    process_collect = "collect",
    bias_title = "A Large Sample Can Still Miss the Population Mean",
    bias_subtitle = "In this simulation, people with higher interest are more likely to respond",
    target = "Target population",
    random_sample = "Random sample",
    respondents = "Voluntary respondents",
    mean_outcome = "Mean interest score",
    low_stress = "Low stress",
    high_stress = "High stress",
    high_anxiety = "High anxiety",
    low_anxiety = "Low anxiety",
    high_anxiety_event = "High anxiety (score >= 23)",
    low_anxiety_event = "Low anxiety (score < 23)",
    high_stress_event = "High stress group",
    low_stress_event = "Low stress group",
    total = "Total",
    group = "Group",
    cond_high = "P(high anxiety | group)",
    cond_low = "P(low anxiety | group)",
    high_anxiety_probability = "Probability of high anxiety",
    cond_title = "Conditional probability of high anxiety by stress group",
    stress_group = "Stress group",
    anxiety_level = "Anxiety level",
    normal_fit_title = "Exam anxiety scores with fitted normal distribution",
    normal_fit_mean = "Mean",
    normal_fit_boundary = "23-or-above boundary at 22.5 (orange dashed line)",
    exam_score = "Exam anxiety score (0–40)",
    continuous_model_value = "Value before rounding",
    binomial_count = "Number of students with high anxiety",
    binomial_expected = "E(X)",
    sampling_mean_title = "Sampling distribution of the mean",
    sample_means_mean = "Mean of sample means",
    plugin_se = "plug-in SE estimate",
    sample_mean_anxiety = "Sample mean exam anxiety",
    participant_id = "Participant ID",
    exam_anxiety_score = "Exam anxiety score"
  ),
  de = list(
    event_title = "Ereignisse als Ergebnismengen",
    event_subtitle = "Die Überlappung ist der Schnitt; beide Kreise zusammen bilden die Vereinigung",
    event_a = "Ereignis A",
    event_b = "Ereignis B",
    intersection = "A und B",
    operations_title = "Vier Ereignisoperationen im selben Ergebnisraum",
    operations_subtitle = "Die hervorgehobenen Felder zeigen, welche Ergebnisse zum genannten Ereignis gehören",
    operation_union = "Vereinigung: A oder D oder beide",
    operation_intersection = "Schnitt: sowohl A als auch D",
    operation_complement = "Komplement: nicht A",
    operation_disjoint = "Disjunkte Ereignisse: A und B überlappen nie",
    operation_union_result = "A oder D: {1, 2, 3, 7}",
    operation_intersection_result = "A und D: {2, 3}",
    operation_complement_result = "Nicht A: {4, 5, 6, 7, 8, 9, 10}",
    operation_disjoint_result = "A und B: keine gemeinsamen Ergebnisse",
    sample_space_short = "Ergebnisraum",
    chain_title = "Eine dreistufige bedingte Wahrscheinlichkeitskette",
    chain_subtitle = "Jede spätere Wahrscheinlichkeit ist durch alle früheren Erfolge bedingt",
    chain_start = "Start",
    chain_stage_1 = "Datensatz gefunden",
    chain_stage_2 = "Brauchbarer Scan",
    chain_stage_3 = "Metadaten geprüft",
    bayes_title = "Weshalb der Ausgangsanteil die Bedeutung eines positiven Ergebnisses verändert",
    bayes_subtitle = "Erwartete positive Ergebnisse unter 10 000 hypothetischen Personen bei den angegebenen Raten",
    bayes_status = "Zustand",
    bayes_count = "Erwartete positive Ergebnisse",
    bayes_present = "Vorhanden: richtig positiv",
    bayes_absent = "Nicht vorhanden: falsch positiv",
    pmf_cdf_title = "Eine diskrete Verteilung in zwei Darstellungen",
    pmf_cdf_subtitle = "Die Wahrscheinlichkeitsfunktion zeigt einzelne Wahrscheinlichkeiten; die Verteilungsfunktion addiert sie von links nach rechts",
    pmf = "Wahrscheinlichkeitsfunktion",
    cdf = "Kumulative Verteilungsfunktion",
    requests = "Rückfragen",
    value = "Wert",
    probability = "Wahrscheinlichkeit",
    density_title = "Wahrscheinlichkeit ist eine Fläche unter der Dichte",
    density_subtitle = "Das markierte Intervall hat positive Wahrscheinlichkeit; ein einzelner Punkt hat Wahrscheinlichkeit null",
    standard_value = "Standardisierter Wert",
    density = "Dichte",
    binomial_title = "Die Form der Binomialverteilung hängt von der Erfolgswahrscheinlichkeit ab",
    binomial_subtitle = "Jede Teilgrafik verwendet n = 12 unabhängige Versuche",
    successes = "Anzahl Erfolge",
    normal_title = "Vier Fragetypen zur Normalverteilung",
    normal_subtitle = "Richtung und Grenzen bestimmen die gesuchte Fläche oder den gesuchten Grenzwert",
    below = "Unter einem Grenzwert",
    above = "Über einem Grenzwert",
    between = "Zwischen zwei Grenzwerten",
    inverse = "Grenzwert für 99% darunter",
    sampling_title = "Wie die Stichprobengrösse Stichprobenverteilungen verändert",
    sampling_subtitle = "1 500 simulierte Mittelwerte je Teilgrafik aus standardisierten Ausgangspopulationen",
    normal_source = "Normale Ausgangsverteilung",
    uniform_source = "Gleichverteilte Ausgangsverteilung",
    skewed_source = "Rechtsschiefe Ausgangsverteilung",
    sample_mean = "Stichprobenmittelwert",
    simulation_density = "Simulationsdichte",
    sample_size = "Stichprobengrösse",
    sampling_process_title = "Von der Grundgesamtheit zur Stichprobenverteilung",
    sampling_process_subtitle = "Wiederholte Zufallsstichproben ergeben unterschiedliche Stichprobenmittelwerte",
    process_stage = "Schritt",
    process_population = "Grundgesamtheit\nalle möglichen Einheiten",
    process_samples = "Viele Zufallsstichproben\nmit Umfang n",
    process_means = "Ein Mittelwert aus\njeder Stichprobe",
    process_distribution = "Stichprobenverteilung\ndes Mittelwerts",
    process_draw = "ziehen",
    process_calculate = "berechnen",
    process_collect = "zusammenfassen",
    bias_title = "Auch eine grosse Stichprobe kann den\nMittelwert der Grundgesamtheit verfehlen",
    bias_subtitle = "In dieser Simulation antworten Personen mit höherem Interesse eher",
    target = "Zielpopulation",
    random_sample = "Zufallsstichprobe",
    respondents = "Freiwillig Antwortende",
    mean_outcome = "Mittlerer Interessenwert",
    low_stress = "Niedriger Stress",
    high_stress = "Hoher Stress",
    high_anxiety = "Hohe Prüfungsangst",
    low_anxiety = "Niedrige Prüfungsangst",
    high_anxiety_event = "Hohe Prüfungsangst (Wert >= 23)",
    low_anxiety_event = "Niedrige Prüfungsangst (Wert < 23)",
    high_stress_event = "Gruppe mit hohem Stress",
    low_stress_event = "Gruppe mit niedrigem Stress",
    total = "Gesamt",
    group = "Gruppe",
    cond_high = "P(hohe Prüfungsangst | Gruppe)",
    cond_low = "P(niedrige Prüfungsangst | Gruppe)",
    high_anxiety_probability = "Wahrscheinlichkeit hoher Prüfungsangst",
    cond_title = "Bedingte Wahrscheinlichkeit hoher Prüfungsangst nach Stressgruppe",
    stress_group = "Stressgruppe",
    anxiety_level = "Prüfungsangst",
    normal_fit_title = "Prüfungsangstwerte mit angepasster Normalverteilung",
    normal_fit_mean = "Mittelwert",
    normal_fit_boundary = "Grenze für mindestens 23 bei 22.5 (orange gestrichelte Linie)",
    exam_score = "Prüfungsangstwert (0–40)",
    continuous_model_value = "Kontinuierlicher Modellwert vor dem Runden",
    binomial_count = "Anzahl Studierende mit hoher Prüfungsangst",
    binomial_expected = "E(X)",
    sampling_mean_title = "Stichprobenverteilung des Mittelwerts",
    sample_means_mean = "Mittelwert der Stichprobenmittelwerte",
    plugin_se = "geschätzter Plug-in-Standardfehler",
    sample_mean_anxiety = "Stichprobenmittelwert der Prüfungsangst",
    participant_id = "Teilnehmenden-ID",
    exam_anxiety_score = "Prüfungsangstwert"
  ),
  sq = list(
    event_title = "Ngjarjet si bashkësi rezultatesh",
    event_subtitle = "Mbivendosja është prerja; të dy rrathët së bashku formojnë bashkimin",
    event_a = "Ngjarja A",
    event_b = "Ngjarja B",
    intersection = "A dhe B",
    operations_title = "Katër veprime me ngjarje në të njëjtën hapësirë të rezultateve",
    operations_subtitle = "Fushat e theksuara tregojnë cilat rezultate i përkasin ngjarjes së emërtuar",
    operation_union = "Bashkimi: A ose D ose të dyja",
    operation_intersection = "Prerja: edhe A, edhe D",
    operation_complement = "Komplementi: jo A",
    operation_disjoint = "Ngjarje disjunkte: A dhe B nuk mbivendosen kurrë",
    operation_union_result = "A ose D: {1, 2, 3, 7}",
    operation_intersection_result = "A dhe D: {2, 3}",
    operation_complement_result = "Jo A: {4, 5, 6, 7, 8, 9, 10}",
    operation_disjoint_result = "A dhe B: asnjë rezultat i përbashkët",
    sample_space_short = "Hapësira e rezultateve",
    chain_title = "Një zinxhir probabiliteti të kushtëzuar me tri faza",
    chain_subtitle = "Çdo probabilitet i mëvonshëm kushtëzohet nga të gjitha sukseset e mëparshme",
    chain_start = "Fillimi",
    chain_stage_1 = "U gjet regjistrimi",
    chain_stage_2 = "Skanim i përdorshëm",
    chain_stage_3 = "U verifikuan metadatat",
    bayes_title = "Pse përqindja fillestare e ndryshon kuptimin e një rezultati pozitiv",
    bayes_subtitle = "Rezultatet pozitive të pritshme mes 10 000 personave hipotetikë me normat e dhëna",
    bayes_status = "Gjendja",
    bayes_count = "Rezultatet pozitive të pritshme",
    bayes_present = "E pranishme: pozitive të vërteta",
    bayes_absent = "Jo e pranishme: pozitive të rreme",
    pmf_cdf_title = "Një shpërndarje diskrete në dy pamje",
    pmf_cdf_subtitle = "Funksioni i masës tregon probabilitete të veçanta; funksioni kumulativ i mbledh nga e majta në të djathtë",
    pmf = "Funksioni i masës së probabilitetit",
    cdf = "Funksioni kumulativ i shpërndarjes",
    requests = "Kërkesa vijuese",
    value = "Vlera",
    probability = "Probabiliteti",
    density_title = "Probabiliteti është sipërfaqe nën dendësi",
    density_subtitle = "Intervali i hijezuar ka probabilitet pozitiv; një pikë e saktë ka probabilitet zero",
    standard_value = "Vlera e standardizuar",
    density = "Dendësia",
    binomial_title = "Forma binomiale varet nga probabiliteti i suksesit",
    binomial_subtitle = "Çdo panel përdor n = 12 prova të pavarura",
    successes = "Numri i sukseseve",
    normal_title = "Katër lloje pyetjesh për shpërndarjen normale",
    normal_subtitle = "Drejtimi dhe kufijtë përcaktojnë sipërfaqen ose pikën kufitare që kërkohet",
    below = "Nën një kufi",
    above = "Mbi një kufi",
    between = "Mes dy kufijve",
    inverse = "Kufiri për 99% poshtë",
    sampling_title = "Si e ndryshon madhësia e kampionit shpërndarjen e kampionimit",
    sampling_subtitle = "1 500 mesatare të simuluara për panel nga popullata burimore të standardizuara",
    normal_source = "Burim normal",
    uniform_source = "Burim uniform",
    skewed_source = "Burim me anim djathtas",
    sample_mean = "Mesatarja e kampionit",
    simulation_density = "Dendësia e simulimit",
    sample_size = "Madhësia e kampionit",
    sampling_process_title = "Nga popullata te shpërndarja e kampionimit",
    sampling_process_subtitle = "Kampionet e përsëritura të rastësishme japin mesatare të ndryshme",
    process_stage = "Hapi",
    process_population = "Popullata\ntë gjitha njësitë\ne mundshme",
    process_samples = "Shumë kampione\ntë rastësishme\nme madhësi n",
    process_means = "Një mesatare nga\nçdo kampion",
    process_distribution = "Shpërndarja\ne kampionimit\ne mesatares",
    process_draw = "përzgjidh",
    process_calculate = "llogarit",
    process_collect = "mbledh",
    bias_title = "Një kampion i madh mund të mos e japë mesataren e popullatës",
    bias_subtitle = "Në këtë simulim, personat me më shumë interes kanë më shumë gjasa të përgjigjen",
    target = "Popullata e synuar",
    random_sample = "Kampioni i rastësishëm",
    respondents = "Të anketuarit vullnetarë",
    mean_outcome = "Rezultati mesatar i interesit",
    low_stress = "Stres i ulët",
    high_stress = "Stres i lartë",
    high_anxiety = "Ankth i lartë",
    low_anxiety = "Ankth i ulët",
    high_anxiety_event = "Ankth i lartë (pikëzimi >= 23)",
    low_anxiety_event = "Ankth i ulët (pikëzimi < 23)",
    high_stress_event = "Grupi me stres të lartë",
    low_stress_event = "Grupi me stres të ulët",
    total = "Gjithsej",
    group = "Grupi",
    cond_high = "P(ankth i lartë | grupi)",
    cond_low = "P(ankth i ulët | grupi)",
    high_anxiety_probability = "Probabiliteti i ankthit të lartë",
    cond_title = "Probabiliteti i kushtëzuar i ankthit të lartë sipas grupit të stresit",
    stress_group = "Grupi i stresit",
    anxiety_level = "Niveli i ankthit",
    normal_fit_title = "Pikëzimet e ankthit nga provimi me shpërndarjen normale të përshtatur",
    normal_fit_mean = "Mesatarja",
    normal_fit_boundary = "Kufiri për 23 ose më lart te 22.5 (vijë portokalli e ndërprerë)",
    exam_score = "Pikëzimi i ankthit nga provimi (0–40)",
    continuous_model_value = "Vlera e vazhdueshme e modelit para rrumbullakimit",
    binomial_count = "Numri i studentëve me ankth të lartë",
    binomial_expected = "E(X)",
    sampling_mean_title = "Shpërndarja e kampionimit e mesatares",
    sample_means_mean = "Mesatarja e mesatareve të kampioneve",
    plugin_se = "vlerësimi zëvendësues i gabimit standard",
    sample_mean_anxiety = "Mesatarja e kampionit për ankthin nga provimi",
    participant_id = "ID-ja e pjesëmarrësit",
    exam_anxiety_score = "Pikëzimi i ankthit nga provimi"
  )
)[[topic_locale]]

# Static figures cannot rely on Plotly's automatic title wrapping. Preserve
# every localized word while inserting a line break only where a long heading
# would otherwise extend beyond the teaching canvas.
wrap_topic2_label <- function(text, width) {
  paste(strwrap(text, width = width), collapse = "\n")
}

topic2_theme <- function(base_size = 12) {
  theme_minimal(base_size = base_size) +
    theme(
      plot.title = element_text(face = "bold", color = "#172B3A"),
      plot.subtitle = element_text(color = "#536475"),
      axis.title = element_text(color = "#34495E"),
      axis.text = element_text(color = "#465A6B"),
      strip.text = element_text(face = "bold", color = "#203A4F"),
      panel.grid.minor = element_blank(),
      panel.grid.major = element_line(color = "#E7ECF1"),
      plot.background = element_rect(fill = "white", color = NA)
    )
}

# ggplotly derives tooltip field names from the underlying R columns. That is
# useful during development, but names such as x, y, xbar, and probability are
# not suitable learner-facing labels. Plots can register a localized field map
# without changing their data or geometry; this helper then rewrites only the
# generated tooltip text and gives each value a consistent readable precision.
localize_topic2_tooltips <- function(widget, field_specs) {
  if (is.null(field_specs) || !length(field_specs)) return(widget)

  localize_line <- function(line) {
    if (is.na(line) || !nzchar(line)) return("")

    parts <- strsplit(line, "<br\\s*/?>", perl = TRUE)[[1]]
    for (part_index in seq_along(parts)) {
      part <- trimws(parts[[part_index]])
      for (field in names(field_specs)) {
        prefix <- paste0(field, ":")
        if (!startsWith(part, prefix)) next

        spec <- field_specs[[field]]
        raw_value <- trimws(substring(part, nchar(prefix) + 1L))
        numeric_value <- suppressWarnings(as.numeric(raw_value))
        display_value <- if (is.na(numeric_value)) {
          raw_value
        } else {
          formatC(
            numeric_value,
            format = "f",
            digits = as.integer(spec$digits)
          )
        }
        parts[[part_index]] <- paste0(spec$label, ": ", display_value)
        break
      }
    }
    paste(parts, collapse = "<br>")
  }

  for (trace_index in seq_along(widget$x$data)) {
    trace_text <- widget$x$data[[trace_index]]$text
    trace_hovertext <- widget$x$data[[trace_index]]$hovertext
    if (!is.null(trace_hovertext) && length(trace_hovertext)) {
      widget$x$data[[trace_index]]$hovertext <- vapply(
        as.character(trace_hovertext),
        localize_line,
        character(1),
        USE.NAMES = FALSE
      )
    }
    if (is.null(trace_text) || !length(trace_text) || !any(nzchar(trace_text), na.rm = TRUE)) {
      widget$x$data[[trace_index]]$hoverinfo <- "skip"
      next
    }

    widget$x$data[[trace_index]]$text <- vapply(
      as.character(trace_text),
      localize_line,
      character(1),
      USE.NAMES = FALSE
    )
    widget$x$data[[trace_index]]$hovertemplate <- "%{text}<extra></extra>"
    widget$x$data[[trace_index]]$hoverinfo <- "text"
  }

  widget
}

accessible_plotly <- function(plot, alt_text, tooltip = c("x", "y")) {
  plotly_height <- attr(plot, "topic2_plotly_height", exact = TRUE)
  plotly_title_width <- attr(
    plot,
    "topic2_plotly_title_width",
    exact = TRUE
  )
  if (is.null(plotly_title_width)) plotly_title_width <- 22L

  plotly_margin <- attr(plot, "topic2_plotly_margin", exact = TRUE)
  if (is.null(plotly_margin)) plotly_margin <- list()
  plotly_margin <- utils::modifyList(
    list(l = 76, r = 28, b = 82, t = 96, pad = 2),
    plotly_margin
  )

  tooltip_field_specs <- if (inherits(plot, "plotly")) {
    NULL
  } else {
    attr(plot, "topic2_tooltip_fields", exact = TRUE)
  }
  # Direct Plotly diagrams also carry field names such as x, y, outcome,
  # label_x, and edge_label in their hover text. Give them the same localized
  # fallback map as ggplotly figures so those implementation names never leak
  # into German or Albanian tooltips.
  if (is.null(tooltip_field_specs)) {
    tooltip_field_specs <- list(
      x = list(label = topic2_labels$value, digits = 2L),
      y = list(label = topic2_labels$probability, digits = 3L),
      count = list(label = topic2_labels$bayes_count, digits = 0L),
      status = list(label = topic2_labels$bayes_status, digits = 0L),
      probability = list(label = topic2_labels$probability, digits = 3L),
      density = list(label = topic2_labels$density, digits = 4L),
      outcome = list(label = topic2_labels$value, digits = 0L),
      mean = list(label = topic2_labels$sample_mean, digits = 2L),
      label = list(label = topic2_labels$process_stage, digits = 0L),
      edge_label = list(label = topic2_labels$process_stage, digits = 0L),
      midpoint = list(label = topic2_labels$value, digits = 2L),
      label_x = list(label = topic2_labels$value, digits = 2L),
      label_y = list(label = topic2_labels$value, digits = 2L)
    )
  }
  hide_legend <- if (inherits(plot, "plotly")) {
    FALSE
  } else {
    isTRUE(attr(plot, "topic2_hide_legend", exact = TRUE))
  }
  disable_hover <- if (inherits(plot, "plotly")) {
    FALSE
  } else {
    isTRUE(attr(plot, "topic2_disable_hover", exact = TRUE))
  }
  widget <- if (inherits(plot, "plotly")) {
    plot
  } else {
    ggplotly(
      ratiomera_make_plotly_compatible(plot),
      tooltip = tooltip,
      dynamicTicks = TRUE
    )
  }

  widget <- ratiomera_prepare_plotly_widget(
    widget,
    # Topic 2 includes several ordinary-width widgets. A 22-character title
    # line remains readable while preventing translated headings from
    # escaping a phone-sized plot. Individual diagram attributes may opt into
    # a wider line when their named scroll region preserves a wider canvas.
    title_width = plotly_title_width,
    axis_width = 28,
    annotation_width = 32
  )
  widget <- localize_topic2_tooltips(widget, tooltip_field_specs)
  widget <- ratiomera_localize_plotly_hover(
    widget,
    ratiomera_plotly_hover_labels(plot, topic_locale)
  )

  if (hide_legend) {
    for (trace_index in seq_along(widget$x$data)) {
      widget$x$data[[trace_index]]$showlegend <- FALSE
    }
    widget$x$layout$showlegend <- FALSE
  }

  if (disable_hover) {
    for (trace_index in seq_along(widget$x$data)) {
      widget$x$data[[trace_index]]$hoverinfo <- "skip"
      widget$x$data[[trace_index]]$hovertemplate <- "<extra></extra>"
    }
  }

  widget <- widget |>
    layout(
      autosize = TRUE,
      hovermode = "closest",
      margin = plotly_margin
    ) |>
    config(
      responsive = TRUE,
      displayModeBar = FALSE,
      displaylogo = FALSE,
      scrollZoom = FALSE
    ) |>
    htmlwidgets::onRender(
      paste0(
        "function(el, x, altText) {",
        "el.setAttribute('role', 'img');",
        "el.setAttribute('aria-label', altText);",
        "el.style.width = '100%';",
        "requestAnimationFrame(function() { if (window.Plotly) Plotly.Plots.resize(el); });",
        "window.addEventListener('resize', function() { if (window.Plotly) Plotly.Plots.resize(el); });",
        "}"
      ),
      data = alt_text
    )

  # A few instructional diagrams use a vertical composition so that their
  # meaning survives in a phone-width reading column. Give only those widgets
  # the extra height they declare; every other figure continues to inherit its
  # ordinary Quarto chunk height.
  if (!is.null(plotly_height)) {
    widget$height <- as.numeric(plotly_height)
    widget$sizingPolicy$defaultHeight <- as.numeric(plotly_height)
  }

  widget
}

# Shared simulated cohort and every quantity derived from it.
set.seed(42)
n <- 160
dat <- tibble(
  id = 1:n,
  group_code = sample(
    c("low", "high"),
    size = n,
    replace = TRUE,
    prob = c(0.55, 0.45)
  )
) |>
  mutate(
    exam_anxiety = rnorm(
      n,
      mean = ifelse(group_code == "high", 24, 18),
      sd = 5
    ),
    exam_anxiety = pmin(pmax(round(exam_anxiety), 0), 40),
    high_anxiety = exam_anxiety >= 23,
    group = ifelse(
      group_code == "high",
      topic2_labels$high_stress,
      topic2_labels$low_stress
    )
  )

display_dat <- dat |>
  transmute(
    !!topic2_labels$participant_id := id,
    !!topic2_labels$group := group,
    !!topic2_labels$exam_anxiety_score := exam_anxiety,
    !!topic2_labels$anxiety_level := ifelse(
      high_anxiety,
      topic2_labels$high_anxiety,
      topic2_labels$low_anxiety
    )
  )

n_total <- nrow(dat)
n_high_anx <- sum(dat$high_anxiety)
n_low_anx <- n_total - n_high_anx
n_high_s <- sum(dat$group_code == "high")
n_low_s <- n_total - n_high_s
n_both <- sum(dat$high_anxiety & dat$group_code == "high")
n_low_s_ha <- sum(dat$high_anxiety & dat$group_code == "low")

p_ha <- n_high_anx / n_total
p_hs <- n_high_s / n_total
p_both <- n_both / n_total
p_ha_given_hs <- n_both / n_high_s
p_ha_given_ls <- n_low_s_ha / n_low_s
p_hs_given_ha <- n_both / n_high_anx
p_union <- p_ha + p_hs - p_both

mu_anx <- mean(dat$exam_anxiety)
sd_anx <- sd(dat$exam_anxiety)
normal_model_mean <- 24
normal_model_sd <- 5
normal_cutoff <- 22.5
p_theor <- pnorm(normal_cutoff, mean = normal_model_mean, sd = normal_model_sd, lower.tail = FALSE)
normal_q90 <- qnorm(0.90, mean = normal_model_mean, sd = normal_model_sd)

prob_tbl <- tibble(
  Event = c(
    topic2_labels$high_anxiety_event,
    topic2_labels$low_anxiety_event,
    topic2_labels$high_stress_event,
    topic2_labels$low_stress_event
  ),
  Count = c(n_high_anx, n_low_anx, n_high_s, n_low_s),
  Probability = round(c(p_ha, 1 - p_ha, p_hs, 1 - p_hs), 3)
)

cont_tbl <- tibble(
  !!topic2_labels$group := c(topic2_labels$high_stress, topic2_labels$low_stress),
  !!topic2_labels$high_anxiety := c(n_both, n_low_s_ha),
  !!topic2_labels$low_anxiety := c(n_high_s - n_both, n_low_s - n_low_s_ha),
  !!topic2_labels$total := c(n_high_s, n_low_s)
)

cond_tbl <- tibble(
  !!topic2_labels$group := c(topic2_labels$high_stress, topic2_labels$low_stress),
  !!topic2_labels$cond_high := round(c(p_ha_given_hs, p_ha_given_ls), 3),
  !!topic2_labels$cond_low := round(c(1 - p_ha_given_hs, 1 - p_ha_given_ls), 3)
)

cond_bar_dat <- tibble(
  group = factor(
    c(topic2_labels$high_stress, topic2_labels$low_stress),
    levels = c(topic2_labels$low_stress, topic2_labels$high_stress)
  ),
  probability = c(p_ha_given_hs, p_ha_given_ls)
)

stress_colors <- c("#2E6DA4", "#C05A47")
names(stress_colors) <- c(topic2_labels$low_stress, topic2_labels$high_stress)
p_cond_bar <- plot_ly(
  data = cond_bar_dat,
  x = ~probability,
  y = ~group,
  type = "bar",
  orientation = "h",
  text = ~paste0(round(probability * 100, 1), "%"),
  textposition = "outside",
  textangle = 0,
  textfont = list(color = "#203A4F", size = 14),
  hovertext = ~paste0(
    as.character(group),
    "<br>",
    topic2_labels$high_anxiety_probability,
    ": ",
    round(probability * 100, 1),
    "%"
  ),
  cliponaxis = FALSE,
  marker = list(
    color = unname(stress_colors[as.character(cond_bar_dat$group)]),
    line = list(color = "white", width = 1)
  ),
  hoverinfo = "text",
  showlegend = FALSE
) |>
  layout(
    bargap = 0.38,
    paper_bgcolor = "white",
    plot_bgcolor = "white",
    xaxis = list(
      title = list(text = topic2_labels$high_anxiety_probability),
      range = c(0, 1),
      tickmode = "array",
      tickvals = c(0, 0.5, 1),
      ticktext = c("0%", "50%", "100%"),
      gridcolor = "#E7ECF1",
      zeroline = FALSE,
      fixedrange = TRUE
    ),
    yaxis = list(
      title = list(text = ""),
      categoryorder = "array",
      categoryarray = c(topic2_labels$low_stress, topic2_labels$high_stress),
      fixedrange = TRUE
    )
  )

normal_model_data <- tibble(
  x = seq(
    normal_model_mean - 4 * normal_model_sd,
    normal_model_mean + 4 * normal_model_sd,
    length.out = 401
  ),
  y = dnorm(x, mean = normal_model_mean, sd = normal_model_sd)
)
p_norm <- ggplot(normal_model_data, aes(x, y)) +
  geom_area(
    data = normal_model_data |> filter(x >= normal_cutoff),
    fill = "#77A9CF",
    alpha = 0.8
  ) +
  geom_line(
    color = "#203A4F",
    linewidth = 1.1
  ) +
  geom_vline(xintercept = normal_cutoff, linetype = "dashed", color = "#C05A47", linewidth = 0.9) +
  labs(
    title = NULL,
    subtitle = NULL,
    x = topic2_labels$continuous_model_value,
    y = topic2_labels$density
  ) +
  topic2_theme(base_size = 13)
attr(p_norm, "topic2_tooltip_fields") <- list(
  x = list(label = topic2_labels$continuous_model_value, digits = 1L),
  y = list(label = topic2_labels$density, digits = 5L)
)

n_binom <- 10
binom_dat <- tibble(
  x = 0:n_binom,
  probability = dbinom(0:n_binom, size = n_binom, prob = p_ha)
) |>
  mutate(cumulative_probability = cumsum(probability))
binom_ev <- n_binom * p_ha
binom_var <- n_binom * p_ha * (1 - p_ha)
binom_sd <- sqrt(binom_var)
p_binom_4 <- dbinom(4, size = n_binom, prob = p_ha)
p_binom_over5 <- pbinom(5, size = n_binom, prob = p_ha, lower.tail = FALSE)

p_binom <- ggplot(binom_dat, aes(x, probability)) +
  geom_col(fill = "#2E6DA4", color = "white", width = 0.7) +
  scale_x_continuous(breaks = seq(0, n_binom, 2)) +
  labs(
    title = NULL,
    subtitle = NULL,
    x = topic2_labels$successes,
    y = paste0(topic2_labels$probability, " P(X = x)")
  ) +
  topic2_theme(base_size = 13) +
  theme(panel.grid.major.x = element_blank())
attr(p_binom, "topic2_tooltip_fields") <- list(
  x = list(label = topic2_labels$successes, digits = 0L),
  probability = list(label = topic2_labels$probability, digits = 4L)
)

sample_n <- 30
sampling_population_mean <- 20
sampling_population_sd <- 6
set.seed(2044)
sample_means <- replicate(
  1000,
  mean(rnorm(sample_n, mean = sampling_population_mean, sd = sampling_population_sd))
)
se_theoretical <- sampling_population_sd / sqrt(sample_n)
se_est <- se_theoretical
sampling_precision_tbl <- tibble(
  sample_size = c(10, 30, 90),
  standard_error = round(sampling_population_sd / sqrt(c(10, 30, 90)), 3)
)

sampling_fit_data <- tibble(
  x = seq(min(sample_means) - 0.5, max(sample_means) + 0.5, length.out = 401),
  y = dnorm(x, mean = sampling_population_mean, sd = se_theoretical)
)

p_sampling <- ggplot(tibble(xbar = sample_means), aes(xbar)) +
  geom_histogram(
    aes(y = after_stat(density)),
    binwidth = 0.4,
    boundary = 0,
    color = "white",
    fill = "#2E6DA4",
    alpha = 0.75
  ) +
  geom_line(
    data = sampling_fit_data,
    aes(x, y),
    inherit.aes = FALSE,
    color = "#C0392B",
    linewidth = 1.1
  ) +
  labs(
    title = NULL,
    subtitle = NULL,
    x = topic2_labels$sample_mean,
    y = topic2_labels$density
  ) +
  topic2_theme(base_size = 13)
attr(p_sampling, "topic2_tooltip_fields") <- list(
  xbar = list(label = topic2_labels$sample_mean, digits = 1L),
  density = list(label = topic2_labels$density, digits = 5L),
  x = list(label = topic2_labels$sample_mean, digits = 2L),
  y = list(label = topic2_labels$density, digits = 5L)
)

# Event sets.
event_theta <- seq(0, 2 * pi, length.out = 240)
event_set_lines <- bind_rows(
  tibble(event = "A", x = -0.65 + cos(event_theta), y = sin(event_theta)),
  tibble(event = "B", x = 0.65 + cos(event_theta), y = sin(event_theta))
)
p_event_sets <- ggplot(event_set_lines, aes(x, y, group = event, color = event)) +
  geom_path(linewidth = 1.3, show.legend = FALSE) +
  annotate("text", x = -1.05, y = 0.08, label = topic2_labels$event_a, color = "#2E6DA4", fontface = "bold") +
  annotate("text", x = 1.05, y = 0.08, label = topic2_labels$event_b, color = "#C05A47", fontface = "bold") +
  annotate("text", x = 0, y = -0.18, label = topic2_labels$intersection, color = "#34495E", size = 3.5) +
  scale_color_manual(values = c(A = "#2E6DA4", B = "#C05A47")) +
  coord_equal(xlim = c(-1.9, 1.9), ylim = c(-1.25, 1.25), clip = "off") +
  labs(title = topic2_labels$event_title, subtitle = topic2_labels$event_subtitle) +
  theme_void(base_size = 12) +
  theme(
    plot.title = element_text(face = "bold", color = "#172B3A"),
    plot.subtitle = element_text(color = "#536475"),
    plot.margin = margin(10, 15, 10, 15)
  )

# The same finite sample space shown through union, intersection, complement,
# and disjointness. Exact outcomes follow the course-material example.
event_operation_panels <- c(
  topic2_labels$operation_union,
  topic2_labels$operation_intersection,
  topic2_labels$operation_complement,
  topic2_labels$operation_disjoint
)
event_operation_data <- tidyr::crossing(
  panel = factor(event_operation_panels, levels = event_operation_panels),
  outcome = 1:10
) |>
  mutate(
    state = case_when(
      panel == topic2_labels$operation_union & outcome %in% c(1, 2, 3, 7) ~ "union",
      panel == topic2_labels$operation_intersection & outcome %in% c(2, 3) ~ "intersection",
      panel == topic2_labels$operation_complement & !outcome %in% c(1, 2, 3) ~ "complement",
      panel == topic2_labels$operation_disjoint & outcome %in% c(1, 2, 3) ~ "event_a",
      panel == topic2_labels$operation_disjoint & outcome %in% c(4, 5, 6, 7) ~ "event_b",
      TRUE ~ "outside"
    ),
    membership = case_when(
      panel == topic2_labels$operation_disjoint & outcome %in% c(1, 2, 3) ~ "A",
      panel == topic2_labels$operation_disjoint & outcome %in% c(4, 5, 6, 7) ~ "B",
      panel != topic2_labels$operation_disjoint & outcome == 1 ~ "A",
      panel != topic2_labels$operation_disjoint & outcome %in% c(2, 3) ~ "A, D",
      panel != topic2_labels$operation_disjoint & outcome == 7 ~ "D",
      TRUE ~ ""
    ),
    text_color = if_else(state == "outside", "dark", "light")
  )

event_operation_notes <- tibble(
  panel = factor(event_operation_panels, levels = event_operation_panels),
  outcome = 5.5,
  y = -0.78,
  label = c(
    topic2_labels$operation_union_result,
    topic2_labels$operation_intersection_result,
    topic2_labels$operation_complement_result,
    topic2_labels$operation_disjoint_result
  )
)

p_event_operations <- ggplot(event_operation_data, aes(outcome, 0, fill = state)) +
  geom_tile(width = 0.88, height = 0.82, color = "white", linewidth = 0.9) +
  geom_text(aes(label = outcome, color = text_color), fontface = "bold", size = 4) +
  geom_text(aes(y = -0.28, label = membership, color = text_color), size = 2.7) +
  geom_text(
    data = event_operation_notes,
    aes(outcome, y, label = label),
    inherit.aes = FALSE,
    color = "#34495E",
    fontface = "bold",
    size = 3.2
  ) +
  facet_wrap(vars(panel), ncol = 2) +
  scale_fill_manual(
    values = c(
      union = "#2E6DA4",
      intersection = "#6A4C93",
      complement = "#317873",
      event_a = "#2E6DA4",
      event_b = "#C05A47",
      outside = "#E8EDF2"
    ),
    guide = "none"
  ) +
  scale_color_manual(values = c(dark = "#203A4F", light = "white"), guide = "none") +
  scale_x_continuous(breaks = NULL, limits = c(0.4, 10.6), expand = c(0, 0)) +
  coord_cartesian(ylim = c(-1.0, 0.55), clip = "off") +
  labs(
    title = topic2_labels$operations_title,
    subtitle = topic2_labels$operations_subtitle,
    x = NULL,
    y = NULL
  ) +
  theme_void(base_size = 11) +
  theme(
    plot.title = element_text(face = "bold", color = "#172B3A"),
    plot.subtitle = element_text(color = "#536475"),
    strip.text = element_text(face = "bold", color = "#203A4F", margin = margin(5, 0, 8, 0)),
    panel.spacing = grid::unit(1.1, "lines"),
    plot.background = element_rect(fill = "white", color = NA),
    panel.background = element_rect(fill = "white", color = NA),
    plot.margin = margin(12, 18, 12, 18)
  )
attr(p_event_operations, "topic2_hide_legend") <- TRUE
attr(p_event_operations, "topic2_disable_hover") <- TRUE

# Conditional probability chain.
chain_nodes <- tibble(
  x = 0:3,
  y = 0,
  label = c(
    topic2_labels$chain_start,
    topic2_labels$chain_stage_1,
    topic2_labels$chain_stage_2,
    topic2_labels$chain_stage_3
  )
)
chain_edges <- tibble(
  x = c(0.18, 1.28, 2.28),
  xend = c(0.62, 1.68, 2.58),
  y = 0,
  yend = 0,
  probability = c("0.72", "0.80", "0.85")
) |>
  mutate(midpoint = (x + xend) / 2)
p_probability_chain <- ggplot() +
  geom_segment(
    data = chain_edges,
    aes(x, y, xend = xend, yend = yend),
    linewidth = 1.1,
    color = "#93A7B7",
    arrow = grid::arrow(length = grid::unit(0.18, "cm"))
  ) +
  geom_label(
    data = chain_nodes,
    aes(x, y, label = label),
    fill = "#F5F8FA",
    color = "#203A4F",
    linewidth = 0.3,
    size = 3.1
  ) +
  geom_text(data = chain_edges, aes(x = midpoint, y = 0.18, label = probability), color = "#2E6DA4", fontface = "bold") +
  coord_cartesian(xlim = c(-0.25, 3.25), ylim = c(-0.35, 0.45), clip = "off") +
  labs(title = topic2_labels$chain_title, subtitle = topic2_labels$chain_subtitle) +
  theme_void(base_size = 12) +
  theme(
    plot.title = element_text(face = "bold", color = "#172B3A"),
    plot.subtitle = element_text(color = "#536475"),
    plot.margin = margin(15, 20, 15, 20)
  )

# Natural frequencies in the Bayes example.
bayes_plot_data <- tibble(
  status = factor(
    c(topic2_labels$bayes_present, topic2_labels$bayes_absent),
    levels = c(topic2_labels$bayes_present, topic2_labels$bayes_absent)
  ),
  count = c(270, 1455)
)
p_bayes_base_rates <- ggplot(bayes_plot_data, aes(status, count, fill = status)) +
  geom_col(width = 0.62, show.legend = FALSE) +
  geom_text(aes(label = format(count, big.mark = " ")), vjust = -0.45, fontface = "bold", color = "#203A4F") +
  scale_fill_manual(values = c("#2E6DA4", "#D38B5D")) +
  scale_y_continuous(expand = expansion(mult = c(0, 0.12))) +
  labs(
    title = wrap_topic2_label(topic2_labels$bayes_title, 68),
    subtitle = wrap_topic2_label(topic2_labels$bayes_subtitle, 82),
    x = NULL,
    y = topic2_labels$bayes_count
  ) +
  topic2_theme() +
  theme(axis.text.x = element_text(angle = 8, hjust = 0.5), panel.grid.major.x = element_blank())

# Beginner bridge for Bayes' theorem. The geometry follows the same natural
# frequencies used in the lesson table.
bayes_tree_text <- if (topic_locale == "de") {
  list(
    node_labels = c(
      "Hypothetische Grundgesamtheit\n10 000 Personen",
      "Störung vorhanden\n300 Personen",
      "Störung nicht vorhanden\n9 700 Personen",
      "Positiv\n270 richtig positive",
      "Negativ\n30 falsch negative",
      "Positiv\n1 455 falsch positive",
      "Negativ\n8 245 richtig negative",
      "Alle positiven Ergebnisse\n270 + 1 455 = 1 725"
    ),
    edge_labels = c(
      "3%  →  300", "97%  →  9 700",
      "Sensitivität: 90%  →  270", "10%  →  30",
      "Falsch-positiv-Rate: 15%  →  1 455", "Spezifität: 85%  →  8 245",
      "", ""
    ),
    result = "Unter den positiven Ergebnissen:\n270 ÷ 1 725 = 15.7%",
    title = "Der Satz von Bayes verfolgt jeden Pfad zu einem positiven Ergebnis",
    subtitle = "Die Grundgesamtheit wird zuerst nach Zustand und danach nach Testergebnis aufgeteilt"
  )
} else if (topic_locale == "sq") {
  list(
    node_labels = c(
      "Popullatë hipotetike\n10 000 persona",
      "Çrregullimi i pranishëm\n300 persona",
      "Çrregullimi mungon\n9 700 persona",
      "Pozitiv\n270 pozitivë të vërtetë",
      "Negativ\n30 negativë të rremë",
      "Pozitiv\n1 455 pozitivë të rremë",
      "Negativ\n8 245 negativë të vërtetë",
      "Të gjitha rezultatet pozitive\n270 + 1 455 = 1 725"
    ),
    edge_labels = c(
      "3%  →  300", "97%  →  9 700",
      "Ndjeshmëria: 90%  →  270", "10%  →  30",
      "Pozitivë të rremë: 15%  →  1 455", "Specifiteti: 85%  →  8 245",
      "", ""
    ),
    result = "Mes rezultateve pozitive:\n270 ÷ 1 725 = 15.7%",
    title = "Teorema e Bayes-it ndjek çdo rrugë drejt një rezultati pozitiv",
    subtitle = "Popullata fillestare ndahet së pari sipas gjendjes dhe më pas sipas rezultatit të testit"
  )
} else {
  list(
    node_labels = c(
      "Hypothetical population\n10 000 people",
      "Condition present\n300 people",
      "Condition absent\n9 700 people",
      "Positive\n270 true positives",
      "Negative\n30 false negatives",
      "Positive\n1 455 false positives",
      "Negative\n8 245 true negatives",
      "All positive results\n270 + 1 455 = 1 725"
    ),
    edge_labels = c(
      "3%  →  300", "97%  →  9 700",
      "Sensitivity: 90%  →  270", "10%  →  30",
      "False-positive rate: 15%  →  1 455", "Specificity: 85%  →  8 245",
      "", ""
    ),
    result = "Among positive results:\n270 ÷ 1 725 = 15.7%",
    title = "Bayes' Theorem Follows Every Path to a Positive Result",
    subtitle = "The starting population splits by condition status and then by test result"
  )
}

bayes_tree_nodes <- tibble(
  node = c(
    "population", "present", "absent", "present_positive",
    "present_negative", "absent_positive", "absent_negative", "positive_total"
  ),
  x = c(0, 1.15, 1.15, 2.35, 2.35, 2.35, 2.35, 3.72),
  y = c(1.55, 2.35, 0.75, 2.72, 1.98, 1.12, 0.38, 1.92),
  label = bayes_tree_text$node_labels,
  node_type = c("start", "status", "status", "positive", "negative", "positive", "negative", "denominator")
)

bayes_tree_edges <- tribble(
  ~from, ~to, ~edge_label,
  "population", "present", bayes_tree_text$edge_labels[[1]],
  "population", "absent", bayes_tree_text$edge_labels[[2]],
  "present", "present_positive", bayes_tree_text$edge_labels[[3]],
  "present", "present_negative", bayes_tree_text$edge_labels[[4]],
  "absent", "absent_positive", bayes_tree_text$edge_labels[[5]],
  "absent", "absent_negative", bayes_tree_text$edge_labels[[6]],
  "present_positive", "positive_total", bayes_tree_text$edge_labels[[7]],
  "absent_positive", "positive_total", bayes_tree_text$edge_labels[[8]]
) |>
  left_join(
    bayes_tree_nodes |> select(from = node, x, y),
    by = "from"
  ) |>
  left_join(
    bayes_tree_nodes |> select(to = node, xend = x, yend = y),
    by = "to"
  ) |>
  mutate(
    label_x = x + 0.52 * (xend - x),
    label_y = y + 0.52 * (yend - y)
  )

p_bayes_tree <- ggplot() +
  geom_segment(
    data = bayes_tree_edges,
    aes(x, y, xend = xend, yend = yend),
    color = "#91A4B3",
    linewidth = 0.8,
    arrow = grid::arrow(length = grid::unit(0.13, "cm"), type = "closed")
  ) +
  geom_label(
    data = bayes_tree_nodes,
    aes(x, y, label = label, fill = node_type),
    color = "#203A4F",
    size = 3.1,
    lineheight = 0.95,
    linewidth = 0.3,
    label.padding = grid::unit(0.2, "lines")
  ) +
  geom_label(
    data = bayes_tree_edges |> filter(edge_label != ""),
    aes(label_x, label_y, label = edge_label),
    fill = "white",
    color = "#536475",
    size = 2.75,
    linewidth = 0,
    label.padding = grid::unit(0.08, "lines")
  ) +
  annotate(
    "label",
    x = 3.72,
    y = 1.30,
    label = bayes_tree_text$result,
    fill = "#FFF4EA",
    color = "#713D31",
    fontface = "bold",
    size = 3.1,
    linewidth = 0.35
  ) +
  scale_fill_manual(
    values = c(
      start = "#EAF2F8",
      status = "#F3F6F8",
      positive = "#FFF0E6",
      negative = "#F3F6F8",
      denominator = "#FFE0CC"
    ),
    guide = "none"
  ) +
  coord_cartesian(xlim = c(-0.42, 4.28), ylim = c(0.02, 3.05), clip = "off") +
  labs(
    title = bayes_tree_text$title,
    subtitle = bayes_tree_text$subtitle
  ) +
  theme_void(base_size = 11) +
  theme(
    plot.title = element_text(face = "bold", color = "#172B3A"),
    plot.subtitle = element_text(color = "#536475"),
    plot.background = element_rect(fill = "white", color = NA),
    panel.background = element_rect(fill = "white", color = NA),
    plot.margin = margin(16, 24, 16, 24)
  )

# PMF and CDF for the worked discrete distribution.
pmf_values <- tibble(x = c(0, 1, 2, 4), probability = c(0.10, 0.35, 0.40, 0.15)) |>
  mutate(cumulative = cumsum(probability))
pmf_panel <- pmf_values |>
  transmute(x, y = probability, panel = topic2_labels$pmf) |>
  mutate(panel = factor(panel, levels = c(topic2_labels$pmf, topic2_labels$cdf)))
cdf_step_values <- tibble(
  x = c(-1, 0, 1, 2, 4, 5),
  y = c(0, 0.10, 0.45, 0.85, 1.00, 1.00),
  panel = factor(topic2_labels$cdf, levels = c(topic2_labels$pmf, topic2_labels$cdf))
)
cdf_points <- pmf_values |>
  transmute(
    x,
    y = cumulative,
    panel = factor(topic2_labels$cdf, levels = c(topic2_labels$pmf, topic2_labels$cdf))
  )
p_pmf_cdf <- ggplot(pmf_panel, aes(x, y)) +
  geom_col(width = 0.55, fill = "#2E6DA4") +
  geom_step(data = cdf_step_values, direction = "hv", linewidth = 1.1, color = "#C05A47") +
  geom_point(data = cdf_points, size = 2.4, color = "#C05A47") +
  facet_wrap(vars(panel), nrow = 1, scales = "free_x") +
  scale_x_continuous(breaks = c(-1, 0, 1, 2, 4, 5)) +
  scale_y_continuous(limits = c(0, 1), breaks = seq(0, 1, 0.2)) +
  labs(
    title = topic2_labels$pmf_cdf_title,
    subtitle = wrap_topic2_label(topic2_labels$pmf_cdf_subtitle, 86),
    x = topic2_labels$requests,
    y = topic2_labels$probability
  ) +
  topic2_theme()

# Continuous density and a shaded interval.
density_data <- tibble(x = seq(-4, 4, length.out = 700)) |>
  mutate(y = dnorm(x), inside = x >= -0.75 & x <= 1.25)
p_density_interval <- ggplot(density_data, aes(x, y)) +
  geom_area(data = density_data |> filter(inside), fill = "#77A9CF", alpha = 0.75) +
  geom_line(linewidth = 1.05, color = "#203A4F") +
  geom_vline(xintercept = c(-0.75, 1.25), linetype = "dashed", color = "#C05A47") +
  labs(
    title = topic2_labels$density_title,
    subtitle = wrap_topic2_label(topic2_labels$density_subtitle, 82),
    x = topic2_labels$value,
    y = topic2_labels$density
  ) +
  topic2_theme()

# Binomial shapes at fixed n and three values of pi.
binomial_shape_data <- tidyr::crossing(x = 0:12, pi = c(0.20, 0.50, 0.80)) |>
  mutate(
    probability = dbinom(x, size = 12, prob = pi),
    panel = paste0("\u03c0 = ", format(pi, nsmall = 2))
  )
p_binomial_shape <- ggplot(binomial_shape_data, aes(x, probability)) +
  geom_col(width = 0.72, fill = "#2E6DA4") +
  facet_wrap(vars(panel), nrow = 1) +
  scale_x_continuous(breaks = seq(0, 12, 2)) +
  labs(
    title = topic2_labels$binomial_title,
    subtitle = topic2_labels$binomial_subtitle,
    x = topic2_labels$successes,
    y = topic2_labels$probability
  ) +
  topic2_theme()

# Four forward/inverse normal questions.
normal_x <- seq(-3.5, 3.5, length.out = 700)
normal_panels <- c(topic2_labels$below, topic2_labels$inverse, topic2_labels$above, topic2_labels$between)
normal_question_data <- tidyr::crossing(panel = factor(normal_panels, levels = normal_panels), x = normal_x) |>
  mutate(
    y = dnorm(x),
    shade = case_when(
      panel == topic2_labels$below ~ x <= 0.67,
      panel == topic2_labels$above ~ x >= 0.67,
      panel == topic2_labels$between ~ x >= 0 & x <= 0.67,
      panel == topic2_labels$inverse ~ x <= 2.33,
      TRUE ~ FALSE
    )
  )
normal_question_boundaries <- bind_rows(
  tibble(panel = topic2_labels$below, boundary = 0.67),
  tibble(panel = topic2_labels$inverse, boundary = 2.33),
  tibble(panel = topic2_labels$above, boundary = 0.67),
  tibble(panel = topic2_labels$between, boundary = c(0, 0.67))
) |>
  mutate(panel = factor(panel, levels = normal_panels))
p_normal_questions <- ggplot(normal_question_data, aes(x, y)) +
  geom_area(data = normal_question_data |> filter(shade), fill = "#77A9CF", alpha = 0.8) +
  geom_line(linewidth = 0.8, color = "#203A4F") +
  geom_vline(
    data = normal_question_boundaries,
    aes(xintercept = boundary),
    color = "#C05A47",
    linetype = "dashed",
    linewidth = 0.7
  ) +
  facet_wrap(vars(panel), nrow = 2) +
  labs(
    title = topic2_labels$normal_title,
    subtitle = topic2_labels$normal_subtitle,
    x = topic2_labels$standard_value,
    y = topic2_labels$density
  ) +
  topic2_theme()

# Sampling distributions from three standardized source shapes.
set.seed(2042)
sampling_source <- function(kind, n) {
  switch(
    kind,
    normal = rnorm(n),
    uniform = (runif(n) - 0.5) * sqrt(12),
    skewed = rexp(n) - 1
  )
}
sampling_grid_data <- bind_rows(lapply(c("normal", "uniform", "skewed"), function(kind) {
  bind_rows(lapply(c(1, 5, 30), function(sample_n) {
    tibble(
      mean = replicate(1500, mean(sampling_source(kind, sample_n))),
      source = kind,
      n = sample_n
    )
  }))
})) |>
  mutate(
    source = recode(
      source,
      normal = topic2_labels$normal_source,
      uniform = topic2_labels$uniform_source,
      skewed = topic2_labels$skewed_source
    ),
    source = factor(
      source,
      levels = c(topic2_labels$normal_source, topic2_labels$uniform_source, topic2_labels$skewed_source)
    ),
    n = factor(paste0("n = ", n), levels = c("n = 1", "n = 5", "n = 30"))
  )
p_sampling_grid <- ggplot(sampling_grid_data, aes(mean)) +
  geom_histogram(
    data = sampling_grid_data |> filter(n == "n = 1"),
    aes(y = after_stat(density)),
    binwidth = 0.25,
    boundary = 0,
    fill = "#2E6DA4",
    color = "white"
  ) +
  geom_histogram(
    data = sampling_grid_data |> filter(n == "n = 5"),
    aes(y = after_stat(density)),
    binwidth = 0.12,
    boundary = 0,
    fill = "#2E6DA4",
    color = "white"
  ) +
  geom_histogram(
    data = sampling_grid_data |> filter(n == "n = 30"),
    aes(y = after_stat(density)),
    binwidth = 0.06,
    boundary = 0,
    fill = "#2E6DA4",
    color = "white"
  ) +
  facet_wrap(vars(source, n), ncol = 3) +
  coord_cartesian(xlim = c(-3.5, 3.5)) +
  labs(
    title = topic2_labels$sampling_title,
    subtitle = topic2_labels$sampling_subtitle,
    x = topic2_labels$sample_mean,
    y = topic2_labels$simulation_density
  ) +
  topic2_theme(base_size = 10)

# Conceptual path from repeated sampling to a sampling distribution. The
# stages run from top to bottom rather than left to right so all four remain
# readable at phone width without horizontal scrolling.
sampling_process_nodes <- tibble(
  x = 0,
  y = c(7.5, 5.0, 2.5, 0),
  label = c(
    topic2_labels$process_population,
    topic2_labels$process_samples,
    topic2_labels$process_means,
    topic2_labels$process_distribution
  ),
  node_fill = c("emphasis", "standard", "standard", "emphasis")
)
sampling_process_edges <- tibble(
  x = 0,
  xend = 0,
  y = c(6.76, 4.26, 1.76),
  yend = c(5.74, 3.24, 0.74),
  label = c(
    topic2_labels$process_draw,
    topic2_labels$process_calculate,
    topic2_labels$process_collect
  )
  ) |>
  mutate(midpoint = (y + yend) / 2)

p_sampling_process <- ggplot() +
  geom_segment(
    data = sampling_process_edges,
    aes(x, y, xend = xend, yend = yend),
    linewidth = 1.1,
    color = "#93A7B7",
    arrow = grid::arrow(length = grid::unit(0.18, "cm"))
  ) +
  geom_tile(
    data = sampling_process_nodes,
    aes(x, y, fill = node_fill),
    width = 1.72,
    height = 1.40,
    color = "#AFC0CC",
    linewidth = 0.35,
    show.legend = FALSE
  ) +
  geom_text(
    data = sampling_process_nodes,
    aes(x, y, label = label),
    color = "#203A4F",
    lineheight = 0.94,
    size = 2.9
  ) +
  geom_text(
    data = sampling_process_edges,
    aes(x = 0.15, y = midpoint, label = label),
    color = "#2E6DA4",
    fontface = "bold",
    hjust = 0,
    size = 3.0
  ) +
  coord_cartesian(
    xlim = c(-1.02, 1.02),
    ylim = c(-0.82, 8.32),
    expand = FALSE,
    clip = "off"
  ) +
  scale_fill_manual(values = c(emphasis = "#EAF2F8", standard = "#F5F8FA"), guide = "none") +
  labs(
    title = topic2_labels$sampling_process_title,
    subtitle = topic2_labels$sampling_process_subtitle
  ) +
  theme_void(base_size = 12) +
  theme(
    plot.title = element_text(face = "bold", color = "#172B3A"),
    plot.subtitle = element_text(color = "#536475"),
    plot.background = element_rect(fill = "white", color = NA),
    panel.background = element_rect(fill = "white", color = NA),
    plot.margin = margin(15, 24, 15, 24)
  )

attr(p_sampling_process, "topic2_tooltip_fields") <- list(
  label = list(label = topic2_labels$process_stage, digits = 0L)
)
attr(p_sampling_process, "topic2_hide_legend") <- TRUE
attr(p_sampling_process, "topic2_plotly_title_width") <- 40L
attr(p_sampling_process, "topic2_plotly_margin") <- list(
  l = 24,
  r = 24,
  b = 24,
  t = 120
)
attr(p_sampling_process, "topic2_plotly_height") <- 660

# A simulated voluntary-response mechanism.
set.seed(2043)
bias_population <- tibble(interest = pmin(pmax(rnorm(10000, 50, 10), 0), 100)) |>
  mutate(response_probability = plogis(-4.8 + 0.09 * interest), responded = rbinom(n(), 1, response_probability) == 1)
bias_response_n <- sum(bias_population$responded)
set.seed(2045)
bias_random_sample <- sample(seq_len(nrow(bias_population)), size = bias_response_n, replace = FALSE)
bias_plot_data <- tibble(
  group = factor(
    c(topic2_labels$target, topic2_labels$random_sample, topic2_labels$respondents),
    levels = c(topic2_labels$target, topic2_labels$random_sample, topic2_labels$respondents)
  ),
  mean = c(
    mean(bias_population$interest),
    mean(bias_population$interest[bias_random_sample]),
    mean(bias_population$interest[bias_population$responded])
  )
)
# Build this compact comparison directly in Plotly. ggplotly misidentifies the
# orientation of a three-row horizontal bar chart in some package versions,
# which can leave only value labels visible. A single explicit horizontal trace
# preserves the exact three means and stays readable at phone width.
bias_plot_data <- bias_plot_data |>
  mutate(
    hover_text = paste0(
      as.character(group),
      "<br>",
      topic2_labels$mean_outcome,
      ": ",
      sprintf("%.1f", mean)
    ),
    value_label = sprintf("%.1f", mean)
  )

# The Theory tab intentionally uses a static figure. Keep a dedicated ggplot
# version of the same three means so the interactive Plotly object below is
# reserved for the Simulated Example tab.
p_sampling_bias_theory <- ggplot(
  bias_plot_data,
  aes(x = mean, y = group, fill = group)
) +
  geom_col(width = 0.58, show.legend = FALSE) +
  geom_text(
    aes(label = value_label),
    hjust = -0.18,
    color = "#203A4F",
    size = 3.7
  ) +
  scale_fill_manual(values = c("#2E6DA4", "#3F8B6D", "#D38B5D"), guide = "none") +
  scale_x_continuous(
    limits = c(0, 62),
    breaks = c(0, 20, 40, 60),
    expand = expansion(mult = c(0, 0.01))
  ) +
  labs(
    title = topic2_labels$bias_title,
    subtitle = topic2_labels$bias_subtitle,
    x = topic2_labels$mean_outcome,
    y = NULL
  ) +
  topic2_theme(base_size = 11) +
  theme(
    legend.position = "none",
    plot.margin = margin(14, 24, 14, 18)
  )

p_sampling_bias <- plot_ly(
  data = bias_plot_data,
  x = ~mean,
  y = ~group,
  type = "bar",
  orientation = "h",
  text = ~value_label,
  textposition = "outside",
  hovertext = ~hover_text,
  hoverinfo = "text",
  cliponaxis = FALSE,
  marker = list(color = c("#2E6DA4", "#3F8B6D", "#D38B5D")),
  showlegend = FALSE
) |>
  layout(
    title = list(
      text = paste0(
        "<b>",
        topic2_labels$bias_title,
        "</b><br><sup>",
        topic2_labels$bias_subtitle,
        "</sup>"
      ),
      x = 0.03,
      xanchor = "left"
    ),
    xaxis = list(
      title = list(text = topic2_labels$mean_outcome),
      range = c(0, 62),
      zeroline = FALSE,
      gridcolor = "#E7ECF1"
    ),
    yaxis = list(
      title = list(text = ""),
      categoryorder = "array",
      categoryarray = rev(levels(bias_plot_data$group))
    ),
    paper_bgcolor = "white",
    plot_bgcolor = "white",
    showlegend = FALSE
  )

attr(p_sampling_bias, "topic2_plotly_title_width") <- 38L
attr(p_sampling_bias, "topic2_plotly_margin") <- list(l = 104, r = 34, t = 238)
attr(p_sampling_bias, "topic2_plotly_height") <- 620
