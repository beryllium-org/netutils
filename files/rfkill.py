rename_process("rfkill")
vr("opts", be.api.xarg())
if (
    "help" in vr("opts")["o"]
    or "h" in vr("opts")["o"]
    or not vr("opts")["aw"]
    or (len(vr("opts")["aw"]) and vr("opts")["aw"][0] == "help")
):
    be.based.run("man rfkill")
elif vr("opts")["aw"]:
    vr("s", 0)
    if vr("opts")["aw"][0] == "list":
        for pv[get_pid()]["i"] in cptoml.keys("RFKILL"):
            term.write(
                str(vr("s"))
                + ": "
                + vr("i")
                + ":\n"
                + (" " * 6)
                + "Blocked: "
                + ("yes" if cptoml.fetch(vr("i"), subtable="RFKILL") else "no")
            )
            vrp("s")
    elif vr("opts")["aw"][0] == "unblock":
        if len(vr("opts")["aw"]) > 1:
            vr("d", vr("opts")["aw"][1])
            if vr("d") in cptoml.keys("RFKILL"):
                if vr("d") == "wlan":
                    be.devices["network"][0].start()
                elif vr("d") == "bluetooth":
                    pass
                try:
                    remount("/", False)
                    cptoml.put(vr("d"), False, subtable="RFKILL")
                    remount("/", True)
                except RuntimeError:
                    term.write("Could not commit rfkill state to storage!")
            else:
                term.write("Unknown device!")
        else:
            term.write("No device specified!")
    elif vr("opts")["aw"][0] == "block":
        if len(vr("opts")["aw"]) > 1:
            vr("d", vr("opts")["aw"][1])
            if vr("d") in cptoml.keys("RFKILL"):
                if vr("d") == "wlan":
                    be.devices["network"][0].stop()
                elif vr("d") == "bluetooth":
                    pass
                try:
                    remount("/", False)
                    cptoml.put(vr("d"), True, subtable="RFKILL")
                    remount("/", True)
                except RuntimeError:
                    term.write("Could not commit rfkill state to storage!")
            else:
                term.write("Unknown device!")
        else:
            term.write("No device specified!")
    elif vr("opts")["aw"][0] == "toggle":
        if len(vr("opts")["aw"]) > 1:
            vr("d", vr("opts")["aw"][1])
            vr("s", cptoml.fetch(vr("d"), subtable="RFKILL"))
            if vr("d") in cptoml.keys("RFKILL"):
                if vr("d") == "wlan":
                    if vr("s"):
                        be.devices["network"][0].start()
                    else:
                        be.devices["network"][0].stop()
                elif vr("d") == "bluetooth":
                    pass
                try:
                    remount("/", False)
                    cptoml.put(vr("d"), not vr("s"), subtable="RFKILL")
                    remount("/", True)
                except RuntimeError:
                    term.write("Could not commit rfkill state to storage!")
            else:
                term.write("Unknown device!")
        else:
            term.write("No device specified!")
    elif vr("opts")["aw"][0] == "event":
        term.write("Currently not implemented!")
    else:
        term.write("Invalid command, for more info, run `man rfkill`.")
