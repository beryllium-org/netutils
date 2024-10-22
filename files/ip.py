rename_process("ip")
be.api.setvar("return", "1")
vr("opts", be.api.xarg())
vr(
    "htext",
    """Usage: ip [ OPTIONS ] OBJECT { COMMAND | help }
       ip [ -force ] -batch filename
where  OBJECT := { address | addrlabel | fou | help | ila | ioam | l2tp | link |
                   macsec | maddress | monitor | mptcp | mroute | mrule |
                   neighbor | neighbour | netconf | netns | nexthop | ntable |
                   ntbl | route | rule | sr | stats | tap | tcpmetrics |
                   token | tunnel | tuntap | vrf | xfrm }
       OPTIONS := { -V[ersion] | -s[tatistics] | -d[etails] | -r[esolve] |
                    -h[uman-readable] | -iec | -j[son] | -p[retty] |
                    -f[amily] { inet | inet6 | mpls | bridge | link } |
                    -4 | -6 | -M | -B | -0 |
                    -l[oops] { maximum-addr-flush-attempts } | -echo | -br[ief] |
                    -o[neline] | -t[imestamp] | -ts[hort] | -b[atch] [filename] |
                    -rc[vbuf] [size] | -n[etns] name | -N[umeric] | -a[ll] |
                    -c[olor]}
""",
)
if not vr("opts")["aw"]:
    term.write(vr("htext"))
elif vr("opts")["aw"]:
    vr("cmd", vr("opts")["aw"][0])
    vr("args", vr("opts")["aw"][1:])
    if vr("cmd") in ["addr", "a"]:
        if "network" in be.devices.keys():
            for pv[get_pid()]["i"] in list(be.devices["network"].keys()):
                vr("dat", be.devices["network"][vr("i")].get_ipconf())
                vr("hwn", be.devices["network"][vr("i")].hw_name)
                vr("st", ("DOWN" if (vr("dat")["ip"] is None) else "UP"))
                if (
                    vr("st") == "DOWN"
                    and "ip_ap" in vr("dat")
                    and vr("dat")["ip_ap"] is not None
                ):
                    vr("st", "UP")
                term.nwrite(str(vr("i")) + ": " + vr("hwn") + ": <" + vr("st") + ",")
                if "ip_ap" in vr("dat") and vr("dat")["ip_ap"] is not None:
                    term.nwrite("BROADCAST,")
                term.write("\010 \010> noqueue state " + vr("st") + " group DEFAULT")
                term.nwrite((" " * 4) + "link/" + vr("hwn"))
                if "mac_pretty_ap" in vr("dat"):
                    term.nwrite(
                        " "
                        + vr("dat")["mac_pretty"]
                        + " ap "
                        + vr("dat")["mac_pretty_ap"]
                    )
                term.write()
                if vr("dat")["ip"] is not None:
                    term.write(
                        (" " * 4)
                        + "inet_st "
                        + str(vr("dat")["ip"])
                        + "/? scope global"
                    )
                    term.write((" " * 8) + "valid_lft forever preferred_lft forever")
                else:
                    term.write((" " * 4) + "inet_st 0.0.0.0/16 scope host lo")
                    term.write((" " * 8) + "valid_lft forever preferred_lft forever")
                if "ip_ap" in vr("dat"):
                    if vr("dat")["ip_ap"] is not None:
                        term.write(
                            (" " * 4)
                            + "inet_ap "
                            + str(vr("dat")["ip_ap"])
                            + "/? scope global"
                        )
                        term.write(
                            (" " * 8) + "valid_lft forever preferred_lft forever"
                        )
                    else:
                        term.write((" " * 4) + "inet_ap 0.0.0.0/16 scope host lo")
                        term.write(
                            (" " * 8) + "valid_lft forever preferred_lft forever"
                        )
    elif vr("cmd") in ["link", "l"]:
        pass
    elif vr("cmd") in ["route", "r"]:
        pass
    elif vr("cmd") in ["neighbor", "n"]:
        pass
    else:
        term.write(vr("htext"))
