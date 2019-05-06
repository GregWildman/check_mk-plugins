#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-
# +------------------------------------------------------------------+
# |             ____ _               _        __  __ _  __           |
# |            / ___| |__   ___  ___| | __   |  \/  | |/ /           |
# |           | |   | '_ \ / _ \/ __| |/ /   | |\/| | ' /            |
# |           | |___| | | |  __/ (__|   <    | |  | | . \            |
# |            \____|_| |_|\___|\___|_|\_\___|_|  |_|_|\_\           |
# |                                                                  |
# | Copyright Mathias Kettner 2018             mk@mathias-kettner.de |
# +------------------------------------------------------------------+
#
# This file is part of Check_MK.
# The official homepage is at http://mathias-kettner.de/check_mk.
#
# check_mk is free software;  you can redistribute it and/or modify it
# under the  terms of the  GNU General Public License  as published by
# the Free Software Foundation in version 2.  check_mk is  distributed
# in the hope that it will be useful, but WITHOUT ANY WARRANTY;  with-
# out even the implied warranty of  MERCHANTABILITY  or  FITNESS FOR A
# PARTICULAR PURPOSE. See the  GNU General Public License for more de-
# tails. You should have  received  a copy of the  GNU  General Public
# License along with GNU Make; see the file  COPYING.  If  not,  write
# to the Free Software Foundation, Inc., 51 Franklin St,  Fifth Floor,
# Boston, MA 02110-1301 USA.

# Techfu / Greg Wildman <greg.wildman@techfu.co.za> - 2018

# ppp_sessions=223;;;;
check_metrics["check_mk-mikrotik_aaa"] = {
    "ppp_sessions" : { "name" : "active_sessions" }
}


# in_voltage=17.9;;;;
check_metrics["check_mk-mikrotik_health.voltage"] = {
    "in_voltage"   : { "name" : "voltage" }
}


# input_power=-3.7dBm;;;; output_power=-2.5dBm;;;;
check_metrics["check_mk-mikrotik_optical"] = {
    "output_power" : { "name" : "output_signal_power_dbm" },
    "input_power"  : { "name" : "input_signal_power_dbm" }
}


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


# mikrotik_queue
# (in=7311.400000;;;; out=4136.800000;;;; inpkts=7311.400000;;;; outpkts=4136.800000;;;; indisc=3830356.000000;;;; outdisc=8898.000000;;;; inpcq=0.000000;;;; outpcq=0.000000;;;;)
metric_info["in_pcq_substreams"] = {
    "title" : _("Downlod PCQ Substreams"),
    "unit"  : "1/s",
    "color" : "41/b",
}

metric_info["out_pcq_substreams"] = {
    "title" : _("Upload PCQ Substreams"),
    "unit"  : "1/s",
    "color" : "45/b",
}

metric_info["in_dropped_pkts"] = {
    "title" : _("Download Packets Dropped"),
    "unit": "1/s",
    "color": "#ff8000"
}

metric_info["out_dropped_pkts"] = {
    "title" : _("Upload Packets Dropped"),
    "unit": "1/s",
    "color": "#ff8080"
}

graph_info["pcq_substreams"] = {
    "title" : _("PCQ Substreams"),
    "metrics" : [
        ("out_pcq_substreams", "-area"),
        ("in_pcq_substreams", "area"),
    ]
}

graph_info["packets_dropped"] = {
    "title" : _("Packets Dropped"),
    "metrics" : [
        ("out_dropped_pkts", "-area"),
        ("in_dropped_pkts", "area"),
    ]
}

mikrotik_queue_if_translation = {
    "in"          : { "name": "if_in_bps", "scale": 8 },
    "out"         : { "name": "if_out_bps", "scale": 8 },
    "inpkts"      : { "name": "if_in_pkts" },
    "outpkts"     : { "name": "if_out_pkts" },
    "indrop"      : { "name": "in_dropped_pkts" },
    "outdrop"     : { "name": "out_dropped_pkts" },
    "inpcq"       : { "name": "in_pcq_substreams" },
    "outpcq"      : { "name": "out_pcq_substreams" }
}

check_metrics["check_mk-mikrotik_queue"] = mikrotik_queue_if_translation


# Fin.

