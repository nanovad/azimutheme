from setuptools import setup

setup(
	author='Nicholas De Nova',
	author_email='nanovad@gmail.com',
	description='Sets XFCE window borders and GTK theme based on solar position.',
	install_requires=[
		'ephem==3.7.6.0',
		'daemonize==2.4.7'
		],
	name='Azimutheme',
	license='ISC License',
	packages=['azimutheme'],
	version='0.2.1',
)
