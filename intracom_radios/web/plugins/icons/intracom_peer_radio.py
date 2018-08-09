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

# Extract the peer radio IP from the service detail. Present a icon to open this
# peers web interface.
#
# Example plugin_output
# OK - connected, IP: 10.12.42.17, MAC: 00:05:59:74:0E:7C, dl: 128q  ul: 128q, RSSI (dBm) dl: -67.57 ul: -68.16, Distance: 9966m

def paint_peer_radio_icon(what, row, tags, custom_vars):
    if what == 'service' and row['service_description'].startswith('TS '):
        peer_ip = row['service_plugin_output'].split(",")[1][5:]
        url = 'http://%s/' % peer_ip
        return u'<a href="%s" title="Peer Radio Web Interface" target="_blank">' \
               '<img class=icon src="images/icon_www.png"/>Open terminal station web interface</a>' % (url)

multisite_icons.append({
    'paint':           paint_peer_radio_icon,
    'host_columns':    [ 'address' ],
    'service_columns': [ 'host_address', 'plugin_output' ],
})

# Fin.

