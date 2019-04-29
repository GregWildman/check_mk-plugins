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

telegram_notification_dict =  Dictionary(
    optional_keys = None,
    elements = [
        ("bot_token", TextAscii(
            title = _("BOT Token"),
            help = _("You need to provide a valid BOT token to be able to send notifications using Telegram. "
                     "For information see <a href=\"https://core.telegram.org/bots#create-a-new-bot\" "
                     "target=\"_blank\">Bots: An introduction for developers</a>"),
            size = 40,
            allow_empty = False,
            regex = "[a-zA-Z0-9:-_]{40,50}",
        )),
        ("api_url", TextAscii(
            title = _("API Endpoint"),
            help = _("Telegram API endpoint URL. Do <tt>not</tt> change unless you know what you are doing."),
            default_value = "https://api.telegram.org"
        )),
    ]
)

register_notification_parameters("telegram", telegram_notification_dict)
register_notification_parameters("telegram-graphs", telegram_notification_dict)

