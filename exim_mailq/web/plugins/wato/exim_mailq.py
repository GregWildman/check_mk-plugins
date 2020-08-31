#!/usr/bin/env python
# -*- encoding: utf-8; py-indent-offset: 4 -*-

# Greg Wildman <greg@techno.co.za>

# This is free software;  you can redistribute it and/or modify it
# under the  terms of the  GNU General Public License  as published by
# the Free Software Foundation in version 2.  check_mk is  distributed
# in the hope that it will be useful, but WITHOUT ANY WARRANTY;  with-
# out even the implied warranty of  MERCHANTABILITY  or  FITNESS FOR A
# PARTICULAR PURPOSE. See the  GNU General Public License for more de-
# ails.  You should have  received  a copy of the  GNU  General Public
# License along with GNU Make; see the file  COPYING.  If  not,  write
# to the Free Software Foundation, Inc., 51 Franklin St,  Fifth Floor,
# Boston, MA 02110-1301 USA.

register_check_parameters(
    subgroup_environment,
    "exim_mailq",
    _("Exim Mail Queue"),
    Dictionary(
        title = _('Exim Mail Queue'),
        elements = [
            ( 'length',
            Tuple(
                title = _('Levels for Queue Length'),
                elements = [
                    Integer(title = _("Warning at"), unit = u"Mails", default_value=50),
                    Integer(title = _("Critical at"), unit = u"Mails", default_value=100),
                ],
            )),
            ( 'size',
            Tuple(
                title = _('Size of Queue'),
                elements = [
                    Integer(title = _("Warning at"), unit = u"MiB", default_value=100),
                    Integer(title = _("Critical at"), unit = u"MiB", default_value=200),
                ],
            )),
            ( 'age',
            Tuple(
                title = _('Age of oldest mail in Queue'),
                elements = [
                    Integer(title = _("Warning below"), unit = u"Min", default_value=1440),
                    Integer(title = _("Critical below"), unit = u"Min", default_value=2160),
                ],
            )),
        ],
    ),
    TextAscii(title = _("Exim instance")),
    match_type = "dict",
)

register_rule("agents/" + _("Agent Plugins"),
    "agent_config:exim_mailq",
    DropdownChoice(
        title = _("Exim Mail Queue (Linux)"),
        help = _("Deploy the agent plugin <tt>exim_mailq</tt>."),
        choices = [
            ( True, _("Deploy Exim Mail Queue plugin") ),
            ( None, _("Do not deploy Exim Mail Queue plugin") ),
        ]
    )
)


