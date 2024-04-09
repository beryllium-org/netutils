vr("passwd", None)
vr("inc", 1)
if vr("args")[0] == "--passphrase":
    if vr("args")[1].startswith('"'):
        while True:
            if vr("args")[vr("inc")].endswith('"'):
                break
            elif vr("inc") < vr("argl"):
                vrp("inc")
            else:
                be.based.error(1)
                vrm("inc")
        if vr("inc") is not -1:
            vr("passwd", vr("args")[1] + " ")
            for pv[get_pid()]["i"] in range(2, vr("inc") + 1):
                vrp("passwd", vr("args")[vr("i")] + " ")
            vr("passwd", vr("passwd")[1:-2])
    else:
        vr("passwd", vr("args")[1])
else:
    vr("inc", None)
if vr("inc") is not None:
    vrp("inc")
    vr("args", vr("args")[vr("inc") :])
    vrm("argl", vr("inc"))

if vr("argl") > 2 and vr("args")[0] == "station" and vr("args")[1] == vr("device_n"):
    if vr("argl") > 3 and vr("args")[2] == "connect":
        vr("networks", be.devices["network"][0].scan())
        if vr("args")[3] in vr("networks"):
            vr("res", False)
            if vr("networks")[vr("args")[3]][0] != "OPEN":
                vr("tpd", cptoml.fetch(vr("args")[3], subtable="IWD"))
                if vr("passwd") is not None:
                    be.devices["network"][0].disconnect()
                    be.devices["network"][0].disconnect_ap()
                    dmtex('IWD: Connecting to: "{}"'.format(vr("args")[3]))
                    vr(
                        "res",
                        be.devices["network"][0].connect(vr("args")[3], vr("passwd")),
                    )
                elif vr("tpd") is not None:
                    be.devices["network"][0].disconnect()
                    be.devices["network"][0].disconnect_ap()
                    dmtex(
                        'IWD: Connecting to: "{}" with stored password.'.format(
                            vr("args")[3]
                        )
                    )
                    vr(
                        "res",
                        be.devices["network"][0].connect(vr("args")[3], vr("tpd")),
                    )
                else:
                    term.write("Error: No password specified")
            else:
                be.devices["network"][0].disconnect()
                be.devices["network"][0].disconnect_ap()
                dmtex('IWD: Connecting to: "{}"'.format(vr("args")[3]))
                vr("res", be.devices["network"][0].connect(vr("args")[3]))
            exec(vr("wifi_connect_msg"))
            if (
                vr("res")
                and (
                    vr("args")[3] not in cptoml.keys("IWD")
                    or cptoml.fetch(vr("args")[3], subtable="IWD") != vr("passwd")
                )
            ) and vr("passwd") is not None:
                # Store this network
                try:
                    remount("/", False)
                    cptoml.put(vr("args")[3], vr("passwd"), subtable="IWD")
                    remount("/", True)
                    dmtex("IWD: Network stored in settings.toml")
                except RuntimeError:
                    be.based.error(7)
            be.api.setvar("return", str(int(not vr("res"))))
        else:
            term.write("Network not found")
            be.api.setvar("return", "1")
    elif vr("args")[2] == "ap_mode" and vr("argl") > 3:
        if hasattr(be.devices["network"][0], "connect_ap"):
            vr(
                "res",
                be.devices["network"][0].connect_ap(vr("args")[3], vr("passwd")),
            )
            exec(vr("wifi_ap_msg"))
            be.api.setvar("return", str(int(not vr("res"))))
        else:
            dmtex("IWD: This interface does not support AP.")
    elif vr("args")[2] == "auto":
        if not be.devices["network"][0].connected:
            # We don't need to run on an already connected interface
            vr("stored_networks", cptoml.keys("IWD"))
            vr("res", False)
            if vr("stored_networks"):
                vr("scanned_networks", be.devices["network"][0].scan())
                for pv[get_pid()]["network"] in vr("stored_networks"):
                    if vr("network") in vr("scanned_networks"):
                        exec(vr("wifi_conn"))
                        if vr("res"):
                            break
            if not vr("res"):  # We have to create a hotspot based on toml settings.
                vr("apssid", cptoml.fetch("SSID", subtable="IWD-AP"))
                vr("appasswd", cptoml.fetch("PASSWD", subtable="IWD-AP"))
                if vr("apssid") is not None:
                    vr(
                        "res",
                        be.devices["network"][0].connect_ap(
                            vr("apssid"), vr("appasswd")
                        ),
                    )
                    exec(vr("wifi_ap_msg"))
    elif vr("args")[2] == "disconnect":
        be.devices["network"][0].disconnect()
        be.devices["network"][0].disconnect_ap()
        be.api.setvar("return", "0")
    else:
        be.based.error(1)
else:
    be.based.error(1)
