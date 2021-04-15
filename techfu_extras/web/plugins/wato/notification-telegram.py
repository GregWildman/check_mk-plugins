#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-
# +------------------------------------------------------------------+
# |             ____ _               _        __  __ _  __           |
# |            / ___| |__   ___  ___| | __   |  \/  | |/ /           |
# |           | |   | '_ \ / _ \/ __| |/ /   | |\/| | ' /            |
# |           | |___| | | |  __/ (__|   <    | |  | | . \            |
# |            \____|_| |_|\___|\___|_|\_\___|_|  |_|_|\_\           |
# |                                                                  |
# | Copyright Mathias Kettner 2014             mk@mathias-kettner.de |
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

import cmk.utils.version as cmk_version
import cmk.gui.config as config
from cmk.gui.i18n import _
from cmk.gui.globals import html

from cmk.gui.valuespec import (
    DEF_VALUE,
    Dictionary,
    FixedValue,
    Password,
    TextAreaUnicode,
    TextAscii,
    TextUnicode,
)

from cmk.gui.plugins.wato import (
    notification_parameter_registry,
    NotificationParameter,
    passwordstore_choices,
    IndividualOrStoredPassword,
)

from cmk.gui.plugins.wato.utils import (
    PasswordFromStore,)

@notification_parameter_registry.register
class NotificationParameterTelegramGraphs(NotificationParameter):
    @property
    def ident(self):
        return "telegram"

    @property
    def spec(self):
        return Dictionary(
            title=_("Create notification with the following parameters"),
            optional_keys=["api_url", "host_desc", "svc_desc", "host_msg", "svc_msg", "ignore_graphs"],
            required_keys=["bot_token"],
            elements = [
                ("bot_token",
                 PasswordFromStore(
                     title = _("BOT Token"),
                     help = _("You need to provide a valid BOT token to be able to send notifications using Telegram. "
                              "For information see <a href=\"https://core.telegram.org/bots#create-a-new-bot\" "
                              "target=\"_blank\">Bots: An introduction for developers</a>"),
                     size = 58,
                     allow_empty = False,
                )),
                ("api_url",
                 TextAscii(
                     title = _("API Endpoint"),
                     help = _("Telegram API endpoint URL. Do <tt>not</tt> change unless you know what you are doing."),
                     default_value = "https://api.telegram.org",
                )),
                ("host_desc",
                 TextUnicode(
                     title=_("Description for host alerts"),
                     help=_("Description field of host alert that is generally "
                            "used to provide a detailed information about the "
                            "alert."),
                     default_value="Check_MK: $HOSTNAME$ - $EVENT_TXT$",
                     size=64,
                 )),
                ("svc_desc",
                 TextUnicode(
                     title=_("Description for service alerts"),
                     help=_("Description field of service alert that is generally "
                            "used to provide a detailed information about the "
                            "alert."),
                     default_value="Check_MK: $HOSTNAME$/$SERVICEDESC$ $EVENT_TXT$",
                     size=68,
                 )),
                ("host_msg",
                 TextAreaUnicode(
                     title=_("Message for host alerts"),
                     rows=8,
                     cols=58,
                     monospaced=True,
                     default_value="""```
Host:    $HOSTNAME$
Alias:   $HOSTALIAS$
Address: $HOSTADDRESS$
Event:   $EVENT_TXT$
Output:  $HOSTOUTPUT$
```""")),
                ("svc_msg",
                 TextAreaUnicode(
                     title=_("Message for service alerts"),
                     rows=11,
                     cols=58,
                     monospaced=True,
                     default_value="""```
Host:     $HOSTNAME$
Alias:    $HOSTALIAS$
Address:  $HOSTADDRESS$
Service:  $SERVICEDESC$
Event:    $EVENT_TXT$
Output:   $SERVICEOUTPUT$
```""")),
                ("ignore_graphs",
                 FixedValue(
                     False,
                     title=_("Disable attaching graphs for PROBLEM and CUSTOM types"),
                     totext=_("Disable attaching graphs for PROBLEM and CUSTOM types"),
                     help=_("Do not attach graphs of the host or service for PROBLEM and CUSTOM notification types."),
                 )),

                ])

        return Dictionary(title=_("Create notification with the following parameters"),
                          elements=elements)

