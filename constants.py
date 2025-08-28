# File: constants
# This file contains physical and mathematical constants used in the simulation.

import numpy as np 

# Universal Constants
G = 6.67430e-11  # Gravitational constant, m^3 kg^-1 s^-2
c = 299792458    # Speed of light in vacuum, m/s  

# Earth Constants
R_earth = 6371e3  # Earth's radius in meters
M_earth = 5.972e24  # Earth's mass in kg
mu_earth = G * M_earth  # Earth's standard gravitational parameter, m^3
B_earth = [3.12e-5, 3.12e-5, 3.12e-5]  # Earth's magnetic field strength at surface, Tesla

# Mathematical Constants
pi = np.pi  # Pi
e = np.e    # Euler's number
deg2rad = pi / 180  # Degrees to radians conversion factor
rad2deg = 180 / pi  # Radians to degrees conversion factor

# Time Constants
seconds_per_minute = 60
seconds_per_hour = 3600
seconds_per_day = 86400
seconds_per_year = 31557600  # Average year length in seconds
