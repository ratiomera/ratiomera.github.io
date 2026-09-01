#!/usr/bin/env Rscript

# Generate the allowlisted raster assets used by the topic-summary pipeline.
#
# This script owns the small raster Ratiomera mark and exports one reviewed plot
# from each trusted shared topic asset file. It never reads learner-authored
# Markdown, raw teaching materials, remote resources, or SVG files.

args <- commandArgs(trailingOnly = TRUE)
script_arg <- grep("^--file=", commandArgs(trailingOnly = FALSE), value = TRUE)
if (length(script_arg) != 1L) {
  stop("Could not identify this script's path.", call. = FALSE)
}

script_path <- normalizePath(sub("^--file=", "", script_arg), mustWork = TRUE)
project_root <- normalizePath(file.path(dirname(script_path), ".."), mustWork = TRUE)
source_root <- file.path(project_root, "ratiomera-statistics", "_shared")
summary_root <- file.path(source_root, "summary-sources")
asset_root <- file.path(summary_root, "assets")

if (!file.exists(file.path(project_root, "_quarto.yml"))) {
  stop("The detected project root does not contain _quarto.yml.", call. = FALSE)
}

topic_registry <- list(
  `01` = list(
    source = "t01-descriptive-assets.R",
    object = "p_hist_exam",
    asset = "topic-01-descriptive-statistics-summary-figure-en.png"
  ),
  `02` = list(
    source = "t02-probability-assets.R",
    object = "p_event_operations",
    asset = "topic-02-probability-summary-figure-en.png"
  ),
  `03` = list(
    source = "t03-inference-assets.R",
    object = "p_inference_bridge",
    asset = "topic-03-hypothesis-testing-summary-figure-en.png"
  ),
  `04` = list(
    source = "t04-cov-corr-assets.R",
    object = "p_shape_checks",
    asset = "topic-04-covariance-correlation-summary-figure-en.png"
  ),
  `05` = list(
    source = "t05-simple-regression-assets.R",
    object = "p_regression_fit",
    asset = "topic-05-simple-linear-regression-summary-figure-en.png"
  ),
  `06` = list(
    source = "t06-partial-corr-assets.R",
    object = "p_raw_adjusted",
    asset = "topic-06-partial-correlation-summary-figure-en.png"
  ),
  `07` = list(
    source = "t07-multiple-regression-assets.R",
    object = "p_topic7_coefficient_change",
    asset = "topic-07-multiple-regression-summary-figure-en.png"
  ),
  `08` = list(
    source = "t08-anova-assets.R",
    object = "p_sim_ss_partition",
    asset = "topic-08-analysis-of-variance-summary-figure-en.png"
  )
)

parse_arguments <- function(arguments) {
  selected_locale <- "en"
  selected_topics <- character()
  index <- 1L
  while (index <= length(arguments)) {
    option <- arguments[[index]]
    if (index == length(arguments)) {
      stop(
        "Usage: Rscript scripts/generate-summary-assets.R [--locale en|de|sq] [--topic 1 ... --topic 8]",
        call. = FALSE
      )
    }
    value <- arguments[[index + 1L]]
    if (identical(option, "--locale")) {
      if (!value %in% c("en", "de", "sq")) {
        stop("Locale must be en, de, or sq.", call. = FALSE)
      }
      selected_locale <- value
    } else if (identical(option, "--topic")) {
      if (!grepl("^[1-8]$", value)) {
        stop("Topic numbers must be integers from 1 through 8.", call. = FALSE)
      }
      selected_topics <- c(selected_topics, sprintf("%02d", as.integer(value)))
    } else {
      stop(
        "Usage: Rscript scripts/generate-summary-assets.R [--locale en|de|sq] [--topic 1 ... --topic 8]",
        call. = FALSE
      )
    }
    index <- index + 2L
  }
  if (length(selected_topics) == 0L) selected_topics <- names(topic_registry)
  list(locale = selected_locale, topics = unique(selected_topics))
}

parsed_arguments <- parse_arguments(args)
selected_locale <- parsed_arguments$locale
selected_topics <- parsed_arguments$topics

require_namespace <- function(package) {
  if (!requireNamespace(package, quietly = TRUE)) {
    stop("Missing required local R package: ", package, call. = FALSE)
  }
}
require_namespace("ggplot2")
require_namespace("ragg")
require_namespace("grid")

dir.create(file.path(asset_root, selected_locale), recursive = TRUE, showWarnings = FALSE)
asset_root <- normalizePath(asset_root, mustWork = TRUE)
locale_asset_root <- normalizePath(file.path(asset_root, selected_locale), mustWork = TRUE)

assert_owned_output <- function(path) {
  parent <- normalizePath(dirname(path), mustWork = TRUE)
  if (!identical(parent, locale_asset_root)) {
    stop("Refusing to write outside the owned locale summary asset directory: ", path, call. = FALSE)
  }
  if (file.exists(path) && Sys.readlink(path) != "") {
    stop("Refusing to replace a symlinked summary asset: ", path, call. = FALSE)
  }
}

assert_png <- function(path) {
  connection <- file(path, open = "rb")
  on.exit(close(connection), add = TRUE)
  signature <- readBin(connection, what = "raw", n = 8L)
  expected <- as.raw(c(0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a))
  if (!identical(signature, expected)) {
    stop("Generated asset is not a valid PNG: ", path, call. = FALSE)
  }
}

atomic_png <- function(destination, draw) {
  assert_owned_output(destination)
  temporary <- tempfile(
    pattern = paste0(".", basename(destination), "."),
    tmpdir = dirname(destination),
    fileext = ".png"
  )
  on.exit(unlink(temporary), add = TRUE)
  draw(temporary)
  assert_png(temporary)
  if (!file.rename(temporary, destination)) {
    stop("Could not atomically install summary asset: ", destination, call. = FALSE)
  }
  Sys.chmod(destination, mode = "0644")
  invisible(destination)
}

logo_path <- file.path(locale_asset_root, "ratiomera-summary-logo.png")
atomic_png(logo_path, function(path) {
  ragg::agg_png(path, width = 900, height = 230, units = "px", res = 144, background = "transparent")
  on.exit(grDevices::dev.off(), add = TRUE)
  grid::grid.newpage()
  navy <- "#183B56"
  blue <- "#2F6F9F"
  # Draw the same open, measured R used by the browser identity. The upper
  # curve is sampled explicitly so the document pipeline remains independent
  # of SVG rendering support.
  grid::grid.lines(
    x = grid::unit(rep(0.055, 2), "npc"),
    y = grid::unit(c(0.16, 0.84), "npc"),
    gp = grid::gpar(col = navy, lwd = 16, lineend = "round")
  )
  grid::grid.lines(
    x = grid::unit(c(0.055, 0.105, 0.155, 0.190, 0.205, 0.190, 0.155, 0.105, 0.055), "npc"),
    y = grid::unit(c(0.84, 0.84, 0.82, 0.75, 0.68, 0.60, 0.54, 0.52, 0.52), "npc"),
    gp = grid::gpar(col = navy, lwd = 16, lineend = "round", linejoin = "round")
  )
  grid::grid.lines(
    x = grid::unit(c(0.115, 0.205), "npc"),
    y = grid::unit(c(0.52, 0.16), "npc"),
    gp = grid::gpar(col = blue, lwd = 16, lineend = "round")
  )
  grid::grid.lines(
    x = grid::unit(c(0.110, 0.172), "npc"),
    y = grid::unit(c(0.68, 0.68), "npc"),
    gp = grid::gpar(col = blue, lwd = 7, lineend = "round")
  )
  grid::grid.text(
    "RATIOMERA",
    x = grid::unit(0.235, "npc"),
    y = grid::unit(0.51, "npc"),
    just = "left",
    gp = grid::gpar(col = navy, fontsize = 34, fontface = "bold", fontfamily = "sans")
  )
  grid::grid.text(
    "STATISTICS",
    x = grid::unit(0.238, "npc"),
    y = grid::unit(0.28, "npc"),
    just = "left",
    gp = grid::gpar(col = blue, fontsize = 12, fontface = "bold", fontfamily = "sans")
  )
})
message("Generated ", sub(paste0("^", project_root, "/"), "", logo_path))

for (topic_number in selected_topics) {
  registration <- topic_registry[[topic_number]]
  source_path <- normalizePath(file.path(source_root, registration$source), mustWork = TRUE)
  if (!identical(dirname(source_path), normalizePath(source_root, mustWork = TRUE))) {
    stop("Registered plot source escaped the trusted shared directory.", call. = FALSE)
  }
  environment <- new.env(parent = globalenv())
  environment$topic_locale <- selected_locale
  sys.source(source_path, envir = environment, keep.source = FALSE)
  if (!exists(registration$object, envir = environment, inherits = FALSE)) {
    stop("Registered plot object was not created: ", registration$object, call. = FALSE)
  }
  plot <- get(registration$object, envir = environment, inherits = FALSE)
  if (!inherits(plot, "ggplot")) {
    stop("Registered plot object is not a ggplot: ", registration$object, call. = FALSE)
  }
  # Keep titles, axis labels, and bottom legends clear of the raster boundary.
  # Applying the same margin at export time preserves figure geometry across
  # locales while accommodating the different lengths of localized labels.
  plot <- plot + ggplot2::theme(
    plot.margin = ggplot2::margin(t = 12, r = 16, b = 20, l = 16)
  )
  localized_asset <- sub(
    "-en\\.png$", paste0("-", selected_locale, ".png"), registration$asset
  )
  destination <- file.path(locale_asset_root, localized_asset)
  atomic_png(destination, function(path) {
    ggplot2::ggsave(
      filename = path,
      plot = plot,
      device = ragg::agg_png,
      width = 8.3,
      height = 4.9,
      units = "in",
      dpi = 180,
      bg = "white",
      limitsize = TRUE
    )
  })
  message("Generated ", sub(paste0("^", project_root, "/"), "", destination))
}
