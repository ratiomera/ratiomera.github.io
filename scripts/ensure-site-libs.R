#!/usr/bin/env Rscript

# Quarto can perform a narrow preview render while a complete website build is
# present in docs/. In that situation it may prune shared files that the narrow
# input did not itself use. A cloud provider can also reconcile selected R
# htmlwidget bindings out of docs/site_libs after Quarto exits. Keep those
# widget dependencies in a source-owned vendor tree, rewrite their rendered
# URLs to that stable namespace, and then restore/verify any remaining Quarto
# site_libs dependencies from the current render cache.

script_arg <- grep("^--file=", commandArgs(trailingOnly = FALSE), value = TRUE)
script_path <- if (length(script_arg)) {
  sub("^--file=", "", script_arg[[1]])
} else {
  "scripts/ensure-site-libs.R"
}
project_dir <- normalizePath(file.path(dirname(script_path), ".."), mustWork = TRUE)
output_dir <- file.path(project_dir, "docs")
cache_dir <- file.path(project_dir, ".quarto", "_freeze", "site_libs")
vendor_source_dir <- file.path(project_dir, "assets", "vendor", "r-widgets")
vendor_output_dir <- file.path(output_dir, "assets", "vendor", "r-widgets")

widget_dependencies <- c(
  "htmltools-fill-0.5.9/fill.css",
  "htmlwidgets-1.6.4/htmlwidgets.js",
  "datatables-css-0.0.0/datatables-crosstalk.css",
  "datatables-binding-0.34.0/datatables.js",
  "jquery-3.6.0/jquery-3.6.0.min.js",
  "dt-core-1.13.6/css/jquery.dataTables.min.css",
  "dt-core-1.13.6/css/jquery.dataTables.extra.css",
  "dt-core-1.13.6/js/jquery.dataTables.min.js",
  "crosstalk-1.2.2/css/crosstalk.min.css",
  "crosstalk-1.2.2/js/crosstalk.min.js",
  "plotly-binding-4.11.0/plotly.js",
  "typedarray-0.1/typedarray.min.js",
  "plotly-htmlwidgets-css-2.11.1/plotly-htmlwidgets.css",
  "plotly-main-2.11.1/plotly-latest.min.js"
)

is_nonempty_file <- function(path) {
  info <- file.info(path)
  isTRUE(
    !is.na(info$isdir) && !info$isdir &&
      !is.na(info$size) && info$size > 0
  )
}

if (!dir.exists(output_dir)) {
  stop("Rendered output directory does not exist: ", output_dir, call. = FALSE)
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

restored_vendor <- character()
for (relative in widget_dependencies) {
  source_path <- file.path(vendor_source_dir, relative)
  frozen_path <- file.path(cache_dir, relative)
  destination_path <- file.path(vendor_output_dir, relative)

  if (!is_nonempty_file(source_path)) {
    stop("Source-owned widget dependency is missing: ", source_path, call. = FALSE)
  }
  if (is_nonempty_file(frozen_path) && !identical(
    unname(tools::md5sum(source_path)),
    unname(tools::md5sum(frozen_path))
  )) {
    stop(
      "Vendored widget dependency differs from Quarto's versioned cache: ",
      relative,
      call. = FALSE
    )
  }

  destination_complete <- is_nonempty_file(destination_path) && identical(
    unname(tools::md5sum(source_path)),
    unname(tools::md5sum(destination_path))
  )
  if (!destination_complete) {
    dir.create(dirname(destination_path), recursive = TRUE, showWarnings = FALSE)
    copied <- file.copy(
      source_path,
      destination_path,
      overwrite = TRUE,
      copy.mode = TRUE,
      copy.date = FALSE
    )
    if (isTRUE(copied)) {
      Sys.chmod(destination_path, mode = "0644", use_umask = FALSE)
    }
    destination_complete <- isTRUE(copied) && is_nonempty_file(destination_path) && identical(
      unname(tools::md5sum(source_path)),
      unname(tools::md5sum(destination_path))
    )
    if (destination_complete) restored_vendor <- c(restored_vendor, relative)
  }
  if (!destination_complete) {
    stop("Published vendored widget dependency is incomplete: ", relative, call. = FALSE)
  }
}

rewritten_html <- character()
for (html_path in html_files) {
  contents <- paste(
    readLines(html_path, warn = FALSE, encoding = "UTF-8"),
    collapse = "\n"
  )
  rewritten <- contents
  for (relative in widget_dependencies) {
    rewritten <- gsub(
      paste0("site_libs/", relative),
      paste0("assets/vendor/r-widgets/", relative),
      rewritten,
      fixed = TRUE
    )
  }
  if (!identical(rewritten, contents)) {
    writeLines(
      strsplit(rewritten, "\n", fixed = TRUE)[[1]],
      html_path,
      useBytes = TRUE
    )
    Sys.chmod(html_path, mode = "0644", use_umask = FALSE)
    rewritten_html <- c(rewritten_html, html_path)
  }
}

dependency_pattern <- "(?:src|href)=[\"'][^\"']*site_libs/[^\"'?#]+"
referenced_paths <- unique(unlist(lapply(html_files, function(path) {
  contents <- paste(readLines(path, warn = FALSE, encoding = "UTF-8"), collapse = "\n")
  matches <- regmatches(
    contents,
    gregexpr(dependency_pattern, contents, perl = TRUE)
  )[[1]]
  if (!length(matches) || identical(matches, "")) return(character())
  relative <- sub("^.*?site_libs/", "", matches, perl = TRUE)
  utils::URLdecode(relative)
}), use.names = FALSE))

referenced_paths <- referenced_paths[nzchar(referenced_paths)]
if (any(grepl("(^|/)\\.\\.(/|$)", referenced_paths, perl = TRUE))) {
  stop("Unsafe parent-directory segment in a rendered site_libs reference.", call. = FALSE)
}

destination_paths <- file.path(output_dir, "site_libs", referenced_paths)
dependency_is_complete <- function(index) {
  destination_path <- destination_paths[[index]]
  if (!is_nonempty_file(destination_path)) return(FALSE)

  # Versioned R htmlwidget dependencies are available in Quarto's current
  # freeze cache.  When that source exists, require byte identity as well as a
  # nonempty destination so a partially synchronized cloud placeholder cannot
  # make the publication check pass.
  source_path <- file.path(cache_dir, referenced_paths[[index]])
  if (!is_nonempty_file(source_path)) return(TRUE)

  identical(
    unname(tools::md5sum(destination_path)),
    unname(tools::md5sum(source_path))
  )
}

missing_before <- !vapply(
  seq_along(referenced_paths),
  dependency_is_complete,
  logical(1)
)
restored <- character()
unavailable <- character()

for (index in which(missing_before)) {
  relative <- referenced_paths[[index]]
  source_path <- file.path(cache_dir, relative)
  destination_path <- destination_paths[[index]]
  if (!is_nonempty_file(source_path)) {
    unavailable <- c(unavailable, relative)
    next
  }
  dir.create(dirname(destination_path), recursive = TRUE, showWarnings = FALSE)
  copied <- file.copy(
    source_path,
    destination_path,
    overwrite = TRUE,
    copy.mode = TRUE,
    # A fresh timestamp marks this as intentional final output. Preserving an
    # old cache timestamp allowed a cloud provider to reconcile the restored
    # file away shortly after an otherwise successful render.
    copy.date = FALSE
  )
  if (isTRUE(copied)) {
    Sys.chmod(destination_path, mode = "0644", use_umask = FALSE)
  }
  if (!isTRUE(copied) || !dependency_is_complete(index)) {
    unavailable <- c(unavailable, relative)
  } else {
    restored <- c(restored, relative)
  }
}

missing_after <- referenced_paths[!vapply(
  seq_along(referenced_paths),
  dependency_is_complete,
  logical(1)
)]
if (length(unavailable) || length(missing_after)) {
  unresolved <- sort(unique(c(unavailable, missing_after)))
  stop(
    "Rendered HTML references shared dependencies that are unavailable in both docs/site_libs and .quarto/_freeze/site_libs:\n- ",
    paste(unresolved, collapse = "\n- "),
    call. = FALSE
  )
}

if (length(restored)) {
  message(
    "Restored ", length(restored),
    " referenced site_libs file(s) from Quarto's render cache."
  )
} else {
  message(
    "Verified ", length(referenced_paths),
    " referenced site_libs file(s); none were missing."
  )
}

message(
  "Verified ", length(widget_dependencies),
  " source-owned widget dependency file(s); restored ",
  length(restored_vendor), " published copy/copies and rewrote ",
  length(rewritten_html), " HTML file(s) to the stable vendor namespace."
)
