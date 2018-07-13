# Perf data from the check.
#    ("batt_capacity", batt_capacity, warn, crit, 0, 100)
#    ("load_voltage",  load_voltage)
#    ("load_current",  load_current)
#
# as per 'perfometer_battery' in check_mk.py

def perfometer_check_mk_mgeups_battery(row, command, perf):
    return "%0.2f%%" % float(perf[0][1]), perfometer_linear(float(perf[0][1]), '#B2FF7F')

perfometers["check_mk-mgeups_battery"] = perfometer_check_mk_mgeups_battery

