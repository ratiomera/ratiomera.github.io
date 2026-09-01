# Shared presentation helpers for interactive Plotly figures.
#
# Plotly does not wrap ggplot titles or axis labels automatically. Long German
# and Albanian labels can therefore be clipped even when the surrounding page
# is responsive. Keep the underlying figure geometry unchanged, but insert
# deliberate HTML line breaks at word boundaries before the widget is built.

ratiomera_wrap_plotly_text <- function(value, width) {
  if (is.null(value) || !length(value) || is.na(value[[1]])) return(value)

  original <- as.character(value[[1]])
  is_bold <- grepl("^\\s*<b>", original, ignore.case = TRUE)
  plain <- gsub("<br\\s*/?>", "\n", original, ignore.case = TRUE)
  plain <- gsub("<[^>]+>", "", plain)
  plain <- trimws(plain)

  paragraphs <- strsplit(plain, "\n", fixed = TRUE)[[1]]
  wrapped <- unlist(
    lapply(
      paragraphs,
      function(paragraph) {
        lines <- strwrap(trimws(paragraph), width = width, simplify = TRUE)
        if (length(lines)) lines else ""
      }
    ),
    use.names = FALSE
  )
  output <- paste(wrapped, collapse = "<br>")

  if (is_bold) paste0("<b>", output, "</b>") else output
}

# ggplotly currently drops GeomLabel layers altogether. Those layers often
# carry the most important words in a teaching diagram, so silently losing
# them would make an interactive conversion less informative than the static
# source. For browser output, copy the plot and turn label layers into plain
# text layers at the identical coordinates. The original ggplot object is not
# changed, and its data and mathematical geometry remain untouched.
ratiomera_make_plotly_compatible <- function(plot) {
  if (!inherits(plot, "ggplot")) return(plot)

  compatible <- plot
  for (layer_index in seq_along(compatible$layers)) {
    layer <- compatible$layers[[layer_index]]
    if (!inherits(layer$geom, "GeomLabel")) next

    layer$geom <- ggplot2::GeomText
    label_only_parameters <- c(
      "fill", "linewidth", "label.padding", "label.r", "label.size"
    )
    layer$aes_params[label_only_parameters] <- NULL
    layer$geom_params[label_only_parameters] <- NULL
    compatible$layers[[layer_index]] <- layer
  }

  compatible
}

ratiomera_plotly_alt_from_plot <- function(plot, locale = "en", detail = NULL) {
  prefix <- switch(
    locale,
    de = "Interaktive Lehrabbildung.",
    sq = "Figurë mësimore ndërvepruese.",
    "Interactive teaching figure."
  )
  title <- if (inherits(plot, "ggplot") && !is.null(plot$labels$title)) {
    as.character(plot$labels$title)
  } else {
    ""
  }
  subtitle <- if (inherits(plot, "ggplot") && !is.null(plot$labels$subtitle)) {
    as.character(plot$labels$subtitle)
  } else {
    ""
  }

  paste(Filter(nzchar, c(prefix, title, subtitle, detail)), collapse = " ")
}

ratiomera_plotly_hover_labels <- function(plot, locale = "en") {
  generic <- switch(
    locale,
    de = c(
      x = "Horizontaler Wert", y = "Vertikaler Wert", label = "Beschriftung",
      value = "Wert", density = "Dichte", sample = "Stichprobe",
      edge_label = "Verbindung", label_x = "Horizontale Position",
      label_y = "Vertikale Position", point_label_y = "Vertikale Position",
      scenario_y = "Szenario", coefficient = "Koeffizient", kind = "Element"
    ),
    sq = c(
      x = "Vlera horizontale", y = "Vlera vertikale", label = "Etiketa",
      value = "Vlera", density = "Dendësia", sample = "Kampioni",
      edge_label = "Lidhja", label_x = "Pozicioni horizontal",
      label_y = "Pozicioni vertikal", point_label_y = "Pozicioni vertikal",
      scenario_y = "Skenari", coefficient = "Koeficienti", kind = "Elementi"
    ),
    c(
      x = "Horizontal value", y = "Vertical value", label = "Label",
      value = "Value", density = "Density", sample = "Sample",
      edge_label = "Connection", label_x = "Horizontal position",
      label_y = "Vertical position", point_label_y = "Vertical position",
      scenario_y = "Scenario", coefficient = "Coefficient", kind = "Element"
    )
  )

  if (inherits(plot, "ggplot")) {
    if (!is.null(plot$labels$x) && nzchar(as.character(plot$labels$x))) {
      generic[["x"]] <- as.character(plot$labels$x)
    }
    if (!is.null(plot$labels$y) && nzchar(as.character(plot$labels$y))) {
      generic[["y"]] <- as.character(plot$labels$y)
    }
  }
  generic
}

ratiomera_localize_plotly_hover <- function(widget, field_labels) {
  if (!inherits(widget, "plotly") || !length(field_labels)) return(widget)

  rewrite <- function(values) {
    if (is.null(values) || !length(values)) return(values)
    vapply(
      as.character(values),
      function(value) {
        if (is.na(value) || !nzchar(value)) return("")
        parts <- strsplit(value, "<br\\s*/?>", perl = TRUE)[[1]]
        for (part_index in seq_along(parts)) {
          part <- parts[[part_index]]
          for (field in names(field_labels)) {
            prefix <- paste0(field, ":")
            if (!startsWith(trimws(part), prefix)) next
            remainder <- trimws(substring(trimws(part), nchar(prefix) + 1L))
            parts[[part_index]] <- paste0(field_labels[[field]], ": ", remainder)
            break
          }
        }
        paste(parts, collapse = "<br>")
      },
      character(1),
      USE.NAMES = FALSE
    )
  }

  for (trace_index in seq_along(widget$x$data)) {
    trace <- widget$x$data[[trace_index]]
    trace$text <- rewrite(trace$text)
    trace$hovertext <- rewrite(trace$hovertext)

    has_hovertext <- !is.null(trace$hovertext) && any(nzchar(trace$hovertext))
    has_text <- !is.null(trace$text) && any(nzchar(trace$text))
    if (has_hovertext) {
      # htmlwidgets serializes a one-value character vector as a scalar. For
      # a one-point teaching trace, older bundled Plotly builds can then show
      # the token `%{hovertext}` literally instead of substituting its value.
      # Writing the already localized value directly avoids that ambiguity;
      # multi-point traces keep the ordinary per-point token.
      trace$hovertemplate <- if (length(trace$hovertext) == 1L) {
        paste0(trace$hovertext[[1]], "<extra></extra>")
      } else {
        "%{hovertext}<extra></extra>"
      }
      trace$hoverinfo <- "text"
    } else if (has_text) {
      trace$hovertemplate <- if (length(trace$text) == 1L) {
        paste0(trace$text[[1]], "<extra></extra>")
      } else {
        "%{text}<extra></extra>"
      }
      trace$hoverinfo <- "text"
    }
    widget$x$data[[trace_index]] <- trace
  }
  widget
}

# Plotly generates its box-summary tooltip inside the browser. Those built-in
# labels ("median", "upper fence", and similar) therefore remain English even
# after the ordinary trace text has been localized in R. Suppress only the box
# traces so an accompanying observation layer can provide deliberate,
# localized interaction without an English tooltip appearing on top of it.
ratiomera_suppress_box_trace_hover <- function(widget) {
  if (!inherits(widget, "plotly")) return(widget)

  for (trace_index in seq_along(widget$x$data)) {
    trace <- widget$x$data[[trace_index]]
    if (!identical(trace$type, "box")) next
    trace$hoverinfo <- "skip"
    trace$hovertemplate <- "<extra></extra>"
    widget$x$data[[trace_index]] <- trace
  }

  widget
}

ratiomera_prepare_plotly_widget <- function(
  widget,
  title_width = 42L,
  axis_width = 32L,
  annotation_width = 34L,
  title_size = 16
) {
  if (!inherits(widget, "plotly")) return(widget)

  # ggplotly can defer conversion of axes, annotations, and traces until the
  # widget is printed. Build once here so every localization and wrapping rule
  # below acts on the structure that the browser will actually receive.
  if (!length(widget$x$data)) {
    widget <- plotly::plotly_build(widget)
  }

  if (!is.null(widget$x$layout$title$text)) {
    widget$x$layout$title$text <- ratiomera_wrap_plotly_text(
      widget$x$layout$title$text,
      title_width
    )
    # ggplotly otherwise converts the same source theme to a relatively large
    # browser font that can dominate a compact widget. One shared value keeps
    # figure headings visually consistent across topics and languages.
    if (is.null(widget$x$layout$title$font)) {
      widget$x$layout$title$font <- list()
    }
    widget$x$layout$title$font$size <- title_size
  }

  axis_names <- grep("^[xyz]axis[0-9]*$", names(widget$x$layout), value = TRUE)
  for (axis_name in axis_names) {
    axis <- widget$x$layout[[axis_name]]
    if (is.null(axis$title)) next

    if (is.list(axis$title) && !is.null(axis$title$text)) {
      axis$title$text <- ratiomera_wrap_plotly_text(axis$title$text, axis_width)
    } else if (is.character(axis$title)) {
      axis$title <- ratiomera_wrap_plotly_text(axis$title, axis_width)
    }
    widget$x$layout[[axis_name]] <- axis
  }

  if (length(widget$x$layout$annotations)) {
    for (annotation_index in seq_along(widget$x$layout$annotations)) {
      annotation <- widget$x$layout$annotations[[annotation_index]]
      if (is.null(annotation$text)) next

      width <- if (identical(annotation$annotationType, "axis")) {
        axis_width
      } else {
        annotation_width
      }
      annotation$text <- ratiomera_wrap_plotly_text(annotation$text, width)
      widget$x$layout$annotations[[annotation_index]] <- annotation
    }
  }

  widget
}
