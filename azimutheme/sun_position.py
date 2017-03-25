# sun_position.py
# Calculate the sun's current position (and if the theme needs to be switched)
# via PyEphem.

import ephem
import datetime

def get_sun_position_rad(latitude, longitude):
	obs = ephem.Observer()
	obs.lat = latitude
	obs.long = longitude
	obs.date = ephem.now()

	sun = ephem.Sun(obs)
	sun.compute(obs)
	return float(sun.alt)

def get_sun_position_deg(latitude, longitude):
	return get_sun_position_rad(latitude, longitude) * 57.2957795
