# Shared DataTables interface labels for every Introduction to Statistics topic.
# Topic pages set `topic_locale` before calling `topic_dt_options()`. Keeping the
# labels here prevents an interactive table from silently reverting to English
# when the learner is reading the German or Albanian version.

topic_dt_language <- function(locale = "en") {
  language_sets <- list(
    en = list(
      decimal = ".",
      thousands = ",",
      emptyTable = "No data available in this table",
      info = "Showing _START_ to _END_ of _TOTAL_ entries",
      infoEmpty = "Showing 0 to 0 of 0 entries",
      infoFiltered = "(filtered from _MAX_ total entries)",
      loadingRecords = "Loading...",
      processing = "Processing...",
      search = "Search:",
      zeroRecords = "No matching records found",
      paginate = list(
        first = "First",
        previous = "Previous",
        `next` = "Next",
        last = "Last"
      ),
      aria = list(
        sortAscending = ": activate to sort the column in ascending order",
        sortDescending = ": activate to sort the column in descending order"
      )
    ),
    de = list(
      decimal = ".",
      thousands = ",",
      emptyTable = "Keine Daten in dieser Tabelle verfügbar",
      info = "Einträge _START_ bis _END_ von _TOTAL_",
      infoEmpty = "Einträge 0 bis 0 von 0",
      infoFiltered = "(gefiltert aus insgesamt _MAX_ Einträgen)",
      loadingRecords = "Daten werden geladen...",
      processing = "Daten werden verarbeitet...",
      search = "Suchen:",
      zeroRecords = "Keine passenden Einträge gefunden",
      paginate = list(
        first = "Erste",
        previous = "Zurück",
        `next` = "Weiter",
        last = "Letzte"
      ),
      aria = list(
        sortAscending = ": aktivieren, um die Spalte aufsteigend zu sortieren",
        sortDescending = ": aktivieren, um die Spalte absteigend zu sortieren"
      )
    ),
    sq = list(
      decimal = ".",
      thousands = ",",
      emptyTable = "Nuk ka të dhëna në këtë tabelë",
      info = "Po shfaqen rreshtat _START_ deri në _END_ nga _TOTAL_ gjithsej",
      infoEmpty = "Nuk ka rreshta për t'u shfaqur",
      infoFiltered = "(filtruar nga _MAX_ rreshta gjithsej)",
      loadingRecords = "Të dhënat po ngarkohen...",
      processing = "Të dhënat po përpunohen...",
      search = "Kërko:",
      zeroRecords = "Nuk u gjet asnjë rresht që përputhet",
      paginate = list(
        first = "E para",
        previous = "E mëparshmja",
        `next` = "Tjetra",
        last = "E fundit"
      ),
      aria = list(
        sortAscending = ": aktivizo për ta renditur kolonën në rritje",
        sortDescending = ": aktivizo për ta renditur kolonën në zbritje"
      )
    )
  )

  if (!locale %in% names(language_sets)) {
    stop("Unsupported DataTables locale: ", locale, call. = FALSE)
  }

  language_sets[[locale]]
}

topic_dt_options <- function(
  locale = "en",
  page_length = 10,
  dom = "ftip",
  auto_width = FALSE,
  ...
) {
  base_options <- list(
    pageLength = page_length,
    dom = dom,
    autoWidth = auto_width,
    language = topic_dt_language(locale)
  )

  utils::modifyList(base_options, list(...))
}
