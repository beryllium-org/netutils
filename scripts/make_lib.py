from os import listdir, system
from sys import path as spath


def errexit():
    print("Compilation error, exiting")
    exit(1)


spath.append("./submodules/CircuitMPY/")
import circuitmpy

circuitmpy.fetch_mpy()

try:
    print("adafruit_connection_manager.py -> adafruit_connection_manager.mpy")
    circuitmpy.compile_mpy("./submodules/Adafruit_CircuitPython_ConnectionManager/adafruit_connection_manager.py", "./files/adafruit_connection_manager.mpy")
except:
    errexit()

try:
    print(f"adafruit_ntp.py -> adafruit_ntp.mpy")
    circuitmpy.compile_mpy("./submodules/Adafruit_CircuitPython_NTP/adafruit_ntp.py", "./files/adafruit_ntp.mpy")
except:
    errexit()

try:
    print(f"adafruit_requests.py -> adafruit_requests.mpy")
    circuitmpy.compile_mpy("./submodules/Adafruit_CircuitPython_Requests/adafruit_requests.py", "./files/adafruit_requests.mpy")
except:
    errexit()

try:
    print(f"telnet_console.py -> telnet_console.mpy")
    circuitmpy.compile_mpy("./other/telnet_console.py", "./files/telnet_console.mpy")
except:
    errexit()

print()
