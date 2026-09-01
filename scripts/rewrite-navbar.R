#!/usr/bin/env Rscript

# Quarto supports one project-wide website navbar. This post-render step
# converts that shared seed into the correct static navbar for each section,
# so navigation remains structurally correct without client-side JavaScript.

if (!requireNamespace("xml2", quietly = TRUE)) {
  stop(
    "Navbar post-render step requires the R package 'xml2'. ",
    "Install it before rendering Ratiomera.",
    call. = FALSE
  )
}
if (!requireNamespace("yaml", quietly = TRUE)) {
  stop("Counter configuration requires the R package 'yaml'.", call. = FALSE)
}
if (!requireNamespace("jsonlite", quietly = TRUE)) {
  stop("Counter configuration requires the R package 'jsonlite'.", call. = FALSE)
}

project_dir <- Sys.getenv("QUARTO_PROJECT_DIR", unset = getwd())
output_list <- Sys.getenv("QUARTO_PROJECT_OUTPUT_FILES", unset = "")

if (!nzchar(output_list)) {
  quit(save = "no", status = 0)
}

counter_config_path <- file.path(project_dir, "config/counters.yml")
counter_manifest_path <- file.path(project_dir, "config/content-parity.yml")
public_variables_path <- file.path(project_dir, "_variables.yml")
if (!file.exists(counter_config_path)) stop("Missing counter configuration: ", counter_config_path, call. = FALSE)
if (!file.exists(counter_manifest_path)) stop("Missing counter route manifest: ", counter_manifest_path, call. = FALSE)
if (!file.exists(public_variables_path)) stop("Missing public variables: ", public_variables_path, call. = FALSE)

counter_config <- yaml::read_yaml(counter_config_path)
counter_manifest <- yaml::read_yaml(counter_manifest_path)
public_variables <- yaml::read_yaml(public_variables_path)
linkedin_url <- trimws(as.character(public_variables$social$linkedin))
if (length(linkedin_url) != 1L ||
    !identical(linkedin_url, "https://www.linkedin.com/company/ratiomera/")) {
  stop("_variables.yml must define the canonical Ratiomera LinkedIn URL.", call. = FALSE)
}

make_counter_id <- function(template, values) {
  identifier <- as.character(template)
  for (name in names(values)) {
    identifier <- gsub(
      paste0("{", name, "}"), as.character(values[[name]]), identifier, fixed = TRUE
    )
  }
  if (grepl("\\{[^}]+\\}", identifier)) {
    stop("Unresolved counter ID template: ", identifier, call. = FALSE)
  }
  identifier
}

xml_escape <- function(value, attribute = FALSE) {
  escaped <- gsub("&", "&amp;", as.character(value), fixed = TRUE)
  escaped <- gsub("<", "&lt;", escaped, fixed = TRUE)
  escaped <- gsub(">", "&gt;", escaped, fixed = TRUE)
  if (attribute) {
    escaped <- gsub('"', "&quot;", escaped, fixed = TRUE)
    escaped <- gsub("'", "&apos;", escaped, fixed = TRUE)
  }
  escaped
}

counter_page_types <- as.character(unlist(
  counter_config$page_visits$included_page_types, use.names = FALSE
))
counter_route_map <- list()
for (page in counter_manifest$pages) {
  if (!as.character(page$page_type) %in% counter_page_types) next
  for (locale in c("en", "de", "sq")) {
    output_path <- sub("\\.qmd$", ".html", as.character(page$paths[[locale]]))
    if (!is.null(counter_route_map[[output_path]])) {
      stop("Duplicate canonical counter route: ", output_path, call. = FALSE)
    }
    counter_route_map[[output_path]] <- list(
      page_id = as.character(page$id),
      locale = locale,
      counter_id = make_counter_id(
        counter_config$page_visits$id_template,
        list(page_id = as.character(page$id), locale = locale)
      )
    )
  }
}

counter_config_json <- jsonlite::toJSON(
  counter_config, auto_unbox = TRUE, null = "null", digits = NA
)
counter_config_json <- gsub("</", "<\\/", counter_config_json, fixed = TRUE)
counter_config_script <- paste0(
  '<script id="usage-counter-config" type="application/json">',
  counter_config_json,
  "</script>"
)

output_files <- strsplit(output_list, "\n", fixed = TRUE)[[1]]
output_files <- output_files[nzchar(output_files) & grepl("\\.html$", output_files)]
output_files <- vapply(
  output_files,
  function(path) {
    if (grepl("^/", path)) path else file.path(project_dir, path)
  },
  character(1)
)

paths <- list(
  root = list(
    home = c(
      en = "en/home-ratiomera-en.html",
      de = "de/home-ratiomera-de.html",
      sq = "sq/home-ratiomera-sq.html"
    ),
    about = c(
      en = "en/pages/about-ratiomera-en.html",
      de = "de/pages/about-ratiomera-de.html",
      sq = "sq/pages/about-ratiomera-sq.html"
    ),
    contact = c(
      en = "en/pages/contact-ratiomera-en.html",
      de = "de/pages/contact-ratiomera-de.html",
      sq = "sq/pages/contact-ratiomera-sq.html"
    ),
    support = c(
      en = "en/pages/support-ratiomera-en.html",
      de = "de/pages/support-ratiomera-de.html",
      sq = "sq/pages/support-ratiomera-sq.html"
    ),
    legal = c(
      en = "en/pages/legal-ratiomera-en.html",
      de = "de/pages/legal-ratiomera-de.html",
      sq = "sq/pages/legal-ratiomera-sq.html"
    )
  ),
  statistics = list(
    home = c(
      en = "ratiomera-statistics/en/home-statistics-en.html",
      de = "ratiomera-statistics/de/home-statistics-de.html",
      sq = "ratiomera-statistics/sq/home-statistics-sq.html"
    ),
    course = c(
      en = "ratiomera-statistics/en/intro-stats/overview-intro-stats-en.html",
      de = "ratiomera-statistics/de/intro-stats/overview-intro-stats-de.html",
      sq = "ratiomera-statistics/sq/intro-stats/overview-intro-stats-sq.html"
    ),
    downloads = c(
      en = "ratiomera-statistics/en/downloads/overview-downloads-en.html",
      de = "ratiomera-statistics/de/downloads/overview-downloads-de.html",
      sq = "ratiomera-statistics/sq/downloads/overview-downloads-sq.html"
    )
  ),
  mathematics = list(
    home = c(
      en = "ratiomera-mathematics/en/home-mathematics-en.html",
      de = "ratiomera-mathematics/de/home-mathematics-de.html",
      sq = "ratiomera-mathematics/sq/home-mathematics-sq.html"
    )
  )
)

labels <- list(
  en = c(
    about = "About", statistics = "Statistics", mathematics = "Mathematics",
    contact = "Contact", support = "Support", ratiomera = "Ratiomera",
    course = "Introduction to Statistics", downloads = "Downloads",
    home = "home", primary_nav = "Primary navigation",
    page_tools = "Page tools", course_nav = "Learning-sequence navigation",
    breadcrumb = "Breadcrumb", toggle_nav = "Toggle navigation",
    toggle_sidebar = "Toggle learning-sequence navigation", legal = "Legal Notice",
    language_nav = "Language selection",
    linkedin_aria = "Ratiomera on LinkedIn, opens in a new tab",
    copyright = "© 2025–2026 Ratiomera. Free education in mathematics and statistics."
  ),
  de = c(
    about = "Über uns", statistics = "Statistik", mathematics = "Mathematik",
    contact = "Kontakt", support = "Unterstützen", ratiomera = "Ratiomera",
    course = "Einführung in die Statistik", downloads = "Downloads",
    home = "Startseite", primary_nav = "Hauptnavigation",
    page_tools = "Seitenwerkzeuge", course_nav = "Navigation der Lernsequenz",
    breadcrumb = "Pfadnavigation", toggle_nav = "Navigation ein- oder ausblenden",
    toggle_sidebar = "Navigation der Lernsequenz ein- oder ausblenden", legal = "Impressum",
    language_nav = "Sprachauswahl",
    linkedin_aria = "Ratiomera auf LinkedIn, öffnet sich in einem neuen Tab",
    copyright = "© 2025–2026 Ratiomera. Freie Bildung in Mathematik und Statistik."
  ),
  sq = c(
    about = "Rreth Nesh", statistics = "Statistikë", mathematics = "Matematikë",
    contact = "Kontakt", support = "Mbështetje", ratiomera = "Ratiomera",
    course = "Hyrje në Statistikë", downloads = "Shkarkime",
    home = "faqja kryesore", primary_nav = "Navigimi kryesor",
    page_tools = "Mjetet e faqes", course_nav = "Navigimi i renditjes mësimore",
    breadcrumb = "Gjurmë navigimi", toggle_nav = "Hap ose mbyll navigimin",
    toggle_sidebar = "Hap ose mbyll navigimin e renditjes mësimore", legal = "Njoftimi ligjor",
    language_nav = "Zgjedhja e gjuhës",
    linkedin_aria = "Ratiomera në LinkedIn, hapet në një skedë të re",
    copyright = "© 2025–2026 Ratiomera. Arsim i lirë në matematikë dhe statistikë."
  )
)

missing_node <- function(node) inherits(node, "xml_missing")

required_node <- function(parent, xpath, description) {
  node <- xml2::xml_find_first(parent, xpath)
  if (missing_node(node)) stop("Missing ", description, call. = FALSE)
  node
}

nav_links <- function(header) {
  xml2::xml_find_all(
    header,
    ".//a[contains(concat(' ', normalize-space(@class), ' '), ' nav-link ')]"
  )
}

link_by_suffix <- function(header, suffix, description) {
  candidates <- nav_links(header)
  hrefs <- xml2::xml_attr(candidates, "href")
  hits <- candidates[!is.na(hrefs) & grepl(suffix, hrefs, fixed = TRUE)]
  if (length(hits) != 1L) {
    stop("Expected one ", description, " link; found ", length(hits), call. = FALSE)
  }
  hits[[1]]
}

set_label <- function(link, value) {
  text_node <- xml2::xml_find_first(
    link,
    ".//span[contains(concat(' ', normalize-space(@class), ' '), ' menu-text ')]"
  )
  if (missing_node(text_node)) {
    xml2::xml_set_text(link, value)
  } else {
    xml2::xml_set_text(text_node, value)
  }
}

remove_nav_item <- function(link) {
  item <- xml2::xml_find_first(
    link,
    "ancestor::li[contains(concat(' ', normalize-space(@class), ' '), ' nav-item ')][1]"
  )
  if (missing_node(item)) stop("Navbar link has no nav-item parent", call. = FALSE)
  xml2::xml_remove(item)
}

class_tokens <- function(node) {
  value <- xml2::xml_attr(node, "class")
  if (is.na(value) || !nzchar(trimws(value))) character() else strsplit(trimws(value), "\\s+")[[1]]
}

remove_class <- function(node, value) {
  xml2::xml_set_attr(node, "class", paste(setdiff(class_tokens(node), value), collapse = " "))
}

add_class <- function(node, value) {
  xml2::xml_set_attr(node, "class", paste(unique(c(class_tokens(node), value)), collapse = " "))
}

clear_current <- function(link) {
  remove_class(link, "active")
  xml2::xml_attr(link, "aria-current") <- NULL
}

preferred_home <- function(section, language) {
  homes <- paths[[section]]$home
  if (language %in% names(homes)) unname(homes[[language]]) else unname(homes[["en"]])
}

preferred_course <- function(language) {
  courses <- paths$statistics$course
  if (language %in% names(courses)) unname(courses[[language]]) else unname(courses[["en"]])
}

preferred_path <- function(localized_paths, language) {
  if (language %in% names(localized_paths)) {
    unname(localized_paths[[language]])
  } else {
    unname(localized_paths[["en"]])
  }
}

localized_output_path <- function(relative_file, target_language) {
  path <- sub("^docs/", "", relative_file)

  fixed_routes <- c(
    "index.html" = preferred_home("root", target_language),
    "en/index.html" = preferred_home("root", target_language),
    "about.html" = preferred_path(paths$root$about, target_language),
    "contact.html" = preferred_path(paths$root$contact, target_language),
    "support.html" = preferred_path(paths$root$support, target_language),
    "legal.html" = preferred_path(paths$root$legal, target_language),
    "ratiomera-statistics/index.html" = preferred_home("statistics", target_language),
    "ratiomera-mathematics/index.html" = preferred_home("mathematics", target_language)
  )
  if (path %in% names(fixed_routes)) return(unname(fixed_routes[[path]]))

  path <- sub(
    "(^|/)(en|de|sq)/",
    paste0("\\1", target_language, "/"),
    path,
    perl = TRUE
  )
  sub(
    "-(en|de|sq)(\\.html)$",
    paste0("-", target_language, "\\2"),
    path,
    perl = TRUE
  )
}

splice_header <- function(
  output_file, original, header, footer, alternate_links, sidebar_label,
  counter_script = ""
) {
  opening <- regexpr('<header id="quarto-header"', original, fixed = TRUE)[1]
  if (opening < 1L) stop("Could not locate original Quarto header in ", output_file, call. = FALSE)

  remainder <- substring(original, opening)
  closing_relative <- regexpr("</header>", remainder, fixed = TRUE)[1]
  if (closing_relative < 1L) stop("Could not locate header closing tag in ", output_file, call. = FALSE)

  closing <- opening + closing_relative + nchar("</header>") - 2L
  replacement <- paste0(
    if (opening > 1L) substr(original, 1L, opening - 1L) else "",
    as.character(header),
    if (closing < nchar(original)) substr(original, closing + 1L, nchar(original)) else ""
  )

  sidebar_marker <- '<nav id="quarto-sidebar"'
  if (grepl(sidebar_marker, replacement, fixed = TRUE)) {
    replacement <- sub(
      sidebar_marker,
      paste0(sidebar_marker, ' aria-label="', sidebar_label, '"'),
      replacement,
      fixed = TRUE
    )
    replacement <- sub(
      'class="sidebar-logo-link"',
      'class="sidebar-logo-link" aria-hidden="true" tabindex="-1"',
      replacement,
      fixed = TRUE
    )
    replacement <- gsub(
      'role="navigation" aria-expanded=',
      'role="button" aria-expanded=',
      replacement,
      fixed = TRUE
    )
  }

  footer_opening <- regexpr('<footer class="footer"', replacement, fixed = TRUE)[1]
  if (footer_opening < 1L) stop("Could not locate page footer in ", output_file, call. = FALSE)

  # substring() defaults its final index to one million characters. Fully
  # interactive teaching pages can legitimately exceed that size, which used
  # to make an otherwise intact footer appear absent. Always slice through the
  # actual end of the rendered document.
  footer_remainder <- substr(replacement, footer_opening, nchar(replacement))
  footer_closing_relative <- regexpr("</footer>", footer_remainder, fixed = TRUE)[1]
  if (footer_closing_relative < 1L) stop("Could not locate footer closing tag in ", output_file, call. = FALSE)

  footer_closing <- footer_opening + footer_closing_relative + nchar("</footer>") - 2L
  replacement <- paste0(
    if (footer_opening > 1L) substr(replacement, 1L, footer_opening - 1L) else "",
    as.character(footer),
    if (footer_closing < nchar(replacement)) substr(replacement, footer_closing + 1L, nchar(replacement)) else ""
  )

  head_closing <- regexpr("</head>", replacement, fixed = TRUE)[1]
  if (head_closing < 1L) stop("Could not locate document head in ", output_file, call. = FALSE)
  head_insertions <- c(alternate_links, counter_script[nzchar(counter_script)])
  replacement <- paste0(
    if (head_closing > 1L) substr(replacement, 1L, head_closing - 1L) else "",
    paste0(head_insertions, collapse = "\n"),
    "\n",
    substr(replacement, head_closing, nchar(replacement))
  )

  connection <- file(output_file, open = "wb")
  on.exit(close(connection), add = TRUE)
  writeChar(replacement, connection, eos = NULL, useBytes = TRUE)
}

rewrite_navbar <- function(file) {
  original <- readChar(file, nchars = file.info(file)$size, useBytes = TRUE)
  document <- xml2::read_html(file, options = c("RECOVER", "NOERROR", "NOWARNING"))
  header <- required_node(document, "//*[@id='quarto-header']", "Quarto header")

  relative_file <- gsub("\\\\", "/", substring(file, nchar(project_dir) + 2L))
  section <- if (grepl("(^|/)ratiomera-statistics/", relative_file)) {
    "statistics"
  } else if (grepl("(^|/)ratiomera-mathematics/", relative_file)) {
    "mathematics"
  } else {
    "root"
  }
  language <- if (grepl("(^|/)de/", relative_file)) {
    "de"
  } else if (grepl("(^|/)sq/", relative_file)) {
    "sq"
  } else {
    "en"
  }
  text <- labels[[language]]
  brand_name <- switch(
    section,
    statistics = "Ratiomera Statistics",
    mathematics = "Ratiomera Mathematics",
    "Ratiomera"
  )

  primary_nav <- required_node(
    header,
    ".//nav[contains(concat(' ', normalize-space(@class), ' '), ' navbar ')]",
    "primary navigation"
  )
  xml2::xml_set_attr(primary_nav, "aria-label", text[["primary_nav"]])

  secondary_nav <- xml2::xml_find_first(
    header,
    ".//nav[contains(concat(' ', normalize-space(@class), ' '), ' quarto-secondary-nav ')]"
  )
  if (!missing_node(secondary_nav)) {
    xml2::xml_set_attr(secondary_nav, "aria-label", text[["page_tools"]])
  }

  breadcrumb_nav <- xml2::xml_find_first(
    header,
    ".//nav[contains(concat(' ', normalize-space(@class), ' '), ' quarto-page-breadcrumbs ')]"
  )
  if (!missing_node(breadcrumb_nav)) {
    xml2::xml_set_attr(breadcrumb_nav, "aria-label", text[["breadcrumb"]])
  }

  navbar_toggle <- xml2::xml_find_first(
    header,
    ".//button[contains(concat(' ', normalize-space(@class), ' '), ' navbar-toggler ')]"
  )
  if (!missing_node(navbar_toggle)) {
    xml2::xml_set_attr(navbar_toggle, "aria-label", text[["toggle_nav"]])
    xml2::xml_attr(navbar_toggle, "role") <- NULL
  }

  sidebar_toggles <- xml2::xml_find_all(header, ".//*[@aria-controls='quarto-sidebar']")
  invisible(lapply(
    sidebar_toggles,
    xml2::xml_set_attr,
    attr = "aria-label",
    value = text[["toggle_sidebar"]]
  ))
  sidebar_toggle_links <- xml2::xml_find_all(
    header,
    ".//a[@aria-controls='quarto-sidebar']"
  )
  invisible(lapply(
    sidebar_toggle_links,
    xml2::xml_set_attr,
    attr = "role",
    value = "button"
  ))

  links <- list(
    course = link_by_suffix(header, paths$statistics$course[["en"]], "course"),
    downloads = link_by_suffix(header, paths$statistics$downloads[["en"]], "Downloads"),
    about = link_by_suffix(header, paths$root$about[["en"]], "About"),
    statistics = link_by_suffix(header, paths$statistics$home[["en"]], "Statistics"),
    mathematics = link_by_suffix(header, paths$mathematics$home[["en"]], "Mathematics"),
    contact = link_by_suffix(header, paths$root$contact[["en"]], "Contact"),
    support = link_by_suffix(header, paths$root$support[["en"]], "Support")
  )

  about_href <- xml2::xml_attr(links$about, "href")
  suffix_position <- regexpr(paths$root$about[["en"]], about_href, fixed = TRUE)[1]
  if (suffix_position < 1L) stop("Could not derive project-root href prefix", call. = FALSE)
  root_prefix <- if (suffix_position == 1L) "" else substr(about_href, 1L, suffix_position - 1L)

  brand_links <- xml2::xml_find_all(
    header,
    ".//a[contains(concat(' ', normalize-space(@class), ' '), ' navbar-brand ')]"
  )
  if (!length(brand_links)) stop("Missing navbar brand links", call. = FALSE)
  brand_title <- required_node(header, ".//*[contains(concat(' ', normalize-space(@class), ' '), ' navbar-title ')]", "navbar title")
  brand_images <- xml2::xml_find_all(
    header,
    ".//img[contains(concat(' ', normalize-space(@class), ' '), ' navbar-logo ')]"
  )
  if (!length(brand_images)) stop("Missing navbar logo images", call. = FALSE)
  brand_logo_link <- required_node(
    header,
    ".//a[contains(concat(' ', normalize-space(@class), ' '), ' navbar-brand-logo ')]",
    "navbar logo link"
  )
  xml2::xml_set_attr(
    brand_logo_link,
    "aria-label",
    paste(brand_name, text[["home"]])
  )

  invisible(lapply(nav_links(header), clear_current))

  if (section == "root") {
    remove_nav_item(links$course)
    remove_nav_item(links$downloads)
    brand_target <- paste0(root_prefix, preferred_home("root", language))
    xml2::xml_set_text(brand_title, "Ratiomera")
    set_label(links$about, text[["about"]])
    set_label(links$statistics, text[["statistics"]])
    set_label(links$mathematics, text[["mathematics"]])
    set_label(links$contact, text[["contact"]])
    set_label(links$support, text[["support"]])
    xml2::xml_set_attr(links$about, "href", paste0(root_prefix, preferred_path(paths$root$about, language)))
    xml2::xml_set_attr(links$statistics, "href", paste0(root_prefix, preferred_home("statistics", language)))
    xml2::xml_set_attr(links$mathematics, "href", paste0(root_prefix, preferred_home("mathematics", language)))
    xml2::xml_set_attr(links$contact, "href", paste0(root_prefix, preferred_path(paths$root$contact, language)))
    xml2::xml_set_attr(links$support, "href", paste0(root_prefix, preferred_path(paths$root$support, language)))
    expected <- unname(text[c("about", "statistics", "mathematics", "contact", "support")])
  } else {
    brand_target <- paste0(root_prefix, preferred_home(section, language))
    xml2::xml_set_text(brand_title, brand_name)

    if (section == "statistics") {
      remove_nav_item(links$statistics)
      set_label(links$course, text[["course"]])
      xml2::xml_set_attr(links$course, "href", paste0(root_prefix, preferred_course(language)))
      set_label(links$downloads, text[["downloads"]])
      xml2::xml_set_attr(links$downloads, "href", paste0(root_prefix, preferred_path(paths$statistics$downloads, language)))
      set_label(links$mathematics, text[["mathematics"]])
      xml2::xml_set_attr(links$mathematics, "href", paste0(root_prefix, preferred_home("mathematics", language)))
      expected <- c(
        text[["course"]], text[["downloads"]], text[["ratiomera"]],
        text[["mathematics"]], text[["contact"]], text[["support"]]
      )
    } else {
      remove_nav_item(links$course)
      remove_nav_item(links$downloads)
      remove_nav_item(links$mathematics)
      set_label(links$statistics, text[["statistics"]])
      xml2::xml_set_attr(links$statistics, "href", paste0(root_prefix, preferred_home("statistics", language)))
      expected <- c(
        text[["ratiomera"]], text[["statistics"]],
        text[["contact"]], text[["support"]]
      )
    }

    set_label(links$about, text[["ratiomera"]])
    xml2::xml_set_attr(links$about, "href", paste0(root_prefix, preferred_home("root", language)))
    set_label(links$contact, text[["contact"]])
    xml2::xml_set_attr(links$contact, "href", paste0(root_prefix, preferred_path(paths$root$contact, language)))
    set_label(links$support, text[["support"]])
    xml2::xml_set_attr(links$support, "href", paste0(root_prefix, preferred_path(paths$root$support, language)))
  }

  invisible(lapply(brand_links, xml2::xml_set_attr, attr = "href", value = brand_target))
  brand_mark <- switch(
    section,
    statistics = "assets/brand/ratiomera-statistics-mark.svg",
    mathematics = "assets/brand/ratiomera-mathematics-mark.svg",
    "assets/brand/ratiomera-mark.svg"
  )
  invisible(lapply(brand_images, xml2::xml_set_attr, attr = "src", value = paste0(root_prefix, brand_mark)))
  invisible(lapply(brand_images, xml2::xml_set_attr, attr = "alt", value = ""))

  current_file <- normalizePath(file, winslash = "/", mustWork = TRUE)
  for (link in nav_links(header)) {
    href <- xml2::xml_attr(link, "href")
    if (is.na(href) || grepl("^(#|[a-z]+:)", href, ignore.case = TRUE)) next
    href_path <- sub("[?#].*$", "", href)
    target_file <- normalizePath(file.path(dirname(file), href_path), winslash = "/", mustWork = FALSE)
    if (identical(target_file, current_file)) {
      add_class(link, "active")
      xml2::xml_set_attr(link, "aria-current", "page")
    }
  }

  if (section == "statistics" && grepl("/intro-stats/", relative_file, fixed = TRUE)) {
    course_link <- link_by_suffix(header, preferred_course(language), "course")
    add_class(course_link, "active")
  }

  if (section == "statistics" && grepl("/downloads/", relative_file, fixed = TRUE)) {
    downloads_link <- link_by_suffix(header, preferred_path(paths$statistics$downloads, language), "Downloads")
    add_class(downloads_link, "active")
  }

  actual <- trimws(xml2::xml_text(nav_links(header)))
  if (!identical(actual, unname(expected))) {
    stop(
      "Unexpected final navbar for ", relative_file, ": ",
      paste(actual, collapse = " | "),
      call. = FALSE
    )
  }

  footer <- required_node(
    document,
    "//footer[contains(concat(' ', normalize-space(@class), ' '), ' footer ')]",
    "page footer"
  )
  footer_left <- required_node(
    footer,
    ".//*[contains(concat(' ', normalize-space(@class), ' '), ' nav-footer-left ')]//p",
    "footer copyright"
  )
  xml2::xml_set_text(footer_left, text[["copyright"]])

  footer_right_link <- required_node(
    footer,
    ".//*[contains(concat(' ', normalize-space(@class), ' '), ' nav-footer-right ')]//a",
    "footer legal link"
  )
  xml2::xml_set_attr(
    footer_right_link,
    "href",
    paste0(root_prefix, preferred_path(paths$root$legal, language))
  )
  footer_right_text <- xml2::xml_find_first(footer_right_link, ".//p")
  if (missing_node(footer_right_text)) {
    xml2::xml_set_text(footer_right_link, text[["legal"]])
  } else {
    xml2::xml_set_text(footer_right_text, text[["legal"]])
  }

  footer_right_items <- required_node(
    footer,
    ".//*[contains(concat(' ', normalize-space(@class), ' '), ' nav-footer-right ')]//ul",
    "footer right item list"
  )
  existing_linkedin_items <- xml2::xml_find_all(
    footer,
    ".//*[contains(concat(' ', normalize-space(@class), ' '), ' footer-linkedin-item ')]"
  )
  if (length(existing_linkedin_items)) {
    stop("Footer already contains a LinkedIn item: ", relative_file, call. = FALSE)
  }
  linkedin_markup <- xml2::read_xml(paste0(
    '<li class="nav-item footer-linkedin-item">',
    '<a class="nav-link" href="', xml_escape(linkedin_url, attribute = TRUE), '"',
    ' target="_blank" rel="noopener noreferrer"',
    ' aria-label="', xml_escape(text[["linkedin_aria"]], attribute = TRUE), '">',
    '<p>LinkedIn</p></a></li>'
  ))
  xml2::xml_add_child(footer_right_items, linkedin_markup)

  footer_center <- required_node(
    footer,
    ".//*[contains(concat(' ', normalize-space(@class), ' '), ' nav-footer-center ')]",
    "footer center"
  )
  xml2::xml_remove(xml2::xml_contents(footer_center))
  language_codes <- c(en = "EN", de = "DE", sq = "SQ")
  alternate_links <- mapply(
    function(target_language) {
      target <- paste0(root_prefix, localized_output_path(relative_file, target_language))
      paste0(
        '<link rel="alternate" hreflang="', target_language,
        '" href="', target, '">'
      )
    },
    names(language_codes),
    USE.NAMES = FALSE
  )
  alternate_links <- c(
    alternate_links,
    paste0(
      '<link rel="alternate" hreflang="x-default" href="',
      root_prefix,
      localized_output_path(relative_file, "en"),
      '">'
    )
  )
  language_items <- mapply(
    function(target_language, label) {
      target <- paste0(root_prefix, localized_output_path(relative_file, target_language))
      if (identical(target_language, language)) {
        paste0('<span class="active" lang="', target_language, '" aria-current="page">', label, "</span>")
      } else {
        paste0('<a href="', target, '" lang="', target_language, '" hreflang="', target_language, '">', label, "</a>")
      }
    },
    names(language_codes),
    unname(language_codes),
    USE.NAMES = FALSE
  )
  language_nav <- xml2::read_xml(paste0(
    '<nav class="footer-language-selector" aria-label="', text[["language_nav"]], '">',
    language_items[[1]], '<span class="separator" aria-hidden="true">|</span>',
    language_items[[2]], '<span class="separator" aria-hidden="true">|</span>',
    language_items[[3]],
    "</nav>"
  ))
  xml2::xml_add_child(footer_center, language_nav)

  output_route <- sub("^docs/", "", relative_file)
  counter_entry <- counter_route_map[[output_route]]
  if (!is.null(counter_entry)) {
    refresh_meta <- xml2::xml_find_first(
      document,
      "//meta[translate(@http-equiv, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz')='refresh']"
    )
    if (!missing_node(refresh_meta)) {
      stop("Canonical counter route unexpectedly redirects: ", output_route, call. = FALSE)
    }

    existing_counters <- xml2::xml_find_all(
      footer,
      ".//*[contains(concat(' ', normalize-space(@class), ' '), ' page-visit-counter ')]"
    )
    if (length(existing_counters)) {
      stop("Footer already contains a page visit counter: ", output_route, call. = FALSE)
    }

    counter_labels <- counter_config$locales[[counter_entry$locale]]
    counter_aria <- paste0(counter_labels$visits, ": ", counter_labels$unavailable)
    counter_markup <- xml2::read_xml(paste0(
      '<li class="nav-item footer-visit-item">',
      '<usage-page-visit-counter class="page-visit-counter usage-counter" role="group"',
      ' data-counter-id="', xml_escape(counter_entry$counter_id, attribute = TRUE), '"',
      ' data-page-id="', xml_escape(counter_entry$page_id, attribute = TRUE), '"',
      ' data-locale="', xml_escape(counter_entry$locale, attribute = TRUE), '"',
      ' data-label="', xml_escape(counter_labels$visits, attribute = TRUE), '"',
      ' aria-label="', xml_escape(counter_aria, attribute = TRUE), '">',
      '<span class="counter-fallback" aria-hidden="true">',
      '<span class="counter-label">', xml_escape(counter_labels$visits), '</span>',
      '<span class="counter-value">', xml_escape(counter_config$placeholder), '</span>',
      "</span></usage-page-visit-counter></li>"
    ))
    xml2::xml_add_child(footer_right_items, counter_markup)
  }

  splice_header(
    file,
    original,
    header,
    footer,
    alternate_links,
    text[["course_nav"]],
    if (is.null(counter_entry)) "" else counter_config_script
  )
}

for (output_file in output_files) {
  tryCatch(
    rewrite_navbar(output_file),
    error = function(error) {
      stop("Navbar rewrite failed for ", output_file, ": ", conditionMessage(error), call. = FALSE)
    }
  )
}

# Quarto's `aliases` feature emits minimal JavaScript redirect documents that
# do not inherit the canonical page's `lang` metadata. Keep those legacy
# routes accessible and standards-compliant without turning them into full
# pages or adding counters. The redirect target determines the language; the
# current aliases all target canonical English routes, while the general
# mapping also handles future German or Albanian aliases honestly.
normalize_alias_redirects <- function(site_output_dir) {
  alias_redirect_count <- 0L
  alias_files <- if (dir.exists(site_output_dir)) {
    list.files(site_output_dir, pattern = "\\.html$", recursive = TRUE, full.names = TRUE)
  } else {
    character()
  }

  for (alias_file in alias_files) {
    alias_text <- paste(readLines(alias_file, warn = FALSE, encoding = "UTF-8"), collapse = "\n")
    if (!grepl("var redirects =", alias_text, fixed = TRUE) ||
        grepl("<html[^>]*[[:space:]]lang=", alias_text, perl = TRUE)) {
      next
    }

    target_match <- regexec(
      'var redirects = \\{\"\":\"([^\"]+)\"\\};',
      alias_text,
      perl = TRUE
    )
    target_parts <- regmatches(alias_text, target_match)[[1]]
    target <- if (length(target_parts) >= 2L) target_parts[[2]] else ""
    target_segments <- strsplit(gsub("\\\\", "/", target), "/", fixed = TRUE)[[1]]
    alias_language <- if ("sq" %in% target_segments) {
      "sq"
    } else if ("de" %in% target_segments) {
      "de-CH"
    } else {
      "en"
    }

    html_tag <- '<html xmlns="http://www.w3.org/1999/xhtml">'
    if (!grepl(html_tag, alias_text, fixed = TRUE)) {
      stop("Unexpected Quarto alias redirect structure: ", alias_file, call. = FALSE)
    }
    alias_text <- sub(
      html_tag,
      paste0('<html xmlns="http://www.w3.org/1999/xhtml" lang="', alias_language, '">'),
      alias_text,
      fixed = TRUE
    )
    writeLines(alias_text, alias_file, useBytes = TRUE)
    alias_redirect_count <- alias_redirect_count + 1L
  }

  alias_redirect_count
}

alias_redirect_count <- if (length(output_files)) {
  normalize_alias_redirects(file.path(project_dir, "docs"))
} else {
  0L
}

message(
  "Rewrote static section navigation in ", length(output_files),
  " HTML file(s); normalized ", alias_redirect_count,
  " Quarto alias redirect(s)."
)
