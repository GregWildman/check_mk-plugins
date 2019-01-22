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

# (in=2797568.000000;;;0;125000000 out=188544.000000;;;0;125000000 inpkts=3024.000000;;;; outpkts=528.000000;;;;)
check_metrics["check_mk-intracom_eth"] = {
    "in"        : { "name": "if_in_bps", "scale": 8 },
    "out"       : { "name": "if_out_bps", "scale": 8 },
    "inpkts"    : { "name": "if_in_pkts" },
    "outpkts"   : { "name": "if_out_pkts" },
}

metric_info["if_in_pkts"] = {
    "title" : _("Input unicast packets"),
    "unit"  : "1/s",
    "color" : "#00ffc0",
}

metric_info["if_out_pkts"] = {
    "title" : _("Output unicast packets"),
    "unit"  : "1/s",
    "color" : "#00c0ff",
}

graph_info["packets_intracom"] = {
    "title" : _("Packets"),
    "metrics" : [
        ( "if_in_pkts",  "area" ),
        ( "if_out_pkts", "-area" ),
    ],
}


# output_power=-68.8dBm;;;; input_power=-64.8dBm;;;;
check_metrics["check_mk-intracom_bsts"] = {
    "output_power" : { "name" : "output_signal_power_dbm" },
    "input_power"  : { "name" : "input_signal_power_dbm" }
}

# input_power=-78.3dBm;;;; snr=20.6dBm;;;;
check_metrics["check_mk-intracom_cpe"] = {
    "input_power"  : { "name" : "input_signal_power_dbm" },
    "snr"          : { "name" : "signal_noise" }
}

# output_power=21.4dBm;;;;
check_metrics["check_mk-intracom_chassis"] = {
    "output_power" : { "name" : "output_signal_power_dbm" }
}

# Fin.

