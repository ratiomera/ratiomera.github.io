#!/usr/bin/env Rscript

# Quarto's Pandoc template adds an obsolete remote ES6 polyfill whenever
# MathJax is selected. Ratiomera supports current browsers and vendors the exact
# MathJax 3.2.2 CHTML distribution instead. This post-render step removes that
# polyfill, gives every formula page a depth-correct local MathJax URL, and
# fails if a rendered page retains a remote math dependency.

script_arg <- grep("^--file=", commandArgs(trailingOnly = FALSE), value = TRUE)
script_path <- if (length(script_arg)) {
  sub("^--file=", "", script_arg[[1]])
} else {
  "scripts/localize-mathjax.R"
}
project_dir <- normalizePath(file.path(dirname(script_path), ".."), mustWork = TRUE)
output_dir <- file.path(project_dir, "docs")
vendor_dir <- file.path(project_dir, "assets", "vendor", "mathjax-3.2.2")
entry_point <- file.path(vendor_dir, "es5", "tex-chtml-full.js")
license_file <- file.path(vendor_dir, "LICENSE")

if (!file.exists(entry_point) || !file.exists(license_file)) {
  stop(
    "Pinned MathJax runtime or licence is missing under assets/vendor/mathjax-3.2.2.",
    call. = FALSE
  )
}

html_files <- list.files(
  output_dir,
  pattern = "\\.html$",
  recursive = TRUE,
  full.names = TRUE
)
if (!length(html_files)) {
  stop("No rendered HTML files found under ", output_dir, call. = FALSE)
}

polyfill_pattern <- paste0(
  "[[:space:]]*<script src=\"https://cdnjs\\.cloudflare\\.com/polyfill/v3/",
  "polyfill\\.min\\.js\\?features=es6\"></script>"
)
remote_math_pattern <- paste0(
  "https?://[^\"']*(?:mathjax|tex-chtml|polyfill/v3/polyfill\\.min\\.js)[^\"']*"
)
mathjax_script_pattern <- paste0(
  "(<script src=\")[^\"]*(?:mathjax@3/es5/)?tex-chtml-full\\.js",
  "(\" type=\"text/javascript\"></script>)"
)

rewritten <- 0L
formula_pages <- character()

for (html_file in html_files) {
  original <- paste(readLines(html_file, warn = FALSE, encoding = "UTF-8"), collapse = "\n")
  if (!grepl("tex-chtml-full\\.js", original, perl = TRUE)) next

  relative_file <- substring(
    normalizePath(html_file, mustWork = TRUE),
    nchar(normalizePath(output_dir, mustWork = TRUE)) + 2L
  )
  depth <- length(strsplit(dirname(relative_file), "/", fixed = TRUE)[[1]])
  if (identical(dirname(relative_file), ".")) depth <- 0L
  local_url <- paste0(
    paste(rep("../", depth), collapse = ""),
    "assets/vendor/mathjax-3.2.2/es5/tex-chtml-full.js"
  )

  updated <- gsub(polyfill_pattern, "", original, perl = TRUE)
  updated <- gsub(
    mathjax_script_pattern,
    paste0("\\1", local_url, "\\2"),
    updated,
    perl = TRUE
  )

  if (grepl(remote_math_pattern, updated, perl = TRUE, ignore.case = TRUE)) {
    stop("Remote math dependency remains in ", relative_file, call. = FALSE)
  }
  if (!grepl(local_url, updated, fixed = TRUE)) {
    stop("Local MathJax entry point was not installed in ", relative_file, call. = FALSE)
  }

  formula_pages <- c(formula_pages, relative_file)
  if (!identical(updated, original)) {
    writeLines(updated, html_file, useBytes = TRUE)
    rewritten <- rewritten + 1L
  }
}

if (!length(formula_pages)) {
  message("No MathJax page was present in this rendered output set.")
} else {
  message(
    "Verified ", length(formula_pages),
    " local MathJax page(s); rewrote ", rewritten,
    " rendered file(s)."
  )
}
