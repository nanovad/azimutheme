# xfconf_query.py
# Xfconf interfaces via CLI/subprocess Popen.

import subprocess
from subprocess import Popen

def set_setting(channel, property, value):
	Popen(["xfconf-query", "-c", channel, "-p", property, "-s", value])

def get_setting(channel, property):
	with Popen(["xfconf-query", "-c", channel, "-p", property],
			   stdout=subprocess.PIPE) as proc:
		return proc.stdout.read().decode("UTF-8").rstrip("\n")
