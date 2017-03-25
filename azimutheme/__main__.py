import os
import os.path
import signal
import sys
import time

import argparse
import configparser
import daemonize

from azimutheme import xfconf_query, sun_position

config = configparser.ConfigParser()

def set_theme(theme_name):
	xfconf_query.set_setting("xsettings", "/Net/ThemeName", theme_name)

def set_window_theme(theme_name):
	xfconf_query.set_setting("xfwm4", "/general/theme", theme_name)

def get_theme():
	return xfconf_query.get_setting("xsettings", "/Net/ThemeName")

def get_window_theme():
	return xfconf_query.get_setting("xfwm4", "/general/theme")

def error_on_missing_section(section_name, configuration):
	if not section_name in configuration:
		print("configuration file does not have required section \"{}\"".format(
			section_name), file=sys.stderr)
		sys.exit(1)

def is_daytime(latitude, longitude):
	position = sun_position.get_sun_position_deg(latitude, longitude)
	# 3 degrees is a magic threshold - sun must rise above 3 degrees before it
	# is considered daytime, or below 3 to be considered nighttime.
	return True if position > 3 else False

last_is_day = False
longitude = 0
latitude = 0

def update_if_needed():
	global config
	global last_is_day

	global latitude
	global longitude

	# TODO: Possibly query Xfconf before actually switching the theme?

	if is_daytime(latitude, longitude) and last_is_day == False:
		set_theme(config["theme"].get("day"))
		set_window_theme(config["window_theme"].get("day"))
		last_is_day = True
	elif not is_daytime(latitude, longitude) and last_is_day == True:
		set_theme(config["theme"].get("night"))
		set_window_theme(config["window_theme"].get("night"))
		last_is_day = False

def handle_sigusr1(signum, stack):
	update_if_needed()

def main():
	global config

	global latitude
	global longitude

	global last_is_day

	config_filename = os.path.join(os.path.expanduser("~"), ".config",
								   "azimutheme", "azimutheme.ini")
	config_parent_dir = os.path.abspath(os.path.join(config_filename,
													 os.pardir))
	if not os.path.exists(config_parent_dir):
		os.makedirs(config_parent_dir)

	if os.path.isfile(config_filename):
		config.read(config_filename)
	else:
		print("could not find configuration file", file=sys.stderr)
		sys.exit(1)

	for section in ["theme", "window_theme", "location"]:
		error_on_missing_section(section, config)

	latitude = config["location"].get("latitude")
	longitude = config["location"].get("longitude")

	signal.signal(signal.SIGUSR1, handle_sigusr1)

	# Setting last_is_day to not is_daytime() forces an update on app startup.
	last_is_day = not is_daytime(latitude, longitude)
	while True:
		update_if_needed()
		time.sleep(10 * 60) # 10 minutes (time.sleep arguments are in seconds)

if __name__ == "__main__":
	pidfile = "/run/user/{}/azimutheme.pid".format(os.getuid())

	parser = argparse.ArgumentParser(
		description="change the GTK theme based on	current daylight state")
	parser.add_argument("-d", "--daemonize", dest="daemonize",
						action="store_true", help="fork into the background")
	args = parser.parse_args()
	if args.daemonize:
		daemon = daemonize.Daemonize(app="azimutheme", pid=pidfile, action=main)
		daemon.start()
	else:
		main()
