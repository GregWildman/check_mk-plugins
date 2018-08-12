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


# Create new metrics
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

# link_rx=-66.0dBm;;;; link_tx=18.0dBm;;;;
check_metrics["check_mk-radwin_2000"] = {
    "link_tx" : { "name" : "output_signal_power_dbm" },
    "link_rx" : { "name" : "input_signal_power_dbm" }
}

# hsu_rss=-56.0dBm;;;;
check_metrics["check_mk-radwin_5000_cpe"] = {
    "hsu_rss" : { "name" : "input_signal_power_dbm" }
}

# Create metrics + graph template
# sats=9;;;;
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

# hbs_rss=-75.0dBm;;;; hsu_rss=-67.0dBm;;;;
check_metrics["check_mk-radwin_5000"] = {
    "hbs_rss" : { "name" : "output_signal_power_dbm" },
    "hsu_rss" : { "name" : "input_signal_power_dbm" }
}

# Fin.

