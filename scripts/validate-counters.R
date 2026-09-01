#!/usr/bin/env Rscript

script_arg <- grep("^--file=", commandArgs(trailingOnly = FALSE), value = TRUE)
script_path <- if (length(script_arg)) sub("^--file=", "", script_arg[[1]]) else "scripts/validate-counters.R"
project_dir <- normalizePath(file.path(dirname(script_path), ".."), mustWork = TRUE)
old_dir <- setwd(project_dir)
on.exit(setwd(old_dir), add = TRUE)

for (package in c("xml2", "yaml", "jsonlite")) {
  if (!requireNamespace(package, quietly = TRUE)) {
    stop("Counter validation requires the R package '", package, "'.", call. = FALSE)
  }
}

config <- yaml::read_yaml("config/counters.yml")
manifest <- yaml::read_yaml("config/content-parity.yml")
downloads <- yaml::read_yaml("ratiomera-statistics/_shared/downloads.yml")
locales <- c("en", "de", "sq")
failures <- character()
fail <- function(message) failures <<- c(failures, message)

if (!identical(as.integer(config$schema_version), 2L)) {
  fail("Counter configuration must use schema_version 2.")
}
if (!identical(as.integer(downloads$schema_version), 4L)) {
  fail("Download metadata must use schema_version 4.")
}

render_identifier <- function(template, values) {
  identifier <- as.character(template)
  for (name in names(values)) {
    identifier <- gsub(
      paste0("{", name, "}"), as.character(values[[name]]), identifier, fixed = TRUE
    )
  }
  identifier
}

download_topics <- function(metadata) {
  if (!is.null(metadata$courses)) {
    return(unlist(lapply(metadata$courses, function(course) course$topics), recursive = FALSE))
  }
  metadata$topics
}

download_bundles <- function(metadata) {
  if (is.null(metadata$courses)) return(list())
  unlist(lapply(metadata$courses, function(course) {
    if (is.null(course$bundles)) list() else course$bundles
  }), recursive = FALSE)
}

download_files <- function(material) {
  if (!is.null(material$files)) return(material$files)
  if (is.null(material$format) || is.null(material$paths)) return(list())
  list(list(format = material$format, paths = material$paths))
}

included_page_types <- as.character(unlist(
  config$page_visits$included_page_types, use.names = FALSE
))
canonical_pages <- manifest$pages[vapply(manifest$pages, function(page) {
  as.character(page$page_type) %in% included_page_types
}, logical(1))]

route_records <- unlist(lapply(canonical_pages, function(page) {
  lapply(locales, function(locale) {
    list(
      page_id = as.character(page$id),
      locale = locale,
      output = file.path("docs", sub("\\.qmd$", ".html", as.character(page$paths[[locale]]))),
      counter_id = render_identifier(
        config$page_visits$id_template,
        list(page_id = as.character(page$id), locale = locale)
      )
    )
  })
}), recursive = FALSE)
names(route_records) <- vapply(route_records, function(record) record$output, character(1))

output_list <- Sys.getenv("QUARTO_PROJECT_OUTPUT_FILES", unset = "")
if (nzchar(output_list)) {
  rendered <- strsplit(output_list, "\n", fixed = TRUE)[[1]]
  rendered <- rendered[nzchar(rendered) & grepl("\\.html$", rendered)]
  rendered <- vapply(rendered, function(path) {
    normalized <- gsub("\\\\", "/", path)
    if (startsWith(normalized, paste0(gsub("\\\\", "/", project_dir), "/"))) {
      substring(normalized, nchar(project_dir) + 2L)
    } else {
      normalized
    }
  }, character(1))
  records_to_check <- route_records[names(route_records) %in% rendered]
  full_validation <- length(records_to_check) == length(route_records)
} else {
  rendered <- character()
  records_to_check <- route_records
  full_validation <- TRUE
}

counter_xpath <- "//*[local-name()='usage-page-visit-counter' and contains(concat(' ', normalize-space(@class), ' '), ' page-visit-counter ')]"
for (record in records_to_check) {
  if (!file.exists(record$output)) {
    fail(sprintf("Missing rendered canonical counter route: %s", record$output))
    next
  }
  document <- xml2::read_html(record$output)
  refresh <- xml2::xml_find_all(
    document,
    "//meta[translate(@http-equiv, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz')='refresh']"
  )
  counters <- xml2::xml_find_all(document, counter_xpath)
  config_nodes <- xml2::xml_find_all(document, "//*[@id='usage-counter-config']")
  if (length(refresh)) fail(sprintf("Canonical counter route redirects: %s", record$output))
  if (length(counters) != 1L) fail(sprintf("Expected one page counter in %s; found %d.", record$output, length(counters)))
  if (length(config_nodes) != 1L) fail(sprintf("Expected one embedded counter config in %s; found %d.", record$output, length(config_nodes)))
  if (length(counters) == 1L) {
    expected_label <- as.character(config$locales[[record$locale]]$visits)
    if (!identical(xml2::xml_attr(counters, "data-counter-id"), record$counter_id)) {
      fail(sprintf("Page-counter ID mismatch in %s.", record$output))
    }
    if (!identical(xml2::xml_attr(counters, "data-page-id"), record$page_id) ||
        !identical(xml2::xml_attr(counters, "data-locale"), record$locale)) {
      fail(sprintf("Page-counter route metadata mismatch in %s.", record$output))
    }
    if (!identical(xml2::xml_attr(counters, "data-label"), expected_label)) {
      fail(sprintf("Page-counter label mismatch in %s.", record$output))
    }
    visible_value <- trimws(xml2::xml_text(xml2::xml_find_first(counters, ".//*[contains(concat(' ', normalize-space(@class), ' '), ' counter-value ')]")))
    if (!identical(visible_value, as.character(config$placeholder))) {
      fail(sprintf("Page-counter placeholder mismatch in %s.", record$output))
    }
  }
  if (length(config_nodes) == 1L) {
    embedded <- tryCatch(
      jsonlite::fromJSON(xml2::xml_text(config_nodes)),
      error = function(error) NULL
    )
    if (is.null(embedded) ||
        !identical(as.character(embedded$page_visits$provider), as.character(config$page_visits$provider)) ||
        !identical(as.character(embedded$download_counts$provider), as.character(config$download_counts$provider))) {
      fail(sprintf("Embedded counter configuration is invalid in %s.", record$output))
    }
  }
}

all_rendered_html <- if (dir.exists("docs")) {
  list.files("docs", pattern = "\\.html$", recursive = TRUE, full.names = TRUE)
} else {
  character()
}
files_to_check_for_redirects <- unique(c(rendered, all_rendered_html))
for (path in files_to_check_for_redirects[file.exists(files_to_check_for_redirects)]) {
  document <- xml2::read_html(path)
  refresh <- xml2::xml_find_all(
    document,
    "//meta[translate(@http-equiv, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz')='refresh']"
  )
  source_text <- paste(readLines(path, warn = FALSE, encoding = "UTF-8"), collapse = "\n")
  script_redirect <- grepl("var redirects =", source_text, fixed = TRUE)
  if (!length(refresh) && !script_redirect) next
  counters <- xml2::xml_find_all(document, counter_xpath)
  if (length(counters)) fail(sprintf("Redirect output contains a page counter: %s", path))
  html_language <- xml2::xml_attr(xml2::xml_find_first(document, "//html"), "lang")
  if (is.na(html_language) || !nzchar(trimws(html_language))) {
    fail(sprintf("Redirect output lacks a document language: %s", path))
  }
}

courses <- if (is.null(downloads$courses)) list() else downloads$courses
topics <- download_topics(downloads)
bundles <- download_bundles(downloads)
individual_materials <- unlist(lapply(topics, function(topic) topic$materials), recursive = FALSE)
topic_packages <- lapply(topics, function(topic) topic$package)
primary_bundles <- bundles[vapply(bundles, function(bundle) identical(bundle$primary, TRUE), logical(1))]
secondary_bundles <- bundles[vapply(bundles, function(bundle) !identical(bundle$primary, TRUE), logical(1))]
counted_packages <- c(topic_packages, primary_bundles)
all_materials <- c(individual_materials, topic_packages, bundles)
material_ids <- vapply(all_materials, function(material) as.character(material$id), character(1))
counted_package_ids <- vapply(counted_packages, function(material) as.character(material$id), character(1))
if (length(counted_package_ids) != 9L || anyDuplicated(counted_package_ids)) {
  fail("The current Downloads architecture must define exactly nine unique visible package IDs.")
}
if (anyDuplicated(material_ids)) {
  fail("All registered download IDs must be unique.")
}

release_key_by_material <- character()
for (course in courses) {
  release_key <- as.character(course$release_key)
  release_settings <- if (nzchar(release_key)) {
    config$download_counts$providers$github_releases$releases[[release_key]]
  } else {
    NULL
  }
  if (!nzchar(release_key) || is.null(release_settings)) {
    fail(sprintf("Download course %s has no matching release-key configuration.", course$id))
  }
  course_materials <- c(
    unlist(lapply(course$topics, function(topic) topic$materials), recursive = FALSE),
    lapply(course$topics, function(topic) topic$package),
    course$bundles
  )
  course_ids <- vapply(course_materials, function(material) as.character(material$id), character(1))
  release_key_by_material[course_ids] <- release_key
}
downloads_records <- records_to_check[vapply(records_to_check, function(record) {
  identical(record$page_id, "statistics-downloads")
}, logical(1))]

for (record in downloads_records) {
  document <- xml2::read_html(record$output)
  count_nodes <- xml2::xml_find_all(document, "//*[local-name()='usage-download-count']")
  if (length(count_nodes) != length(counted_package_ids)) {
    fail(sprintf(
      "Expected %d package-count fields in %s; found %d.",
      length(counted_package_ids), record$output, length(count_nodes)
    ))
  }
  collections <- xml2::xml_find_all(
    document,
    "//section[contains(concat(' ', normalize-space(@class), ' '), ' download-course ')]"
  )
  if (length(collections) != length(downloads$courses) ||
      any(is.na(xml2::xml_attr(collections, "aria-labelledby")))) {
    fail(sprintf("Download collections lack one accessible heading reference each in %s.", record$output))
  } else {
    heading_ids <- xml2::xml_attr(collections, "aria-labelledby")
    for (heading_id in heading_ids) {
      targets <- xml2::xml_find_all(document, sprintf("//*[@id='%s']", heading_id))
      if (length(targets) != 1L) {
        fail(sprintf("Download collection heading reference %s is not unique in %s.", heading_id, record$output))
      }
    }
  }

  topic_cards <- xml2::xml_find_all(
    document,
    "//*[contains(concat(' ', normalize-space(@class), ' '), ' download-topic-card ')][@data-topic-id]"
  )
  topic_details <- xml2::xml_find_all(
    document,
    "//*[contains(concat(' ', normalize-space(@class), ' '), ' download-topic-card ')]/details[contains(concat(' ', normalize-space(@class), ' '), ' download-topic-files ')]"
  )
  material_options <- xml2::xml_find_all(
    document,
    "//*[contains(concat(' ', normalize-space(@class), ' '), ' download-material-option ')]"
  )
  if (length(topic_cards) != length(topics) || length(topic_details) != length(topics) ||
      length(material_options) != length(individual_materials)) {
    fail(sprintf("Downloads topic-package structure mismatch in %s.", record$output))
  }

  primary_sections <- xml2::xml_find_all(
    document,
    "//section[contains(concat(' ', normalize-space(@class), ' '), ' download-primary-package ')]"
  )
  secondary_sections <- xml2::xml_find_all(
    document,
    "//details[contains(concat(' ', normalize-space(@class), ' '), ' download-secondary-bundles ')]"
  )
  bundle_cards <- xml2::xml_find_all(
    document,
    "//*[contains(concat(' ', normalize-space(@class), ' '), ' download-bundle-card ')]"
  )
  primary_cards <- xml2::xml_find_all(
    document,
    "//section[contains(concat(' ', normalize-space(@class), ' '), ' download-primary-package ')]//*[contains(concat(' ', normalize-space(@class), ' '), ' download-bundle-card ')]"
  )
  secondary_cards <- xml2::xml_find_all(
    document,
    "//details[contains(concat(' ', normalize-space(@class), ' '), ' download-secondary-bundles ')]//*[contains(concat(' ', normalize-space(@class), ' '), ' download-bundle-card ')]"
  )
  if (length(primary_sections) != length(courses) ||
      length(secondary_sections) != length(courses) ||
      length(bundle_cards) != length(bundles) ||
      length(primary_cards) != length(primary_bundles) ||
      length(secondary_cards) != length(secondary_bundles)) {
    fail(sprintf("Downloads bundle structure mismatch in %s.", record$output))
  }

  for (material in all_materials) {
    material_id <- as.character(material$id)
    release_key <- unname(release_key_by_material[[material_id]])
    available <- identical(as.character(material$status), "available")
    locale_files <- download_files(material)
    locale_files <- locale_files[vapply(locale_files, function(file) {
      !is.null(file$paths) && !is.null(file$paths[[record$locale]]) &&
        nzchar(as.character(file$paths[[record$locale]]))
    }, logical(1))]
    expected_assets <- if (available) {
      vapply(locale_files, function(file) basename(as.character(file$paths[[record$locale]])), character(1))
    } else {
      character()
    }
    links <- xml2::xml_find_all(
      document,
      sprintf("//a[contains(concat(' ', normalize-space(@class), ' '), ' download-asset-action ')][@data-material-id='%s']", material_id)
    )
    if (available && length(links) != length(expected_assets)) {
      fail(sprintf(
        "Available material %s must expose %d release-resolvable link(s) in %s; found %d.",
        material_id, length(expected_assets), record$output, length(links)
      ))
    }
    if (!available && length(links)) {
      fail(sprintf("Unavailable material %s has a download link in %s.", material_id, record$output))
    }
    if (length(links)) {
      link_ids <- xml2::xml_attr(links, "data-material-id")
      link_release_keys <- xml2::xml_attr(links, "data-release-key")
      link_assets <- xml2::xml_attr(links, "data-release-asset")
      link_fallbacks <- xml2::xml_attr(links, "download")
      if (any(link_ids != material_id) || any(link_release_keys != release_key) ||
          any(is.na(link_fallbacks)) || !identical(sort(link_assets), sort(expected_assets))) {
        fail(sprintf("Download-link metadata mismatch for %s in %s.", material_id, record$output))
      }
    }

    counter <- xml2::xml_find_all(
      document,
      sprintf("//*[local-name()='usage-download-count' and @data-material-id='%s']", material_id)
    )
    should_be_counted <- material_id %in% counted_package_ids
    if (!should_be_counted && length(counter)) {
      fail(sprintf("Uncounted individual or secondary material %s exposes a count in %s.", material_id, record$output))
    }
    if (!should_be_counted) next

    expected_id <- render_identifier(
      config$download_counts$id_template,
      list(material_id = material_id, locale = record$locale)
    )
    if (length(counter) != 1L ||
        !identical(xml2::xml_attr(counter, "data-counter-id"), expected_id) ||
        !identical(xml2::xml_attr(counter, "data-release-key"), release_key)) {
      fail(sprintf("Download-counter identity mismatch for %s in %s.", material_id, record$output))
      next
    }
    if (!identical(trimws(xml2::xml_text(counter)), as.character(config$placeholder))) {
      fail(sprintf("Download-counter placeholder mismatch for %s in %s.", material_id, record$output))
    }
    expected_available <- if (available) "true" else "false"
    expected_asset_value <- paste(expected_assets, collapse = "|")
    if (!identical(xml2::xml_attr(counter, "data-material-available"), expected_available) ||
        (available && !identical(xml2::xml_attr(counter, "data-release-assets"), expected_asset_value))) {
      fail(sprintf("Download-counter asset metadata mismatch for %s in %s.", material_id, record$output))
    }
  }
}

if (full_validation && length(records_to_check) != as.integer(manifest$usage_counters$canonical_route_count)) {
  fail("Full counter validation did not cover the declared canonical route count.")
}

if (length(failures)) {
  cat("Counter validation failures\n")
  cat(paste0("- ", unique(failures), collapse = "\n"), "\n")
  quit(save = "no", status = 1L)
}

mode <- if (full_validation) "full" else "partial"
cat(sprintf(
  "Counter validation PASS (%s): %d canonical route(s), %d stable download ID(s), %d visible package ID(s), providers %s/%s.\n",
  mode, length(records_to_check), length(material_ids), length(counted_package_ids),
  config$page_visits$provider, config$download_counts$provider
))
