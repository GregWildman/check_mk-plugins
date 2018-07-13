# in=60518.909091;;;0;88064 out=1248366.090909;;;0;147456 inpkts=519.818182;;;; outpkts=944.454545;;;; rx_strength=-56.0dBm;;;; tx_strength=-52.0dBm;;;;

mikrotik_wiresless_clients_if_translation = {
    "in"          : { "name": "if_in_bps", "scale": 8 },
    "out"         : { "name": "if_out_bps", "scale": 8 },
    "inpkts"      : { "name": "if_in_unicast" },
    "outpkts"     : { "name": "if_out_unicast" },
    "tx_strength" : { "name" : "output_signal_power_dbm" },
    "rx_strength" : { "name" : "input_signal_power_dbm" }
}

check_metrics["check_mk-mikrotik_wireless_clients"] = mikrotik_wiresless_clients_if_translation

