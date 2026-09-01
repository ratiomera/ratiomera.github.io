#!/usr/bin/env Rscript

# Lightweight source-level parity checks for the Ratiomera Quarto website.
# The script uses base R plus yaml, which is already used by the project.

script_arg <- grep("^--file=", commandArgs(trailingOnly = FALSE), value = TRUE)
script_path <- if (length(script_arg)) sub("^--file=", "", script_arg[[1]]) else "scripts/validate-multilingual.R"
project_dir <- normalizePath(file.path(dirname(script_path), ".."), mustWork = TRUE)
old_dir <- setwd(project_dir)
on.exit(setwd(old_dir), add = TRUE)

if (!requireNamespace("yaml", quietly = TRUE)) {
  stop("The multilingual validator requires the R package 'yaml'.", call. = FALSE)
}

manifest_path <- "config/content-parity.yml"
terminology_path <- "config/terminology.yml"
failures <- character()
warnings <- character()

fail <- function(message) failures <<- c(failures, message)
warn <- function(message) warnings <<- c(warnings, message)
as_character <- function(value) if (is.null(value)) character() else as.character(unlist(value, use.names = FALSE))
render_identifier <- function(template, values) {
  identifier <- as.character(template)
  for (name in names(values)) {
    identifier <- gsub(
      paste0("{", name, "}"), as.character(values[[name]]), identifier, fixed = TRUE
    )
  }
  if (grepl("\\{[^}]+\\}", identifier)) return(NA_character_)
  identifier
}

has_pdf_magic <- function(path) {
  tryCatch({
    connection <- file(path, open = "rb")
    on.exit(close(connection), add = TRUE)
    signature <- readBin(connection, what = "raw", n = 5L)
    identical(rawToChar(signature), "%PDF-")
  }, error = function(error) FALSE)
}

has_zip_magic <- function(path) {
  tryCatch({
    connection <- file(path, open = "rb")
    on.exit(close(connection), add = TRUE)
    signature <- readBin(connection, what = "raw", n = 4L)
    identical(signature, as.raw(c(0x50, 0x4b, 0x03, 0x04)))
  }, error = function(error) FALSE)
}

if (!file.exists(manifest_path)) stop("Missing ", manifest_path, call. = FALSE)
if (!file.exists(terminology_path)) stop("Missing ", terminology_path, call. = FALSE)

manifest <- yaml::read_yaml(manifest_path)
terminology <- yaml::read_yaml(terminology_path)
locales <- c("en", "de", "sq")
locale_tags <- c(en = "en", de = "de-CH", sq = "sq")

# Keep an internal language/subject audit distinct from independent human
# approval. Automated and AI-assisted checks can find many issues, but they
# must never silently turn into a native-speaker or team sign-off claim.
review_workflow <- manifest$review_workflow
internal_sq_review <- review_workflow$internal_ai_assisted$sq
human_sq_review <- review_workflow$independent_human$sq
allowed_internal_review_states <- c(
  "in_progress",
  "completed_with_open_findings",
  "completed_pending_human_decisions",
  "complete"
)

if (is.null(internal_sq_review) || is.null(human_sq_review)) {
  fail("The parity manifest must distinguish the internal Albanian audit from independent human review.")
} else {
  for (section_name in c("editorial_consistency", "subject_parity")) {
    status <- as.character(internal_sq_review[[section_name]]$status)
    if (!length(status) || !status %in% allowed_internal_review_states) {
      fail(sprintf(
        "Unknown internal Albanian %s review status: %s.",
        section_name,
        if (length(status)) status else "<missing>"
      ))
    }
  }
  if (!identical(as.character(internal_sq_review$method), "ai_assisted_internal")) {
    fail("The current internal Albanian audit must be identified as ai_assisted_internal.")
  }
  if (!identical(as.character(internal_sq_review$automated_checks$status), "passed")) {
    fail("The internal Albanian review record must retain its automated-check result.")
  }

  for (section_name in c("native_language", "statistics_subject", "team_final_signoff")) {
    section <- human_sq_review[[section_name]]
    status <- as.character(section$status)
    if (!length(status) || !status %in% c("pending", "complete")) {
      fail(sprintf(
        "Unknown independent Albanian %s review status: %s.",
        section_name,
        if (length(status)) status else "<missing>"
      ))
    }
    if (identical(status, "complete")) {
      reviewer <- trimws(as.character(section$reviewer))
      reviewed_on <- trimws(as.character(section$reviewed_on))
      if (!length(reviewer) || !nzchar(reviewer) ||
          !length(reviewed_on) || !nzchar(reviewed_on)) {
        fail(sprintf(
          "Completed independent Albanian %s review requires a real reviewer and date.",
          section_name
        ))
      }
    }
  }

  page_sq_review_states <- function(field_name) {
    states <- as.character(manifest$entry_defaults[[field_name]]$sq)
    for (page in manifest$pages) {
      if (!is.null(page[[field_name]]$sq)) {
        states <- c(states, as.character(page[[field_name]]$sq))
      }
    }
    unique(states)
  }
  human_status <- vapply(
    c("native_language", "statistics_subject", "team_final_signoff"),
    function(section_name) as.character(human_sq_review[[section_name]]$status),
    character(1)
  )
  completed_claims <- c("complete", "approved", "approved_for_platform")
  if (any(page_sq_review_states("translation_review") %in% completed_claims) &&
      !all(human_status[c("native_language", "team_final_signoff")] == "complete")) {
    fail("Albanian translation review cannot be marked complete before native-language and team sign-off are recorded.")
  }
  if (any(page_sq_review_states("terminology_review") %in% completed_claims) &&
      !all(human_status[c("native_language", "statistics_subject", "team_final_signoff")] == "complete")) {
    fail("Albanian terminology review cannot be marked complete before language, subject, and team sign-off are recorded.")
  }
}

# Static topic figures contain genuine mathematical hats, bars, subscripts,
# and superscripts. Keep every locale on the same Unicode-capable bitmap
# device so the generated PNG files cannot silently replace them with tofu
# squares even when an editor preview looked correct.
for (locale in locales) {
  metadata_path <- file.path(
    "ratiomera-statistics", locale, "intro-stats", "_metadata.yml"
  )
  if (!file.exists(metadata_path)) {
    fail(sprintf("Missing Introduction to Statistics metadata: %s.", metadata_path))
    next
  }
  topic_metadata <- tryCatch(
    yaml::read_yaml(metadata_path),
    error = function(error) {
      fail(sprintf("Invalid topic metadata %s: %s", metadata_path, conditionMessage(error)))
      NULL
    }
  )
  if (!is.null(topic_metadata) &&
      !identical(as.character(topic_metadata$knitr$opts_chunk$dev), "ragg_png")) {
    fail(sprintf(
      "Introduction to Statistics metadata must use dev: ragg_png in %s.",
      metadata_path
    ))
  }
}

counter_manifest <- manifest$usage_counters
counter_config_path <- as.character(counter_manifest$configuration)
counter_client_path <- as.character(counter_manifest$client)
counter_injector_path <- as.character(counter_manifest$footer_injector)
counter_config <- if (file.exists(counter_config_path)) {
  tryCatch(yaml::read_yaml(counter_config_path), error = function(error) {
    fail(sprintf("Invalid counter configuration %s: %s", counter_config_path, conditionMessage(error)))
    NULL
  })
} else {
  fail(sprintf("Missing counter configuration: %s", counter_config_path))
  NULL
}

if (!file.exists(counter_client_path)) fail(sprintf("Missing counter client: %s", counter_client_path))
if (!file.exists(counter_injector_path)) fail(sprintf("Missing counter footer injector: %s", counter_injector_path))

if (!is.null(counter_config)) {
  if (!identical(as.integer(counter_config$schema_version), 2L)) {
    fail("Counter configuration must use schema_version 2.")
  }
  if (!identical(as.character(counter_config$page_visits$provider), as.character(counter_manifest$page_provider))) {
    fail("Page-counter provider differs between config and parity manifest.")
  }
  if (!identical(as.character(counter_config$download_counts$provider), as.character(counter_manifest$download_provider))) {
    fail("Download-counter provider differs between config and parity manifest.")
  }
  for (section_name in c("page_visits", "download_counts")) {
    section <- counter_config[[section_name]]
    provider <- as.character(section$provider)
    if (!provider %in% names(section$providers)) {
      fail(sprintf("Unknown %s counter provider: %s.", section_name, provider))
    }
  }
  github_provider <- counter_config$download_counts$providers$github_releases
  if (is.null(github_provider$releases) || !length(github_provider$releases)) {
    fail("GitHub download configuration must define a release-key map.")
  }
  legacy_github_fields <- intersect(
    c("owner", "repository", "release", "release_tag"),
    names(github_provider)
  )
  if (length(legacy_github_fields)) {
    fail(paste(
      "GitHub download configuration must not use global release fields:",
      paste(legacy_github_fields, collapse = ", ")
    ))
  }
  if (identical(as.character(counter_config$download_counts$provider), "github_releases")) {
    for (release_key in names(github_provider$releases)) {
      settings <- github_provider$releases[[release_key]]
      required_settings <- c("owner", "repository", "release_tag")
      incomplete <- required_settings[vapply(required_settings, function(field) {
        is.null(settings[[field]]) || !nzchar(as.character(settings[[field]]))
      }, logical(1))]
      if (length(incomplete)) {
        fail(sprintf(
          "Enabled GitHub release key %s lacks: %s.",
          release_key, paste(incomplete, collapse = ", ")
        ))
      }
    }
  }
  expected_counter_labels <- list(
    en = c(visits = "Visits", downloads = "Downloads"),
    de = c(visits = "Besuche", downloads = "Downloads"),
    sq = c(visits = "Vizita", downloads = "Shkarkime")
  )
  for (locale in locales) {
    labels <- counter_config$locales[[locale]]
    required <- c("visits", "downloads", "loading", "unavailable")
    missing <- required[!required %in% names(labels)]
    if (length(missing)) {
      fail(sprintf("Counter configuration lacks %s labels: %s.", locale, paste(missing, collapse = ", ")))
    } else if (!identical(
      unlist(labels[c("visits", "downloads")], use.names = TRUE),
      expected_counter_labels[[locale]]
    )) {
      fail(sprintf("Counter display labels do not match the required %s wording.", locale))
    }
  }
  placeholder <- as.character(counter_config$placeholder)
  if (!nzchar(placeholder) || grepl("^[0-9]+$", placeholder)) {
    fail("The disabled counter placeholder must be nonnumeric.")
  }
}

if (!identical(as_character(manifest$locale_order), locales)) {
  fail("Manifest locale_order must be en, de, sq.")
}
if (!identical(as_character(terminology$locale_order), locales)) {
  fail("Terminology locale_order must be en, de, sq.")
}
if (!identical(as.character(manifest$canonical_locale), "en")) {
  fail("Manifest canonical_locale must be en.")
}

terms <- terminology$terms
if (!length(terms)) {
  fail("Terminology resource contains no terms.")
} else {
  allowed_reviews <- as_character(terminology$review_status_values)
  for (term_id in names(terms)) {
    term <- terms[[term_id]]
    missing_text <- locales[vapply(locales, function(locale) {
      is.null(term[[locale]]) || !nzchar(trimws(as.character(term[[locale]])))
    }, logical(1))]
    if (length(missing_text)) {
      fail(sprintf("Terminology %s has empty locale values: %s.", term_id, paste(missing_text, collapse = ", ")))
    }
    if (is.null(term$domain) || !nzchar(as.character(term$domain))) {
      fail(sprintf("Terminology %s has no domain.", term_id))
    }
    if (is.null(term$review_status) || !as.character(term$review_status) %in% allowed_reviews) {
      fail(sprintf("Terminology %s has an invalid review_status.", term_id))
    }
  }
}

read_front_matter <- function(path) {
  lines <- readLines(path, warn = FALSE, encoding = "UTF-8")
  if (!length(lines) || trimws(sub("^\ufeff", "", lines[[1]])) != "---") return(NULL)
  closing <- which(trimws(lines[-1]) %in% c("---", "..."))
  if (!length(closing)) return(NULL)
  end <- closing[[1]] + 1L
  text <- paste(lines[2L:(end - 1L)], collapse = "\n")
  tryCatch(yaml::yaml.load(text), error = function(error) {
    fail(sprintf("Invalid YAML front matter in %s: %s", path, conditionMessage(error)))
    NULL
  })
}

effective_language <- function(path, metadata) {
  if (!is.null(metadata$lang)) return(as.character(metadata$lang))
  directory <- dirname(path)
  repeat {
    candidate <- file.path(directory, "_metadata.yml")
    if (file.exists(candidate)) {
      inherited <- tryCatch(yaml::read_yaml(candidate), error = function(error) NULL)
      if (!is.null(inherited$lang)) return(as.character(inherited$lang))
    }
    if (directory %in% c(".", "")) break
    parent <- dirname(directory)
    if (identical(parent, directory)) break
    directory <- parent
  }
  "en"
}

strip_fenced_blocks <- function(lines) {
  inside <- FALSE
  keep <- logical(length(lines))
  for (i in seq_along(lines)) {
    if (grepl("^\\s*(```|~~~)", lines[[i]])) {
      inside <- !inside
      next
    }
    keep[[i]] <- !inside
  }
  lines[keep]
}

source_character_is_escaped <- function(characters, index) {
  backslashes <- 0L
  cursor <- index - 1L
  while (cursor >= 1L && identical(characters[[cursor]], "\\")) {
    backslashes <- backslashes + 1L
    cursor <- cursor - 1L
  }
  backslashes %% 2L == 1L
}

mask_inline_code_spans <- function(line) {
  characters <- strsplit(line, "", fixed = TRUE)[[1]]
  character_count <- length(characters)
  if (!character_count) return(line)

  cursor <- 1L
  while (cursor <= character_count) {
    if (!identical(characters[[cursor]], "`") ||
        source_character_is_escaped(characters, cursor)) {
      cursor <- cursor + 1L
      next
    }

    opening_end <- cursor
    while (opening_end <= character_count && identical(characters[[opening_end]], "`")) {
      opening_end <- opening_end + 1L
    }
    delimiter_length <- opening_end - cursor
    search_cursor <- opening_end
    closing_end <- NA_integer_

    while (search_cursor <= character_count) {
      if (!identical(characters[[search_cursor]], "`") ||
          source_character_is_escaped(characters, search_cursor)) {
        search_cursor <- search_cursor + 1L
        next
      }
      candidate_end <- search_cursor
      while (candidate_end <= character_count && identical(characters[[candidate_end]], "`")) {
        candidate_end <- candidate_end + 1L
      }
      if (candidate_end - search_cursor == delimiter_length) {
        closing_end <- candidate_end
        break
      }
      search_cursor <- candidate_end
    }

    if (is.na(closing_end)) {
      cursor <- opening_end
      next
    }
    characters[cursor:(closing_end - 1L)] <- " "
    cursor <- closing_end
  }

  paste(characters, collapse = "")
}

strip_tex_text_arguments <- function(text) {
  text_command <- paste0(
    "\\\\(?:text|textrm|textnormal|textup|textsf|texttt|mbox|operatorname|",
    "mathrm|mathbf|mathit|mathsf|mathtt)\\*?[[:space:]]*\\{[^{}]*\\}"
  )
  previous <- NULL
  while (!identical(previous, text)) {
    previous <- text
    text <- gsub(text_command, " ", text, perl = TRUE)
  }
  text <- gsub("\\\\[[:alpha:]]+\\*?", " ", text, perl = TRUE)
  gsub("\\\\.", " ", text, perl = TRUE)
}

inline_math_span_contains_prose <- function(text) {
  without_tex_text <- strip_tex_text_arguments(text)
  words <- regmatches(
    without_tex_text,
    gregexpr("\\p{L}{2,}", without_tex_text, perl = TRUE)
  )[[1]]
  word_count <- length(words)
  letter_count <- nchar(gsub("[^\\p{L}]", "", without_tex_text, perl = TRUE), type = "chars")
  sentence_like <- grepl("[.!?][[:space:]]+\\p{L}", without_tex_text, perl = TRUE)
  markdown_like <- grepl(
    "(^|[[:space:]])#{1,6}[[:space:]]|\\*\\*|__|:{3,}|\\[[^]]+\\]\\(",
    without_tex_text,
    perl = TRUE
  )

  (word_count >= 5L && letter_count >= 12L) ||
    (word_count >= 3L && sentence_like) ||
    (word_count >= 2L && markdown_like)
}

source_line_preview <- function(line, maximum_length = 140L) {
  preview <- trimws(gsub("[[:space:]]+", " ", line))
  if (nchar(preview, type = "chars") <= maximum_length) return(preview)
  paste0(substr(preview, 1L, maximum_length - 3L), "...")
}

check_topic_inline_math <- function(path) {
  lines <- readLines(path, warn = FALSE, encoding = "UTF-8")
  if (!length(lines)) return(invisible(NULL))

  front_matter_end <- 0L
  if (identical(trimws(sub("^\ufeff", "", lines[[1]])), "---")) {
    closing <- which(trimws(lines[-1L]) %in% c("---", "..."))
    if (length(closing)) front_matter_end <- closing[[1]] + 1L
  }

  fence_character <- NULL
  fence_length <- 0L
  inside_display_math <- FALSE

  for (line_number in seq_along(lines)) {
    if (line_number <= front_matter_end) next
    line <- lines[[line_number]]
    left_trimmed <- sub("^[[:space:]]+", "", line)

    if (is.null(fence_character)) {
      fence_match <- regexpr("^(`{3,}|~{3,})", left_trimmed, perl = TRUE)
      if (fence_match[[1]] == 1L) {
        fence <- regmatches(left_trimmed, fence_match)
        fence_character <- substr(fence, 1L, 1L)
        fence_length <- nchar(fence, type = "chars")
        next
      }
    } else {
      closing_pattern <- sprintf(
        "^%s{%d,}[[:space:]]*$", fence_character, fence_length
      )
      if (grepl(closing_pattern, left_trimmed, perl = TRUE)) {
        fence_character <- NULL
        fence_length <- 0L
      }
      next
    }

    masked_line <- mask_inline_code_spans(line)
    characters <- strsplit(masked_line, "", fixed = TRUE)[[1]]
    character_count <- length(characters)
    inline_delimiters <- integer()
    cursor <- 1L

    while (cursor <= character_count) {
      if (!identical(characters[[cursor]], "$")) {
        cursor <- cursor + 1L
        next
      }
      if (source_character_is_escaped(characters, cursor)) {
        cursor <- cursor + 1L
        next
      }
      if (cursor < character_count && identical(characters[[cursor + 1L]], "$")) {
        inside_display_math <- !inside_display_math
        cursor <- cursor + 2L
        next
      }
      if (!inside_display_math) inline_delimiters <- c(inline_delimiters, cursor)
      cursor <- cursor + 1L
    }

    if (length(inline_delimiters) %% 2L == 1L) {
      fail(sprintf(
        paste0(
          "Malformed inline math delimiters in %s:%d: found %d unescaped single-dollar ",
          "delimiter(s) outside code and display math at column(s) %s. Source: %s"
        ),
        path,
        line_number,
        length(inline_delimiters),
        paste(inline_delimiters, collapse = ", "),
        source_line_preview(line)
      ))
    }

    complete_pair_count <- length(inline_delimiters) %/% 2L
    if (!complete_pair_count) next
    for (pair_index in seq_len(complete_pair_count)) {
      opening_column <- inline_delimiters[[2L * pair_index - 1L]]
      closing_column <- inline_delimiters[[2L * pair_index]]
      span <- substr(masked_line, opening_column + 1L, closing_column - 1L)
      if (inline_math_span_contains_prose(span)) {
        fail(sprintf(
          paste0(
            "Suspicious inline math span in %s:%d at columns %d-%d: the paired ",
            "single-dollar delimiters appear to enclose prose. Source: %s"
          ),
          path,
          line_number,
          opening_column,
          closing_column,
          source_line_preview(line)
        ))
      }
    }
  }

  invisible(NULL)
}

extract_panel_tabs <- function(path) {
  lines <- readLines(path, warn = FALSE, encoding = "UTF-8")
  panels <- list()
  panel_depth <- 0L
  active_panel <- 0L
  inside_code <- FALSE

  for (line in lines) {
    if (grepl("^\\s*(```|~~~)", line)) {
      inside_code <- !inside_code
      next
    }
    if (inside_code) next

    panel_open <- grepl(
      "^\\s*:{3,}\\s*\\{[^}]*\\.panel-tabset(?:[[:space:]}]|$)",
      line,
      perl = TRUE
    )
    container_open <- grepl("^\\s*:{3,}\\s*\\{", line, perl = TRUE)
    container_close <- grepl("^\\s*:{3,}\\s*$", line, perl = TRUE)

    if (panel_depth == 0L) {
      if (panel_open) {
        panels[[length(panels) + 1L]] <- character()
        active_panel <- length(panels)
        panel_depth <- 1L
      }
      next
    }

    if (container_open) {
      panel_depth <- panel_depth + 1L
      next
    }
    if (container_close) {
      panel_depth <- panel_depth - 1L
      if (panel_depth == 0L) active_panel <- 0L
      next
    }
    if (panel_depth == 1L && grepl("^\\s*##\\s+", line, perl = TRUE)) {
      label <- sub("^\\s*##\\s+", "", line, perl = TRUE)
      label <- sub("\\s+\\{[^}]*\\}\\s*$", "", label, perl = TRUE)
      panels[[active_panel]] <- c(panels[[active_panel]], trimws(label))
    }
  }

  panels
}

structural_signature <- function(path) {
  lines <- readLines(path, warn = FALSE, encoding = "UTF-8")
  prose <- strip_fenced_blocks(lines)
  heading_lines <- grep("^#{1,6}\\s+", prose, value = TRUE)
  heading_levels <- nchar(sub("^(#{1,6}).*$", "\\1", heading_lines))
  text <- paste(lines, collapse = "\n")
  explicit_heading_ids <- regmatches(text, gregexpr("\\{#[A-Za-z][A-Za-z0-9_.:-]*", text, perl = TRUE))[[1]]
  explicit_heading_ids <- sub("^\\{#", "", explicit_heading_ids)
  html_ids <- regmatches(text, gregexpr("\\bid=[\"'][A-Za-z][A-Za-z0-9_.:-]*[\"']", text, perl = TRUE))[[1]]
  html_ids <- sub("^id=[\"']", "", html_ids)
  html_ids <- sub("[\"']$", "", html_ids)
  chunk_labels <- trimws(sub("^\\s*#\\|\\s*label:\\s*", "", grep("^\\s*#\\|\\s*label:\\s*", lines, value = TRUE)))
  container_lines <- grep("^:{3,}.*\\{", prose, value = TRUE)
  container_classes <- unlist(regmatches(container_lines, gregexpr("\\.[A-Za-z][A-Za-z0-9_-]*", container_lines, perl = TRUE)), use.names = FALSE)
  list(
    heading_levels = heading_levels,
    explicit_ids = sort(unique(c(explicit_heading_ids, html_ids))),
    chunk_labels = sort(unique(chunk_labels)),
    container_classes = sort(container_classes)
  )
}

same_vector <- function(left, right) identical(as.character(left), as.character(right))

extract_links <- function(path) {
  lines <- strip_fenced_blocks(readLines(path, warn = FALSE, encoding = "UTF-8"))
  text <- paste(lines, collapse = "\n")
  markdown_matches <- regmatches(text, gregexpr("\\[[^]]*\\]\\(([^)]+)\\)", text, perl = TRUE))[[1]]
  markdown_links <- sub("^.*\\]\\(([^)]+)\\)$", "\\1", markdown_matches, perl = TRUE)
  html_matches <- regmatches(text, gregexpr("\\bhref=[\"'][^\"']+[\"']", text, perl = TRUE))[[1]]
  html_links <- sub("^href=[\"']", "", html_matches)
  html_links <- sub("[\"']$", "", html_links)
  unique(c(markdown_links, html_links))
}

resolve_link <- function(source, target) {
  target <- trimws(target)
  target <- sub("\\s+[\"'][^\"']*[\"']$", "", target)
  if (!nzchar(target) || startsWith(target, "#") || grepl("^(https?:|mailto:|tel:|javascript:|data:)", target, ignore.case = TRUE)) return(NULL)
  if (grepl("\\{\\{|`r|^<", target)) return(NULL)
  target <- sub("[?#].*$", "", target)
  if (!nzchar(target)) return(NULL)
  target <- utils::URLdecode(target)
  relative <- if (startsWith(target, "/")) sub("^/+", "", target) else file.path(dirname(source), target)
  relative <- gsub("\\\\", "/", relative)
  if (grepl("\\.html$", relative, ignore.case = TRUE)) relative <- sub("\\.html$", ".qmd", relative, ignore.case = TRUE)
  relative
}

check_links <- function(path) {
  for (target in extract_links(path)) {
    resolved <- resolve_link(path, target)
    if (is.null(resolved)) next
    if (!grepl("\\.(qmd|md|csv|tsv|json|ya?ml|png|jpe?g|gif|svg|webp|pdf|docx?|xlsx?|zip|rds)$", resolved, ignore.case = TRUE)) next
    if (!file.exists(resolved)) fail(sprintf("Broken internal link in %s: %s", path, target))
  }
}

pages <- manifest$pages
if (!length(pages)) stop("Manifest contains no page entries.", call. = FALSE)

expected_lesson_tabs <- list(
  en = c("Theory", "Simulated Example", "Exercises and Solutions", "Summary"),
  de = c("Theorie", "Simuliertes Beispiel", "Übungen und Lösungen", "Zusammenfassung"),
  sq = c("Teoria", "Shembull i simuluar", "Ushtrime dhe zgjidhje", "Përmbledhje")
)

expected_topic_endings <- list(
  en = c("Potential Pitfalls", "How This Example Brings the Theory Together"),
  de = c("Mögliche Stolperfallen", "Wie dieses Beispiel die Theorie zusammenführt"),
  sq = c("Gabime të mundshme", "Si i bashkon ky shembull idetë e teorisë")
)

page_ids <- vapply(pages, function(page) as.character(page$id), character(1))
if (anyDuplicated(page_ids)) fail(paste("Duplicate manifest page IDs:", paste(unique(page_ids[duplicated(page_ids)]), collapse = ", ")))

if (!is.null(counter_config)) {
  included_page_types <- as_character(counter_config$page_visits$included_page_types)
  canonical_counter_pages <- pages[vapply(pages, function(page) {
    as.character(page$page_type) %in% included_page_types
  }, logical(1))]
  if (any(vapply(canonical_counter_pages, function(page) {
    identical(as.character(page$page_type), "compatibility_redirect")
  }, logical(1)))) {
    fail("Compatibility redirects must not receive page-visit counters.")
  }
  expected_counter_routes <- length(canonical_counter_pages) * length(locales)
  if (!identical(expected_counter_routes, as.integer(counter_manifest$canonical_route_count))) {
    fail(sprintf(
      "Counter manifest expects %s canonical routes but the page inventory defines %s.",
      counter_manifest$canonical_route_count, expected_counter_routes
    ))
  }
  page_counter_ids <- unlist(lapply(canonical_counter_pages, function(page) {
    vapply(locales, function(locale) {
      render_identifier(
        counter_config$page_visits$id_template,
        list(page_id = as.character(page$id), locale = locale)
      )
    }, character(1))
  }), use.names = FALSE)
  if (anyNA(page_counter_ids) || anyDuplicated(page_counter_ids)) {
    fail("Page-counter IDs must resolve and remain unique across canonical routes and locales.")
  }
}

all_paths <- character()
manifest_en_paths <- character()
download_ids_from_manifest <- character()
topic_page_contexts <- list()

for (page in pages) {
  page_id <- as.character(page$id)
  lesson_page <- identical(as.character(page$page_type), "lesson")
  if (is.null(page$paths) || !all(locales %in% names(page$paths))) {
    fail(sprintf("Manifest page %s does not define en, de, and sq paths.", page_id))
    next
  }
  paths <- vapply(locales, function(locale) as.character(page$paths[[locale]]), character(1))
  names(paths) <- locales
  all_paths <- c(all_paths, paths)
  manifest_en_paths <- c(manifest_en_paths, paths[["en"]])
  download_ids_from_manifest <- c(download_ids_from_manifest, as_character(page$downloads))

  if (is.null(page$content_status) || !all(locales %in% names(page$content_status))) {
    fail(sprintf("Manifest page %s lacks locale-specific content_status values.", page_id))
  }
  translation_review <- if (is.null(page$translation_review)) manifest$entry_defaults$translation_review else page$translation_review
  terminology_review <- if (is.null(page$terminology_review)) manifest$entry_defaults$terminology_review else page$terminology_review
  if (is.null(translation_review) || !all(locales %in% names(translation_review))) {
    fail(sprintf("Manifest page %s lacks locale-specific translation_review values or defaults.", page_id))
  }
  if (is.null(terminology_review) || !all(locales %in% names(terminology_review))) {
    fail(sprintf("Manifest page %s lacks locale-specific terminology_review values or defaults.", page_id))
  }

  metadata_by_locale <- list()
  signatures <- list()
  for (locale in locales) {
    path <- paths[[locale]]
    if (!file.exists(path)) {
      fail(sprintf("Missing %s route for %s: %s", locale, page_id, path))
      next
    }
    metadata <- read_front_matter(path)
    metadata_by_locale[[locale]] <- metadata
    if (is.null(metadata)) {
      fail(sprintf("Missing front matter in %s.", path))
    } else {
      for (field in c("pagetitle", "description", "title-prefix")) {
        if (!field %in% names(metadata)) fail(sprintf("Missing metadata field %s in %s.", field, path))
      }
      lang <- effective_language(path, metadata)
      expected <- locale_tags[[locale]]
      if (!identical(lang, expected)) fail(sprintf("Language metadata mismatch in %s: expected %s, found %s.", path, expected, lang))
    }
    check_links(path)
    if (grepl("\u2014", paste(readLines(path, warn = FALSE, encoding = "UTF-8"), collapse = "\n"), fixed = TRUE)) {
      fail(sprintf("Em dash found in user-facing source: %s", path))
    }
    if (lesson_page) {
      check_topic_inline_math(path)
      panels <- extract_panel_tabs(path)
      if (length(panels) != 1L) {
        fail(sprintf(
          "Lesson %s must contain exactly one .panel-tabset; found %d in %s.",
          page_id, length(panels), path
        ))
      } else if (!identical(as.character(panels[[1]]), expected_lesson_tabs[[locale]])) {
        fail(sprintf(
          "Lesson tabs in %s must be exactly: %s. Found: %s.",
          path,
          paste(expected_lesson_tabs[[locale]], collapse = " | "),
          paste(panels[[1]], collapse = " | ")
        ))
      }

      topic_lines <- readLines(path, warn = FALSE, encoding = "UTF-8")
      datatable_calls <- grep("^[[:space:]]*(DT::)?datatable\\(", topic_lines, perl = TRUE)
      if (length(datatable_calls)) {
        helper_sources <- grep(
          "source\\(\"\\.\\./\\.\\./_shared/topic-table-options\\.R\"",
          topic_lines,
          perl = TRUE
        )
        localized_options <- grep(
          "^[[:space:]]*options[[:space:]]*=[[:space:]]*topic_dt_options\\(topic_locale\\)",
          topic_lines,
          perl = TRUE
        )
        if (length(helper_sources) != 1L) {
          fail(sprintf("Lesson %s must source the shared DataTables locale helper exactly once: %s", page_id, path))
        }
        if (length(localized_options) != length(datatable_calls)) {
          fail(sprintf(
            "Lesson %s has %d DataTables but %d centralized localized option calls: %s",
            page_id, length(datatable_calls), length(localized_options), path
          ))
        }
      }

      theory_heading <- paste0("## ", expected_lesson_tabs[[locale]][[1]])
      simulated_heading <- paste0("## ", expected_lesson_tabs[[locale]][[2]])
      exercise_heading <- paste0("## ", expected_lesson_tabs[[locale]][[3]])
      theory_start <- which(trimws(topic_lines) == theory_heading)
      simulated_start <- which(trimws(topic_lines) == simulated_heading)
      simulated_end <- which(trimws(topic_lines) == exercise_heading)
      if (length(theory_start) == 1L && length(simulated_start) == 1L && theory_start < simulated_start) {
        theory_lines <- topic_lines[(theory_start + 1L):(simulated_start - 1L)]
        interactive_theory_calls <- grep(
          "^[[:space:]]*(topic([0-9]+)?_plotly|topic1_stress_pie_plotly|t04_plotly|accessible_plotly|ggplotly|plot_ly)\\(",
          theory_lines,
          perl = TRUE
        )
        if (length(interactive_theory_calls)) {
          fail(sprintf(
            "Lesson %s must render Theory figures statically; found %d interactive figure calls in %s.",
            page_id, length(interactive_theory_calls), path
          ))
        }
      }
      if (length(simulated_start) == 1L && length(simulated_end) == 1L && simulated_start < simulated_end) {
        simulated_lines <- topic_lines[(simulated_start + 1L):(simulated_end - 1L)]
        simulated_figures <- grep("^[[:space:]]*#\\|[[:space:]]*label:[[:space:]]*fig-", simulated_lines, perl = TRUE)
        interactive_figures <- grep(
          "^[[:space:]]*(topic([0-9]+)?_plotly|t04_plotly|accessible_plotly)\\(",
          simulated_lines,
          perl = TRUE
        )
        if (length(simulated_figures) != length(interactive_figures)) {
          fail(sprintf(
            "Lesson %s must render every Simulated Example figure interactively; found %d figure labels and %d shared Plotly calls in %s.",
            page_id, length(simulated_figures), length(interactive_figures), path
          ))
        }
        for (ending in expected_topic_endings[[locale]]) {
          expected_heading <- paste0("### ", ending, " {.cs-heading}")
          if (sum(trimws(simulated_lines) == expected_heading) != 1L) {
            fail(sprintf("Lesson %s lacks the canonical Simulated Example ending '%s' in %s.", page_id, ending, path))
          }
        }
      }

      expected_warning <- paste0(
        "::: {.callout-warning title=\"",
        expected_topic_endings[[locale]][[1]],
        "\"}"
      )
      if (sum(trimws(topic_lines) == expected_warning) != 1L) {
        fail(sprintf("Lesson %s must contain exactly one canonical Theory warning callout in %s.", page_id, path))
      }
    }
    signatures[[locale]] <- structural_signature(path)
  }

  if (!is.null(page$topic)) {
    topic_number <- as.integer(page$topic)
    topic_page_contexts[[length(topic_page_contexts) + 1L]] <- list(
      page_id = page_id,
      topic_number = topic_number,
      paths = paths,
      declared_downloads = as_character(page$downloads)
    )
  }

  if (identical(as.character(page$parity_mode), "full") && all(locales %in% names(signatures))) {
    reference <- signatures$en
    for (locale in c("de", "sq")) {
      candidate <- signatures[[locale]]
      if (!same_vector(reference$heading_levels, candidate$heading_levels)) {
        fail(sprintf("Heading-level sequence differs for %s between en and %s.", page_id, locale))
      }
      if (!same_vector(reference$explicit_ids, candidate$explicit_ids)) {
        fail(sprintf("Explicit structural IDs differ for %s between en and %s.", page_id, locale))
      }
      if (!same_vector(reference$chunk_labels, candidate$chunk_labels)) {
        fail(sprintf("Chunk labels differ for %s between en and %s.", page_id, locale))
      }
      if (!same_vector(reference$container_classes, candidate$container_classes)) {
        fail(sprintf("Container class sequence differs for %s between en and %s.", page_id, locale))
      }
    }
  }

  figure_ids <- as_character(page$figures)
  if (length(figure_ids)) {
    for (locale in locales) {
      path <- paths[[locale]]
      if (!file.exists(path)) next
      contents <- paste(readLines(path, warn = FALSE, encoding = "UTF-8"), collapse = "\n")
      missing_figures <- figure_ids[!vapply(figure_ids, function(id) grepl(paste0("label:\\s*", id, "\\b"), contents, perl = TRUE), logical(1))]
      if (length(missing_figures)) fail(sprintf("Missing figure identifiers in %s: %s", path, paste(missing_figures, collapse = ", ")))
    }
  }

  for (asset in as_character(page$assets)) {
    if (!file.exists(asset)) fail(sprintf("Missing manifest asset for %s: %s", page_id, asset))
  }
}

if (anyDuplicated(all_paths)) {
  duplicates <- unique(all_paths[duplicated(all_paths)])
  fail(paste("Duplicate locale paths in manifest:", paste(duplicates, collapse = ", ")))
}

excluded <- vapply(manifest$language_independent_or_compatibility_sources, function(item) as.character(item$path), character(1))
canonical_sources <- list.files(".", pattern = "\\.qmd$", recursive = TRUE, full.names = FALSE)
canonical_sources <- canonical_sources[grepl("^(en|ratiomera-statistics/en|ratiomera-mathematics/en)/", canonical_sources)]
unrepresented <- setdiff(canonical_sources, c(manifest_en_paths, excluded))
if (length(unrepresented)) fail(paste("English QMD sources missing from manifest:", paste(unrepresented, collapse = ", ")))
stale_manifest <- setdiff(manifest_en_paths, canonical_sources)
if (length(stale_manifest)) fail(paste("Manifest English paths are not canonical English sources:", paste(stale_manifest, collapse = ", ")))

download_metadata_paths <- unique(unlist(lapply(pages, function(page) {
  assets <- as_character(page$assets)
  assets[grepl("downloads\\.ya?ml$", assets)]
}), use.names = FALSE))
available_download_ids <- character()
registered_material_ids <- character()
material_counter_ids <- character()
download_status_by_id <- character()
for (metadata_path in download_metadata_paths) {
  if (!file.exists(metadata_path)) next
  metadata <- tryCatch(yaml::read_yaml(metadata_path), error = function(error) {
    fail(sprintf("Invalid download metadata %s: %s", metadata_path, conditionMessage(error)))
    NULL
  })
  if (is.null(metadata)) next
  if (!identical(as.integer(metadata$schema_version), 4L)) {
    fail(sprintf("Download metadata %s must use schema_version 4.", metadata_path))
    next
  }
  if (!identical(as_character(metadata$locale_order), locales)) {
    fail(sprintf("Download metadata %s must use locale_order en, de, sq.", metadata_path))
  }
  required_labels <- c(
    "collection_label", "topic_label", "material_column", "download_column", "unavailable_text",
    "download_action_template", "download_aria_template", "caption_template",
    "collection_caption_template", "bundle_label", "bundle_heading", "bundle_description",
    "format_choice_text", "topic_package_label", "topic_package_description",
    "topic_packages_heading", "topic_packages_description", "individual_files_summary",
    "complete_package_label", "complete_package_heading", "complete_package_description",
    "secondary_bundles_summary", "secondary_bundles_description"
  )
  for (locale in locales) {
    locale_labels <- metadata$locales[[locale]]
    missing_labels <- required_labels[!required_labels %in% names(locale_labels)]
    if (length(missing_labels)) {
      fail(sprintf("Download metadata %s lacks %s labels: %s", metadata_path, locale, paste(missing_labels, collapse = ", ")))
    }
  }

  expected_categories <- c("summary", "exercises", "solutions")
  if (!identical(names(metadata$categories), expected_categories)) {
    fail(sprintf("Download metadata %s must define summary, exercises, and solutions in canonical order.", metadata_path))
  }
  for (category_id in names(metadata$categories)) {
    category <- metadata$categories[[category_id]]
    missing_locales <- locales[!locales %in% names(category)]
    if (length(missing_locales)) {
      fail(sprintf("Download category %s lacks labels for: %s", category_id, paste(missing_locales, collapse = ", ")))
    }
  }

  if (length(metadata$courses) != 1L ||
      !identical(as.character(metadata$courses[[1]]$id), "intro-statistics")) {
    fail(sprintf("Download metadata %s must define the intro-statistics collection exactly once.", metadata_path))
    next
  }
  collection <- metadata$courses[[1]]
  release_key <- if (is.null(collection$release_key)) "" else as.character(collection$release_key)
  if (!grepl("^[a-z][a-z0-9-]*$", release_key)) {
    fail(sprintf("Download collection %s must define a stable release_key.", collection$id))
  }
  github_releases <- if (!is.null(counter_config)) {
    counter_config$download_counts$providers$github_releases$releases
  } else {
    NULL
  }
  if (!nzchar(release_key) || is.null(github_releases[[release_key]])) {
    fail(sprintf("Download collection %s has no matching GitHub release-key configuration.", collection$id))
  }
  for (field in c("title", "description")) {
    missing_locales <- locales[!locales %in% names(collection[[field]])]
    if (length(missing_locales)) {
      fail(sprintf("Download collection %s lacks %s for: %s", collection$id, field, paste(missing_locales, collapse = ", ")))
    }
  }
  topics <- collection$topics
  topic_ids <- vapply(topics, function(topic) as.character(topic$id), character(1))
  if (anyDuplicated(topic_ids)) fail(sprintf("Duplicate topic IDs in %s.", metadata_path))
  expected_topic_numbers <- seq_len(8L)
  topic_numbers <- vapply(topics, function(topic) {
    if (is.null(topic$number)) NA_integer_ else suppressWarnings(as.integer(topic$number))
  }, integer(1))
  expected_topic_ids <- paste0("dl-topic-", expected_topic_numbers)
  if (!identical(topic_numbers, expected_topic_numbers) ||
      !identical(topic_ids, expected_topic_ids)) {
    fail(sprintf(
      "Download metadata %s must define dl-topic-1 through dl-topic-8 in canonical numeric order.",
      metadata_path
    ))
  }
  material_ids <- character()
  for (topic in topics) {
    missing_title_locales <- locales[!locales %in% names(topic$title)]
    if (length(missing_title_locales)) {
      fail(sprintf("Download topic %s lacks titles for: %s", topic$id, paste(missing_title_locales, collapse = ", ")))
    }
    topic_categories <- vapply(topic$materials, function(material) as.character(material$category), character(1))
    if (!identical(topic_categories, expected_categories)) {
      fail(sprintf("Download topic %s must contain summary, exercises, and solutions in canonical order.", topic$id))
    }
    topic_number <- suppressWarnings(as.integer(topic$number))
    package <- topic$package
    expected_package_id <- if (length(topic_number) == 1L && !is.na(topic_number)) {
      sprintf("intro-statistics-topic-%02d-package", topic_number)
    } else {
      ""
    }
    required_package_fields <- c("id", "status", "includes", "files")
    missing_package_fields <- if (is.null(package)) {
      required_package_fields
    } else {
      required_package_fields[!required_package_fields %in% names(package)]
    }
    if (length(missing_package_fields)) {
      fail(sprintf(
        "Download topic %s package lacks fields: %s.",
        topic$id, paste(missing_package_fields, collapse = ", ")
      ))
    } else {
      package_id <- as.character(package$id)
      material_ids <- c(material_ids, package_id)
      registered_material_ids <- c(registered_material_ids, package_id)
      download_status_by_id[[package_id]] <- as.character(package$status)
      if (!identical(package_id, expected_package_id)) {
        fail(sprintf("Download topic %s must use package ID %s.", topic$id, expected_package_id))
      }
      if (!identical(as_character(package$includes), expected_categories)) {
        fail(sprintf("Download topic package %s must include the three canonical categories.", package_id))
      }
      if (!identical(as.character(package$status), "available")) {
        fail(sprintf("Download topic package %s must be available when its ZIP is registered.", package_id))
      } else {
        available_download_ids <- c(available_download_ids, package_id)
      }
      package_formats <- toupper(vapply(package$files, function(file) {
        if (is.null(file$format)) "" else as.character(file$format)
      }, character(1)))
      if (!identical(package_formats, "ZIP")) {
        fail(sprintf("Download topic package %s must define exactly one ZIP file.", package_id))
      }
      for (file_record in package$files) {
        if (!all(locales %in% names(file_record$paths))) {
          fail(sprintf("Download topic package %s must define en, de, and sq paths.", package_id))
          next
        }
        for (locale in locales) {
          resource_path <- as.character(file_record$paths[[locale]])
          normalized_path <- gsub("\\\\", "/", resource_path)
          expected_directory <- sprintf("ratiomera-statistics/%s/downloads/files/", locale)
          expected_suffix <- sprintf("-%s\\.zip$", locale)
          if (!startsWith(normalized_path, expected_directory) ||
              !grepl(expected_suffix, basename(normalized_path), perl = TRUE)) {
            fail(sprintf("Download topic package %s has a noncanonical %s path: %s", package_id, locale, resource_path))
          }
          if (!file.exists(resource_path)) {
            fail(sprintf("Missing %s ZIP file for %s: %s", locale, package_id, resource_path))
          } else if (!has_zip_magic(resource_path)) {
            fail(sprintf("Download topic package %s is not a readable ZIP asset for %s: %s", package_id, locale, resource_path))
          }
        }
      }
      if (!is.null(counter_config)) {
        material_counter_ids <- c(
          material_counter_ids,
          vapply(locales, function(locale) {
            render_identifier(
              counter_config$download_counts$id_template,
              list(material_id = package_id, locale = locale)
            )
          }, character(1))
        )
      }
    }
    expected_material_ids <- if (length(topic_number) == 1L && !is.na(topic_number)) {
      sprintf(
        "t%02d-%s",
        topic_number,
        gsub("_", "-", expected_categories, fixed = TRUE)
      )
    } else {
      character()
    }
    topic_material_ids <- vapply(
      topic$materials,
      function(material) if (is.null(material$id)) "" else as.character(material$id),
      character(1)
    )
    if (length(expected_material_ids) && !identical(topic_material_ids, expected_material_ids)) {
      fail(sprintf(
        "Download topic %s must use canonical material IDs in category order: %s.",
        topic$id, paste(expected_material_ids, collapse = ", ")
      ))
    }
    practice_positions <- match(c("exercises", "solutions"), topic_categories)
    if (!anyNA(practice_positions)) {
      practice_materials <- topic$materials[practice_positions]
      practice_statuses <- vapply(
        practice_materials,
        function(material) as.character(material$status),
        character(1)
      )
      if (any(practice_statuses == "available") &&
          !all(practice_statuses == "available")) {
        fail(sprintf(
          "Download topic %s must publish exercises and solutions as a pair.",
          topic$id
        ))
      }
    }
    for (material in topic$materials) {
      required_material_fields <- c("id", "category", "status")
      missing_material_fields <- required_material_fields[!required_material_fields %in% names(material)]
      if (length(missing_material_fields)) {
        fail(sprintf("Download material in topic %s lacks fields: %s", topic$id, paste(missing_material_fields, collapse = ", ")))
        next
      }
      material_id <- as.character(material$id)
      material_ids <- c(material_ids, material_id)
      registered_material_ids <- c(registered_material_ids, material_id)
      if (!grepl("^[a-z][a-z0-9-]*$", material_id)) {
        fail(sprintf("Download material ID is not a stable lowercase identifier: %s.", material_id))
      }
      status <- as.character(material$status)
      if (!status %in% c("available", "unavailable")) {
        fail(sprintf("Download material %s has invalid status %s.", material_id, status))
        next
      }
      download_status_by_id[[material_id]] <- status
      if (identical(status, "available")) {
        if (is.null(material$files) || !length(material$files)) {
          fail(sprintf("Available download %s must define at least one file.", material_id))
          next
        }
        available_download_ids <- c(available_download_ids, material_id)
        formats <- toupper(vapply(material$files, function(file) {
          if (is.null(file$format)) "" else as.character(file$format)
        }, character(1)))
        expected_formats <- c("PDF", "DOCX")
        if (!identical(formats, expected_formats)) {
          fail(sprintf(
            "Download material %s must define formats in this order: %s.",
            material_id, paste(expected_formats, collapse = ", ")
          ))
        }
        for (file_record in material$files) {
          format <- toupper(as.character(file_record$format))
          if (!all(locales %in% names(file_record$paths))) {
            fail(sprintf("Download file for %s must define en, de, and sq paths.", material_id))
            next
          }
          for (locale in locales) {
            resource_path <- as.character(file_record$paths[[locale]])
            normalized_path <- gsub("\\\\", "/", resource_path)
            expected_directory <- sprintf("ratiomera-statistics/%s/downloads/files/", locale)
            expected_suffix <- sprintf("-%s\\.%s$", locale, tolower(format))
            if (!startsWith(normalized_path, expected_directory) ||
                !grepl(expected_suffix, basename(normalized_path), perl = TRUE)) {
              fail(sprintf("Download %s has a noncanonical %s path: %s", material_id, locale, resource_path))
            }
            if (grepl("\\.svg$", resource_path, ignore.case = TRUE)) {
              fail(sprintf("Download material %s must not use an SVG file: %s", material_id, resource_path))
            }
            if (!file.exists(resource_path)) {
              fail(sprintf("Missing %s %s file for %s: %s", locale, format, material_id, resource_path))
            } else if (identical(format, "PDF") && !has_pdf_magic(resource_path)) {
              fail(sprintf("Download %s is not a readable PDF asset for %s: %s", material_id, locale, resource_path))
            }
          }
        }
      } else if (!is.null(material$files) && length(material$files)) {
        fail(sprintf("Unavailable download %s must not define files.", material_id))
      }
    }
  }
  bundles <- collection$bundles
  expected_bundle_ids <- c(
    "intro-statistics-all-summaries",
    "intro-statistics-all-exercises",
    "intro-statistics-all-solutions",
    "intro-statistics-all-materials"
  )
  bundle_ids <- vapply(bundles, function(bundle) {
    if (is.null(bundle$id)) "" else as.character(bundle$id)
  }, character(1))
  if (!identical(bundle_ids, expected_bundle_ids)) {
    fail(sprintf(
      "Download metadata %s must define the four canonical ZIP bundle IDs in order.",
      metadata_path
    ))
  }
  primary_flags <- vapply(
    bundles,
    function(bundle) identical(bundle$primary, TRUE),
    logical(1)
  )
  if (!identical(which(primary_flags), 4L)) {
    fail(sprintf(
      "Download metadata %s must mark only intro-statistics-all-materials as the primary bundle.",
      metadata_path
    ))
  }
  expected_bundle_categories <- list(
    c("summary"), c("exercises"), c("solutions"), expected_categories
  )
  for (bundle_index in seq_along(bundles)) {
    bundle <- bundles[[bundle_index]]
    required_bundle_fields <- c("id", "primary", "title", "description", "includes", "status", "files")
    missing_bundle_fields <- required_bundle_fields[!required_bundle_fields %in% names(bundle)]
    if (length(missing_bundle_fields)) {
      fail(sprintf(
        "Download bundle %s lacks fields: %s.",
        if (is.null(bundle$id)) bundle_index else as.character(bundle$id),
        paste(missing_bundle_fields, collapse = ", ")
      ))
      next
    }
    material_id <- as.character(bundle$id)
    material_ids <- c(material_ids, material_id)
    registered_material_ids <- c(registered_material_ids, material_id)
    for (field in c("title", "description")) {
      missing_locales <- locales[!locales %in% names(bundle[[field]])]
      if (length(missing_locales)) {
        fail(sprintf("Download bundle %s lacks %s for: %s.", material_id, field, paste(missing_locales, collapse = ", ")))
      }
    }
    includes <- as_character(bundle$includes)
    if (bundle_index <= length(expected_bundle_categories) &&
        !identical(includes, expected_bundle_categories[[bundle_index]])) {
      fail(sprintf("Download bundle %s has a noncanonical category set or order.", material_id))
    }
    if (!grepl("^[a-z][a-z0-9-]*$", material_id)) {
      fail(sprintf("Download bundle ID is not a stable lowercase identifier: %s.", material_id))
    }
    if (!is.null(counter_config) && identical(bundle$primary, TRUE)) {
      material_counter_ids <- c(
        material_counter_ids,
        vapply(locales, function(locale) {
          render_identifier(
            counter_config$download_counts$id_template,
            list(material_id = material_id, locale = locale)
          )
        }, character(1))
      )
    }
    status <- as.character(bundle$status)
    download_status_by_id[[material_id]] <- status
    if (!identical(status, "available")) {
      fail(sprintf("Download bundle %s must be available when its real ZIP files are registered.", material_id))
      next
    }
    available_download_ids <- c(available_download_ids, material_id)
    formats <- toupper(vapply(bundle$files, function(file) {
      if (is.null(file$format)) "" else as.character(file$format)
    }, character(1)))
    if (!identical(formats, "ZIP")) {
      fail(sprintf("Download bundle %s must define exactly one ZIP file.", material_id))
    }
    for (file_record in bundle$files) {
      if (!all(locales %in% names(file_record$paths))) {
        fail(sprintf("Download bundle %s must define en, de, and sq paths.", material_id))
        next
      }
      for (locale in locales) {
        resource_path <- as.character(file_record$paths[[locale]])
        normalized_path <- gsub("\\\\", "/", resource_path)
        expected_directory <- sprintf("ratiomera-statistics/%s/downloads/files/", locale)
        expected_suffix <- sprintf("-%s\\.zip$", locale)
        if (!startsWith(normalized_path, expected_directory) ||
            !grepl(expected_suffix, basename(normalized_path), perl = TRUE)) {
          fail(sprintf("Download bundle %s has a noncanonical %s path: %s", material_id, locale, resource_path))
        }
        if (!file.exists(resource_path)) {
          fail(sprintf("Missing %s ZIP file for %s: %s", locale, material_id, resource_path))
        } else if (!has_zip_magic(resource_path)) {
          fail(sprintf("Download bundle %s is not a readable ZIP asset for %s: %s", material_id, locale, resource_path))
        }
      }
    }
  }
  if (anyDuplicated(material_ids)) fail(sprintf("Duplicate material IDs in %s.", metadata_path))
}

for (context in topic_page_contexts) {
  topic_number <- context$topic_number
  expected_summary <- sprintf("t%02d-summary", topic_number)
  expected_topic_downloads <- sprintf(
    "t%02d-%s", topic_number, c("exercises", "solutions")
  )
  practice_statuses <- unname(download_status_by_id[expected_topic_downloads])
  pair_is_published <- any(practice_statuses == "available", na.rm = TRUE)
  if (!pair_is_published) next

  declared_pair <- expected_topic_downloads %in% context$declared_downloads
  if (!all(declared_pair)) {
    fail(sprintf(
      "Lesson %s must declare its published paired downloads: %s.",
      context$page_id, paste(expected_topic_downloads, collapse = ", ")
    ))
  }
  if (!expected_summary %in% context$declared_downloads) {
    fail(sprintf(
      "Lesson %s must declare its downloadable summary: %s.",
      context$page_id, expected_summary
    ))
  }

  for (locale in locales) {
    path <- context$paths[[locale]]
    if (!file.exists(path)) next
    source_text <- paste(readLines(path, warn = FALSE, encoding = "UTF-8"), collapse = "\n")
    resource_calls <- regmatches(
      source_text,
      gregexpr("\\brender_topic_resources\\s*\\(", source_text, perl = TRUE)
    )[[1]]
    if (length(resource_calls) != 1L) {
      fail(sprintf(
        "Lesson %s must call render_topic_resources() exactly once in %s; found %d calls.",
        context$page_id, path, length(resource_calls)
      ))
      next
    }
    number_pattern <- sprintf("topic_number\\s*=\\s*%d(?:\\D|$)", topic_number)
    id_pattern <- sprintf(
      "topic_id\\s*=\\s*['\"]dl-topic-%d['\"]", topic_number
    )
    if (!grepl(number_pattern, source_text, perl = TRUE) &&
        !grepl(id_pattern, source_text, perl = TRUE)) {
      fail(sprintf(
        "Topic-resource selector in %s does not match lesson topic %d.",
        path, topic_number
      ))
    }
    summary_calls <- regmatches(
      source_text,
      gregexpr("\\brender_summary_resources\\s*\\(", source_text, perl = TRUE)
    )[[1]]
    if (length(summary_calls) != 1L) {
      fail(sprintf(
        "Lesson %s must call render_summary_resources() exactly once in %s; found %d calls.",
        context$page_id, path, length(summary_calls)
      ))
    }
    if (!grepl("course_id\\s*=\\s*['\"]intro-statistics['\"]", source_text, perl = TRUE)) {
      fail(sprintf("Topic-resource calls in %s must name the intro-statistics collection.", path))
    }
  }
}

expected_visible_counter_ids <- 9L * length(locales)
if (length(material_counter_ids) != expected_visible_counter_ids ||
    anyNA(material_counter_ids) || anyDuplicated(material_counter_ids)) {
  fail(sprintf(
    "Exactly %d package-counter IDs must resolve and remain unique across locales.",
    expected_visible_counter_ids
  ))
}
missing_download_records <- setdiff(unique(download_ids_from_manifest), unique(available_download_ids))
if (length(missing_download_records)) fail(paste("Manifest download IDs missing from download metadata:", paste(missing_download_records, collapse = ", ")))
orphan_download_records <- setdiff(unique(available_download_ids), unique(download_ids_from_manifest))
if (length(orphan_download_records)) fail(paste("Download metadata IDs missing from the parity manifest:", paste(orphan_download_records, collapse = ", ")))

extra_user_sources <- c("_variables.yml", download_metadata_paths, counter_config_path)
for (path in unique(extra_user_sources[file.exists(extra_user_sources)])) {
  contents <- paste(readLines(path, warn = FALSE, encoding = "UTF-8"), collapse = "\n")
  if (grepl("\u2014", contents, fixed = TRUE)) fail(sprintf("Em dash found in user-facing metadata: %s", path))
}

if (file.exists(counter_client_path)) {
  counter_client_text <- paste(readLines(counter_client_path, warn = FALSE, encoding = "UTF-8"), collapse = "\n")
  required_client_tokens <- c(
    "usage-page-visit-counter", "usage-download-count", "hits_sh",
    "github_releases", "counterState", "browser_download_url",
    "githubReleasePromises", "data-release-key", "resolveDownloadAssetLinks",
    "download-asset-action", "release_tag", "releases/tags/",
    "typeof value !== \"number\"", "value.trim() === \"\"",
    "countFromBadgeSvg", "image/svg+xml",
    "Counter badge did not expose a numeric total"
  )
  missing_tokens <- required_client_tokens[!vapply(required_client_tokens, function(token) {
    grepl(token, counter_client_text, fixed = TRUE)
  }, logical(1))]
  if (length(missing_tokens)) {
    fail(paste("Counter client lacks required provider/component tokens:", paste(missing_tokens, collapse = ", ")))
  }
  if (grepl("addEventListener\\([\"']click", counter_client_text, perl = TRUE) ||
      grepl("\\bonclick\\s*=", counter_client_text, perl = TRUE)) {
    fail("Counter client must not count local download clicks.")
  }
  if (grepl("releases/latest", counter_client_text, fixed = TRUE)) {
    fail("Counter client must resolve an exact configured release tag, not a moving latest release.")
  }
}

download_renderer_path <- "ratiomera-statistics/_shared/render-downloads.R"
if (!file.exists(download_renderer_path)) {
  fail(sprintf("Missing Downloads renderer: %s", download_renderer_path))
} else {
  renderer_text <- paste(readLines(download_renderer_path, warn = FALSE, encoding = "UTF-8"), collapse = "\n")
  for (token in c(
    "data-material-id", "usage-download-count", "download-topic-card",
    "download-primary-package", "download-secondary-bundles", "download-material-count",
    "counter_config_path", "render_topic_resources", "topic-download-resources",
    "render_summary_resources", "topic-summary-resources", "data-release-assets",
    "data-release-key", "data-release-asset", "download-asset-action",
    "topic-resource-card", "render_grouped_material_cards",
    "topic-resource-format-action", "download-bundle-card"
  )) {
    if (!grepl(token, renderer_text, fixed = TRUE)) {
      fail(sprintf("Downloads renderer does not emit required counter structure: %s.", token))
    }
  }
}

linkedin_channel <- manifest$official_social_channels$linkedin
canonical_linkedin_url <- "https://www.linkedin.com/company/ratiomera/"
linkedin_footer_class <- "footer-linkedin-item"
if (is.null(linkedin_channel)) {
  fail("The parity manifest must define the official Ratiomera LinkedIn channel.")
} else {
  linkedin_variable_reference <- as.character(linkedin_channel$url_variable)
  linkedin_variable_path <- sub("#.*$", "", linkedin_variable_reference)
  if (!identical(linkedin_variable_reference, "_variables.yml#social.linkedin")) {
    fail("The LinkedIn manifest entry must reference _variables.yml#social.linkedin.")
  } else if (!file.exists(linkedin_variable_path)) {
    fail(sprintf("Missing public social-variable file: %s", linkedin_variable_path))
  } else {
    public_variables <- yaml::read_yaml(linkedin_variable_path)
    configured_linkedin_url <- trimws(as.character(public_variables$social$linkedin))
    if (length(configured_linkedin_url) != 1L ||
        !identical(configured_linkedin_url, canonical_linkedin_url)) {
      fail("_variables.yml must define the canonical Ratiomera LinkedIn URL exactly once.")
    }
  }

  if (!identical(as.character(linkedin_channel$canonical_url), canonical_linkedin_url)) {
    fail("The LinkedIn manifest URL does not match the canonical Ratiomera company-page URL.")
  }
  if (!identical(as.character(linkedin_channel$placement), "global_footer_and_localized_contact_pages")) {
    fail("The LinkedIn channel must be declared for the global footer and all localized contact pages.")
  }
  if (!identical(as.character(linkedin_channel$footer_item_class), linkedin_footer_class)) {
    fail(sprintf("The LinkedIn footer item must use .%s.", linkedin_footer_class))
  }
  if (!identical(linkedin_channel$external_widget_or_tracker, FALSE)) {
    fail("The official LinkedIn channel must remain a plain link without a widget or tracker.")
  }

  contact_page_index <- which(page_ids == "ratiomera-contact")
  if (length(contact_page_index) != 1L) {
    fail("The page inventory must contain exactly one localized Ratiomera contact triplet.")
  } else {
    contact_page <- pages[[contact_page_index]]
    linkedin_variable_shortcode <- "{{< var social.linkedin >}}"
    for (locale in locales) {
      contact_path <- as.character(contact_page$paths[[locale]])
      if (!file.exists(contact_path)) next
      contact_text <- paste(readLines(contact_path, warn = FALSE, encoding = "UTF-8"), collapse = "\n")
      shortcode_matches <- gregexpr(linkedin_variable_shortcode, contact_text, fixed = TRUE)[[1]]
      shortcode_count <- if (identical(shortcode_matches[[1]], -1L)) 0L else length(shortcode_matches)
      if (shortcode_count != 1L) {
        fail(sprintf("%s must use the canonical LinkedIn variable exactly once.", contact_path))
      }
      for (token in c("contact-channel-link", "target=\"_blank\"", "rel=\"noopener noreferrer\"")) {
        if (!grepl(token, contact_text, fixed = TRUE)) {
          fail(sprintf("%s lacks required LinkedIn link semantics: %s.", contact_path, token))
        }
      }
      if (grepl("contact-label", contact_text, fixed = TRUE)) {
        fail(sprintf("%s contains a redundant visible contact-channel label.", contact_path))
      }
      if (grepl(canonical_linkedin_url, contact_text, fixed = TRUE)) {
        fail(sprintf("%s hardcodes the LinkedIn URL instead of using the shared variable.", contact_path))
      }
    }
  }

  contact_styles_path <- "styles/site.css"
  if (!file.exists(contact_styles_path)) {
    fail(sprintf("Missing contact stylesheet: %s", contact_styles_path))
  } else {
    contact_styles <- paste(readLines(contact_styles_path, warn = FALSE, encoding = "UTF-8"), collapse = "\n")
    contact_layout_patterns <- c(
      "\\.contact-card\\s*\\{[^}]*display:\\s*flex;[^}]*flex-direction:\\s*column;",
      "\\.contact-address\\s*\\{[^}]*align-self:\\s*flex-start;[^}]*max-width:\\s*100%;[^}]*margin-top:\\s*auto;[^}]*color:\\s*var\\(--color-link\\);",
      "\\.contact-channel-link\\s*\\{[^}]*align-self:\\s*flex-start;[^}]*max-width:\\s*100%;[^}]*margin-top:\\s*auto;[^}]*color:\\s*var\\(--color-link\\);"
    )
    if (!all(vapply(contact_layout_patterns, function(pattern) {
      grepl(pattern, contact_styles, perl = TRUE)
    }, logical(1)))) {
      fail("Contact cards must bottom-align email and LinkedIn links and use the shared link color.")
    }
  }
}

footer <- manifest$footer_language_selector
quarto_path <- as.character(footer$quarto_config)
switcher_path <- as.character(footer$mapping_script)
selector_class <- as.character(footer$selector_class)
mapping_function <- as.character(footer$mapping_function)
if (!file.exists(quarto_path)) {
  fail(sprintf("Missing footer configuration file: %s", quarto_path))
} else {
  quarto_text <- paste(readLines(quarto_path, warn = FALSE, encoding = "UTF-8"), collapse = "\n")
  if (!grepl("page-footer:", quarto_text, fixed = TRUE)) fail("_quarto.yml has no page-footer configuration.")
  if (!grepl(switcher_path, quarto_text, fixed = TRUE)) fail(sprintf("%s is not configured as a Quarto post-render step.", switcher_path))
  if (!grepl(counter_client_path, quarto_text, fixed = TRUE)) fail(sprintf("%s is not configured as a shared Quarto include.", counter_client_path))
}
if (!file.exists(switcher_path)) {
  fail(sprintf("Missing static footer language mapping script: %s", switcher_path))
} else {
  switcher_text <- paste(readLines(switcher_path, warn = FALSE, encoding = "UTF-8"), collapse = "\n")
  if (!all(vapply(as_character(footer$labels), function(label) grepl(paste0("['\"]", label, "['\"]"), switcher_text), logical(1)))) {
    fail(sprintf("%s does not recognize EN, DE, and SQ.", switcher_path))
  }
  if (!grepl(selector_class, switcher_text, fixed = TRUE)) {
    fail(sprintf("%s does not emit .%s.", switcher_path, selector_class))
  }
  if (!grepl(paste0(mapping_function, " <- function"), switcher_text, fixed = TRUE)) {
    fail(sprintf("%s does not define %s().", switcher_path, mapping_function))
  }
  if (!grepl("hreflang", switcher_text, fixed = TRUE) || !grepl("aria-current", switcher_text, fixed = TRUE)) {
    fail(sprintf("%s lacks alternate-language or active-language semantics.", switcher_path))
  }
  if (!grepl("page-visit-counter", switcher_text, fixed = TRUE) ||
      !grepl("counter_route_map", switcher_text, fixed = TRUE)) {
    fail(sprintf("%s does not inject route-mapped page-visit counters.", switcher_path))
  }
  if (!is.null(linkedin_channel)) {
    for (token in c(
      linkedin_footer_class, canonical_linkedin_url, "linkedin_aria",
      "target=\"_blank\"", "rel=\"noopener noreferrer\""
    )) {
      if (!grepl(token, switcher_text, fixed = TRUE)) {
        fail(sprintf("%s lacks required official LinkedIn footer semantics: %s.", switcher_path, token))
      }
    }
    if (!identical(as.character(linkedin_channel$footer_injector), switcher_path)) {
      fail("The LinkedIn footer injector must match the configured footer mapping script.")
    }
  }

  route_environment <- new.env(parent = globalenv())
  previous_output_files <- Sys.getenv("QUARTO_PROJECT_OUTPUT_FILES", unset = NA_character_)
  previous_project_dir <- Sys.getenv("QUARTO_PROJECT_DIR", unset = NA_character_)
  Sys.setenv(
    QUARTO_PROJECT_OUTPUT_FILES = "multilingual-validation-sentinel.txt",
    QUARTO_PROJECT_DIR = project_dir
  )
  source_error <- tryCatch(
    {
      suppressMessages(sys.source(switcher_path, envir = route_environment))
      NULL
    },
    error = function(error) conditionMessage(error)
  )
  if (is.na(previous_output_files)) Sys.unsetenv("QUARTO_PROJECT_OUTPUT_FILES") else Sys.setenv(QUARTO_PROJECT_OUTPUT_FILES = previous_output_files)
  if (is.na(previous_project_dir)) Sys.unsetenv("QUARTO_PROJECT_DIR") else Sys.setenv(QUARTO_PROJECT_DIR = previous_project_dir)

  if (!is.null(source_error)) {
    fail(sprintf("Could not load %s for route tests: %s", switcher_path, source_error))
  } else if (!exists(mapping_function, envir = route_environment, inherits = FALSE)) {
    fail(sprintf("Could not find %s() after loading %s.", mapping_function, switcher_path))
  } else {
    route_mapper <- get(mapping_function, envir = route_environment, inherits = FALSE)
    for (page in pages) {
      source_outputs <- vapply(locales, function(locale) sub("\\.qmd$", ".html", as.character(page$paths[[locale]])), character(1))
      names(source_outputs) <- locales
      for (source_locale in locales) {
        for (target_locale in locales) {
          actual <- tryCatch(
            route_mapper(source_outputs[[source_locale]], target_locale),
            error = function(error) structure(conditionMessage(error), class = "route_mapping_error")
          )
          expected <- source_outputs[[target_locale]]
          if (inherits(actual, "route_mapping_error")) {
            fail(sprintf("Footer mapping error for %s from %s to %s: %s", page$id, source_locale, target_locale, as.character(actual)))
          } else if (!identical(as.character(actual), expected)) {
            fail(sprintf("Footer mapping mismatch for %s from %s to %s: expected %s, found %s.", page$id, source_locale, target_locale, expected, actual))
          }
        }
      }
    }
  }
}

qmd_sources <- unique(all_paths[file.exists(all_paths)])
page_switcher_hits <- qmd_sources[vapply(qmd_sources, function(path) {
  grepl("class=[\"'][^\"']*language-switcher", paste(readLines(path, warn = FALSE, encoding = "UTF-8"), collapse = "\n"), perl = TRUE)
}, logical(1))]
if (identical(footer$page_level_selectors_allowed, FALSE) && length(page_switcher_hits)) {
  fail(paste("Page-level language switchers are not allowed; use the global footer:", paste(page_switcher_hits, collapse = ", ")))
}

cat(sprintf("Ratiomera multilingual validation: %d manifest pages, %d terminology entries, %d download records.\n", length(pages), length(terms), length(unique(available_download_ids))))
cat(sprintf(
  "Counter validation: %d canonical routes, %d stable download IDs, %d visible package IDs, providers %s/%s.\n",
  as.integer(counter_manifest$canonical_route_count), length(unique(registered_material_ids)),
  length(unique(material_counter_ids)) / length(locales),
  as.character(counter_config$page_visits$provider),
  as.character(counter_config$download_counts$provider)
))
if (length(warnings)) {
  cat("\nWARNINGS\n")
  cat(paste0("- ", unique(warnings), collapse = "\n"), "\n")
}
if (length(failures)) {
  cat("\nFAILURES\n")
  cat(paste0("- ", unique(failures), collapse = "\n"), "\n")
  quit(save = "no", status = 1L)
}

cat("PASS: route triplets, metadata, Unicode-safe figure rendering, internal links, inline math, em dashes, structural parity, static Theory figures, interactive Simulated Example figures, downloads, assets, terminology, footer language and official social mapping, and counter configuration.\n")
