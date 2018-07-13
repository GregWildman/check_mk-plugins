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

# Input power
#  --vertical-label 'Decibel-milliwatts' --title 'Input power'  -l 0
# DEF:input_signal_power_dbm=$RRDBASE$_input_power.rrd:1:MAX
# CDEF:input_signal_power_dbm_LEGSCALED=input_signal_power_dbm,1.000000,/
# CDEF:input_signal_power_dbm_NEG=input_signal_power_dbm,-1,*
# CDEF:input_signal_power_dbm_LEGSCALED_NEG=input_signal_power_dbm_LEGSCALED,-1,*
# DEF:output_signal_power_dbm=$RRDBASE$_output_power.rrd:1:MAX
# CDEF:output_signal_power_dbm_LEGSCALED=output_signal_power_dbm,1.000000,/
# CDEF:output_signal_power_dbm_NEG=output_signal_power_dbm,-1,*
# CDEF:output_signal_power_dbm_LEGSCALED_NEG=output_signal_power_dbm_LEGSCALED,-1,*
# AREA:input_signal_power_dbm#20c080:"Input power"
# LINE:input_signal_power_dbm#199966
# GPRINT:input_signal_power_dbm_LEGSCALED:AVERAGE:"%8.2lf dBm average"
# GPRINT:input_signal_power_dbm_LEGSCALED:MAX:"%8.2lf dBm max"
# GPRINT:input_signal_power_dbm_LEGSCALED:LAST:"%8.2lf dBm last"
# COMMENT:"\n" 

# Output power
#  --vertical-label 'Decibel-milliwatts' --title 'Output power'  -l 0
# DEF:input_signal_power_dbm=$RRDBASE$_input_power.rrd:1:MAX CDEF:input_signal_power_dbm_LEGSCALED=input_signal_power_dbm,1.000000,/ CDEF:input_signal_power_dbm_NEG=input_signal_power_dbm,-1,* CDEF:input_signal_power_dbm_LEGSCALED_NEG=input_signal_power_dbm_LEGSCALED,-1,* DEF:output_signal_power_dbm=$RRDBASE$_output_power.rrd:1:MAX CDEF:output_signal_power_dbm_LEGSCALED=output_signal_power_dbm,1.000000,/ CDEF:output_signal_power_dbm_NEG=output_signal_power_dbm,-1,* CDEF:output_signal_power_dbm_LEGSCALED_NEG=output_signal_power_dbm_LEGSCALED,-1,* AREA:output_signal_power_dbm#2080c0:"Output power" LINE:output_signal_power_dbm#196699 GPRINT:output_signal_power_dbm_LEGSCALED:AVERAGE:"%8.2lf dBm average" GPRINT:output_signal_power_dbm_LEGSCALED:MAX:"%8.2lf dBm max" GPRINT:output_signal_power_dbm_LEGSCALED:LAST:"%8.2lf dBm last" COMMENT:"\n" 


#
# Define some colors ..
#
$_WARNRULE = '#FFFF00';
$_CRITRULE = '#FF0000';

# TODO: calculate these limits better
$UPPER = $CRIT_MAX[1];
$LOWER = $CRIT_MIN[1];
$ds_name[1] = 'Input Power';
$opt[1] = "--vertical-label \"Decibel-milliwatts\"  --title \"$hostname / $servicedesc Input Power\" -u $UPPER -l $LOWER ";
$def[1] = 
  "DEF:input_signal_power_dbm=$RRDFILE[1]:$DS[1]:MAX ".
  "CDEF:input_signal_power_dbm_LEGSCALED=input_signal_power_dbm,1.000000,/ ".
  "CDEF:input_signal_power_dbm_NEG=input_signal_power_dbm,-1,* ".
  "CDEF:input_signal_power_dbm_LEGSCALED_NEG=input_signal_power_dbm_LEGSCALED,-1,* ".
  "HRULE:0#000000 ".
  "HRULE:$WARN_MIN[1]$_WARNRULE::dashes=2,5 ".
  "HRULE:$WARN_MAX[1]$_WARNRULE:\"Warning level\:  low $WARN_MIN[1] dBm, high $WARN_MAX[1] dBm \\n\":dashes=2,5 ".
  "HRULE:$CRIT_MIN[1]$_CRITRULE::dashes=2,5 ".
  "HRULE:$CRIT_MAX[1]$_CRITRULE:\"Critical level\: low $CRIT_MIN[1] dBm, high $CRIT_MAX[1] dBm \\n\":dashes=2,5 ".
  "AREA:input_signal_power_dbm#20c080#7ce9bd:\"Input power\" ".
  "LINE:input_signal_power_dbm#199966 ".
  "GPRINT:input_signal_power_dbm_LEGSCALED:AVERAGE:\"%8.2lf dBm average\" ".
  "GPRINT:input_signal_power_dbm_LEGSCALED:MAX:\"%8.2lf dBm max\" ".
  "GPRINT:input_signal_power_dbm_LEGSCALED:LAST:\"%8.2lf dBm last\"";


$UPPER = $CRIT_MAX[2];
$LOWER = $CRIT_MIN[2];
$ds_name[2] = 'Output Power';
$opt[2] = "--vertical-label \"Decibel-milliwatts\"  --title \"$hostname / $servicedesc Output Power\" -u $UPPER -l $LOWER";
#$def[2] = "DEF:input_signal_power_dbm=$RRDFILE[1]:$DS[1]:MAX CDEF:input_signal_power_dbm_LEGSCALED=input_signal_power_dbm,1.000000,/ CDEF:input_signal_power_dbm_NEG=input_signal_power_dbm,-1,* CDEF:input_signal_power_dbm_LEGSCALED_NEG=input_signal_power_dbm_LEGSCALED,-1,* DEF:output_signal_power_dbm=$RRDFILE[2]:$DS[1]:MAX CDEF:output_signal_power_dbm_LEGSCALED=output_signal_power_dbm,1.000000,/ CDEF:output_signal_power_dbm_NEG=output_signal_power_dbm,-1,* CDEF:output_signal_power_dbm_LEGSCALED_NEG=output_signal_power_dbm_LEGSCALED,-1,* AREA:output_signal_power_dbm#2080c0:\"Output power\" LINE:output_signal_power_dbm#196699 GPRINT:output_signal_power_dbm_LEGSCALED:AVERAGE:\"%8.2lf dBm average\" GPRINT:output_signal_power_dbm_LEGSCALED:MAX:\"%8.2lf dBm max\" GPRINT:output_signal_power_dbm_LEGSCALED:LAST:\"%8.2lf dBm last\""; 
$def[2] =
  "DEF:output_signal_power_dbm=$RRDFILE[2]:$DS[1]:MAX ".
  "CDEF:output_signal_power_dbm_LEGSCALED=output_signal_power_dbm,1.000000,/ ".
  "CDEF:output_signal_power_dbm_NEG=output_signal_power_dbm,-1,* ".
  "CDEF:output_signal_power_dbm_LEGSCALED_NEG=output_signal_power_dbm_LEGSCALED,-1,* ".
  "HRULE:0#000000 ".
  "HRULE:$WARN_MIN[2]$_WARNRULE::dashes=2,5 ".
  "HRULE:$WARN_MAX[2]$_WARNRULE:\"Warning level\:  low $WARN_MIN[2] dBm, high $WARN_MAX[2] dBm \\n\":dashes=2,5 ".
  "HRULE:$CRIT_MIN[2]$_CRITRULE::dashes=2,5 ".
  "HRULE:$CRIT_MAX[2]$_CRITRULE:\"Critical level\: low $CRIT_MIN[2] dBm, high $CRIT_MAX[2] dBm \\n\":dashes=2,5 ".
  "AREA:output_signal_power_dbm#2080c0#7cbde9:\"Output power\" ".
  "LINE:output_signal_power_dbm#199966 ".
  "GPRINT:output_signal_power_dbm_LEGSCALED:AVERAGE:\"%8.2lf dBm average\" ".
  "GPRINT:output_signal_power_dbm_LEGSCALED:MAX:\"%8.2lf dBm max\" ".
  "GPRINT:output_signal_power_dbm_LEGSCALED:LAST:\"%8.2lf dBm last\"";

?>
