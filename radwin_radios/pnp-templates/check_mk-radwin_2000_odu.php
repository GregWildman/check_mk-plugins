<?php
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

# Performance data from check:
# UAS=0;;;;
# ES=56;;;;
# SRS=0;;;;
# BBE=285;;;;

#
# Name	 winlink1000OduPerfMonCurrUAS (.1.1)
#        The current number of Unavailable Seconds starting from
#        the present 15 minutes period.
#
# Name	 winlink1000OduPerfMonCurrES (.1.2)
#        Current number of Errored Seconds starting from the
#        present 15 minutes period.
#
# Name	 winlink1000OduPerfMonCurrSES (.1.3)
#        Current number of Severely Errored Seconds starting
#        from the present 15 minutes period.
#
# Name	 winlink1000OduPerfMonCurrBBE (.1.4)
#        Current number of Background Block Errors starting from
#        the present 15 minutes period.
#

# Graph 1: Unavailable Seconds
$ds_name[1] = 'winlink1000OduPerfMonCurrUAS';
$opt[1] = "--vertical-label \"Seconds\" --title \"Unavailable Seconds / $hostname\" ";

$def[1] = "DEF:var1=$RRDFILE[1]:$DS[1]:MAX ";
$def[1] .= "AREA:var1#2080ff:\"Seconds\:\" ";
$def[1] .= "GPRINT:var1:LAST:\"%3.0lf\" ";
$def[1] .= "LINE1:var1#000080:\"\" ";
$def[1] .= "GPRINT:var1:MAX:\"(Max\: %3.0lf,\" ";
$def[1] .= "GPRINT:var1:AVERAGE:\"Avg\: %3.0lf)\" ";
if ($WARN[1] != "") {
    $def[1] .= "HRULE:$WARN[1]#FFFF00:\"Warning\: $WARN[1]\" ";
    $def[1] .= "HRULE:$CRIT[1]#FF0000:\"Critical\: $CRIT[1]\" ";
}

# Graph 2: Errored Seconds
$ds_name[2] = 'winlink1000OduPerfMonCurrES';
$opt[2] = "--vertical-label \"Seconds\" --title \"Errored Seconds / $hostname\" ";

$def[2] = "DEF:var1=$RRDFILE[2]:$DS[2]:MAX ";
$def[2] .= "AREA:var1#2080ff:\"Seconds\:\" ";
$def[2] .= "GPRINT:var1:LAST:\"%3.0lf\" ";
$def[2] .= "LINE1:var1#000080:\"\" ";
$def[2] .= "GPRINT:var1:MAX:\"(Max\: %3.0lf,\" ";
$def[2] .= "GPRINT:var1:AVERAGE:\"Avg\: %3.0lf)\" ";
if ($WARN[2] != "") {
    $def[2] .= "HRULE:$WARN[2]#FFFF00:\"Warning\: $WARN[2]\" ";
    $def[2] .= "HRULE:$CRIT[2]#FF0000:\"Critical\: $CRIT[2]\" ";
}

# Graph 3: Severely Errored Seconds
$ds_name[3] = 'winlink1000OduPerfMonCurrSES';
$opt[3] = "--vertical-label \"Seconds\" --title \"Severely Errored Seconds / $hostname\" ";

$def[3] = "DEF:var1=$RRDFILE[3]:$DS[3]:MAX ";
$def[3] .= "AREA:var1#2080ff:\"Seconds\:\" ";
$def[3] .= "GPRINT:var1:LAST:\"%3.0lf\" ";
$def[3] .= "LINE1:var1#000080:\"\" ";
$def[3] .= "GPRINT:var1:MAX:\"(Max\: %3.0lf,\" ";
$def[3] .= "GPRINT:var1:AVERAGE:\"Avg\: %3.0lf)\" ";
if ($WARN[3] != "") {
    $def[3] .= "HRULE:$WARN[3]#FFFF00:\"Warning\: $WARN[3]\" ";
    $def[3] .= "HRULE:$CRIT[3]#FF0000:\"Critical\: $CRIT[3]\" ";
}

# Graph 4: Background Block Errors
$ds_name[4] = 'winlink1000OduPerfMonCurrBBE';
$opt[4] = "--vertical-label \"Seconds\" --title \"Background Block Errors / $hostname\" ";

$def[4] = "DEF:var1=$RRDFILE[4]:$DS[4]:MAX ";
$def[4] .= "AREA:var1#2080ff:\"Seconds\:\" ";
$def[4] .= "GPRINT:var1:LAST:\"%3.0lf\" ";
$def[4] .= "LINE1:var1#000080:\"\" ";
$def[4] .= "GPRINT:var1:MAX:\"(Max\: %3.0lf,\" ";
$def[4] .= "GPRINT:var1:AVERAGE:\"Avg\: %3.0lf)\" ";
if ($WARN[4] != "") {
    $def[4] .= "HRULE:$WARN[4]#FFFF00:\"Warning\: $WARN[4]\" ";
    $def[4] .= "HRULE:$CRIT[4]#FF0000:\"Critical\: $CRIT[4]\" ";
}

?>
