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

# Perf data: intracom_chassis
# output_power=20.9dBm;;;;

def perfometer_check_mk_intracom_chassis(row, check_command, perf_data):
    dbm = float(perf_data[0][1])
    return "%.1f dBm" % dbm, perfometer_logarithmic(dbm, 50, 2, "#2080c0")

perfometers["check_mk-intracom_chassis"] = perfometer_check_mk_intracom_chassis



def perfometer_check_mk_if_intracom(row, check_command, perf_data):
    unit = "Bit" if  "Bit/s" in row["service_plugin_output"] else "B"
    return perfometer_bandwidth(
        in_traffic  = savefloat(perf_data[0][1]),
        out_traffic = savefloat(perf_data[1][1]),
#        in_bw     = savefloat(perf_data[0][6]),
#        out_bw    = savefloat(perf_data[1][6]),
        in_bw     = float(125000000),
        out_bw    = float(125000000),
        unit      = unit
    )

#perfometers["check_mk-intracom_eth"] = perfometer_check_mk_if
perfometers["check_mk-intracom_eth"] = perfometer_check_mk_if_intracom

# Fin.

