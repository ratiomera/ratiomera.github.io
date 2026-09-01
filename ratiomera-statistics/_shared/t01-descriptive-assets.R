# Shared data and figure specification for Descriptive Statistics, Topic 1.
# Each language page sets `topic_locale` before sourcing this file. Simulation,
# formulas, bins, scales, and geometry stay identical; only visible labels vary.

if (!exists("topic_locale", inherits = FALSE)) topic_locale <- "en"
if (!topic_locale %in% c("en", "de", "sq")) {
  stop("Unsupported Topic 1 locale: ", topic_locale, call. = FALSE)
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

required_packages <- c("dplyr", "tibble", "ggplot2", "DT", "plotly", "htmlwidgets", "knitr")
missing_packages <- required_packages[
  !vapply(required_packages, requireNamespace, logical(1), quietly = TRUE)
]
if (length(missing_packages)) {
  stop(
    "Topic 1 requires these R packages: ",
    paste(missing_packages, collapse = ", "),
    call. = FALSE
  )
}

suppressPackageStartupMessages({
  library(dplyr)
  library(tibble)
  library(ggplot2)
  library(DT)
  library(plotly)
  library(knitr)
})

topic_labels <- list(
  en = list(
    low_stress = "Low stress",
    high_stress = "High stress",
    woman = "Woman",
    man = "Man",
    diverse = "Diverse",
    exam_title = "Exam Anxiety Scores",
    exam_subtitle = "Distribution of total scores on a 0–40 scale",
    exam_x = "Exam anxiety score (0–40)",
    students_y = "Number of students",
    box_title = "Anxiety by Stress",
    box_subtitle = "Higher center, with similar overall variability across groups",
    z_title = "Anxiety z-Scores",
    z_subtitle = "Mean = 0 and SD = 1. The dashed line marks the mean",
    z_x = "z-score",
    gender_title = "Distribution of Gender (Nominal Variable)",
    gender_subtitle = "Each bar represents one category, and nominal categories can appear in any order",
    gender_x = "Gender",
    stress_title = "Stress Group Distribution (Nominal Variable)",
    stress_subtitle = "Slice angle encodes the proportion in each category",
    stress_bar_subtitle = "Bar length encodes the count in each category",
    satisfaction_title = "Study Satisfaction Ratings (Ordinal Variable)",
    satisfaction_subtitle = "Categories remain in their natural 1–5 order",
    satisfaction_x = "Satisfaction rating (1 = very dissatisfied, 5 = very satisfied)",
    scale_learners_y = "Number of learners",
    scale_worked = "Worked examples",
    scale_visual = "Visual explanations",
    scale_guided = "Guided practice",
    scale_nominal_title = "Preferred Learning Format",
    scale_nominal_subtitle = "The categories describe choices and have no natural order",
    scale_nominal_x = "Preferred format",
    scale_ordinal_title = "Confidence Before the Workshop",
    scale_ordinal_subtitle = "Ratings stay in their meaningful order from 1 to 5",
    scale_ordinal_x = "Confidence rating (1 = very unsure, 5 = very sure)",
    scale_interval_title = "Room Temperature During the Workshop",
    scale_interval_subtitle = "Equal one-degree differences are meaningful on the Celsius scale",
    scale_temperature_x = "Room temperature (°C)",
    scale_ratio_title = "Optional Study Time Before the Workshop",
    scale_ratio_subtitle = "Zero minutes means that no study time was recorded",
    scale_minutes_x = "Study time (minutes)",
    scale_absolute_title = "Practice Questions Completed",
    scale_absolute_subtitle = "Each value is a count with a fixed unit of one question",
    scale_questions_x = "Questions completed",
    axis_full_title = "Same Scores, Full 0–100 Axis",
    axis_truncated_title = "Same Scores, Truncated 64–76 Axis",
    axis_subtitle = "Identical values can create very different visual impressions",
    program_x = "Workshop format",
    wellbeing_y = "Mean well-being score (0–100)",
    guided_program = "Guided reflection",
    peer_program = "Peer discussion",
    bins_narrow_title = "Exam Anxiety with 2-Point Bins",
    bins_wide_title = "Exam Anxiety with 8-Point Bins",
    bins_subtitle = "The observations stay the same while the grouping changes",
    value_x = "Value",
    frequency_y = "Frequency",
    shape_symmetric = "Symmetric Distribution",
    shape_right = "Right-Skewed Distribution",
    shape_left = "Left-Skewed Distribution",
    shape_unimodal = "Unimodal Distribution",
    shape_bimodal = "Bimodal Distribution",
    shape_high_kurtosis = "High-Kurtosis Distribution",
    shape_low_kurtosis = "Low-Kurtosis Distribution",
    hover_count = "Students:",
    hover_exam = "Anxiety score:",
    hover_group = "Stress group:",
    hover_satisfaction = "Satisfaction rating:",
    hover_z = "z-score:",
    hover_mean = "Sample mean:",
    widget_alt_exam = "Interactive histogram of exam anxiety scores with most observations concentrated around moderate values.",
    widget_alt_box = "Interactive side-by-side boxplots showing a higher center and similar overall spread for the high-stress group.",
    widget_alt_z = "Interactive histogram of standardized exam anxiety scores with the sample mean marked at zero."
  ),
  de = list(
    low_stress = "Niedrige Belastung",
    high_stress = "Hohe Belastung",
    woman = "Frau",
    man = "Mann",
    diverse = "Divers",
    exam_title = "Prüfungsangst bei Studierenden im ersten Studienjahr",
    exam_subtitle = "Verteilung der Gesamtwerte auf einer Skala von 0–40",
    exam_x = "Prüfungsangstwert (0–40)",
    students_y = "Anzahl der Studierenden",
    box_title = "Prüfungsangst nach selbst berichteter Belastungsgruppe",
    box_subtitle = "Höhere Lage bei ähnlicher Gesamtstreuung",
    z_title = "Standardisierte Prüfungsangstwerte",
    z_subtitle = "Mittelwert = 0 und SD = 1. Die gestrichelte Linie markiert den Mittelwert",
    z_x = "z-Wert",
    gender_title = "Geschlechtsverteilung (Nominalvariable)",
    gender_subtitle = "Jeder Balken steht für eine Kategorie, deren Reihenfolge bei Nominaldaten frei gewählt werden kann",
    gender_x = "Geschlecht",
    stress_title = "Verteilung der Belastungsgruppen (Nominalvariable)",
    stress_subtitle = "Der Winkel eines Segments bildet den Anteil der Kategorie ab",
    stress_bar_subtitle = "Die Balkenlänge bildet die Anzahl in jeder Kategorie ab",
    satisfaction_title = "Studienzufriedenheit (Ordinalvariable)",
    satisfaction_subtitle = "Die Kategorien bleiben in ihrer natürlichen Reihenfolge von 1 bis 5",
    satisfaction_x = "Zufriedenheit (1 = sehr unzufrieden, 5 = sehr zufrieden)",
    scale_learners_y = "Anzahl der Lernenden",
    scale_worked = "Durchgerechnete Beispiele",
    scale_visual = "Visuelle Erklärungen",
    scale_guided = "Angeleitete Übung",
    scale_nominal_title = "Bevorzugtes Lernformat",
    scale_nominal_subtitle = "Die Kategorien bezeichnen Wahlmöglichkeiten ohne natürliche Reihenfolge",
    scale_nominal_x = "Bevorzugtes Format",
    scale_ordinal_title = "Sicherheit vor dem Workshop",
    scale_ordinal_subtitle = "Die Bewertungen bleiben in ihrer sinnvollen Reihenfolge von 1 bis 5",
    scale_ordinal_x = "Sicherheit (1 = sehr unsicher, 5 = sehr sicher)",
    scale_interval_title = "Raumtemperatur während des Workshops",
    scale_interval_subtitle = "Gleich grosse Unterschiede von einem Grad sind auf der Celsius-Skala bedeutsam",
    scale_temperature_x = "Raumtemperatur (°C)",
    scale_ratio_title = "Freiwillige Lernzeit vor dem Workshop",
    scale_ratio_subtitle = "Null Minuten bedeutet, dass keine Lernzeit erfasst wurde",
    scale_minutes_x = "Lernzeit (Minuten)",
    scale_absolute_title = "Bearbeitete Übungsfragen",
    scale_absolute_subtitle = "Jeder Wert ist eine Anzahl mit der festen Einheit einer Frage",
    scale_questions_x = "Bearbeitete Fragen",
    axis_full_title = "Dieselben Werte, vollständige Achse von 0 bis 100",
    axis_truncated_title = "Dieselben Werte, verkürzte Achse von 64 bis 76",
    axis_subtitle = "Identische Werte können sehr unterschiedliche Eindrücke erzeugen",
    program_x = "Workshopformat",
    wellbeing_y = "Mittlerer Wohlbefindenswert (0–100)",
    guided_program = "Angeleitete Reflexion",
    peer_program = "Austausch unter Peers",
    bins_narrow_title = "Prüfungsangst mit 2-Punkte-Klassen",
    bins_wide_title = "Prüfungsangst mit 8-Punkte-Klassen",
    bins_subtitle = "Die Beobachtungen bleiben gleich, während sich die Gruppierung ändert",
    value_x = "Wert",
    frequency_y = "Häufigkeit",
    shape_symmetric = "Symmetrische Verteilung",
    shape_right = "Rechtsschiefe Verteilung",
    shape_left = "Linksschiefe Verteilung",
    shape_unimodal = "Unimodale Verteilung",
    shape_bimodal = "Bimodale Verteilung",
    shape_high_kurtosis = "Verteilung mit hoher Kurtosis",
    shape_low_kurtosis = "Verteilung mit niedriger Kurtosis",
    hover_count = "Studierende:",
    hover_exam = "Prüfungsangstwert:",
    hover_group = "Belastungsgruppe:",
    hover_satisfaction = "Zufriedenheitswert:",
    hover_z = "z-Wert:",
    hover_mean = "Stichprobenmittelwert:",
    widget_alt_exam = "Interaktives Histogramm der Prüfungsangstwerte mit einer Häufung im mittleren Bereich.",
    widget_alt_box = "Interaktive Boxplots der Prüfungsangst mit höherer Lage und ähnlicher Gesamtstreuung in der hoch belasteten Gruppe.",
    widget_alt_z = "Interaktives Histogramm der z-standardisierten Prüfungsangstwerte mit dem Stichprobenmittelwert bei null."
  ),
  sq = list(
    low_stress = "Stres i ulët",
    high_stress = "Stres i lartë",
    woman = "Grua",
    man = "Burrë",
    diverse = "Divers",
    exam_title = "Ankthi nga provimi te studentët e vitit të parë",
    exam_subtitle = "Shpërndarja e rezultateve të përgjithshme në shkallën 0–40",
    exam_x = "Rezultati i ankthit nga provimi (0–40)",
    students_y = "Numri i studentëve",
    box_title = "Ankthi nga provimi sipas grupit të stresit të vetëraportuar",
    box_subtitle = "Qendër më e lartë me ndryshueshmëri të përgjithshme të ngjashme mes grupeve",
    z_title = "Pikëzimet e standardizuara të ankthit nga provimi",
    z_subtitle = "Mesatarja = 0 dhe SD = 1. Vija e ndërprerë shënon mesataren",
    z_x = "Pikëzimi z",
    gender_title = "Shpërndarja e gjinisë (ndryshore nominale)",
    gender_subtitle = "Çdo shtyllë paraqet një kategori, ndërsa rendi i kategorive nominale mund të zgjidhet lirisht",
    gender_x = "Gjinia",
    stress_title = "Shpërndarja e grupeve të stresit (ndryshore nominale)",
    stress_subtitle = "Këndi i sektorit paraqet përqindjen e secilës kategori",
    stress_bar_subtitle = "Gjatësia e shtyllës paraqet numrin në secilën kategori",
    satisfaction_title = "Vlerësimet e kënaqësisë me studimet (ndryshore rendore)",
    satisfaction_subtitle = "Kategoritë ruhen në rendin e tyre natyror nga 1 deri në 5",
    satisfaction_x = "Kënaqësia (1 = kënaqësi shumë e ulët, 5 = kënaqësi shumë e lartë)",
    scale_learners_y = "Numri i nxënësve",
    scale_worked = "Shembuj të zgjidhur",
    scale_visual = "Shpjegime pamore",
    scale_guided = "Ushtrim i udhëhequr",
    scale_nominal_title = "Formati i parapëlqyer i të nxënit",
    scale_nominal_subtitle = "Kategoritë përshkruajnë zgjedhje pa rend natyror",
    scale_nominal_x = "Formati i parapëlqyer",
    scale_ordinal_title = "Siguria para punëtorisë",
    scale_ordinal_subtitle = "Vlerësimet ruhen në rendin e tyre kuptimplotë nga 1 deri në 5",
    scale_ordinal_x = "Siguria (1 = shumë i pasigurt, 5 = shumë i sigurt)",
    scale_interval_title = "Temperatura e dhomës gjatë punëtorisë",
    scale_interval_subtitle = "Dallimet e barabarta prej një grade kanë kuptim në shkallën Celsius",
    scale_temperature_x = "Temperatura e dhomës (°C)",
    scale_ratio_title = "Koha vullnetare e studimit para punëtorisë",
    scale_ratio_subtitle = "Zero minuta do të thotë se nuk u regjistrua kohë studimi",
    scale_minutes_x = "Koha e studimit (minuta)",
    scale_absolute_title = "Pyetjet praktike të përfunduara",
    scale_absolute_subtitle = "Çdo vlerë është numërim me njësinë fikse prej një pyetjeje",
    scale_questions_x = "Pyetjet e përfunduara",
    axis_full_title = "Të njëjtat vlera, boshti i plotë 0–100",
    axis_truncated_title = "Të njëjtat vlera, boshti i shkurtuar 64–76",
    axis_subtitle = "Vlerat identike mund të krijojnë përshtypje shumë të ndryshme",
    program_x = "Formati i punëtorisë",
    wellbeing_y = "Rezultati mesatar i mirëqenies (0–100)",
    guided_program = "Reflektim i udhëhequr",
    peer_program = "Diskutim mes bashkëmoshatarëve",
    bins_narrow_title = "Ankthi nga provimi me klasa prej 2 pikësh",
    bins_wide_title = "Ankthi nga provimi me klasa prej 8 pikësh",
    bins_subtitle = "Vrojtimet mbeten të njëjta, ndërsa grupimi ndryshon",
    value_x = "Vlera",
    frequency_y = "Frekuenca",
    shape_symmetric = "Shpërndarje simetrike",
    shape_right = "Shpërndarje me asimetri djathtas",
    shape_left = "Shpërndarje me asimetri majtas",
    shape_unimodal = "Shpërndarje unimodale",
    shape_bimodal = "Shpërndarje bimodale",
    shape_high_kurtosis = "Shpërndarje me kurtozë të lartë",
    shape_low_kurtosis = "Shpërndarje me kurtozë të ulët",
    hover_count = "Studentë:",
    hover_exam = "Rezultati i ankthit nga provimi:",
    hover_group = "Grupi i stresit:",
    hover_satisfaction = "Vlerësimi i kënaqësisë:",
    hover_z = "Pikëzimi z:",
    hover_mean = "Mesatarja e kampionit:",
    widget_alt_exam = "Histogram ndërveprues i pikëve të ankthit nga provimi, me shumicën e vlerave të përqendruara në mes.",
    widget_alt_box = "Dy diagrame ndërvepruese kuti-me-mustaqe krah për krah që tregojnë qendër më të lartë dhe shpërhapje të përgjithshme të ngjashme për grupin me stres të lartë.",
    widget_alt_z = "Histogram ndërveprues i pikëzimeve të standardizuara të ankthit nga provimi, me mesataren e kampionit të shënuar në zero."
  )
)[[topic_locale]]

# Keep long localized headings readable in both static teaching figures and
# the interactive versions reused in the simulated example. The wording is
# unchanged; only a natural line break is inserted when the available figure
# width would otherwise clip the text.
wrap_topic1_label <- function(text, width) {
  paste(strwrap(text, width = width), collapse = "\n")
}

# Convert a shared ggplot into a locale-aware Plotly figure. This keeps the
# same data and geometry while localizing hover labels, removing the default
# English toolbar, and exposing a detailed alternative to assistive technology.
topic_plotly <- function(
  plot,
  kind = c("generic", "exam", "box", "z"),
  alt_text = NULL,
  tooltip = c("x", "y")
) {
  kind <- match.arg(kind)
  plot <- ratiomera_make_plotly_compatible(plot)
  widget <- ggplotly(plot, tooltip = tooltip) |>
    ratiomera_prepare_plotly_widget(
      # Ordinary-width figures use the responsive page width; diagrams with a
      # wider teaching canvas are contained by the page's focusable scroll
      # region. Short lines keep translated headings inside either widget.
      title_width = 22,
      axis_width = 28,
      annotation_width = 32
    )

  common_replacements <- c(
    "count:" = topic_labels$hover_count,
    "n:" = topic_labels$hover_count,
    "gender:" = paste0(topic_labels$gender_x, ":"),
    "group:" = topic_labels$hover_group,
    "satisfaction:" = topic_labels$hover_satisfaction,
    "exam_anxiety:" = topic_labels$hover_exam,
    "z_exam_anxiety:" = topic_labels$hover_z
  )
  specific_replacements <- switch(
    kind,
    generic = character(),
    exam = c(
      "count:" = topic_labels$hover_count,
      "exam_anxiety:" = topic_labels$hover_exam
    ),
    box = c(
      "group:" = topic_labels$hover_group,
      "exam_anxiety:" = topic_labels$hover_exam
    ),
    z = c(
      "count:" = topic_labels$hover_count,
      "z_exam_anxiety:" = topic_labels$hover_z,
      "xintercept:" = topic_labels$hover_mean
    )
  )
  replacements <- c(specific_replacements, common_replacements)
  replacements <- replacements[!duplicated(names(replacements))]
  # Replace longer internal field names first. Otherwise the short token
  # "n:" also changes the end of "satisfaction:" before that field can be
  # translated into a concise, readable hover label.
  replacements <- replacements[
    order(nchar(names(replacements)), decreasing = TRUE)
  ]

  for (trace_index in seq_along(widget$x$data)) {
    for (field in c("text", "hovertext", "hovertemplate")) {
      field_value <- widget$x$data[[trace_index]][[field]]
      if (is.null(field_value)) next
      for (source_text in names(replacements)) {
        field_value <- gsub(
          source_text,
          replacements[[source_text]],
          field_value,
          fixed = TRUE
        )
      }
      widget$x$data[[trace_index]][[field]] <- field_value
    }
  }

  # Localize the generic ggplotly field prefixes that remain after the
  # topic-specific replacements above. Suppress raw trace names as well, so a
  # German or Albanian reader never encounters internal column names on hover.
  widget <- ratiomera_localize_plotly_hover(
    widget,
    ratiomera_plotly_hover_labels(plot, topic_locale)
  )

  if (identical(kind, "box")) {
    # The browser-generated box-summary labels are English-only. Keep the
    # boxes visually unchanged, suppress those default labels, and add a
    # transparent observation layer whose concise hover is localized here.
    # The layer is interactive but does not add visible dots to the boxplot.
    widget <- ratiomera_suppress_box_trace_hover(widget)
    box_group_levels <- c(topic_labels$low_stress, topic_labels$high_stress)
    box_hover_text <- paste0(
      topic_labels$hover_group,
      " ",
      as.character(plot$data$group),
      "<br>",
      topic_labels$hover_exam,
      " ",
      formatC(plot$data$exam_anxiety, format = "f", digits = 0)
    )
    widget$x$data[[length(widget$x$data) + 1L]] <- list(
      x = unname(match(as.character(plot$data$group), box_group_levels)),
      y = unname(plot$data$exam_anxiety),
      text = unname(box_hover_text),
      type = "scatter",
      mode = "markers",
      marker = list(
        color = "rgba(255,255,255,0.01)",
        line = list(width = 0),
        size = 14
      ),
      hoverinfo = "text",
      hovertemplate = "%{text}<extra></extra>",
      showlegend = FALSE,
      xaxis = "x",
      yaxis = "y"
    )
  }

  if (is.null(alt_text)) {
    alt_text <- switch(
      kind,
      generic = ratiomera_plotly_alt_from_plot(plot, topic_locale),
      exam = topic_labels$widget_alt_exam,
      box = topic_labels$widget_alt_box,
      z = topic_labels$widget_alt_z
    )
  }

  widget |>
    layout(
      autosize = TRUE,
      hovermode = "closest",
      margin = list(l = 76, r = 28, b = 82, t = 96, pad = 2)
    ) |>
    config(
      responsive = TRUE,
      displayModeBar = FALSE,
      displaylogo = FALSE,
      scrollZoom = FALSE
    ) |>
    htmlwidgets::onRender(
      "function(el, x, altText) { el.setAttribute('role', 'img'); el.setAttribute('aria-label', altText); }",
      data = alt_text
    )
}

# coord_polar is not converted reliably by ggplotly. Build this one chart as
# a native Plotly pie so its proportions, labels, and hover values remain
# correct rather than silently dropping the circular geometry.
topic1_stress_pie_plotly <- function(alt_text = NULL) {
  pie_hover <- paste0(
    as.character(tab_group_pie$group),
    "<br>", topic_labels$hover_count, " ", tab_group_pie$n,
    "<br>", tab_group_pie$pct
  )
  if (is.null(alt_text)) {
    alt_text <- if (topic_locale == "de") {
      "Interaktives Kreisdiagramm der Anteile in den beiden selbst berichteten Belastungsgruppen."
    } else if (topic_locale == "sq") {
      "Diagram ndërveprues rrethor i përqindjeve në dy grupet e stresit të vetëraportuar."
    } else {
      "Interactive pie chart of the proportions in the two self-reported stress groups."
    }
  }

  plot_ly(
    labels = as.character(tab_group_pie$group),
    values = tab_group_pie$n,
    type = "pie",
    text = pie_hover,
    hovertemplate = "%{text}<extra></extra>",
    textinfo = "label+percent",
    marker = list(
      colors = c("#2F6F9F", "#B7483B"),
      line = list(color = "white", width = 1.2)
    ),
    sort = FALSE
  ) |>
    layout(
      title = list(
        text = paste0("<b>", topic_labels$stress_title, "</b>")
      ),
      legend = list(orientation = "h", x = 0.5, xanchor = "center", y = -0.04),
      margin = list(l = 36, r = 36, b = 70, t = 112, pad = 2)
    ) |>
    ratiomera_prepare_plotly_widget(
      title_width = 28,
      axis_width = 28,
      annotation_width = 32
    ) |>
    config(
      responsive = TRUE,
      displayModeBar = FALSE,
      displaylogo = FALSE,
      scrollZoom = FALSE
    ) |>
    htmlwidgets::onRender(
      "function(el, x, altText) { el.setAttribute('role', 'img'); el.setAttribute('aria-label', altText); }",
      data = alt_text
    )
}

plot_theme <- function(base_size = 13) {
  theme_minimal(base_size = base_size) +
    theme(
      plot.title = element_text(face = "bold", color = "#172B3A"),
      plot.subtitle = element_text(color = "#536475"),
      axis.title = element_text(color = "#34495E"),
      axis.text = element_text(color = "#465A6B"),
      panel.grid.minor = element_blank(),
      panel.grid.major = element_line(color = "#E7ECF1"),
      plot.background = element_rect(fill = "white", color = NA)
    )
}

# A compact, newly authored workshop dataset supports the guided measurement-
# level sequence in all locales. The same twelve learners and values are reused
# across the five scales so that the statistical meaning, rather than a changing
# story, remains the focus. Internal codes and numerical geometry stay fixed.
scale_learning_data <- tibble(
  learner = seq_len(12),
  format_code = c(
    "worked", "visual", "guided", "worked", "guided", "visual",
    "worked", "worked", "guided", "visual", "worked", "visual"
  ),
  confidence = c(3, 4, 2, 3, 5, 4, 3, 2, 4, 1, 5, 3),
  room_temperature = c(18, 19, 19, 20, 20, 20, 21, 21, 21, 21, 22, 23),
  study_minutes = c(0, 15, 20, 25, 30, 35, 40, 45, 50, 60, 75, 90),
  practice_questions = c(0, 1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 7)
) |>
  mutate(
    learning_format = factor(
      format_code,
      levels = c("worked", "visual", "guided"),
      labels = c(
        topic_labels$scale_worked,
        topic_labels$scale_visual,
        topic_labels$scale_guided
      )
    ),
    confidence_category = factor(confidence, levels = 1:5, ordered = TRUE)
  )

scale_nominal_frequency <- scale_learning_data |>
  count(learning_format, name = "n", .drop = FALSE) |>
  mutate(proportion = n / sum(n))

scale_ordinal_frequency <- scale_learning_data |>
  count(confidence_category, name = "n", .drop = FALSE) |>
  arrange(confidence_category) |>
  mutate(
    proportion = n / sum(n),
    cumulative_proportion = cumsum(proportion)
  )

scale_absolute_frequency <- tibble(practice_questions = 0:7) |>
  left_join(
    scale_learning_data |> count(practice_questions, name = "n"),
    by = "practice_questions"
  ) |>
  mutate(n = coalesce(n, 0L)) |>
  mutate(proportion = n / sum(n))

p_scale_nominal_bar <- ggplot(
  scale_nominal_frequency,
  aes(x = learning_format, y = n)
) +
  geom_col(fill = "#2F6F9F", color = "white", width = 0.68) +
  geom_text(aes(label = n), vjust = -0.45, fontface = "bold", color = "#172B3A") +
  scale_x_discrete(
    labels = function(values) vapply(
      as.character(values),
      wrap_topic1_label,
      character(1),
      width = 16
    )
  ) +
  scale_y_continuous(breaks = 0:6, limits = c(0, 6)) +
  labs(
    title = wrap_topic1_label(topic_labels$scale_nominal_title, 46),
    subtitle = wrap_topic1_label(topic_labels$scale_nominal_subtitle, 64),
    x = topic_labels$scale_nominal_x,
    y = topic_labels$scale_learners_y
  ) +
  plot_theme(base_size = 11) +
  theme(panel.grid.major.x = element_blank())

p_scale_nominal_pie <- ggplot(
  scale_nominal_frequency,
  aes(x = "", y = n, fill = learning_format)
) +
  geom_col(width = 1, color = "white", linewidth = 1.1) +
  coord_polar(theta = "y") +
  geom_text(
    aes(label = paste0(round(100 * proportion), "%")),
    position = position_stack(vjust = 0.5),
    color = "white",
    fontface = "bold",
    size = 4
  ) +
  scale_fill_manual(
    values = c("#2F6F9F", "#B46124", "#39745A"),
    labels = function(values) vapply(
      as.character(values),
      wrap_topic1_label,
      character(1),
      width = 18
    )
  ) +
  labs(
    title = wrap_topic1_label(topic_labels$scale_nominal_title, 46),
    subtitle = wrap_topic1_label(topic_labels$scale_nominal_subtitle, 64),
    fill = topic_labels$scale_nominal_x
  ) +
  theme_void(base_size = 11) +
  theme(
    legend.position = "bottom",
    plot.title = element_text(face = "bold", hjust = 0.5, color = "#172B3A"),
    plot.subtitle = element_text(hjust = 0.5, color = "#536475")
  )

p_scale_ordinal_bar <- ggplot(
  scale_ordinal_frequency,
  aes(x = confidence_category, y = n)
) +
  geom_col(fill = "#B46124", color = "white", width = 0.72) +
  geom_text(aes(label = n), vjust = -0.45, fontface = "bold", color = "#172B3A") +
  scale_y_continuous(breaks = 0:5, limits = c(0, 5)) +
  labs(
    title = wrap_topic1_label(topic_labels$scale_ordinal_title, 46),
    subtitle = wrap_topic1_label(topic_labels$scale_ordinal_subtitle, 64),
    x = wrap_topic1_label(topic_labels$scale_ordinal_x, 52),
    y = topic_labels$scale_learners_y
  ) +
  plot_theme(base_size = 11) +
  theme(panel.grid.major.x = element_blank())

p_scale_interval_hist <- ggplot(
  scale_learning_data,
  aes(x = room_temperature)
) +
  geom_histogram(
    binwidth = 1,
    boundary = 17.5,
    fill = "#70558F",
    color = "white"
  ) +
  scale_x_continuous(breaks = 18:23) +
  labs(
    title = wrap_topic1_label(topic_labels$scale_interval_title, 46),
    subtitle = wrap_topic1_label(topic_labels$scale_interval_subtitle, 64),
    x = topic_labels$scale_temperature_x,
    y = topic_labels$scale_learners_y
  ) +
  plot_theme(base_size = 11)

p_scale_interval_box <- ggplot(
  scale_learning_data,
  aes(x = "", y = room_temperature)
) +
  geom_boxplot(width = 0.34, fill = "#D9CFE6", color = "#70558F", outlier.shape = NA) +
  geom_jitter(width = 0.075, height = 0, color = "#4E376A", size = 2.2) +
  scale_y_continuous(breaks = 18:23) +
  labs(
    title = wrap_topic1_label(topic_labels$scale_interval_title, 46),
    subtitle = wrap_topic1_label(topic_labels$scale_interval_subtitle, 64),
    x = NULL,
    y = topic_labels$scale_temperature_x
  ) +
  plot_theme(base_size = 11) +
  theme(panel.grid.major.x = element_blank(), axis.text.x = element_blank())

p_scale_ratio_hist <- ggplot(scale_learning_data, aes(x = study_minutes)) +
  geom_histogram(
    binwidth = 15,
    boundary = 0,
    fill = "#25796E",
    color = "white"
  ) +
  scale_x_continuous(breaks = seq(0, 90, by = 15), limits = c(0, 90)) +
  labs(
    title = wrap_topic1_label(topic_labels$scale_ratio_title, 46),
    subtitle = wrap_topic1_label(topic_labels$scale_ratio_subtitle, 64),
    x = topic_labels$scale_minutes_x,
    y = topic_labels$scale_learners_y
  ) +
  plot_theme(base_size = 11)

p_scale_ratio_box <- ggplot(scale_learning_data, aes(x = "", y = study_minutes)) +
  geom_boxplot(width = 0.34, fill = "#CBE4DF", color = "#25796E", outlier.shape = NA) +
  geom_jitter(width = 0.075, height = 0, color = "#15594F", size = 2.2) +
  scale_y_continuous(breaks = seq(0, 90, by = 15), limits = c(0, 90)) +
  labs(
    title = wrap_topic1_label(topic_labels$scale_ratio_title, 46),
    subtitle = wrap_topic1_label(topic_labels$scale_ratio_subtitle, 64),
    x = NULL,
    y = topic_labels$scale_minutes_x
  ) +
  plot_theme(base_size = 11) +
  theme(panel.grid.major.x = element_blank(), axis.text.x = element_blank())

p_scale_absolute_bar <- ggplot(
  scale_absolute_frequency,
  aes(x = factor(practice_questions), y = n)
) +
  geom_col(fill = "#B7483B", color = "white", width = 0.72) +
  geom_text(aes(label = n), vjust = -0.45, fontface = "bold", color = "#172B3A") +
  scale_y_continuous(breaks = 0:4, limits = c(0, 4)) +
  labs(
    title = wrap_topic1_label(topic_labels$scale_absolute_title, 46),
    subtitle = wrap_topic1_label(topic_labels$scale_absolute_subtitle, 64),
    x = topic_labels$scale_questions_x,
    y = topic_labels$scale_learners_y
  ) +
  plot_theme(base_size = 11) +
  theme(panel.grid.major.x = element_blank())

p_scale_absolute_box <- ggplot(
  scale_learning_data,
  aes(x = "", y = practice_questions)
) +
  geom_boxplot(width = 0.34, fill = "#F0D2CE", color = "#B7483B", outlier.shape = NA) +
  geom_jitter(width = 0.075, height = 0, color = "#86342C", size = 2.2) +
  scale_y_continuous(breaks = 0:7, limits = c(0, 7)) +
  labs(
    title = wrap_topic1_label(topic_labels$scale_absolute_title, 46),
    subtitle = wrap_topic1_label(topic_labels$scale_absolute_subtitle, 64),
    x = NULL,
    y = topic_labels$scale_questions_x
  ) +
  plot_theme(base_size = 11) +
  theme(panel.grid.major.x = element_blank(), axis.text.x = element_blank())

# Deliberately constructed summary values make each Tukey-boxplot component
# visible. They do not claim an underlying raw dataset and remain identical
# across locales.
boxplot_anatomy_text <- if (topic_locale == "de") {
  list(
    title = "Anatomie eines Tukey-Boxplots",
    subtitle = "Berechnete Grenzen und beobachtete Whisker-Enden sind nicht dasselbe",
    axis = "Geordneter Wert",
    q1 = "Q₁ = 4,5",
    median = "Median = 7",
    q3 = "Q₃ = 9,5",
    iqr = "IQR = 5",
    lower_fence = "Untere Grenze = -3",
    upper_fence = "Obere Grenze = 17",
    lower_whisker = "Unterer Whisker = 2",
    upper_whisker = "Oberer Whisker = 11",
    outlier = "Möglicher Ausreisser = 30"
  )
} else if (topic_locale == "sq") {
  list(
    title = "Anatomia e diagramit kuti-me-mustaqe të Tukey-t",
    subtitle = "Kufijtë e llogaritur dhe skajet e vrojtuara të mustaqeve nuk janë e njëjta gjë",
    axis = "Vlera e renditur",
    q1 = "Q₁ = 4,5",
    median = "Mediana = 7",
    q3 = "Q₃ = 9,5",
    iqr = "IQR = 5",
    lower_fence = "Kufiri i poshtëm = -3",
    upper_fence = "Kufiri i sipërm = 17",
    lower_whisker = "Mustaqja e poshtme = 2",
    upper_whisker = "Mustaqja e sipërme = 11",
    outlier = "Vlerë e mundshme e veçuar = 30"
  )
} else {
  list(
    title = "Anatomy of a Tukey Boxplot",
    subtitle = "Calculated fences and observed whisker endpoints are not the same thing",
    axis = "Ordered value",
    q1 = "Q₁ = 4.5",
    median = "Median = 7",
    q3 = "Q₃ = 9.5",
    iqr = "IQR = 5",
    lower_fence = "Lower fence = -3",
    upper_fence = "Upper fence = 17",
    lower_whisker = "Lower whisker = 2",
    upper_whisker = "Upper whisker = 11",
    outlier = "Potential outlier = 30"
  )
}

boxplot_q1 <- 4.5
boxplot_median <- 7
boxplot_q3 <- 9.5
boxplot_iqr <- boxplot_q3 - boxplot_q1
boxplot_lower_fence <- boxplot_q1 - 1.5 * boxplot_iqr
boxplot_upper_fence <- boxplot_q3 + 1.5 * boxplot_iqr
boxplot_lower_whisker <- 2
boxplot_upper_whisker <- 11
boxplot_outlier <- 30

p_boxplot_anatomy <- ggplot() +
  annotate(
    "rect",
    xmin = boxplot_q1,
    xmax = boxplot_q3,
    ymin = 0.91,
    ymax = 1.09,
    fill = "#DCEAF2",
    color = "#2F6F9F",
    linewidth = 0.8
  ) +
  annotate(
    "segment",
    x = boxplot_lower_whisker,
    xend = boxplot_q1,
    y = 1,
    yend = 1,
    color = "#2F6F9F",
    linewidth = 0.9
  ) +
  annotate(
    "segment",
    x = boxplot_q3,
    xend = boxplot_upper_whisker,
    y = 1,
    yend = 1,
    color = "#2F6F9F",
    linewidth = 0.9
  ) +
  annotate(
    "segment",
    x = c(boxplot_lower_whisker, boxplot_upper_whisker, boxplot_median),
    xend = c(boxplot_lower_whisker, boxplot_upper_whisker, boxplot_median),
    y = c(0.93, 0.93, 0.90),
    yend = c(1.07, 1.07, 1.10),
    color = c("#2F6F9F", "#2F6F9F", "#173B57"),
    linewidth = c(0.8, 0.8, 1.1)
  ) +
  annotate(
    "segment",
    x = c(boxplot_lower_fence, boxplot_upper_fence),
    xend = c(boxplot_lower_fence, boxplot_upper_fence),
    y = 0.78,
    yend = 1.33,
    linetype = "dashed",
    color = "#B46124",
    linewidth = 0.65
  ) +
  annotate(
    "segment",
    x = boxplot_q1,
    xend = boxplot_q3,
    y = 0.69,
    yend = 0.69,
    color = "#536475",
    linewidth = 0.65
  ) +
  annotate(
    "segment",
    x = c(boxplot_q1, boxplot_q3),
    xend = c(boxplot_q1, boxplot_q3),
    y = 0.65,
    yend = 0.73,
    color = "#536475",
    linewidth = 0.65
  ) +
  annotate("point", x = boxplot_outlier, y = 1, color = "#B7483B", size = 3.1) +
  annotate(
    "text",
    x = c(boxplot_q1, boxplot_median, boxplot_q3),
    y = c(1.22, 1.38, 1.22),
    label = c(boxplot_anatomy_text$q1, boxplot_anatomy_text$median, boxplot_anatomy_text$q3),
    color = "#203A4F",
    fontface = "bold",
    size = 3.05
  ) +
  annotate(
    "text",
    x = (boxplot_q1 + boxplot_q3) / 2,
    y = 0.60,
    label = boxplot_anatomy_text$iqr,
    color = "#536475",
    fontface = "bold",
    size = 3.05
  ) +
  annotate(
    "text",
    x = c(boxplot_lower_fence, boxplot_upper_fence),
    y = 1.48,
    label = c(boxplot_anatomy_text$lower_fence, boxplot_anatomy_text$upper_fence),
    color = "#8A4B1E",
    fontface = "bold",
    size = 2.9
  ) +
  annotate(
    "text",
    x = c(boxplot_lower_whisker, boxplot_upper_whisker),
    y = 0.82,
    label = c(boxplot_anatomy_text$lower_whisker, boxplot_anatomy_text$upper_whisker),
    color = "#204D70",
    size = 2.85
  ) +
  annotate(
    "text",
    x = boxplot_outlier,
    y = 1.19,
    label = boxplot_anatomy_text$outlier,
    color = "#8A3F36",
    fontface = "bold",
    size = 2.95
  ) +
  scale_x_continuous(
    breaks = c(-3, 2, 4.5, 7, 9.5, 11, 17, 30),
    limits = c(-4.5, 32)
  ) +
  scale_y_continuous(NULL, breaks = NULL) +
  coord_cartesian(ylim = c(0.50, 1.58), clip = "off") +
  labs(
    title = boxplot_anatomy_text$title,
    subtitle = boxplot_anatomy_text$subtitle,
    x = boxplot_anatomy_text$axis
  ) +
  plot_theme(base_size = 11) +
  theme(
    panel.grid.major.y = element_blank(),
    panel.grid.minor = element_blank(),
    plot.margin = margin(14, 22, 14, 22)
  )

set.seed(42)
n <- 160

dat <- tibble(
  id = 1:n,
  group = sample(
    c(topic_labels$low_stress, topic_labels$high_stress),
    size = n,
    replace = TRUE,
    prob = c(0.55, 0.45)
  ),
  gender = sample(
    c(topic_labels$woman, topic_labels$man, topic_labels$diverse),
    size = n,
    replace = TRUE,
    prob = c(0.60, 0.35, 0.05)
  )
) |>
  mutate(
    group = factor(
      group,
      levels = c(topic_labels$low_stress, topic_labels$high_stress)
    ),
    gender = factor(
      gender,
      levels = c(topic_labels$woman, topic_labels$man, topic_labels$diverse)
    )
  )

dat <- dat |>
  mutate(
    sleep_hours = rnorm(
      n(),
      mean = ifelse(group == topic_labels$high_stress, 6.2, 7.1),
      sd = 1.1
    ),
    sleep_hours = round(pmin(pmax(sleep_hours, 3), 10), 1),
    exam_anxiety = rnorm(
      n(),
      mean = ifelse(group == topic_labels$high_stress, 24, 18),
      sd = 5
    ),
    exam_anxiety = round(pmin(pmax(exam_anxiety, 0), 40))
  )

z_anx <- scale(dat$exam_anxiety)[, 1]
dat <- dat |>
  mutate(
    satisfaction_latent = 4.2 - 0.6 * z_anx + rnorm(n(), 0, 0.5),
    satisfaction = round(pmin(pmax(satisfaction_latent, 1), 5)),
    z_exam_anxiety = (exam_anxiety - mean(exam_anxiety)) / sd(exam_anxiety)
  ) |>
  select(-satisfaction_latent)

tab_group <- dat |>
  count(group, name = "n") |>
  mutate(prop = 100 * n / sum(n))

tab_gender <- dat |>
  count(gender, name = "n") |>
  mutate(prop = 100 * n / sum(n))

tab_satisfaction <- dat |>
  mutate(satisfaction = factor(satisfaction, levels = 1:5)) |>
  count(satisfaction, name = "n", .drop = FALSE) |>
  arrange(satisfaction) |>
  mutate(prop = 100 * n / sum(n))

data_profile <- dat |>
  summarise(
    sleep_min = min(sleep_hours),
    sleep_max = max(sleep_hours),
    anxiety_min = min(exam_anxiety),
    anxiety_max = max(exam_anxiety),
    satisfaction_min = min(satisfaction),
    satisfaction_max = max(satisfaction),
    missing_values = sum(is.na(across(everything())))
  )

overall_exam <- dat |>
  summarise(
    n = n(),
    mean = mean(exam_anxiety),
    median = median(exam_anxiety),
    sd = sd(exam_anxiety),
    IQR = IQR(exam_anxiety),
    min = min(exam_anxiety),
    max = max(exam_anxiety)
  )

exam_by_group <- dat |>
  group_by(group) |>
  summarise(
    n = n(),
    mean = mean(exam_anxiety),
    median = median(exam_anxiety),
    sd = sd(exam_anxiety),
    IQR = IQR(exam_anxiety),
    .groups = "drop"
  )

z_sample <- dat |>
  select(id, group, exam_anxiety, z_exam_anxiety) |>
  mutate(z_exam_anxiety = round(z_exam_anxiety, 2)) |>
  slice(1:12)

p_hist_exam <- ggplot(dat, aes(x = exam_anxiety)) +
  geom_histogram(binwidth = 2, boundary = 0, color = "white", fill = "#2F6F9F") +
  scale_x_continuous(breaks = seq(0, 40, by = 5), limits = c(0, 40)) +
  labs(
    title = topic_labels$exam_title,
    subtitle = topic_labels$exam_subtitle,
    x = topic_labels$exam_x,
    y = topic_labels$students_y
  ) +
  plot_theme()

p_box_exam <- ggplot(dat, aes(x = group, y = exam_anxiety, fill = group)) +
  geom_boxplot(alpha = 0.9, width = 0.55, outlier.alpha = 0.9, outlier.size = 2.2) +
  scale_fill_manual(
    values = setNames(c("#2F6F9F", "#B7483B"), c(topic_labels$low_stress, topic_labels$high_stress))
  ) +
  scale_x_discrete(
    labels = function(values) vapply(
      as.character(values),
      wrap_topic1_label,
      character(1),
      width = 10
    )
  ) +
  scale_y_continuous(breaks = seq(0, 40, by = 5), limits = c(0, 40)) +
  labs(
    title = wrap_topic1_label(topic_labels$box_title, 46),
    subtitle = wrap_topic1_label(topic_labels$box_subtitle, 58),
    x = "",
    y = topic_labels$exam_x
  ) +
  plot_theme() +
  theme(legend.position = "none")

z_hist_breaks <- (seq(0, 40, by = 2) - mean(dat$exam_anxiety)) / sd(dat$exam_anxiety)

p_hist_z <- ggplot(dat, aes(x = z_exam_anxiety)) +
  geom_histogram(breaks = z_hist_breaks, color = "white", fill = "#70558F") +
  geom_vline(xintercept = 0, linetype = "dashed", color = "#536475", linewidth = 0.8) +
  scale_x_continuous(breaks = seq(-3, 3, by = 1)) +
  labs(
    title = topic_labels$z_title,
    subtitle = topic_labels$z_subtitle,
    x = topic_labels$z_x,
    y = topic_labels$students_y
  ) +
  plot_theme()

tab_group_pie <- tab_group |>
  mutate(
    pct = paste0(round(prop, 1), "%"),
    pie_label = paste0(
      vapply(as.character(group), wrap_topic1_label, character(1), width = 12),
      "\n",
      pct
    )
  )

p_bar_gender <- ggplot(dat, aes(x = gender)) +
  geom_bar(fill = "#2F6F9F", color = "white") +
  labs(
    title = wrap_topic1_label(topic_labels$gender_title, 46),
    subtitle = wrap_topic1_label(topic_labels$gender_subtitle, 58),
    x = topic_labels$gender_x,
    y = topic_labels$students_y
  ) +
  plot_theme() +
  theme(panel.grid.major.x = element_blank())

p_bar_stress <- ggplot(tab_group, aes(x = group, y = n, fill = group)) +
  geom_col(color = "white", width = 0.68) +
  geom_text(aes(label = n), vjust = -0.45, fontface = "bold", color = "#172B3A") +
  scale_fill_manual(
    values = setNames(c("#2F6F9F", "#B7483B"), c(topic_labels$low_stress, topic_labels$high_stress))
  ) +
  scale_y_continuous(expand = expansion(mult = c(0, 0.1))) +
  labs(
    title = wrap_topic1_label(topic_labels$stress_title, 46),
    subtitle = topic_labels$stress_bar_subtitle,
    x = "",
    y = topic_labels$students_y
  ) +
  plot_theme() +
  theme(legend.position = "none", panel.grid.major.x = element_blank())

p_pie_group <- ggplot(tab_group_pie, aes(x = "", y = n, fill = group)) +
  geom_col(width = 1, color = "white", linewidth = 1.2) +
  coord_polar(theta = "y") +
  geom_text(
    aes(label = pie_label),
    position = position_stack(vjust = 0.5),
    size = 4.2,
    fontface = "bold",
    color = "white"
  ) +
  scale_fill_manual(
    values = setNames(c("#2F6F9F", "#B7483B"), c(topic_labels$low_stress, topic_labels$high_stress))
  ) +
  labs(
    title = wrap_topic1_label(topic_labels$stress_title, 46),
    subtitle = wrap_topic1_label(topic_labels$stress_subtitle, 66)
  ) +
  theme_void(base_size = 13) +
  theme(
    legend.position = "none",
    plot.title = element_text(face = "bold", hjust = 0.5, color = "#172B3A"),
    plot.subtitle = element_text(color = "#536475", hjust = 0.5)
  )

p_bar_satisfaction <- ggplot(tab_satisfaction, aes(x = satisfaction, y = n)) +
  geom_col(fill = "#B46124", color = "white") +
  labs(
    title = topic_labels$satisfaction_title,
    subtitle = topic_labels$satisfaction_subtitle,
    x = topic_labels$satisfaction_x,
    y = topic_labels$students_y
  ) +
  plot_theme() +
  theme(panel.grid.major.x = element_blank())

axis_comparison <- tibble(
  program = factor(
    c(topic_labels$guided_program, topic_labels$peer_program),
    levels = c(topic_labels$guided_program, topic_labels$peer_program)
  ),
  wellbeing = c(68, 72)
)

axis_plot <- function(title, y_breaks, y_limits = NULL) {
  plot <- ggplot(axis_comparison, aes(x = program, y = wellbeing)) +
    geom_col(width = 0.62, fill = "#2F6F9F", color = "white") +
    geom_text(aes(label = wellbeing), vjust = -0.5, fontface = "bold", color = "#172B3A") +
    scale_y_continuous(breaks = y_breaks, expand = expansion(mult = c(0, 0.08))) +
    labs(
      title = title,
      subtitle = topic_labels$axis_subtitle,
      x = topic_labels$program_x,
      y = topic_labels$wellbeing_y
    ) +
    plot_theme() +
    theme(panel.grid.major.x = element_blank())
  if (!is.null(y_limits)) plot <- plot + coord_cartesian(ylim = y_limits)
  plot
}

p_axis_full <- axis_plot(topic_labels$axis_full_title, seq(0, 100, by = 20), c(0, 100))
p_axis_truncated <- axis_plot(topic_labels$axis_truncated_title, seq(64, 76, by = 2), c(64, 76))

p_bins_narrow <- ggplot(dat, aes(x = exam_anxiety)) +
  geom_histogram(binwidth = 2, boundary = 0, color = "white", fill = "#2F6F9F") +
  scale_x_continuous(breaks = seq(0, 40, by = 5), limits = c(0, 40)) +
  labs(
    title = topic_labels$bins_narrow_title,
    subtitle = topic_labels$bins_subtitle,
    x = topic_labels$exam_x,
    y = topic_labels$students_y
  ) +
  plot_theme()

p_bins_wide <- ggplot(dat, aes(x = exam_anxiety)) +
  geom_histogram(binwidth = 8, boundary = 0, color = "white", fill = "#70558F") +
  scale_x_continuous(breaks = seq(0, 40, by = 5), limits = c(0, 40)) +
  labs(
    title = topic_labels$bins_wide_title,
    subtitle = topic_labels$bins_subtitle,
    x = topic_labels$exam_x,
    y = topic_labels$students_y
  ) +
  plot_theme()

set.seed(99)
n_shape <- 350
shape_symmetric <- rnorm(n_shape, 50, 10)
shape_right <- rbeta(n_shape, 1.5, 6) * 100
shape_left <- rbeta(n_shape, 6, 1.5) * 100
shape_unimodal <- rnorm(n_shape, 50, 10)
shape_bimodal <- c(rnorm(n_shape / 2, 30, 5), rnorm(n_shape / 2, 70, 5))
shape_high_kurtosis <- c(rnorm(round(n_shape * 0.9), 50, 4), rnorm(n_shape - round(n_shape * 0.9), 50, 22))
shape_high_kurtosis <- 50 + 10 * as.numeric(scale(shape_high_kurtosis))
shape_low_kurtosis <- runif(n_shape, 50 - sqrt(3) * 10, 50 + sqrt(3) * 10)

shape_plot <- function(values, title, fill, bins = 22, breaks = NULL, limits = NULL) {
  histogram_layer <- if (is.null(breaks)) {
    geom_histogram(bins = bins, fill = fill, color = "white")
  } else {
    geom_histogram(breaks = breaks, fill = fill, color = "white")
  }

  plot <- ggplot(data.frame(x = values), aes(x)) +
    histogram_layer +
    labs(title = title, x = topic_labels$value_x, y = topic_labels$frequency_y) +
    plot_theme(base_size = 11)
  if (!is.null(limits)) plot <- plot + scale_x_continuous(limits = limits)
  plot
}

p_shape_sym <- shape_plot(shape_symmetric, topic_labels$shape_symmetric, "#2F6F9F")
p_shape_right <- shape_plot(shape_right, topic_labels$shape_right, "#B7483B")
p_shape_left <- shape_plot(shape_left, topic_labels$shape_left, "#B46124")
p_shape_uni <- shape_plot(shape_unimodal, topic_labels$shape_unimodal, "#39745A")
p_shape_bi <- shape_plot(shape_bimodal, topic_labels$shape_bimodal, "#70558F", bins = 28)
kurtosis_breaks <- seq(0, 100, by = 5)

p_shape_high_kurtosis <- shape_plot(
  shape_high_kurtosis,
  topic_labels$shape_high_kurtosis,
  "#25796E",
  breaks = kurtosis_breaks,
  limits = c(0, 100)
)
p_shape_low_kurtosis <- shape_plot(
  shape_low_kurtosis,
  topic_labels$shape_low_kurtosis,
  "#66737F",
  breaks = kurtosis_breaks,
  limits = c(0, 100)
)
