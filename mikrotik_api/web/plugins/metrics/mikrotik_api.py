#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.
      
from cmk.gui.i18n import _        
                                  
from cmk.gui.plugins.metrics import (
    metric_info,)                 

#.
#   .--Metrics-------------------------------------------------------------.
#   |                   __  __      _        _                             |
#   |                  |  \/  | ___| |_ _ __(_) ___ ___                    |
#   |                  | |\/| |/ _ \ __| '__| |/ __/ __|                   |
#   |                  | |  | |  __/ |_| |  | | (__\__ \                   |
#   |                  |_|  |_|\___|\__|_|  |_|\___|___/                   |
#   |                                                                      |
#   +----------------------------------------------------------------------+
#   |  Definitions of metrics                                              |
#   '----------------------------------------------------------------------'

# Title are always lower case - except the first character!
# Colors: See indexed_color() in cmk/gui/plugins/metrics/utils.py

## Firewall
metric_info["bps"] = {
    "title" : _("Bandwidth"),
    "unit"  : "bits/s",
    "color" : "#00e060",
}

metric_info["packetsps"] = {
    "title" : _("Packets/s"),
    "unit"  : "1/s",
    "color" : "31/a",
}

## BGP Peers
metric_info["prefix_count"] = {
    "title" : _("Prefixes"),
    "unit"  : "count",
    "color" : "#00e060",
}
# ROSv6
metric_info["updates_sent"] = {
    "title" : _("Updates Sent"),
    "unit"  : "count",
    "color" : "34/a",
}
metric_info["updates_received"] = {
    "title" : _("Updates Received"),
    "unit"  : "count",
    "color" : "41/a",
}
# ROSv7
metric_info["local_messages"] = {
    "title" : _("Updates Sent"),
    "unit"  : "count",
    "color" : "34/a",
}
metric_info["remote_messages"] = {
    "title" : _("Updates Received"),
    "unit"  : "count",
    "color" : "41/a",
}

# ROS6
metric_info["withdrawn_sent"] = {
    "title" : _("Withdrawn Sent"),
    "unit"  : "count",
    "color" : "11/a",
}
metric_info["withdrawn_received"] = {
    "title" : _("Withdrawn Received"),
    "unit"  : "count",
    "color" : "13/a",
}
# ROS7
metric_info["local_bytes"] = {
    "title" : _("Traffic Sent"),
    "unit"  : "bytes/s",
    "color" : "11/a",
}
metric_info["remote_bytes"] = {
    "title" : _("Traffic Received"),
    "unit"  : "bytes/s",
    "color" : "13/a",
}

## PPP Sessions
metric_info["sessions"] = {
    "title" : _("Active Sessions"),
    "unit"  : "count",
    "color" : "21/a",
}

## Radius servers
## 'requests' are already handled in CMK
metric_info["pending"] = {
    "title" : _("Requests Pending"),
    "unit"  : "count",
    "color" : "21/a",
}
metric_info["accepts"] = {
    "title" : _("Request Accepted"),
    "unit"  : "count",
    "color" : "21/a",
}
metric_info["rejects"] = {
    "title" : _("Request Rejected"),
    "unit"  : "count",
    "color" : "21/a",
}
metric_info["resends"] = {
    "title" : _("Request Resends"),
    "unit"  : "count",
    "color" : "21/a",
}
metric_info["timeouts"] = {
    "title" : _("Requests Timeouts"),
    "unit"  : "count",
    "color" : "21/a",
}
metric_info["bad_replies"] = {
    "title" : _("Bad Replies"),
    "unit"  : "count",
    "color" : "21/a",
}



# Fin.

