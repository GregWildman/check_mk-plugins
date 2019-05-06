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

# Perf data: mikrotik_queue
# in=6652.000000;;;; out=6456.750000;;;; inpkts=17.750000;;;; outpkts=20.750000;;;; indrop=0.000000;;;; outdrop=0.000000;;;; inpcq=0.000000;;;; outpcq=0.000000;;;;

def perfometer_check_mk_mikrotik_queue(row, check_command, perf_data):
    unit = "Bit" if  "bit/s" in row["service_plugin_output"] else "B"
    return perfometer_bandwidth(
        in_traffic  = savefloat(perf_data[0][1]),
        out_traffic = savefloat(perf_data[1][1]),
        in_bw     = 0,
        out_bw    = 0,
        unit      = unit
    )

perfometers["check_mk-mikrotik_queue"] = perfometer_check_mk_mikrotik_queue

# Fin.

