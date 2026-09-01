# Shared deterministic data, calculations, tables, and figure geometry for
# Multiple Regression, Topic 7.

if (!exists("topic_locale", inherits = FALSE)) topic_locale <- "en"

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

topic7_label_sets <- list(
  en = list(
    independent = "Independent study",
    peer = "Peer workshop",
    guided = "Guided lab",
    prior = "Prior reasoning score",
    practice = "Weekly guided practice (hours)",
    outcome = "Statistical reasoning score",
    fitted = "Fitted reasoning score",
    residual = "Residual (observed minus fitted)",
    observed = "Observed reasoning score",
    reference_format_slope = "reference-format slope"
  ),
  de = list(
    independent = "Selbststudium",
    peer = "Peer-Workshop",
    guided = "Begleitetes Lernlabor",
    prior = "Punktwert im statistischen Vorwissen",
    practice = "Wöchentliche begleitete Übung (Stunden)",
    outcome = "Punktwert im statistischen Denken",
    fitted = "Angepasster Punktwert im statistischen Denken",
    residual = "Residuum (beobachtet minus angepasst)",
    observed = "Beobachteter Punktwert im statistischen Denken",
    reference_format_slope = "Steigung im Referenzformat"
  ),
  sq = list(
    independent = "Studim i pavarur",
    peer = "Punëtori në grup",
    guided = "Laborator i udhëhequr",
    prior = "Pikët paraprake të arsyetimit",
    practice = "Ushtrimi javor i udhëhequr (orë)",
    outcome = "Pikët e arsyetimit statistikor",
    fitted = "Pikët e përshtatura të arsyetimit",
    residual = "Reziduali (vlera e vëzhguar minus vlera e përshtatur)",
    observed = "Pikët e vëzhguara të arsyetimit",
    reference_format_slope = "pjerrësia në formatin referues"
  )
)

if (!topic_locale %in% names(topic7_label_sets)) {
  stop(
    "Topic 7 labels have not yet been reviewed for locale: ",
    topic_locale,
    call. = FALSE
  )
}
topic7_labels <- topic7_label_sets[[topic_locale]]

topic7_text_sets <- list(
  en = list(
    model_descriptions = c(
      M0 = "Intercept only",
      M1 = "Practice hours",
      M2 = "Prior score + practice hours",
      M3 = "M2 + tutorial-format indicators",
      M4 = "M3 + practice-by-format interactions"
    ),
    term_labels = c(
      "Intercept",
      "Peer workshop minus independent study at 0 practice hours",
      "Guided lab minus independent study at 0 practice hours",
      "Practice slope difference: peer minus independent",
      "Practice slope difference: guided minus independent"
    ),
    nested_labels = c("M3: additive format model", "M4: format interactions added"),
    semipartial_quantities = c(
      "Bivariate r: practice hours with reasoning score",
      "r: prior score with practice hours",
      "Semipartial r: practice hours after prior score",
      "Squared semipartial correlation",
      "Increment in R-squared from adding practice hours"
    ),
    variable_names = c(
      "Statistical reasoning score",
      "Prior reasoning score",
      "Weekly guided practice",
      "Tutorial format"
    ),
    variable_roles = c(
      "Quantitative outcome", "Quantitative predictor",
      "Quantitative predictor", "Categorical predictor"
    ),
    variable_measurements = c(
      "Points on a constructed assessment",
      "Points on a constructed baseline assessment",
      "Hours per week",
      "Independent study, peer workshop, or guided lab"
    ),
    dummy_interpretations = c(
      "Reference category",
      "Peer coefficient is included",
      "Guided coefficient is included"
    ),
    reference_prefix = "Reference: ",
    profile_components = c("Starting value", "Prior-score contribution", "Practice-hours contribution"),
    profile_title = "Predictor Contributions Build Each Fitted Value",
    profile_subtitle = "Four profiles change one predictor at a time",
    profile_axis = "Contribution to the fitted reasoning score",
    profile_prefix = "Profile ",
    fitted_total_prefix = "Fitted = ",
    dummy_title = "A Dummy Variable Adds a Group Difference to the Same Practice Slope",
    dummy_subtitle = "Constructed additive model: independent study is the reference category",
    dummy_group_difference = "Guided minus independent = 6 points",
    interaction_concept_title = "Interactions Allow Different Slopes",
    interaction_concept_subtitle = "Constructed predictions use the same reference group and the same practice scale",
    surface_prior_annotation = "Prior score held at 10",
    surface_practice_annotation = "Practice held at 6 hours",
    surface_fill = "Fitted\nreasoning score",
    surface_title = "Two Predictors Form One Fitted Surface",
    surface_subtitle = "Contour lines join predictor profiles with the same fitted score",
    prior_score_prefix = "Prior score = ",
    conditional_change_prefix = "Conditional change = ",
    conditional_title = "A Conditional Coefficient Holds the Other Predictor Fixed",
    conditional_subtitle = "The practice slope is read along one prior-score line, not between different lines",
    coefficient_patterns = c(
      "Little change",
      "Shrinkage, possible confounding",
      "Growth, possible suppression"
    ),
    before_adjustment = "Before adjustment",
    after_adjustment = "After adjustment",
    coefficient_title = "Coefficient Changes Are Clues, Not Diagnoses",
    coefficient_subtitle = "Schematic values show three possible directions after adjustment",
    illustrative_coefficient = "Illustrative coefficient",
    residual_prefix = ": residual = ",
    fitted_title = "Each Row Produces a Fitted Value and a Residual",
    fitted_subtitle = "The dashed diagonal marks observed = fitted; one residual is highlighted",
    diagnostic_residual_title = "Residuals Should Form an Unstructured Band Around Zero",
    diagnostic_residual_subtitle = "M4 residuals against fitted scores; the horizontal line marks zero",
    diagnostic_qq_title = "A Q-Q Plot Compares Residuals With a Normal Reference",
    diagnostic_qq_subtitle = "Points close to the diagonal are broadly compatible with a normal error shape",
    expected_normal_quantile = "Expected quantile from a normal distribution",
    standardized_residual = "Standardized residual",
    practice_residual_prefix = "Practice residual: ",
    reasoning_score_prefix = "\nReasoning score: ",
    semipartial_title = "Semipartial Correlation Isolates One Predictor's Increment",
    semipartial_subtitle_prefix = "Practice residualized on prior score; raw outcome retained, sr = ",
    semipartial_x = "Practice-hours residual after prior score",
    additive_model = "Additive: parallel slopes",
    interaction_model = "Interaction: conditional slopes",
    interaction_title = "Interactions Allow Different Practice Slopes",
    interaction_subtitle = "Predictions hold prior reasoning score fixed at 10",
    reference_title = "Reference Choice Changes Coefficients, Not Predictions",
    reference_subtitle = "Only the emphasized reference line changes",
    r_squared = "R²",
    adjusted_r_squared = "Adjusted R²",
    fit_title = "Fit Improves as the Prespecified Model Sequence Expands",
    fit_subtitle = "Adjusted R² applies a penalty for additional predictor parameters",
    candidate_model = "Candidate model",
    outcome_share = "Share of outcome variation",
    fit_legend_title = "Model fit measure"
  ),
  de = list(
    model_descriptions = c(
      M0 = "Nur Achsenabschnitt",
      M1 = "Übungsstunden",
      M2 = "Vorwissenswert + Übungsstunden",
      M3 = "M2 + Indikatoren für das Lernformat",
      M4 = "M3 + Interaktionen zwischen Übung und Format"
    ),
    term_labels = c(
      "Achsenabschnitt",
      "Peer-Workshop minus Selbststudium bei 0 Übungsstunden",
      "Begleitetes Lernlabor minus Selbststudium bei 0 Übungsstunden",
      "Differenz der Übungssteigung: Peer minus Selbststudium",
      "Differenz der Übungssteigung: Lernlabor minus Selbststudium"
    ),
    nested_labels = c("M3: additives Formatmodell", "M4: Formatinteraktionen hinzugefügt"),
    semipartial_quantities = c(
      "Bivariates r: Übungsstunden mit Punktwert im statistischen Denken",
      "r: Vorwissenswert mit Übungsstunden",
      "Semipartielles r: Übungsstunden nach dem Vorwissenswert",
      "Quadrierte semipartielle Korrelation",
      "Zuwachs von R-Quadrat durch Hinzufügen der Übungsstunden"
    ),
    variable_names = c(
      "Punktwert im statistischen Denken",
      "Punktwert im statistischen Vorwissen",
      "Wöchentliche begleitete Übung",
      "Lernformat"
    ),
    variable_roles = c(
      "Quantitative Zielvariable", "Quantitativer Prädiktor",
      "Quantitativer Prädiktor", "Kategorialer Prädiktor"
    ),
    variable_measurements = c(
      "Punkte in einer konstruierten Beurteilung",
      "Punkte in einer konstruierten Ausgangsbeurteilung",
      "Stunden pro Woche",
      "Selbststudium, Peer-Workshop oder begleitetes Lernlabor"
    ),
    dummy_interpretations = c(
      "Referenzkategorie",
      "Peer-Koeffizient wird einbezogen",
      "Lernlabor-Koeffizient wird einbezogen"
    ),
    reference_prefix = "Referenz: ",
    profile_components = c("Ausgangswert", "Beitrag des Vorwissenswerts", "Beitrag der Übungsstunden"),
    profile_title = "Prädiktorbeiträge bilden jeden angepassten Wert",
    profile_subtitle = "Vier Profile verändern jeweils einen Prädiktor",
    profile_axis = "Beitrag zum angepassten Punktwert im statistischen Denken",
    profile_prefix = "Profil ",
    fitted_total_prefix = "Angepasst = ",
    dummy_title = "Eine Dummy-Variable ergänzt dieselbe Übungssteigung um eine Gruppendifferenz",
    dummy_subtitle = "Konstruiertes additives Modell: Selbststudium ist die Referenzkategorie",
    dummy_group_difference = "Lernlabor minus Selbststudium = 6 Punkte",
    interaction_concept_title = "Interaktionen erlauben unterschiedliche Steigungen",
    interaction_concept_subtitle = "Konstruierte Vorhersagen verwenden dieselbe Referenzgruppe und dieselbe Übungsskala",
    surface_prior_annotation = "Vorwissenswert bei 10 festgehalten",
    surface_practice_annotation = "Übung bei 6 Stunden festgehalten",
    surface_fill = "Angepasster\nPunktwert",
    surface_title = "Zwei Prädiktoren bilden eine gemeinsame angepasste Fläche",
    surface_subtitle = "Konturlinien verbinden Prädiktorprofile mit demselben angepassten Punktwert",
    prior_score_prefix = "Vorwissenswert = ",
    conditional_change_prefix = "Bedingte Veränderung = ",
    conditional_title = "Ein bedingter Koeffizient hält den anderen Prädiktor konstant",
    conditional_subtitle = "Die Übungssteigung wird innerhalb einer Vorwissenslinie gelesen",
    coefficient_patterns = c(
      "Geringe Veränderung",
      "Abnahme, mögliche Konfundierung",
      "Zunahme, mögliche Suppression"
    ),
    before_adjustment = "Vor der Bereinigung",
    after_adjustment = "Nach der Bereinigung",
    coefficient_title = "Koeffizientenänderungen richtig deuten",
    coefficient_subtitle = "Drei Richtungen sind Hinweise, keine Diagnosen",
    illustrative_coefficient = "Veranschaulichender Koeffizient",
    residual_prefix = ": Residuum = ",
    fitted_title = "Jede Zeile ergibt einen angepassten Wert und ein Residuum",
    fitted_subtitle = "Die Diagonale zeigt beobachtet = angepasst; ein Residuum ist markiert",
    diagnostic_residual_title = "Residuen sollten ein ungeordnetes Band um null bilden",
    diagnostic_residual_subtitle = "M4-Residuen gegen angepasste Punktwerte; die horizontale Linie markiert null",
    diagnostic_qq_title = "Ein Q-Q-Diagramm vergleicht Residuen mit einer Normalverteilung",
    diagnostic_qq_subtitle = "Punkte nahe der Diagonale sind mit einer annähernd normalen Fehlerform vereinbar",
    expected_normal_quantile = "Erwartetes Quantil einer Normalverteilung",
    standardized_residual = "Standardisiertes Residuum",
    practice_residual_prefix = "Übungsresiduum: ",
    reasoning_score_prefix = "\nPunktwert im statistischen Denken: ",
    semipartial_title = "Die semipartielle Korrelation isoliert den Zuwachs eines Prädiktors",
    semipartial_subtitle_prefix = "Übung um den Vorwissenswert residualisiert; rohe Zielvariable beibehalten, sr = ",
    semipartial_x = "Residuum der Übungsstunden nach dem Vorwissenswert",
    additive_model = "Additiv: parallele Steigungen",
    interaction_model = "Interaktion: bedingte Steigungen",
    interaction_title = "Interaktionen erlauben unterschiedliche Übungssteigungen",
    interaction_subtitle = "Die Vorhersagen halten den Vorwissenswert bei 10 fest",
    reference_title = "Die Referenzwahl ändert Koeffizienten, nicht Vorhersagen",
    reference_subtitle = "Nur die hervorgehobene Referenzlinie wechselt",
    r_squared = "R²",
    adjusted_r_squared = "Korrigiertes R²",
    fit_title = "Modellgüte entlang der vorab festgelegten Modellfolge",
    fit_subtitle = "Korrigiertes R² berücksichtigt zusätzliche Parameter",
    candidate_model = "Kandidatenmodell",
    outcome_share = "Anteil der Variation der Zielvariable",
    fit_legend_title = "Kennzahl der Modellanpassung"
  ),
  sq = list(
    model_descriptions = c(
      M0 = "Vetëm prerja",
      M1 = "Orët e ushtrimit",
      M2 = "Pikët paraprake + orët e ushtrimit",
      M3 = "M2 + treguesit e formatit të mësimit",
      M4 = "M3 + ndërveprimet ushtrim-sipas-formatit"
    ),
    term_labels = c(
      "Prerja",
      "Punëtoria me bashkëmoshatarë minus studimi i pavarur në 0 orë ushtrim",
      "Laboratori i udhëhequr minus studimi i pavarur në 0 orë ushtrim",
      "Dallimi në pjerrësinë e ushtrimit: punëtori minus studim i pavarur",
      "Dallimi në pjerrësinë e ushtrimit: laborator minus studim i pavarur"
    ),
    nested_labels = c(
      "M3: modeli aditiv i formatit",
      "M4: ndërveprimet e formatit të shtuara"
    ),
    semipartial_quantities = c(
      "r me dy ndryshore: orët e ushtrimit me pikët e arsyetimit",
      "r: pikët paraprake me orët e ushtrimit",
      "r gjysmëpartial: orët e ushtrimit pas pikëve paraprake",
      "Korrelacioni gjysmëpartial në katror",
      "Rritja e R-katrorit nga shtimi i orëve të ushtrimit"
    ),
    variable_names = c(
      "Pikët e arsyetimit statistikor",
      "Pikët paraprake të arsyetimit",
      "Ushtrimi javor i udhëhequr",
      "Formati i mësimit"
    ),
    variable_roles = c(
      "Ndryshore sasiore e rezultatit", "Ndryshore parashikuese sasiore",
      "Ndryshore parashikuese sasiore", "Ndryshore parashikuese kategorike"
    ),
    variable_measurements = c(
      "Pikë në një vlerësim të krijuar",
      "Pikë në një vlerësim fillestar të krijuar",
      "Orë në javë",
      "Studim i pavarur, punëtori me bashkëmoshatarë ose laborator i udhëhequr"
    ),
    dummy_interpretations = c(
      "Kategoria referuese",
      "Përfshihet koeficienti i punëtorisë",
      "Përfshihet koeficienti i laboratorit"
    ),
    reference_prefix = "Ref.: ",
    profile_components = c("Vlera fillestare", "Kontributi i pikëve paraprake", "Kontributi i orëve të ushtrimit"),
    profile_title = "Kontributet parashikuese formojnë çdo vlerë të përshtatur",
    profile_subtitle = "Katër profile ndryshojnë nga një parashikues",
    profile_axis = "Kontributi në pikët e përshtatura të arsyetimit",
    profile_prefix = "Profili ",
    fitted_total_prefix = "E përshtatur = ",
    dummy_title = "Një ndryshore treguese i shton një dallim grupi të njëjtës pjerrësi të ushtrimit",
    dummy_subtitle = "Model aditiv i krijuar: studimi i pavarur është kategoria referuese",
    dummy_group_difference = "Laboratori minus studimi i pavarur = 6 pikë",
    interaction_concept_title = "Ndërveprimet lejojnë pjerrësi të ndryshme",
    interaction_concept_subtitle = "Parashikimet e krijuara përdorin të njëjtin grup referues dhe të njëjtën shkallë ushtrimi",
    surface_prior_annotation = "Pikët paraprake mbahen në 10",
    surface_practice_annotation = "Ushtrimi mbahet në 6 orë",
    surface_fill = "Pikët e përshtatura\ntë arsyetimit",
    surface_title = "Dy ndryshore parashikuese formojnë një sipërfaqe të përshtatur",
    surface_subtitle = "Vijat e kontureve lidhin profile parashikuese me të njëjtin rezultat të përshtatur",
    prior_score_prefix = "Pikët paraprake = ",
    conditional_change_prefix = "Ndryshimi i kushtëzuar = ",
    conditional_title = "Koeficienti i kushtëzuar e mban tjetrën të pandryshuar",
    conditional_subtitle = "Pjerrësia lexohet brenda një vije të pikëve paraprake",
    coefficient_patterns = c(
      "Pak ndryshim",
      "Zvogëlim, ngatërrim i mundshëm",
      "Rritje, shtypje e mundshme"
    ),
    before_adjustment = "Para përshtatjes",
    after_adjustment = "Pas përshtatjes",
    coefficient_title = "Ndryshimi i koeficientit është shenjë, jo diagnozë",
    coefficient_subtitle = "Tri drejtime skematike pas përshtatjes",
    illustrative_coefficient = "Koeficient ilustrues",
    residual_prefix = ": reziduali = ",
    fitted_title = "Secili rresht jep një vlerë të përshtatur dhe një rezidual",
    fitted_subtitle = "Diagonalja e ndërprerë shënon vëzhguar = përshtatur; një rezidual është theksuar",
    diagnostic_residual_title = "Rezidualet duhet të formojnë një brez pa strukturë rreth zeros",
    diagnostic_residual_subtitle = "Rezidualet e M4 kundrejt pikëve të përshtatura; vija horizontale shënon zeron",
    diagnostic_qq_title = "Grafiku Q-Q i krahason rezidualet me një referencë normale",
    diagnostic_qq_subtitle = "Pikat afër diagonales përputhen gjerësisht me një formë normale të gabimeve",
    expected_normal_quantile = "Kuantili i pritur nga një shpërndarje normale",
    standardized_residual = "Reziduali i standardizuar",
    practice_residual_prefix = "Reziduali i ushtrimit: ",
    reasoning_score_prefix = "\nPikët e arsyetimit: ",
    semipartial_title = "Korrelacioni gjysmëpartial izolon kontributin unik",
    semipartial_subtitle_prefix = "Ushtrimi përshtatet për pikët paraprake; sr = ",
    semipartial_x = "Reziduali i orëve të ushtrimit pas pikëve paraprake",
    additive_model = "Aditiv: pjerrësi paralele",
    interaction_model = "Ndërveprim: pjerrësi të kushtëzuara",
    interaction_title = "Ndërveprimet lejojnë pjerrësi të ndryshme të ushtrimit",
    interaction_subtitle = "Parashikimet i mbajnë pikët paraprake të arsyetimit në 10",
    reference_title = "Referenca ndryshon koeficientët, jo parashikimet",
    reference_subtitle = "Ndryshon vetëm vija e theksuar e referencës",
    r_squared = "R²",
    adjusted_r_squared = "R² i përshtatur",
    fit_title = "Përshtatja përmirësohet me zgjerimin e modelit",
    fit_subtitle = "R² i përshtatur zbaton një dënim për parametra shtesë parashikues",
    candidate_model = "Modeli kandidat",
    outcome_share = "Pjesa e ndryshueshmërisë së rezultatit",
    fit_legend_title = "Masa e përshtatjes së modelit"
  )
)

topic7_text <- topic7_text_sets[[topic_locale]]

# Hover labels are kept with the shared data so every interactive simulated-
# example figure uses the page language. Albanian and German are provided
# explicitly; English remains the fallback for the canonical English path.
topic7_hover_text <- if (topic_locale == "sq") {
  list(
    participant = "Pjesëmarrësi: ",
    tutorial_format = "Formati i mësimit: ",
    prior_score = "Pikët paraprake: ",
    practice_hours = "Orët e ushtrimit: ",
    observed_score = "Pikët e vëzhguara: ",
    fitted_score = "Pikët e përshtatura: ",
    residual = "Reziduali: ",
    expected_normal_quantile = "Kuantili normal i pritur: ",
    standardized_residual = "Reziduali i standardizuar: ",
    model = "Modeli: ",
    prior_score_held = "Pikët paraprake mbahen në: ",
    displayed_reference = "Referenca e paraqitur: ",
    fitted_line = "Vija e përshtatur: ",
    measure = "Masa: ",
    value = "Vlera: ",
    profile = "Profili: ",
    component = "Pjesa e ekuacionit: ",
    contribution = "Kontributi: "
  )
} else if (topic_locale == "de") {
  list(
    participant = "Teilnehmenden-ID: ",
    tutorial_format = "Lernformat: ",
    prior_score = "Vorwissenswert: ",
    practice_hours = "Übungsstunden: ",
    observed_score = "Beobachteter Punktwert: ",
    fitted_score = "Angepasster Punktwert: ",
    residual = "Residuum: ",
    expected_normal_quantile = "Erwartetes Normalquantil: ",
    standardized_residual = "Standardisiertes Residuum: ",
    model = "Modell: ",
    prior_score_held = "Konstant gehaltener Vorwissenswert: ",
    displayed_reference = "Dargestellte Referenz: ",
    fitted_line = "Angepasste Linie: ",
    measure = "Kennzahl: ",
    value = "Wert: ",
    profile = "Profil: ",
    component = "Teil der Gleichung: ",
    contribution = "Beitrag: "
  )
} else {
  list(
    participant = "Participant: ",
    tutorial_format = "Tutorial format: ",
    prior_score = "Prior score: ",
    practice_hours = "Practice hours: ",
    observed_score = "Observed score: ",
    fitted_score = "Fitted score: ",
    residual = "Residual: ",
    expected_normal_quantile = "Expected normal quantile: ",
    standardized_residual = "Standardized residual: ",
    model = "Model: ",
    prior_score_held = "Prior score held at: ",
    displayed_reference = "Displayed reference: ",
    fitted_line = "Fitted line: ",
    measure = "Measure: ",
    value = "Value: ",
    profile = "Profile: ",
    component = "Equation part: ",
    contribution = "Contribution: "
  )
}

required_topic7_packages <- c(
  "dplyr", "tibble", "tidyr", "ggplot2", "DT", "knitr", "plotly", "htmlwidgets"
)
missing_topic7_packages <- required_topic7_packages[
  !vapply(required_topic7_packages, requireNamespace, logical(1), quietly = TRUE)
]
if (length(missing_topic7_packages)) {
  stop(
    "Topic 7 requires these R packages: ",
    paste(missing_topic7_packages, collapse = ", "),
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

format_t07 <- function(value, digits = 2) {
  formatC(value, format = "f", digits = digits, big.mark = ",")
}

format_p_t07 <- function(value) {
  ifelse(
    is.na(value),
    "",
    ifelse(value < 0.001, "< .001", sub("^0", "", sprintf("%.3f", value)))
  )
}

topic7_plotly <- function(plot, alt_text, tooltip = "text", top_margin = 60) {
  plot_kind <- attr(plot, "ratiomera_plotly_kind", exact = TRUE)
  widget_height <- attr(plot, "ratiomera_widget_height", exact = TRUE)
  skip_scalar_hover <- isTRUE(attr(plot, "ratiomera_skip_scalar_hover", exact = TRUE))
  if (exists("ratiomera_make_plotly_compatible", mode = "function")) {
    plot <- ratiomera_make_plotly_compatible(plot)
  }

  widget <- ggplotly(
    plot,
    tooltip = tooltip,
    dynamicTicks = FALSE,
    height = widget_height
  ) |>
    ratiomera_prepare_plotly_widget(
      title_width = 36,
      axis_width = 28,
      annotation_width = 30,
      title_size = 14
    )

  # Quarto owns the responsive htmlwidget container height. Removing the
  # duplicate fixed Plotly layout height keeps the SVG, legend, and caption in
  # one consistent box at every viewport while preserving the intrinsic widget
  # height requested on each teaching figure.
  widget$x$layout$height <- NULL

  widget$x$data <- lapply(widget$x$data, function(trace) {
    if (!is.null(trace$name) && identical(trace$name, "fitted values")) {
      trace$name <- topic7_labels$fitted
    }
    trace
  })

  if (
    exists("ratiomera_localize_plotly_hover", mode = "function") &&
      exists("ratiomera_plotly_hover_labels", mode = "function")
  ) {
    widget <- ratiomera_localize_plotly_hover(
      widget,
      ratiomera_plotly_hover_labels(plot, topic_locale)
    )
  }

  if (isTRUE(plot_kind %in% c("interaction", "reference", "fit_path"))) {
    widget$x$data <- lapply(widget$x$data, function(trace) {
      if (isTRUE(trace$showlegend) && !is.null(trace$name)) {
        trace$name <- ratiomera_wrap_plotly_text(trace$name, width = 16)
      }
      trace
    })
  }

  if (skip_scalar_hover) {
    widget$x$data <- lapply(widget$x$data, function(trace) {
      has_scalar_text <-
        (!is.null(trace$text) && length(trace$text) <= 1L) ||
        (!is.null(trace$hovertext) && length(trace$hovertext) <= 1L)
      if (has_scalar_text) {
        trace$hoverinfo <- "skip"
        trace$hovertemplate <- NULL
      }
      trace
    })
  }

  bottom_margin <- if (isTRUE(plot_kind %in% c("interaction", "reference"))) {
    220
  } else if (identical(plot_kind, "fit_path")) {
    190
  } else {
    82
  }

  widget <- widget |>
    layout(
      autosize = TRUE,
      hovermode = "closest",
      margin = list(l = 76, r = 34, b = bottom_margin, t = max(top_margin, 84), pad = 2)
    )

  if (isTRUE(plot_kind %in% c("interaction", "reference"))) {
    widget <- widget |>
      layout(
        legend = list(
          orientation = "v",
          x = 0.5,
          xanchor = "center",
          y = -0.23,
          yanchor = "top",
          font = list(size = 10.5),
          tracegroupgap = 3,
          title = list(text = "")
        )
      )
  } else if (identical(plot_kind, "fit_path")) {
    widget <- widget |>
      layout(
        legend = list(
          orientation = "v",
          x = 0.5,
          xanchor = "center",
          y = -0.28,
          yanchor = "top",
          font = list(size = 10.5),
          title = list(text = "")
        )
      )
  }

  if (identical(plot_kind, "fit_path")) {
    widget <- widget |>
      layout(xaxis = list(tickangle = 0, automargin = TRUE))
  }

  widget |>
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

t07_theme <- function(base_size = 12) {
  theme_minimal(base_size = base_size) +
    theme(
      plot.title = element_text(face = "bold", color = "#172B3A"),
      plot.subtitle = element_text(color = "#536475"),
      axis.title = element_text(color = "#34495E"),
      axis.text = element_text(color = "#465A6B"),
      strip.text = element_text(face = "bold", color = "#203A4F"),
      legend.position = "bottom",
      legend.title = element_blank(),
      panel.grid.minor = element_blank(),
      panel.grid.major = element_line(color = "#E7ECF1"),
      plot.background = element_rect(fill = "white", color = NA),
      panel.background = element_rect(fill = "white", color = NA)
    )
}

coefficient_table_t07 <- function(model, term_labels) {
  coefficient_matrix <- coef(summary(model))
  confidence_limits <- confint(model, level = 0.95)
  terms <- rownames(coefficient_matrix)

  tibble(
    term = unname(term_labels[terms]),
    estimate = unname(coefficient_matrix[, "Estimate"]),
    standard_error = unname(coefficient_matrix[, "Std. Error"]),
    t_value = unname(coefficient_matrix[, "t value"]),
    p_value = unname(coefficient_matrix[, "Pr(>|t|)"]),
    ci_lower = unname(confidence_limits[, 1]),
    ci_upper = unname(confidence_limits[, 2])
  )
}

# Deterministic instructional cohort. These simulated values are not empirical
# observations and make no claim about real students or tutorial formats.
set.seed(707)
topic7_n <- 180L
topic7_format_levels <- c(
  topic7_labels$independent,
  topic7_labels$peer,
  topic7_labels$guided
)
topic7_peer_term <- paste0("tutorial_format", topic7_labels$peer)
topic7_guided_term <- paste0("tutorial_format", topic7_labels$guided)
topic7_peer_interaction_term <- paste0("practice_hours:", topic7_peer_term)
topic7_guided_interaction_term <- paste0("practice_hours:", topic7_guided_term)

topic7_data <- tibble(
  participant_id = sprintf("S%03d", seq_len(topic7_n)),
  tutorial_format = factor(
    sample(rep(topic7_format_levels, each = topic7_n / length(topic7_format_levels))),
    levels = topic7_format_levels
  ),
  prior_score = round(
    pmin(pmax(rnorm(topic7_n, mean = 10, sd = 3), 1), 19),
    1
  )
) |>
  mutate(
    practice_hours = round(
      pmin(
        pmax(1.2 + 0.48 * prior_score + rnorm(topic7_n, 0, 2.35), 0),
        16
      ),
      1
    ),
    format_shift = unname(
      setNames(c(0, 1.8, 3.7), topic7_format_levels)[as.character(tutorial_format)]
    ),
    interaction_shift = unname(
      setNames(c(0, 0.35, 0.85), topic7_format_levels)[as.character(tutorial_format)]
    ),
    reasoning_score = round(
      25 + 2.2 * prior_score + 0.85 * practice_hours + format_shift +
        interaction_shift * practice_hours + rnorm(topic7_n, 0, 5.2),
      1
    )
  ) |>
  select(-format_shift, -interaction_shift)

topic7_models <- list(
  M0 = lm(reasoning_score ~ 1, data = topic7_data),
  M1 = lm(reasoning_score ~ practice_hours, data = topic7_data),
  M2 = lm(reasoning_score ~ prior_score + practice_hours, data = topic7_data),
  M3 = lm(
    reasoning_score ~ prior_score + practice_hours + tutorial_format,
    data = topic7_data
  ),
  M4 = lm(
    reasoning_score ~ prior_score + practice_hours * tutorial_format,
    data = topic7_data
  )
)

topic7_model_descriptions <- topic7_text$model_descriptions

topic7_model_table <- bind_rows(lapply(names(topic7_models), function(model_id) {
  fitted_model <- topic7_models[[model_id]]
  model_summary <- summary(fitted_model)
  tibble(
    model = model_id,
    terms = unname(topic7_model_descriptions[model_id]),
    predictor_parameters = length(coef(fitted_model)) - 1L,
    r_squared = unname(model_summary$r.squared),
    adjusted_r_squared = unname(model_summary$adj.r.squared),
    residual_standard_error = unname(model_summary$sigma),
    residual_df = unname(fitted_model$df.residual),
    aic = unname(AIC(fitted_model))
  )
}))

topic7_simple_practice_model <- topic7_models$M1
topic7_continuous_model <- topic7_models$M2
topic7_additive_model <- topic7_models$M3
topic7_interaction_model <- topic7_models$M4
topic7_prior_only_model <- lm(reasoning_score ~ prior_score, data = topic7_data)

topic7_full_summary <- summary(topic7_interaction_model)
topic7_global_f <- unname(topic7_full_summary$fstatistic[["value"]])
topic7_global_df1 <- unname(topic7_full_summary$fstatistic[["numdf"]])
topic7_global_df2 <- unname(topic7_full_summary$fstatistic[["dendf"]])
topic7_global_p <- pf(
  topic7_global_f,
  topic7_global_df1,
  topic7_global_df2,
  lower.tail = FALSE
)

topic7_full_term_labels <- setNames(
  c(
    topic7_text$term_labels[[1]],
    topic7_labels$prior,
    paste0(topic7_labels$practice, ": ", topic7_labels$reference_format_slope),
    topic7_text$term_labels[[2]],
    topic7_text$term_labels[[3]],
    topic7_text$term_labels[[4]],
    topic7_text$term_labels[[5]]
  ),
  c(
    "(Intercept)",
    "prior_score",
    "practice_hours",
    topic7_peer_term,
    topic7_guided_term,
    topic7_peer_interaction_term,
    topic7_guided_interaction_term
  )
)

topic7_full_coefficient_table <- coefficient_table_t07(
  topic7_interaction_model,
  topic7_full_term_labels
)

topic7_continuous_coefficient_table <- tibble(
  predictor = c(topic7_labels$prior, topic7_labels$practice),
  unstandardized_b = unname(coef(topic7_continuous_model)[c("prior_score", "practice_hours")]),
  standardized_beta = unname(
    coef(topic7_continuous_model)[c("prior_score", "practice_hours")] *
      c(sd(topic7_data$prior_score), sd(topic7_data$practice_hours)) /
      sd(topic7_data$reasoning_score)
  ),
  bivariate_r = c(
    cor(topic7_data$prior_score, topic7_data$reasoning_score),
    cor(topic7_data$practice_hours, topic7_data$reasoning_score)
  )
)

topic7_nested_test <- anova(topic7_additive_model, topic7_interaction_model)
topic7_nested_stats <- tibble(
  restricted_model = topic7_text$nested_labels[[1]],
  unrestricted_model = topic7_text$nested_labels[[2]],
  parameters_added = unname(topic7_nested_test$Df[2]),
  rss_restricted = unname(topic7_nested_test$RSS[1]),
  rss_unrestricted = unname(topic7_nested_test$RSS[2]),
  f_value = unname(topic7_nested_test$F[2]),
  numerator_df = unname(topic7_nested_test$Df[2]),
  denominator_df = df.residual(topic7_interaction_model),
  p_value = unname(topic7_nested_test$`Pr(>F)`[2])
)

# Semipartial correlation for the incremental contribution of practice hours
# after the existing prior-score predictor. The outcome is not residualized.
topic7_practice_on_prior <- lm(practice_hours ~ prior_score, data = topic7_data)
topic7_practice_residual <- unname(resid(topic7_practice_on_prior))
topic7_semipartial_r <- cor(topic7_practice_residual, topic7_data$reasoning_score)
topic7_delta_r2 <- unname(
  summary(topic7_continuous_model)$r.squared -
    summary(topic7_prior_only_model)$r.squared
)

topic7_semipartial_stats <- tibble(
  quantity = topic7_text$semipartial_quantities,
  value = c(
    cor(topic7_data$practice_hours, topic7_data$reasoning_score),
    cor(topic7_data$prior_score, topic7_data$practice_hours),
    topic7_semipartial_r,
    topic7_semipartial_r^2,
    topic7_delta_r2
  )
)

topic7_data <- topic7_data |>
  mutate(
    fitted_score = unname(fitted(topic7_interaction_model)),
    residual = unname(resid(topic7_interaction_model)),
    standardized_residual = unname(rstandard(topic7_interaction_model)),
    leverage = unname(hatvalues(topic7_interaction_model)),
    cooks_distance = unname(cooks.distance(topic7_interaction_model)),
    practice_after_prior = topic7_practice_residual,
    hover = paste0(
      topic7_hover_text$participant, participant_id,
      "<br>", topic7_hover_text$tutorial_format, tutorial_format,
      "<br>", topic7_hover_text$prior_score, format_t07(prior_score, 1),
      "<br>", topic7_hover_text$practice_hours, format_t07(practice_hours, 1),
      "<br>", topic7_hover_text$observed_score, format_t07(reasoning_score, 1),
      "<br>", topic7_hover_text$fitted_score, format_t07(fitted_score, 2),
      "<br>", topic7_hover_text$residual, format_t07(residual, 2)
    )
  )

# A short, descriptive review list for the cases with the largest Cook's
# distances. This is a ranking for closer inspection, not a deletion rule.
topic7_influence_table <- topic7_data |>
  arrange(desc(cooks_distance)) |>
  select(
    participant_id,
    fitted_score,
    residual,
    standardized_residual,
    leverage,
    cooks_distance
  ) |>
  slice_head(n = 5)

topic7_variable_table <- tibble(
  variable = topic7_text$variable_names,
  role = topic7_text$variable_roles,
  measurement = topic7_text$variable_measurements
)

topic7_preview <- topic7_data |>
  select(participant_id, prior_score, practice_hours, tutorial_format, reasoning_score) |>
  slice_head(n = 10)

topic7_fitted_preview <- topic7_data |>
  select(
    participant_id,
    reasoning_score,
    fitted_score,
    residual,
    prior_score,
    practice_hours,
    tutorial_format
  ) |>
  slice_head(n = 8)

topic7_dummy_table <- tibble(
  tutorial_format = factor(topic7_format_levels, levels = topic7_format_levels),
  peer_indicator = c(0L, 1L, 0L),
  guided_indicator = c(0L, 0L, 1L),
  interpretation = topic7_text$dummy_interpretations
)

# Group-specific equations from the fitted interaction model. The prior-score
# coefficient is common, while intercept and practice slope can vary by format.
topic7_beta <- coef(topic7_interaction_model)
topic7_group_equations <- tibble(
  tutorial_format = factor(topic7_format_levels, levels = topic7_format_levels),
  intercept_component = c(
    topic7_beta[["(Intercept)"]],
    topic7_beta[["(Intercept)"]] + topic7_beta[[topic7_peer_term]],
    topic7_beta[["(Intercept)"]] + topic7_beta[[topic7_guided_term]]
  ),
  prior_score_slope = rep(topic7_beta[["prior_score"]], 3),
  practice_slope = c(
    topic7_beta[["practice_hours"]],
    topic7_beta[["practice_hours"]] +
      topic7_beta[[topic7_peer_interaction_term]],
    topic7_beta[["practice_hours"]] +
      topic7_beta[[topic7_guided_interaction_term]]
  )
)

topic7_prediction_profile <- tibble(
  prior_score = rep(10, 3),
  practice_hours = rep(6, 3),
  tutorial_format = factor(topic7_format_levels, levels = topic7_format_levels)
)
topic7_prediction_profile$fitted_score <- unname(
  predict(topic7_interaction_model, newdata = topic7_prediction_profile)
)

# Refit the identical interaction model under every possible reference level.
# Predictions remain invariant even though the displayed coefficient set moves.
topic7_reference_models <- setNames(lapply(topic7_format_levels, function(reference_level) {
  reference_data <- topic7_data |>
    mutate(
      tutorial_format_releveled = relevel(tutorial_format, ref = reference_level)
    )
  lm(
    reasoning_score ~ prior_score + practice_hours * tutorial_format_releveled,
    data = reference_data
  )
}), topic7_format_levels)

topic7_reference_coefficient_table <- bind_rows(lapply(topic7_format_levels, function(reference_level) {
  model <- topic7_reference_models[[reference_level]]
  tibble(
    reference_category = reference_level,
    intercept = unname(coef(model)[["(Intercept)"]]),
    reference_practice_slope = unname(coef(model)[["practice_hours"]])
  )
}))

topic7_reference_prediction_table <- bind_rows(lapply(topic7_format_levels, function(reference_level) {
  model <- topic7_reference_models[[reference_level]]
  prediction_data <- tibble(
    prior_score = rep(10, 3),
    practice_hours = rep(6, 3),
    tutorial_format_releveled = factor(
      topic7_format_levels,
      levels = levels(model$model$tutorial_format_releveled)
    )
  )
  tibble(
    parameterization = paste0(topic7_text$reference_prefix, reference_level),
    tutorial_format = topic7_format_levels,
    fitted_score = unname(predict(model, newdata = prediction_data))
  )
}))

# Bridge from the fitted equation to one row. The selected constructed case is
# evaluated with M2, the same two-predictor model used by the Theory surface
# below. Geometry and values are shared; labels follow the page locale.
topic7_composition_case <- topic7_data[1, ]
topic7_composition_beta <- coef(topic7_continuous_model)
topic7_composition_intercept <- unname(topic7_composition_beta[["(Intercept)"]])
topic7_composition_prior <- unname(
  topic7_composition_beta[["prior_score"]] * topic7_composition_case$prior_score
)
topic7_composition_practice <- unname(
  topic7_composition_beta[["practice_hours"]] * topic7_composition_case$practice_hours
)
topic7_composition_fitted <- unname(
  predict(topic7_continuous_model, newdata = topic7_composition_case)
)
topic7_composition_residual <- unname(
  topic7_composition_case$reasoning_score - topic7_composition_fitted
)

topic7_composition_text <- if (topic_locale == "de") {
  list(
    starting = "Ausgangswert",
    prior = "Beitrag des\nVorwissens",
    practice = "Beitrag der\nÜbung",
    fitted = "Angepasster\nZielwert",
    observed = "Beobachtetes Yᵢ = ",
    residual = "Residuum eᵢ = Yᵢ − Ŷᵢ = ",
    title = "Ein angepasster Wert addiert die Beiträge aller aufgenommenen Prädiktoren",
    subtitle_prefix = "Konstruierter Fall ",
    subtitle_suffix = paste0(
      " im Modell mit zwei Prädiktoren; alle Terme tragen zum selben ",
      "angepassten Zielwert bei"
    )
  )
} else if (topic_locale == "sq") {
  list(
    starting = "Vlera fillestare",
    prior = "Kontributi i\npikëve paraprake",
    practice = "Kontributi i\nushtrimit",
    fitted = "Rezultati i\npërshtatur",
    observed = "E vrojtuara Yᵢ = ",
    residual = "reziduali eᵢ = Yᵢ − Ŷᵢ = ",
    title = "Një vlerë e përshtatur mbledh kontributet e çdo ndryshoreje parashikuese të përfshirë",
    subtitle_prefix = "Rasti i krijuar ",
    subtitle_suffix = paste0(
      " në modelin me dy ndryshore parashikuese; të gjithë termat kontribuojnë ",
      "në të njëjtin rezultat të përshtatur"
    )
  )
} else {
  list(
    starting = "Starting value",
    prior = "Prior contribution",
    practice = "Practice contribution",
    fitted = "Fitted outcome",
    observed = "Observed Yᵢ = ",
    residual = "residual eᵢ = Yᵢ − Ŷᵢ = ",
    title = "One Fitted Value Adds the Contributions from Every Included Predictor",
    subtitle_prefix = "Constructed case ",
    subtitle_suffix = " in the two-predictor model; all terms contribute to the same fitted outcome"
  )
}

topic7_composition_boxes <- tibble(
  x = c(0.9, 3.0, 5.1, 7.3),
  y = 1.25,
  label = c(
    paste0(topic7_composition_text$starting, "\nb₀ = ", format_t07(topic7_composition_intercept, 2)),
    paste0(
      topic7_composition_text$prior, "\nb₁Xᵢ₁ = ", format_t07(topic7_composition_beta[["prior_score"]], 2),
      " × ", format_t07(topic7_composition_case$prior_score, 1), "\n= ", format_t07(topic7_composition_prior, 2)
    ),
    paste0(
      topic7_composition_text$practice, "\nb₂Xᵢ₂ = ", format_t07(topic7_composition_beta[["practice_hours"]], 2),
      " × ", format_t07(topic7_composition_case$practice_hours, 1), "\n= ", format_t07(topic7_composition_practice, 2)
    ),
    paste0(topic7_composition_text$fitted, "\nŶᵢ = ", format_t07(topic7_composition_fitted, 2))
  ),
  kind = c("start", "contribution", "contribution", "fitted")
)

p_topic7_fitted_composition_en <- ggplot() +
  geom_segment(
    data = tibble(
      x = c(1.62, 3.72, 5.84),
      xend = c(2.28, 4.38, 6.50),
      y = 1.25,
      yend = 1.25
    ),
    aes(x, y, xend = xend, yend = yend),
    color = "#8198A8",
    linewidth = 0.9,
    arrow = grid::arrow(length = grid::unit(0.13, "cm"), type = "closed")
  ) +
  annotate("text", x = c(1.95, 4.05), y = 1.53, label = "+", color = "#34495E", fontface = "bold", size = 5) +
  annotate("text", x = 6.17, y = 1.53, label = "=", color = "#34495E", fontface = "bold", size = 5) +
  geom_label(
    data = topic7_composition_boxes,
    aes(x, y, label = label, fill = kind),
    color = "#203A4F",
    fontface = "bold",
    size = 3.05,
    lineheight = 0.95,
    linewidth = 0.32,
    label.padding = grid::unit(0.22, "lines")
  ) +
  annotate(
    "label",
    x = 4.1,
    y = 0.30,
    label = paste0(
      topic7_composition_text$observed, format_t07(topic7_composition_case$reasoning_score, 1),
      "   |   ", topic7_composition_text$residual, format_t07(topic7_composition_residual, 2)
    ),
    fill = "#FFF4EA",
    color = "#713D31",
    fontface = "bold",
    size = 3.15,
    linewidth = 0.3
  ) +
  scale_fill_manual(
    values = c(start = "#EAF2F8", contribution = "#EAF4EF", fitted = "#FFE0CC"),
    guide = "none"
  ) +
  coord_cartesian(xlim = c(0.0, 8.2), ylim = c(-0.05, 1.95), clip = "off") +
  labs(
    title = topic7_composition_text$title,
    subtitle = paste0(
      topic7_composition_text$subtitle_prefix, topic7_composition_case$participant_id,
      topic7_composition_text$subtitle_suffix
    )
  ) +
  theme_void(base_size = 11) +
  theme(
    plot.title = element_text(face = "bold", color = "#172B3A"),
    plot.subtitle = element_text(color = "#536475"),
    plot.background = element_rect(fill = "white", color = NA),
    panel.background = element_rect(fill = "white", color = NA),
    plot.margin = margin(14, 24, 14, 24)
  )

# Theory figure: the two-predictor fitted surface from M2, displayed from
# above so both predictor axes and the fitted outcome remain readable without
# an inaccessible three-dimensional projection. Horizontal and vertical guide
# lines show what it means to change one predictor while holding the other
# fixed.
topic7_surface_grid <- expand_grid(
  practice_hours = seq(0, 12, length.out = 121),
  prior_score = seq(4, 16, length.out = 121)
)
topic7_surface_grid$fitted_score <- unname(
  predict(topic7_continuous_model, newdata = topic7_surface_grid)
)

if (topic_locale %in% c("en", "de", "sq")) {
  topic7_surface_levels <- c(40, 50, 60, 70)
  topic7_surface_label_data <- tibble(
    fitted_score = topic7_surface_levels,
    practice_hours = c(1.5, 3.5, 5.5, 10)
  ) |>
    mutate(
      prior_score = (
        fitted_score - coef(topic7_continuous_model)[["(Intercept)"]] -
          coef(topic7_continuous_model)[["practice_hours"]] * practice_hours
      ) / coef(topic7_continuous_model)[["prior_score"]],
      label = paste0(
        if (topic_locale == "de") {
          "Angepasster Punktwert = "
        } else if (topic_locale == "sq") {
          "Pikët e përshtatura = "
        } else {
          "Fitted score = "
        },
        fitted_score
      )
    ) |>
    filter(between(prior_score, 4.3, 15.7))

  p_topic7_surface <- ggplot(
    topic7_surface_grid,
    aes(practice_hours, prior_score)
  ) +
    geom_contour(
      aes(z = fitted_score),
      breaks = topic7_surface_levels,
      color = "#477C9D",
      linewidth = 0.9
    ) +
    geom_label(
      data = topic7_surface_label_data,
      aes(practice_hours, prior_score, label = label),
      inherit.aes = FALSE,
      fill = "white",
      color = "#244C69",
      fontface = "bold",
      size = 2.9,
      linewidth = 0.25,
      label.padding = grid::unit(0.12, "lines")
    ) +
    geom_hline(
      yintercept = 10,
      color = "#C05A47",
      linetype = "longdash",
      linewidth = 0.9
    ) +
    geom_vline(
      xintercept = 6,
      color = "#173F5F",
      linetype = "dotted",
      linewidth = 0.9
    ) +
    annotate(
      "label",
      x = 11.45,
      y = 10.35,
      label = topic7_text$surface_prior_annotation,
      hjust = 1,
      size = 3.05,
      fill = "#FFF8F5",
      color = "#713D31"
    ) +
    annotate(
      "label",
      x = 6.25,
      y = 15.35,
      label = topic7_text$surface_practice_annotation,
      hjust = 0,
      size = 3.05,
      fill = "#F4F8FB",
      color = "#173F5F"
    ) +
    coord_cartesian(xlim = c(0, 12), ylim = c(4, 16), clip = "off") +
    labs(
      title = topic7_text$surface_title,
      subtitle = topic7_text$surface_subtitle,
      x = topic7_labels$practice,
      y = topic7_labels$prior
    ) +
    t07_theme() +
    theme(
      legend.position = "none",
      panel.grid.minor = element_blank(),
      plot.margin = margin(14, 24, 14, 18)
    )
} else {
  p_topic7_surface <- ggplot(
    topic7_surface_grid,
    aes(practice_hours, prior_score, fill = fitted_score)
  ) +
    geom_raster(interpolate = TRUE) +
    geom_contour(
      data = topic7_surface_grid,
      aes(x = practice_hours, y = prior_score, z = fitted_score),
      inherit.aes = FALSE,
      color = "white",
      alpha = 0.72,
      linewidth = 0.45,
      bins = 8
    ) +
    geom_hline(yintercept = 10, color = "#C05A47", linetype = "longdash", linewidth = 0.9) +
    geom_vline(xintercept = 6, color = "#173F5F", linetype = "dotted", linewidth = 0.9) +
    annotate(
      "label", x = 10.8, y = 10.35,
      label = topic7_text$surface_prior_annotation,
      hjust = 1, size = 3.05, fill = "#FFF8F5", color = "#713D31"
    ) +
    annotate(
      "label", x = 6.25, y = 15.4,
      label = topic7_text$surface_practice_annotation,
      hjust = 0, size = 3.05, fill = "#F4F8FB", color = "#173F5F"
    ) +
    scale_fill_gradientn(
      colors = c("#EEF4F8", "#80A9C4", "#1F5C83", "#173F5F"),
      name = topic7_text$surface_fill
    ) +
    labs(
      title = topic7_text$surface_title,
      subtitle = topic7_text$surface_subtitle,
      x = topic7_labels$practice,
      y = topic7_labels$prior
    ) +
    t07_theme() +
    theme(legend.position = "right")
}

p_topic7_surface_enriched_en <- p_topic7_surface +
  geom_point(
    data = tibble(practice_hours = 6, prior_score = 10),
    aes(practice_hours, prior_score),
    inherit.aes = FALSE,
    shape = 21,
    fill = "#FFE0CC",
    color = "#713D31",
    stroke = 1.1,
    size = 4
  ) +
  annotate(
    "label",
    x = 6.35,
    y = 9.18,
    label = if (topic_locale == "de") {
      "Ausgewähltes Prädiktorprofil\nÜbung = 6, Vorwissenswert = 10"
    } else if (topic_locale == "sq") {
      "Profili i zgjedhur parashikues\nushtrimi = 6, pikët paraprake = 10"
    } else {
      "Selected predictor profile\npractice = 6, prior score = 10"
    },
    hjust = 0,
    fill = "#FFF4EA",
    color = "#713D31",
    fontface = "bold",
    size = 3.0,
    linewidth = 0.3
  ) +
  annotate(
    "segment",
    x = 2.0,
    xend = 4.8,
    y = 10,
    yend = 10,
    color = "#C05A47",
    linewidth = 1.2,
    arrow = grid::arrow(length = grid::unit(0.14, "cm"), type = "closed")
  ) +
  annotate(
    "segment",
    x = 6,
    xend = 6,
    y = 5.3,
    yend = 8.4,
    color = "#173F5F",
    linewidth = 1.2,
    arrow = grid::arrow(length = grid::unit(0.14, "cm"), type = "closed")
  ) +
  annotate(
    "label",
    x = 1.25,
    y = 14.9,
    label = if (topic_locale == "de") {
      "Jede Konturlinie verbindet Profile\nmit demselben angepassten Zielwert"
    } else if (topic_locale == "sq") {
      "Çdo vijë e bardhë konturi lidh profile\nme të njëjtin rezultat të përshtatur"
    } else {
      "Each contour joins profiles\nwith the same fitted outcome"
    },
    hjust = 0,
    fill = "#F4F8FB",
    color = "#173F5F",
    size = 2.95,
    linewidth = 0.25
  )

# Theory figure: four concrete predictor profiles replace the abstract
# top-down surface as the learner-facing bridge from one line to several
# predictor contributions. The underlying M2 coefficients and predictions are
# unchanged. Each stacked segment is one term in the same fitted-value sum.
topic7_profile_specs <- tibble(
  profile_id = c("A", "B", "C", "D"),
  prior_score = c(8, 8, 12, 12),
  practice_hours = c(2, 6, 2, 6)
)
topic7_profile_specs$fitted_score <- unname(
  predict(topic7_continuous_model, newdata = topic7_profile_specs)
)

topic7_profile_specs <- topic7_profile_specs |>
  mutate(
    profile_label = paste0(
      topic7_text$profile_prefix, profile_id,
      if (topic_locale == "de") {
        paste0(": Vorwissen ", prior_score, ", Übung ", practice_hours)
      } else if (topic_locale == "sq") {
        paste0(": pikët paraprake ", prior_score, ", ushtrimi ", practice_hours)
      } else {
        paste0(": prior ", prior_score, ", practice ", practice_hours)
      }
    )
  )

topic7_profile_components <- bind_rows(
  topic7_profile_specs |>
    transmute(
      profile_id, profile_label, prior_score, practice_hours, fitted_score,
      component = topic7_text$profile_components[[1]],
      contribution = unname(topic7_composition_beta[["(Intercept)"]])
    ),
  topic7_profile_specs |>
    transmute(
      profile_id, profile_label, prior_score, practice_hours, fitted_score,
      component = topic7_text$profile_components[[2]],
      contribution = unname(topic7_composition_beta[["prior_score"]]) * prior_score
    ),
  topic7_profile_specs |>
    transmute(
      profile_id, profile_label, prior_score, practice_hours, fitted_score,
      component = topic7_text$profile_components[[3]],
      contribution = unname(topic7_composition_beta[["practice_hours"]]) * practice_hours
    )
) |>
  mutate(
    profile_label = factor(
      profile_label,
      levels = rev(unique(topic7_profile_specs$profile_label))
    ),
    component = factor(component, levels = topic7_text$profile_components),
    # Keep the stack order independent of translated component labels. ggplot2
    # otherwise derives grouping from the locale-specific strings, which can
    # place the same equation terms in a different visual order by language.
    component_order = factor(
      match(component, topic7_text$profile_components),
      levels = seq_along(topic7_text$profile_components)
    ),
    hover = paste0(
      topic7_hover_text$profile, as.character(profile_label),
      "<br>", topic7_hover_text$component, component,
      "<br>", topic7_hover_text$contribution, format_t07(contribution, 2),
      "<br>", topic7_hover_text$fitted_score, format_t07(fitted_score, 2)
    )
  )

topic7_profile_totals <- topic7_profile_specs |>
  mutate(
    profile_label = factor(
      profile_label,
      levels = rev(unique(topic7_profile_specs$profile_label))
    ),
    total_label = paste0(topic7_text$fitted_total_prefix, format_t07(fitted_score, 2))
  )

p_topic7_profile_contributions <- ggplot(
  topic7_profile_components,
  aes(
    contribution,
    profile_label,
    fill = component,
    group = component_order
  )
) +
  geom_col(
    aes(text = hover),
    width = 0.64,
    color = "white",
    linewidth = 0.45,
    position = position_stack(reverse = TRUE)
  ) +
  geom_text(
    data = topic7_profile_totals,
    aes(x = fitted_score, y = profile_label, label = total_label),
    inherit.aes = FALSE,
    hjust = -0.12,
    color = "#203A4F",
    fontface = "bold",
    size = 3.2
  ) +
  scale_fill_manual(
    values = setNames(
      c("#D9E7F1", "#6F9FC0", "#E6A06D"),
      topic7_text$profile_components
    )
  ) +
  scale_x_continuous(expand = expansion(mult = c(0, 0.23))) +
  labs(
    title = topic7_text$profile_title,
    subtitle = topic7_text$profile_subtitle,
    x = topic7_text$profile_axis,
    y = NULL,
    fill = NULL
  ) +
  t07_theme() +
  theme(
    panel.grid.major.y = element_blank(),
    legend.position = "bottom",
    plot.margin = margin(14, 26, 14, 18)
  )

# Theory figure 1: a conditional practice coefficient in the two-continuous-
# predictor model. Parallel lines hold prior score fixed at three values.
topic7_conditional_grid <- expand_grid(
  practice_hours = seq(0, 12, length.out = 100),
  prior_score = c(7, 10, 13)
) |>
  mutate(
    prior_label = factor(
      paste0(topic7_text$prior_score_prefix, prior_score),
      levels = paste0(topic7_text$prior_score_prefix, c(7, 10, 13))
    )
  )
topic7_conditional_grid$fitted_score <- unname(
  predict(topic7_continuous_model, newdata = topic7_conditional_grid)
)
topic7_conditional_grid <- topic7_conditional_grid |>
  mutate(
    hover = paste0(
      topic7_hover_text$practice_hours, format_t07(practice_hours, 1),
      "<br>", topic7_hover_text$prior_score_held, format_t07(prior_score, 1),
      "<br>", topic7_hover_text$fitted_score, format_t07(fitted_score, 2)
    )
  )

topic7_step_start <- tibble(practice_hours = 5, prior_score = 10)
topic7_step_end <- tibble(practice_hours = 6, prior_score = 10)
topic7_step_y_start <- unname(predict(topic7_continuous_model, topic7_step_start))
topic7_step_y_end <- unname(predict(topic7_continuous_model, topic7_step_end))

p_topic7_conditional <- ggplot(
  topic7_conditional_grid,
  aes(
    practice_hours,
    fitted_score,
    color = prior_label,
    group = prior_label
  )
) +
  geom_line(aes(text = hover), linewidth = 1.15) +
  annotate(
    "segment",
    x = 5,
    xend = 6,
    y = topic7_step_y_start,
    yend = topic7_step_y_start,
    color = "#C05A47",
    linewidth = 1,
    arrow = grid::arrow(length = grid::unit(0.14, "cm"))
  ) +
  annotate(
    "segment",
    x = 6,
    xend = 6,
    y = topic7_step_y_start,
    yend = topic7_step_y_end,
    color = "#C05A47",
    linewidth = 1,
    arrow = grid::arrow(length = grid::unit(0.14, "cm"))
  ) +
  annotate(
    "label",
    x = 6.2,
    y = (topic7_step_y_start + topic7_step_y_end) / 2,
    label = paste0(topic7_text$conditional_change_prefix, format_t07(coef(topic7_continuous_model)[["practice_hours"]], 2)),
    hjust = 0,
    size = 3.2,
    fill = "#FFF8F5",
    color = "#713D31"
  ) +
  scale_color_manual(values = c("#7A9CB5", "#2F6F9F", "#183E5A")) +
  coord_cartesian(xlim = c(0, 12), clip = "off") +
  labs(
    title = topic7_text$conditional_title,
    subtitle = topic7_text$conditional_subtitle,
    x = topic7_labels$practice,
    y = topic7_labels$fitted
  ) +
  t07_theme()

# Theory figure 2: illustrative directions of coefficient change. These values
# are deliberately labeled as schematic, not as results from the simulation.
topic7_coefficient_patterns <- tibble(
  pattern = factor(
    topic7_text$coefficient_patterns,
    levels = rev(topic7_text$coefficient_patterns)
  ),
  bivariate = c(0.60, 0.60, 0.18),
  conditional = c(0.56, 0.18, 0.60)
)

# Two internally coherent correlation patterns make the adjustment logic
# calculable. They are newly constructed teaching values, not empirical
# results and not diagnostic thresholds.
topic7_adjustment_pattern_text <- if (topic_locale == "de") {
  list(
    patterns = c("Mögliche Konfundierung", "Mögliche Suppression"),
    interpretations = c(
      paste0(
        "Der interessierende Prädiktor und der andere Prädiktor tragen einen grossen Teil ",
        "derselben zielbezogenen Information."
      ),
      paste0(
        "Der andere Prädiktor entfernt überlappende Variation, die vom Zusammenhang ",
        "zwischen dem interessierenden Prädiktor und der Zielvariable wegweist."
      )
    )
  )
} else if (topic_locale == "sq") {
  list(
    patterns = c("Ngatërrim i mundshëm", "Shtypje e mundshme"),
    interpretations = c(
      paste0(
        "Ndryshorja parashikuese që na intereson dhe ndryshorja tjetër mbartin ",
        "një pjesë të madhe të të njëjtit informacion për rezultatin."
      ),
      paste0(
        "Ndryshorja tjetër heq ndryshueshmërinë e përbashkët që drejtohet larg ",
        "lidhjes midis ndryshores që na intereson dhe rezultatit."
      )
    )
  )
} else {
  list(
    patterns = c("Possible confounding", "Possible suppression"),
    interpretations = c(
      "The focal predictor and the other predictor carry much of the same outcome-related information.",
      "The other predictor removes overlapping variation that points away from the focal predictor's outcome relationship."
    )
  )
}

topic7_adjustment_pattern_table <- tibble(
  pattern = topic7_adjustment_pattern_text$patterns,
  focal_outcome_r = c(0.60, 0.18),
  focal_other_r = c(0.70, 0.60),
  other_outcome_r = c(0.73, -0.34),
  focal_standardized_coefficient = c(
    (0.60 - 0.70 * 0.73) / (1 - 0.70^2),
    (0.18 - 0.60 * -0.34) / (1 - 0.60^2)
  ),
  interpretation = topic7_adjustment_pattern_text$interpretations
)

topic7_coefficient_points <- topic7_coefficient_patterns |>
  pivot_longer(c(bivariate, conditional), names_to = "coefficient", values_to = "value") |>
  mutate(
    coefficient = factor(
      recode(
        coefficient,
        bivariate = topic7_text$before_adjustment,
        conditional = topic7_text$after_adjustment
      ),
      levels = c(
        topic7_text$before_adjustment,
        topic7_text$after_adjustment
      )
    ),
    label_x = case_when(
      pattern == topic7_text$coefficient_patterns[[1]] & coefficient == topic7_text$before_adjustment ~ value + 0.025,
      pattern == topic7_text$coefficient_patterns[[1]] & coefficient == topic7_text$after_adjustment ~ value - 0.025,
      TRUE ~ value
    ),
    hover = paste0(
      as.character(pattern),
      "<br>", coefficient, ": ", format_t07(value, 2)
    )
  )

topic7_coefficient_segments <- topic7_coefficient_patterns |>
  mutate(
    direction = sign(conditional - bivariate),
    visible_arrow_end = conditional - 0.022 * direction
  )

p_topic7_coefficient_change <- ggplot(topic7_coefficient_patterns, aes(y = pattern)) +
  geom_segment(
    data = topic7_coefficient_segments,
    aes(x = bivariate, xend = visible_arrow_end, yend = pattern),
    color = "#9AAAB6",
    linewidth = 1.1,
    arrow = grid::arrow(length = grid::unit(0.13, "cm"), type = "closed")
  ) +
  geom_point(
    data = topic7_coefficient_points,
    aes(x = value, color = coefficient, text = hover),
    size = 3.4
  ) +
  geom_text(
    data = topic7_coefficient_points,
    aes(x = label_x, label = format_t07(value, 2), color = coefficient),
    nudge_y = 0.16,
    size = 3.2,
    show.legend = FALSE
  ) +
  scale_color_manual(values = setNames(c("#2F6F9F", "#C05A47"), c(topic7_text$before_adjustment, topic7_text$after_adjustment))) +
  scale_x_continuous(limits = c(0, 0.7), breaks = seq(0, 0.6, 0.1)) +
  labs(
    title = topic7_text$coefficient_title,
    subtitle = topic7_text$coefficient_subtitle,
    x = topic7_text$illustrative_coefficient,
    y = NULL
  ) +
  t07_theme() +
  theme(panel.grid.major.y = element_blank())

# Constructed numeric teaching model for the transition from quantitative to
# categorical predictors and then to interactions. These values are not taken
# from the simulated cohort and are not empirical findings. Keeping the same
# numbers across locales makes every equation, table, and plot directly
# comparable.
topic7_concept_numbers <- list(
  intercept = 42,
  practice_slope = 2.5,
  guided_difference = 6,
  interaction_difference = 1.5
)

topic7_concept_formats <- c(topic7_labels$independent, topic7_labels$guided)

topic7_dummy_worked_table <- tibble(
  tutorial_format = topic7_concept_formats,
  practice_hours = c(4, 4),
  guided_indicator = c(0, 1)
) |>
  mutate(
    intercept_contribution = topic7_concept_numbers$intercept,
    practice_contribution = topic7_concept_numbers$practice_slope * practice_hours,
    group_contribution = topic7_concept_numbers$guided_difference * guided_indicator,
    fitted_score = intercept_contribution + practice_contribution + group_contribution
  )

topic7_dummy_reference_predictions <- tibble(
  parameterization = c(
    paste0(topic7_text$reference_prefix, topic7_labels$independent),
    paste0(topic7_text$reference_prefix, topic7_labels$guided)
  ),
  independent_prediction = c(52, 52),
  guided_prediction = c(58, 58)
)

topic7_concept_grid <- expand_grid(
  practice_hours = seq(0, 8, by = 0.1),
  tutorial_format = factor(topic7_concept_formats, levels = topic7_concept_formats)
) |>
  mutate(
    guided_indicator = as.numeric(tutorial_format == topic7_labels$guided),
    additive_score =
      topic7_concept_numbers$intercept +
      topic7_concept_numbers$practice_slope * practice_hours +
      topic7_concept_numbers$guided_difference * guided_indicator,
    interaction_score =
      topic7_concept_numbers$intercept +
      topic7_concept_numbers$practice_slope * practice_hours +
      topic7_concept_numbers$guided_difference * guided_indicator +
      topic7_concept_numbers$interaction_difference * practice_hours * guided_indicator
  )

topic7_dummy_highlight <- topic7_concept_grid |>
  filter(practice_hours == 4) |>
  mutate(
    hover = paste0(
      topic7_hover_text$tutorial_format, tutorial_format,
      "<br>", topic7_hover_text$practice_hours, format_t07(practice_hours, 1),
      "<br>", topic7_hover_text$fitted_score, format_t07(additive_score, 2)
    )
  )

topic7_dummy_plot_data <- topic7_concept_grid |>
  mutate(
    hover = paste0(
      topic7_hover_text$tutorial_format, tutorial_format,
      "<br>", topic7_hover_text$practice_hours, format_t07(practice_hours, 1),
      "<br>", topic7_hover_text$fitted_score, format_t07(additive_score, 2)
    )
  )

p_topic7_dummy_additive <- ggplot(
  topic7_dummy_plot_data,
  aes(practice_hours, additive_score, color = tutorial_format, group = tutorial_format)
) +
  geom_line(aes(text = hover), linewidth = 1.2) +
  geom_point(
    data = topic7_dummy_highlight,
    aes(text = hover),
    size = 3.1,
    show.legend = FALSE
  ) +
  annotate(
    "segment",
    x = 4,
    xend = 4,
    y = 52,
    yend = 58,
    color = "#34495E",
    linewidth = 0.9,
    linetype = "dashed"
  ) +
  annotate(
    "label",
    x = 4.18,
    y = 55,
    label = topic7_text$dummy_group_difference,
    hjust = 0,
    size = 3.0,
    fill = "white",
    color = "#34495E",
    linewidth = 0.25
  ) +
  scale_color_manual(values = c("#2F6F9F", "#C05A47")) +
  scale_x_continuous(breaks = 0:8) +
  labs(
    title = topic7_text$dummy_title,
    subtitle = topic7_text$dummy_subtitle,
    x = topic7_labels$practice,
    y = topic7_labels$fitted,
    color = NULL
  ) +
  t07_theme() +
  theme(plot.margin = margin(14, 34, 14, 18))

topic7_interaction_concept_data <- bind_rows(
  topic7_concept_grid |>
    transmute(
      practice_hours, tutorial_format,
      fitted_score = additive_score,
      model = topic7_text$additive_model
    ),
  topic7_concept_grid |>
    transmute(
      practice_hours, tutorial_format,
      fitted_score = interaction_score,
      model = topic7_text$interaction_model
    )
) |>
  mutate(
    model = factor(
      model,
      levels = c(topic7_text$additive_model, topic7_text$interaction_model)
    ),
    hover = paste0(
      topic7_hover_text$model, model,
      "<br>", topic7_hover_text$tutorial_format, tutorial_format,
      "<br>", topic7_hover_text$practice_hours, format_t07(practice_hours, 1),
      "<br>", topic7_hover_text$fitted_score, format_t07(fitted_score, 2)
    )
  )

topic7_interaction_numeric_table <- expand_grid(
  model = c(topic7_text$additive_model, topic7_text$interaction_model),
  practice_hours = c(0, 4, 8)
) |>
  mutate(
    independent_prediction =
      topic7_concept_numbers$intercept +
      topic7_concept_numbers$practice_slope * practice_hours,
    guided_prediction = if_else(
      model == topic7_text$additive_model,
      topic7_concept_numbers$intercept +
        topic7_concept_numbers$guided_difference +
        topic7_concept_numbers$practice_slope * practice_hours,
      topic7_concept_numbers$intercept +
        topic7_concept_numbers$guided_difference +
        (topic7_concept_numbers$practice_slope +
          topic7_concept_numbers$interaction_difference) * practice_hours
    ),
    guided_minus_independent = guided_prediction - independent_prediction
  )

p_topic7_interaction_concept <- ggplot(
  topic7_interaction_concept_data,
  aes(practice_hours, fitted_score, color = tutorial_format, group = tutorial_format)
) +
  geom_line(aes(text = hover), linewidth = 1.2) +
  facet_wrap(
    ~model,
    nrow = 1,
    labeller = labeller(model = label_wrap_gen(width = 18))
  ) +
  scale_color_manual(values = c("#2F6F9F", "#C05A47")) +
  scale_x_continuous(breaks = 0:8) +
  labs(
    title = topic7_text$interaction_concept_title,
    subtitle = topic7_text$interaction_concept_subtitle,
    x = topic7_labels$practice,
    y = topic7_labels$fitted,
    color = NULL
  ) +
  t07_theme() +
  theme(
    panel.spacing.x = grid::unit(1.5, "lines"),
    plot.margin = margin(14, 28, 14, 18)
  )

# Simulated-example figure: observed outcome against full-model fitted outcome.
topic7_case_index <- which.max(abs(topic7_data$residual))
topic7_case <- topic7_data[topic7_case_index, ]

p_topic7_fitted <- ggplot(topic7_data, aes(fitted_score, reasoning_score)) +
  geom_abline(slope = 1, intercept = 0, color = "#8B9AA6", linetype = "dashed") +
  geom_point(aes(text = hover), color = "#2F6F9F", alpha = 0.58, size = 2) +
  geom_segment(
    data = topic7_case,
    aes(
      x = fitted_score,
      xend = fitted_score,
      y = fitted_score,
      yend = reasoning_score
    ),
    color = "#C05A47",
    linewidth = 1.15
  ) +
  geom_point(data = topic7_case, color = "#C05A47", size = 3) +
  annotate(
    "label",
    x = ifelse(
      topic7_case$fitted_score > mean(topic7_data$fitted_score),
      topic7_case$fitted_score - 3,
      topic7_case$fitted_score + 3
    ),
    y = topic7_case$reasoning_score,
    label = paste0(topic7_case$participant_id, topic7_text$residual_prefix, format_t07(topic7_case$residual, 2)),
    hjust = ifelse(topic7_case$fitted_score > mean(topic7_data$fitted_score), 1, 0),
    size = 3.1,
    fill = "#FFF8F5",
    color = "#713D31"
  ) +
  labs(
    title = topic7_text$fitted_title,
    subtitle = topic7_text$fitted_subtitle,
    x = topic7_labels$fitted,
    y = topic7_labels$observed
  ) +
  t07_theme()
attr(p_topic7_fitted, "ratiomera_plotly_kind") <- "fitted_residual"
attr(p_topic7_fitted, "ratiomera_skip_scalar_hover") <- TRUE

# Simulated-example diagnostics for the same full M4 model. These displays do
# not alter the fitted model; they show different aspects of its residuals and
# case geometry.
p_topic7_residual_diagnostic <- ggplot(
  topic7_data,
  aes(fitted_score, residual)
) +
  geom_hline(
    yintercept = 0,
    color = "#8B9AA6",
    linetype = "dashed",
    linewidth = 0.8
  ) +
  geom_point(aes(text = hover), color = "#2F6F9F", alpha = 0.6, size = 2) +
  labs(
    title = topic7_text$diagnostic_residual_title,
    subtitle = topic7_text$diagnostic_residual_subtitle,
    x = topic7_labels$fitted,
    y = topic7_labels$residual
  ) +
  t07_theme()
attr(p_topic7_residual_diagnostic, "ratiomera_skip_scalar_hover") <- TRUE

topic7_qq_data <- topic7_data |>
  arrange(standardized_residual) |>
  mutate(
    expected_quantile = qnorm(ppoints(n())),
    qq_hover = paste0(
      topic7_hover_text$participant, participant_id,
      "<br>", topic7_hover_text$expected_normal_quantile, format_t07(expected_quantile, 2),
      "<br>", topic7_hover_text$standardized_residual, format_t07(standardized_residual, 2)
    )
  )
topic7_qq_quartiles <- quantile(topic7_qq_data$standardized_residual, c(0.25, 0.75))
topic7_qq_reference_x <- qnorm(c(0.25, 0.75))
topic7_qq_reference_slope <- diff(topic7_qq_quartiles) / diff(topic7_qq_reference_x)
topic7_qq_reference_intercept <-
  topic7_qq_quartiles[[1]] - topic7_qq_reference_slope * topic7_qq_reference_x[[1]]

p_topic7_qq <- ggplot(
  topic7_qq_data,
  aes(expected_quantile, standardized_residual)
) +
  geom_abline(
    intercept = topic7_qq_reference_intercept,
    slope = topic7_qq_reference_slope,
    color = "#C05A47",
    linewidth = 0.9
  ) +
  geom_point(aes(text = qq_hover), color = "#2F6F9F", alpha = 0.65, size = 2) +
  labs(
    title = topic7_text$diagnostic_qq_title,
    subtitle = topic7_text$diagnostic_qq_subtitle,
    x = topic7_text$expected_normal_quantile,
    y = topic7_text$standardized_residual
  ) +
  t07_theme()
attr(p_topic7_qq, "ratiomera_skip_scalar_hover") <- TRUE

# Simulated-example semipartial display. Only practice hours are residualized;
# the raw outcome stays on the vertical axis.
topic7_semipartial_plot_data <- topic7_data |>
  mutate(
    label = paste0(
      topic7_hover_text$participant, participant_id,
      "<br>", topic7_text$practice_residual_prefix, format_t07(practice_after_prior, 2),
      "<br>", trimws(topic7_text$reasoning_score_prefix), " ", format_t07(reasoning_score, 1)
    )
  )

p_topic7_semipartial <- ggplot(
  topic7_semipartial_plot_data,
  aes(practice_after_prior, reasoning_score)
) +
  geom_vline(xintercept = 0, color = "#AAB6C0", linewidth = 0.6) +
  geom_point(aes(text = label), color = "#2F6F9F", alpha = 0.58, size = 2) +
  geom_smooth(method = "lm", formula = y ~ x, se = FALSE, color = "#C05A47", linewidth = 1) +
  labs(
    title = topic7_text$semipartial_title,
    subtitle = paste0(
      topic7_text$semipartial_subtitle_prefix,
      format_t07(topic7_semipartial_r, 3)
    ),
    x = topic7_text$semipartial_x,
    y = topic7_labels$outcome
  ) +
  t07_theme()
attr(p_topic7_semipartial, "ratiomera_skip_scalar_hover") <- TRUE

# Predictions at a representative prior score make the additive and
# interaction alternatives directly comparable.
topic7_interaction_grid <- expand_grid(
  practice_hours = seq(0, 12, length.out = 100),
  prior_score = 10,
  tutorial_format = factor(topic7_format_levels, levels = topic7_format_levels)
)

topic7_additive_predictions <- topic7_interaction_grid |>
  mutate(model = topic7_text$additive_model)
topic7_additive_predictions$fitted_score <- unname(
  predict(topic7_additive_model, newdata = topic7_additive_predictions)
)

topic7_interaction_predictions <- topic7_interaction_grid |>
  mutate(model = topic7_text$interaction_model)
topic7_interaction_predictions$fitted_score <- unname(
  predict(topic7_interaction_model, newdata = topic7_interaction_predictions)
)

topic7_interaction_plot_data <- bind_rows(
  topic7_additive_predictions,
  topic7_interaction_predictions
) |>
  mutate(
    model = factor(
      model,
      levels = c(topic7_text$additive_model, topic7_text$interaction_model)
    ),
    hover = paste0(
      topic7_hover_text$model, model,
      "<br>", topic7_hover_text$tutorial_format, tutorial_format,
      "<br>", topic7_hover_text$practice_hours, format_t07(practice_hours, 1),
      "<br>", topic7_hover_text$prior_score_held, format_t07(prior_score, 1),
      "<br>", topic7_hover_text$fitted_score, format_t07(fitted_score, 2)
    )
  )

p_topic7_interaction <- ggplot(
  topic7_interaction_plot_data,
  aes(practice_hours, fitted_score, color = tutorial_format, group = tutorial_format)
) +
  geom_line(aes(text = hover), linewidth = 1.15) +
  facet_wrap(
    ~model,
    ncol = 1,
    labeller = labeller(model = label_wrap_gen(width = 28))
  ) +
  scale_color_manual(values = c("#6C8799", "#2F6F9F", "#C05A47")) +
  scale_x_continuous(breaks = c(0, 4, 8, 12)) +
  labs(
    title = topic7_text$interaction_title,
    subtitle = topic7_text$interaction_subtitle,
    x = topic7_labels$practice,
    y = topic7_labels$fitted,
    color = sub(":$", "", trimws(topic7_hover_text$tutorial_format))
  ) +
  t07_theme() +
  theme(
    panel.spacing.y = grid::unit(1.5, "lines"),
    plot.margin = margin(12, 20, 12, 16)
  )
if (topic_locale == "de") {
  p_topic7_interaction <- p_topic7_interaction +
    theme(panel.spacing.y = grid::unit(1.5, "lines"))
}
attr(p_topic7_interaction, "ratiomera_plotly_kind") <- "interaction"
attr(p_topic7_interaction, "ratiomera_widget_height") <- 740

# The identical fitted relationship is repeated under all three possible
# reference choices. The reference group's line is emphasized in each panel.
topic7_reference_facet_prefix <- if (topic_locale == "de") {
  "Referenz:\n"
} else if (topic_locale == "sq") {
  "Referenca:\n"
} else {
  "Reference:\n"
}

topic7_reference_plot_data <- bind_rows(lapply(topic7_format_levels, function(reference_level) {
  topic7_interaction_predictions |>
    mutate(
      reference_category = factor(
        paste0(topic7_reference_facet_prefix, reference_level),
        levels = paste0(topic7_reference_facet_prefix, topic7_format_levels)
      ),
      is_reference = tutorial_format == reference_level,
      hover = paste0(
        topic7_hover_text$displayed_reference, reference_level,
        "<br>", topic7_hover_text$fitted_line, tutorial_format,
        "<br>", topic7_hover_text$practice_hours, format_t07(practice_hours, 1),
        "<br>", topic7_hover_text$prior_score_held, format_t07(prior_score, 1),
        "<br>", topic7_hover_text$fitted_score, format_t07(fitted_score, 2)
      )
    )
}))

p_topic7_reference <- ggplot(
  topic7_reference_plot_data,
  aes(
    practice_hours,
    fitted_score,
    group = tutorial_format,
    color = tutorial_format
  )
) +
  geom_line(
    data = filter(topic7_reference_plot_data, !is_reference),
    aes(text = hover),
    linewidth = 0.75,
    alpha = 0.55
  ) +
  geom_line(
    data = filter(topic7_reference_plot_data, is_reference),
    aes(text = hover),
    linewidth = 1.45,
    alpha = 1,
    show.legend = FALSE
  ) +
  facet_wrap(
    ~reference_category,
    ncol = 1,
    labeller = labeller(reference_category = label_wrap_gen(width = 28))
  ) +
  scale_color_manual(values = c("#6C8799", "#2F6F9F", "#C05A47")) +
  scale_x_continuous(breaks = c(0, 4, 8, 12)) +
  labs(
    title = topic7_text$reference_title,
    subtitle = topic7_text$reference_subtitle,
    x = topic7_labels$practice,
    y = topic7_labels$fitted,
    color = sub(":$", "", trimws(topic7_hover_text$tutorial_format))
  ) +
  t07_theme(base_size = 10.5) +
  guides(color = guide_legend(nrow = 1, byrow = TRUE)) +
  theme(
    panel.spacing.y = grid::unit(1.5, "lines"),
    plot.title = element_text(size = 13.5),
    plot.subtitle = element_text(size = 10.5),
    legend.margin = margin(t = 6),
    plot.margin = margin(14, 28, 14, 20)
  )
if (topic_locale == "de") {
  p_topic7_reference <- p_topic7_reference +
    theme(panel.spacing.y = grid::unit(1.5, "lines"))
}
attr(p_topic7_reference, "ratiomera_plotly_kind") <- "reference"
attr(p_topic7_reference, "ratiomera_widget_height") <- 930

topic7_fit_plot_data <- topic7_model_table |>
  select(model, r_squared, adjusted_r_squared) |>
  pivot_longer(
    c(r_squared, adjusted_r_squared),
    names_to = "fit_measure",
    values_to = "value"
  ) |>
  mutate(
    fit_measure = recode(
      fit_measure,
      r_squared = topic7_text$r_squared,
      adjusted_r_squared = topic7_text$adjusted_r_squared
    ),
    fit_measure = factor(
      fit_measure,
      levels = c(topic7_text$r_squared, topic7_text$adjusted_r_squared)
    ),
    model = factor(model, levels = names(topic7_models)),
    hover = paste0(
      topic7_hover_text$model, model,
      "<br>", topic7_hover_text$measure, fit_measure,
      "<br>", topic7_hover_text$value, format_t07(value, 3)
    )
  )

p_topic7_fit_path <- ggplot(
  topic7_fit_plot_data,
  aes(model, value, color = fit_measure, group = fit_measure)
) +
  geom_line(aes(text = hover), linewidth = 1) +
  geom_point(aes(text = hover), size = 3) +
  scale_color_manual(values = setNames(c("#2F6F9F", "#C05A47"), c(topic7_text$r_squared, topic7_text$adjusted_r_squared))) +
  scale_x_discrete(drop = FALSE) +
  scale_y_continuous(limits = c(0, 0.82), breaks = seq(0, 0.8, 0.2)) +
  labs(
    title = topic7_text$fit_title,
    subtitle = topic7_text$fit_subtitle,
    x = topic7_text$candidate_model,
    y = topic7_text$outcome_share,
    color = topic7_text$fit_legend_title
  ) +
  t07_theme() +
  guides(color = guide_legend(nrow = 1, byrow = TRUE)) +
  theme(
    legend.margin = margin(t = 6),
    plot.margin = margin(12, 20, 14, 18)
  )
attr(p_topic7_fit_path, "ratiomera_plotly_kind") <- "fit_path"
attr(p_topic7_fit_path, "ratiomera_widget_height") <- 580

topic7_stats <- list(
  n = topic7_n,
  predictor_correlation = cor(topic7_data$prior_score, topic7_data$practice_hours),
  outcome_prior_correlation = cor(topic7_data$reasoning_score, topic7_data$prior_score),
  outcome_practice_correlation = cor(topic7_data$reasoning_score, topic7_data$practice_hours),
  outcome_sd = sd(topic7_data$reasoning_score),
  prior_sd = sd(topic7_data$prior_score),
  practice_sd = sd(topic7_data$practice_hours),
  practice_slope_adjusted_numerator =
    cor(topic7_data$reasoning_score, topic7_data$practice_hours) -
      cor(topic7_data$reasoning_score, topic7_data$prior_score) *
      cor(topic7_data$prior_score, topic7_data$practice_hours),
  practice_slope_overlap_denominator =
    1 - cor(topic7_data$prior_score, topic7_data$practice_hours)^2,
  practice_slope_unit_ratio =
    sd(topic7_data$reasoning_score) / sd(topic7_data$practice_hours),
  prior_conditional_slope = unname(coef(topic7_continuous_model)[["prior_score"]]),
  practice_simple_slope = unname(coef(topic7_simple_practice_model)[["practice_hours"]]),
  practice_conditional_slope = unname(coef(topic7_continuous_model)[["practice_hours"]]),
  practice_standardized_coefficient = unname(
    coef(topic7_continuous_model)[["practice_hours"]] *
      sd(topic7_data$practice_hours) / sd(topic7_data$reasoning_score)
  ),
  full_practice_standard_error = unname(
    coef(summary(topic7_interaction_model))["practice_hours", "Std. Error"]
  ),
  full_practice_t = unname(
    coef(summary(topic7_interaction_model))["practice_hours", "t value"]
  ),
  full_r_squared = unname(topic7_full_summary$r.squared),
  full_adjusted_r_squared = unname(topic7_full_summary$adj.r.squared),
  full_residual_standard_error = unname(topic7_full_summary$sigma),
  full_predictor_parameters = length(coef(topic7_interaction_model)) - 1L,
  full_residual_df = df.residual(topic7_interaction_model),
  global_f = topic7_global_f,
  global_df1 = topic7_global_df1,
  global_df2 = topic7_global_df2,
  global_p = topic7_global_p,
  semipartial_r = topic7_semipartial_r,
  delta_r2 = topic7_delta_r2,
  case_id = topic7_case$participant_id,
  case_observed = topic7_case$reasoning_score,
  case_fitted = topic7_case$fitted_score,
  case_residual = topic7_case$residual,
  mean_leverage = mean(topic7_data$leverage),
  max_leverage = max(topic7_data$leverage),
  max_cooks_distance = max(topic7_data$cooks_distance),
  max_abs_standardized_residual = max(abs(topic7_data$standardized_residual)),
  most_influential_id = topic7_influence_table$participant_id[[1]],
  prior_min = min(topic7_data$prior_score),
  prior_max = max(topic7_data$prior_score),
  practice_min = min(topic7_data$practice_hours),
  practice_max = max(topic7_data$practice_hours),
  outcome_min = min(topic7_data$reasoning_score),
  outcome_max = max(topic7_data$reasoning_score)
)
