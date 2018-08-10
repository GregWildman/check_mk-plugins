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

# Radwin 5000 HSB series radio
# Extract the peer radio IP from the service detail. Present a icon to open this
# peers web interface. Using default user/pass for website. Change to suit.
#
# Example plugin_output
# OK - [GP3127 & vlan GP3133 - Joe Soap cc] (syncRegistered) MAC: 00:15:67:5E:6E:82, IP: 10.10.70.34, Timeslots: 4/4, Range: 3450m

def paint_rw5k_peer_radio_icon(what, row, tags, custom_vars):
    if what == 'service' and row['service_description'].startswith('HSU '):
        peer_ip = row['service_plugin_output'].split(",")[1][5:]
        url = 'http://operator:public@%s/mobile/monitor.asp' % peer_ip
        return u'<a href="%s" title="Peer Radio Web Interface" target="_blank">' \
               '<img class=icon src="images/icon_www.png"/>Open terminal station web interface</a>' % (url)

multisite_icons.append({
    'paint':           paint_rw5k_peer_radio_icon,
    'host_columns':    [ 'address' ],
    'service_columns': [ 'host_address', 'plugin_output' ],
})

# Fin.

