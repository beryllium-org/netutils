for pv[get_pid()]["f"] in [
    "adafruit_connection_manager.mpy",
    "adafruit_ntp.mpy",
    "adafruit_requests.mpy",
    "telnet_console.mpy",
]:
    be.based.run("cp " + vr("f") + " /lib/" + vr("f"))

be.based.run("mkdir /bin/iwctl")
for pv[get_pid()]["f"] in [
    "headless.py",
    "interactive.py",
    "main.py",
]:
    be.based.run("cp " + vr("f") + " /bin/iwctl/" + vr("f"))

for pv[get_pid()]["f"] in [
    "ping.lja",
    "ping.py",
    "iwctl.lja",
    "telnet.lja",
    "telnet.py",
    "timesync.lja",
    "timesync.py",
    "load_networking.lja",
    "load_wifi.py",
    "rfkill.lja",
    "rfkill.py",
    "ip.lja",
    "ip.py",
]:
    be.based.run("cp " + vr("f") + " /bin/" + vr("f"))

be.based.run("cp rfkill.man /usr/share/man/rfkill.man")

be.api.setvar("return", "0")
