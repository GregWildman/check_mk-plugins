# in=378935.231579;;;0;125000000 inucast=610.184834;;;; innucast=31.442246;;;; indisc=0.0933;;;; inerr=0;0.01;0.1;; out=375237.268903;;;0;125000000 outucast=708.710092;;;; outnucast=196.117511;;;; outdisc=0;;;; outerr=0;0.01;0.1;; outqlen=0;;;0;

intracom_if_translation = {
    "in"        : { "name": "if_in_bps", "scale": 8 },
    "out"       : { "name": "if_out_bps", "scale": 8 },
    "indisc"    : { "name": "if_in_discards" },
    "inerr"     : { "name": "if_in_errors" },
    "outdisc"   : { "name": "if_out_discards" },
    "outerr"    : { "name": "if_out_errors" },
    "inucast"   : { "name": "if_in_unicast" },
    "innucast"  : { "name": "if_in_non_unicast" },
    "outucast"  : { "name": "if_out_unicast" },
    "outnucast" : { "name": "if_out_non_unicast" },
}

check_metrics["check_mk-intracom_eth"] = intracom_if_translation

