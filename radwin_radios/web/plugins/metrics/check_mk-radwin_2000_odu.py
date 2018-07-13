# UAS=0;;;; ES=0.761194;;;; SRS=0;;;; BBE=2.19403;;;;

metric_info["unavailable_seconds"] = {
    "title" : _("Unavailable Seconds"),
    "unit"  : "",
    "color" : "41/b",
}

metric_info["errored_seconds"] = {
    "title" : _("Errored Seconds"),
    "unit"  : "",
    "color" : "45/b",
}

metric_info["severely_errored_seconds"] = {
    "title" : _("Severely Errored Seconds"),
    "unit"  : "",
    "color" : "22/b",
}

metric_info["background_block_errors"] = {
    "title" : _("Background Block Errors"),
    "unit"  : "",
    "color" : "31/b",
}

check_metrics["check_mk-radwin_2000_odu"] = {
    "UAS"   : { "name" : "unavailable_seconds" },
    "ES"    : { "name" : "errored_seconds" },
    "SRS"   : { "name" : "severely_errored_seconds" },
    "BBE"   : { "name" : "background_block_errors" },
}

