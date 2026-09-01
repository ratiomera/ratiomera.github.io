download_metadata <- function(metadata_path) {
  if (!requireNamespace("yaml", quietly = TRUE)) {
    stop("Download components require the R package 'yaml'.", call. = FALSE)
  }
  yaml::read_yaml(metadata_path)
}

download_escape_helpers <- function() {
  if (!requireNamespace("htmltools", quietly = TRUE)) {
    stop("Download components require the R package 'htmltools'.", call. = FALSE)
  }
  list(
    text = function(value) htmltools::htmlEscape(as.character(value), attribute = FALSE),
    attr = function(value) htmltools::htmlEscape(as.character(value), attribute = TRUE)
  )
}

download_courses <- function(metadata) {
  if (!is.null(metadata$courses)) return(metadata$courses)
  list(list(id = "intro-statistics", topics = metadata$topics))
}

download_files <- function(material) {
  if (!is.null(material$files)) return(material$files)
  if (is.null(material$format) || is.null(material$paths)) return(list())
  list(list(format = material$format, paths = material$paths))
}

download_counter_id <- function(template, values) {
  identifier <- as.character(template)
  for (name in names(values)) {
    identifier <- gsub(
      paste0("{", name, "}"), as.character(values[[name]]), identifier, fixed = TRUE
    )
  }
  if (grepl("\\{[^}]+\\}", identifier)) {
    stop(sprintf("Unresolved counter ID template: %s", identifier), call. = FALSE)
  }
  identifier
}

download_locale_files <- function(material, locale) {
  files <- download_files(material)
  files[vapply(files, function(file) {
    !is.null(file$paths) && !is.null(file$paths[[locale]]) &&
      nzchar(as.character(file$paths[[locale]]))
  }, logical(1))]
}

download_count_markup <- function(
  material,
  locale_files,
  locale,
  release_key,
  counter_config,
  counter_labels,
  escape,
  escape_attr,
  wrapper_class = "download-material-count"
) {
  material_id <- as.character(material$id)
  available <- identical(as.character(material$status), "available")
  counter_id <- download_counter_id(
    counter_config$download_counts$id_template,
    list(material_id = material_id, locale = locale)
  )
  release_assets <- if (available) {
    paste(vapply(locale_files, function(file) {
      basename(as.character(file$paths[[locale]]))
    }, character(1)), collapse = "|")
  } else {
    ""
  }
  counter <- paste0(
    '<usage-download-count class="download-count usage-counter" role="group"',
    ' data-counter-id="', escape_attr(counter_id), '"',
    ' data-material-id="', escape_attr(material_id), '"',
    ' data-material-available="', if (available) "true" else "false", '"',
    ' data-locale="', escape_attr(locale), '"',
    ' data-release-key="', escape_attr(release_key), '"',
    ' data-label="', escape_attr(counter_labels$downloads), '"',
    if (nzchar(release_assets)) paste0(' data-release-assets="', escape_attr(release_assets), '"') else "",
    ' aria-label="', escape_attr(sprintf("%s: %s", counter_labels$downloads, counter_labels$unavailable)), '">',
    '<span class="counter-value" aria-hidden="true">', escape(counter_config$placeholder),
    '</span></usage-download-count>'
  )
  paste0(
    '<div class="', escape_attr(wrapper_class), '">',
    '<span class="download-count-label" aria-hidden="true">',
    escape(counter_labels$downloads), '</span>', counter, '</div>'
  )
}

download_find_topic <- function(metadata, course_id, topic_id = NULL, topic_number = NULL) {
  if (is.null(topic_id) == is.null(topic_number)) {
    stop("Supply exactly one of topic_id or topic_number.", call. = FALSE)
  }
  courses <- download_courses(metadata)
  course_matches <- vapply(
    courses,
    function(course) identical(as.character(course$id), as.character(course_id)),
    logical(1)
  )
  if (sum(course_matches) != 1L) {
    stop(sprintf("Expected one download collection for %s; found %d.", course_id, sum(course_matches)), call. = FALSE)
  }
  course <- courses[[which(course_matches)]]
  topic_matches <- vapply(course$topics, function(topic) {
    if (!is.null(topic_id)) {
      identical(as.character(topic$id), as.character(topic_id))
    } else {
      identical(as.integer(topic$number), as.integer(topic_number))
    }
  }, logical(1))
  if (sum(topic_matches) != 1L) {
    selector <- if (!is.null(topic_id)) as.character(topic_id) else as.character(topic_number)
    stop(sprintf("Expected one Downloads topic for %s in %s; found %d.", selector, course_id, sum(topic_matches)), call. = FALSE)
  }
  list(course = course, topic = course$topics[[which(topic_matches)]])
}

render_downloads <- function(metadata_path, locale, counter_config_path) {
  metadata <- download_metadata(metadata_path)
  counter_config <- yaml::read_yaml(counter_config_path)
  allowed_locales <- as.character(unlist(metadata$locale_order, use.names = FALSE))
  if (!locale %in% allowed_locales) {
    stop(sprintf("Unsupported Downloads locale: %s", locale), call. = FALSE)
  }
  if (!identical(as.integer(metadata$schema_version), 4L)) {
    stop("Downloads renderer requires metadata schema_version 4.", call. = FALSE)
  }

  labels <- metadata$locales[[locale]]
  counter_labels <- counter_config$locales[[locale]]
  if (is.null(counter_labels)) {
    stop(sprintf("Missing counter labels for Downloads locale: %s", locale), call. = FALSE)
  }
  esc <- download_escape_helpers()
  escape <- esc$text
  escape_attr <- esc$attr

  render_actions <- function(
    material,
    descriptor,
    context_title,
    release_key,
    href_prefix = "files",
    extra_classes = ""
  ) {
    material_id <- as.character(material$id)
    available <- identical(as.character(material$status), "available")
    locale_files <- download_locale_files(material, locale)
    if (available && !length(locale_files)) {
      stop(sprintf("Available download %s has no %s file.", material_id, locale), call. = FALSE)
    }
    if (!available) {
      return(sprintf('<span class="download-unavailable">%s</span>', escape(labels$unavailable_text)))
    }
    actions <- vapply(locale_files, function(file) {
      source_path <- as.character(file$paths[[locale]])
      format <- as.character(file$format)
      display_format <- if (!is.null(file$label) && !is.null(file$label[[locale]])) {
        as.character(file$label[[locale]])
      } else {
        format
      }
      href <- paste0(sub("/+$", "", href_prefix), "/", basename(source_path))
      action_label <- sprintf(labels$download_action_template, display_format)
      action_aria <- sprintf(labels$download_aria_template, descriptor, context_title, format)
      classes <- trimws(paste("download-action download-asset-action", extra_classes))
      paste0(
        '<a class="', escape_attr(classes), '" href="', escape_attr(href), '" download',
        ' data-material-id="', escape_attr(material_id), '"',
        ' data-release-key="', escape_attr(release_key), '"',
        ' data-release-asset="', escape_attr(basename(source_path)), '"',
        ' aria-label="', escape_attr(action_aria), '">', escape(action_label), '</a>'
      )
    }, character(1))
    paste0('<div class="download-action-group">', paste(actions, collapse = ""), '</div>')
  }

  render_topic <- function(topic, release_key) {
    topic_title <- as.character(topic$title[[locale]])
    topic_categories <- vapply(
      topic$materials, function(material) as.character(material$category), character(1)
    )
    if (!identical(topic_categories, names(metadata$categories))) {
      stop(sprintf("Topic %s does not use the canonical material order.", topic$id), call. = FALSE)
    }
    package <- topic$package
    if (is.null(package)) {
      stop(sprintf("Topic %s has no package.", topic$id), call. = FALSE)
    }
    package_files <- download_locale_files(package, locale)
    package_actions <- render_actions(
      package, labels$topic_package_label, topic_title, release_key,
      extra_classes = "download-package-action"
    )
    package_count <- download_count_markup(
      package, package_files, locale, release_key, counter_config, counter_labels,
      escape, escape_attr,
      wrapper_class = "download-material-count download-package-count"
    )
    individual_materials <- vapply(topic$materials, function(material) {
      category <- as.character(metadata$categories[[material$category]][[locale]])
      actions <- render_actions(material, category, topic_title, release_key)
      paste0(
        '<article class="download-material-option" data-material-id="',
        escape_attr(material$id), '"><h4>', escape(category), '</h4>', actions, '</article>'
      )
    }, character(1))
    heading_id <- paste0("download-topic-title-", topic$id)
    paste0(
      '<article id="', escape_attr(topic$id), '" class="download-topic-card" role="listitem"',
      ' data-topic-id="', escape_attr(topic$id), '" data-material-id="',
      escape_attr(package$id), '">',
      '<header class="download-topic-card-heading"><span class="download-module-number" aria-hidden="true">',
      escape(topic$number), '</span><h4 id="', escape_attr(heading_id), '">',
      escape(topic_title), '</h4></header>',
      '<p class="download-topic-package-description">', escape(labels$topic_package_description), '</p>',
      package_actions, package_count,
      '<details class="download-topic-files"><summary>', escape(labels$individual_files_summary),
      '</summary><div class="download-topic-file-list">',
      paste(individual_materials, collapse = ""), '</div></details></article>'
    )
  }

  render_bundle <- function(bundle, course_title, release_key, counted = FALSE) {
    material_id <- as.character(bundle$id)
    bundle_title <- as.character(bundle$title[[locale]])
    bundle_description <- as.character(bundle$description[[locale]])
    locale_files <- download_locale_files(bundle, locale)
    actions <- render_actions(
      bundle, bundle_title, course_title, release_key,
      extra_classes = "download-bundle-action"
    )
    count <- if (counted) {
      download_count_markup(
        bundle, locale_files, locale, release_key, counter_config, counter_labels,
        escape, escape_attr,
        wrapper_class = "download-material-count download-package-count download-bundle-count"
      )
    } else {
      ""
    }
    paste0(
      '<article class="download-bundle-card" data-material-id="', escape_attr(material_id), '">',
      '<div class="download-bundle-copy"><h4>', escape(bundle_title), '</h4><p>',
      escape(bundle_description), '</p></div>', actions, count, '</article>'
    )
  }

  output <- character()
  for (course in download_courses(metadata)) {
    course_title <- as.character(course$title[[locale]])
    course_description <- if (!is.null(course$description)) {
      as.character(course$description[[locale]])
    } else {
      ""
    }
    release_key <- as.character(course$release_key)
    if (!nzchar(release_key)) {
      stop(sprintf("Download course %s has no release_key.", course$id), call. = FALSE)
    }
    primary_matches <- vapply(
      course$bundles,
      function(bundle) identical(bundle$primary, TRUE),
      logical(1)
    )
    if (sum(primary_matches) != 1L) {
      stop(sprintf("Download course %s must define exactly one primary bundle.", course$id), call. = FALSE)
    }
    primary_bundle <- course$bundles[[which(primary_matches)]]
    secondary_bundles <- course$bundles[!primary_matches]
    primary_heading_id <- paste0("download-primary-package-", course$id, "-title")
    topics_heading_id <- paste0("download-topic-packages-", course$id, "-title")
    primary_markup <- render_bundle(primary_bundle, course_title, release_key, counted = TRUE)
    topics_markup <- vapply(course$topics, render_topic, character(1), release_key = release_key)
    secondary_markup <- if (length(secondary_bundles)) {
      vapply(
        secondary_bundles, render_bundle, character(1),
        course_title = course_title, release_key = release_key, counted = FALSE
      )
    } else {
      character()
    }

    output <- c(
      output,
      paste0('<section id="download-course-', escape_attr(course$id),
             '" class="download-course" aria-labelledby="download-course-',
             escape_attr(course$id), '-title">'),
      '<div class="download-course-heading">',
      paste0('<p class="download-course-label">', escape(labels$collection_label), '</p>'),
      paste0('<h2 id="download-course-', escape_attr(course$id), '-title">',
             escape(course_title), '</h2>'),
      if (nzchar(course_description)) paste0('<p>', escape(course_description), '</p>') else "",
      '</div>',
      '<section class="download-primary-package" aria-labelledby="',
      escape_attr(primary_heading_id), '">',
      '<div class="download-primary-package-copy"><p class="download-course-label">',
      escape(labels$complete_package_label), '</p>',
      '<h3 id="', escape_attr(primary_heading_id), '">',
      escape(labels$complete_package_heading), '</h3>',
      '<p>', escape(labels$complete_package_description), '</p></div>',
      primary_markup, '</section>',
      '<section class="download-topic-packages" aria-labelledby="',
      escape_attr(topics_heading_id), '">',
      '<div class="download-topic-packages-heading"><h3 id="',
      escape_attr(topics_heading_id), '">',
      escape(labels$topic_packages_heading), '</h3><p>',
      escape(labels$topic_packages_description), '</p></div>',
      '<div class="download-topic-grid" role="list">', paste(topics_markup, collapse = ""),
      '</div></section>',
      if (length(secondary_markup)) paste0(
        '<details class="download-secondary-bundles"><summary>',
        escape(labels$secondary_bundles_summary), '</summary><p>',
        escape(labels$secondary_bundles_description), '</p>',
        '<div class="download-bundle-grid">', paste(secondary_markup, collapse = ""),
        '</div></details>'
      ) else "",
      '</section>'
    )
  }
  cat(paste(output, collapse = "\n"))
}

render_material_cards <- function(
  metadata_path,
  locale,
  course_id,
  categories,
  topic_id = NULL,
  topic_number = NULL,
  href_prefix = "../downloads/files",
  container_class = "topic-download-resources",
  formats = NULL
) {
  metadata <- download_metadata(metadata_path)
  allowed_locales <- as.character(unlist(metadata$locale_order, use.names = FALSE))
  if (!locale %in% allowed_locales) {
    stop(sprintf("Unsupported topic-resource locale: %s", locale), call. = FALSE)
  }
  selection <- download_find_topic(metadata, course_id, topic_id, topic_number)
  course <- selection$course
  topic <- selection$topic
  release_key <- as.character(course$release_key)
  labels <- metadata$locales[[locale]]
  esc <- download_escape_helpers()
  escape <- esc$text
  escape_attr <- esc$attr
  requested_formats <- if (is.null(formats)) NULL else unique(as.character(formats))
  if (!is.null(requested_formats) &&
      (!length(requested_formats) || anyNA(requested_formats) || any(!nzchar(requested_formats)))) {
    stop("Requested topic-resource formats must be non-empty strings.", call. = FALSE)
  }
  material_categories <- vapply(topic$materials, function(material) as.character(material$category), character(1))
  if (!all(categories %in% material_categories) || anyDuplicated(material_categories[material_categories %in% categories])) {
    stop(sprintf("Topic %s does not define the requested material categories exactly once.", topic$id), call. = FALSE)
  }
  selected <- topic$materials[match(categories, material_categories)]
  if (all(c("exercises", "solutions") %in% categories)) {
    practice <- selected[match(c("exercises", "solutions"), categories)]
    practice_available <- vapply(practice, function(material) identical(as.character(material$status), "available"), logical(1))
    if (any(practice_available) && !all(practice_available)) {
      stop(sprintf("Topic %s must publish exercises and solutions as a pair.", topic$id), call. = FALSE)
    }
  }

  links <- unlist(lapply(selected, function(material) {
    if (!identical(as.character(material$status), "available")) return(character())
    category <- as.character(metadata$categories[[material$category]][[locale]])
    files <- download_files(material)
    locale_files <- files[vapply(files, function(file) {
      !is.null(file$paths) && !is.null(file$paths[[locale]]) && nzchar(as.character(file$paths[[locale]]))
    }, logical(1))]
    if (!is.null(requested_formats)) {
      locale_formats <- vapply(locale_files, function(file) as.character(file$format), character(1))
      missing_formats <- setdiff(requested_formats, locale_formats)
      if (length(missing_formats)) {
        stop(sprintf(
          "Available download %s has no %s file for requested format(s): %s.",
          material$id,
          locale,
          paste(missing_formats, collapse = ", ")
        ), call. = FALSE)
      }
      if (anyDuplicated(locale_formats[locale_formats %in% requested_formats])) {
        stop(sprintf(
          "Available download %s defines a requested %s format more than once.",
          material$id,
          locale
        ), call. = FALSE)
      }
      locale_files <- locale_files[match(requested_formats, locale_formats)]
    }
    vapply(locale_files, function(file) {
      source_path <- as.character(file$paths[[locale]])
      format <- as.character(file$format)
      display_format <- if (!is.null(file$label) && !is.null(file$label[[locale]])) {
        as.character(file$label[[locale]])
      } else {
        format
      }
      href <- paste0(sub("/+$", "", href_prefix), "/", basename(source_path))
      action_label <- sprintf(labels$download_action_template, display_format)
      action_aria <- sprintf(labels$download_aria_template, category, topic$title[[locale]], format)
      paste0(
        '<a class="topic-resource-card download-asset-action" href="', escape_attr(href), '" download',
        ' data-material-id="', escape_attr(material$id), '"',
        ' data-release-key="', escape_attr(release_key), '"',
        ' data-release-asset="', escape_attr(basename(source_path)), '"',
        ' aria-label="', escape_attr(action_aria), '">',
        '<span class="topic-resource-title">', escape(category), '</span>',
        '<span class="topic-resource-action">', escape(action_label), '</span>',
        '</a>'
      )
    }, character(1))
  }), use.names = FALSE)
  group_label <- sprintf("%s %s: %s", labels$topic_label, topic$number, topic$title[[locale]])
  output <- c(
    paste0('<div class="', escape_attr(container_class), '" role="group" aria-label="', escape_attr(group_label), '">'),
    if (length(links)) links else paste0('<p class="topic-resources-empty">', escape(labels$unavailable_text), '</p>'),
    '</div>'
  )
  cat(paste(output, collapse = "\n"))
}

render_grouped_material_cards <- function(
  metadata_path,
  locale,
  course_id,
  categories,
  topic_id = NULL,
  topic_number = NULL,
  href_prefix = "../downloads/files",
  container_class = "topic-download-resources",
  formats = c("PDF", "DOCX")
) {
  metadata <- download_metadata(metadata_path)
  allowed_locales <- as.character(unlist(metadata$locale_order, use.names = FALSE))
  if (!locale %in% allowed_locales) {
    stop(sprintf("Unsupported topic-resource locale: %s", locale), call. = FALSE)
  }
  selection <- download_find_topic(metadata, course_id, topic_id, topic_number)
  course <- selection$course
  topic <- selection$topic
  release_key <- as.character(course$release_key)
  labels <- metadata$locales[[locale]]
  esc <- download_escape_helpers()
  escape <- esc$text
  escape_attr <- esc$attr
  requested_formats <- unique(as.character(formats))
  if (!length(requested_formats) || anyNA(requested_formats) || any(!nzchar(requested_formats))) {
    stop("Requested grouped-resource formats must be non-empty strings.", call. = FALSE)
  }
  material_categories <- vapply(
    topic$materials, function(material) as.character(material$category), character(1)
  )
  if (!all(categories %in% material_categories) ||
      anyDuplicated(material_categories[material_categories %in% categories])) {
    stop(sprintf("Topic %s does not define the requested material categories exactly once.", topic$id), call. = FALSE)
  }
  selected <- topic$materials[match(categories, material_categories)]
  availability <- vapply(
    selected, function(material) identical(as.character(material$status), "available"), logical(1)
  )
  if (any(availability) && !all(availability)) {
    stop(sprintf("Topic %s must publish its grouped resources as a complete set.", topic$id), call. = FALSE)
  }

  cards <- vapply(selected, function(material) {
    material_id <- as.character(material$id)
    category <- as.character(metadata$categories[[material$category]][[locale]])
    available <- identical(as.character(material$status), "available")
    locale_files <- download_locale_files(material, locale)
    if (available) {
      locale_formats <- vapply(locale_files, function(file) as.character(file$format), character(1))
      missing_formats <- setdiff(requested_formats, locale_formats)
      if (length(missing_formats)) {
        stop(sprintf(
          "Available download %s has no %s file for requested format(s): %s.",
          material_id, locale, paste(missing_formats, collapse = ", ")
        ), call. = FALSE)
      }
      if (anyDuplicated(locale_formats[locale_formats %in% requested_formats])) {
        stop(sprintf("Available download %s defines a requested %s format more than once.", material_id, locale), call. = FALSE)
      }
      locale_files <- locale_files[match(requested_formats, locale_formats)]
    }
    actions <- if (available) {
      vapply(locale_files, function(file) {
        source_path <- as.character(file$paths[[locale]])
        format <- as.character(file$format)
        display_format <- if (!is.null(file$label) && !is.null(file$label[[locale]])) {
          as.character(file$label[[locale]])
        } else {
          format
        }
        href <- paste0(sub("/+$", "", href_prefix), "/", basename(source_path))
        action_label <- sprintf(labels$download_action_template, display_format)
        action_aria <- sprintf(labels$download_aria_template, category, topic$title[[locale]], format)
        paste0(
          '<a class="topic-resource-format-action download-asset-action" href="', escape_attr(href), '" download',
          ' data-material-id="', escape_attr(material_id), '"',
          ' data-release-key="', escape_attr(release_key), '"',
          ' data-release-asset="', escape_attr(basename(source_path)), '"',
          ' aria-label="', escape_attr(action_aria), '">', escape(action_label), '</a>'
        )
      }, character(1))
    } else {
      sprintf('<span class="download-unavailable">%s</span>', escape(labels$unavailable_text))
    }
    paste0(
      '<article class="topic-resource-card topic-resource-card-grouped" role="listitem"',
      ' data-material-id="', escape_attr(material_id), '">',
      '<div class="topic-resource-copy"><h4 class="topic-resource-title">', escape(category), '</h4>',
      '<p>', escape(labels$format_choice_text), '</p></div>',
      '<div class="topic-resource-format-actions">', paste(actions, collapse = ""), '</div>',
      '</article>'
    )
  }, character(1))

  group_label <- sprintf("%s %s: %s", labels$topic_label, topic$number, topic$title[[locale]])
  output <- c(
    paste0('<div class="', escape_attr(container_class), '" role="list" aria-label="', escape_attr(group_label), '">'),
    cards,
    '</div>'
  )
  cat(paste(output, collapse = "\n"))
}

render_topic_resources <- function(
  metadata_path,
  locale,
  course_id = "intro-statistics",
  topic_id = NULL,
  topic_number = NULL,
  href_prefix = "../downloads/files"
) {
  render_grouped_material_cards(
    metadata_path = metadata_path,
    locale = locale,
    course_id = course_id,
    categories = c("exercises", "solutions"),
    topic_id = topic_id,
    topic_number = topic_number,
    href_prefix = href_prefix,
    container_class = "topic-download-resources",
    formats = c("PDF", "DOCX")
  )
}

render_summary_resources <- function(
  metadata_path,
  locale,
  course_id = "intro-statistics",
  topic_id = NULL,
  topic_number = NULL,
  href_prefix = "../downloads/files"
) {
  render_material_cards(
    metadata_path = metadata_path,
    locale = locale,
    course_id = course_id,
    categories = "summary",
    topic_id = topic_id,
    topic_number = topic_number,
    href_prefix = href_prefix,
    container_class = "topic-summary-resources",
    formats = c("PDF", "DOCX")
  )
}
