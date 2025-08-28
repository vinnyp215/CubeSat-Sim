#File: spacecraft_config.py
# This file contains the configuration parameters for the CubeSat simulation.

import numpy as np

# --- CubeSat Physical Parameters ---
mass = 1.33  # kg     
dimensions = (0.1, 0.1, 0.1)  # meters (1U CubeSat)
I = np.diag([0.01, 0.01, 0.02])  # Inertia matrix (kg·m²) for a typical CubeSat
I_inv = np.linalg.inv(I) # Inverse of inertia matrix

# --- Initial Conditions ---
r0 = [7000e3, 0, 0]  # Initial position
v0 = [0, 7.5e3, 0]  # Initial velocity
q0 = [1, 0, 0, 0]  # Initial attitude quaternion
w0 = [0.1, 0, 0]  # Initial angular velocity

# --- ADCS ---
sensors = ['sun_sensor', 'magnetometer']
actuators = ['reaction_wheel', 'magnetorquer']
K_mt = 100 # Magnetorquer control gain factor
K_p = 0.1  # Reaction wheel proportional gain
K_d = 0.1  # Reaction wheel derivative gain

# --- Power ---
battery_capacity=10
solar_panel_area=0.01
solar_panel_efficiency=0.3

