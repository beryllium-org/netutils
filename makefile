SHELL = bash
all:
	@echo -e "JPKG package builder.\n\nUsage:\n\tmake package\n\tmake clean"
update_modules:
	@echo "Updating git submodules from remotes.."
	@git submodule update --init --recursive --remote .
	@echo -e "Submodules ready\n\nMake sure to git commit before procceding to make!!"
modules:
	@echo "Preparing git submodules.."
	@git submodule update --init --recursive .
	@echo "Submodules ready"
package: modules
	@python3 -u scripts/make_lib.py
	@python3 -u scripts/generate_package.py
clean:
	@if [ -e "netutils.jpk" ]; then rm netutils.jpk; fi
	@if [ -e "./files/adafruit_connection_manager.mpy" ]; then rm ./files/adafruit_connection_manager.mpy; fi
	@if [ -e "./files/adafruit_ntp.mpy" ]; then rm ./files/adafruit_ntp.mpy; fi
	@if [ -e "./files/adafruit_requests.mpy" ]; then rm ./files/adafruit_requests.mpy; fi
	@if [ -e "./files/telnet_console.mpy" ]; then rm ./files/telnet_console.mpy; fi
