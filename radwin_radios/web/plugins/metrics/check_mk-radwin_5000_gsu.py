
unit_info["sats"] = {
    "title"    : _("Satellites"),
    "symbol"   : "",
    "render"   : lambda v: "%s sats" % (metric_number_with_precision(v, drop_zeroes=True)),
    "stepping" : "integer", # for vertical graph labels
}

metric_info["satellites"] = {
    "title" : _("Satellites"),
    "unit"  : "sats",
    "color" : "31/b",
}

perfometer_info.append({
    "type"     : "linear",
    "segments" : [ "satellites" ],
    "total"    : 14,
})

graph_info["satellites"] = {
    "title" : _("Satellites with Lock"),
    "metrics" : [
        ("satellites", "area"),
    ]
}

check_metrics["check_mk-radwin_5000_gsu"] = {
    "sats"   : { "name" : "satellites" }
}

