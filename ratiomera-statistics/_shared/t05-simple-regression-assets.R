# Shared data, calculations, tables, and figure geometry for Simple Linear
# Regression, Topic 5. Locale pages select reviewed learner-facing labels
# without changing the simulation, calculations, or numerical results.

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

topic5_label_sets <- list(
  en = list(
    participant_id = "Participant ID",
    study_hours = "Guided practice per week (hours)",
    assessment_score = "Statistical reasoning score",
    fitted_score = "Fitted score",
    residual = "Residual",
    standardized_residual = "Standardized residual",
    leverage = "Leverage",
    cooks_distance = "Cook's distance",
    intercept = "Intercept",
    slope = "Guided practice hours",
    regression = "Regression",
    residual_source = "Residual",
    total = "Total",
    candidate_ols = "Least-squares line",
    candidate_flat = "Flatter candidate",
    candidate_steep = "Steeper candidate",
    inside_range = "Within observed range",
    outside_range = "Outside observed range",
    estimate = "Estimate",
    standard_error = "Standard error",
    t_value = "t value",
    p_value = "p-value",
    ci_lower = "95% CI lower",
    ci_upper = "95% CI upper",
    source = "Source",
    df = "df",
    sum_squares = "Sum of squares",
    mean_square = "Mean square",
    f_value = "F value",
    quantity = "Quantity",
    value = "Value",
    method = "Calculation",
    interpretation = "Interpretation",
    prediction_status = "Status",
    candidate_line = "Candidate line",
    sse = "Sum of squared residuals",
    sample_size = "Sample size",
    pearson_correlation = "Pearson correlation",
    r_squared = "R-squared",
    residual_standard_error = "Residual standard error",
    residual_df = "Residual degrees of freedom",
    direct_estimate = "Direct model estimate",
    covariance_method = "Covariance divided by predictor variance",
    correlation_method = "Correlation times the SD ratio",
    standardized_slope_method = "Standardized simple-regression slope",
    observed_deviation = "Observed deviation from the outcome mean",
    explained_deviation = "Deviation represented by the fitted line",
    unexplained_deviation = "Residual",
    fit_title = "A Fitted Line Summarizes the Conditional Mean",
    fit_subtitle = "The orange segment is one observed residual",
    least_squares_title = "Least Squares Selects the Line with the Smallest SSE",
    least_squares_subtitle = "All three candidates pass through the sample means",
    extrapolation_title = "Predictions Become Extrapolations beyond the Observed Range",
    extrapolation_subtitle = "The dashed continuation is a mathematical extension, not observed evidence",
    outside_label = "No observed\npredictor values",
    residual_title = "Residuals versus Fitted Values",
    residual_subtitle = "Look for a roughly patternless band around zero",
    qq_title = "Normal Q-Q Plot of the Residuals",
    qq_subtitle = "Points close to the reference line are compatible with approximate normality",
    influence_title = "Leverage, Residual Size, and Influence",
    influence_subtitle = "Larger points have larger Cook's distances; investigate rather than delete",
    fitted_axis = "Fitted statistical reasoning score",
    residual_axis = "Residual (observed minus fitted)",
    theoretical_quantiles = "Theoretical normal quantiles",
    sample_quantiles = "Ordered standardized residuals",
    anatomy_title = "Anatomy of a Simple Regression Line",
    anatomy_subtitle = "The intercept positions the line; the slope sets its rise",
    anatomy_predictor = "Predictor X",
    anatomy_outcome = "Outcome Y",
    anatomy_intercept = "Intercept at X = 0",
    anatomy_run = "Run = 1 X unit",
    anatomy_rise = "Rise = slope",
    anatomy_fitted = "Fitted value",
    anatomy_observed = "Observed value",
    anatomy_residual = "Residual = observed - fitted",
    patterns_title = "Three Residual Patterns, Three Diagnostic Readings",
    patterns_subtitle = "Compare a horizontal band with curvature and a funnel-shaped spread",
    pattern_compatible = "Compatible horizontal band",
    pattern_curve = "Curvature: linearity problem",
    pattern_funnel = "Funnel: unequal variance",
    pattern_fitted = "Fitted value",
    pattern_residual = "Residual",
    alt_anatomy = paste(
      "Conceptual straight regression line with predictor X on the horizontal axis and outcome Y on the vertical axis.",
      "The intercept is marked where X equals zero.",
      "A horizontal one-unit run and its vertical rise show the slope.",
      "At one predictor value, a fitted point lies on the line, an observed point lies above it, and a vertical segment labels the residual as observed minus fitted."
    ),
    alt_patterns = paste(
      "Three side-by-side residual-versus-fitted plots.",
      "The first shows a roughly even horizontal band around zero, compatible with a linear constant-variance model.",
      "The second shows a U-shaped curve, indicating missed nonlinearity.",
      "The third shows a funnel that widens from left to right, indicating unequal residual variance."
    ),
    alt_fit = paste(
      "Scatterplot of 160 simulated students' guided practice hours and statistical reasoning scores.",
      "A rising fitted line summarizes the positive linear association.",
      "One vertical orange segment shows the residual between an observed and fitted score."
    ),
    alt_least_squares = paste(
      "Scatterplot with three candidate straight lines through the sample means.",
      "The least-squares line runs through the center of the point cloud and has the smallest sum of squared vertical residuals."
    ),
    alt_extrapolation = paste(
      "Scatterplot and fitted line across the observed range of guided practice hours.",
      "The line continues as a dashed segment into a shaded region with no observed predictor values, illustrating extrapolation."
    ),
    alt_residual = paste(
      "Residual-versus-fitted plot for the simulated regression.",
      "Points form a roughly even horizontal band around zero and the smooth line stays close to zero."
    ),
    alt_qq = paste(
      "Normal Q-Q plot of standardized regression residuals.",
      "Most points follow the diagonal reference line, with modest departures near the ends."
    ),
    alt_influence = paste(
      "Influence diagnostic plotting leverage against standardized residuals.",
      "Point size represents Cook's distance and the three largest values are labeled for investigation."
    )
  ),
  de = list(
    participant_id = "Teilnehmenden-ID",
    study_hours = "Angeleitete Übungszeit pro Woche (Stunden)",
    assessment_score = "Punktzahl zum statistischen Denken",
    fitted_score = "Angepasste Punktzahl",
    residual = "Residuum",
    standardized_residual = "Standardisiertes Residuum",
    leverage = "Hebelwert",
    cooks_distance = "Cook-Distanz",
    intercept = "Achsenabschnitt",
    slope = "Angeleitete Übungsstunden",
    regression = "Regression",
    residual_source = "Residuum",
    total = "Gesamt",
    candidate_ols = "Kleinste-Quadrate-Gerade",
    candidate_flat = "Flachere Kandidatin",
    candidate_steep = "Steilere Kandidatin",
    inside_range = "Innerhalb des beobachteten Bereichs",
    outside_range = "Ausserhalb des beobachteten Bereichs",
    estimate = "Schätzwert",
    standard_error = "Standardfehler",
    t_value = "t-Wert",
    p_value = "p-Wert",
    ci_lower = "Untere Grenze des 95%-KI",
    ci_upper = "Obere Grenze des 95%-KI",
    source = "Quelle",
    df = "df",
    sum_squares = "Quadratsumme",
    mean_square = "Mittlere Quadratsumme",
    f_value = "F-Wert",
    quantity = "Grösse",
    value = "Wert",
    method = "Berechnung",
    interpretation = "Interpretation",
    prediction_status = "Status",
    candidate_line = "Geradenkandidatin",
    sse = "Summe der quadrierten Residuen",
    sample_size = "Stichprobenumfang",
    pearson_correlation = "Pearson-Korrelation",
    r_squared = "Bestimmtheitsmass R²",
    residual_standard_error = "Residualstandardfehler",
    residual_df = "Residual-Freiheitsgrade",
    direct_estimate = "Direkte Modellschätzung",
    covariance_method = "Kovarianz geteilt durch die Prädiktorvarianz",
    correlation_method = "Korrelation mal Verhältnis der Standardabweichungen",
    standardized_slope_method = "Standardisierte Steigung der einfachen Regression",
    observed_deviation = "Beobachtete Abweichung vom Mittelwert des Ergebnisses",
    explained_deviation = "Von der angepassten Geraden dargestellte Abweichung",
    unexplained_deviation = "Residuum",
    fit_title = "Eine angepasste Gerade fasst den bedingten Mittelwert zusammen",
    fit_subtitle = "Die orange Strecke ist ein beobachtetes Residuum",
    least_squares_title = "Die gewöhnliche Methode der kleinsten Quadrate wählt die Gerade mit der kleinsten SSE",
    least_squares_subtitle = "Alle drei Kandidatengeraden verlaufen durch die Stichprobenmittelwerte",
    extrapolation_title = "Vorhersagen werden ausserhalb des beobachteten Bereichs zu Extrapolationen",
    extrapolation_subtitle = "Die gestrichelte Fortsetzung ist eine mathematische Verlängerung und keine beobachtete Evidenz",
    outside_label = "Keine beobachteten\nPrädiktorwerte",
    residual_title = "Residuen gegen angepasste Werte",
    residual_subtitle = "Achte auf ein ungefähr musterloses Band um null",
    qq_title = "Normal-Q-Q-Diagramm der Residuen",
    qq_subtitle = "Punkte nahe der Referenzgeraden sind mit annähernder Normalverteilung vereinbar",
    influence_title = "Hebelwert, Residualgrösse und Einfluss",
    influence_subtitle = "Grössere Punkte haben grössere Cook-Distanzen; untersuche sie, statt sie einfach zu löschen",
    fitted_axis = "Angepasste Punktzahl zum statistischen Denken",
    residual_axis = "Residuum (beobachtet minus angepasst)",
    theoretical_quantiles = "Theoretische Quantile der Normalverteilung",
    sample_quantiles = "Geordnete standardisierte Residuen",
    anatomy_title = "Anatomie einer einfachen Regressionsgeraden",
    anatomy_subtitle = "Der Achsenabschnitt positioniert die Gerade; die Steigung bestimmt ihren Anstieg",
    anatomy_predictor = "Prädiktor X",
    anatomy_outcome = "Ergebnis Y",
    anatomy_intercept = "Achsenabschnitt bei X = 0",
    anatomy_run = "Schritt = 1 X-Einheit",
    anatomy_rise = "Anstieg = Steigung",
    anatomy_fitted = "Angepasster Wert",
    anatomy_observed = "Beobachteter Wert",
    anatomy_residual = "Residuum = beobachtet - angepasst",
    patterns_title = "Drei Residualmuster, drei diagnostische Deutungen",
    patterns_subtitle = "Vergleiche ein horizontales Band mit einer Krümmung und einer trichterförmigen Streuung",
    pattern_compatible = "Vereinbares horizontales Band",
    pattern_curve = "Krümmung: Linearitätsproblem",
    pattern_funnel = "Trichter: ungleiche Varianz",
    pattern_fitted = "Angepasster Wert",
    pattern_residual = "Residuum",
    alt_anatomy = paste(
      "Konzeptionelle gerade Regressionslinie mit dem Prädiktor X auf der horizontalen Achse und dem Ergebnis Y auf der vertikalen Achse.",
      "Der Achsenabschnitt ist an der Stelle X gleich null markiert.",
      "Ein horizontaler Schritt um eine Einheit und sein vertikaler Anstieg zeigen die Steigung.",
      "Bei einem Prädiktorwert liegt ein angepasster Punkt auf der Geraden, ein beobachteter Punkt darüber und eine vertikale Strecke kennzeichnet das Residuum als beobachtet minus angepasst."
    ),
    alt_patterns = paste(
      "Drei nebeneinanderliegende Diagramme der Residuen gegen die angepassten Werte.",
      "Das erste zeigt ein ungefähr gleichmässiges horizontales Band um null, das mit einem linearen Modell mit konstanter Varianz vereinbar ist.",
      "Das zweite zeigt eine U-förmige Kurve, die auf übersehene Nichtlinearität hinweist.",
      "Das dritte zeigt einen von links nach rechts breiter werdenden Trichter, der auf ungleiche Residualvarianz hinweist."
    ),
    alt_fit = paste(
      "Streudiagramm der angeleiteten Übungsstunden und der Punktzahlen zum statistischen Denken von 160 simulierten Studierenden.",
      "Eine ansteigende angepasste Gerade fasst die positive lineare Beziehung zusammen.",
      "Eine vertikale orange Strecke zeigt das Residuum zwischen einer beobachteten und einer angepassten Punktzahl."
    ),
    alt_least_squares = paste(
      "Streudiagramm mit drei möglichen Geraden durch die Stichprobenmittelwerte.",
      "Die Kleinste-Quadrate-Gerade verläuft durch das Zentrum der Punktwolke und besitzt die kleinste Summe quadrierter vertikaler Residuen."
    ),
    alt_extrapolation = paste(
      "Streudiagramm und angepasste Gerade im beobachteten Bereich der angeleiteten Übungsstunden.",
      "Die Gerade setzt sich als gestrichelte Strecke in einen schattierten Bereich ohne beobachtete Prädiktorwerte fort und veranschaulicht so eine Extrapolation."
    ),
    alt_residual = paste(
      "Diagramm der Residuen gegen die angepassten Werte für die simulierte Regression.",
      "Die Punkte bilden ein ungefähr gleichmässiges horizontales Band um null und die geglättete Linie bleibt nahe bei null."
    ),
    alt_qq = paste(
      "Normal-Q-Q-Diagramm der standardisierten Regressionsresiduen.",
      "Die meisten Punkte folgen der diagonalen Referenzgeraden; an den Enden gibt es leichte Abweichungen."
    ),
    alt_influence = paste(
      "Einflussdiagnose, in der Hebelwerte gegen standardisierte Residuen aufgetragen sind.",
      "Die Punktgrösse stellt die Cook-Distanz dar und die drei grössten Werte sind zur Untersuchung beschriftet."
    )
  ),
  sq = list(
    participant_id = "ID-ja e pjesëmarrësit",
    study_hours = "Ushtrimi i udhëzuar në javë (orë)",
    assessment_score = "Pikët e arsyetimit statistikor",
    fitted_score = "Pikët e përshtatura",
    residual = "Reziduali",
    standardized_residual = "Reziduali i standardizuar",
    leverage = "Leverage-i",
    cooks_distance = "Largësia e Cook-ut",
    intercept = "Prerja me boshtin",
    slope = "Orët e ushtrimit të udhëzuar",
    regression = "Regresioni",
    residual_source = "Reziduali",
    total = "Gjithsej",
    candidate_ols = "Vija e katrorëve më të vegjël",
    candidate_flat = "Vija kandidate më e sheshtë",
    candidate_steep = "Vija kandidate më e pjerrët",
    inside_range = "Brenda diapazonit të vrojtuar",
    outside_range = "Jashtë diapazonit të vrojtuar",
    estimate = "Vlerësimi",
    standard_error = "Gabimi standard",
    t_value = "Vlera t",
    p_value = "Vlera p",
    ci_lower = "Kufiri i poshtëm i intervalit të besimit 95%",
    ci_upper = "Kufiri i sipërm i intervalit të besimit 95%",
    source = "Burimi",
    df = "df",
    sum_squares = "Shuma e katrorëve",
    mean_square = "Katrori mesatar",
    f_value = "Vlera F",
    quantity = "Madhësia",
    value = "Vlera",
    method = "Llogaritja",
    interpretation = "Interpretimi",
    prediction_status = "Statusi",
    candidate_line = "Vija kandidate",
    sse = "Shuma e rezidualeve të ngritura në katror",
    sample_size = "Madhësia e kampionit",
    pearson_correlation = "Korrelacioni i Pearson-it",
    r_squared = "R²",
    residual_standard_error = "Gabimi standard i rezidualeve",
    residual_df = "Shkallët e lirisë të rezidualeve",
    direct_estimate = "Vlerësimi i drejtpërdrejtë i modelit",
    covariance_method = "Kovarianca pjesëtuar me variancën e ndryshores parashikuese",
    correlation_method = "Korrelacioni shumëzuar me raportin e devijimeve standarde",
    standardized_slope_method = "Pjerrësia e standardizuar e regresionit të thjeshtë",
    observed_deviation = "Shmangia e vrojtuar nga mesatarja e rezultatit",
    explained_deviation = "Shmangia e përfaqësuar nga vija e përshtatur",
    unexplained_deviation = "Reziduali",
    fit_title = "Një vijë e përshtatur përmbledh mesataren e kushtëzuar",
    fit_subtitle = "Segmenti portokalli është një rezidual i vrojtuar",
    least_squares_title = "Metoda e katrorëve më të vegjël zgjedh vijën me SSE-në më të vogël",
    least_squares_subtitle = "Të tria vijat kandidate kalojnë nëpër mesataret e kampionit",
    extrapolation_title = "Parashikimet bëhen ekstrapolime përtej diapazonit të vrojtuar",
    extrapolation_subtitle = "Vazhdimi me vija të ndërprera është zgjatim matematikor, jo dëshmi e vrojtuar",
    outside_label = "Nuk ka vlera\ntë vrojtuara për\nndryshoren parashikuese",
    residual_title = "Rezidualet kundrejt vlerave të përshtatura",
    residual_subtitle = "Kërko një brez përafërsisht pa model rreth zeros",
    qq_title = "Diagrami normal Q-Q i rezidualeve",
    qq_subtitle = "Pikat pranë vijës referuese përputhen me normalitetin e përafërt",
    influence_title = "Leverage-i, madhësia e rezidualit dhe ndikimi",
    influence_subtitle = "Pikat më të mëdha kanë largësi më të mëdha të Cook-ut; shqyrtoji në vend se t'i fshish",
    fitted_axis = "Pikët e përshtatura të arsyetimit statistikor",
    residual_axis = "Reziduali (vlera e vrojtuar minus vlera e përshtatur)",
    theoretical_quantiles = "Kuantilet teorike të shpërndarjes normale",
    sample_quantiles = "Rezidualet e standardizuara të renditura",
    anatomy_title = "Anatomia e një vije të thjeshtë regresioni",
    anatomy_subtitle = "Prerja me boshtin e pozicionon vijën; pjerrësia përcakton ngritjen e saj",
    anatomy_predictor = "Ndryshorja parashikuese X",
    anatomy_outcome = "Rezultati Y",
    anatomy_intercept = "Prerja me boshtin kur X = 0",
    anatomy_run = "Hapi = 1 njësi e X",
    anatomy_rise = "Ngritja = pjerrësia",
    anatomy_fitted = "Vlera e përshtatur",
    anatomy_observed = "Vlera e vrojtuar",
    anatomy_residual = "Reziduali = vlera e vrojtuar - vlera e përshtatur",
    patterns_title = "Tri modele rezidualesh, tri lexime diagnostike",
    patterns_subtitle = "Krahaso një brez horizontal me një lakore dhe një shpërndarje në formë hinke",
    pattern_compatible = "Brez horizontal i pajtueshëm",
    pattern_curve = "Lakore: problem lineariteti",
    pattern_funnel = "Hinkë: variancë e pabarabartë",
    pattern_fitted = "Vlera e përshtatur",
    pattern_residual = "Reziduali",
    alt_anatomy = paste(
      "Vijë konceptuale e drejtë regresioni me ndryshoren parashikuese X në boshtin horizontal dhe rezultatin Y në boshtin vertikal.",
      "Prerja me boshtin shënohet aty ku X është zero.",
      "Një hap horizontal prej një njësie dhe ngritja përkatëse vertikale tregojnë pjerrësinë.",
      "Në një vlerë të ndryshores parashikuese, pika e përshtatur ndodhet në vijë, pika e vrojtuar ndodhet mbi të dhe segmenti vertikal e emërton rezidualin si vlera e vrojtuar minus vlera e përshtatur."
    ),
    alt_patterns = paste(
      "Tri diagrame krah për krah të rezidualeve kundrejt vlerave të përshtatura.",
      "I pari tregon një brez horizontal përafërsisht të njëtrajtshëm rreth zeros, i pajtueshëm me një model linear me variancë konstante.",
      "I dyti tregon një lakore në formë U-je, e cila sinjalizon jolinearitet të pakapur nga modeli.",
      "I treti tregon një hinkë që zgjerohet nga e majta në të djathtë, e cila sinjalizon variancë të pabarabartë të rezidualeve."
    ),
    alt_fit = paste(
      "Diagram shpërndarjeje i orëve të ushtrimit të udhëzuar dhe pikëve të arsyetimit statistikor për 160 studentë të simuluar.",
      "Një vijë e përshtatur që ngrihet përmbledh lidhjen pozitive lineare.",
      "Një segment vertikal portokalli tregon rezidualin mes pikëve të vrojtuara dhe atyre të përshtatura."
    ),
    alt_least_squares = paste(
      "Diagram shpërndarjeje me tri vija të drejta kandidate që kalojnë nëpër mesataret e kampionit.",
      "Vija e katrorëve më të vegjël kalon nëpër qendrën e resë së pikave dhe ka shumën më të vogël të rezidualeve vertikale të ngritura në katror."
    ),
    alt_extrapolation = paste(
      "Diagram shpërndarjeje dhe vijë e përshtatur në tërë diapazonin e vrojtuar të orëve të ushtrimit të udhëzuar.",
      "Vija vazhdon si segment me vija të ndërprera në një zonë të hijezuar pa vlera të vrojtuara të ndryshores parashikuese, duke ilustruar ekstrapolimin."
    ),
    alt_residual = paste(
      "Diagram i rezidualeve kundrejt vlerave të përshtatura për regresionin e simuluar.",
      "Pikat formojnë një brez horizontal përafërsisht të njëtrajtshëm rreth zeros dhe vija e lëmuar qëndron pranë zeros."
    ),
    alt_qq = paste(
      "Diagram normal Q-Q i rezidualeve të standardizuara të regresionit.",
      "Shumica e pikave ndjekin vijën diagonale referuese, me shmangie të lehta pranë skajeve."
    ),
    alt_influence = paste(
      "Diagnostikë e ndikimit ku leverage-i vendoset kundrejt rezidualeve të standardizuara.",
      "Madhësia e pikës përfaqëson largësinë e Cook-ut dhe tri vlerat më të mëdha etiketohen për shqyrtim."
    )
  )
)

if (!topic_locale %in% names(topic5_label_sets)) {
  stop(
    "Topic 5 labels have not yet been reviewed for locale: ",
    topic_locale,
    call. = FALSE
  )
}
topic5_labels <- topic5_label_sets[[topic_locale]]

required_topic5_packages <- c(
  "dplyr", "tibble", "tidyr", "ggplot2", "DT", "plotly", "htmlwidgets", "knitr"
)
missing_topic5_packages <- required_topic5_packages[
  !vapply(required_topic5_packages, requireNamespace, logical(1), quietly = TRUE)
]
if (length(missing_topic5_packages)) {
  stop(
    "Topic 5 requires these R packages: ",
    paste(missing_topic5_packages, collapse = ", "),
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

fmt_num <- function(x, digits = 2) {
  formatC(x, format = "f", digits = digits, big.mark = ",")
}

fmt_p <- function(x) {
  ifelse(
    is.na(x),
    "",
    ifelse(x < 0.001, "< .001", sub("^0", "", sprintf("%.3f", x)))
  )
}

topic5_theme <- function(base_size = 12) {
  theme_minimal(base_size = base_size) +
    theme(
      plot.title = element_text(face = "bold", color = "#172B3A"),
      plot.subtitle = element_text(color = "#536475"),
      axis.title = element_text(color = "#34495E"),
      axis.text = element_text(color = "#465A6B"),
      legend.title = element_blank(),
      legend.text = element_text(color = "#34495E"),
      panel.grid.minor = element_blank(),
      panel.grid.major = element_line(color = "#E7ECF1"),
      plot.background = element_rect(fill = "white", color = NA)
    )
}

topic5_plotly <- function(
  plot,
  kind = c(
    "anatomy", "ss_geometry", "patterns", "fit", "least_squares", "extrapolation",
    "residual", "qq", "influence"
  )
) {
  kind <- match.arg(kind)
  top_margin <- if (identical(kind, "patterns")) 140 else 80
  alt_text <- switch(
    kind,
    anatomy = topic5_labels$alt_anatomy,
    ss_geometry = ratiomera_plotly_alt_from_plot(plot, topic_locale),
    patterns = topic5_labels$alt_patterns,
    fit = topic5_labels$alt_fit,
    least_squares = topic5_labels$alt_least_squares,
    extrapolation = topic5_labels$alt_extrapolation,
    residual = topic5_labels$alt_residual,
    qq = topic5_labels$alt_qq,
    influence = topic5_labels$alt_influence
  )
  tooltip_fields <- if (kind %in% c("anatomy", "ss_geometry")) {
    c("label", "x", "y")
  } else {
    "text"
  }
  hover_enabled <- TRUE

  plot <- ratiomera_make_plotly_compatible(plot)
  widget <- ggplotly(
    plot,
    tooltip = tooltip_fields,
    dynamicTicks = TRUE
  ) |>
    ratiomera_prepare_plotly_widget(
      title_width = 40,
      axis_width = 28,
      annotation_width = 30
    )

  widget$x$data <- lapply(widget$x$data, function(trace) {
    if (!is.null(trace$name) && identical(trace$name, "fitted values")) {
      trace$name <- topic5_labels$fitted_score
    }
    trace
  })
  widget <- ratiomera_localize_plotly_hover(
    widget,
    ratiomera_plotly_hover_labels(plot, topic_locale)
  )

  if (identical(kind, "least_squares")) {
    widget$x$data <- lapply(widget$x$data, function(trace) {
      if (isTRUE(trace$showlegend) && !is.null(trace$name)) {
        trace$name <- ratiomera_wrap_plotly_text(trace$name, width = 16)
      }
      trace
    })
  }

  # Reference lines, residual guides, shaded areas, and fixed annotations do
  # not represent additional cases. Suppress their duplicate scalar hover so
  # that the learner encounters only the observation and fitted-line detail.
  if (kind %in% c("fit", "extrapolation")) {
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

  if (identical(kind, "extrapolation")) {
    # Replace ggplotly's unboxed text trace with one native annotation. The
    # light background keeps the observed-range boundary from running through
    # the note, while the centered paper-safe position retains every localized
    # line inside the widget at phone width.
    widget$x$data <- lapply(widget$x$data, function(trace) {
      if (
        identical(trace$type, "scatter") &&
        identical(trace$mode, "text") &&
        !is.null(trace$text) &&
        any(grepl("observed|beobacht|vrojtuar", trace$text, ignore.case = TRUE))
      ) {
        trace$visible <- FALSE
      }
      trace
    })
    widget$x$layout$annotations <- c(
      widget$x$layout$annotations,
      list(list(
        x = 18.0,
        y = min(dat$assessment_score) + 4,
        xref = "x",
        yref = "y",
        text = gsub("\n", "<br>", topic5_labels$outside_label, fixed = TRUE),
        showarrow = FALSE,
        xanchor = "center",
        yanchor = "middle",
        align = "center",
        bgcolor = "rgba(255,255,255,0.92)",
        bordercolor = "#D8E0E6",
        borderwidth = 1,
        borderpad = 3,
        font = list(color = "#8A3F36", size = 10)
      ))
    )
  }

  # The sum-of-squares diagram labels its three colored boxes directly.
  # ggplotly otherwise exposes the identity-fill tuples as legend text such
  # as "(#EAF4EF,1)", which is implementation detail rather than instruction.
  if (identical(kind, "ss_geometry")) {
    widget$x$data <- lapply(widget$x$data, function(trace) {
      trace$showlegend <- FALSE
      trace
    })
    widget$x$layout$showlegend <- FALSE
  }

  bottom_margin <- if (identical(kind, "least_squares")) 176 else 72
  right_margin <- if (identical(kind, "extrapolation")) 44 else 28

  widget <- widget |>
    layout(
      autosize = TRUE,
      hovermode = if (hover_enabled) "closest" else FALSE,
      hoverlabel = list(
        bgcolor = "white",
        bordercolor = "#AAB6C0",
        font = list(color = "#172B3A")
      ),
      margin = list(l = 72, r = right_margin, b = bottom_margin, t = top_margin, pad = 2)
    )

  if (identical(kind, "least_squares")) {
    widget <- widget |>
      layout(
        legend = list(
          orientation = "h",
          x = 0.5,
          xanchor = "center",
          y = -0.42,
          yanchor = "top",
          font = list(size = 11)
        )
      )
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

# Deterministic instructional cohort. These are simulated values, not empirical
# observations or claims about real students.
set.seed(42)
n <- 160
dat <- tibble(
  participant_id = sprintf("S%03d", seq_len(n)),
  study_hours = round(runif(n, min = 0, max = 16), 1),
  assessment_score = round(
    42 + 2.15 * study_hours + rnorm(n, mean = 0, sd = 6.5),
    1
  )
)

simple_model <- lm(assessment_score ~ study_hours, data = dat)
model_summary <- summary(simple_model)

dat <- dat |>
  mutate(
    fitted_score = unname(fitted(simple_model)),
    residual = unname(residuals(simple_model)),
    standardized_residual = unname(rstandard(simple_model)),
    leverage = unname(hatvalues(simple_model)),
    cooks_distance = unname(cooks.distance(simple_model)),
    hover_observation = paste0(
      topic5_labels$participant_id, ": ", participant_id,
      "<br>", topic5_labels$study_hours, ": ", formatC(study_hours, format = "f", digits = 1),
      "<br>", topic5_labels$assessment_score, ": ", formatC(assessment_score, format = "f", digits = 1),
      "<br>", topic5_labels$fitted_score, ": ", formatC(fitted_score, format = "f", digits = 2),
      "<br>", topic5_labels$residual, ": ", formatC(residual, format = "f", digits = 2)
    ),
    hover_residual = paste0(
      topic5_labels$participant_id, ": ", participant_id,
      "<br>", topic5_labels$fitted_score, ": ", formatC(fitted_score, format = "f", digits = 2),
      "<br>", topic5_labels$residual, ": ", formatC(residual, format = "f", digits = 2)
    ),
    hover_influence = paste0(
      topic5_labels$participant_id, ": ", participant_id,
      "<br>", topic5_labels$leverage, ": ", formatC(leverage, format = "f", digits = 3),
      "<br>", topic5_labels$standardized_residual, ": ", formatC(standardized_residual, format = "f", digits = 2),
      "<br>", topic5_labels$cooks_distance, ": ", formatC(cooks_distance, format = "f", digits = 3)
    )
  )

display_dat <- dat |>
  transmute(
    !!topic5_labels$participant_id := participant_id,
    !!topic5_labels$study_hours := study_hours,
    !!topic5_labels$assessment_score := assessment_score
  )

x_bar <- mean(dat$study_hours)
y_bar <- mean(dat$assessment_score)
s_x <- sd(dat$study_hours)
s_y <- sd(dat$assessment_score)
s_xy <- cov(dat$study_hours, dat$assessment_score)
r_xy <- cor(dat$study_hours, dat$assessment_score)

b0_hat <- unname(coef(simple_model)[1])
b1_hat <- unname(coef(simple_model)[2])
b1_from_covariance <- s_xy / s_x^2
b1_from_correlation <- r_xy * s_y / s_x
b0_from_means <- y_bar - b1_hat * x_bar
standardized_slope <- unname(
  coef(lm(as.numeric(scale(assessment_score)) ~ as.numeric(scale(study_hours)), data = dat))[2]
)

ss_total <- sum((dat$assessment_score - y_bar)^2)
ss_regression <- sum((dat$fitted_score - y_bar)^2)
ss_residual <- sum(dat$residual^2)
df_regression <- 1L
df_residual <- n - 2L
df_total <- n - 1L
ms_regression <- ss_regression / df_regression
ms_residual <- ss_residual / df_residual
f_statistic <- ms_regression / ms_residual
model_p_value <- pf(f_statistic, df_regression, df_residual, lower.tail = FALSE)
r_squared <- unname(model_summary$r.squared)
residual_standard_error <- unname(model_summary$sigma)

coefficient_matrix <- coef(model_summary)
coefficient_ci <- confint(simple_model, level = 0.95)
coefficient_table <- tibble(
  term = c(topic5_labels$intercept, topic5_labels$slope),
  estimate = unname(coefficient_matrix[, "Estimate"]),
  standard_error = unname(coefficient_matrix[, "Std. Error"]),
  t_value = unname(coefficient_matrix[, "t value"]),
  p_value = unname(coefficient_matrix[, "Pr(>|t|)"]),
  ci_lower = unname(coefficient_ci[, 1]),
  ci_upper = unname(coefficient_ci[, 2])
)

anova_table <- tibble(
  source = c(topic5_labels$regression, topic5_labels$residual_source, topic5_labels$total),
  df = c(df_regression, df_residual, df_total),
  sum_squares = c(ss_regression, ss_residual, ss_total),
  mean_square = c(ms_regression, ms_residual, NA_real_),
  f_value = c(f_statistic, NA_real_, NA_real_),
  p_value = c(model_p_value, NA_real_, NA_real_)
)

fit_table <- tibble(
  quantity = c(
    topic5_labels$sample_size,
    topic5_labels$pearson_correlation,
    topic5_labels$r_squared,
    topic5_labels$residual_standard_error,
    topic5_labels$residual_df
  ),
  value = c(n, r_xy, r_squared, residual_standard_error, df_residual)
)

identity_table <- tibble(
  method = c(
    topic5_labels$direct_estimate,
    topic5_labels$covariance_method,
    topic5_labels$correlation_method,
    topic5_labels$standardized_slope_method
  ),
  value = c(b1_hat, b1_from_covariance, b1_from_correlation, standardized_slope)
)

focal_candidates <- which(abs(dat$study_hours - 8) <= 1)
focal_index <- focal_candidates[
  which.max(abs(dat$residual[focal_candidates]))
]
focal_case <- dat[focal_index, ]

focal_table <- focal_case |>
  transmute(
    !!topic5_labels$participant_id := participant_id,
    !!topic5_labels$study_hours := study_hours,
    !!topic5_labels$assessment_score := assessment_score,
    !!topic5_labels$fitted_score := fitted_score,
    !!topic5_labels$residual := residual
  )

residual_preview <- dat |>
  slice_head(n = 8) |>
  transmute(
    !!topic5_labels$participant_id := participant_id,
    !!topic5_labels$study_hours := study_hours,
    !!topic5_labels$assessment_score := assessment_score,
    !!topic5_labels$fitted_score := fitted_score,
    !!topic5_labels$residual := residual
  )

decomposition_table <- tibble(
  quantity = c(
    topic5_labels$observed_deviation,
    topic5_labels$explained_deviation,
    topic5_labels$unexplained_deviation
  ),
  value = c(
    focal_case$assessment_score - y_bar,
    focal_case$fitted_score - y_bar,
    focal_case$residual
  )
)

candidate_slopes <- c(
  flat = 0.60 * b1_hat,
  ols = b1_hat,
  steep = 1.40 * b1_hat
)
candidate_names <- c(
  flat = topic5_labels$candidate_flat,
  ols = topic5_labels$candidate_ols,
  steep = topic5_labels$candidate_steep
)
candidate_lines <- tibble(
  candidate_key = names(candidate_slopes),
  candidate_line = unname(candidate_names[names(candidate_slopes)]),
  slope = unname(candidate_slopes),
  intercept = y_bar - unname(candidate_slopes) * x_bar
) |>
  rowwise() |>
  mutate(
    sse = sum(
      (dat$assessment_score - (intercept + slope * dat$study_hours))^2
    )
  ) |>
  ungroup() |>
  mutate(
    candidate_line = factor(
      candidate_line,
      levels = c(
        topic5_labels$candidate_ols,
        topic5_labels$candidate_flat,
        topic5_labels$candidate_steep
      )
    )
  )

candidate_grid <- tidyr::crossing(
  candidate_key = names(candidate_slopes),
  study_hours = seq(min(dat$study_hours), max(dat$study_hours), length.out = 120)
) |>
  left_join(candidate_lines, by = "candidate_key") |>
  mutate(
    predicted = intercept + slope * study_hours,
    hover_text = paste0(
      topic5_labels$candidate_line, ": ", as.character(candidate_line),
      "<br>", topic5_labels$study_hours, ": ", formatC(study_hours, format = "f", digits = 1),
      "<br>", topic5_labels$fitted_score, ": ", formatC(predicted, format = "f", digits = 2),
      "<br>", topic5_labels$sse, ": ", formatC(sse, format = "f", digits = 1, big.mark = ",")
    )
  )

prediction_hours <- c(10, 20)
prediction_table <- tibble(
  study_hours = prediction_hours,
  fitted_score = unname(
    predict(simple_model, newdata = tibble(study_hours = prediction_hours))
  ),
  status = c(topic5_labels$inside_range, topic5_labels$outside_range)
)

diagnostic_table <- dat |>
  arrange(desc(cooks_distance)) |>
  slice_head(n = 5) |>
  transmute(
    !!topic5_labels$participant_id := participant_id,
    !!topic5_labels$study_hours := study_hours,
    !!topic5_labels$assessment_score := assessment_score,
    !!topic5_labels$standardized_residual := standardized_residual,
    !!topic5_labels$leverage := leverage,
    !!topic5_labels$cooks_distance := cooks_distance
  )

regression_stats <- list(
  n = n,
  x_min = min(dat$study_hours),
  x_max = max(dat$study_hours),
  y_min = min(dat$assessment_score),
  y_max = max(dat$assessment_score),
  x_mean = x_bar,
  y_mean = y_bar,
  x_sd = s_x,
  y_sd = s_y,
  covariance = s_xy,
  correlation = r_xy,
  intercept = b0_hat,
  slope = b1_hat,
  standardized_slope = standardized_slope,
  ss_total = ss_total,
  ss_regression = ss_regression,
  ss_residual = ss_residual,
  r_squared = r_squared,
  correlation_squared = r_xy^2,
  residual_standard_error = residual_standard_error,
  residual_df = df_residual,
  slope_se = coefficient_table$standard_error[2],
  slope_t = coefficient_table$t_value[2],
  slope_p = coefficient_table$p_value[2],
  slope_ci_low = coefficient_table$ci_lower[2],
  slope_ci_high = coefficient_table$ci_upper[2],
  f_statistic = f_statistic,
  model_p = model_p_value,
  focal_id = focal_case$participant_id,
  focal_x = focal_case$study_hours,
  focal_y = focal_case$assessment_score,
  focal_fitted = focal_case$fitted_score,
  focal_residual = focal_case$residual,
  in_range_prediction = prediction_table$fitted_score[1],
  extrapolated_prediction = prediction_table$fitted_score[2]
)

# Conceptual Theory figure: begin with an unlabeled point cloud before showing
# any fitted-line anatomy. The small teaching dataset is deliberately separate
# from the simulated study. It gives every locale the same geometry while the
# prompt, axes, and accessible description remain fully localized.
guided_cloud_data <- tibble(
  study_hours = c(1.0, 1.7, 2.5, 3.2, 4.1, 5.0, 5.8, 6.7, 7.5, 8.4),
  test_score = c(48, 54, 52, 61, 59, 68, 73, 70, 80, 84)
)

guided_cloud_text <- if (topic_locale == "de") {
  list(
    title = "Bevor wir eine Gerade anpassen:\nWas siehst du in der Punktwolke?",
    subtitle = "Betrachte zuerst Richtung, Mitte und Streuung;\nzeichne noch keine Gerade",
    x_axis = "Lernzeit vor der Prüfung (Stunden)",
    y_axis = "Prüfungsergebnis (Punkte)",
    prompt = "Welche Gerade würde durch die Mitte der Punkte verlaufen?",
    alt = paste(
      "Streudiagramm von zehn erfundenen Lernzeiten und Prüfungsergebnissen ohne eingezeichnete Gerade.",
      "Die Punktwolke steigt insgesamt von links unten nach rechts oben, doch die Punkte liegen nicht auf einer einzigen Geraden.",
      "Eine Frage im freien oberen Bereich fordert dazu auf, eine Gerade durch die Mitte der Punktwolke zu erwägen."
    )
  )
} else if (topic_locale == "sq") {
  list(
    title = "Para se ta përshtatim vijën:\nÇfarë sheh në renë e pikave?",
    subtitle = "Shiko fillimisht drejtimin, qendrën dhe shpërndarjen;\nmos vizato ende vijë",
    x_axis = "Koha e studimit para testit (orë)",
    y_axis = "Rezultati në test (pikë)",
    prompt = "Cila vijë do të kalonte nëpër mesin e pikave?",
    alt = paste(
      "Diagram shpërndarjeje me dhjetë kohë studimi dhe rezultate testi të sajuara, pa vijë të vizatuar.",
      "Reja e pikave ngrihet në përgjithësi nga poshtë majtas drejt lart djathtas, por pikat nuk shtrihen në një vijë të vetme.",
      "Një pyetje në hapësirën e lirë sipër fton lexuesin të mendojë për një vijë që kalon nëpër mesin e resë së pikave."
    )
  )
} else {
  list(
    title = "Before We Fit a Line:\nWhat Do You See in the Point Cloud?",
    subtitle = "Look first at direction, center, and scatter;\ndo not draw a line yet",
    x_axis = "Study time before the test (hours)",
    y_axis = "Test result (points)",
    prompt = "Which line would pass through the middle of the points?",
    alt = paste(
      "Scatterplot of ten invented study times and test results with no line drawn.",
      "The point cloud generally rises from lower left to upper right, but the points do not lie on one line.",
      "A question in the open upper area invites the reader to consider a line through the middle of the point cloud."
    )
  )
}

p_regression_guided_cloud <- ggplot(
  guided_cloud_data,
  aes(study_hours, test_score)
) +
  geom_point(
    shape = 21,
    size = 4.2,
    stroke = 0.9,
    fill = "#DCECF6",
    color = "#245B7D"
  ) +
  annotate(
    "label",
    x = 4.65,
    y = 87.2,
    label = guided_cloud_text$prompt,
    fill = "#FFF7EB",
    color = "#6F4324",
    fontface = "bold",
    size = 3.45,
    label.padding = grid::unit(0.18, "lines"),
    linewidth = 0.3
  ) +
  scale_x_continuous(breaks = 1:9, limits = c(0.5, 9)) +
  scale_y_continuous(breaks = seq(45, 90, by = 5), limits = c(44, 91)) +
  labs(
    title = guided_cloud_text$title,
    subtitle = guided_cloud_text$subtitle,
    x = guided_cloud_text$x_axis,
    y = guided_cloud_text$y_axis
  ) +
  topic5_theme(base_size = 11.5) +
  theme(plot.margin = margin(14, 20, 14, 16))

# Conceptual Theory figure: the four anatomical parts of a simple fitted line.
# Values are deliberately simple and separate from the simulated study.
anatomy_intercept <- 2.0
anatomy_slope <- 1.2
anatomy_line <- tibble(
  x = seq(0, 6, length.out = 160),
  y = anatomy_intercept + anatomy_slope * x
)
anatomy_step_x0 <- 1.2
anatomy_step_x1 <- anatomy_step_x0 + 1
anatomy_step_y0 <- anatomy_intercept + anatomy_slope * anatomy_step_x0
anatomy_step_y1 <- anatomy_intercept + anatomy_slope * anatomy_step_x1
anatomy_case <- tibble(
  x = 4.4,
  fitted = anatomy_intercept + anatomy_slope * x,
  observed = anatomy_intercept + anatomy_slope * x + 1.45
)

p_regression_anatomy <- ggplot(anatomy_line, aes(x, y)) +
  geom_line(color = "#173F5F", linewidth = 1.25) +
  geom_point(
    data = tibble(x = 0, y = anatomy_intercept),
    aes(x, y),
    color = "#2E6DA4",
    size = 3.2,
    inherit.aes = FALSE
  ) +
  annotate(
    "segment",
    x = anatomy_step_x0,
    xend = anatomy_step_x1,
    y = anatomy_step_y0,
    yend = anatomy_step_y0,
    color = "#3F8B6D",
    linewidth = 1.15
  ) +
  annotate(
    "segment",
    x = anatomy_step_x1,
    xend = anatomy_step_x1,
    y = anatomy_step_y0,
    yend = anatomy_step_y1,
    color = "#3F8B6D",
    linewidth = 1.15,
    arrow = grid::arrow(length = grid::unit(0.16, "cm"))
  ) +
  geom_segment(
    data = anatomy_case,
    aes(x = x, xend = x, y = fitted, yend = observed),
    color = "#C05A47",
    linewidth = 1.25,
    inherit.aes = FALSE
  ) +
  geom_point(
    data = anatomy_case,
    aes(x = x, y = fitted),
    shape = 21,
    fill = "white",
    color = "#C05A47",
    stroke = 1.1,
    size = 3.4,
    inherit.aes = FALSE
  ) +
  geom_point(
    data = anatomy_case,
    aes(x = x, y = observed),
    color = "#C05A47",
    size = 3.4,
    inherit.aes = FALSE
  ) +
  annotate(
    "text",
    x = 0.82,
    y = 1.18,
    label = topic5_labels$anatomy_intercept,
    color = "#203A4F",
    size = 3.1,
    fontface = "bold"
  ) +
  annotate(
    "text",
    x = (anatomy_step_x0 + anatomy_step_x1) / 2,
    y = anatomy_step_y0 - 0.52,
    label = topic5_labels$anatomy_run,
    color = "#276449",
    size = 3.1,
    fontface = "bold"
  ) +
  annotate(
    "text",
    x = anatomy_step_x1 + 0.68,
    y = (anatomy_step_y0 + anatomy_step_y1) / 2,
    label = topic5_labels$anatomy_rise,
    color = "#276449",
    size = 3.1,
    fontface = "bold"
  ) +
  annotate(
    "text",
    x = anatomy_case$x - 0.74,
    y = anatomy_case$fitted - 0.42,
    label = topic5_labels$anatomy_fitted,
    color = "#8A3F36",
    size = 3.1,
    fontface = "bold"
  ) +
  annotate(
    "text",
    x = anatomy_case$x + 0.76,
    y = anatomy_case$observed + 0.32,
    label = topic5_labels$anatomy_observed,
    color = "#8A3F36",
    size = 3.1,
    fontface = "bold"
  ) +
  annotate(
    "text",
    x = 5.12,
    y = 6.28,
    label = topic5_labels$anatomy_residual,
    color = "#8A3F36",
    size = 3.1,
    fontface = "bold"
  ) +
  scale_x_continuous(breaks = 0:6, expand = expansion(mult = c(0.02, 0.03))) +
  scale_y_continuous(breaks = seq(0, 10, by = 2)) +
  coord_cartesian(xlim = c(-0.18, 6.15), ylim = c(0.65, 10), clip = "off") +
  labs(
    title = topic5_labels$anatomy_title,
    subtitle = topic5_labels$anatomy_subtitle,
    x = topic5_labels$anatomy_predictor,
    y = topic5_labels$anatomy_outcome
  ) +
  topic5_theme() +
  theme(plot.margin = margin(14, 60, 14, 18))

# Detailed anatomy figure. Its geometry is shared; learner-facing text follows
# the active locale.
anatomy_expanded_text <- if (topic_locale == "de") {
  list(
    panels = c(
      "A. So wird die angepasste Gerade positioniert",
      "B. So wird ein beobachteter Fall zerlegt"
    ),
    labels = c(
      "Angepasste Gleichung: Ŷ = b₀ + b₁X",
      "Achsenabschnitt (0, b₀)\nX = 0, Ŷ = 2",
      "Schritt: ΔX = 1",
      "Anstieg: ΔŶ = b₁ = 1.2",
      "Steigung = Anstieg ÷ Schritt = 1.2 ÷ 1",
      "Mittelwertpunkt (X̄, Ȳ)\nDie angepasste Stichprobengerade verläuft durch ihn",
      "angepasste Gerade",
      "angepasster Punkt (Xᵢ, Ŷᵢ)",
      "beobachteter Punkt (Xᵢ, Yᵢ)",
      "gewählter Prädiktorwert Xᵢ = 4.4",
      "eᵢ = Yᵢ − Ŷᵢ = +1.45",
      "Yᵢ = Ŷᵢ + eᵢ",
      "über der Geraden: eᵢ > 0\nunter der Geraden: eᵢ < 0",
      "angepasste Gerade"
    ),
    title = "Jeder Bestandteil einer einfachen Regressionsgeraden hat eine Aufgabe",
    subtitle = "Das erste Feld positioniert die Gerade; das zweite verbindet eine Beobachtung mit ihrem angepassten Wert und ihrem Residuum",
    x_axis = "Prädiktor X (Prädiktoreinheiten)",
    y_axis = "Ergebnisvariable Y (Ergebniseinheiten)"
  )
} else if (topic_locale == "sq") {
  list(
    panels = c(
      "A. Si pozicionohet vija e përshtatur",
      "B. Si zbërthehet një rast i vrojtuar"
    ),
    labels = c(
      "Ekuacioni i përshtatur: Ŷ = b₀ + b₁X",
      "Prerja me boshtin (0, b₀)\nX = 0, Ŷ = 2",
      "hapi: ΔX = 1",
      "ngritja: ΔŶ = b₁ = 1.2",
      "pjerrësia = ngritja ÷ hapi = 1.2 ÷ 1",
      "pika e mesatareve (X̄, Ȳ)\nVija e përshtatur e kampionit kalon nëpër të",
      "vija e përshtatur",
      "pika e përshtatur (Xᵢ, Ŷᵢ)",
      "pika e vrojtuar (Xᵢ, Yᵢ)",
      "vlera e zgjedhur parashikuese Xᵢ = 4.4",
      "eᵢ = Yᵢ − Ŷᵢ = +1.45",
      "Yᵢ = Ŷᵢ + eᵢ",
      "mbi vijë: eᵢ > 0\nnën vijë: eᵢ < 0",
      "vija e përshtatur"
    ),
    title = "Çdo pjesë e një vije të thjeshtë regresioni ka një rol",
    subtitle = "Paneli i parë pozicionon vijën; i dyti lidh një vrojtim me vlerën e tij të përshtatur dhe rezidualin",
    x_axis = "Ndryshorja parashikuese X (njësi parashikuese)",
    y_axis = "Rezultati Y (njësi rezultati)"
  )
} else {
  list(
    panels = c(
      "A. How the fitted line is positioned",
      "B. How one observed case is decomposed"
    ),
    labels = c(
      "Fitted equation: Ŷ = b₀ + b₁X",
      "Intercept (0, b₀)\nX = 0, Ŷ = 2",
      "run: ΔX = 1",
      "rise: ΔŶ = b₁ = 1.2",
      "slope = rise ÷ run = 1.2 ÷ 1",
      "mean point (X̄, Ȳ)\nThe fitted sample line passes through it",
      "fitted line",
      "fitted point (Xᵢ, Ŷᵢ)",
      "observed point (Xᵢ, Yᵢ)",
      "chosen predictor value Xᵢ = 4.4",
      "eᵢ = Yᵢ − Ŷᵢ = +1.45",
      "Yᵢ = Ŷᵢ + eᵢ",
      "above line: eᵢ > 0\nbelow line: eᵢ < 0",
      "fitted line"
    ),
    title = "Every Part of a Simple Regression Line Has a Job",
    subtitle = "The first panel positions the line; the second connects one observation to its fitted value and residual",
    x_axis = "Predictor X (predictor units)",
    y_axis = "Outcome Y (outcome units)"
  )
}

anatomy_en_panels <- anatomy_expanded_text$panels

anatomy_en_line <- bind_rows(lapply(anatomy_en_panels, function(panel_name) {
  anatomy_line |> mutate(panel = factor(panel_name, levels = anatomy_en_panels))
}))

anatomy_en_points <- tribble(
  ~panel, ~x, ~y, ~kind,
  anatomy_en_panels[[1]], 0, anatomy_intercept, "Intercept",
  anatomy_en_panels[[1]], 3, anatomy_intercept + anatomy_slope * 3, "Mean point",
  anatomy_en_panels[[2]], anatomy_case$x, anatomy_case$fitted, "Fitted",
  anatomy_en_panels[[2]], anatomy_case$x, anatomy_case$observed, "Observed"
) |>
  mutate(panel = factor(panel, levels = anatomy_en_panels))

anatomy_en_segments <- tribble(
  ~panel, ~x, ~xend, ~y, ~yend, ~kind,
  anatomy_en_panels[[1]], anatomy_step_x0, anatomy_step_x1, anatomy_step_y0, anatomy_step_y0, "Slope step",
  anatomy_en_panels[[1]], anatomy_step_x1, anatomy_step_x1, anatomy_step_y0, anatomy_step_y1, "Slope step",
  anatomy_en_panels[[2]], anatomy_case$x, anatomy_case$x, 0.8, anatomy_case$fitted, "Case guide",
  anatomy_en_panels[[2]], anatomy_case$x, anatomy_case$x, anatomy_case$fitted, anatomy_case$observed, "Positive residual"
) |>
  mutate(panel = factor(panel, levels = anatomy_en_panels))

anatomy_en_labels <- tribble(
  ~panel, ~x, ~y, ~label, ~kind,
  anatomy_en_panels[[1]], 4.48, 9.42, anatomy_expanded_text$labels[[1]], "Equation",
  anatomy_en_panels[[1]], 0.72, 1.15, anatomy_expanded_text$labels[[2]], "Definition",
  anatomy_en_panels[[1]], 1.66, 2.72, anatomy_expanded_text$labels[[3]], "Slope",
  anatomy_en_panels[[1]], 2.98, 3.80, anatomy_expanded_text$labels[[4]], "Slope",
  anatomy_en_panels[[1]], 1.12, 5.54, anatomy_expanded_text$labels[[5]], "Slope",
  anatomy_en_panels[[1]], 4.18, 4.62, anatomy_expanded_text$labels[[6]], "Mean",
  anatomy_en_panels[[1]], 5.12, 8.72, anatomy_expanded_text$labels[[7]], "Line",
  anatomy_en_panels[[2]], 3.20, 6.82, anatomy_expanded_text$labels[[8]], "Fitted",
  anatomy_en_panels[[2]], 5.18, 9.28, anatomy_expanded_text$labels[[9]], "Observed",
  anatomy_en_panels[[2]], 3.24, 1.28, anatomy_expanded_text$labels[[10]], "Case",
  anatomy_en_panels[[2]], 3.02, 8.14, anatomy_expanded_text$labels[[11]], "Residual",
  anatomy_en_panels[[2]], 1.48, 9.35, anatomy_expanded_text$labels[[12]], "Equation",
  anatomy_en_panels[[2]], 1.22, 5.18, anatomy_expanded_text$labels[[13]], "Sign",
  anatomy_en_panels[[2]], 5.30, 7.32, anatomy_expanded_text$labels[[14]], "Line"
) |>
  mutate(panel = factor(panel, levels = anatomy_en_panels))

# Thin leaders keep every definition visibly tied to its geometry without
# placing long translated labels directly on top of the line, slope step, or
# residual. Their endpoints are shared across locales so the mathematical
# geometry remains identical.
anatomy_en_label_leaders <- tribble(
  ~panel, ~x, ~y, ~xend, ~yend, ~kind,
  anatomy_en_panels[[1]], 0.00, anatomy_intercept, 0.38, 1.48, "Definition",
  anatomy_en_panels[[1]], 1.70, anatomy_step_y0, 1.66, 3.03, "Slope",
  anatomy_en_panels[[1]], anatomy_step_x1, 4.04, 2.58, 3.86, "Slope",
  anatomy_en_panels[[1]], anatomy_step_x1, anatomy_step_y1, 1.70, 5.12, "Slope",
  anatomy_en_panels[[1]], 3.00, 5.60, 3.48, 4.92, "Mean",
  anatomy_en_panels[[1]], 5.12, 8.14, 5.12, 8.46, "Line",
  anatomy_en_panels[[2]], anatomy_case$x, anatomy_case$fitted, 3.82, 6.98, "Fitted",
  anatomy_en_panels[[2]], anatomy_case$x, anatomy_case$observed, 4.78, 9.05, "Observed",
  anatomy_en_panels[[2]], anatomy_case$x, 0.80, 3.88, 1.08, "Case",
  anatomy_en_panels[[2]], anatomy_case$x, mean(c(anatomy_case$fitted, anatomy_case$observed)), 3.92, 8.14, "Residual",
  anatomy_en_panels[[2]], 5.22, anatomy_intercept + anatomy_slope * 5.22, 5.28, 7.66, "Line"
) |>
  mutate(panel = factor(panel, levels = anatomy_en_panels))

p_regression_anatomy_enriched <- ggplot(anatomy_en_line, aes(x, y)) +
  geom_line(color = "#173F5F", linewidth = 1.15) +
  geom_segment(
    data = anatomy_en_segments,
    aes(x, y, xend = xend, yend = yend, color = kind),
    inherit.aes = FALSE,
    linewidth = 1.1,
    linetype = ifelse(anatomy_en_segments$kind == "Case guide", "dashed", "solid"),
    arrow = grid::arrow(length = grid::unit(0.12, "cm"), type = "closed")
  ) +
  geom_point(
    data = anatomy_en_points,
    aes(x, y, fill = kind),
    inherit.aes = FALSE,
    shape = 21,
    color = "white",
    stroke = 0.9,
    size = 4.1
  ) +
  geom_segment(
    data = anatomy_en_label_leaders,
    aes(x, y, xend = xend, yend = yend, color = kind),
    inherit.aes = FALSE,
    linewidth = 0.42,
    alpha = 0.82,
    lineend = "round"
  ) +
  geom_label(
    data = anatomy_en_labels,
    aes(x, y, label = label, color = kind),
    inherit.aes = FALSE,
    fill = "white",
    size = 2.9,
    lineheight = 0.96,
    linewidth = 0.23,
    label.padding = grid::unit(0.12, "lines")
  ) +
  facet_wrap(vars(panel), ncol = 1) +
  scale_color_manual(
    values = c(
      "Slope step" = "#3F8B6D", "Case guide" = "#718494",
      "Positive residual" = "#C05A47", "Equation" = "#173F5F",
      "Definition" = "#34495E", "Slope" = "#276449", "Mean" = "#5A4E8A",
      "Line" = "#173F5F", "Fitted" = "#8A3F36", "Observed" = "#8A3F36",
      "Case" = "#536475", "Residual" = "#8A3F36", "Sign" = "#536475"
    ),
    guide = "none"
  ) +
  scale_fill_manual(
    values = c(
      Intercept = "#2E6DA4", `Mean point` = "#6A4C93",
      Fitted = "white", Observed = "#C05A47"
    ),
    guide = "none"
  ) +
  scale_x_continuous(breaks = 0:6, expand = expansion(mult = c(0.02, 0.03))) +
  scale_y_continuous(breaks = seq(0, 10, by = 2)) +
  coord_cartesian(xlim = c(-0.18, 6.2), ylim = c(0.65, 10), clip = "off") +
  labs(
    title = anatomy_expanded_text$title,
    subtitle = anatomy_expanded_text$subtitle,
    x = anatomy_expanded_text$x_axis,
    y = anatomy_expanded_text$y_axis
  ) +
  topic5_theme(base_size = 10.5) +
  theme(
    strip.text = element_text(face = "bold", color = "#203A4F"),
    panel.spacing = grid::unit(1.2, "lines"),
    legend.position = "none",
    plot.margin = margin(14, 28, 14, 18)
  )

# Formula-to-geometry bridge for the sum-of-squares partition. The left side
# uses the same teaching case as the anatomy plot. The right side uses symbols
# rather than arbitrary proportions, so it does not imply a fabricated R2.
ss_geometry_text <- if (topic_locale == "de") {
  list(
    point_labels = c(
      "Mittelwert der Ergebnisvariable Ȳ",
      "Angepasster Wert Ŷᵢ",
      "Beobachteter Wert Yᵢ"
    ),
    box_labels = c("SS Modell", "SS Fehler", "SS gesamt"),
    total = "gesamt: Yᵢ − Ȳ",
    model = "Modell: Ŷᵢ − Ȳ",
    residual = "Residuum: Yᵢ − Ŷᵢ",
    equation = "Yᵢ − Ȳ = (Ŷᵢ − Ȳ) + (Yᵢ − Ŷᵢ)",
    r_squared = "R² = Modell-SS ÷ Gesamt-SS",
    instruction = "Quadriere die drei vertikalen Abstände jedes Falls und addiere sie über alle Fälle",
    title = "Eine vertikale Differenz führt zur Quadratsummenzerlegung des Modells",
    subtitle = "Zerlege zuerst einen Fall; quadriere und addiere danach die entsprechenden Abstände über alle Fälle"
  )
} else if (topic_locale == "sq") {
  list(
    point_labels = c(
      "Mesatarja e ndryshores së rezultatit Ȳ",
      "Vlera e përshtatur Ŷᵢ",
      "Vlera e vrojtuar Yᵢ"
    ),
    box_labels = c("SS e modelit", "SS e gabimit", "SS totale"),
    total = "totale: Yᵢ − Ȳ",
    model = "modeli: Ŷᵢ − Ȳ",
    residual = "reziduali: Yᵢ − Ŷᵢ",
    equation = "Yᵢ − Ȳ = (Ŷᵢ − Ȳ) + (Yᵢ − Ŷᵢ)",
    r_squared = "R² = SS e modelit ÷ SS totale",
    instruction = "Ngriji në katror tri largësitë vertikale të çdo rasti dhe pastaj mblidhi për të gjitha rastet",
    title = "Një diferencë vertikale bëhet ndarja e shumave të katrorëve të modelit",
    subtitle = "Zbërthe fillimisht një rast, pastaj ngriji në katror dhe mblidhi largësitë përkatëse nëpër të gjitha rastet"
  )
} else {
  list(
    point_labels = c("Outcome mean Ȳ", "Fitted value Ŷᵢ", "Observed value Yᵢ"),
    box_labels = c("SS model", "SS error", "SS total"),
    total = "total: Yᵢ − Ȳ",
    model = "model: Ŷᵢ − Ȳ",
    residual = "residual: Yᵢ − Ŷᵢ",
    equation = "Yᵢ − Ȳ = (Ŷᵢ − Ȳ) + (Yᵢ − Ŷᵢ)",
    r_squared = "R² = model SS ÷ total SS",
    instruction = "Square each case's three vertical distances, then add across all cases",
    title = "One Vertical Difference Becomes the Model's Sum-of-Squares Partition",
    subtitle = "First decompose one case, then square and add the corresponding distances across all cases"
  )
}

ss_geometry_labels <- tibble(
  x = c(1.0, 1.0, 1.0),
  y = c(5.6, anatomy_case$fitted, anatomy_case$observed),
  label = ss_geometry_text$point_labels,
  kind = c("Mean", "Model", "Observed"),
  point_fill = c("#718494", "#3F8B6D", "#C05A47")
)

ss_geometry_segments <- tribble(
  ~x, ~xend, ~y, ~yend, ~kind,
  0.58, 0.58, 5.6, anatomy_case$observed, "Total deviation",
  1.0, 1.0, 5.6, anatomy_case$fitted, "Model deviation",
  1.42, 1.42, anatomy_case$fitted, anatomy_case$observed, "Residual deviation"
)

ss_symbol_boxes <- tibble(
  xmin = c(3.0, 5.15, 7.30),
  xmax = c(4.55, 6.70, 8.85),
  ymin = 5.55,
  ymax = 6.65,
  label = ss_geometry_text$box_labels,
  fill = c("#EAF4EF", "#FFF0EA", "#EAF2F8")
)

p_regression_ss_geometry_en <- ggplot() +
  geom_segment(
    data = ss_geometry_segments,
    aes(x, y, xend = xend, yend = yend, color = kind),
    linewidth = 1.25,
    arrow = grid::arrow(length = grid::unit(0.14, "cm"), type = "closed")
  ) +
  geom_point(data = ss_geometry_labels, aes(x, y, fill = point_fill), shape = 21, size = 4, color = "white", stroke = 0.8) +
  geom_label(
    data = ss_geometry_labels,
    aes(x = 1.72, y, label = label, color = kind),
    fill = "white",
    size = 3.05,
    linewidth = 0.2
  ) +
  annotate("text", x = 0.34, y = 7.15, label = ss_geometry_text$total, color = "#244C69", angle = 90, fontface = "bold", size = 3.1) +
  annotate("text", x = 0.77, y = 6.42, label = ss_geometry_text$model, color = "#276449", angle = 90, fontface = "bold", size = 3.0) +
  annotate("text", x = 1.62, y = 8.03, label = ss_geometry_text$residual, color = "#8A3F36", angle = 90, fontface = "bold", size = 3.0) +
  annotate("label", x = 1.0, y = 4.72, label = ss_geometry_text$equation, fill = "#F4F8FA", color = "#203A4F", fontface = "bold", size = 3.0, linewidth = 0.25) +
  geom_rect(data = ss_symbol_boxes, aes(xmin = xmin, xmax = xmax, ymin = ymin, ymax = ymax, fill = fill), color = "#9AAAB6", linewidth = 0.45) +
  geom_text(data = ss_symbol_boxes, aes(x = (xmin + xmax) / 2, y = (ymin + ymax) / 2, label = label), color = "#203A4F", fontface = "bold", size = 3.5) +
  annotate("text", x = 4.85, y = 6.1, label = "+", color = "#34495E", fontface = "bold", size = 5) +
  annotate("text", x = 7.0, y = 6.1, label = "=", color = "#34495E", fontface = "bold", size = 5) +
  annotate("label", x = 5.93, y = 4.9, label = ss_geometry_text$r_squared, fill = "#FFF4EA", color = "#713D31", fontface = "bold", size = 3.4, linewidth = 0.3) +
  annotate("text", x = 5.93, y = 7.28, label = ss_geometry_text$instruction, color = "#536475", size = 3.15) +
  scale_color_manual(
    values = c(
      "Total deviation" = "#244C69", "Model deviation" = "#3F8B6D",
      "Residual deviation" = "#C05A47", Mean = "#536475",
      Model = "#276449", Observed = "#8A3F36"
    ),
    guide = "none"
  ) +
  scale_fill_identity() +
  coord_cartesian(xlim = c(0, 9.15), ylim = c(4.25, 9.25), clip = "off") +
  labs(
    title = ss_geometry_text$title,
    subtitle = ss_geometry_text$subtitle
  ) +
  theme_void(base_size = 11) +
  theme(
    plot.title = element_text(face = "bold", color = "#172B3A"),
    plot.subtitle = element_text(color = "#536475"),
    plot.background = element_rect(fill = "white", color = NA),
    panel.background = element_rect(fill = "white", color = NA),
    plot.margin = margin(16, 24, 16, 24)
  )

# Concrete Theory figure: the three sums of squares for one deliberately small
# four-case OLS example. The values are selected so every fitted value,
# deviation, squared deviation, and whole-sample partition can be checked by
# hand: model SS 20 + error SS 6 = total SS 26. Bar heights share one scale,
# preventing the panel geometry from implying different units.
ss_concrete_cases <- tibble(
  case = factor(paste0("i = ", 1:4), levels = paste0("i = ", 1:4)),
  x = 1:4,
  observed = c(2, 5, 4, 9),
  fitted = c(2, 4, 6, 8),
  outcome_mean = 5
)

ss_concrete_text <- if (topic_locale == "de") {
  list(
    components = c(
      model = "Modell-Quadratsumme",
      error = "Fehlerquadratsumme",
      total = "Gesamtquadratsumme"
    ),
    title = "Vier Fälle machen die drei Quadratsummen konkret",
    subtitle = "Jeder Balken ist eine quadrierte Abweichung; die Zahl im Feld ist die Summe des jeweiligen Panels",
    x_axis = "Fall",
    y_axis = "Quadrierte Abweichung",
    partition = "Modell-SS 20 + Fehler-SS 6 = Gesamt-SS 26",
    alt = paste(
      "Drei Balkendiagramme zeigen für dieselben vier erfundenen Fälle die quadrierten Modellabweichungen, quadrierten Residuen und quadrierten Gesamtabweichungen.",
      "Die Modellwerte 9, 1, 1 und 9 summieren sich zu 20; die Fehlerwerte 0, 1, 4 und 1 zu 6; die Gesamtwerte 9, 0, 1 und 16 zu 26.",
      "Unter den Feldern steht die vollständige Zerlegung: Modell-Quadratsumme 20 plus Fehlerquadratsumme 6 gleich Gesamtquadratsumme 26."
    )
  )
} else if (topic_locale == "sq") {
  list(
    components = c(
      model = "Shuma e katrorëve e modelit",
      error = "Shuma e katrorëve e gabimit",
      total = "Shuma totale e katrorëve"
    ),
    title = "Katër raste i bëjnë konkrete tri shumat e katrorëve",
    subtitle = "Çdo shtyllë është një shmangie e ngritur në katror; numri në panel është shuma e tij",
    x_axis = "Rasti",
    y_axis = "Shmangia e ngritur në katror",
    partition = "SS e modelit 20 + SS e gabimit 6 = SS totale 26",
    alt = paste(
      "Tri diagrame me shtylla tregojnë për të njëjtat katër raste të sajuara shmangiet e modelit, rezidualet dhe shmangiet totale, të gjitha të ngritura në katror.",
      "Vlerat e modelit 9, 1, 1 dhe 9 japin shumën 20; vlerat e gabimit 0, 1, 4 dhe 1 japin 6; vlerat totale 9, 0, 1 dhe 16 japin 26.",
      "Poshtë paneleve paraqitet ndarja e plotë: shuma e katrorëve e modelit 20 plus shuma e katrorëve e gabimit 6 baras me shumën totale të katrorëve 26."
    )
  )
} else {
  list(
    components = c(
      model = "Model sum of squares",
      error = "Error sum of squares",
      total = "Total sum of squares"
    ),
    title = "Four Cases Make the Three Sums of Squares Concrete",
    subtitle = "Each bar is one squared deviation; the number in each panel is that panel's sum",
    x_axis = "Case",
    y_axis = "Squared deviation",
    partition = "Model SS 20 + error SS 6 = total SS 26",
    alt = paste(
      "Three bar charts show squared model deviations, squared residuals, and squared total deviations for the same four invented cases.",
      "The model values 9, 1, 1, and 9 sum to 20; the error values 0, 1, 4, and 1 sum to 6; the total values 9, 0, 1, and 16 sum to 26.",
      "A statement below the panels gives the complete partition: model sum of squares 20 plus error sum of squares 6 equals total sum of squares 26."
    )
  )
}

ss_concrete_long <- bind_rows(
  ss_concrete_cases |>
    transmute(
      case,
      component_key = "model",
      signed_deviation = fitted - outcome_mean,
      squared_deviation = signed_deviation^2
    ),
  ss_concrete_cases |>
    transmute(
      case,
      component_key = "error",
      signed_deviation = observed - fitted,
      squared_deviation = signed_deviation^2
    ),
  ss_concrete_cases |>
    transmute(
      case,
      component_key = "total",
      signed_deviation = observed - outcome_mean,
      squared_deviation = signed_deviation^2
    )
) |>
  mutate(
    component = factor(
      unname(ss_concrete_text$components[component_key]),
      levels = unname(ss_concrete_text$components[c("model", "error", "total")])
    ),
    calculation = paste0(
      "(",
      ifelse(signed_deviation >= 0, "+", ""),
      signed_deviation,
      ")² = ",
      squared_deviation
    )
  ) |>
  group_by(component) |>
  mutate(component_sum = sum(squared_deviation)) |>
  ungroup()

ss_concrete_sums <- ss_concrete_long |>
  distinct(component, component_sum)

p_regression_ss_concrete <- ggplot(
  ss_concrete_long,
  aes(case, squared_deviation, fill = component)
) +
  geom_col(width = 0.68, color = "white", linewidth = 0.55) +
  geom_text(
    aes(label = calculation),
    vjust = -0.38,
    color = "#203A4F",
    fontface = "bold",
    size = 3.05
  ) +
  geom_label(
    data = ss_concrete_sums,
    aes(x = 2.5, y = 18.25, label = paste0("SS = ", component_sum)),
    inherit.aes = FALSE,
    fill = "white",
    color = "#203A4F",
    fontface = "bold",
    size = 3.25,
    linewidth = 0.25
  ) +
  facet_wrap(vars(component), nrow = 1) +
  scale_fill_manual(
    values = setNames(
      c("#3F8B6D", "#C05A47", "#2F6F9F"),
      unname(ss_concrete_text$components[c("model", "error", "total")])
    ),
    guide = "none"
  ) +
  scale_y_continuous(
    breaks = seq(0, 16, by = 4),
    limits = c(0, 20),
    expand = expansion(mult = c(0, 0.02))
  ) +
  coord_cartesian(clip = "off") +
  labs(
    title = ss_concrete_text$title,
    subtitle = ss_concrete_text$subtitle,
    x = ss_concrete_text$x_axis,
    y = ss_concrete_text$y_axis,
    caption = ss_concrete_text$partition
  ) +
  topic5_theme(base_size = 10.7) +
  theme(
    strip.text = element_text(face = "bold", color = "#203A4F", size = 10),
    panel.spacing.x = grid::unit(0.9, "lines"),
    plot.caption = element_text(
      face = "bold",
      color = "#203A4F",
      hjust = 0.5,
      margin = margin(t = 12)
    ),
    plot.margin = margin(16, 20, 16, 16)
  )

# Conceptual Theory figure: contrasting residual patterns. A shared fitted-value
# sequence makes shape and spread, rather than axis changes, drive the contrast.
set.seed(5042)
pattern_n <- 60
pattern_x <- seq(0.5, 9.5, length.out = pattern_n)
residual_pattern_data <- bind_rows(
  tibble(
    fitted = pattern_x,
    residual = pmin(
      pmax(rnorm(pattern_n, mean = 0, sd = 0.75), -1.8),
      1.8
    ),
    pattern = topic5_labels$pattern_compatible
  ),
  tibble(
    fitted = pattern_x,
    residual = 0.13 * (pattern_x - 5)^2 - 1.05 + rnorm(pattern_n, 0, 0.28),
    pattern = topic5_labels$pattern_curve
  ),
  tibble(
    fitted = pattern_x,
    residual = rnorm(pattern_n, mean = 0, sd = 0.15 + 0.18 * pattern_x),
    pattern = topic5_labels$pattern_funnel
  )
) |>
  mutate(
    pattern = factor(
      pattern,
      levels = c(
        topic5_labels$pattern_compatible,
        topic5_labels$pattern_curve,
        topic5_labels$pattern_funnel
      )
    ),
    hover_text = paste0(
      as.character(pattern),
      "<br>", topic5_labels$pattern_fitted, ": ", formatC(fitted, format = "f", digits = 2),
      "<br>", topic5_labels$pattern_residual, ": ", formatC(residual, format = "f", digits = 2)
    )
  )

residual_pattern_guides <- bind_rows(
  tibble(
    fitted = pattern_x,
    guide = 0,
    pattern = topic5_labels$pattern_compatible
  ),
  tibble(
    fitted = pattern_x,
    guide = 0.13 * (pattern_x - 5)^2 - 1.05,
    pattern = topic5_labels$pattern_curve
  ),
  tibble(
    fitted = pattern_x,
    guide = 0,
    pattern = topic5_labels$pattern_funnel
  )
) |>
  mutate(
    pattern = factor(
      pattern,
      levels = levels(residual_pattern_data$pattern)
    )
  )

p_residual_patterns <- ggplot(residual_pattern_data, aes(fitted, residual)) +
  geom_hline(yintercept = 0, color = "#536475", linewidth = 0.65) +
  geom_point(aes(text = hover_text), color = "#2E6DA4", alpha = 0.70, size = 1.75) +
  geom_line(
    data = residual_pattern_guides,
    aes(fitted, guide),
    color = "#C05A47",
    linewidth = 0.9,
    inherit.aes = FALSE
  ) +
  facet_wrap(
    vars(pattern),
    nrow = 1,
    labeller = labeller(pattern = label_wrap_gen(width = 18))
  ) +
  coord_cartesian(ylim = c(-4, 4)) +
  scale_x_continuous(breaks = c(2, 5, 8)) +
  labs(
    title = topic5_labels$patterns_title,
    subtitle = topic5_labels$patterns_subtitle,
    x = topic5_labels$pattern_fitted,
    y = topic5_labels$pattern_residual
  ) +
  topic5_theme(base_size = 11) +
  theme(
    strip.background = element_rect(fill = "#EDF3F7", color = "#D7E1E8"),
    strip.text = element_text(face = "bold", color = "#203A4F", size = 9.5)
  )

fit_grid <- tibble(
  study_hours = seq(min(dat$study_hours), max(dat$study_hours), length.out = 160)
) |>
  mutate(
    fit = b0_hat + b1_hat * study_hours,
    hover_text = paste0(
      topic5_labels$candidate_line, ": ", topic5_labels$candidate_ols,
      "<br>", topic5_labels$study_hours, ": ", formatC(study_hours, format = "f", digits = 1),
      "<br>", topic5_labels$fitted_score, ": ", formatC(fit, format = "f", digits = 2)
    )
  )

p_regression_fit <- ggplot(dat, aes(study_hours, assessment_score)) +
  geom_point(aes(text = hover_observation), color = "#2E6DA4", alpha = 0.78, size = 2.1) +
  geom_line(
    data = fit_grid,
    aes(x = study_hours, y = fit, text = hover_text, group = 1),
    inherit.aes = FALSE,
    color = "#173F5F",
    linewidth = 1.1
  ) +
  geom_segment(
    data = focal_case,
    aes(
      x = study_hours,
      xend = study_hours,
      y = fitted_score,
      yend = assessment_score,
      text = hover_observation
    ),
    color = "#C05A47",
    linewidth = 1.2,
    inherit.aes = FALSE
  ) +
  geom_point(
    data = focal_case,
    aes(x = study_hours, y = fitted_score, text = hover_observation),
    color = "#C05A47",
    fill = "white",
    shape = 21,
    stroke = 1.1,
    size = 3,
    inherit.aes = FALSE
  ) +
  scale_x_continuous(breaks = seq(0, 16, by = 4)) +
  labs(
    title = topic5_labels$fit_title,
    subtitle = topic5_labels$fit_subtitle,
    x = topic5_labels$study_hours,
    y = topic5_labels$assessment_score
  ) +
  topic5_theme()

p_least_squares <- ggplot(dat, aes(study_hours, assessment_score)) +
  geom_point(aes(text = hover_observation), color = "#8AA0B2", alpha = 0.55, size = 1.8) +
  geom_line(
    data = candidate_grid,
    aes(
      x = study_hours,
      y = predicted,
      color = candidate_line,
      text = hover_text,
      group = candidate_line
    ),
    linewidth = 1.05,
    inherit.aes = FALSE
  ) +
  scale_color_manual(
    values = setNames(
      c("#173F5F", "#C05A47", "#3F8B6D"),
      c(
        topic5_labels$candidate_ols,
        topic5_labels$candidate_flat,
        topic5_labels$candidate_steep
      )
    )
  ) +
  scale_x_continuous(breaks = seq(0, 16, by = 2)) +
  labs(
    title = topic5_labels$least_squares_title,
    subtitle = topic5_labels$least_squares_subtitle,
    x = topic5_labels$study_hours,
    y = topic5_labels$assessment_score,
    color = NULL
  ) +
  topic5_theme() +
  theme(legend.position = "bottom")

extrapolation_grid <- tibble(study_hours = seq(0, 22, length.out = 220)) |>
  mutate(
    fitted_score = b0_hat + b1_hat * study_hours,
    segment = ifelse(
      study_hours <= max(dat$study_hours),
      topic5_labels$inside_range,
      topic5_labels$outside_range
    ),
    hover_text = paste0(
      topic5_labels$prediction_status, ": ", segment,
      "<br>", topic5_labels$study_hours, ": ", formatC(study_hours, format = "f", digits = 1),
      "<br>", topic5_labels$fitted_score, ": ", formatC(fitted_score, format = "f", digits = 2)
    )
  )

p_extrapolation <- ggplot(dat, aes(study_hours, assessment_score)) +
  annotate(
    "rect",
    xmin = max(dat$study_hours),
    xmax = 22,
    ymin = -Inf,
    ymax = Inf,
    fill = "#F5E8E4",
    alpha = 0.70
  ) +
  geom_point(aes(text = hover_observation), color = "#2E6DA4", alpha = 0.72, size = 1.9) +
  geom_line(
    data = extrapolation_grid |> filter(segment == topic5_labels$inside_range),
    aes(study_hours, fitted_score, text = hover_text, group = 1),
    color = "#173F5F",
    linewidth = 1.1,
    inherit.aes = FALSE
  ) +
  geom_line(
    data = extrapolation_grid |> filter(segment == topic5_labels$outside_range),
    aes(study_hours, fitted_score, text = hover_text, group = 1),
    color = "#C05A47",
    linewidth = 1.1,
    linetype = "dashed",
    inherit.aes = FALSE
  ) +
  geom_vline(
    xintercept = max(dat$study_hours),
    color = "#C05A47",
    linewidth = 0.7,
    linetype = "dotted"
  ) +
  annotate(
    "text",
    x = 18.0,
    y = min(dat$assessment_score) + 4,
    label = topic5_labels$outside_label,
    color = "#8A3F36",
    size = 2.8,
    hjust = 0.5
  ) +
  scale_x_continuous(
    breaks = seq(0, 22, by = 2),
    expand = expansion(mult = c(0.02, 0.08))
  ) +
  labs(
    title = topic5_labels$extrapolation_title,
    subtitle = topic5_labels$extrapolation_subtitle,
    x = topic5_labels$study_hours,
    y = topic5_labels$assessment_score
  ) +
  topic5_theme()

p_residuals <- ggplot(dat, aes(fitted_score, residual)) +
  geom_hline(yintercept = 0, color = "#536475", linewidth = 0.7) +
  geom_point(aes(text = hover_residual), color = "#2E6DA4", alpha = 0.75, size = 2) +
  geom_smooth(
    method = "loess",
    formula = y ~ x,
    se = FALSE,
    color = "#C05A47",
    linewidth = 0.95
  ) +
  labs(
    title = topic5_labels$residual_title,
    subtitle = topic5_labels$residual_subtitle,
    x = topic5_labels$fitted_axis,
    y = topic5_labels$residual_axis
  ) +
  topic5_theme()

qq_data <- tibble(
  theoretical_quantile = qnorm(ppoints(n)),
  sample_quantile = sort(dat$standardized_residual)
) |>
  mutate(
    hover_text = paste0(
      topic5_labels$theoretical_quantiles, ": ", formatC(theoretical_quantile, format = "f", digits = 2),
      "<br>", topic5_labels$sample_quantiles, ": ", formatC(sample_quantile, format = "f", digits = 2)
    )
  )
qq_sample_quartiles <- quantile(dat$standardized_residual, c(0.25, 0.75))
qq_theoretical_quartiles <- qnorm(c(0.25, 0.75))
qq_line_slope <- diff(qq_sample_quartiles) / diff(qq_theoretical_quartiles)
qq_line_intercept <- qq_sample_quartiles[1] - qq_line_slope * qq_theoretical_quartiles[1]
qq_line <- tibble(
  theoretical_quantile = range(qq_data$theoretical_quantile),
  sample_quantile = qq_line_intercept + qq_line_slope * theoretical_quantile
)

p_qq <- ggplot(qq_data, aes(theoretical_quantile, sample_quantile)) +
  geom_point(aes(text = hover_text), color = "#2E6DA4", alpha = 0.78, size = 2) +
  geom_line(
    data = qq_line,
    aes(theoretical_quantile, sample_quantile),
    color = "#C05A47",
    linewidth = 0.9,
    inherit.aes = FALSE
  ) +
  labs(
    title = topic5_labels$qq_title,
    subtitle = topic5_labels$qq_subtitle,
    x = topic5_labels$theoretical_quantiles,
    y = topic5_labels$sample_quantiles
  ) +
  topic5_theme()

influence_labels <- dat |>
  arrange(desc(cooks_distance)) |>
  slice_head(n = 3) |>
  mutate(
    label_x = case_when(
      participant_id == "S035" ~ leverage - 0.0020,
      participant_id == "S110" ~ leverage + 0.0020,
      TRUE ~ leverage
    ),
    label_y = case_when(
      participant_id == "S035" ~ standardized_residual - 0.25,
      participant_id == "S110" ~ standardized_residual + 0.38,
      TRUE ~ standardized_residual + 0.30
    )
  )

p_influence <- ggplot(dat, aes(leverage, standardized_residual)) +
  geom_hline(yintercept = 0, color = "#536475", linewidth = 0.7) +
  geom_point(
    aes(size = cooks_distance, text = hover_influence),
    color = "#2E6DA4",
    alpha = 0.68
  ) +
  geom_text(
    data = influence_labels,
    aes(x = label_x, y = label_y, label = participant_id),
    color = "#8A3F36",
    fontface = "bold",
    size = 3.1,
    show.legend = FALSE
  ) +
  scale_x_continuous(expand = expansion(mult = c(0.08, 0.20))) +
  scale_size_continuous(range = c(1.5, 7)) +
  labs(
    title = topic5_labels$influence_title,
    subtitle = topic5_labels$influence_subtitle,
    x = topic5_labels$leverage,
    y = topic5_labels$standardized_residual,
    size = topic5_labels$cooks_distance
  ) +
  topic5_theme() +
  theme(legend.position = "bottom")
