# Shared deterministic data, calculations, tables, and figures for Topic 6.

if (!exists("topic_locale", inherits = FALSE)) {
  topic_locale <- "en"
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

t06_text_sets <- list(
  en = list(
    third_z = "Third variable Z",
    variable_x = "Variable X",
    variable_y = "Variable Y",
    observed_xy = "Observed X-Y association",
    police_population_bands = c("Smaller cities", "Medium cities", "Larger cities"),
    police_population_title = "Population Can Reverse the Story Told by Raw Counts",
    police_population_subtitle = "Constructed counts show a positive overall pattern and negative within-population patterns",
    police_axis = "Constructed police count",
    offense_axis = "Constructed recorded-offense count",
    population_band = "Population band",
    hover_participant = "Participant",
    hover_fitted = "Fitted value",
    hover_residual = "Residual",
    third_title = "A Third Variable Can Contribute to a Bivariate Association",
    third_subtitle = "The arrows are one possible explanation to investigate, not a causal conclusion",
    scenario_shared = "Z contributes shared movement",
    scenario_opposing = "Z contributes opposing movement",
    bivariate_r = "Bivariate r",
    partial_r = "Partial r",
    adjustment_title = "Adjustment Does Not Always Make a Correlation Smaller",
    adjustment_subtitle = "Two constructed patterns show the two directions of change supported by the formula",
    correlation_coefficient = "Correlation coefficient",
    summary_quantities = c(
      "Number of paired cases",
      "Mean baseline-preparation score",
      "Mean weekly practice hours",
      "Mean assessment score",
      "SD of baseline-preparation score",
      "SD of weekly practice hours",
      "SD of assessment score"
    ),
    pair_labels = c(
      "Practice hours and assessment score",
      "Practice hours and baseline preparation",
      "Assessment score and baseline preparation"
    ),
    method_labels = c(
      "Correlation of the two residuals",
      "Formula from the three bivariate correlations"
    ),
    residual_panels = c(
      "Practice hours adjusted for baseline preparation",
      "Assessment score adjusted for baseline preparation"
    ),
    residual_title = "Residualization Separates Observed and Fitted Values",
    residual_subtitle = "Orange segments show four residuals in each regression",
    baseline_axis = "Baseline-preparation score",
    baseline_hover = "Baseline preparation",
    observed_axis = "Observed value",
    raw_panel_prefix = "Raw standardized values\nBivariate r = ",
    adjusted_panel_prefix = "Standardized residuals\nPartial r = ",
    raw_adjusted_title = "Raw Association and Association After Linear Adjustment",
    raw_adjusted_subtitle = "Standardization aligns the axes but does not change either correlation",
    practice_sd_axis = "Practice measure (standard-deviation units)",
    assessment_sd_axis = "Assessment measure (standard-deviation units)",
    practice_sd_hover = "Standardized practice",
    assessment_sd_hover = "Standardized assessment"
  ),
  de = list(
    third_z = "Drittvariable Z",
    variable_x = "Variable X",
    variable_y = "Variable Y",
    observed_xy = "Beobachteter X-Y-Zusammenhang",
    police_population_bands = c("Kleinere Städte", "Mittelgrosse Städte", "Grössere Städte"),
    police_population_title = "Die Bevölkerungszahl kann die Aussage roher Häufigkeiten umkehren",
    police_population_subtitle = "Konstruierte Häufigkeiten zeigen insgesamt ein positives und innerhalb der Bevölkerungsgruppen negative Muster",
    police_axis = "Konstruierte Anzahl Polizeikräfte",
    offense_axis = "Konstruierte Anzahl registrierter Delikte",
    population_band = "Bevölkerungsgruppe",
    hover_participant = "Teilnehmenden-ID",
    hover_fitted = "Angepasster Wert",
    hover_residual = "Residuum",
    third_title = "Eine Drittvariable kann zu einem bivariaten Zusammenhang beitragen",
    third_subtitle = "Die Pfeile zeigen eine zu prüfende Erklärungsmöglichkeit, keine kausale Schlussfolgerung",
    scenario_shared = "Z trägt zu gemeinsamer Bewegung bei",
    scenario_opposing = "Z trägt zu gegenläufiger Bewegung bei",
    bivariate_r = "Bivariates r",
    partial_r = "Partielles r",
    adjustment_title = "Eine Bereinigung macht eine Korrelation nicht immer kleiner",
    adjustment_subtitle = "Zwei konstruierte Muster zeigen beide von der Formel gestützten Änderungsrichtungen",
    correlation_coefficient = "Korrelationskoeffizient",
    summary_quantities = c(
      "Anzahl gepaarter Fälle",
      "Mittelwert des Ausgangsvorbereitungswerts",
      "Mittlere wöchentliche Übungsstunden",
      "Mittlerer Beurteilungspunktwert",
      "SD des Ausgangsvorbereitungswerts",
      "SD der wöchentlichen Übungsstunden",
      "SD des Beurteilungspunktwerts"
    ),
    pair_labels = c(
      "Übungsstunden und Beurteilungspunktwert",
      "Übungsstunden und Ausgangsvorbereitung",
      "Beurteilungspunktwert und Ausgangsvorbereitung"
    ),
    method_labels = c(
      "Korrelation der beiden Residuen",
      "Formel aus den drei bivariaten Korrelationen"
    ),
    residual_panels = c(
      "Übungsstunden, bereinigt um Ausgangsvorbereitung",
      "Beurteilungspunktwert, bereinigt um Ausgangsvorbereitung"
    ),
    residual_title = "Residualisierung trennt beobachtete und angepasste Werte",
    residual_subtitle = "Orange Segmente zeigen in jeder Regression vier Residuen",
    baseline_axis = "Ausgangsvorbereitung",
    baseline_hover = "Ausgangsvorbereitung",
    observed_axis = "Beobachteter Wert",
    raw_panel_prefix = "Rohe standardisierte Werte\nBivariates r = ",
    adjusted_panel_prefix = "Standardisierte Residuen\nPartielles r = ",
    raw_adjusted_title = "Roher Zusammenhang und Zusammenhang nach linearer Bereinigung",
    raw_adjusted_subtitle = "Die Standardisierung gleicht die Achsen an, verändert aber keine der beiden Korrelationen",
    practice_sd_axis = "Übungsmass (in Standardabweichungseinheiten)",
    assessment_sd_axis = "Beurteilungsmass (in Standardabweichungseinheiten)",
    practice_sd_hover = "Standardisierte Übung",
    assessment_sd_hover = "Standardisierte Beurteilung"
  ),
  sq = list(
    third_z = "Ndryshorja e tretë Z",
    variable_x = "Ndryshorja X",
    variable_y = "Ndryshorja Y",
    observed_xy = "Lidhja e vrojtuar X-Y",
    police_population_bands = c("Qytete më të vogla", "Qytete mesatare", "Qytete më të mëdha"),
    police_population_title = "Madhësia e popullsisë mund ta përmbysë rrëfimin e numërimeve të papërshtatura",
    police_population_subtitle = "Numërimet e krijuara tregojnë një model të përgjithshëm pozitiv, por modele negative brenda grupeve të popullsisë",
    police_axis = "Numri i krijuar i punonjësve të policisë",
    offense_axis = "Numri i krijuar i veprave penale të regjistruara",
    population_band = "Grupi i popullsisë",
    hover_participant = "Pjesëmarrësi",
    hover_fitted = "Vlera e përshtatur",
    hover_residual = "Reziduali",
    third_title = "Një ndryshore e tretë mund të kontribuojë në një lidhje bivariate",
    third_subtitle = "Shigjetat tregojnë një shpjegim të mundshëm për t'u shqyrtuar, jo një përfundim shkakësor",
    scenario_shared = "Z kontribuon në lëvizjen e përbashkët",
    scenario_opposing = "Z kontribuon në lëvizjen në drejtime të kundërta",
    bivariate_r = "r me dy ndryshore",
    partial_r = "r e pjesshme",
    adjustment_title = "Përshtatja nuk e zvogëlon gjithmonë një korrelacion",
    adjustment_subtitle = "Dy modele të krijuara tregojnë të dyja drejtimet e ndryshimit që mbështet formula",
    correlation_coefficient = "Koeficienti i korrelacionit",
    summary_quantities = c(
      "Numri i rasteve të çiftuara",
      "Mesatarja e pikëve të përgatitjes fillestare",
      "Mesatarja e orëve javore të ushtrimit",
      "Mesatarja e pikëve të vlerësimit",
      "SD e pikëve të përgatitjes fillestare",
      "SD e orëve javore të ushtrimit",
      "SD e pikëve të vlerësimit"
    ),
    pair_labels = c(
      "Orët e ushtrimit dhe pikët e vlerësimit",
      "Orët e ushtrimit dhe përgatitja fillestare",
      "Pikët e vlerësimit dhe përgatitja fillestare"
    ),
    method_labels = c(
      "Korrelacioni i dy serive të rezidualeve",
      "Formula nga tri korrelacionet bivariate"
    ),
    residual_panels = c(
      "Orët e ushtrimit të përshtatura për përgatitjen fillestare",
      "Pikët e vlerësimit të përshtatura për përgatitjen fillestare"
    ),
    residual_title = "Rezidualizimi ndan vlerat e vrojtuara nga vlerat e përshtatura",
    residual_subtitle = "Segmentet portokalli tregojnë katër reziduale në secilin regresion",
    baseline_axis = "Pikët e përgatitjes fillestare",
    baseline_hover = "Përgatitja fillestare",
    observed_axis = "Vlera e vrojtuar",
    raw_panel_prefix = "Vlerat e papërshtatura të standardizuara\nr me dy ndryshore = ",
    adjusted_panel_prefix = "Rezidualet e standardizuara\nr e pjesshme = ",
    raw_adjusted_title = "Lidhja e papërshtatur dhe lidhja pas përshtatjes lineare",
    raw_adjusted_subtitle = "Standardizimi i barazon boshtet, por nuk ndryshon asnjërin korrelacion",
    practice_sd_axis = "Matja e ushtrimit (në njësi të devijimit standard)",
    assessment_sd_axis = "Matja e vlerësimit (në njësi të devijimit standard)",
    practice_sd_hover = "Ushtrimi i standardizuar",
    assessment_sd_hover = "Vlerësimi i standardizuar"
  )
)

if (!topic_locale %in% names(t06_text_sets)) {
  stop("Unsupported Topic 6 locale: ", topic_locale, call. = FALSE)
}
t06_text <- t06_text_sets[[topic_locale]]

required_packages <- c(
  "dplyr", "tibble", "tidyr", "ggplot2", "DT", "plotly", "htmlwidgets", "knitr"
)
missing_packages <- required_packages[
  !vapply(required_packages, requireNamespace, logical(1), quietly = TRUE)
]
if (length(missing_packages)) {
  stop(
    "Topic 6 requires these R packages: ",
    paste(missing_packages, collapse = ", "),
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

t06_theme <- function(base_size = 12) {
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

topic6_plotly <- function(
  plot,
  alt_text,
  tooltip_fields = c("x", "y"),
  top_margin = 48
) {
  widget_height <- attr(plot, "ratiomera_widget_height", exact = TRUE)
  plot_top_margin <- attr(plot, "ratiomera_top_margin", exact = TRUE)
  if (!is.null(plot_top_margin)) top_margin <- max(top_margin, plot_top_margin)
  plot <- ratiomera_make_plotly_compatible(plot)
  plotly_widget <- ggplotly(
    plot,
    tooltip = tooltip_fields,
    dynamicTicks = TRUE,
    height = widget_height
  ) |>
    ratiomera_prepare_plotly_widget(
      title_width = 36,
      axis_width = 28,
      annotation_width = 30,
      title_size = 14
    )

  # The htmlwidget container is the single owner of rendered height. Quarto
  # can size that container responsively, while a second fixed Plotly layout
  # height would let the SVG extend beneath the figure caption at narrower
  # viewports. Retain the widget's requested height as its intrinsic size, but
  # let Plotly autosize its internal layout to the actual container.
  plotly_widget$x$layout$height <- NULL

  plotly_widget$x$data <- lapply(plotly_widget$x$data, function(trace) {
    if (!is.null(trace$name) && identical(trace$name, "fitted values")) {
      trace$name <- t06_text$hover_fitted
    }
    trace
  })
  plotly_widget <- ratiomera_localize_plotly_hover(
    plotly_widget,
    ratiomera_plotly_hover_labels(plot, topic_locale)
  )

  plotly_widget |>
    layout(
      autosize = TRUE,
      hovermode = "closest",
      hoverlabel = list(
        bgcolor = "white",
        bordercolor = "#AAB6C0",
        font = list(color = "#172B3A")
      ),
      margin = list(l = 82, r = 32, b = 82, t = max(top_margin, 82), pad = 2)
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
}

format_t06 <- function(value, digits = 3) {
  sprintf(paste0("%.", digits, "f"), value)
}

partial_from_three <- function(r_xy, r_xz, r_yz) {
  denominator <- sqrt((1 - r_xz^2) * (1 - r_yz^2))
  if (!is.finite(denominator) || denominator <= sqrt(.Machine$double.eps)) {
    stop("The partial correlation is undefined because no usable residual variation remains.", call. = FALSE)
  }
  (r_xy - r_xz * r_yz) / denominator
}

# A conceptual third-variable structure. The arrows show one possible
# explanation to investigate, not a conclusion produced by a correlation.
third_variable_nodes <- tibble(
  x = c(0.50, 0.18, 0.82),
  y = c(0.82, 0.20, 0.20),
  label = c(t06_text$third_z, t06_text$variable_x, t06_text$variable_y)
)

third_variable_edges <- tibble(
  x = c(0.45, 0.55),
  y = c(0.73, 0.73),
  xend = c(0.24, 0.76),
  yend = c(0.29, 0.29)
)

p_third_variable <- ggplot() +
  geom_segment(
    data = third_variable_edges,
    aes(x, y, xend = xend, yend = yend),
    color = "#527C99",
    linewidth = 1.05,
    arrow = grid::arrow(length = grid::unit(0.18, "cm"))
  ) +
  geom_segment(
    aes(x = 0.29, y = 0.20, xend = 0.71, yend = 0.20),
    color = "#C05A47",
    linewidth = 0.9,
    linetype = "dashed"
  ) +
  annotate(
    "label",
    x = 0.50,
    y = 0.12,
    label = t06_text$observed_xy,
    size = 3.4,
    fill = "#FFF8F5",
    color = "#713D31",
    linewidth = 0.3
  ) +
  geom_label(
    data = third_variable_nodes,
    aes(x, y, label = label),
    size = 3.8,
    fontface = "bold",
    fill = "#F5F8FA",
    color = "#203A4F",
    linewidth = 0.35
  ) +
  coord_cartesian(xlim = c(0, 1), ylim = c(0.02, 1), clip = "off") +
  labs(
    title = t06_text$third_title,
    subtitle = t06_text$third_subtitle
  ) +
  theme_void(base_size = 12) +
  theme(
    plot.title = element_text(face = "bold", color = "#172B3A"),
    plot.subtitle = element_text(color = "#536475"),
    plot.background = element_rect(fill = "white", color = NA),
    panel.background = element_rect(fill = "white", color = NA),
    plot.margin = margin(12, 24, 12, 24)
  )

# Newly constructed city counts illustrate the source-supported population
# explanation without reproducing the protected source figure or data.
set.seed(4610)
city_population_pattern <- tidyr::crossing(
  band_index = seq_len(3L),
  within_band_position = seq(-1.25, 1.25, length.out = 12L)
) |>
  mutate(
    population_band = factor(
      t06_text$police_population_bands[band_index],
      levels = t06_text$police_population_bands
    ),
    police_count = round(
      28 + 54 * (band_index - 1) + 11 * within_band_position + rnorm(n(), 0, 2.2),
      1
    ),
    offense_count = round(
      150 + 95 * (band_index - 1) - 16 * within_band_position + rnorm(n(), 0, 6.5),
      1
    ),
    hover_text = paste0(
      t06_text$population_band, ": ", population_band,
      "<br>", t06_text$police_axis, ": ", format_t06(police_count, 1),
      "<br>", t06_text$offense_axis, ": ", format_t06(offense_count, 1)
    )
  )

p_police_crime_population <- ggplot(
  city_population_pattern,
  aes(police_count, offense_count, color = population_band, text = hover_text)
) +
  geom_smooth(
    data = city_population_pattern,
    aes(police_count, offense_count, group = 1),
    inherit.aes = FALSE,
    method = "lm",
    formula = y ~ x,
    se = FALSE,
    color = "#172B3A",
    linewidth = 0.9,
    linetype = "dashed"
  ) +
  geom_smooth(
    data = city_population_pattern,
    aes(police_count, offense_count, color = population_band, group = population_band),
    inherit.aes = FALSE,
    method = "lm",
    formula = y ~ x,
    se = FALSE,
    linewidth = 0.9
  ) +
  geom_point(alpha = 0.84, size = 2.7) +
  scale_color_manual(
    values = setNames(
      c("#2F6F9F", "#3F8B6D", "#C05A47"),
      t06_text$police_population_bands
    )
  ) +
  labs(
    title = t06_text$police_population_title,
    subtitle = t06_text$police_population_subtitle,
    x = t06_text$police_axis,
    y = t06_text$offense_axis,
    color = t06_text$population_band
  ) +
  t06_theme(base_size = 11)

# A second source-supported third-variable story is intentionally hypothetical
# and nonnumeric. The arrows describe one plausible explanation to consider;
# they are not estimates and do not assert a demonstrated causal process.
icecream_story_text <- if (topic_locale == "de") {
  list(
    node_labels = c(
      "Heisseres Wetter oder\nSommersaison (Z)",
      "Schwimmen und\nAufenthalt am Wasser",
      "Glacekonsum (X)",
      "Ertrinkungsfälle (Y)"
    ),
    association = paste0(
      "Hier kann ein positiver beobachteter Zusammenhang auftreten,\n",
      "ohne dass Glace Ertrinkungsfälle verursacht"
    ),
    title = "Eine Drittvariable kann eine verlockende, aber irreführende Geschichte erzeugen",
    subtitle = paste0(
      "Nur hypothetische Veranschaulichung: Es werden keine Beobachtungen, ",
      "Korrelationen oder kausalen Effekte berichtet"
    )
  )
} else if (topic_locale == "sq") {
  list(
    node_labels = c(
      "Mot më i nxehtë ose\nstina e verës (Z)",
      "Noti dhe ekspozimi\nndaj ujit",
      "Konsumi i\nakullores (X)",
      "Rastet e mbytjes\nnë ujë (Y)"
    ),
    association = paste0(
      "Këtu mund të shfaqet një lidhje pozitive e vrojtuar,\n",
      "pa qenë akullorja shkak i rasteve të mbytjes"
    ),
    title = "Një ndryshore e tretë mund të krijojë një tregim joshës, por çorientues",
    subtitle = paste0(
      "Vetëm ilustrim hipotetik: nuk raportohen vrojtime, korrelacione ",
      "ose efekte shkakësore"
    )
  )
} else {
  list(
    node_labels = c(
      "Hotter weather or\nsummer season (Z)",
      "Swimming and\nwater exposure",
      "Ice-cream\nconsumption (X)",
      "Drowning\nincidents (Y)"
    ),
    association = paste0(
      "A positive observed association can appear here\n",
      "without ice cream causing drowning incidents"
    ),
    title = "A Third Variable Can Create a Tempting but Misleading Story",
    subtitle = paste0(
      "Hypothetical illustration only: no observations, correlations, ",
      "or causal effects are being reported"
    )
  )
}

icecream_story_nodes <- tibble(
  x = c(0.28, 0.72, 0.18, 0.82),
  y = c(0.82, 0.82, 0.28, 0.28),
  label = icecream_story_text$node_labels,
  kind = c("third", "exposure", "focal", "outcome")
)

icecream_story_edges <- tibble(
  x = c(0.24, 0.39, 0.75),
  y = c(0.72, 0.82, 0.72),
  xend = c(0.20, 0.61, 0.80),
  yend = c(0.38, 0.82, 0.38)
)

p_icecream_third_variable <- ggplot() +
  geom_segment(
    data = icecream_story_edges,
    aes(x, y, xend = xend, yend = yend),
    color = "#527C99",
    linewidth = 1.0,
    arrow = grid::arrow(length = grid::unit(0.16, "cm"), type = "closed")
  ) +
  geom_segment(
    aes(x = 0.29, y = 0.28, xend = 0.71, yend = 0.28),
    color = "#C05A47",
    linewidth = 0.9,
    linetype = "dashed"
  ) +
  annotate(
    "label",
    x = 0.50,
    y = 0.12,
    label = icecream_story_text$association,
    fill = "#FFF8F5",
    color = "#713D31",
    size = 3.15,
    linewidth = 0.3,
    lineheight = 0.95
  ) +
  geom_label(
    data = icecream_story_nodes,
    aes(x, y, label = label, fill = kind),
    color = "#203A4F",
    fontface = "bold",
    size = 3.45,
    lineheight = 0.95,
    linewidth = 0.35,
    label.padding = grid::unit(0.22, "lines")
  ) +
  scale_fill_manual(
    values = c(
      third = "#EAF2F8", exposure = "#EAF4EF",
      focal = "#F5F8FA", outcome = "#FFF4EA"
    ),
    guide = "none"
  ) +
  coord_cartesian(xlim = c(0.02, 0.98), ylim = c(0.02, 1), clip = "off") +
  labs(
    title = icecream_story_text$title,
    subtitle = icecream_story_text$subtitle
  ) +
  theme_void(base_size = 11) +
  theme(
    plot.title = element_text(face = "bold", color = "#172B3A"),
    plot.subtitle = element_text(color = "#536475"),
    plot.background = element_rect(fill = "white", color = NA),
    panel.background = element_rect(fill = "white", color = NA),
    plot.margin = margin(14, 24, 14, 24)
  )

# Process diagram for the residual definition of partial correlation. Its
# geometry is shared while the learner-facing labels follow the page locale.
residualization_flow_text <- if (topic_locale == "de") {
  list(
    node_labels = c(
      "Beobachtetes X", "X aus Z anpassen", "X-Residuum\nêₓ = X − X̂",
      "Beobachtetes Y", "Y aus Z anpassen", "Y-Residuum\nêᵧ = Y − Ŷ",
      "Die beiden\nResiduenspalten paaren", "Residuen korrelieren\npartielles r"
    ),
    edge_labels = c(
      "Z verwenden", "beobachtet − angepasst", "Z verwenden",
      "beobachtet − angepasst", "dieselben Fälle", "dieselben Fälle",
      "Pearson-Korrelation"
    ),
    title = "Partielle Korrelation ist eine Korrelation zwischen zwei Residuenspalten",
    subtitle = paste0(
      "Beide interessierenden Variablen werden um dieselbe Drittvariable bereinigt, ",
      "bevor ihre verbleibende lineare gemeinsame Bewegung verglichen wird"
    )
  )
} else if (topic_locale == "sq") {
  list(
    node_labels = c(
      "X i vrojtuar", "Përshtat X nga Z", "Reziduali i X\nêₓ = X − X̂",
      "Y i vrojtuar", "Përshtat Y nga Z", "Reziduali i Y\nêᵧ = Y − Ŷ",
      "Çifto dy kolonat\ne rezidualeve", "Korrelo rezidualet\nr e pjesshme"
    ),
    edge_labels = c(
      "përdor Z", "e vrojtuar − e përshtatur", "përdor Z",
      "e vrojtuar − e përshtatur", "të njëjtat raste", "të njëjtat raste",
      "Korrelacioni i Pearson-it"
    ),
    title = "Korrelacioni i pjesshëm është korrelacion mes dy kolonave të rezidualeve",
    subtitle = paste0(
      "Të dyja ndryshoret kryesore përshtaten për të njëjtën ndryshore të tretë ",
      "para se të krahasohet lëvizja e tyre lineare e mbetur"
    )
  )
} else {
  list(
    node_labels = c(
      "Observed X", "Fit X from Z", "X residual\nêₓ = X − X̂",
      "Observed Y", "Fit Y from Z", "Y residual\nêᵧ = Y − Ŷ",
      "Pair the two\nresidual columns", "Correlate residuals\npartial r"
    ),
    edge_labels = c(
      "use Z", "observed − fitted", "use Z", "observed − fitted",
      "same cases", "same cases", "Pearson correlation"
    ),
    title = "Partial Correlation Is a Correlation Between Two Residual Columns",
    subtitle = paste0(
      "Both focal variables are adjusted for the same third variable before their ",
      "remaining linear movement is compared"
    )
  )
}

residualization_flow_nodes <- tibble(
  node = c("x", "fit_x", "resid_x", "y", "fit_y", "resid_y", "correlate", "partial"),
  x = c(0.0, 1.6, 3.35, 0.0, 1.6, 3.35, 5.25, 7.0),
  y = c(1.75, 1.75, 1.75, 0.45, 0.45, 0.45, 1.10, 1.10),
  label = residualization_flow_text$node_labels,
  node_type = c("observed", "fit", "residual", "observed", "fit", "residual", "pair", "result")
)

residualization_flow_edges <- tribble(
  ~from, ~to, ~edge_label,
  "x", "fit_x", residualization_flow_text$edge_labels[[1]],
  "fit_x", "resid_x", residualization_flow_text$edge_labels[[2]],
  "y", "fit_y", residualization_flow_text$edge_labels[[3]],
  "fit_y", "resid_y", residualization_flow_text$edge_labels[[4]],
  "resid_x", "correlate", residualization_flow_text$edge_labels[[5]],
  "resid_y", "correlate", residualization_flow_text$edge_labels[[6]],
  "correlate", "partial", residualization_flow_text$edge_labels[[7]]
) |>
  left_join(residualization_flow_nodes |> select(from = node, x, y), by = "from") |>
  left_join(residualization_flow_nodes |> select(to = node, xend = x, yend = y), by = "to") |>
  mutate(
    label_x = x + 0.5 * (xend - x),
    label_y = y + 0.5 * (yend - y) + c(0.28, 0.28, -0.28, -0.28, 0, 0, 0.25)
  )

p_residualization_flow_en <- ggplot() +
  geom_segment(
    data = residualization_flow_edges,
    aes(x, y, xend = xend, yend = yend),
    color = "#8198A8",
    linewidth = 0.85,
    arrow = grid::arrow(length = grid::unit(0.13, "cm"), type = "closed")
  ) +
  geom_label(
    data = residualization_flow_nodes,
    aes(x, y, label = label, fill = node_type),
    color = "#203A4F",
    fontface = "bold",
    size = 3.05,
    lineheight = 0.95,
    linewidth = 0.3,
    label.padding = grid::unit(0.2, "lines")
  ) +
  geom_label(
    data = residualization_flow_edges,
    aes(label_x, label_y, label = edge_label),
    fill = "white",
    color = "#536475",
    size = 2.65,
    linewidth = 0,
    label.padding = grid::unit(0.07, "lines")
  ) +
  scale_fill_manual(
    values = c(
      observed = "#EAF2F8", fit = "#F3F6F8", residual = "#EAF4EF",
      pair = "#FFF4EA", result = "#FFE0CC"
    ),
    guide = "none"
  ) +
  coord_cartesian(xlim = c(-0.65, 7.65), ylim = c(-0.02, 2.25), clip = "off") +
  labs(
    title = residualization_flow_text$title,
    subtitle = residualization_flow_text$subtitle
  ) +
  theme_void(base_size = 11) +
  theme(
    plot.title = element_text(face = "bold", color = "#172B3A"),
    plot.subtitle = element_text(color = "#536475"),
    plot.background = element_rect(fill = "white", color = NA),
    panel.background = element_rect(fill = "white", color = NA),
    plot.margin = margin(14, 24, 14, 24)
  )

# Two newly generated patterns show that adjustment can either reduce or
# increase a coefficient. They are conceptual demonstrations, not source data.
set.seed(4602)
scenario_n <- 160
shared_z <- rnorm(scenario_n)
shared_x <- 0.8 * shared_z + rnorm(scenario_n, 0, 0.8)
shared_y <- 0.3 * shared_x + 0.8 * shared_z + rnorm(scenario_n, 0, 0.8)

set.seed(4603)
opposing_z <- rnorm(scenario_n)
opposing_x <- 0.8 * opposing_z + rnorm(scenario_n, 0, 0.8)
opposing_y <- 0.8 * opposing_x - 0.9 * opposing_z + rnorm(scenario_n, 0, 0.8)

adjustment_scenarios <- bind_rows(
  tibble(
    scenario = t06_text$scenario_shared,
    raw = cor(shared_x, shared_y),
    partial = cor(resid(lm(shared_x ~ shared_z)), resid(lm(shared_y ~ shared_z)))
  ),
  tibble(
    scenario = t06_text$scenario_opposing,
    raw = cor(opposing_x, opposing_y),
    partial = cor(resid(lm(opposing_x ~ opposing_z)), resid(lm(opposing_y ~ opposing_z)))
  )
) |>
  mutate(
    scenario = factor(
      scenario,
      levels = c(t06_text$scenario_shared, t06_text$scenario_opposing)
    ),
    # An explicit numeric position keeps Plotly from mixing discrete tick
    # labels with the arrow segment coordinates. The displayed labels and
    # ordering remain the factor levels above.
    scenario_y = as.numeric(scenario),
    arrow_end = partial - sign(partial - raw) * 0.018
  )

adjustment_scenario_points <- adjustment_scenarios |>
  pivot_longer(c(raw, partial), names_to = "coefficient", values_to = "value") |>
  mutate(
    coefficient = recode(
      coefficient,
      raw = t06_text$bivariate_r,
      partial = t06_text$partial_r
    )
  )

p_adjustment_directions <- ggplot(adjustment_scenarios, aes(y = scenario_y)) +
  geom_vline(xintercept = 0, color = "#AAB6C0", linewidth = 0.6) +
  geom_segment(
    aes(x = raw, xend = arrow_end, yend = scenario_y),
    color = "#93A7B7",
    linewidth = 1.1,
    arrow = grid::arrow(length = grid::unit(0.13, "cm"), type = "closed")
  ) +
  geom_point(
    data = adjustment_scenario_points,
    aes(x = value, color = coefficient),
    size = 3.4
  ) +
  geom_text(
    data = adjustment_scenario_points,
    aes(x = value, label = format_t06(value, 2), color = coefficient),
    nudge_y = 0.14,
    size = 3.4,
    show.legend = FALSE
  ) +
  scale_color_manual(values = setNames(c("#2F6F9F", "#C05A47"), c(t06_text$bivariate_r, t06_text$partial_r))) +
  scale_x_continuous(limits = c(-0.05, 0.85), breaks = seq(0, 0.8, 0.2)) +
  scale_y_continuous(
    breaks = seq_along(levels(adjustment_scenarios$scenario)),
    labels = levels(adjustment_scenarios$scenario)
  ) +
  labs(
    title = t06_text$adjustment_title,
    subtitle = t06_text$adjustment_subtitle,
    x = t06_text$correlation_coefficient,
    y = NULL,
    color = NULL
  ) +
  t06_theme(base_size = 11) +
  theme(panel.grid.major.y = element_blank())

# Deterministic teaching cohort for the full simulated example.
set.seed(4606)
sim_n <- 140
sim_data <- tibble(
  participant_id = sprintf("S%03d", seq_len(sim_n)),
  baseline_preparation = round(pmin(pmax(rnorm(sim_n, 50, 10), 20), 80), 1)
) |>
  mutate(
    practice_hours = round(
      pmin(pmax(1.5 + 0.10 * baseline_preparation + rnorm(sim_n, 0, 1.7), 0), 15),
      1
    ),
    assessment_score = round(
      pmin(
        pmax(
          20 + 2.0 * practice_hours + 0.60 * baseline_preparation + rnorm(sim_n, 0, 8),
          0
        ),
        100
      ),
      1
    )
  )

practice_on_baseline <- lm(practice_hours ~ baseline_preparation, data = sim_data)
score_on_baseline <- lm(assessment_score ~ baseline_preparation, data = sim_data)

sim_data <- sim_data |>
  mutate(
    fitted_practice = unname(fitted(practice_on_baseline)),
    practice_residual = unname(resid(practice_on_baseline)),
    fitted_score = unname(fitted(score_on_baseline)),
    score_residual = unname(resid(score_on_baseline))
  )

sim_r_xy <- cor(sim_data$practice_hours, sim_data$assessment_score)
sim_r_xz <- cor(sim_data$practice_hours, sim_data$baseline_preparation)
sim_r_yz <- cor(sim_data$assessment_score, sim_data$baseline_preparation)
sim_partial_residual <- cor(sim_data$practice_residual, sim_data$score_residual)
sim_partial_formula <- partial_from_three(sim_r_xy, sim_r_xz, sim_r_yz)
sim_formula_numerator <- sim_r_xy - sim_r_xz * sim_r_yz
sim_formula_denominator <- sqrt((1 - sim_r_xz^2) * (1 - sim_r_yz^2))

sim_display_data <- sim_data |>
  select(participant_id, baseline_preparation, practice_hours, assessment_score)

# Retain the existing preview object for locale pages that have not yet adopted
# the full interactive table.
sim_preview <- sim_display_data |>
  slice_head(n = 12)

sim_summary_table <- tibble(
  quantity = t06_text$summary_quantities,
  value = c(
    as.character(sim_n),
    format_t06(mean(sim_data$baseline_preparation), 2),
    format_t06(mean(sim_data$practice_hours), 2),
    format_t06(mean(sim_data$assessment_score), 2),
    format_t06(sd(sim_data$baseline_preparation), 2),
    format_t06(sd(sim_data$practice_hours), 2),
    format_t06(sd(sim_data$assessment_score), 2)
  )
)

pairwise_correlation_table <- tibble(
  pair = t06_text$pair_labels,
  correlation = c(sim_r_xy, sim_r_xz, sim_r_yz)
) |>
  mutate(correlation = round(correlation, 3))

sim_residual_preview <- sim_data |>
  select(
    participant_id,
    practice_hours,
    fitted_practice,
    practice_residual,
    assessment_score,
    fitted_score,
    score_residual
  ) |>
  slice_head(n = 8) |>
  mutate(across(where(is.numeric), ~ round(.x, 2)))

method_comparison_table <- tibble(
  method = t06_text$method_labels,
  partial_correlation = round(c(sim_partial_residual, sim_partial_formula), 6)
)

# Show the two fitted values and residuals for the same selected cases.
residualization_data <- bind_rows(
  sim_data |>
    transmute(
      participant_id,
      baseline_preparation,
      observed = practice_hours,
      fitted = fitted_practice,
      residual = practice_residual,
      panel = t06_text$residual_panels[[1]]
    ),
  sim_data |>
    transmute(
      participant_id,
      baseline_preparation,
      observed = assessment_score,
      fitted = fitted_score,
      residual = score_residual,
      panel = t06_text$residual_panels[[2]]
    )
) |>
  mutate(
    panel = factor(
      panel,
      levels = t06_text$residual_panels
    ),
    hover_text = paste0(
      t06_text$hover_participant, ": ", participant_id,
      "<br>", t06_text$baseline_hover, ": ", format_t06(baseline_preparation, 1),
      "<br>", t06_text$observed_axis, ": ", format_t06(observed, 2),
      "<br>", t06_text$hover_fitted, ": ", format_t06(fitted, 2),
      "<br>", t06_text$hover_residual, ": ", format_t06(residual, 2)
    )
  )

residual_highlights <- residualization_data |>
  filter(participant_id %in% c("S012", "S041", "S078", "S119"))

p_residualization <- ggplot(
  residualization_data,
  aes(baseline_preparation, observed, text = hover_text)
) +
  geom_point(color = "#2F6F9F", alpha = 0.62, size = 1.8) +
  geom_line(
    aes(y = fitted, group = panel),
    color = "#527C99",
    linewidth = 0.9
  ) +
  geom_segment(
    data = residual_highlights,
    aes(xend = baseline_preparation, yend = fitted),
    color = "#C05A47",
    linewidth = 0.9
  ) +
  geom_point(
    data = residual_highlights,
    color = "#C05A47",
    size = 2.4
  ) +
  facet_wrap(
    vars(panel),
    ncol = 1,
    scales = "free_y",
    labeller = labeller(panel = label_wrap_gen(width = 34))
  ) +
  labs(
    title = t06_text$residual_title,
    subtitle = t06_text$residual_subtitle,
    x = t06_text$baseline_axis,
    y = t06_text$observed_axis
  ) +
  t06_theme(base_size = 11) +
  theme(
    panel.spacing.y = grid::unit(1.5, "lines"),
    strip.text = element_text(lineheight = 1.02)
  )
attr(p_residualization, "ratiomera_widget_height") <- 720
attr(p_residualization, "ratiomera_top_margin") <- 176

# Standardize both raw and residual values so the two panels can use common
# axes while preserving their respective correlations.
raw_adjusted_data <- bind_rows(
  sim_data |>
    transmute(
      participant_id,
      x = as.numeric(scale(practice_hours)),
      y = as.numeric(scale(assessment_score)),
      panel = paste0(t06_text$raw_panel_prefix, format_t06(sim_r_xy, 3))
    ),
  sim_data |>
    transmute(
      participant_id,
      x = as.numeric(scale(practice_residual)),
      y = as.numeric(scale(score_residual)),
      panel = paste0(
        t06_text$adjusted_panel_prefix,
        format_t06(sim_partial_residual, 3)
      )
    )
)

raw_adjusted_levels <- raw_adjusted_data |>
  distinct(panel) |>
  pull(panel)
raw_adjusted_data <- raw_adjusted_data |>
  mutate(
    panel = factor(panel, levels = raw_adjusted_levels),
    hover_text = paste0(
      t06_text$hover_participant, ": ", participant_id,
      "<br>", t06_text$practice_sd_hover, ": ", format_t06(x, 2),
      "<br>", t06_text$assessment_sd_hover, ": ", format_t06(y, 2)
    )
  )

p_raw_adjusted <- ggplot(raw_adjusted_data, aes(x, y, text = hover_text)) +
  geom_hline(yintercept = 0, color = "#C9D2D9", linewidth = 0.5) +
  geom_vline(xintercept = 0, color = "#C9D2D9", linewidth = 0.5) +
  geom_point(color = "#2F6F9F", alpha = 0.70, size = 1.9) +
  geom_smooth(
    data = raw_adjusted_data,
    aes(x, y),
    inherit.aes = FALSE,
    method = "lm",
    formula = y ~ x,
    se = FALSE,
    color = "#C05A47",
    linewidth = 0.9
  ) +
  facet_wrap(
    vars(panel),
    ncol = 1,
    labeller = labeller(panel = label_wrap_gen(width = 34))
  ) +
  labs(
    title = t06_text$raw_adjusted_title,
    subtitle = t06_text$raw_adjusted_subtitle,
    x = t06_text$practice_sd_axis,
    y = t06_text$assessment_sd_axis
  ) +
  t06_theme(base_size = 11) +
  theme(
    panel.spacing.y = grid::unit(1.5, "lines"),
    strip.text = element_text(lineheight = 1.02)
  )
attr(p_raw_adjusted, "ratiomera_widget_height") <- 780
attr(p_raw_adjusted, "ratiomera_top_margin") <- 232
