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

## PPP Sessions
metric_info["sessions"] = {
    "title" : _("Active Sessions"),
    "unit"  : "count",
    "color" : "21/a",
}



# Fin.

