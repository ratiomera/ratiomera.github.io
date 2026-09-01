# Shared data, calculations, and figure geometry for Topic 3.
# Each locale page sets topic_locale before sourcing this file. The simulated
# observations and every numerical result remain identical across locales.

if (!exists("topic_locale", inherits = FALSE)) topic_locale <- "en"
if (!topic_locale %in% c("en", "de", "sq")) {
  stop("Unsupported Topic 3 locale: ", topic_locale, call. = FALSE)
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
    "Topic 3 requires these R packages: ",
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

topic3_labels <- list(
  en = list(
    guided = "Guided planning",
    usual = "Usual study routine",
    before = "Before",
    after = "After",
    completed = "Completed",
    not_completed = "Not completed",
    sample = "Sample",
    population = "Population",
    statistic = "Sample statistic",
    sampling_distribution = "Sampling distribution",
    conclusion = "Careful population conclusion",
    lower_tail = "Lower tailed: H₁ says smaller",
    upper_tail = "Upper tailed: H₁ says larger",
    two_sided = "Two sided: H₁ says different",
    test_statistic = "Test statistic under H₀",
    standardized_test_statistic = "Standardized test statistic",
    density = "Density",
    observed_statistic = "Observed\nstatistic",
    h0_true = "When H₀ is true",
    h1_true = "When the selected H₁ is true",
    correct_non_rejection = "Correct non-rejection",
    type_i = "Type I error (α)",
    type_ii = "Type II error (β)",
    power = "Power (1 − β)",
    ci_covers = "Covers the parameter",
    ci_misses = "Misses the parameter",
    interval_center = "Interval center",
    normal = "Standard normal",
    df2 = "t, df = 2",
    df5 = "t, df = 5",
    df30 = "t, df = 30",
    design_one = "One sample",
    design_one_answer = "Compare one mean\nwith a reference value",
    design_independent = "Two independent groups",
    design_independent_answer = "Compare means from\ntwo separate groups",
    design_paired = "Paired observations",
    design_paired_answer = "Calculate one difference\nfor every pair",
    participant = "Participant ID",
    program = "Program",
    score_before = "Planning score before the program",
    score_after = "Planning score after the program",
    score_change = "Change in planning score",
    follow_through = "Completed the study plan",
    score = "Study planning score",
    sample_size = "Planned sample size",
    planned_power = "Power",
    outcome = "Study plan outcome",
    count = "Number of participants",
    observed = "Observed",
    expected = "Expected under independence"
  ),
  de = list(
    guided = "Angeleitete Planung",
    usual = "Übliche Lernroutine",
    before = "Vorher",
    after = "Nachher",
    completed = "Abgeschlossen",
    not_completed = "Nicht abgeschlossen",
    sample = "Stichprobe",
    population = "Grundgesamtheit",
    statistic = "Stichproben-\nkennwert",
    sampling_distribution = "Stichprobenverteilung",
    conclusion = "Sorgfältiger Schluss\nauf die Grundgesamtheit",
    lower_tail = "Linksseitig: H₁ besagt kleiner",
    upper_tail = "Rechtsseitig: H₁ besagt grösser",
    two_sided = "Zweiseitig: H₁ besagt verschieden",
    test_statistic = "Prüfgrösse unter H₀",
    standardized_test_statistic = "Standardisierte Prüfgrösse",
    density = "Dichte",
    observed_statistic = "Beobachtete\nPrüfgrösse",
    h0_true = "Wenn H₀ gilt",
    h1_true = "Wenn die gewählte H₁ gilt",
    correct_non_rejection = "Korrektes Nichtablehnen",
    type_i = "Fehler 1. Art (α)",
    type_ii = "Fehler 2. Art (β)",
    power = "Teststärke (1 − β)",
    ci_covers = "Überdeckt den Parameter",
    ci_misses = "Verfehlt den Parameter",
    interval_center = "Intervallmitte",
    normal = "Standardnormalverteilung",
    df2 = "t, df = 2",
    df5 = "t, df = 5",
    df30 = "t, df = 30",
    design_one = "Eine Stichprobe",
    design_one_answer = "Einen Mittelwert mit\neinem Referenzwert vergleichen",
    design_independent = "Zwei unabhängige Gruppen",
    design_independent_answer = "Mittelwerte von zwei\ngetrennten Gruppen vergleichen",
    design_paired = "Verbundene Beobachtungen",
    design_paired_answer = "Für jedes Paar eine\nDifferenz berechnen",
    participant = "Teilnehmenden-ID",
    program = "Programm",
    score_before = "Planungswert vor dem Programm",
    score_after = "Planungswert nach dem Programm",
    score_change = "Veränderung des Planungswerts",
    follow_through = "Studienplan abgeschlossen",
    score = "Studienplanungswert",
    sample_size = "Geplanter Stichprobenumfang",
    planned_power = "Teststärke",
    outcome = "Ergebnis des Studienplans",
    count = "Anzahl Personen",
    observed = "Beobachtet",
    expected = "Unter Unabhängigkeit erwartet"
  ),
  sq = list(
    guided = "Planifikimi i udhëzuar",
    usual = "Rutina e zakonshme e studimit",
    before = "Para",
    after = "Pas",
    completed = "I përfunduar",
    not_completed = "I papërfunduar",
    sample = "Kampioni",
    population = "Popullata",
    statistic = "Statistika e\nkampionit",
    sampling_distribution = "Shpërndarja e kampionimit",
    conclusion = "Përfundim i kujdesshëm\npër popullatën",
    lower_tail = "Majtas: H₁ thotë më e vogël",
    upper_tail = "Djathtas: H₁ thotë më e madhe",
    two_sided = "Dyanëshe: H₁ thotë e ndryshme",
    test_statistic = "Statistika e testit nën H₀",
    standardized_test_statistic = "Statistika e standardizuar e testit",
    density = "Dendësia",
    observed_statistic = "Statistika\ne vrojtuar",
    h0_true = "Kur H₀ është e vërtetë",
    h1_true = "Kur H₁ e zgjedhur është e vërtetë",
    correct_non_rejection = "Mosrefuzim i saktë",
    type_i = "Gabim i llojit I (α)",
    type_ii = "Gabim i llojit II (β)",
    power = "Fuqia (1 − β)",
    ci_covers = "E mbulon parametrin",
    ci_misses = "Nuk e mbulon parametrin",
    interval_center = "Qendra e intervalit",
    normal = "Normalja standarde",
    df2 = "t, df = 2",
    df5 = "t, df = 5",
    df30 = "t, df = 30",
    design_one = "Një kampion",
    design_one_answer = "Krahaso një mesatare\nme një vlerë reference",
    design_independent = "Dy grupe të pavarura",
    design_independent_answer = "Krahaso mesataret e\ndy grupeve të ndara",
    design_paired = "Vrojtimet e çiftuara",
    design_paired_answer = "Llogarit një diferencë\npër secilin çift",
    participant = "ID-ja e pjesëmarrësit",
    program = "Programi",
    score_before = "Pikëzimi i planifikimit para programit",
    score_after = "Pikëzimi i planifikimit pas programit",
    score_change = "Ndryshimi në pikëzimin e planifikimit",
    follow_through = "E përfundoi planin e studimit",
    score = "Pikëzimi i planifikimit të studimit",
    sample_size = "Madhësia e planifikuar e kampionit",
    planned_power = "Fuqia",
    outcome = "Rezultati i planit të studimit",
    count = "Numri i pjesëmarrësve",
    observed = "E vrojtuar",
    expected = "E pritshme nën pavarësi"
  )
)[[topic_locale]]

# Result-table labels are kept separate because the original helper predated
# full page-level localization. Every reviewed locale now has its own labels.
topic3_result_label_sets <- list(
  en = list(
    sample_size = "Sample size",
    sample_mean = "Sample mean",
    sample_sd = "Sample standard deviation",
    estimated_se = "Estimated standard error",
    t_statistic = "t statistic",
    degrees_freedom = "Degrees of freedom",
    two_sided_p = "Two sided p-value",
    ci_95 = "95% confidence interval",
    quantity = "Quantity",
    value = "Value",
    program = "Program",
    mean_change = "Mean change",
    sd_change = "SD of change",
    planned_n = "Planned sample size",
    power = "Power",
    rank = "Rank",
    outcome = "Outcome",
    observed = "Observed",
    expected = "Expected",
    contribution = "Contribution",
    question = "Question",
    procedure = "Procedure",
    statistic = "Statistic",
    p_value = "p-value",
    q_baseline = "Baseline mean versus 50",
    q_independent = "Guided versus usual mean change",
    q_paired = "Guided group before versus after",
    q_chi = "Program by plan completion",
    proc_one = "One-sample t-test",
    proc_independent = "Pooled independent-samples t-test",
    proc_paired = "Paired-samples t-test",
    proc_chi = "Chi-square independence test",
    chi_label = "chi-square = "
  ),
  de = list(
    sample_size = "Stichprobenumfang",
    sample_mean = "Stichprobenmittelwert",
    sample_sd = "Stichprobenstandardabweichung",
    estimated_se = "Geschätzter Standardfehler",
    t_statistic = "t-Teststatistik",
    degrees_freedom = "Freiheitsgrade",
    two_sided_p = "Zweiseitiger p-Wert",
    ci_95 = "95%-Konfidenzintervall",
    quantity = "Grösse",
    value = "Wert",
    program = "Programm",
    mean_change = "Mittlere Veränderung",
    sd_change = "SD der Veränderung",
    planned_n = "Geplanter Stichprobenumfang",
    power = "Teststärke",
    rank = "Rang",
    outcome = "Ergebnis",
    observed = "Beobachtet",
    expected = "Erwartet",
    contribution = "Beitrag",
    question = "Frage",
    procedure = "Verfahren",
    statistic = "Teststatistik",
    p_value = "p-Wert",
    q_baseline = "Ausgangsmittelwert gegen 50",
    q_independent = "Mittlere Veränderung: angeleitet gegen üblich",
    q_paired = "Angeleitete Gruppe: vorher gegen nachher",
    q_chi = "Programm nach Abschluss des Lernplans",
    proc_one = "t-Test für eine Stichprobe",
    proc_independent = "Gepoolter t-Test für unabhängige Stichproben",
    proc_paired = "t-Test für verbundene Stichproben",
    proc_chi = "Chi-Quadrat-Unabhängigkeitstest",
    chi_label = "Chi-Quadrat = "
  ),
  sq = list(
    sample_size = "Madhësia e kampionit",
    sample_mean = "Mesatarja e kampionit",
    sample_sd = "Devijimi standard i kampionit",
    estimated_se = "Gabimi standard i vlerësuar",
    t_statistic = "Statistika t",
    degrees_freedom = "Shkallët e lirisë",
    two_sided_p = "Vlera p dyanëshe",
    ci_95 = "Intervali i besimit 95%",
    quantity = "Madhësia",
    value = "Vlera",
    program = "Programi",
    mean_change = "Ndryshimi mesatar",
    sd_change = "Devijimi standard i ndryshimit",
    planned_n = "Madhësia e planifikuar e kampionit",
    power = "Fuqia statistikore",
    rank = "Rangu",
    outcome = "Rezultati",
    observed = "E vrojtuar",
    expected = "E pritshme",
    contribution = "Kontributi",
    question = "Pyetja",
    procedure = "Procedura",
    statistic = "Statistika",
    p_value = "Vlera p",
    q_baseline = "Mesatarja fillestare kundrejt 50",
    q_independent = "Ndryshimi mesatar: planifikimi i udhëzuar kundrejt rutinës së zakonshme",
    q_paired = "Grupi i udhëzuar: para kundrejt pas",
    q_chi = "Programi sipas përfundimit të planit",
    proc_one = "Testi t për një kampion",
    proc_independent = "Testi t me variancë të përbashkët për kampione të pavarura",
    proc_paired = "Testi t për kampione të çiftuara",
    proc_chi = "Testi hi-katror i pavarësisë",
    chi_label = "Hi-katror = "
  )
)
topic3_result_labels <- topic3_result_label_sets[[topic_locale]]
if (is.null(topic3_result_labels)) {
  topic3_result_labels <- topic3_result_label_sets$en
}

topic3_theme <- function(base_size = 12) {
  theme_minimal(base_size = base_size) +
    theme(
      axis.title = element_text(color = "#34495E"),
      axis.text = element_text(color = "#465A6B"),
      strip.text = element_text(face = "bold", color = "#203A4F"),
      panel.grid.minor = element_blank(),
      panel.grid.major = element_line(color = "#E7ECF1"),
      legend.position = "bottom",
      plot.background = element_rect(fill = "white", color = NA)
    )
}

# Convert Theory and Simulated Example plots into responsive, inspectable
# figures while preserving shared calculations and geometry across locales.
topic3_plotly <- function(plot, alt_text, tooltip = c("x", "y")) {
  plotly_height <- attr(plot, "topic3_plotly_height", exact = TRUE)
  legend_below <- isTRUE(attr(plot, "topic3_legend_below", exact = TRUE))
  plot <- ratiomera_make_plotly_compatible(plot)
  widget <- ggplotly(
    plot,
    tooltip = tooltip,
    dynamicTicks = FALSE
  ) |>
    ratiomera_prepare_plotly_widget(
      title_width = 40,
      # The German categorical-outcome axis needs two short lines at phone
      # width; the same limit is harmless for the parallel EN and SQ labels.
      axis_width = 22,
      annotation_width = 30
    )

  widget <- ratiomera_localize_plotly_hover(
    widget,
    ratiomera_plotly_hover_labels(plot, topic_locale)
  )
  widget <- ratiomera_suppress_box_trace_hover(widget)

  # Long translated legend entries need to wrap inside a phone-width widget.
  # Only the displayed trace name changes; grouping, data, and hover content
  # remain untouched and therefore identical across locales.
  widget$x$data <- lapply(widget$x$data, function(trace) {
    if (!is.null(trace$name) && nzchar(trace$name)) {
      trace$name <- ratiomera_wrap_plotly_text(trace$name, width = 24)
    }
    trace
  })

  widget <- widget |>
    layout(
      autosize = TRUE,
      hovermode = "closest",
      margin = list(l = 76, r = 28, b = 82, t = 78, pad = 2)
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
    widget$height <- as.numeric(plotly_height)
    widget$sizingPolicy$defaultHeight <- as.numeric(plotly_height)
  }

  if (legend_below) {
    widget <- widget |>
      layout(
        margin = list(l = 76, r = 28, b = 132, t = 78, pad = 2),
        legend = list(
          orientation = "v",
          x = 0.5,
          xanchor = "center",
          y = -0.18,
          yanchor = "top"
        )
      )
  }

  widget
}

topic3_hover <- if (topic_locale == "de") {
  list(
    p_region = "Teil der zweiseitigen p-Wert-Fläche",
    center_region = "Zwischen den beobachteten Referenzlinien",
    confidence_interval = "95%-Konfidenzintervall",
    reference = "Referenzwert",
    group_mean = "Gruppenmittelwert"
  )
} else if (topic_locale == "sq") {
  list(
    p_region = "Pjesë e sipërfaqes dyanëshe të vlerës p",
    center_region = "Midis vijave të referencës së statistikës së vrojtuar",
    confidence_interval = "Intervali i besimit 95%",
    reference = "Vlera e referencës",
    group_mean = "Mesatarja e grupit"
  )
} else {
  list(
    p_region = "Included in the two-sided p-value area",
    center_region = "Between the observed-statistic reference lines",
    confidence_interval = "95% confidence interval",
    reference = "Reference value",
    group_mean = "Group mean"
  )
}

format_p <- function(p) {
  if (p < 0.001) "< .001" else paste0("= ", formatC(p, format = "f", digits = 3))
}

# Theory figures -----------------------------------------------------------

bridge_nodes <- tibble(
  x = 1:4,
  y = 1,
  label = c(
    topic3_labels$population,
    topic3_labels$sample,
    topic3_labels$statistic,
    topic3_labels$conclusion
  )
)

p_inference_bridge <- ggplot(bridge_nodes, aes(x, y)) +
  annotate(
    "segment",
    x = c(1.35, 2.35, 3.35),
    xend = c(1.65, 2.65, 3.65),
    y = 1,
    yend = 1,
    linewidth = 0.8,
    color = "#59758A",
    arrow = grid::arrow(length = grid::unit(0.13, "inches"), type = "closed")
  ) +
  geom_label(
    aes(label = label),
    size = 3.5,
    fontface = "bold",
    fill = "#EEF4F8",
    color = "#173B57",
    linewidth = 0.35,
    label.padding = grid::unit(0.28, "lines")
  ) +
  annotate(
    "label",
    x = 2.5,
    y = 0.43,
    label = topic3_labels$sampling_distribution,
    size = 3.3,
    fill = "#FFF4E8",
    color = "#7A4518",
    linewidth = 0.3
  ) +
  annotate(
    "segment",
    x = 2.5,
    xend = 2.5,
    y = 0.69,
    yend = 0.83,
    color = "#9A6538",
    arrow = grid::arrow(length = grid::unit(0.1, "inches"), type = "closed")
  ) +
  coord_cartesian(xlim = c(0.62, 4.38), ylim = c(0.18, 1.35), clip = "off") +
  theme_void(base_size = 12) +
  theme(plot.margin = margin(12, 20, 12, 20))

# Conceptual bridge from an estimate to a standardized test statistic. The
# small values are intentionally transparent and are not study data.
test_statistic_process_text <- if (topic_locale == "de") {
  list(
    nodes = c(
      "Beobachtete Schätzung\nStichprobenmittelwert = 54",
      "Abstand zu H₀\n54 − 50 = 4 Punkte",
      "Abstand in\nStandardfehler-Einheiten\n4 ÷ 2 = 2",
      "2 in der\nNullverteilung einordnen"
    ),
    formula = "Prüfgrösse = (Schätzung − Nullwert) ÷ Standardfehler = 2",
    title = "Eine Prüfgrösse überführt eine Rohdifferenz auf eine gemeinsame Skala",
    subtitle = "Das Beispiel vergleicht einen Stichprobenmittelwert von 54 mit dem Nullwert 50 bei einem Standardfehler von 2"
  )
} else if (topic_locale == "sq") {
  list(
    nodes = c(
      "Vlerësimi i vrojtuar\nmesatarja e kampionit = 54",
      "Largësia nga H₀\n54 − 50 = 4 pikë",
      "Shprehe largësinë\nnë njësi të gabimit standard\n4 ÷ 2 = 2",
      "Vendose 2 në shpërndarjen\nnën hipotezën zero"
    ),
    formula = "statistika e testit = (vlerësimi − vlera nën H₀) ÷ gabimi standard = 2",
    title = "Statistika e testit e shndërron një diferencë fillestare në një shkallë të përbashkët",
    subtitle = "Shembulli krahason mesataren 54 të kampionit me vlerën 50 të hipotezës zero, duke përdorur gabimin standard 2"
  )
} else {
  list(
    nodes = c(
      "Observed estimate\nsample mean = 54",
      "Distance from H₀\n54 − 50 = 4 points",
      "Express the distance\nin standard-error units\n4 ÷ 2 = 2",
      "Locate 2 in the\nnull distribution"
    ),
    formula = "test statistic = (estimate − null value) ÷ standard error = 2",
    title = "A Test Statistic Turns a Raw Difference into a Common Scale",
    subtitle = "The example compares a sample mean of 54 with a null value of 50 using a standard error of 2"
  )
}

test_statistic_nodes <- tibble(
  x = 1:4,
  y = 1,
  label = test_statistic_process_text$nodes,
  step = c("1", "2", "3", "4")
)

test_statistic_arrows <- tibble(
  x = c(1.35, 2.35, 3.35),
  xend = c(1.65, 2.65, 3.65),
  y = 1,
  yend = 1
)

p_test_statistic_process <- ggplot() +
  geom_segment(
    data = test_statistic_arrows,
    aes(x, y, xend = xend, yend = yend),
    color = "#7B92A3",
    linewidth = 0.9,
    arrow = grid::arrow(length = grid::unit(0.14, "cm"), type = "closed")
  ) +
  geom_label(
    data = test_statistic_nodes,
    aes(x, y, label = label),
    fill = "#F4F8FA",
    color = "#203A4F",
    fontface = "bold",
    size = 3.05,
    lineheight = 0.95,
    linewidth = 0.35,
    label.padding = grid::unit(0.24, "lines")
  ) +
  geom_label(
    data = test_statistic_nodes,
    aes(x, y = 1.55, label = step),
    fill = "#2E6DA4",
    color = "white",
    fontface = "bold",
    size = 3.2,
    linewidth = 0,
    label.padding = grid::unit(0.15, "lines")
  ) +
  annotate(
    "label",
    x = 2.5,
    y = 0.33,
    label = test_statistic_process_text$formula,
    fill = "#FFF4EA",
    color = "#713D31",
    fontface = "bold",
    size = 3.25,
    linewidth = 0.3
  ) +
  coord_cartesian(xlim = c(0.55, 4.45), ylim = c(0.05, 1.78), clip = "off") +
  labs(
    title = test_statistic_process_text$title,
    subtitle = test_statistic_process_text$subtitle
  ) +
  theme_void(base_size = 11) +
  theme(
    plot.title = element_text(face = "bold", color = "#172B3A"),
    plot.subtitle = element_text(color = "#536475"),
    plot.background = element_rect(fill = "white", color = NA),
    panel.background = element_rect(fill = "white", color = NA),
    plot.margin = margin(14, 22, 14, 22)
  )

tail_x <- seq(-3.8, 3.8, length.out = 700)
tail_panels <- c(
  topic3_labels$lower_tail,
  topic3_labels$upper_tail,
  topic3_labels$two_sided
)
tail_curve <- bind_rows(lapply(tail_panels, function(panel_name) {
  tibble(panel = panel_name, x = tail_x, density = dnorm(tail_x))
})) |>
  mutate(
    panel = factor(panel, levels = tail_panels),
    shaded = case_when(
      panel == topic3_labels$lower_tail ~ x <= qnorm(0.05),
      panel == topic3_labels$upper_tail ~ x >= qnorm(0.95),
      TRUE ~ abs(x) >= qnorm(0.975)
    ),
    tail_segment = case_when(
      !shaded ~ NA_character_,
      x < 0 ~ "left",
      TRUE ~ "right"
    )
  )

tail_critical <- tibble(
  panel = factor(
    c(
      topic3_labels$lower_tail,
      topic3_labels$upper_tail,
      topic3_labels$two_sided,
      topic3_labels$two_sided
    ),
    levels = tail_panels
  ),
  x = c(qnorm(0.05), qnorm(0.95), -qnorm(0.975), qnorm(0.975))
)

p_tail_regions <- ggplot(tail_curve, aes(x, density)) +
  geom_area(
    data = filter(tail_curve, shaded),
    aes(group = interaction(panel, tail_segment, drop = TRUE)),
    fill = "#C65D3E",
    alpha = 0.78
  ) +
  geom_line(linewidth = 0.7, color = "#244C69") +
  geom_vline(
    data = tail_critical,
    aes(xintercept = x),
    linetype = "dashed",
    linewidth = 0.55,
    color = "#8F3F2B"
  ) +
  facet_wrap(~panel, nrow = 1) +
  scale_x_continuous(breaks = c(-3, 0, 3)) +
  labs(x = topic3_labels$test_statistic, y = topic3_labels$density) +
  topic3_theme(11) +
  theme(legend.position = "none")

pvalue_observed <- 2.10
pvalue_curve <- tibble(
  x = tail_x,
  density = dnorm(tail_x),
  shaded = abs(tail_x) >= pvalue_observed,
  tail_segment = if_else(x < 0, "left", "right")
)

p_pvalue <- ggplot(pvalue_curve, aes(x, density)) +
  geom_area(
    data = filter(pvalue_curve, shaded),
    aes(group = tail_segment),
    fill = "#C65D3E",
    alpha = 0.8
  ) +
  geom_line(linewidth = 0.8, color = "#244C69") +
  geom_vline(
    xintercept = c(-pvalue_observed, pvalue_observed),
    linetype = "dashed",
    linewidth = 0.6,
    color = "#8F3F2B"
  ) +
  annotate(
    "text",
    x = pvalue_observed,
    y = 0.19,
    label = topic3_labels$observed_statistic,
    hjust = 0.5,
    size = 3.3,
    color = "#713321"
  ) +
  coord_cartesian(xlim = c(-3.8, 3.8), ylim = c(0, 0.43), clip = "off") +
  labs(x = topic3_labels$test_statistic, y = topic3_labels$density) +
  topic3_theme(11) +
  theme(legend.position = "none")

power_x <- seq(-3.8, 6.2, length.out = 900)
power_critical <- qnorm(0.95)
power_true_effect <- 2.50
power_panels <- c(topic3_labels$h0_true, topic3_labels$h1_true)
power_curve <- bind_rows(
  tibble(
    panel = topic3_labels$h0_true,
    x = power_x,
    density = dnorm(power_x, 0, 1),
    region = if_else(
      power_x > power_critical,
      topic3_labels$type_i,
      topic3_labels$correct_non_rejection
    )
  ),
  tibble(
    panel = topic3_labels$h1_true,
    x = power_x,
    density = dnorm(power_x, power_true_effect, 1),
    region = if_else(
      power_x > power_critical,
      topic3_labels$power,
      topic3_labels$type_ii
    )
  )
) |>
  mutate(
    panel = factor(panel, levels = power_panels),
    region = factor(
      region,
      levels = c(
        topic3_labels$correct_non_rejection,
        topic3_labels$type_i,
        topic3_labels$type_ii,
        topic3_labels$power
      )
    )
  )

p_power_decisions <- ggplot(power_curve, aes(x, density, fill = region)) +
  geom_area(alpha = 0.82) +
  geom_line(linewidth = 0.65, color = "#244C69") +
  geom_vline(
    xintercept = power_critical,
    linetype = "dashed",
    color = "#172B3A",
    linewidth = 0.6
  ) +
  facet_wrap(~panel, nrow = 1) +
  scale_fill_manual(
    values = c("#DCEAF2", "#C65D3E", "#E9B76A", "#2F7E6E"),
    drop = FALSE
  ) +
  labs(
    x = topic3_labels$standardized_test_statistic,
    y = topic3_labels$density,
    fill = NULL
  ) +
  topic3_theme(11)

set.seed(3007)
ci_population_mean <- 50
ci_standard_error <- 2
ci_repetitions <- 30
ci_centers <- ci_population_mean + rnorm(ci_repetitions) * ci_standard_error
ci_examples <- tibble(
  sample = 1:ci_repetitions,
  estimate = ci_centers,
  lower = ci_centers - qnorm(0.975) * ci_standard_error,
  upper = ci_centers + qnorm(0.975) * ci_standard_error
) |>
  mutate(
    coverage = if_else(
      lower <= ci_population_mean & upper >= ci_population_mean,
      topic3_labels$ci_covers,
      topic3_labels$ci_misses
    ),
    coverage = factor(
      coverage,
      levels = c(topic3_labels$ci_covers, topic3_labels$ci_misses)
    )
  )

p_ci_coverage <- ggplot(ci_examples, aes(y = sample, color = coverage)) +
  geom_segment(
    aes(x = lower, xend = upper, yend = sample),
    linewidth = 0.8
  ) +
  geom_point(aes(x = estimate), size = 1.7) +
  geom_vline(
    xintercept = ci_population_mean,
    linetype = "dashed",
    linewidth = 0.65,
    color = "#172B3A"
  ) +
  scale_color_manual(values = c("#2F6F9F", "#C65D3E")) +
  scale_y_continuous(breaks = seq(5, ci_repetitions, by = 5)) +
  labs(
    x = topic3_labels$interval_center,
    y = topic3_labels$sample,
    color = NULL
  ) +
  topic3_theme(11)

t_x <- seq(-4, 4, length.out = 650)
t_shapes <- bind_rows(
  tibble(x = t_x, density = dnorm(t_x), distribution = topic3_labels$normal),
  tibble(x = t_x, density = dt(t_x, 2), distribution = topic3_labels$df2),
  tibble(x = t_x, density = dt(t_x, 5), distribution = topic3_labels$df5),
  tibble(x = t_x, density = dt(t_x, 30), distribution = topic3_labels$df30)
) |>
  mutate(
    distribution = factor(
      distribution,
      levels = c(
        topic3_labels$normal,
        topic3_labels$df2,
        topic3_labels$df5,
        topic3_labels$df30
      )
    )
  )

p_t_shapes <- ggplot(t_shapes, aes(x, density, color = distribution)) +
  geom_line(linewidth = 0.85) +
  scale_color_manual(values = c("#172B3A", "#C65D3E", "#D69937", "#2F7E6E")) +
  labs(
    x = topic3_labels$test_statistic,
    y = topic3_labels$density,
    color = NULL
  ) +
  topic3_theme(11)

design_map <- tibble(
  y = c(3, 2, 1),
  design = c(
    topic3_labels$design_one,
    topic3_labels$design_independent,
    topic3_labels$design_paired
  ),
  answer = c(
    topic3_labels$design_one_answer,
    topic3_labels$design_independent_answer,
    topic3_labels$design_paired_answer
  )
)

p_design_map <- ggplot(design_map, aes(y = y)) +
  geom_label(
    aes(x = 1, label = design),
    size = 3.4,
    fontface = "bold",
    fill = "#EEF4F8",
    color = "#173B57",
    linewidth = 0.3,
    label.padding = grid::unit(0.25, "lines")
  ) +
  geom_segment(
    aes(x = 1.42, xend = 2.58, yend = y),
    color = "#59758A",
    linewidth = 0.75,
    arrow = grid::arrow(length = grid::unit(0.12, "inches"), type = "closed")
  ) +
  geom_label(
    aes(x = 3, label = answer),
    size = 3.2,
    fill = "#FFF4E8",
    color = "#6E421F",
    linewidth = 0.3,
    label.padding = grid::unit(0.24, "lines")
  ) +
  coord_cartesian(xlim = c(0.42, 3.58), ylim = c(0.52, 3.48), clip = "off") +
  theme_void(base_size = 12) +
  theme(plot.margin = margin(12, 22, 12, 22))

# Deterministic Ratiomera study ----------------------------------------------

set.seed(3042)
n_total <- 160
study_dat <- tibble(
  id = 1:n_total,
  program_code = sample(rep(c("usual", "guided"), each = n_total / 2)),
  baseline_score = round(rnorm(n_total, mean = 50, sd = 10), 1)
) |>
  mutate(
    followup_score = round(
      baseline_score +
        if_else(program_code == "guided", 4, 1) +
        rnorm(n_total, mean = 0, sd = 6),
      1
    ),
    change_score = round(followup_score - baseline_score, 1),
    completion = rbinom(
      n_total,
      size = 1,
      prob = if_else(program_code == "guided", 0.72, 0.43)
    ),
    program = factor(
      if_else(
        program_code == "guided",
        topic3_labels$guided,
        topic3_labels$usual
      ),
      levels = c(topic3_labels$usual, topic3_labels$guided)
    ),
    completion_label = if_else(
      completion == 1,
      topic3_labels$completed,
      topic3_labels$not_completed
    )
  )

display_dat <- study_dat |>
  transmute(
    !!topic3_labels$participant := id,
    !!topic3_labels$program := program,
    !!topic3_labels$score_before := baseline_score,
    !!topic3_labels$score_after := followup_score,
    !!topic3_labels$score_change := change_score,
    !!topic3_labels$follow_through := completion_label
  )

# One-sample baseline test and confidence interval.
baseline_reference <- 50
baseline_n <- nrow(study_dat)
baseline_mean <- mean(study_dat$baseline_score)
baseline_sd <- sd(study_dat$baseline_score)
baseline_se <- baseline_sd / sqrt(baseline_n)
baseline_df <- baseline_n - 1
baseline_t <- (baseline_mean - baseline_reference) / baseline_se
baseline_p <- 2 * pt(-abs(baseline_t), df = baseline_df)
baseline_critical <- qt(0.975, df = baseline_df)
baseline_ci <- baseline_mean + c(-1, 1) * baseline_critical * baseline_se

baseline_summary_tbl <- tibble(
  quantity = c(
    topic3_result_labels$sample_size,
    topic3_result_labels$sample_mean,
    topic3_result_labels$sample_sd,
    topic3_result_labels$estimated_se,
    topic3_result_labels$t_statistic,
    topic3_result_labels$degrees_freedom,
    topic3_result_labels$two_sided_p,
    topic3_result_labels$ci_95
  ),
  value = c(
    as.character(baseline_n),
    formatC(baseline_mean, format = "f", digits = 2),
    formatC(baseline_sd, format = "f", digits = 2),
    formatC(baseline_se, format = "f", digits = 2),
    formatC(baseline_t, format = "f", digits = 2),
    as.character(baseline_df),
    formatC(baseline_p, format = "f", digits = 3),
    paste0(
      "[",
      formatC(baseline_ci[1], format = "f", digits = 2),
      ", ",
      formatC(baseline_ci[2], format = "f", digits = 2),
      "]"
    )
  )
) |>
  setNames(c(topic3_result_labels$quantity, topic3_result_labels$value))

baseline_interval_dat <- tibble(
  mean = baseline_mean,
  lower = baseline_ci[1],
  upper = baseline_ci[2],
  hover_text = paste0(
    topic3_result_labels$sample_mean,
    ": ",
    formatC(baseline_mean, format = "f", digits = 2),
    "<br>",
    topic3_hover$confidence_interval,
    ": [",
    formatC(baseline_ci[1], format = "f", digits = 2),
    ", ",
    formatC(baseline_ci[2], format = "f", digits = 2),
    "]<br>",
    topic3_hover$reference,
    ": ",
    baseline_reference
  )
)

p_baseline_interval <- ggplot(
  baseline_interval_dat,
  aes(x = mean, y = 1, text = hover_text)
) +
  geom_vline(
    xintercept = baseline_reference,
    linetype = "dashed",
    linewidth = 0.7,
    color = "#C65D3E"
  ) +
  geom_segment(
    aes(x = lower, xend = upper, y = 1, yend = 1),
    linewidth = 1.2,
    color = "#2F6F9F"
  ) +
  geom_point(size = 3.2, color = "#173B57") +
  annotate(
    "text",
    x = baseline_reference,
    y = 1.22,
    label = "50",
    color = "#8F3F2B",
    fontface = "bold",
    size = 3.4
  ) +
  scale_y_continuous(NULL, breaks = NULL) +
  coord_cartesian(
    xlim = range(c(baseline_ci, baseline_reference)) + c(-1.2, 1.2),
    ylim = c(0.72, 1.3),
    clip = "off"
  ) +
  labs(x = topic3_labels$score, y = NULL) +
  topic3_theme(11) +
  theme(panel.grid.major.y = element_blank(), legend.position = "none")

baseline_null_x <- seq(-4, 4, length.out = 700)
baseline_null_dat <- tibble(
  x = baseline_null_x,
  density = dt(baseline_null_x, df = baseline_df),
  p_region = abs(baseline_null_x) >= abs(baseline_t),
  tail_segment = if_else(baseline_null_x < 0, "left", "right")
) |>
  mutate(
    hover_text = paste0(
      topic3_labels$standardized_test_statistic,
      ": ",
      formatC(x, format = "f", digits = 2),
      "<br>",
      topic3_labels$density,
      ": ",
      formatC(density, format = "f", digits = 3),
      "<br>",
      if_else(p_region, topic3_hover$p_region, topic3_hover$center_region)
    )
  )

p_baseline_null <- ggplot(baseline_null_dat, aes(x, density, text = hover_text, group = 1)) +
  geom_area(
    data = filter(baseline_null_dat, p_region),
    aes(group = tail_segment),
    fill = "#E9B76A",
    alpha = 0.72
  ) +
  geom_line(color = "#244C69", linewidth = 0.8) +
  geom_vline(
    xintercept = c(-abs(baseline_t), abs(baseline_t)),
    linetype = "dashed",
    color = "#8F3F2B",
    linewidth = 0.55
  ) +
  labs(x = topic3_labels$test_statistic, y = topic3_labels$density) +
  topic3_theme(11) +
  theme(legend.position = "none")

# Pooled independent-samples t calculation for change scores.
guided_change <- study_dat$change_score[study_dat$program_code == "guided"]
usual_change <- study_dat$change_score[study_dat$program_code == "usual"]
guided_n <- length(guided_change)
usual_n <- length(usual_change)
guided_mean <- mean(guided_change)
usual_mean <- mean(usual_change)
guided_sd <- sd(guided_change)
usual_sd <- sd(usual_change)
pooled_df <- guided_n + usual_n - 2
pooled_variance <- (
  (guided_n - 1) * guided_sd^2 +
    (usual_n - 1) * usual_sd^2
) / pooled_df
pooled_sd <- sqrt(pooled_variance)
change_difference <- guided_mean - usual_mean
change_se <- pooled_sd * sqrt(1 / guided_n + 1 / usual_n)
change_t <- change_difference / change_se
change_p <- 2 * pt(-abs(change_t), df = pooled_df)
change_critical <- qt(0.975, df = pooled_df)
change_ci <- change_difference + c(-1, 1) * change_critical * change_se

change_group_tbl <- tibble(
  program = c(topic3_labels$guided, topic3_labels$usual),
  sample_size = c(guided_n, usual_n),
  mean_change = round(c(guided_mean, usual_mean), 2),
  sd_change = round(c(guided_sd, usual_sd), 2)
) |>
  setNames(c(
    topic3_result_labels$program,
    topic3_result_labels$sample_size,
    topic3_result_labels$mean_change,
    topic3_result_labels$sd_change
  ))

p_group_change <- ggplot(
  study_dat,
  aes(x = program, y = change_score, fill = program, color = program)
) +
  geom_boxplot(width = 0.54, alpha = 0.23, outlier.shape = NA, linewidth = 0.65) +
  suppressWarnings(geom_jitter(
    aes(
      text = paste0(
        topic3_labels$participant,
        ": ",
        id,
        "<br>",
        topic3_labels$program,
        ": ",
        program,
        "<br>",
        topic3_labels$score_change,
        ": ",
        formatC(change_score, format = "f", digits = 1)
      )
    ),
    width = 0.13,
    height = 0,
    alpha = 0.58,
    size = 1.45
  )) +
  scale_fill_manual(
    values = setNames(
      c("#8BAFC7", "#E2A26C"),
      c(topic3_labels$usual, topic3_labels$guided)
    )
  ) +
  scale_color_manual(
    values = setNames(
      c("#2F6F9F", "#A64A33"),
      c(topic3_labels$usual, topic3_labels$guided)
    )
  ) +
  scale_x_discrete(
    labels = function(values) vapply(
      values,
      function(value) paste(strwrap(value, width = 16), collapse = "\n"),
      character(1)
    )
  ) +
  geom_hline(yintercept = 0, linetype = "dashed", color = "#566A78") +
  labs(x = topic3_labels$program, y = topic3_labels$score_change) +
  topic3_theme(11) +
  theme(legend.position = "none")

# Paired comparison within the guided group.
guided_dat <- study_dat |>
  filter(program_code == "guided")
paired_difference <- guided_dat$followup_score - guided_dat$baseline_score
paired_n <- length(paired_difference)
paired_mean <- mean(paired_difference)
paired_sd <- sd(paired_difference)
paired_se <- paired_sd / sqrt(paired_n)
paired_df <- paired_n - 1
paired_t <- paired_mean / paired_se
paired_p <- 2 * pt(-abs(paired_t), df = paired_df)
paired_critical <- qt(0.975, df = paired_df)
paired_ci <- paired_mean + c(-1, 1) * paired_critical * paired_se

paired_long <- bind_rows(
  guided_dat |>
    transmute(id, time = topic3_labels$before, score = baseline_score),
  guided_dat |>
    transmute(id, time = topic3_labels$after, score = followup_score)
) |>
  mutate(
    time = factor(time, levels = c(topic3_labels$before, topic3_labels$after)),
    hover_text = paste0(
      topic3_labels$participant,
      ": ",
      id,
      "<br>",
      as.character(time),
      "<br>",
      topic3_labels$score,
      ": ",
      formatC(score, format = "f", digits = 1)
    )
  )

paired_means <- paired_long |>
  group_by(time) |>
  summarize(score = mean(score), .groups = "drop")

p_paired_change <- ggplot(paired_long, aes(time, score, group = id)) +
  suppressWarnings(geom_line(aes(text = hover_text), color = "#7B98AA", alpha = 0.23, linewidth = 0.45)) +
  suppressWarnings(geom_point(aes(text = hover_text), color = "#55778C", alpha = 0.33, size = 1.1)) +
  geom_line(
    data = paired_means,
    aes(time, score, group = 1),
    color = "#A64A33",
    linewidth = 1.3
  ) +
  geom_point(
    data = paired_means,
    aes(time, score),
    inherit.aes = FALSE,
    color = "#7D321F",
    fill = "white",
    shape = 21,
    stroke = 1,
    size = 3.1
  ) +
  labs(x = NULL, y = topic3_labels$score) +
  topic3_theme(11) +
  theme(legend.position = "none")

# Source-supported one-sided z power-planning model.
planning_alpha <- 0.05
planning_delta <- 0.40
planning_n <- 5:160
planning_power <- 1 - pnorm(
  qnorm(1 - planning_alpha) - sqrt(planning_n) * planning_delta
)
power_plan_dat <- tibble(n = planning_n, power = planning_power) |>
  mutate(
    hover_text = paste0(
      topic3_labels$sample_size,
      ": ",
      n,
      "<br>",
      topic3_labels$planned_power,
      ": ",
      formatC(100 * power, format = "f", digits = 1),
      "%"
    )
  )
power_plan_points <- tibble(n = c(20, 40, 80, 160)) |>
  mutate(
    power = 1 - pnorm(qnorm(1 - planning_alpha) - sqrt(n) * planning_delta),
    hover_text = paste0(
      topic3_labels$sample_size,
      ": ",
      n,
      "<br>",
      topic3_labels$planned_power,
      ": ",
      formatC(100 * power, format = "f", digits = 1),
      "%"
    ),
    # Keep the labels inside the plotting panel. The largest planned sample
    # sits on the right boundary, while the two nearly-100% values need their
    # labels below rather than above the points.
    label_n = if_else(n == max(n), n - 10, n),
    label_hjust = 0.50,
    label_y = if_else(n >= 80, power - 0.065, power + 0.065)
  )

p_power_curve <- ggplot(power_plan_dat, aes(n, power, text = hover_text, group = 1)) +
  geom_hline(
    yintercept = 0.80,
    linetype = "dashed",
    linewidth = 0.6,
    color = "#9A6538"
  ) +
  geom_line(color = "#2F6F9F", linewidth = 1) +
  geom_point(data = power_plan_points, size = 2.4, color = "#A64A33") +
  geom_text(
    data = power_plan_points,
    aes(
      x = label_n,
      y = label_y,
      label = formatC(power, format = "f", digits = 2),
      hjust = label_hjust
    ),
    size = 3.1,
    color = "#713321"
  ) +
  scale_y_continuous(
    limits = c(0, 1.03),
    breaks = seq(0, 1, by = 0.2),
    labels = function(x) paste0(round(100 * x), "%")
  ) +
  scale_x_continuous(breaks = c(20, 40, 80, 120, 160)) +
  labs(x = topic3_labels$sample_size, y = topic3_labels$planned_power) +
  topic3_theme(11) +
  theme(legend.position = "none")

power_plan_tbl <- power_plan_points |>
  transmute(sample_size = n, power = round(power, 3)) |>
  setNames(c(topic3_result_labels$planned_n, topic3_result_labels$power))

# Rank illustration using six cases from each group.
rank_subset <- bind_rows(
  study_dat |> filter(program_code == "guided") |> slice_head(n = 6),
  study_dat |> filter(program_code == "usual") |> slice_head(n = 6)
) |>
  arrange(id) |>
  mutate(rank = rank(change_score, ties.method = "average")) |>
  transmute(
    !!topic3_labels$participant := id,
    !!topic3_labels$program := program,
    !!topic3_labels$score_change := change_score,
    !!topic3_result_labels$rank := rank
  )

# Chi-square test of program and completion.
completion_factor <- factor(
  study_dat$completion,
  levels = c(1, 0),
  labels = c(topic3_labels$completed, topic3_labels$not_completed)
)
program_factor <- factor(
  study_dat$program_code,
  levels = c("guided", "usual"),
  labels = c(topic3_labels$guided, topic3_labels$usual)
)
completion_table <- table(program_factor, completion_factor)
chi_result <- suppressWarnings(chisq.test(completion_table, correct = FALSE))
chi_statistic <- unname(chi_result$statistic)
chi_df <- unname(chi_result$parameter)
chi_p <- chi_result$p.value
chi_expected <- unclass(chi_result$expected)
chi_contribution <- (unclass(completion_table) - chi_expected)^2 / chi_expected

chi_cell_tbl <- as.data.frame(completion_table, stringsAsFactors = FALSE) |>
  rename(program = program_factor, outcome = completion_factor, observed = Freq) |>
  mutate(
    expected = as.vector(chi_expected),
    contribution = as.vector(chi_contribution),
    expected = round(expected, 2),
    contribution = round(contribution, 3)
  ) |>
  setNames(c(
    topic3_result_labels$program,
    topic3_result_labels$outcome,
    topic3_result_labels$observed,
    topic3_result_labels$expected,
    topic3_result_labels$contribution
  ))

chi_plot_dat <- bind_rows(
  as.data.frame(completion_table, stringsAsFactors = FALSE) |>
    transmute(
      program = program_factor,
      outcome = completion_factor,
      count = Freq,
      count_type = topic3_labels$observed
    ),
  as.data.frame(as.table(chi_expected), stringsAsFactors = FALSE) |>
    transmute(
      program = program_factor,
      outcome = completion_factor,
      count = Freq,
      count_type = topic3_labels$expected
    )
) |>
  mutate(
    program = factor(
      program,
      levels = c(topic3_labels$guided, topic3_labels$usual)
    ),
    outcome = factor(
      outcome,
      levels = c(topic3_labels$completed, topic3_labels$not_completed)
    ),
    count_type = factor(
      count_type,
      levels = c(topic3_labels$observed, topic3_labels$expected)
    ),
    count_label = if_else(
      count_type == topic3_labels$observed,
      as.character(round(count)),
      formatC(count, format = "f", digits = 1)
    ),
    hover_text = paste0(
      topic3_labels$program,
      ": ",
      program,
      "<br>",
      topic3_labels$outcome,
      ": ",
      outcome,
      "<br>",
      as.character(count_type),
      ": ",
      count_label
    )
  )

p_chi_counts <- ggplot(
  chi_plot_dat,
  aes(x = count, y = outcome, fill = count_type, text = hover_text)
) +
  geom_col(position = position_dodge(width = 0.76), width = 0.68) +
  geom_text(
    aes(label = count_label),
    position = position_dodge(width = 0.76),
    hjust = -0.35,
    size = 3.1,
    color = "#243847"
  ) +
  facet_wrap(~program, ncol = 1, labeller = label_wrap_gen(width = 22)) +
  scale_y_discrete(
    limits = rev(levels(chi_plot_dat$outcome)),
    labels = function(values) vapply(
      values,
      function(value) paste(strwrap(value, width = 16), collapse = "\n"),
      character(1)
    )
  ) +
  scale_fill_manual(values = c("#2F6F9F", "#D9B073")) +
  scale_x_continuous(expand = expansion(mult = c(0, 0.20))) +
  labs(
    x = topic3_labels$count,
    y = NULL,
    fill = NULL
  ) +
  topic3_theme(11) +
  theme(legend.position = "bottom")

attr(p_chi_counts, "topic3_plotly_height") <- 640
attr(p_chi_counts, "topic3_legend_below") <- TRUE

analysis_results_tbl <- tibble(
  question = c(
    topic3_result_labels$q_baseline,
    topic3_result_labels$q_independent,
    topic3_result_labels$q_paired,
    topic3_result_labels$q_chi
  ),
  procedure = c(
    topic3_result_labels$proc_one,
    topic3_result_labels$proc_independent,
    topic3_result_labels$proc_paired,
    topic3_result_labels$proc_chi
  ),
  statistic = c(
    paste0("t = ", formatC(baseline_t, format = "f", digits = 2)),
    paste0("t = ", formatC(change_t, format = "f", digits = 2)),
    paste0("t = ", formatC(paired_t, format = "f", digits = 2)),
    paste0(topic3_result_labels$chi_label, formatC(chi_statistic, format = "f", digits = 2))
  ),
  df = c(baseline_df, pooled_df, paired_df, chi_df),
  p_value = c(
    format_p(baseline_p),
    format_p(change_p),
    format_p(paired_p),
    format_p(chi_p)
  )
) |>
  setNames(c(
    topic3_result_labels$question,
    topic3_result_labels$procedure,
    topic3_result_labels$statistic,
    "df",
    topic3_result_labels$p_value
  ))
