def perfometer_check_mk_alcoma_almp_line(row, check_command, perf_data):
    unit =  "Bit/s" in row["service_plugin_output"] and "Bit" or "B"
    return perfometer_bandwidth(
        in_traffic  = savefloat(perf_data[0][1]),
        out_traffic = savefloat(perf_data[2][1]),
        in_bw     = savefloat(perf_data[0][6]),
        out_bw    = savefloat(perf_data[2][6]),
        unit      = unit
    )

perfometers["check_mk-alcoma_almp.line"] = perfometer_check_mk_alcoma_almp_line

