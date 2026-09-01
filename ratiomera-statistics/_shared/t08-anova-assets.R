# Shared deterministic data, calculations, tables, and figures for Topic 8.

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

t08_text_sets <- list(
  en = list(
    conditions = c("Reference", "Planning guide", "Retrieval prompts", "Combined routine"),
    comparison_panels = c("Planned contrast", "Tukey: all pairs", "Dunnett: each versus reference"),
    reference_suffix = "\nreference",
    comparison_title = "Three Comparison Families, Three Questions",
    comparison_subtitle = "Weights define a planned contrast; lines show the pairs included by two post hoc families",
    fwer_title = "Repeated Unadjusted Tests Increase Familywise Error",
    fwer_subtitle = "The curve uses independent tests, each with a 0.05 testwise error rate",
    family_tests_axis = "Number of tests in the family",
    type_i_axis = "Probability of at least one Type I error",
    factorial_patterns = c(
      "No main effects\nor interaction",
      "Main effect of A\nonly",
      "Main effect of B\nonly",
      "Both main effects,\nno interaction",
      "Noncrossing\ninteraction",
      "Crossing interaction,\nequal marginals"
    ),
    overlap_label = "B1 and B2 overlap",
    factorial_title = "Cell Means Separate Main Effects from Interaction",
    factorial_subtitle = "Parallel lines indicate no interaction; nonparallel lines indicate that one factor's pattern changes across the other",
    factor_a_axis = "Level of factor A",
    cell_mean_axis = "Constructed cell mean",
    factor_b_legend = "Factor B",
    icc_patterns = c("Low within-level similarity", "High within-level similarity"),
    icc_title = "The ICC Compares Within-Level Similarity with Between-Level Separation",
    icc_subtitle = "Each vertical set represents observations sharing one randomly sampled factor level",
    random_level_axis = "Random-factor level",
    constructed_outcome_axis = "Constructed outcome",
    occasions = c("First", "Second", "Third"),
    repeated_title = "Repeated Measurements Stay Linked Within Each Person",
    repeated_subtitle = "Blue lines follow individuals; the orange line connects occasion means",
    occasion_axis = "Measurement occasion",
    summary_quantities = c(
      "Total sum of squares", "Factor sum of squares", "Error sum of squares",
      "Factor SS + error SS", "Total degrees of freedom", "Factor df + error df"
    ),
    anova_sources = c("Study condition", "Error", "Total"),
    planned_comparison = "Average of three active routines minus reference",
    groups_title = "Learning Scores Across Four Randomized Conditions",
    groups_subtitle = "White diamonds are group means; the dashed line is the grand mean",
    condition_axis = "Study condition",
    learning_axis = "Learning score (0 to 100)",
    ss_bars = c("Total variability", "Partitioned variability"),
    ss_components = c("Total SS", "Factor SS", "Error SS"),
    ss_title = "The Total Sum of Squares Splits Exactly into Two Components",
    ss_subtitle = "Factor SS records between-group mean differences; error SS records within-group deviations",
    ss_axis = "Sum of squares",
    diagnostic_panels = c("Residuals versus fitted values", "Normal Q-Q plot"),
    diagnostics_title = "Model Diagnostics Address Different Assumptions",
    diagnostics_subtitle = "Look for an even residual band and Q-Q points that remain reasonably near the reference line",
    diagnostics_x = "Standardized fitted value or normal quantile",
    diagnostics_y = "Standardized residual"
  ),
  de = list(
    conditions = c("Referenz", "Planungshilfe", "Abrufhinweise", "Kombinierte Routine"),
    comparison_panels = c("Geplanter Kontrast", "Tukey: alle Paare", "Dunnett: jede Stufe gegen Referenz"),
    reference_suffix = "\nReferenz",
    comparison_title = "Drei Vergleichsfamilien, drei Fragen",
    comparison_subtitle = "Gewichte definieren einen geplanten Kontrast; Linien zeigen die Paare zweier Post-hoc-Familien",
    fwer_title = "Wiederholte unbereinigte Tests erhöhen den familienweisen Fehler",
    fwer_subtitle = "Die Kurve verwendet unabhängige Tests mit je einer testbezogenen Fehlerrate von 0,05",
    family_tests_axis = "Anzahl Tests in der Familie",
    type_i_axis = "Wahrscheinlichkeit mindestens eines Fehlers 1. Art",
    factorial_patterns = c(
      "Keine Haupteffekte\nund keine Interaktion",
      "Nur Haupteffekt\nvon A",
      "Nur Haupteffekt\nvon B",
      "Beide Haupteffekte,\nkeine Interaktion",
      "Nicht kreuzende\nInteraktion",
      "Kreuzende Interaktion,\ngleiche Randmittel"
    ),
    overlap_label = "B1 und B2 überlappen",
    factorial_title = "Zellmittelwerte trennen Haupteffekte von Interaktionen",
    factorial_subtitle = "Parallele Linien bedeuten keine Interaktion; nicht parallele Linien zeigen, dass sich das Muster eines Faktors über den anderen verändert",
    factor_a_axis = "Stufe von Faktor A",
    cell_mean_axis = "Konstruierter Zellmittelwert",
    factor_b_legend = "Faktor B",
    icc_patterns = c("Geringe Ähnlichkeit innerhalb der Stufen", "Hohe Ähnlichkeit innerhalb der Stufen"),
    icc_title = "Die ICC vergleicht Ähnlichkeit innerhalb der Stufen mit Trennung zwischen den Stufen",
    icc_subtitle = "Jede vertikale Gruppe stellt Beobachtungen dar, die dieselbe zufällig gezogene Faktorstufe teilen",
    random_level_axis = "Stufe des Zufallsfaktors",
    constructed_outcome_axis = "Konstruierte Zielvariable",
    occasions = c("Erste", "Zweite", "Dritte"),
    repeated_title = "Wiederholte Messungen bleiben innerhalb jeder Person verbunden",
    repeated_subtitle = "Blaue Linien folgen einzelnen Personen; die orange Linie verbindet die Messzeitpunktmittelwerte",
    occasion_axis = "Messzeitpunkt",
    summary_quantities = c(
      "Gesamtquadratsumme", "Faktorquadratsumme", "Fehlerquadratsumme",
      "Faktor-SS + Fehler-SS", "Gesamtfreiheitsgrade", "Faktor-df + Fehler-df"
    ),
    anova_sources = c("Studienbedingung", "Fehler", "Gesamt"),
    planned_comparison = "Mittelwert der drei aktiven Routinen minus Referenz",
    groups_title = "Lernpunktwerte in vier randomisierten Bedingungen",
    groups_subtitle = "Weisse Rauten sind Gruppenmittelwerte; die gestrichelte Linie ist der Gesamtmittelwert",
    condition_axis = "Studienbedingung",
    learning_axis = "Lernpunktwert (0 bis 100)",
    ss_bars = c("Gesamtvariation", "Zerlegte Variation"),
    ss_components = c("Gesamt-SS", "Faktor-SS", "Fehler-SS"),
    ss_title = "Die gesamte Quadratsumme zerfällt exakt in zwei Komponenten",
    ss_subtitle = "Faktor-SS: zwischen Gruppen; Fehler-SS: innerhalb der Gruppen",
    ss_axis = "Quadratsumme",
    diagnostic_panels = c("Residuen gegen angepasste Werte", "Normales Q-Q-Diagramm"),
    diagnostics_title = "Modelldiagnosen betreffen unterschiedliche Annahmen",
    diagnostics_subtitle = "Achte auf ein gleichmässiges Residuenband und Q-Q-Punkte, die hinreichend nahe an der Referenzlinie bleiben",
    diagnostics_x = "Standardisierter angepasster Wert oder Normalquantil",
    diagnostics_y = "Standardisiertes Residuum"
  ),
  sq = list(
    conditions = c("Referenca", "Planifikimi i udhëzuar", "Nxitje rikujtimi", "Rutinë e kombinuar"),
    comparison_panels = c("Kontrasti i planifikuar", "Tukey: të gjitha çiftet", "Dunnett: kundrejt referencës"),
    reference_suffix = "\nreferenca",
    comparison_title = "Tri familje krahasimi, tri pyetje",
    comparison_subtitle = "Peshat japin kontrastin; vijat tregojnë çiftet post hoc",
    fwer_title = "Testet e papërshtatura e rrisin gabimin familjar",
    fwer_subtitle = "Teste të pavarura, secili me shkallë gabimi 0.05",
    family_tests_axis = "Numri i testeve në familje",
    type_i_axis = "Probabiliteti i të paktën një gabimi të llojit I",
    factorial_patterns = c(
      "Pa efekte kryesore\nose ndërveprim",
      "Vetëm efekti kryesor\ni A-së",
      "Vetëm efekti kryesor\ni B-së",
      "Të dy efektet kryesore,\npa ndërveprim",
      "Ndërveprim pa\nkryqëzim",
      "Ndërveprim me kryqëzim,\nmesatare margjinale të barabarta"
    ),
    overlap_label = "B1 dhe B2 mbivendosen",
    factorial_title = "Mesataret e qelizave ndajnë efektet nga ndërveprimi",
    factorial_subtitle = "Vijat joparalele tregojnë se modeli i një faktori ndryshon përgjatë tjetrit",
    factor_a_axis = "Niveli i faktorit A",
    cell_mean_axis = "Mesatarja e ndërtuar e qelizës",
    factor_b_legend = "Faktori B",
    icc_patterns = c("Ngjashmëri e ulët brenda nivelit", "Ngjashmëri e lartë brenda nivelit"),
    icc_title = "ICC krahason ngjashmërinë brenda dhe ndarjen mes niveleve",
    icc_subtitle = "Çdo grup vertikal ndan një nivel të faktorit të rastësishëm",
    random_level_axis = "Niveli i faktorit të rastësishëm",
    constructed_outcome_axis = "Rezultati i ndërtuar",
    occasions = c("E para", "E dyta", "E treta"),
    repeated_title = "Matjet e përsëritura mbeten të lidhura brenda personit",
    repeated_subtitle = "Vijat blu ndjekin personat; vija portokalli lidh mesataret",
    occasion_axis = "Rasti i matjes",
    summary_quantities = c(
      "Shuma totale e katrorëve", "Shuma e katrorëve e faktorit", "Shuma e katrorëve e gabimit",
      "SS e faktorit + SS e gabimit", "Shkallët totale të lirisë", "df e faktorit + df e gabimit"
    ),
    anova_sources = c("Kushti i studimit", "Gabimi", "Totali"),
    planned_comparison = "Mesatarja e tri rutinave aktive minus referenca",
    groups_title = "Rezultatet e të nxënit në katër kushte të rastësuara",
    groups_subtitle = "Rombet e bardha janë mesataret; vija e ndërprerë është mesatarja e përgjithshme",
    condition_axis = "Kushti i studimit",
    learning_axis = "Rezultati i të nxënit (0 deri në 100)",
    ss_bars = c("Ndryshueshmëria totale", "Ndryshueshmëria e ndarë"),
    ss_components = c("SS totale", "SS e faktorit", "SS e gabimit"),
    ss_title = "Shuma totale e katrorëve ndahet\nsaktësisht në dy pjesë",
    ss_subtitle = "SS e faktorit është mes grupeve; SS e gabimit është brenda grupeve",
    ss_axis = "Shuma e katrorëve",
    diagnostic_panels = c("Rezidualet kundrejt vlerave të përshtatura", "Grafiku normal Q-Q"),
    diagnostics_title = "Diagnostikimet trajtojnë supozime të ndryshme",
    diagnostics_subtitle = "Kërko një brez të njëtrajtshëm dhe pika Q-Q afër vijës referuese",
    diagnostics_x = "Vlera e standardizuar e përshtatur ose kuantili normal",
    diagnostics_y = "Reziduali i standardizuar"
  )
)

if (!topic_locale %in% names(t08_text_sets)) {
  stop("Unsupported Topic 8 locale: ", topic_locale, call. = FALSE)
}
t08_text <- t08_text_sets[[topic_locale]]

# Keep browser-visible hover text in the same language as the page. Albanian
# and German labels are explicit; English remains the fallback for the
# canonical English rendering path.
t08_hover_text <- if (topic_locale == "sq") {
  list(
    participant = "Pjesëmarrësi: ",
    condition = "Kushti: ",
    observed_score = "Rezultati i vëzhguar: ",
    group_fitted_mean = "Mesatarja e përshtatur e grupit: ",
    residual = "Reziduali: ",
    standardized_residual = "Reziduali i standardizuar: ",
    f_under_null = "F nën hipotezën zero: ",
    density = "Dendësia: ",
    inside_p_tail = "Brenda bishtit të vlerës p",
    before_observed_f = "Para F-së së vëzhguar",
    sum_of_squares = "Shuma e katrorëve: ",
    standardized_fitted = "Vlera e standardizuar e përshtatur: ",
    expected_normal_quantile = "Kuantili normal i pritur: ",
    ordered_standardized_residual = "Reziduali i standardizuar i renditur: "
  )
} else if (topic_locale == "de") {
  list(
    participant = "Teilnehmenden-ID: ",
    condition = "Studienbedingung: ",
    observed_score = "Beobachteter Lernpunktwert: ",
    group_fitted_mean = "Angepasster Gruppenmittelwert: ",
    residual = "Residuum: ",
    standardized_residual = "Standardisiertes Residuum: ",
    f_under_null = "F unter der Nullhypothese: ",
    density = "Dichte: ",
    inside_p_tail = "Im rechtsseitigen p-Wert-Bereich",
    before_observed_f = "Links vom beobachteten F",
    sum_of_squares = "Quadratsumme: ",
    standardized_fitted = "Standardisierter angepasster Wert: ",
    expected_normal_quantile = "Erwartetes Normalquantil: ",
    ordered_standardized_residual = "Geordnetes standardisiertes Residuum: "
  )
} else {
  list(
    participant = "Participant: ",
    condition = "Condition: ",
    observed_score = "Observed score: ",
    group_fitted_mean = "Group fitted mean: ",
    residual = "Residual: ",
    standardized_residual = "Standardized residual: ",
    f_under_null = "F under the null: ",
    density = "Density: ",
    inside_p_tail = "Inside the p-value tail",
    before_observed_f = "Before the observed F",
    sum_of_squares = "Sum of squares: ",
    standardized_fitted = "Standardized fitted value: ",
    expected_normal_quantile = "Expected normal quantile: ",
    ordered_standardized_residual = "Ordered standardized residual: "
  )
}

t08_theory_hover <- if (topic_locale == "sq") {
  list(
    design = "Dizajni: ", cell = "Qeliza: ", component = "Përbërësi: ",
    factor_level = "Niveli i faktorit: ", outcome = "Rezultati i krijuar: ",
    group_mean = "Mesatarja e grupit: ", minimum = "Minimumi: ", maximum = "Maksimumi: ",
    comparison = "Krahasimi: ", tests = "Numri i testeve: ", fwer = "Gabimi familjar: ",
    pattern = "Modeli: ", factor_a = "Faktori A: ", factor_b = "Faktori B: ",
    cell_mean = "Mesatarja e qelizës: ", random_level = "Niveli i rastësishëm: ",
    occasion = "Rasti i matjes: ", value = "Vlera: ", analysis = "Analiza: ",
    quantity = "Madhësia: "
  )
} else if (topic_locale == "de") {
  list(
    design = "Design: ", cell = "Zelle: ", component = "Komponente: ",
    factor_level = "Faktorstufe: ", outcome = "Konstruierter Zielwert: ",
    group_mean = "Gruppenmittelwert: ", minimum = "Minimum: ", maximum = "Maximum: ",
    comparison = "Vergleich: ", tests = "Anzahl Tests: ", fwer = "Familienweiser Fehler: ",
    pattern = "Muster: ", factor_a = "Faktor A: ", factor_b = "Faktor B: ",
    cell_mean = "Zellmittelwert: ", random_level = "Zufällige Stufe: ",
    occasion = "Messzeitpunkt: ", value = "Wert: ", analysis = "Analyse: ",
    quantity = "Grösse: "
  )
} else {
  list(
    design = "Design: ", cell = "Cell: ", component = "Component: ",
    factor_level = "Factor level: ", outcome = "Constructed outcome: ",
    group_mean = "Group mean: ", minimum = "Minimum: ", maximum = "Maximum: ",
    comparison = "Comparison: ", tests = "Number of tests: ", fwer = "Familywise error: ",
    pattern = "Pattern: ", factor_a = "Factor A: ", factor_b = "Factor B: ",
    cell_mean = "Cell mean: ", random_level = "Random-factor level: ",
    occasion = "Measurement occasion: ", value = "Value: ", analysis = "Analysis: ",
    quantity = "Quantity: "
  )
}

required_packages <- c(
  "dplyr", "tibble", "tidyr", "ggplot2", "DT", "knitr", "plotly", "htmlwidgets"
)
missing_packages <- required_packages[
  !vapply(required_packages, requireNamespace, logical(1), quietly = TRUE)
]
if (length(missing_packages)) {
  stop(
    "Topic 8 requires these R packages: ",
    paste(missing_packages, collapse = ", "),
    call. = FALSE
  )
}

suppressPackageStartupMessages({
  library(dplyr)
  library(tibble)
  library(tidyr)
  library(ggplot2)
  library(knitr)
  library(plotly)
  library(htmlwidgets)
})

t08_palette <- setNames(
  c("#718494", "#4F84A6", "#2F6F9F", "#C05A47"),
  t08_text$conditions
)

t08_theme <- function(base_size = 12) {
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

format_t08 <- function(value, digits = 3) {
  sprintf(paste0("%.", digits, "f"), value)
}

format_p_t08 <- function(value) {
  ifelse(value < 0.001, "< .001", sub("^0", "", sprintf("%.3f", value)))
}

t08_wrap_axis_labels <- function(values, width = 14L) {
  vapply(
    as.character(values),
    function(value) paste(strwrap(value, width = width), collapse = "\n"),
    character(1),
    USE.NAMES = FALSE
  )
}

topic8_plotly <- function(plot, alt_text, tooltip = "text", top_margin = 60) {
  native_annotation <- attr(plot, "t08_native_annotation", exact = TRUE)
  native_shapes <- attr(plot, "t08_native_shapes", exact = TRUE)
  plot_kind <- attr(plot, "ratiomera_plotly_kind", exact = TRUE)
  widget_height <- attr(plot, "ratiomera_widget_height", exact = TRUE)
  plot_top_margin <- attr(plot, "ratiomera_top_margin", exact = TRUE)
  if (!is.null(plot_top_margin)) top_margin <- max(top_margin, plot_top_margin)
  plot <- ratiomera_make_plotly_compatible(plot)
  widget <- ggplotly(
    plot,
    tooltip = tooltip,
    dynamicTicks = FALSE,
    height = widget_height
  )
  # Keep one responsive source of truth for height. The htmlwidget retains the
  # requested intrinsic height, while Plotly autosizes its SVG to the actual
  # Quarto container instead of overflowing into the caption on narrow pages.
  widget$x$layout$height <- NULL
  widget <- ratiomera_localize_plotly_hover(
    widget,
    ratiomera_plotly_hover_labels(plot, topic_locale)
  )

  # ggplotly generates English-only summary hover labels for box traces.
  # The overlaid observations already carry fully localized teaching detail,
  # so suppress that duplicate browser-generated layer in every locale.
  if (!is.null(widget$x$data)) {
    widget$x$data <- lapply(widget$x$data, function(trace) {
      if (identical(trace$type, "box")) trace$hoverinfo <- "skip"
      if (
        identical(plot_kind, "ss_partition") &&
        identical(trace$mode, "text") &&
        !is.null(trace$text) &&
        any(grepl(t08_text$ss_components[[2]], trace$text, fixed = TRUE))
      ) {
        trace$textposition <- "middle right"
        trace$cliponaxis <- FALSE
      }
      trace
    })
  }

  # geom_label is not implemented by ggplotly. Figures that need a boxed data
  # annotation therefore register a native Plotly annotation on the source
  # plot so the visible explanation is never silently discarded.
  if (!is.null(native_annotation)) {
    widget$x$layout$annotations <- c(
      widget$x$layout$annotations,
      list(native_annotation)
    )
  }

  # The actual right-tail density can be nearly flush with zero when the
  # observed F statistic is large. A narrow band along the baseline keeps the
  # same tail interval visible without changing the distribution or its axes.
  if (!is.null(native_shapes)) {
    widget$x$layout$shapes <- c(widget$x$layout$shapes, native_shapes)
  }

  bottom_margin <- if (isTRUE(plot_kind %in% c("groups", "ss_partition"))) 96 else 84
  left_margin <- if (identical(plot_kind, "groups")) {
    138
  } else if (identical(plot_kind, "ss_partition")) {
    110
  } else {
    76
  }

  widget |>
    ratiomera_prepare_plotly_widget(
      title_width = 36,
      axis_width = 32,
      # The diagnostic facet headings already contain one deliberate line
      # break. Keep each half intact instead of turning them into four lines.
      annotation_width = 58,
      title_size = 14
    ) |>
    layout(
      autosize = TRUE,
      hovermode = "closest",
      margin = list(l = left_margin, r = 34, b = bottom_margin, t = max(top_margin, 104), pad = 2)
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

one_way_components <- function(outcome, group) {
  group <- droplevels(factor(group))
  n_total <- length(outcome)
  n_levels <- nlevels(group)
  group_n <- table(group)
  group_means <- tapply(outcome, group, mean)
  grand_mean <- mean(outcome)
  ss_total <- sum((outcome - grand_mean)^2)
  ss_factor <- sum(as.numeric(group_n) * (group_means - grand_mean)^2)
  ss_error <- sum((outcome - group_means[group])^2)
  df_factor <- n_levels - 1L
  df_error <- n_total - n_levels
  df_total <- n_total - 1L
  ms_factor <- ss_factor / df_factor
  ms_error <- ss_error / df_error
  f_value <- ms_factor / ms_error
  p_value <- pf(f_value, df_factor, df_error, lower.tail = FALSE)

  list(
    n_total = n_total,
    n_levels = n_levels,
    group_n = group_n,
    group_means = group_means,
    grand_mean = grand_mean,
    ss_total = ss_total,
    ss_factor = ss_factor,
    ss_error = ss_error,
    df_factor = df_factor,
    df_error = df_error,
    df_total = df_total,
    ms_factor = ms_factor,
    ms_error = ms_error,
    f_value = f_value,
    p_value = p_value
  )
}

# The new explanatory figures share geometry and numerical values across
# locales. Only their learner-facing labels change.
anova_visual_text <- if (topic_locale == "de") {
  list(
    cell_panels = c(
      "A. Ein Faktor mit vier Stufen",
      "B. Zwei gekreuzte Faktoren bilden sechs Zellen"
    ),
    level = "Stufe ",
    one_cell = "\n= eine Zelle",
    cell = "Zelle\nA",
    with_b = " mit B",
    factor_b_level = "Faktor B, Stufe B",
    factor_a = "Faktor A",
    cells_title = "Stufen bestimmen die Zellen, deren Zielwertmittelwerte verglichen werden",
    cells_subtitle = paste0(
      "Bei zwei Faktoren ist jede Kombination aus einer A-Stufe und einer B-Stufe ",
      "eine eigene Zelle"
    ),
    deviation_point_labels = c(
      "Gesamtmittelwert: ȳ = 60",
      "Gruppenmittelwert: ȳᵢ = 66",
      "Beobachteter Wert: yᵢₘ = 70"
    ),
    deviation_total = "gesamt: yᵢₘ − ȳ = 10",
    deviation_factor = "Faktor: ȳᵢ − ȳ = 6",
    deviation_within = "innerhalb: yᵢₘ − ȳᵢ = 4",
    deviation_box = paste0(
      "Gesamtabweichung\n= Faktoranteil\n+ Anteil innerhalb der Gruppe",
      "\n\n10 = 6 + 4"
    ),
    deviation_title = "Die ANOVA zerlegt eine Beobachtung mithilfe von zwei Mittelwerten",
    deviation_subtitle = paste0(
      "In diesem konstruierten Beispiel liegt der Gruppenmittelwert zwischen dem ",
      "Gesamtmittelwert und der Beobachtung"
    ),
    f_scenarios = c(
      small = "Kleinere Streuung\ninnerhalb der Gruppen",
      large = "Grössere Streuung\ninnerhalb der Gruppen"
    ),
    larger_f = "\nGrösseres F = ",
    smaller_f = "\nKleineres F = ",
    f_title = "F vergleicht Gruppentrennung\nmit Streuung innerhalb der Gruppen",
    f_subtitle = "Mittelwerte: 50, 60, 70. Nur die Streuung innerhalb der Gruppen ändert sich.",
    factor_level = "Faktorstufe",
    constructed_outcome = "Konstruierte Zielvariable",
    observed_f = "Beobachtetes F = ",
    right_tail_p = "\np im rechten Verteilungsschwanz ",
    tail_title = paste0(
      "Der Omnibus-p-Wert ist die Fläche",
      "\nim rechten Rand der F-Verteilung"
    ),
    tail_subtitle_prefix = "Referenzverteilung bei gleichen Populationsmittelwerten: df₁ = ",
    tail_subtitle_middle = ", df₂ = ",
    tail_x = "F-Statistik unter der Nullhypothese",
    density = "Dichte"
  )
} else if (topic_locale == "sq") {
  list(
    cell_panels = c(
      "A. Një faktor me katër nivele",
      "B. Dy faktorë të kryqëzuar krijojnë gjashtë qeliza"
    ),
    level = "Niveli ",
    one_cell = "\n= një qelizë",
    cell = "Qeliza\nA",
    with_b = " me B",
    factor_b_level = "Faktori B, niveli B",
    factor_a = "Faktori A",
    cells_title = "Nivelet përcaktojnë qelizat, mesataret e rezultatit të të cilave krahasohen",
    cells_subtitle = paste0(
      "Me dy faktorë, çdo kombinim i një niveli A dhe një niveli B është ",
      "një qelizë më vete"
    ),
    deviation_point_labels = c(
      "Mesatarja e përgjithshme: ȳ = 60",
      "Mesatarja e grupit: ȳᵢ = 66",
      "Vlera e vrojtuar: yᵢₘ = 70"
    ),
    deviation_total = "totale: yᵢₘ − ȳ = 10",
    deviation_factor = "faktori: ȳᵢ − ȳ = 6",
    deviation_within = "brenda grupit: yᵢₘ − ȳᵢ = 4",
    deviation_box = paste0(
      "Devijimi i përgjithshëm\n= përbërësi i faktorit\n+ përbërësi brenda grupit",
      "\n\n10 = 6 + 4"
    ),
    deviation_title = "ANOVA e zbërthen një vrojtim rreth dy mesatareve",
    deviation_subtitle = paste0(
      "Në këtë shembull të krijuar, mesatarja e grupit gjendet mes mesatares së ",
      "përgjithshme dhe vrojtimit"
    ),
    f_scenarios = c(
      small = "Shpërhapje më e vogël\nbrenda grupeve",
      large = "Shpërhapje më e madhe\nbrenda grupeve"
    ),
    larger_f = "\nF më e madhe = ",
    smaller_f = "\nF më e vogël = ",
    f_title = "F krahason ndarjen e grupeve\nme shpërhapjen brenda grupeve",
    f_subtitle = "Mesataret: 50, 60, 70. Ndryshon vetëm shpërhapja brenda grupeve.",
    factor_level = "Niveli i faktorit",
    constructed_outcome = "Rezultati i krijuar",
    observed_f = "F e vrojtuar = ",
    right_tail_p = "\nvlera p në bishtin e djathtë ",
    tail_title = paste0(
      "Vlera p e testit të përgjithshëm është sipërfaqja",
      "\nnë bishtin e djathtë të shpërndarjes F"
    ),
    tail_subtitle_prefix = "Shpërndarja e referencës kur mesataret e popullatës janë të barabarta: df₁ = ",
    tail_subtitle_middle = ", df₂ = ",
    tail_x = "Statistika F nën hipotezën zero",
    density = "Dendësia"
  )
} else {
  list(
    cell_panels = c(
      "A. One factor with four levels",
      "B. Two crossed factors create six cells"
    ),
    level = "Level ",
    one_cell = "\n= one cell",
    cell = "Cell\nA",
    with_b = " with B",
    factor_b_level = "Factor B level B",
    factor_a = "Factor A",
    cells_title = "Levels Define the Cells Whose Outcome Means Are Compared",
    cells_subtitle = "With two factors, every combination of one A level and one B level is a separate cell",
    deviation_point_labels = c(
      "Grand mean: ȳ = 60", "Group mean: ȳᵢ = 66",
      "Observed score: yᵢₘ = 70"
    ),
    deviation_total = "total: yᵢₘ − ȳ = 10",
    deviation_factor = "factor: ȳᵢ − ȳ = 6",
    deviation_within = "within: yᵢₘ − ȳᵢ = 4",
    deviation_box = paste0(
      "total deviation\n= factor component\n+ within-group component",
      "\n\n10 = 6 + 4"
    ),
    deviation_title = "ANOVA Decomposes One Observation Around Two Means",
    deviation_subtitle = "The group mean sits between the grand mean and the observation in this constructed example",
    f_scenarios = c(
      small = "Smaller spread\nwithin groups",
      large = "Larger spread\nwithin groups"
    ),
    larger_f = "\nLarger F = ",
    smaller_f = "\nSmaller F = ",
    f_title = "F Compares Group Separation\nwith Within-Group Spread",
    f_subtitle = "Means: 50, 60, and 70. Only the spread within groups changes.",
    factor_level = "Factor level",
    constructed_outcome = "Constructed outcome",
    observed_f = "Observed F = ",
    right_tail_p = "\nright-tail p ",
    tail_title = paste0(
      "The Omnibus p-Value Is the F Distribution's",
      "\nRight-Tail Area"
    ),
    tail_subtitle_prefix = "Reference distribution under equal population means: df₁ = ",
    tail_subtitle_middle = ", df₂ = ",
    tail_x = "F statistic under the null hypothesis",
    density = "Density"
  )
}

# Design map. It distinguishes the one-way use of "cell" from the crossed
# combinations created by two factors.
anova_cell_panels <- anova_visual_text$cell_panels

anova_cell_data <- bind_rows(
  tibble(
    panel = anova_cell_panels[[1]],
    x = 1:4,
    y = 1.5,
    label = paste0(anova_visual_text$level, 1:4, anova_visual_text$one_cell),
    fill_group = paste0("L", 1:4)
  ),
  expand_grid(x = 1:3, y = 1:2) |>
    mutate(
      panel = anova_cell_panels[[2]],
      label = paste0(anova_visual_text$cell, y, anova_visual_text$with_b, x),
      fill_group = paste0("B", x)
    )
) |>
  mutate(
    panel = factor(panel, levels = anova_cell_panels),
    hover = paste0(
      t08_theory_hover$design, as.character(panel),
      "<br>", t08_theory_hover$cell, gsub("\\n", " ", label)
    )
  )

p_anova_cells_en <- ggplot(anova_cell_data, aes(x, y)) +
  geom_tile(aes(fill = fill_group, text = hover), width = 0.86, height = 0.72, color = "white", linewidth = 1) +
  geom_text(aes(label = label), color = "white", fontface = "bold", size = 3.3, lineheight = 0.95) +
  geom_text(
    data = tibble(
      panel = factor(anova_cell_panels[[2]], levels = anova_cell_panels),
      x = 1:3,
      y = 2.62,
      label = paste0(anova_visual_text$factor_b_level, 1:3)
    ),
    aes(x, y, label = label),
    inherit.aes = FALSE,
    color = "#34495E",
    fontface = "bold",
    size = 3
  ) +
  geom_text(
    data = tibble(
      panel = factor(anova_cell_panels[[2]], levels = anova_cell_panels),
      x = 0.32,
      y = 1:2,
      label = paste0("A", 1:2)
    ),
    aes(x, y, label = label),
    inherit.aes = FALSE,
    color = "#34495E",
    fontface = "bold",
    size = 3.2
  ) +
  annotate(
    "text",
    x = 0.25,
    y = 2.55,
    label = anova_visual_text$factor_a,
    color = "#34495E",
    fontface = "bold",
    size = 3
  ) +
  facet_wrap(vars(panel), nrow = 1, scales = "free_x") +
  scale_fill_manual(
    values = c(
      L1 = "#315E7D", L2 = "#477C9D", L3 = "#6695B0", L4 = "#C05A47",
      B1 = "#315E7D", B2 = "#5F91AE", B3 = "#C05A47"
    ),
    guide = "none"
  ) +
  coord_cartesian(ylim = c(0.45, 2.9), clip = "off") +
  labs(
    title = anova_visual_text$cells_title,
    subtitle = anova_visual_text$cells_subtitle
  ) +
  theme_void(base_size = 11) +
  theme(
    plot.title = element_text(face = "bold", color = "#172B3A"),
    plot.subtitle = element_text(color = "#536475"),
    strip.text = element_text(face = "bold", color = "#203A4F"),
    panel.spacing = grid::unit(1.4, "lines"),
    plot.background = element_rect(fill = "white", color = NA),
    panel.background = element_rect(fill = "white", color = NA),
    plot.margin = margin(14, 22, 14, 22)
  )

# One-observation geometry for the one-way sum-of-squares identity.
anova_deviation_points <- tibble(
  x = 1,
  y = c(60, 66, 70),
  label = anova_visual_text$deviation_point_labels,
  kind = c("Grand mean", "Group mean", "Observed")
) |>
  mutate(
    hover = paste0(
      t08_theory_hover$component, label,
      "<br>", t08_theory_hover$value, format_t08(y, 0)
    )
  )

anova_deviation_kind_labels <- if (topic_locale == "de") {
  c(
    "Total deviation" = "Gesamtabweichung",
    "Factor component" = "Faktoranteil",
    "Within-group component" = "Anteil innerhalb der Gruppe"
  )
} else if (topic_locale == "sq") {
  c(
    "Total deviation" = "Devijimi i përgjithshëm",
    "Factor component" = "Përbërësi i faktorit",
    "Within-group component" = "Përbërësi brenda grupit"
  )
} else {
  c(
    "Total deviation" = "Total deviation",
    "Factor component" = "Factor component",
    "Within-group component" = "Within-group component"
  )
}

anova_deviation_segments <- tribble(
  ~x, ~xend, ~y, ~yend, ~kind,
  0.58, 0.58, 60, 70, "Total deviation",
  1.00, 1.00, 60, 66, "Factor component",
  1.42, 1.42, 66, 70, "Within-group component"
) |>
  mutate(
    distance = yend - y,
    hover = paste0(
      t08_theory_hover$component, unname(anova_deviation_kind_labels[kind]),
      "<br>", t08_theory_hover$value, format_t08(distance, 0)
    )
  )

p_anova_deviation_en <- ggplot() +
  geom_segment(
    data = anova_deviation_segments,
    aes(x, y, xend = xend, yend = yend, color = kind, text = hover),
    linewidth = 1.3,
    arrow = grid::arrow(length = grid::unit(0.14, "cm"), type = "closed")
  ) +
  geom_point(
    data = anova_deviation_points,
    aes(x, y, fill = kind, text = hover),
    shape = 21,
    size = 4.2,
    color = "white",
    stroke = 0.9
  ) +
  geom_label(
    data = anova_deviation_points,
    aes(x = 1.83, y, label = label, color = kind),
    fill = "white",
    size = 3.15,
    linewidth = 0.22
  ) +
  annotate("text", x = 0.34, y = 65, label = anova_visual_text$deviation_total, angle = 90, color = "#244C69", fontface = "bold", size = 3.1) +
  annotate("text", x = 0.78, y = 63, label = anova_visual_text$deviation_factor, angle = 90, color = "#276449", fontface = "bold", size = 3.0) +
  annotate("text", x = 1.58, y = 68, label = anova_visual_text$deviation_within, hjust = 0, color = "#8A3F36", fontface = "bold", size = 3.0) +
  annotate(
    "label",
    x = 3.75,
    y = 65,
    label = anova_visual_text$deviation_box,
    fill = "#F4F8FA",
    color = "#203A4F",
    fontface = "bold",
    size = 3.4,
    lineheight = 1.05,
    linewidth = 0.35
  ) +
  scale_color_manual(
    values = c(
      "Total deviation" = "#244C69", "Factor component" = "#3F8B6D",
      "Within-group component" = "#C05A47", "Grand mean" = "#536475",
      "Group mean" = "#276449", Observed = "#8A3F36"
    ),
    guide = "none"
  ) +
  scale_fill_manual(
    values = c("Grand mean" = "#718494", "Group mean" = "#3F8B6D", Observed = "#C05A47"),
    guide = "none"
  ) +
  coord_cartesian(xlim = c(0.08, 4.65), ylim = c(58.8, 71.3), clip = "off") +
  labs(
    title = anova_visual_text$deviation_title,
    subtitle = anova_visual_text$deviation_subtitle
  ) +
  theme_void(base_size = 11) +
  theme(
    plot.title = element_text(face = "bold", color = "#172B3A"),
    plot.subtitle = element_text(color = "#536475"),
    plot.background = element_rect(fill = "white", color = NA),
    panel.background = element_rect(fill = "white", color = NA),
    plot.margin = margin(14, 24, 14, 24)
  )

# The group means are identical across panels; only within-group spread changes.
anova_f_offsets <- list(
  small = c(-2.0, -1.2, -0.5, 0.5, 1.2, 2.0),
  large = c(-10, -6, -3, 3, 6, 10)
)
anova_f_means <- c(A = 50, B = 60, C = 70)
anova_f_intuition_data <- bind_rows(lapply(names(anova_f_offsets), function(scenario_name) {
  expand_grid(group = factor(names(anova_f_means), levels = names(anova_f_means)), offset = anova_f_offsets[[scenario_name]]) |>
    mutate(
      outcome = unname(anova_f_means[as.character(group)]) + offset,
      scenario_key = scenario_name,
      scenario = unname(anova_visual_text$f_scenarios[[scenario_name]])
    )
})) |>
  mutate(scenario = factor(scenario, levels = unname(anova_visual_text$f_scenarios)))

anova_f_panel_labels <- anova_f_intuition_data |>
  group_by(scenario) |>
  group_modify(~ {
    components <- one_way_components(.x$outcome, .x$group)
    tibble(
      ms_factor = components$ms_factor,
      ms_error = components$ms_error,
      f_value = components$f_value
    )
  }) |>
  ungroup() |>
  mutate(
    panel = as.character(scenario),
    statistic_label = paste0(
      "MSₐ = ", format_t08(ms_factor, 2),
      "\nMSₑ = ", format_t08(ms_error, 2),
      "  |  F = ", format_t08(f_value, 2)
    )
  )

anova_f_intuition_data <- anova_f_intuition_data |>
  left_join(anova_f_panel_labels, by = "scenario") |>
  mutate(
    panel = factor(panel, levels = anova_f_panel_labels$panel),
    hover = paste0(
      t08_theory_hover$design, as.character(panel),
      "<br>", t08_theory_hover$factor_level, group,
      "<br>", t08_theory_hover$outcome, format_t08(outcome, 1),
      "<br>MSₐ: ", format_t08(ms_factor, 2),
      "<br>MSₑ: ", format_t08(ms_error, 2),
      "<br>F: ", format_t08(f_value, 2)
    )
  )

anova_f_range_data <- anova_f_intuition_data |>
  group_by(panel, group) |>
  summarise(
    minimum = min(outcome),
    maximum = max(outcome),
    group_mean = mean(outcome),
    .groups = "drop"
  ) |>
  mutate(
    hover = paste0(
      t08_theory_hover$factor_level, group,
      "<br>", t08_theory_hover$minimum, format_t08(minimum, 1),
      "<br>", t08_theory_hover$group_mean, format_t08(group_mean, 1),
      "<br>", t08_theory_hover$maximum, format_t08(maximum, 1)
    )
  )

anova_f_annotation_data <- anova_f_panel_labels |>
  mutate(
    panel = factor(panel, levels = anova_f_panel_labels$panel),
    group = factor("A", levels = names(anova_f_means)),
    x = 2,
    y = 87.0
  )

p_anova_f_intuition_en <- ggplot(anova_f_intuition_data, aes(group, outcome, color = group)) +
  geom_hline(yintercept = mean(anova_f_means), color = "#718494", linetype = "dashed", linewidth = 0.75) +
  geom_linerange(
    data = anova_f_range_data,
    aes(group, ymin = minimum, ymax = maximum, color = group, text = hover),
    inherit.aes = FALSE,
    linewidth = 7,
    alpha = 0.13,
    lineend = "round"
  ) +
  geom_point(aes(text = hover), position = position_jitter(width = 0.08, height = 0, seed = 8810), size = 2.3, alpha = 0.78) +
  stat_summary(fun = mean, geom = "point", shape = 23, fill = "white", color = "#172B3A", size = 4) +
  geom_text(
    data = anova_f_range_data,
    aes(
      group,
      y = group_mean + 2.8,
      label = paste0(
        if (topic_locale == "de") {
          "Mittelwert = "
        } else if (topic_locale == "sq") {
          "Mesatarja = "
        } else {
          "mean = "
        },
        format_t08(group_mean, 0)
      )
    ),
    inherit.aes = FALSE,
    color = "#34495E",
    fontface = "bold",
    size = 3
  ) +
  geom_text(
    data = anova_f_annotation_data,
    aes(x, y, label = statistic_label),
    inherit.aes = FALSE,
    hjust = 0,
    vjust = 1,
    color = "#203A4F",
    fontface = "bold",
    lineheight = 1.02,
    size = 3.05
  ) +
  facet_wrap(vars(panel), nrow = 1) +
  scale_color_manual(values = c(A = "#315E7D", B = "#6695B0", C = "#C05A47"), guide = "none") +
  scale_y_continuous(limits = c(38, 89), breaks = seq(40, 80, 10)) +
  labs(
    title = anova_visual_text$f_title,
    subtitle = anova_visual_text$f_subtitle,
    x = anova_visual_text$factor_level,
    y = anova_visual_text$constructed_outcome
  ) +
  t08_theme(base_size = 11) +
  theme(
    legend.position = "none",
    panel.spacing.x = grid::unit(1.5, "lines"),
    plot.margin = margin(14, 20, 12, 16)
  )

# Comparison-family diagrams: one prespecified weighted contrast, every pair,
# and every active level against one reference level.
comparison_panels <- t08_text$comparison_panels

comparison_nodes <- bind_rows(
  expand_grid(panel = comparison_panels, node = c("A1", "A2", "A3", "A4")) |>
    mutate(
      x = recode(node, A1 = 0.15, A2 = 0.38, A3 = 0.62, A4 = 0.85),
      y = 0.48,
      display_label = if_else(
        panel == comparison_panels[[3]] & node == "A1",
        paste0("A1", t08_text$reference_suffix),
        node
      ),
      panel = factor(panel, levels = comparison_panels),
      hover = paste0(
        t08_theory_hover$comparison, as.character(panel),
        "<br>", t08_theory_hover$factor_level, node
      )
    )
)

pair_edges <- tribble(
  ~from, ~to,
  "A1", "A2",
  "A1", "A3",
  "A1", "A4",
  "A2", "A3",
  "A2", "A4",
  "A3", "A4"
)

node_x <- c(A1 = 0.15, A2 = 0.38, A3 = 0.62, A4 = 0.85)
comparison_edges <- bind_rows(
  pair_edges |>
    transmute(
      panel = comparison_panels[[2]],
      x = node_x[from],
      xend = node_x[to],
      edge_index = row_number()
    ),
  tibble(
    panel = comparison_panels[[3]],
    x = node_x["A1"],
    xend = node_x[c("A2", "A3", "A4")],
    edge_index = 1:3
  )
) |>
  mutate(
    y = 0.48 + 0.07 * edge_index,
    yend = y,
    panel = factor(panel, levels = comparison_panels)
  )

comparison_edge_legs <- bind_rows(
  comparison_edges |>
    transmute(panel, x, y, xend = x, yend = 0.52),
  comparison_edges |>
    transmute(panel, x = xend, y, xend = xend, yend = 0.52)
)

planned_weights <- tibble(
  panel = factor(comparison_panels[[1]], levels = comparison_panels),
  x = node_x,
  y = 0.70,
  label = c("−1", "−1", "+1", "+1")
)

planned_span <- tibble(
  panel = factor(comparison_panels[[1]], levels = comparison_panels),
  x = 0.22,
  xend = 0.78,
  y = 0.81,
  yend = 0.81
)

p_comparison_types <- ggplot() +
  geom_segment(
    data = comparison_edges,
    aes(x, y, xend = xend, yend = yend),
    color = "#93A7B7",
    linewidth = 0.8
  ) +
  geom_segment(
    data = comparison_edge_legs,
    aes(x, y, xend = xend, yend = yend),
    color = "#93A7B7",
    linewidth = 0.55
  ) +
  geom_label(
    data = comparison_nodes,
    aes(x, y, label = display_label, text = hover),
    fill = "#F5F8FA",
    color = "#203A4F",
    size = 3.5,
    fontface = "bold",
    linewidth = 0.35
  ) +
  geom_text(
    data = planned_weights,
    aes(x, y, label = label),
    color = "#C05A47",
    size = 4,
    fontface = "bold"
  ) +
  geom_segment(
    data = planned_span,
    aes(x, y, xend = xend, yend = yend),
    color = "#C05A47",
    linewidth = 0.8
  ) +
  facet_wrap(
    vars(panel),
    nrow = 1,
    labeller = labeller(panel = label_wrap_gen(width = 14))
  ) +
  coord_cartesian(xlim = c(0.05, 0.95), ylim = c(0.35, 0.90), clip = "off") +
  labs(
    title = t08_text$comparison_title,
    subtitle = t08_text$comparison_subtitle
  ) +
  theme_void(base_size = 11) +
  theme(
    plot.title = element_text(face = "bold", color = "#172B3A"),
    plot.subtitle = element_text(color = "#536475"),
    strip.text = element_text(face = "bold", color = "#203A4F"),
    panel.spacing = grid::unit(1.2, "lines"),
    plot.background = element_rect(fill = "white", color = NA),
    panel.background = element_rect(fill = "white", color = NA),
    plot.margin = margin(12, 18, 12, 18)
  )

# Multiple-testing values. The raw familywise calculation and the exact Sidak
# equality are for independent tests. Bonferroni controls the familywise bound
# without requiring independence.
multiplicity_table <- tibble(m = 1:6) |>
  mutate(
    raw_fwer_independent = 1 - (1 - 0.05)^m,
    sidak_testwise_independent = 1 - (1 - 0.05)^(1 / m),
    bonferroni_testwise = 0.05 / m,
    hover = paste0(
      t08_theory_hover$tests, m,
      "<br>", t08_theory_hover$fwer, format_t08(raw_fwer_independent, 4)
    )
  )

multiplicity_display <- multiplicity_table |>
  transmute(
    comparisons = m,
    raw_fwer = format_t08(raw_fwer_independent, 4),
    sidak_alpha = format_t08(sidak_testwise_independent, 4),
    bonferroni_alpha = format_t08(bonferroni_testwise, 4)
  )

p_fwer_independent <- ggplot(
  multiplicity_table,
  aes(m, raw_fwer_independent, text = hover, group = 1)
) +
  geom_hline(yintercept = 0.05, color = "#C05A47", linetype = "dashed", linewidth = 0.8) +
  geom_line(color = "#2F6F9F", linewidth = 1) +
  geom_point(color = "#2F6F9F", size = 2.6) +
  scale_x_continuous(breaks = 1:6) +
  scale_y_continuous(limits = c(0, 0.28), breaks = seq(0, 0.25, 0.05)) +
  labs(
    title = t08_text$fwer_title,
    subtitle = t08_text$fwer_subtitle,
    x = t08_text$family_tests_axis,
    y = t08_text$type_i_axis
  ) +
  t08_theme()

# Cell means for six factorial patterns. These are conceptual values, not
# study data. Together they separate absence of effects, each main effect,
# two additive main effects, and two forms of interaction. Marginal means are
# calculated directly from the four cells.
factorial_patterns <- tribble(
  ~pattern, ~factor_a, ~factor_b, ~cell_mean,
  t08_text$factorial_patterns[[1]], "A1", "B1", 55,
  t08_text$factorial_patterns[[1]], "A1", "B2", 55,
  t08_text$factorial_patterns[[1]], "A2", "B1", 55,
  t08_text$factorial_patterns[[1]], "A2", "B2", 55,
  t08_text$factorial_patterns[[2]], "A1", "B1", 50,
  t08_text$factorial_patterns[[2]], "A1", "B2", 50,
  t08_text$factorial_patterns[[2]], "A2", "B1", 65,
  t08_text$factorial_patterns[[2]], "A2", "B2", 65,
  t08_text$factorial_patterns[[3]], "A1", "B1", 50,
  t08_text$factorial_patterns[[3]], "A1", "B2", 65,
  t08_text$factorial_patterns[[3]], "A2", "B1", 50,
  t08_text$factorial_patterns[[3]], "A2", "B2", 65,
  t08_text$factorial_patterns[[4]], "A1", "B1", 45,
  t08_text$factorial_patterns[[4]], "A1", "B2", 55,
  t08_text$factorial_patterns[[4]], "A2", "B1", 60,
  t08_text$factorial_patterns[[4]], "A2", "B2", 70,
  t08_text$factorial_patterns[[5]], "A1", "B1", 50,
  t08_text$factorial_patterns[[5]], "A1", "B2", 55,
  t08_text$factorial_patterns[[5]], "A2", "B1", 58,
  t08_text$factorial_patterns[[5]], "A2", "B2", 75,
  t08_text$factorial_patterns[[6]], "A1", "B1", 45,
  t08_text$factorial_patterns[[6]], "A1", "B2", 65,
  t08_text$factorial_patterns[[6]], "A2", "B1", 65,
  t08_text$factorial_patterns[[6]], "A2", "B2", 45
) |>
  mutate(
    pattern = factor(
      pattern,
      levels = t08_text$factorial_patterns
    ),
    factor_a = factor(factor_a, levels = c("A1", "A2")),
    factor_b = factor(factor_b, levels = c("B1", "B2")),
    hover = paste0(
      t08_theory_hover$pattern, gsub("\\n", " ", as.character(pattern)),
      "<br>", t08_theory_hover$factor_a, factor_a,
      "<br>", t08_theory_hover$factor_b, factor_b,
      "<br>", t08_theory_hover$cell_mean, format_t08(cell_mean, 1)
    )
  )

factorial_marginals_table <- factorial_patterns |>
  group_by(pattern) |>
  summarise(
    `A1 marginal` = mean(cell_mean[factor_a == "A1"]),
    `A2 marginal` = mean(cell_mean[factor_a == "A2"]),
    `B1 marginal` = mean(cell_mean[factor_b == "B1"]),
    `B2 marginal` = mean(cell_mean[factor_b == "B2"]),
    .groups = "drop"
  ) |>
  mutate(pattern = gsub("\\n", " ", as.character(pattern)))

p_factorial_patterns <- ggplot(
  factorial_patterns,
  aes(factor_a, cell_mean, color = factor_b, group = factor_b, text = hover)
) +
  geom_line(linewidth = 1) +
  geom_point(size = 3) +
  facet_wrap(vars(pattern), ncol = 3) +
  scale_color_manual(values = c(B1 = "#2F6F9F", B2 = "#C05A47")) +
  scale_y_continuous(limits = c(40, 78), breaks = seq(40, 75, 5)) +
  labs(
    title = t08_text$factorial_title,
    subtitle = t08_text$factorial_subtitle,
    x = t08_text$factor_a_axis,
    y = t08_text$cell_mean_axis,
    color = t08_text$factor_b_legend
  ) +
  t08_theme(base_size = 10.5)

# Conceptual low- and high-clustering patterns for the one-way random ICC.
icc_pattern_data <- bind_rows(
  tibble(
    pattern = t08_text$icc_patterns[[1]],
    level = rep(paste0("L", 1:5), each = 5),
    value = c(
      42, 47, 50, 55, 60,
      41, 48, 51, 56, 59,
      43, 46, 52, 54, 61,
      40, 49, 50, 57, 58,
      42, 45, 53, 55, 60
    )
  ),
  tibble(
    pattern = t08_text$icc_patterns[[2]],
    level = rep(paste0("L", 1:5), each = 5),
    value = c(
      35, 36, 34, 35, 36,
      43, 42, 44, 43, 42,
      51, 50, 52, 51, 50,
      59, 58, 60, 59, 58,
      67, 66, 68, 67, 66
    )
  )
) |>
  mutate(
    pattern = factor(
      pattern,
      levels = t08_text$icc_patterns
    ),
    hover = paste0(
      t08_theory_hover$pattern, as.character(pattern),
      "<br>", t08_theory_hover$random_level, level,
      "<br>", t08_theory_hover$value, format_t08(value, 1)
    )
  )

icc_numeric_components <- one_way_components(
  outcome = icc_pattern_data$value[
    icc_pattern_data$pattern == t08_text$icc_patterns[[2]]
  ],
  group = icc_pattern_data$level[
    icc_pattern_data$pattern == t08_text$icc_patterns[[2]]
  ]
)
icc_numeric_n_per_level <- unname(icc_numeric_components$group_n[[1]])
icc_numeric_between_variance <-
  (icc_numeric_components$ms_factor - icc_numeric_components$ms_error) /
    icc_numeric_n_per_level
icc_numeric_error_variance <- icc_numeric_components$ms_error
icc_numeric_value <- icc_numeric_between_variance /
  (icc_numeric_between_variance + icc_numeric_error_variance)

icc_numeric_quantities <- if (topic_locale == "de") {
  c(
    "Beobachtungen pro Stufe des Zufallsfaktors",
    "Mittlere Quadratsumme zwischen den Stufen, MSₐ",
    "Mittlere Quadratsumme innerhalb der Stufen, MSₑ",
    "Geschätzte Varianz zwischen den Stufen",
    "Geschätzte Fehlervarianz innerhalb der Stufen",
    "Geschätzte ICC"
  )
} else if (topic_locale == "sq") {
  c(
    "Vrojtimet për nivel të faktorit të rastësishëm",
    "Mesatarja e katrorëve ndërmjet niveleve, MSₐ",
    "Mesatarja e katrorëve brenda niveleve, MSₑ",
    "Varianca e vlerësuar ndërmjet niveleve",
    "Varianca e vlerësuar e gabimit brenda niveleve",
    "ICC e vlerësuar"
  )
} else {
  c(
    "Observations per random-factor level",
    "Between-level mean square, MSₐ",
    "Within-level mean square, MSₑ",
    "Estimated between-level variance",
    "Estimated within-level error variance",
    "Estimated ICC"
  )
}

icc_numeric_table <- tibble(
  quantity = icc_numeric_quantities,
  value = c(
    format_t08(icc_numeric_n_per_level, 0),
    format_t08(icc_numeric_components$ms_factor, 3),
    format_t08(icc_numeric_components$ms_error, 3),
    format_t08(icc_numeric_between_variance, 3),
    format_t08(icc_numeric_error_variance, 3),
    format_t08(icc_numeric_value, 3)
  )
)

p_icc_patterns <- ggplot(icc_pattern_data, aes(level, value, color = level)) +
  geom_point(
    aes(text = hover),
    position = position_jitter(width = 0.08, height = 0, seed = 4811),
    size = 2.5,
    alpha = 0.82
  ) +
  stat_summary(fun = mean, geom = "crossbar", width = 0.55, color = "#172B3A", linewidth = 0.65) +
  facet_wrap(vars(pattern), nrow = 1) +
  scale_color_manual(values = c("#315E7D", "#477C9D", "#6695B0", "#91B3C7", "#C05A47")) +
  labs(
    title = t08_text$icc_title,
    subtitle = t08_text$icc_subtitle,
    x = t08_text$random_level_axis,
    y = t08_text$constructed_outcome_axis,
    color = NULL
  ) +
  t08_theme(base_size = 11) +
  theme(legend.position = "none")

if (topic_locale %in% c("en", "de", "sq")) {
  p_icc_patterns <- p_icc_patterns +
    geom_text(
      data = tibble(
        pattern = factor(t08_text$icc_patterns[[2]], levels = t08_text$icc_patterns),
        level = factor("L1", levels = paste0("L", 1:5)),
        value = 65,
        label = paste0(
          if (topic_locale == "de") {
            "Durchgerechnetes Feld\nMSₐ = "
          } else if (topic_locale == "sq") {
            "Paneli i llogaritur\nMSₐ = "
          } else {
            "Worked panel\nMSₐ = "
          },
          format_t08(icc_numeric_components$ms_factor, 2),
          "\nMSₑ = ", format_t08(icc_numeric_components$ms_error, 2),
          "\nICC = ", format_t08(icc_numeric_value, 3)
        )
      ),
      aes(level, value, label = label),
      inherit.aes = FALSE,
      hjust = 0,
      vjust = 1,
      color = "#203A4F",
      fontface = "bold",
      lineheight = 1.0,
      size = 3.0
    ) +
    coord_cartesian(ylim = c(32, 70.5), clip = "off") +
    theme(panel.spacing.x = grid::unit(1.4, "lines"))
}

# A newly generated repeated-measures pattern. Lines identify the dependence
# created when the same person contributes at every occasion.
set.seed(4812)
repeated_n <- 12
repeated_person_effect <- rnorm(repeated_n, 0, 5)
repeated_data <- expand_grid(
  participant = factor(sprintf("P%02d", seq_len(repeated_n))),
  occasion = factor(t08_text$occasions, levels = t08_text$occasions)
) |>
  mutate(
    person_index = as.integer(participant),
    occasion_effect = setNames(c(0, 3, 5), t08_text$occasions)[as.character(occasion)],
    value = 55 + repeated_person_effect[person_index] + occasion_effect + rnorm(n(), 0, 2),
    hover = paste0(
      t08_hover_text$participant, participant,
      "<br>", t08_theory_hover$occasion, occasion,
      "<br>", t08_theory_hover$value, format_t08(value, 2)
    )
  )

p_repeated_design <- ggplot(
  repeated_data,
  aes(occasion, value, group = participant)
) +
  geom_line(color = "#6F91A8", alpha = 0.62, linewidth = 0.7) +
  geom_point(aes(text = hover), color = "#2F6F9F", alpha = 0.78, size = 1.8) +
  stat_summary(aes(group = 1), fun = mean, geom = "line", color = "#C05A47", linewidth = 1.25) +
  stat_summary(aes(group = 1), fun = mean, geom = "point", color = "#C05A47", size = 3) +
  labs(
    title = t08_text$repeated_title,
    subtitle = t08_text$repeated_subtitle,
    x = t08_text$occasion_axis,
    y = t08_text$constructed_outcome_axis
  ) +
  t08_theme()

# The same balanced repeated observations are analyzed with and without a
# person term. This exposes where stable person-to-person differences go.
repeated_with_person_model <- lm(value ~ occasion + participant, data = repeated_data)
repeated_without_person_model <- lm(value ~ occasion, data = repeated_data)
repeated_with_person_anova <- anova(repeated_with_person_model)
repeated_without_person_anova <- anova(repeated_without_person_model)

repeated_analysis_labels <- if (topic_locale == "de") {
  c("Personenterm aufgenommen", "Personenterm ignoriert")
} else if (topic_locale == "sq") {
  c("Termi i personit i përfshirë", "Termi i personit i shpërfillur")
} else {
  c("Person term included", "Person term ignored")
}

repeated_quantity_labels <- if (topic_locale == "de") {
  c(error_ms = "Mittlere Fehlerquadratsumme", f_value = "F-Quotient für den Messzeitpunkt")
} else if (topic_locale == "sq") {
  c(
    error_ms = "Mesatarja e katrorëve të gabimit",
    f_value = "Raporti F për rastin e matjes"
  )
} else {
  c(error_ms = "Error mean square", f_value = "F ratio for occasion")
}

repeated_model_comparison <- tibble(
  analysis = repeated_analysis_labels,
  occasion_ss = c(
    repeated_with_person_anova["occasion", "Sum Sq"],
    repeated_without_person_anova["occasion", "Sum Sq"]
  ),
  occasion_df = c(
    repeated_with_person_anova["occasion", "Df"],
    repeated_without_person_anova["occasion", "Df"]
  ),
  occasion_ms = occasion_ss / occasion_df,
  error_ss = c(
    repeated_with_person_anova["Residuals", "Sum Sq"],
    repeated_without_person_anova["Residuals", "Sum Sq"]
  ),
  error_df = c(
    repeated_with_person_anova["Residuals", "Df"],
    repeated_without_person_anova["Residuals", "Df"]
  ),
  error_ms = error_ss / error_df,
  f_value = occasion_ms / error_ms
)

repeated_model_comparison_plot_data <- repeated_model_comparison |>
  select(analysis, error_ms, f_value) |>
  pivot_longer(
    c(error_ms, f_value),
    names_to = "quantity",
    values_to = "value"
  ) |>
  mutate(
    quantity = factor(
      recode(quantity, !!!repeated_quantity_labels),
      levels = unname(
        repeated_quantity_labels[c("error_ms", "f_value")]
      )
    ),
    analysis = factor(
      analysis,
      levels = repeated_analysis_labels
    ),
    hover = paste0(
      t08_theory_hover$analysis, analysis,
      "<br>", t08_theory_hover$quantity, quantity,
      "<br>", t08_theory_hover$value, format_t08(value, 3)
    )
  )

p_repeated_person_term <- ggplot(
  repeated_model_comparison_plot_data,
  aes(analysis, value, fill = analysis, text = hover)
) +
  geom_col(width = 0.58) +
  geom_text(
    aes(label = format_t08(value, 2)),
    vjust = -0.35,
    color = "#203A4F",
    fontface = "bold",
    size = 3.2
  ) +
  facet_wrap(vars(quantity), nrow = 1, scales = "free_y") +
  scale_fill_manual(values = c("#2F6F9F", "#AAB6C0"), guide = "none") +
  scale_y_continuous(expand = expansion(mult = c(0, 0.16))) +
  labs(
    title = if (topic_locale == "de") {
      "Der Personenterm trennt stabile Ausgangsunterschiede vom Fehler"
    } else if (topic_locale == "sq") {
      "Termi i personit i ndan dallimet e qëndrueshme fillestare nga gabimi"
    } else {
      "The Person Term Separates Stable Baseline Differences from Error"
    },
    subtitle = if (topic_locale == "de") {
      paste0(
        "Die Quadratsumme des Messzeitpunkts bleibt gleich; der Nenner verändert sich, ",
        "wenn Unterschiede zwischen Personen dargestellt werden"
      )
    } else if (topic_locale == "sq") {
      paste0(
        "Shuma e katrorëve për rastin e matjes nuk ndryshon; emëruesi ndryshon ",
        "kur paraqiten dallimet mes personave"
      )
    } else {
      "The occasion sum of squares is unchanged; the denominator changes when person-to-person differences are represented"
    },
    x = NULL,
    y = NULL
  ) +
  t08_theme(base_size = 10.5) +
  theme(
    legend.position = "none",
    axis.text.x = element_text(angle = 12, hjust = 1),
    panel.spacing.x = grid::unit(1.6, "lines"),
    plot.margin = margin(14, 20, 18, 18)
  )

# Deterministic randomized balanced one-way teaching study.
set.seed(4808)
condition_levels <- t08_text$conditions
sim_n_per_level <- 40L
sim_n <- sim_n_per_level * length(condition_levels)
sim_assignment <- sample(rep(condition_levels, each = sim_n_per_level))
condition_means <- setNames(c(62, 65, 68, 71), condition_levels)

sim_data <- tibble(
  participant_id = sprintf("S%03d", seq_len(sim_n)),
  condition = factor(sim_assignment, levels = condition_levels),
  learning_score = round(
    pmin(
      pmax(rnorm(sim_n, mean = condition_means[sim_assignment], sd = 8), 0),
      100
    ),
    1
  )
)

sim_components <- one_way_components(sim_data$learning_score, sim_data$condition)
sim_model <- aov(learning_score ~ condition, data = sim_data)
sim_lm <- lm(learning_score ~ condition, data = sim_data)

sim_data <- sim_data |>
  mutate(
    fitted_score = unname(fitted(sim_lm)),
    residual = unname(resid(sim_lm)),
    standardized_residual = unname(rstandard(sim_lm)),
    hover = paste0(
      t08_hover_text$participant, participant_id,
      "<br>", t08_hover_text$condition, condition,
      "<br>", t08_hover_text$observed_score, format_t08(learning_score, 1),
      "<br>", t08_hover_text$group_fitted_mean, format_t08(fitted_score, 2),
      "<br>", t08_hover_text$residual, format_t08(residual, 2),
      "<br>", t08_hover_text$standardized_residual, format_t08(standardized_residual, 2)
    )
  )

sim_preview <- sim_data |>
  select(participant_id, condition, learning_score) |>
  slice_head(n = 12)

sim_group_summary <- sim_data |>
  group_by(condition) |>
  summarise(
    n = n(),
    mean = mean(learning_score),
    sd = sd(learning_score),
    minimum = min(learning_score),
    maximum = max(learning_score),
    .groups = "drop"
  ) |>
  mutate(across(c(mean, sd, minimum, maximum), ~ round(.x, 2)))

sim_ss_check <- tibble(
  quantity = t08_text$summary_quantities,
  value = c(
    sim_components$ss_total,
    sim_components$ss_factor,
    sim_components$ss_error,
    sim_components$ss_factor + sim_components$ss_error,
    sim_components$df_total,
    sim_components$df_factor + sim_components$df_error
  )
) |>
  mutate(value = round(value, 3))

sim_anova_table <- tibble(
  source = t08_text$anova_sources,
  ss = c(
    format_t08(sim_components$ss_factor, 3),
    format_t08(sim_components$ss_error, 3),
    format_t08(sim_components$ss_total, 3)
  ),
  df = c(
    as.character(sim_components$df_factor),
    as.character(sim_components$df_error),
    as.character(sim_components$df_total)
  ),
  ms = c(
    format_t08(sim_components$ms_factor, 3),
    format_t08(sim_components$ms_error, 3),
    ""
  ),
  f = c(format_t08(sim_components$f_value, 3), "", ""),
  p = c(format_p_t08(sim_components$p_value), "", "")
)

# Right-tail reference for the exact simulated omnibus result.
sim_f_tail_max <- max(
  qf(0.9995, sim_components$df_factor, sim_components$df_error),
  sim_components$f_value * 1.10
)
sim_f_tail_data <- tibble(
  x = seq(0, sim_f_tail_max, length.out = 1400),
  density = df(x, sim_components$df_factor, sim_components$df_error)
) |>
  mutate(
    in_p_value = x >= sim_components$f_value,
    hover = paste0(
      t08_hover_text$f_under_null, format_t08(x, 2),
      "<br>", t08_hover_text$density, format_t08(density, 4),
      "<br>", if_else(
        in_p_value,
        t08_hover_text$inside_p_tail,
        t08_hover_text$before_observed_f
      )
    )
  )

p_sim_f_tail_en <- ggplot(sim_f_tail_data, aes(x, density)) +
  annotate(
    "rect",
    xmin = sim_components$f_value,
    xmax = Inf,
    ymin = -Inf,
    ymax = Inf,
    fill = "#F7D7CD",
    alpha = 0.34
  ) +
  geom_area(
    data = sim_f_tail_data |> filter(in_p_value),
    aes(text = hover, group = 1),
    fill = "#C05A47",
    alpha = 0.82
  ) +
  geom_line(aes(text = hover, group = 1), color = "#244C69", linewidth = 0.95) +
  geom_vline(
    xintercept = sim_components$f_value,
    color = "#8A3F36",
    linetype = "dashed",
    linewidth = 0.9
  ) +
  scale_x_continuous(expand = expansion(mult = c(0, 0.02))) +
  scale_y_continuous(expand = expansion(mult = c(0, 0.06))) +
  coord_cartesian(clip = "off") +
  labs(
    title = anova_visual_text$tail_title,
    subtitle = paste0(
      anova_visual_text$tail_subtitle_prefix, sim_components$df_factor,
      anova_visual_text$tail_subtitle_middle, sim_components$df_error
    ),
    x = anova_visual_text$tail_x,
    y = anova_visual_text$density
  ) +
  t08_theme(base_size = 11) +
  theme(legend.position = "none", plot.margin = margin(12, 26, 12, 18))

tail_annotation_text <- paste0(
  anova_visual_text$observed_f, format_t08(sim_components$f_value, 3),
  "<br>",
  if (topic_locale == "de") {
    "p im rechten<br>Verteilungsschwanz "
  } else if (topic_locale == "sq") {
    "vlera p në bishtin<br>e djathtë "
  } else {
    "right-tail p "
  },
  gsub("<", "&lt;", format_p_t08(sim_components$p_value), fixed = TRUE)
)
attr(p_sim_f_tail_en, "t08_native_annotation") <- list(
  x = 0.97,
  y = 0.72,
  xref = "paper",
  yref = "paper",
  text = paste0("<b>", tail_annotation_text, "</b>"),
  showarrow = FALSE,
  xanchor = "right",
  yanchor = "middle",
  align = "left",
  bgcolor = "#FFF4EA",
  bordercolor = "#CFAE9C",
  borderwidth = 1,
  borderpad = 4,
  font = list(color = "#713D31", size = 11.5),
  captureevents = FALSE
)
attr(p_sim_f_tail_en, "t08_native_shapes") <- list(
  list(
    type = "rect",
    xref = "x",
    yref = "paper",
    x0 = sim_components$f_value,
    x1 = sim_f_tail_max,
    y0 = 0,
    y1 = 0.045,
    fillcolor = "rgba(192, 90, 71, 0.72)",
    line = list(width = 0),
    layer = "above"
  )
)
attr(p_sim_f_tail_en, "ratiomera_plotly_kind") <- "f_tail"
attr(p_sim_f_tail_en, "ratiomera_widget_height") <- 480

# One prespecified contrast: average of the three active routines versus the
# reference condition. Weights sum to zero; D / 3 has the direct mean-difference
# interpretation because the reference weight is -3.
planned_weights_vector <- c(-3, 1, 1, 1)
names(planned_weights_vector) <- condition_levels
sim_group_means <- sim_components$group_means[condition_levels]
planned_d <- sum(planned_weights_vector * sim_group_means)
planned_average_difference <- planned_d / 3
planned_ss <- planned_d^2 / sum(
  planned_weights_vector^2 / as.numeric(sim_components$group_n[condition_levels])
)
planned_f <- planned_ss / sim_components$ms_error
planned_p <- pf(planned_f, 1, sim_components$df_error, lower.tail = FALSE)

planned_contrast_table <- tibble(
  condition = condition_levels,
  mean = as.numeric(sim_group_means),
  weight = planned_weights_vector,
  weighted_mean = as.numeric(sim_group_means) * planned_weights_vector
) |>
  mutate(
    mean = round(mean, 3),
    weighted_mean = round(weighted_mean, 3)
  )

planned_result_table <- tibble(
  comparison = t08_text$planned_comparison,
  mean_difference = round(planned_average_difference, 3),
  contrast_ss = round(planned_ss, 3),
  numerator_df = 1L,
  denominator_df = sim_components$df_error,
  f = round(planned_f, 3),
  p = format_p_t08(planned_p)
)

sim_tukey <- as.data.frame(TukeyHSD(sim_model, "condition")$condition) |>
  rownames_to_column("comparison") |>
  as_tibble() |>
  transmute(
    comparison,
    mean_difference = round(diff, 3),
    lower_95 = round(lwr, 3),
    upper_95 = round(upr, 3),
    adjusted_p = if_else(`p adj` < 0.001, "< .001", sub("^0", "", sprintf("%.3f", `p adj`)))
  )

p_sim_groups <- ggplot(sim_data, aes(condition, learning_score, color = condition)) +
  geom_boxplot(
    width = 0.52,
    outlier.shape = NA,
    color = "#617483",
    fill = "white",
    linewidth = 0.55
  ) +
  geom_point(
    aes(text = hover),
    position = position_jitter(width = 0.14, height = 0, seed = 4809),
    alpha = 0.55,
    size = 1.8
  ) +
  stat_summary(
    fun = mean,
    geom = "point",
    shape = 23,
    size = 3.8,
    fill = "white",
    color = "#172B3A"
  ) +
  geom_hline(
    yintercept = sim_components$grand_mean,
    color = "#C05A47",
    linetype = "dashed",
    linewidth = 0.8
  ) +
  scale_x_discrete(
    labels = function(values) t08_wrap_axis_labels(values, width = 14L)
  ) +
  scale_color_manual(values = t08_palette) +
  coord_flip(clip = "off") +
  labs(
    title = t08_text$groups_title,
    subtitle = t08_text$groups_subtitle,
    x = t08_text$condition_axis,
    y = t08_text$learning_axis,
    color = NULL
  ) +
  t08_theme(base_size = 11) +
  theme(
    axis.text.y = element_text(
      angle = 0,
      hjust = 1,
      vjust = 0.5,
      size = 9.5,
      lineheight = 0.92
    ),
    legend.position = "none"
  )
attr(p_sim_groups, "ratiomera_plotly_kind") <- "groups"
attr(p_sim_groups, "ratiomera_widget_height") <- 520

ss_plot_data <- tibble(
  bar = factor(
    c(t08_text$ss_bars[[1]], t08_text$ss_bars[[2]], t08_text$ss_bars[[2]]),
    levels = t08_text$ss_bars
  ),
  component = factor(
    c(t08_text$ss_components[[1]], t08_text$ss_components[[2]], t08_text$ss_components[[3]]),
    levels = rev(t08_text$ss_components)
  ),
  value = c(
    sim_components$ss_total,
    sim_components$ss_factor,
    sim_components$ss_error
  )
) |>
  mutate(
    x_position = if_else(bar == t08_text$ss_bars[[1]], 1, 2),
    segment_lower = case_when(
      component == t08_text$ss_components[[3]] ~ sim_components$ss_factor,
      TRUE ~ 0
    ),
    segment_upper = case_when(
      component == t08_text$ss_components[[2]] ~ sim_components$ss_factor,
      TRUE ~ sim_components$ss_total
    ),
    label_y = (segment_lower + segment_upper) / 2,
    xmin = x_position - 0.29,
    xmax = x_position + 0.29,
    hover = paste0(
      as.character(component),
      "<br>", t08_hover_text$sum_of_squares, format_t08(value, 1)
    )
  )

p_sim_ss_partition <- ggplot(ss_plot_data) +
  # Explicit rectangle bounds prevent ggplotly from reversing the visual bar
  # stack while leaving the text coordinates in ggplot's original order.
  geom_rect(
    aes(
      xmin = xmin,
      xmax = xmax,
      ymin = segment_lower,
      ymax = segment_upper,
      fill = component,
      text = hover
    ),
    color = "white",
    linewidth = 0.6
  ) +
  geom_text(
    data = ss_plot_data |>
      filter(component == t08_text$ss_components[[1]]),
    aes(
      x = x_position,
      y = label_y,
      label = paste0(
        t08_wrap_axis_labels(as.character(component), width = 12L),
        "\n",
        format_t08(value, 1)
      )
    ),
    color = "white",
    fontface = "bold",
    lineheight = 0.95,
    size = 3.4
  ) +
  geom_text(
    data = ss_plot_data |>
      filter(component == t08_text$ss_components[[2]]),
    aes(
      x = x_position - 0.40,
      y = (segment_lower + segment_upper) / 2,
      label = paste0(
        as.character(component),
        "\n",
        format_t08(value, 1)
      )
    ),
    color = "#203A4F",
    hjust = 0,
    fontface = "bold",
    lineheight = 0.95,
    size = 3.1
  ) +
  geom_text(
    data = ss_plot_data |>
      filter(component == t08_text$ss_components[[3]]),
    aes(
      x = x_position + 0.40,
      y = (segment_lower + segment_upper) / 2,
      label = paste0(
        as.character(component),
        "\n",
        format_t08(value, 1)
      )
    ),
    color = "#203A4F",
    hjust = 0.5,
    fontface = "bold",
    lineheight = 0.95,
    size = 3.1
  ) +
  scale_x_continuous(
    breaks = c(1, 2),
    labels = t08_wrap_axis_labels(t08_text$ss_bars, width = 15L),
    expand = expansion(mult = c(0.18, 0.18))
  ) +
  scale_y_continuous(
    breaks = c(0, 6000, 12000),
    limits = c(0, 12000),
    expand = expansion(mult = c(0, 0))
  ) +
  scale_fill_manual(
    values = setNames(c("#527C99", "#2F6F9F", "#718494"), t08_text$ss_components)
  ) +
  coord_flip(clip = "off") +
  labs(
    title = t08_text$ss_title,
    subtitle = t08_text$ss_subtitle,
    x = NULL,
    y = t08_text$ss_axis,
    fill = NULL
  ) +
  t08_theme() +
  theme(
    legend.position = "none",
    axis.text.y = element_text(
      size = 9.2,
      lineheight = 0.92,
      hjust = 1
    )
  )
attr(p_sim_ss_partition, "ratiomera_plotly_kind") <- "ss_partition"
attr(p_sim_ss_partition, "ratiomera_widget_height") <- 500

diagnostic_residual <- tibble(
  panel = t08_text$diagnostic_panels[[1]],
  x = as.numeric(scale(sim_data$fitted_score)),
  y = sim_data$standardized_residual,
  participant_id = sim_data$participant_id,
  hover = paste0(
    t08_hover_text$participant, sim_data$participant_id,
    "<br>", t08_hover_text$standardized_fitted, format_t08(as.numeric(scale(sim_data$fitted_score)), 2),
    "<br>", t08_hover_text$standardized_residual, format_t08(sim_data$standardized_residual, 2)
  )
)
diagnostic_qq_order <- order(sim_data$standardized_residual)
diagnostic_qq <- tibble(
  panel = t08_text$diagnostic_panels[[2]],
  x = qnorm(ppoints(sim_n)),
  y = sim_data$standardized_residual[diagnostic_qq_order],
  participant_id = sim_data$participant_id[diagnostic_qq_order],
  hover = paste0(
    t08_hover_text$participant, sim_data$participant_id[diagnostic_qq_order],
    "<br>", t08_hover_text$expected_normal_quantile, format_t08(qnorm(ppoints(sim_n)), 2),
    "<br>", t08_hover_text$ordered_standardized_residual,
    format_t08(sim_data$standardized_residual[diagnostic_qq_order], 2)
  )
)
sim_diagnostic_data <- bind_rows(diagnostic_residual, diagnostic_qq) |>
  mutate(
    panel = factor(
      panel,
      levels = c(unique(diagnostic_residual$panel), unique(diagnostic_qq$panel))
    )
  )

p_sim_diagnostics <- ggplot(sim_diagnostic_data, aes(x, y)) +
  geom_point(aes(text = hover), color = "#2F6F9F", alpha = 0.65, size = 1.8) +
  geom_hline(
    data = tibble(
      panel = factor(unique(diagnostic_residual$panel), levels = levels(sim_diagnostic_data$panel)),
      yintercept = 0
    ),
    aes(yintercept = yintercept),
    color = "#C05A47",
    linewidth = 0.8
  ) +
  geom_abline(
    data = tibble(
      panel = factor(unique(diagnostic_qq$panel), levels = levels(sim_diagnostic_data$panel)),
      intercept = 0,
      slope = 1
    ),
    aes(intercept = intercept, slope = slope),
    color = "#C05A47",
    linewidth = 0.8
  ) +
  facet_wrap(
    vars(panel),
    ncol = 1,
    scales = "free_x",
    labeller = labeller(panel = label_wrap_gen(width = 28))
  ) +
  scale_x_continuous(breaks = c(-2, -1, 0, 1, 2)) +
  labs(
    title = t08_text$diagnostics_title,
    subtitle = t08_text$diagnostics_subtitle,
    x = NULL,
    y = t08_text$diagnostics_y
  ) +
  t08_theme(base_size = 10.5) +
  theme(
    panel.spacing.y = grid::unit(1.6, "lines"),
    strip.text = element_text(lineheight = 1.08),
    plot.margin = margin(14, 22, 12, 18)
  )
attr(p_sim_diagnostics, "ratiomera_plotly_kind") <- "diagnostics"
attr(p_sim_diagnostics, "ratiomera_widget_height") <- 700
attr(p_sim_diagnostics, "ratiomera_top_margin") <- 168
