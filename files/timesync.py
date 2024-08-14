rename_process("timesync")
systemprints(2, "Sync time via ntp")
if "network" in be.devices and be.devices["network"][0].connected:
    if be.devices["network"][0].timeset():
        be.based.system_vars["TIMEZONE_OFFSET"] = be.devices["network"][0]._tz
        systemprints(1, "Sync time via ntp")
        be.api.setvar("return", "0")
    else:
        systemprints(3, "Sync time via ntp")
        be.api.setvar("return", "1")
else:
    systemprints(5, "Sync time via ntp")
