for i in [
    "adafruit_connection_manager.mpy",
    "adafruit_ntp.mpy",
    "adafruit_requests.mpy",
    "telnet_console.mpy",
]:
    shutil.copyfile(i, path.join(root, "lib", i))

try:
    mkdir(path.join(root, "bin/iwctl"))
except FileExistsError:
    pass

for i in [
    "headless.py",
    "interactive.py",
    "main.py",
]:
    shutil.copyfile(i, path.join(root, "bin/iwctl", i))

for i in [
    "ping.lja",
    "ping.py",
    "iwctl.lja",
    "telnet.lja",
    "telnet.py",
    "timesync.lja",
    "timesync.py",
    "load_networking.lja",
    "load_wifi.py",
]:
    shutil.copyfile(i, path.join(root, "bin", i))
