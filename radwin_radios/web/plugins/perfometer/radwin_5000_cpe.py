# Perf data from the check.
#  (hsu_rss=-64.0dBm;;;;)

def perfometer_check_mk_radwin_5000_cpe(row, check_command, perf_data):
    dbm = float(perf_data[0][1])
    return "%.1f dBm" % dbm, perfometer_logarithmic(dbm, 50, 2, "#20c080")

perfometers["check_mk-radwin_5000_cpe"] = perfometer_check_mk_radwin_5000_cpe

