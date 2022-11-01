#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# +------------------------------------------------------------------+
# |             ____ _               _        __  __ _  __           |
# |            / ___| |__   ___  ___| | __   |  \/  | |/ /           |
# |           | |   | '_ \ / _ \/ __| |/ /   | |\/| | ' /            |
# |           | |___| | | |  __/ (__|   <    | |  | | . \            |
# |            \____|_| |_|\___|\___|_|\_\___|_|  |_|_|\_\           |
# |                                                                  |
# | Copyright Mathias Kettner 2014             mk@mathias-kettner.de |
# +------------------------------------------------------------------+

# this file is part of mkp package "mikrotik_api"
# see package description and ~/local/share/doc/check_mk/mikrotik_api
# for details and maintainer
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

from typing import Any, Dict, List, Optional

import cmk.gui.bi as bi
import cmk.gui.watolib as watolib
from cmk.gui.exceptions import MKUserError
from cmk.gui.i18n import _
from cmk.gui.plugins.wato import (
    HostRulespec,
    monitoring_macro_help,
    rulespec_group_registry,
    rulespec_registry,
    RulespecGroup,
    RulespecSubGroup,
)
from cmk.gui.valuespec import (
    Dictionary,
    DropdownChoice,
    Integer,
    ListChoice,
    TextAscii,
    Transform,
)
from cmk.gui.plugins.wato import (
    passwordstore_choices,
    IndividualOrStoredPassword,
)
from cmk.gui.plugins.wato.utils import (
    PasswordFromStore,
)


@rulespec_group_registry.register
class RulespecGroupDatasourcePrograms(RulespecGroup):
    @property
    def name(self):
        return "datasource_programs"

    @property
    def title(self):
        return _("Other integrations")

    @property
    def help(self):
        return _("Integrate platforms using special agents, e.g. SAP R/3")

@rulespec_group_registry.register
class RulespecGroupDatasourceProgramsHardware(RulespecSubGroup):
    @property
    def main_group(self):
        return RulespecGroupDatasourcePrograms

    @property
    def sub_group_name(self):
        return "hw"

    @property
    def title(self):
        return _("Hardware")

def _valuespec_special_agents_mikrotik_api():
    return Dictionary(
        title = _("MikroTik RouterOS via API"),
        help=_("This rule set selects the special agent for Mikrotik Routerboards "
               "instead of the normal Check_MK agent and allows monitoring via API."),
        optional_keys=False,
        elements=[
            ("user", TextAscii(title=_("Username"), allow_empty=False)),
            ("password", PasswordFromStore(title=_("Password"), size=58, allow_empty=False)),
            ("nossl",
             DropdownChoice(title=_("Connection type"),
                            default_value = False,
                            choices=[
                                (True, _("Do not use SSL to connect to API")),
                                (False, _("Use SSL (Default)")),
                            ])),
            ("connect",
             Integer(title = _("TCP Port number"),
                     help = _("Port number for connection to API. Usually 8729 (SSL) "
                              "or 8728 (no SSL)"),
                     default_value = 8729,
                     minvalue = 1,
                     maxvalue = 65535,
              )),
            ("infos",
             Transform(
                 ListChoice(
                     choices=[
                         ( "resource",     _("CPU, Memory, Storage and Uptime")),
                         ( "interface",    _("Network Interfaces")),
                         ( "bgp",          _("BGP sessions")),
                         ( "ospf",         _("OSPF Neighbours")),
                         ( "vrrp",         _("VRRP info")),
                         ( "health",       _("Health")),
                         ( "board",        _("Device Info")),
                         ( "ipsec",        _("IPsec")),
                         ( "ntp",          _("NTP")),
                         ( "firewall",     _("Firewall rules")),
                         ( "firewallv6",   _("Firewall rules IPv6")),
                         ( "certificates", _("Certificate expirations")),
                         ( "ppp",          _("PPP Sessions") ),
                         ( "radius",       _("Radius") ),
                     ],
                     default_value=["resource", "interface", "health", "board"],
                     allow_empty=False,
                 ),
                 title = _("Retrieve information about..."),
            )),
        ],
    )


rulespec_registry.register(
    HostRulespec(
        group=RulespecGroupDatasourceProgramsHardware,
        name="special_agents:mikrotik_api",
        valuespec=_valuespec_special_agents_mikrotik_api,
    ))





