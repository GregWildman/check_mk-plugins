# Alcoma ALMP

check_metrics["check_mk-alcoma_almp.line"] = if_translation

check_metrics["check_mk-alcoma_almp.odu"] = {
    "output_power" : { "name" : "output_signal_power_dbm" },
    "input_power"  : { "name" : "input_signal_power_dbm" },
    "snr"          : { "name" : "signal_noise" }
}

