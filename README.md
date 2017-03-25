# Azimutheme
### A simple daemon that sets XFCE window borders and GTK theme based on solar position

## Installation
#### Get dependencies
You will need Python 3 and Pip for Python 3.  
You will also need XFCE and xfconf-query.
#### Get the code
Clone the repository via HTTPS: `git clone https://github.com/nanovad/azimutheme.git`  
Change to the source tree: `cd azimutheme`
#### Get Azimutheme's dependencies
Use Pip to install Azimutheme's dependencies: `pip3 install -r requirements.txt`
#### Install
Azimutheme comes with a setup.py file that automates installation.  
To install system-wide, run (as root): `python3 setup.py install`
## Configuration
Azimutheme uses a configuration file stored at `~/.config/azimutheme/azimutheme.ini`  
This file uses a syntax similar to Windows INI files.
See [the Python 3 documentation](https://docs.python.org/3/library/configparser.html?highlight=configparser#module-configparser) for more details.

Azimutheme expects 3 configuration sections: `[theme]`, `[window_theme]`, and `[location]`  
These sections specify GTK theme, XFCE window border theme, and current location on Earth, respectively.

In the `[theme]` and `[window_theme]` sections, two values are stored, each: `day` and `night`  
These specify the themes to be used for daytime and nighttime.

The `[location]` section has two values: `latitude` and `longitude`  
These are floating-point values specifying your current location on Earth.  
The more accurate these values are, the better Azimutheme can predict when to switch themes.  
A good way to determine find these values is to use [this website](http://www.latlong.net).

Here is an example configuration file:

```
[theme]
day = Arc
night = Arc-Dark

[window_theme]
day = Arc
night = Arc-Dark

[location]
latitude = 37.7791
longitude = -122.4169
```  
This configuration file  
*  Sets the GTK theme to Arc during the day, and Arc Dark at night.  
*  Sets the XFCE window theme to Arc during the day, and Arc Dark at night.  
*  Specifies a fairly precise latitude and longitude near the heart of San Francisco.

## Running
Make sure you have all dependencies installed and have set up the configuration file before running!  
If you want Azimutheme to run as a daemon, specify the `-d` option after all arguments.
#### From the source tree
`cd` to the source tree.  
Run `python3 azimutheme`
#### From a system-wide install
Run `python3 -m azimutheme`
