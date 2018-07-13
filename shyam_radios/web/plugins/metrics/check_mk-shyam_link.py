
metric_info["signal_quality"] = {
    "title" : _("Signal_quality"),
    "unit"  : "%",
    "color" : "31/b",
}

perfometer_info.append({
    "type"     : "linear",
    "segments" : [ "signal_quality" ],
    "total"    : 100,
})

graph_info["signal_quality"] = {
    "title" : _("Signal Quality of link"),
    "metrics" : [
        ("signal_quality", "area"),
    ]
}

check_metrics["check_mk-shyam_link"] = {
    "quality"   : { "name" : "signal_quality" }
}

