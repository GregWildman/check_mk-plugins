# Gamatronic UPS/Rectifiers

# Create metric and graph for 'rectifier_current' metric
metric_info["rectifier_current"] = {
    "title" : _("Rectifier Current"),
    "unit"  : "a",
    "color" : "#ffb030",
}

graph_info["rectifier_current"] = {
    "title" : _("Electrical Current - Rectifier"),
    "metrics" : [
        ("rectifier_current", "area"),
    ]
}


# Create metric and graph for 'load_current' metric
metric_info["load_current"] = {
    "title" : _("Load Current"),
    "unit"  : "a",
    "color" : "#ffb030",
}

graph_info["load_current"] = {
    "title" : _("Electrical Current - Load"),
    "metrics" : [
        ("load_current", "area"),
    ]
}



check_metrics["check_mk-gamatronic_rectifier"] = {
    "rectifier_current" : { "name" : "rectifier_current" },
    "load_current"      : { "name" : "load_current" }
}

# Fin.
