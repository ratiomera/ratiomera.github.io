# Shared deterministic data, calculations, tables, and figure geometry for
# Topic 4. Each locale page sets topic_locale before sourcing this file. The
# observations and every numerical result remain identical across locales.

if (!exists("topic_locale", inherits = FALSE)) topic_locale <- "en"
if (!topic_locale %in% c("en", "de", "sq")) {
  stop("Topic 4 labels have not yet been reviewed for locale: ", topic_locale, call. = FALSE)
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

t04_label_sets <- list(
  en = list(
    positive = "Positive linear association",
    negative = "Negative linear association",
    little = "Little linear association",
    pearson_prefix = "Pearson r = ",
    variable_x = "Variable X",
    variable_y = "Variable Y",
    direction_title = "The Sign of Covariance and Correlation",
    direction_subtitle = "The sign follows the direction of the straight-line pattern",
    curved_monotonic = "Curved but monotonic",
    u_nonmonotonic = "U-shaped and non-monotonic",
    shape_title = "A Scatterplot Reveals What One Coefficient Can Miss",
    shape_subtitle = "Spearman follows monotonic order; neither coefficient summarizes a U-shape well",
    paired_cases = "Number of paired cases",
    mean_hours = "Mean weekly study hours",
    sd_hours = "SD of weekly study hours",
    mean_score = "Mean exam score",
    sd_score = "SD of exam score",
    sample_covariance = "Sample covariance",
    pearson_correlation = "Pearson correlation",
    spearman_correlation = "Spearman rank correlation",
    hours_points = "Study hours and score points",
    minutes_points = "Study minutes and score points",
    scatter_title = "Weekly Study Time and Exam Score",
    scatter_subtitle = "Constructed teaching cohort; Pearson r = ",
    study_hours_axis = "Weekly study time (hours)",
    exam_score_axis = "Exam score (0 to 100)",
    original_units = "Original units",
    standardized_units = "Standardized units",
    standardization_title = "Standardization Changes the Axes, Not the Correlation",
    standardization_subtitle = "The relative positions of the cases remain the same",
    study_value = "Study-time value",
    score_value = "Exam-score value",
    original_case = "Original case",
    added_point = "Added point",
    original_cohort = "Original cohort",
    point_added = "One illustrative point added",
    outlier_title = "One Unusual Point Can Change Pearson's r",
    outlier_subtitle = "The added point is a diagnostic illustration, not a member of the cohort",
    full_range = "Full observed range",
    restricted_range = "Only 5 to 8 hours",
    range_title = "Restricting the Observed Range Can Weaken r",
    range_subtitle = "Both panels come from the same constructed cohort",
    x_affects_y = "X may affect Y",
    y_affects_x = "Y may affect X",
    third_affects_both = "A third variable may affect both",
    study_node = "Study\nhours",
    score_node = "Exam\nscore",
    preparation_node = "Prior\npreparation",
    causal_title = "One Correlation Is Compatible with Different Causal Stories",
    causal_subtitle = "The correlation coefficient alone cannot choose among these arrows",
    participant = "Participant",
    prior_preparation_axis = "Prior preparation score",
    third_variable_title = "Prior Preparation Connects to Both Measured Variables",
    third_variable_subtitle = "The known simulation recipe makes the two third-variable paths visible",
    third_study_panel = "Prior preparation and study time",
    third_score_panel = "Prior preparation and exam score",
    panel_value = "Value in each panel",
    fitted_values = "Fitted values"
  ),
  de = list(
    positive = "Positive lineare Beziehung",
    negative = "Negative lineare Beziehung",
    little = "Geringe lineare Beziehung",
    pearson_prefix = "Pearson-r = ",
    variable_x = "Variable X",
    variable_y = "Variable Y",
    direction_title = "Das Vorzeichen von Kovarianz und Korrelation",
    direction_subtitle = "Das Vorzeichen folgt der Richtung des geradlinigen Musters",
    curved_monotonic = "Gekrümmt, aber monoton",
    u_nonmonotonic = "U-förmig und nicht monoton",
    shape_title = "Ein Streudiagramm zeigt, was ein einzelner Koeffizient übersehen kann",
    shape_subtitle = "Spearman folgt der monotonen Rangfolge;\neine U-Form wird von keinem der beiden Koeffizienten gut zusammengefasst",
    paired_cases = "Anzahl gepaarter Fälle",
    mean_hours = "Mittlere wöchentliche Lernzeit",
    sd_hours = "SD der wöchentlichen Lernzeit",
    mean_score = "Mittlere Prüfungspunktzahl",
    sd_score = "SD der Prüfungspunktzahl",
    sample_covariance = "Stichprobenkovarianz",
    pearson_correlation = "Pearson-Korrelation",
    spearman_correlation = "Spearman-Rangkorrelation",
    hours_points = "Lernstunden und Prüfungspunkte",
    minutes_points = "Lernminuten und Prüfungspunkte",
    scatter_title = "Wöchentliche Lernzeit und Prüfungspunktzahl",
    scatter_subtitle = "Konstruierte Lernkohorte; Pearson-r = ",
    study_hours_axis = "Wöchentliche Lernzeit (Stunden)",
    exam_score_axis = "Prüfungspunktzahl (0 bis 100)",
    original_units = "Ursprüngliche Einheiten",
    standardized_units = "Standardisierte Einheiten",
    standardization_title = "Standardisierung verändert die Achsen, nicht die Korrelation",
    standardization_subtitle = "Die relativen Positionen der Fälle bleiben gleich",
    study_value = "Wert der Lernzeit",
    score_value = "Wert der Prüfungspunktzahl",
    original_case = "Ursprünglicher Fall",
    added_point = "Hinzugefügter Punkt",
    original_cohort = "Ursprüngliche Kohorte",
    point_added = "Ein veranschaulichender Punkt hinzugefügt",
    outlier_title = "Ein ungewöhnlicher Punkt kann Pearson-r verändern",
    outlier_subtitle = "Der hinzugefügte Punkt dient nur zur Diagnose und gehört nicht zur Kohorte",
    full_range = "Gesamter beobachteter Bereich",
    restricted_range = "Nur 5 bis 8 Stunden",
    range_title = "Ein eingeschränkter Beobachtungsbereich\nkann r abschwächen",
    range_subtitle = "Beide Felder stammen aus derselben konstruierten Kohorte",
    x_affects_y = "X kann Y beeinflussen",
    y_affects_x = "Y kann X beeinflussen",
    third_affects_both = "Eine dritte Variable kann beide beeinflussen",
    study_node = "Lern-\nstunden",
    score_node = "Prüfungs-\npunkte",
    preparation_node = "Vor-\nbereitung",
    causal_title = "Eine Korrelation passt zu unterschiedlichen Kausalgeschichten",
    causal_subtitle = "Der Korrelationskoeffizient allein kann nicht zwischen diesen Pfeilen entscheiden",
    participant = "Teilnehmende Person",
    prior_preparation_axis = "Wert der Vorbereitungsleistung",
    third_variable_title = "Vorbereitung hängt mit beiden gemessenen Variablen zusammen",
    third_variable_subtitle = "Die bekannte Simulationsregel macht beide Pfade der Drittvariable sichtbar",
    third_study_panel = "Vorbereitung und Lernzeit",
    third_score_panel = "Vorbereitung und Prüfungspunktzahl",
    panel_value = "Wert im jeweiligen Feld",
    fitted_values = "Angepasste Werte"
  ),
  sq = list(
    positive = "Lidhje lineare pozitive",
    negative = "Lidhje lineare negative",
    little = "Lidhje e dobët lineare",
    pearson_prefix = "r e Pearson-it = ",
    variable_x = "Ndryshorja X",
    variable_y = "Ndryshorja Y",
    direction_title = "Shenja e kovariancës dhe e korrelacionit",
    direction_subtitle = "Shenja ndjek drejtimin e modelit drejtvizor",
    curved_monotonic = "E lakuar, por monotone",
    u_nonmonotonic = "Në formë U-je dhe jomonotone",
    shape_title = "Diagrami i shpërndarjes tregon çfarë mund të fshehë një koeficient i vetëm",
    shape_subtitle = "Spearman-i ndjek renditjen monotone;\nasnjëri koeficient nuk e përmbledh mirë një formë U-je",
    paired_cases = "Numri i rasteve të çiftuara",
    mean_hours = "Mesatarja e orëve javore të studimit",
    sd_hours = "DS-ja e orëve javore të studimit",
    mean_score = "Mesatarja e pikëve në provim",
    sd_score = "DS-ja e pikëve në provim",
    sample_covariance = "Kovarianca e kampionit",
    pearson_correlation = "Korrelacioni i Pearson-it",
    spearman_correlation = "Korrelacioni i rangjeve të Spearman-it",
    hours_points = "Orë studimi dhe pikë provimi",
    minutes_points = "Minuta studimi dhe pikë provimi",
    scatter_title = "Koha javore e studimit dhe pikët në provim",
    scatter_subtitle = "Kohortë e krijuar për mësim; r e Pearson-it = ",
    study_hours_axis = "Koha javore e studimit (orë)",
    exam_score_axis = "Pikët në provim (0 deri në 100)",
    original_units = "Njësitë fillestare",
    standardized_units = "Njësitë e standardizuara",
    standardization_title = "Standardizimi ndryshon boshtet, jo korrelacionin",
    standardization_subtitle = "Pozicionet relative të rasteve mbeten të njëjta",
    study_value = "Vlera e kohës së studimit",
    score_value = "Vlera e pikëve në provim",
    original_case = "Rast fillestar",
    added_point = "Pikë e shtuar",
    original_cohort = "Kohorta fillestare",
    point_added = "U shtua një pikë ilustruese",
    outlier_title = "Një pikë e pazakontë mund ta ndryshojë r e Pearson-it",
    outlier_subtitle = "Pika e shtuar shërben për kontroll diagnostik dhe nuk është pjesë e kohortës",
    full_range = "Diapazoni i plotë i vrojtuar",
    restricted_range = "Vetëm 5 deri në 8 orë",
    range_title = "Kufizimi i diapazonit të vrojtuar mund ta dobësojë r",
    range_subtitle = "Të dy panelet vijnë nga e njëjta kohortë e krijuar",
    x_affects_y = "X mund të ndikojë te Y",
    y_affects_x = "Y mund të ndikojë te X",
    third_affects_both = "Një ndryshore e tretë mund të ndikojë te të dyja",
    study_node = "Orët e\nstudimit",
    score_node = "Pikët në\nprovim",
    preparation_node = "Përgatitja e\nmëparshme",
    causal_title = "Një korrelacion përputhet me shpjegime të ndryshme shkakësore",
    causal_subtitle = "Vetëm koeficienti i korrelacionit nuk mund të zgjedhë mes këtyre shigjetave",
    participant = "Pjesëmarrësi",
    prior_preparation_axis = "Pikëzimi i përgatitjes së mëparshme",
    third_variable_title = "Përgatitja e mëparshme lidhet me të dyja ndryshoret e matura",
    third_variable_subtitle = "Rregulli i njohur i simulimit i bën të dukshme të dyja rrugët e ndryshores së tretë",
    third_study_panel = "Përgatitja dhe koha e studimit",
    third_score_panel = "Përgatitja dhe pikët në provim",
    panel_value = "Vlera në secilin panel",
    fitted_values = "Vlerat e përshtatura"
  )
)
t04_labels <- t04_label_sets[[topic_locale]]

required_packages <- c("dplyr", "tibble", "tidyr", "ggplot2", "DT", "plotly", "htmlwidgets", "knitr", "cowplot")
missing_packages <- required_packages[
  !vapply(required_packages, requireNamespace, logical(1), quietly = TRUE)
]
if (length(missing_packages)) {
  stop(
    "Topic 4 requires these R packages: ",
    paste(missing_packages, collapse = ", "),
    call. = FALSE
  )
}

suppressPackageStartupMessages({
  library(dplyr)
  library(tibble)
  library(tidyr)
  library(ggplot2)
  library(plotly)
  library(knitr)
})

t04_theme <- function(base_size = 12) {
  theme_minimal(base_size = base_size) +
    theme(
      plot.title = element_text(face = "bold", color = "#172B3A"),
      plot.subtitle = element_text(color = "#536475"),
      axis.title = element_text(color = "#34495E"),
      axis.text = element_text(color = "#465A6B"),
      strip.text = element_text(face = "bold", color = "#203A4F"),
      panel.grid.minor = element_blank(),
      panel.grid.major = element_line(color = "#E7ECF1"),
      plot.background = element_rect(fill = "white", color = NA),
      panel.background = element_rect(fill = "white", color = NA),
      legend.position = "bottom"
    )
}

t04_plotly <- function(plot, alt_text, tooltip = c("x", "y")) {
  plotly_height <- attr(plot, "t04_plotly_height", exact = TRUE)
  plotly_top_margin <- attr(plot, "t04_plotly_top_margin", exact = TRUE)
  if (is.null(plotly_top_margin)) plotly_top_margin <- 152
  legend_below <- isTRUE(attr(plot, "t04_legend_below", exact = TRUE))
  plotly_bottom_margin <- attr(plot, "t04_plotly_bottom_margin", exact = TRUE)
  if (is.null(plotly_bottom_margin)) plotly_bottom_margin <- 118
  plotly_legend_y <- attr(plot, "t04_plotly_legend_y", exact = TRUE)
  if (is.null(plotly_legend_y)) plotly_legend_y <- -0.18
  plotly_title_width <- attr(plot, "t04_plotly_title_width", exact = TRUE)
  if (is.null(plotly_title_width)) plotly_title_width <- 40L
  plot <- ratiomera_make_plotly_compatible(plot)
  plotly_widget <- ggplotly(
    plot,
    tooltip = tooltip,
    dynamicTicks = FALSE
  ) |>
    ratiomera_prepare_plotly_widget(
      title_width = plotly_title_width,
      axis_width = 28,
      annotation_width = 30
    )
  plotly_widget$x$data <- lapply(plotly_widget$x$data, function(trace) {
    if (!is.null(trace$name) && identical(trace$name, "fitted values")) {
      trace$name <- t04_labels$fitted_values
    }
    trace
  })
  plotly_widget <- ratiomera_localize_plotly_hover(
    plotly_widget,
    ratiomera_plotly_hover_labels(plot, topic_locale)
  )

  plotly_widget <- plotly_widget |>
    layout(
      autosize = TRUE,
      hovermode = "closest",
      # Two-line translated titles and facet strips need separate vertical
      # space. A larger shared top margin prevents them from colliding while
      # preserving identical chart geometry across all three languages.
      margin = list(l = 76, r = 28, b = 82, t = plotly_top_margin, pad = 2)
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

  if (!is.null(plotly_height)) {
    plotly_widget$height <- as.numeric(plotly_height)
    plotly_widget$sizingPolicy$defaultHeight <- as.numeric(plotly_height)
  }

  if (legend_below) {
    plotly_widget <- plotly_widget |>
      layout(
        margin = list(l = 76, r = 28, b = plotly_bottom_margin, t = plotly_top_margin, pad = 2),
        legend = list(
          orientation = "h",
          x = 0.5,
          xanchor = "center",
          y = plotly_legend_y,
          yanchor = "top"
        )
      )
  }

  plotly_widget
}

format_r <- function(value, digits = 3) {
  sprintf(paste0("%.", digits, "f"), value)
}

# A small hand-calculation example with values not taken from the worksheets.
worked_covariance <- tibble(
  case = 1:5,
  x = 1:5,
  y = c(2, 3, 1, 5, 4)
) |>
  mutate(
    x_deviation = x - mean(x),
    y_deviation = y - mean(y),
    product = x_deviation * y_deviation
  )

worked_covariance_table <- bind_rows(
  worked_covariance,
  tibble(
    case = NA_integer_,
    x = sum(worked_covariance$x),
    y = sum(worked_covariance$y),
    x_deviation = sum(worked_covariance$x_deviation),
    y_deviation = sum(worked_covariance$y_deviation),
    product = sum(worked_covariance$product)
  )
)
worked_covariance_value <- cov(worked_covariance$x, worked_covariance$y)
worked_correlation_value <- cor(worked_covariance$x, worked_covariance$y)

# Geometry of paired deviations for the same five-case worked example. Case 5
# is highlighted because both deviations are positive and easy to trace.
covariance_geometry_text <- if (topic_locale == "de") {
  list(
    positive = "Positives Kreuzprodukt",
    negative = "Negatives Kreuzprodukt",
    zero = "Kreuzprodukt null",
    case = "Fall",
    both_above = "Beide Werte über ihren Mittelwerten\nPositiver Beitrag",
    both_below = "Beide Werte unter ihren Mittelwerten\nPositiver Beitrag",
    x_below_y_above = "X unter, Y über dem eigenen Mittelwert\nNegativer Beitrag\n(kein berechneter Fall hier)",
    x_above_y_below = "X über, Y unter dem eigenen Mittelwert\nNegativer Beitrag\n(kein berechneter Fall hier)",
    contribution_heading = "Beiträge der Fälle",
    contribution = "Beitrag",
    sum = "Summe",
    worked_heading = "Fall 5, Schritt für Schritt",
    positive_result = "positiver Beitrag",
    title = "Wie jeder Fall zur Kovarianz beiträgt",
    subtitle = "Die Lage relativ zu beiden Mittelwerten bestimmt das Vorzeichen; die Abstände bestimmen den Betrag.",
    x_axis = "Variable X",
    y_axis = "Variable Y"
  )
} else if (topic_locale == "sq") {
  list(
    positive = "Prodhimi i kryqëzuar pozitiv",
    negative = "Prodhimi i kryqëzuar negativ",
    zero = "Prodhimi i kryqëzuar zero",
    case = "Rasti",
    both_above = "Të dyja vlerat mbi mesataret e tyre\nKontribut pozitiv",
    both_below = "Të dyja vlerat nën mesataret e tyre\nKontribut pozitiv",
    x_below_y_above = "X nën, Y mbi mesataren e vet\nKontribut negativ\n(asnjë rast i llogaritur këtu)",
    x_above_y_below = "X mbi, Y nën mesataren e vet\nKontribut negativ\n(asnjë rast i llogaritur këtu)",
    contribution_heading = "Kontributet e rasteve",
    contribution = "Kontributi",
    sum = "Shuma",
    worked_heading = "Rasti 5, hap pas hapi",
    positive_result = "kontribut pozitiv",
    title = "Si kontribuon çdo rast në kovariancë",
    subtitle = "Pozicioni ndaj të dyja mesatareve përcakton shenjën; largësitë përcaktojnë madhësinë.",
    x_axis = "Ndryshorja X",
    y_axis = "Ndryshorja Y"
  )
} else {
  list(
    positive = "Positive cross-product",
    negative = "Negative cross-product",
    zero = "Zero cross-product",
    case = "Case",
    both_above = "Both values above their means\nPositive contribution",
    both_below = "Both values below their means\nPositive contribution",
    x_below_y_above = "X below its mean, Y above its mean\nNegative contribution\n(no worked case here)",
    x_above_y_below = "X above its mean, Y below its mean\nNegative contribution\n(no worked case here)",
    contribution_heading = "Case contributions",
    contribution = "Contribution",
    sum = "Sum",
    worked_heading = "Case 5, step by step",
    positive_result = "positive contribution",
    title = "How Each Case Contributes to Covariance",
    subtitle = "Position relative to the two means determines the sign; distance from the means determines the size.",
    x_axis = "Variable X",
    y_axis = "Variable Y"
  )
}

covariance_geometry <- worked_covariance |>
  mutate(
    contribution = case_when(
      product > 0 ~ covariance_geometry_text$positive,
      product < 0 ~ covariance_geometry_text$negative,
      TRUE ~ covariance_geometry_text$zero
    ),
    point_label_y = if_else(case == 4, y + 0.10, y + 0.23)
  )

format_covariance_sign <- function(value) {
  ifelse(
    value > 0,
    paste0("+", value),
    ifelse(value < 0, paste0("−", abs(value)), "0")
  )
}

covariance_contribution_rows <- covariance_geometry |>
  transmute(
    case = as.character(case),
    x_deviation = format_covariance_sign(x_deviation),
    y_deviation = format_covariance_sign(y_deviation),
    product = format_covariance_sign(product)
  )

p_covariance_regions <- ggplot(covariance_geometry, aes(x, y)) +
  annotate("rect", xmin = 3, xmax = 5.55, ymin = 3, ymax = 5.55, fill = "#EAF4EF", alpha = 0.68) +
  annotate("rect", xmin = 0.45, xmax = 3, ymin = 0.45, ymax = 3, fill = "#EAF4EF", alpha = 0.68) +
  annotate("rect", xmin = 0.45, xmax = 3, ymin = 3, ymax = 5.55, fill = "#FFF0EA", alpha = 0.68) +
  annotate("rect", xmin = 3, xmax = 5.55, ymin = 0.45, ymax = 3, fill = "#FFF0EA", alpha = 0.68) +
  annotate("segment", x = 3, xend = 3, y = 0.45, yend = 5.55, color = "#657B8C", linetype = "dashed", linewidth = 0.8) +
  annotate("segment", x = 0.45, xend = 5.55, y = 3, yend = 3, color = "#657B8C", linetype = "dashed", linewidth = 0.8) +
  annotate(
    "segment",
    x = 3,
    xend = 5,
    y = 3,
    yend = 3,
    color = "#2F6F9F",
    linewidth = 1.2,
    arrow = grid::arrow(length = grid::unit(0.14, "cm"), type = "closed")
  ) +
  annotate(
    "segment",
    x = 5,
    xend = 5,
    y = 3,
    yend = 4,
    color = "#6A4C93",
    linewidth = 1.2,
    arrow = grid::arrow(length = grid::unit(0.14, "cm"), type = "closed")
  ) +
  annotate("text", x = 4, y = 2.79, label = "x₅ − x̄ = +2", color = "#204D70", fontface = "bold", size = 3.05) +
  annotate("text", x = 5.16, y = 3.5, label = "y₅ − ȳ = +1", color = "#5A3E7A", fontface = "bold", size = 3.0, angle = 90) +
  geom_point(aes(fill = contribution), shape = 21, color = "white", stroke = 1.0, size = 7.2) +
  geom_point(
    data = covariance_geometry |> filter(case == 5),
    shape = 21,
    fill = NA,
    color = "#173F5F",
    stroke = 1.1,
    size = 9.1,
    inherit.aes = FALSE,
    aes(x, y)
  ) +
  geom_text(aes(label = case), color = "white", fontface = "bold", size = 3.45) +
  annotate("label", x = 1.65, y = 4.86, label = covariance_geometry_text$x_below_y_above, color = "#8A3F36", fill = "white", size = 2.45, lineheight = 0.96, linewidth = 0.2) +
  annotate("label", x = 4.38, y = 5.20, label = covariance_geometry_text$both_above, color = "#276449", fill = "white", size = 2.55, lineheight = 0.96, linewidth = 0.2) +
  annotate("label", x = 1.62, y = 0.80, label = covariance_geometry_text$both_below, color = "#276449", fill = "white", size = 2.55, lineheight = 0.96, linewidth = 0.2) +
  annotate("label", x = 4.20, y = 0.83, label = covariance_geometry_text$x_above_y_below, color = "#8A3F36", fill = "white", size = 2.42, lineheight = 0.96, linewidth = 0.2) +
  annotate("label", x = 3.04, y = 5.73, label = "x̄ = 3", hjust = 0, fill = "white", color = "#536475", fontface = "bold", size = 3.0, linewidth = 0) +
  annotate("label", x = 0.43, y = 3.05, label = "ȳ = 3", hjust = 0, vjust = 0, fill = "white", color = "#536475", fontface = "bold", size = 3.0, linewidth = 0) +
  scale_fill_manual(
    values = c(
      setNames(
        c("#3F8B6D", "#C05A47", "#718494"),
        c(covariance_geometry_text$positive, covariance_geometry_text$negative, covariance_geometry_text$zero)
      )
    ),
    guide = "none"
  ) +
  scale_x_continuous(breaks = 1:5) +
  scale_y_continuous(breaks = 1:5) +
  coord_cartesian(xlim = c(0.40, 5.62), ylim = c(0.40, 5.92), clip = "off") +
  labs(
    x = covariance_geometry_text$x_axis,
    y = covariance_geometry_text$y_axis
  ) +
  t04_theme(base_size = 10.5) +
  theme(
    panel.grid.minor = element_blank(),
    panel.grid.major = element_blank(),
    legend.position = "none",
    plot.margin = margin(8, 14, 8, 12)
  )

covariance_table_y <- c(6.2, 5.3, 4.4, 3.5, 2.6)
covariance_table_headers <- c(
  covariance_geometry_text$case,
  "xᵢ − x̄",
  "yᵢ − ȳ",
  covariance_geometry_text$contribution
)

p_covariance_calculation <- ggplot() +
  annotate("rect", xmin = 0.25, xmax = 4.75, ymin = 1.98, ymax = 6.72, fill = "#F7F9FB", color = "#D7E0E7", linewidth = 0.55) +
  annotate("rect", xmin = 0.25, xmax = 4.75, ymin = 2.15, ymax = 3.00, fill = "#EAF4EF", color = NA) +
  annotate("text", x = 0.3, y = 7.35, label = covariance_geometry_text$contribution_heading, hjust = 0, color = "#203A4F", fontface = "bold", size = 4.2) +
  annotate("text", x = c(0.65, 1.70, 2.83, 4.05), y = 6.95, label = covariance_table_headers, color = "#34495E", fontface = "bold", size = 3.0) +
  annotate("segment", x = 0.35, xend = 4.65, y = 6.66, yend = 6.66, color = "#AAB9C5", linewidth = 0.5) +
  geom_text(
    data = covariance_contribution_rows,
    aes(x = 0.65, y = covariance_table_y, label = case),
    color = "#203A4F",
    fontface = ifelse(covariance_contribution_rows$case == "5", "bold", "plain"),
    size = 3.15
  ) +
  geom_text(data = covariance_contribution_rows, aes(x = 1.70, y = covariance_table_y, label = x_deviation), color = "#204D70", size = 3.15) +
  geom_text(data = covariance_contribution_rows, aes(x = 2.83, y = covariance_table_y, label = y_deviation), color = "#5A3E7A", size = 3.15) +
  geom_text(
    data = covariance_contribution_rows,
    aes(x = 4.05, y = covariance_table_y, label = product),
    color = ifelse(covariance_contribution_rows$product == "0", "#657B8C", "#276449"),
    fontface = ifelse(covariance_contribution_rows$case == "5", "bold", "plain"),
    size = 3.15
  ) +
  annotate("segment", x = 0.35, xend = 4.65, y = 2.05, yend = 2.05, color = "#AAB9C5", linewidth = 0.5) +
  annotate("text", x = 0.65, y = 1.64, label = covariance_geometry_text$sum, color = "#203A4F", fontface = "bold", size = 3.15) +
  annotate("text", x = 1.70, y = 1.64, label = "0", color = "#204D70", fontface = "bold", size = 3.15) +
  annotate("text", x = 2.83, y = 1.64, label = "0", color = "#5A3E7A", fontface = "bold", size = 3.15) +
  annotate("text", x = 4.05, y = 1.64, label = "+6", color = "#276449", fontface = "bold", size = 3.15) +
  annotate("label", x = 2.5, y = 0.62, label = paste0(
    covariance_geometry_text$worked_heading,
    "\nx₅ − x̄ = 5 − 3 = +2",
    "\ny₅ − ȳ = 4 − 3 = +1",
    "\n(+2)(+1) = +2  →  ", covariance_geometry_text$positive_result
  ), fill = "#F3FAF6", color = "#276449", fontface = "bold", size = 3.0, lineheight = 1.08, linewidth = 0.35, label.padding = grid::unit(0.24, "lines")) +
  coord_cartesian(xlim = c(0, 5), ylim = c(0, 7.7), clip = "off") +
  theme_void() +
  theme(plot.margin = margin(8, 8, 8, 8))

covariance_geometry_body <- cowplot::plot_grid(
  p_covariance_regions,
  p_covariance_calculation,
  nrow = 1,
  rel_widths = c(1.22, 1)
)

p_covariance_geometry <- cowplot::ggdraw() +
  cowplot::draw_label(
    covariance_geometry_text$title,
    x = 0.02,
    y = 0.985,
    hjust = 0,
    vjust = 1,
    fontface = "bold",
    color = "#172B3A",
    size = 15
  ) +
  cowplot::draw_label(
    covariance_geometry_text$subtitle,
    x = 0.02,
    y = 0.935,
    hjust = 0,
    vjust = 1,
    color = "#536475",
    size = 10.5
  ) +
  cowplot::draw_plot(covariance_geometry_body, x = 0, y = 0, width = 1, height = 0.89)

# Three point clouds that isolate the sign of a linear association.
set.seed(4401)
direction_x <- seq(1, 10, length.out = 36)
direction_data <- bind_rows(
  tibble(x = direction_x, y = direction_x + rnorm(36, 0, 1), pattern = t04_labels$positive),
  tibble(x = direction_x, y = 11 - direction_x + rnorm(36, 0, 1), pattern = t04_labels$negative),
  tibble(x = direction_x, y = rnorm(36, 5, 2), pattern = t04_labels$little)
) |>
  group_by(pattern) |>
  mutate(
    r_value = cor(x, y),
    panel = paste0(pattern, "\n", t04_labels$pearson_prefix, format_r(first(r_value), 2))
  ) |>
  ungroup()

direction_levels <- direction_data |>
  distinct(pattern, panel) |>
  arrange(match(pattern, c(
    t04_labels$positive,
    t04_labels$negative,
    t04_labels$little
  ))) |>
  pull(panel)
direction_data <- direction_data |>
  mutate(panel = factor(panel, levels = direction_levels))

p_direction_grid <- ggplot(direction_data, aes(x, y)) +
  geom_point(color = "#2F6F9F", alpha = 0.78, size = 2) +
  facet_wrap(
    vars(panel),
    nrow = 1,
    axes = "all_y",
    axis.labels = "all_y"
  ) +
  labs(
    title = t04_labels$direction_title,
    subtitle = t04_labels$direction_subtitle,
    x = t04_labels$variable_x,
    y = t04_labels$variable_y
  ) +
  t04_theme(base_size = 11) +
  theme(
    panel.spacing.x = grid::unit(1.35, "lines"),
    panel.border = element_rect(color = "#CBD6DF", fill = NA, linewidth = 0.7),
    strip.background = element_rect(fill = "#F4F7F9", color = "#CBD6DF", linewidth = 0.7),
    strip.text = element_text(margin = margin(5, 5, 5, 5))
  )

# Nonlinear examples distinguish linear association from monotonic association.
set.seed(4402)
monotonic_x <- seq(0, 3, length.out = 45)
monotonic_y <- exp(monotonic_x) + rnorm(45, 0, 0.25)
u_x <- seq(-3, 3, length.out = 61)
u_y <- u_x^2 + rnorm(61, 0, 0.35)

shape_check_data <- bind_rows(
  tibble(x = monotonic_x, y = monotonic_y, pattern = t04_labels$curved_monotonic),
  tibble(x = u_x, y = u_y, pattern = t04_labels$u_nonmonotonic)
) |>
  group_by(pattern) |>
  mutate(
    pearson = cor(x, y),
    spearman = cor(x, y, method = "spearman"),
    panel = paste0(
      pattern,
      "\n", t04_labels$pearson_prefix, format_r(first(pearson), 2),
      "; Spearman rₛ = ", format_r(first(spearman), 2)
    )
  ) |>
  ungroup()

shape_levels <- shape_check_data |>
  distinct(pattern, panel) |>
  arrange(match(pattern, c(t04_labels$curved_monotonic, t04_labels$u_nonmonotonic))) |>
  pull(panel)
shape_check_data <- shape_check_data |>
  mutate(panel = factor(panel, levels = shape_levels))

p_shape_checks <- ggplot(shape_check_data, aes(x, y)) +
  geom_point(color = "#2F6F9F", alpha = 0.75, size = 1.9) +
  facet_wrap(vars(panel), nrow = 1, scales = "free") +
  labs(
    title = t04_labels$shape_title,
    subtitle = t04_labels$shape_subtitle,
    x = t04_labels$variable_x,
    y = t04_labels$variable_y
  ) +
  t04_theme(base_size = 11)

# Deterministic Ratiomera teaching cohort for the simulated example.
set.seed(4404)
sim_n <- 120
sim_data <- tibble(
  participant_id = sprintf("S%03d", 1:sim_n),
  prior_preparation = round(pmin(pmax(rnorm(sim_n, 50, 10), 20), 80), 1)
) |>
  mutate(
    study_hours = round(
      pmin(pmax(2 + 0.08 * prior_preparation + rnorm(sim_n, 0, 1.8), 0), 15),
      1
    ),
    exam_score = round(
      pmin(
        pmax(30 + 2.8 * study_hours + 0.35 * prior_preparation + rnorm(sim_n, 0, 7), 0),
        100
      ),
      1
    ),
    hover_text = paste0(
      t04_labels$participant,
      ": ",
      participant_id,
      "<br>",
      t04_labels$prior_preparation_axis,
      ": ",
      format_r(prior_preparation, 1),
      "<br>",
      t04_labels$study_hours_axis,
      ": ",
      format_r(study_hours, 1),
      "<br>",
      t04_labels$exam_score_axis,
      ": ",
      format_r(exam_score, 1)
    )
  )

sim_covariance <- cov(sim_data$study_hours, sim_data$exam_score)
sim_pearson <- cor(sim_data$study_hours, sim_data$exam_score)
sim_spearman <- cor(sim_data$study_hours, sim_data$exam_score, method = "spearman")
sim_z_covariance <- cov(
  as.numeric(scale(sim_data$study_hours)),
  as.numeric(scale(sim_data$exam_score))
)
sim_t <- sim_pearson * sqrt((sim_n - 2) / (1 - sim_pearson^2))
sim_df <- sim_n - 2
sim_p <- 2 * pt(-abs(sim_t), df = sim_df)

sim_display <- sim_data |>
  slice_head(n = 12) |>
  select(participant_id, prior_preparation, study_hours, exam_score)

sim_summary_table <- tibble(
  quantity = c(
    t04_labels$paired_cases,
    t04_labels$mean_hours,
    t04_labels$sd_hours,
    t04_labels$mean_score,
    t04_labels$sd_score,
    t04_labels$sample_covariance,
    t04_labels$pearson_correlation,
    t04_labels$spearman_correlation
  ),
  value = c(
    as.character(sim_n),
    format_r(mean(sim_data$study_hours), 2),
    format_r(sd(sim_data$study_hours), 2),
    format_r(mean(sim_data$exam_score), 2),
    format_r(sd(sim_data$exam_score), 2),
    format_r(sim_covariance, 3),
    format_r(sim_pearson, 3),
    format_r(sim_spearman, 3)
  )
)

sim_centered_table <- sim_data |>
  transmute(
    participant_id,
    study_hours,
    exam_score,
    study_deviation = study_hours - mean(study_hours),
    score_deviation = exam_score - mean(exam_score),
    cross_product = study_deviation * score_deviation
  ) |>
  slice_head(n = 8) |>
  mutate(across(where(is.numeric), ~ round(.x, 2)))

unit_comparison_table <- tibble(
  units = c(t04_labels$hours_points, t04_labels$minutes_points),
  covariance = c(
    sim_covariance,
    cov(60 * sim_data$study_hours, sim_data$exam_score)
  ),
  pearson_r = c(
    sim_pearson,
    cor(60 * sim_data$study_hours, sim_data$exam_score)
  )
) |>
  mutate(
    covariance = round(covariance, 3),
    pearson_r = round(pearson_r, 3)
  )

p_sim_scatter <- ggplot(sim_data, aes(study_hours, exam_score)) +
  suppressWarnings(geom_point(aes(text = hover_text), color = "#2F6F9F", alpha = 0.78, size = 2.2)) +
  geom_smooth(method = "lm", formula = y ~ x, se = FALSE, color = "#C05A47", linewidth = 0.9) +
  labs(
    title = t04_labels$scatter_title,
    subtitle = paste0(t04_labels$scatter_subtitle, format_r(sim_pearson, 2)),
    x = t04_labels$study_hours_axis,
    y = t04_labels$exam_score_axis
  ) +
  t04_theme()

standardized_data <- bind_rows(
  sim_data |>
    transmute(
      x = study_hours,
      y = exam_score,
      panel = paste0(t04_labels$original_units, "\n", t04_labels$pearson_prefix, format_r(sim_pearson, 3))
    ),
  sim_data |>
    transmute(
      x = as.numeric(scale(study_hours)),
      y = as.numeric(scale(exam_score)),
      panel = paste0(t04_labels$standardized_units, "\n", t04_labels$pearson_prefix, format_r(sim_z_covariance, 3))
    )
) |>
  mutate(
    panel = factor(
      panel,
      levels = c(
        paste0(t04_labels$original_units, "\n", t04_labels$pearson_prefix, format_r(sim_pearson, 3)),
        paste0(t04_labels$standardized_units, "\n", t04_labels$pearson_prefix, format_r(sim_z_covariance, 3))
      )
    )
  )

p_standardization <- ggplot(standardized_data, aes(x, y)) +
  geom_point(color = "#2F6F9F", alpha = 0.72, size = 1.8) +
  facet_wrap(vars(panel), nrow = 1, scales = "free") +
  scale_x_continuous(expand = expansion(mult = c(0.05, 0.12))) +
  labs(
    title = t04_labels$standardization_title,
    subtitle = t04_labels$standardization_subtitle,
    x = t04_labels$study_value,
    y = t04_labels$score_value
  ) +
  t04_theme(base_size = 11)

# Add one deliberately influential point to show sensitivity without altering
# the teaching cohort used for any other calculation.
outlier_data <- bind_rows(
  sim_data |>
    transmute(
      participant_id,
      prior_preparation,
      study_hours,
      exam_score,
      point_type = t04_labels$original_case,
      version = t04_labels$original_cohort
    ),
  sim_data |>
    transmute(
      participant_id,
      prior_preparation,
      study_hours,
      exam_score,
      point_type = t04_labels$original_case,
      version = t04_labels$point_added
    ),
  tibble(
    participant_id = t04_labels$added_point,
    prior_preparation = NA_real_,
    study_hours = 14,
    exam_score = 25,
    point_type = t04_labels$added_point,
    version = t04_labels$point_added
  )
) |>
  group_by(version) |>
  mutate(
    r_value = cor(study_hours, exam_score),
    panel = paste0(version, "\n", t04_labels$pearson_prefix, format_r(first(r_value), 2)),
    hover_text = paste0(
      t04_labels$participant,
      ": ",
      participant_id,
      if_else(
        is.na(prior_preparation),
        "",
        paste0("<br>", t04_labels$prior_preparation_axis, ": ", format_r(prior_preparation, 1))
      ),
      "<br>",
      t04_labels$study_hours_axis,
      ": ",
      format_r(study_hours, 1),
      "<br>",
      t04_labels$exam_score_axis,
      ": ",
      format_r(exam_score, 1)
    )
  ) |>
  ungroup()

outlier_levels <- outlier_data |>
  distinct(version, panel) |>
  arrange(match(version, c(t04_labels$original_cohort, t04_labels$point_added))) |>
  pull(panel)
outlier_data <- outlier_data |>
  mutate(panel = factor(panel, levels = outlier_levels))

p_outlier_comparison <- ggplot(outlier_data, aes(study_hours, exam_score, color = point_type)) +
  suppressWarnings(geom_point(aes(text = hover_text), alpha = 0.78, size = 2)) +
  facet_wrap(vars(panel), ncol = 1) +
  scale_color_manual(values = setNames(c("#2F6F9F", "#C05A47"), c(t04_labels$original_case, t04_labels$added_point))) +
  labs(
    title = t04_labels$outlier_title,
    subtitle = t04_labels$outlier_subtitle,
    x = t04_labels$study_hours_axis,
    y = t04_labels$exam_score_axis,
    color = NULL
  ) +
  t04_theme(base_size = 11)

attr(p_outlier_comparison, "t04_plotly_height") <- 740
attr(p_outlier_comparison, "t04_legend_below") <- TRUE
attr(p_outlier_comparison, "t04_plotly_title_width") <- 30L
attr(p_outlier_comparison, "t04_plotly_bottom_margin") <- 158
attr(p_outlier_comparison, "t04_plotly_legend_y") <- -0.24

restricted_data <- sim_data |>
  filter(study_hours >= 5, study_hours <= 8)
restricted_r <- cor(restricted_data$study_hours, restricted_data$exam_score)

range_data <- bind_rows(
  sim_data |>
    transmute(
      participant_id,
      prior_preparation,
      study_hours,
      exam_score,
      panel = paste0(t04_labels$full_range, " (n = ", n(), ")\nr = ", format_r(sim_pearson, 2))
    ),
  restricted_data |>
    transmute(
      participant_id,
      prior_preparation,
      study_hours,
      exam_score,
      panel = paste0(t04_labels$restricted_range, " (n = ", n(), ")\nr = ", format_r(restricted_r, 2))
    )
)
range_levels <- range_data |>
  distinct(panel) |>
  pull(panel)
range_data <- range_data |>
  mutate(
    panel = factor(panel, levels = range_levels),
    hover_text = paste0(
      t04_labels$participant,
      ": ",
      participant_id,
      "<br>",
      t04_labels$prior_preparation_axis,
      ": ",
      format_r(prior_preparation, 1),
      "<br>",
      t04_labels$study_hours_axis,
      ": ",
      format_r(study_hours, 1),
      "<br>",
      t04_labels$exam_score_axis,
      ": ",
      format_r(exam_score, 1)
    )
  )

p_range_restriction <- ggplot(range_data, aes(study_hours, exam_score)) +
  suppressWarnings(geom_point(aes(text = hover_text), color = "#2F6F9F", alpha = 0.75, size = 1.9)) +
  facet_wrap(vars(panel), ncol = 1) +
  coord_cartesian(xlim = c(0, 15), ylim = c(20, 90)) +
  labs(
    title = t04_labels$range_title,
    subtitle = t04_labels$range_subtitle,
    x = t04_labels$study_hours_axis,
    y = t04_labels$exam_score_axis
  ) +
  t04_theme(base_size = 11)

attr(p_range_restriction, "t04_plotly_height") <- 780
attr(p_range_restriction, "t04_plotly_top_margin") <- 210
attr(p_range_restriction, "t04_plotly_title_width") <- 32L

# The known simulation recipe supplies a concrete third-variable example. The
# same cases appear in both panels so hover labels can be matched by ID.
third_variable_panels <- c(t04_labels$third_study_panel, t04_labels$third_score_panel)
sim_third_variable <- bind_rows(
  sim_data |>
    transmute(
      participant_id,
      prior_preparation,
      value = study_hours,
      panel = t04_labels$third_study_panel,
      hover_text
    ),
  sim_data |>
    transmute(
      participant_id,
      prior_preparation,
      value = exam_score,
      panel = t04_labels$third_score_panel,
      hover_text
    )
) |>
  mutate(panel = factor(panel, levels = third_variable_panels))

p_sim_third_variable <- ggplot(
  sim_third_variable,
  aes(prior_preparation, value)
) +
  suppressWarnings(geom_point(aes(text = hover_text), color = "#2F6F9F", alpha = 0.72, size = 1.9)) +
  geom_smooth(
    method = "lm",
    formula = y ~ x,
    se = FALSE,
    color = "#C05A47",
    linewidth = 0.85
  ) +
  facet_wrap(vars(panel), ncol = 1, scales = "free_y") +
  labs(
    title = t04_labels$third_variable_title,
    subtitle = t04_labels$third_variable_subtitle,
    x = t04_labels$prior_preparation_axis,
    y = t04_labels$panel_value
  ) +
  t04_theme(base_size = 11) +
  theme(legend.position = "none")

attr(p_sim_third_variable, "t04_plotly_height") <- 700

# Three causal structures that can all be compatible with an observed X-Y
# association. This is a conceptual diagram, not an empirical claim.
causal_nodes <- bind_rows(
  tibble(panel = t04_labels$x_affects_y, x = c(0.2, 0.8), y = 0.5, label = c(t04_labels$study_node, t04_labels$score_node)),
  tibble(panel = t04_labels$y_affects_x, x = c(0.2, 0.8), y = 0.5, label = c(t04_labels$study_node, t04_labels$score_node)),
  tibble(
    panel = t04_labels$third_affects_both,
    x = c(0.2, 0.8, 0.5),
    y = c(0.25, 0.25, 0.78),
    label = c(t04_labels$study_node, t04_labels$score_node, t04_labels$preparation_node)
  )
)
causal_edges <- bind_rows(
  tibble(panel = t04_labels$x_affects_y, x = 0.31, y = 0.5, xend = 0.69, yend = 0.5),
  tibble(panel = t04_labels$y_affects_x, x = 0.69, y = 0.5, xend = 0.31, yend = 0.5),
  tibble(
    panel = t04_labels$third_affects_both,
    x = c(0.45, 0.55),
    y = c(0.70, 0.70),
    xend = c(0.27, 0.73),
    yend = c(0.35, 0.35)
  )
)
causal_panel_levels <- c(t04_labels$x_affects_y, t04_labels$y_affects_x, t04_labels$third_affects_both)
causal_nodes <- causal_nodes |>
  mutate(panel = factor(panel, levels = causal_panel_levels))
causal_edges <- causal_edges |>
  mutate(panel = factor(panel, levels = causal_panel_levels))

p_causal_alternatives <- ggplot() +
  geom_segment(
    data = causal_edges,
    aes(x, y, xend = xend, yend = yend),
    color = "#527C99",
    linewidth = 1,
    arrow = grid::arrow(length = grid::unit(0.17, "cm"))
  ) +
  geom_label(
    data = causal_nodes,
    aes(x, y, label = label),
    fill = "#F5F8FA",
    color = "#203A4F",
    linewidth = 0.35,
    lineheight = 1.0,
    size = 3.2
  ) +
  facet_wrap(vars(panel), nrow = 1) +
  coord_cartesian(xlim = c(0, 1), ylim = c(0.05, 0.95), clip = "off") +
  labs(
    title = t04_labels$causal_title,
    subtitle = t04_labels$causal_subtitle
  ) +
  theme_void(base_size = 11) +
  theme(
    plot.title = element_text(face = "bold", color = "#172B3A"),
    plot.subtitle = element_text(color = "#536475"),
    strip.text = element_text(face = "bold", color = "#203A4F"),
    panel.spacing = grid::unit(1.2, "lines"),
    plot.background = element_rect(fill = "white", color = NA),
    panel.background = element_rect(fill = "white", color = NA),
    plot.margin = margin(12, 20, 12, 20)
  )
