import numpy as np
import scipy as sp
import matplotlib.pyplot as plt 

# File: main 
# Main entry point for the CubeSat simulation.
# This file initializes the CubeSat, sets up the simulation parameters, and runs the simulation loop

from satellite import CubeSat
from simulator import Simulator   

# Define CubeSat parameters
mass = 1.33  # kg     
dimensions = (0.1, 0.1, 0.1)  # meters (1U CubeSat)
r0 = [7000e3, 0, 0]  # Initial position
v0 = [0, 7.5e3, 0]  # Initial velocity
q0 = [1, 0, 0, 0]  # Initial attitude quaternion
omega0 = [0, 0, 0]  # Initial angular velocity
I = None  # Use default inertia

# Create CubeSat instance
cubesat = CubeSat(mass, dimensions, r0, v0, q0, omega0, I)

# Define simulation parameters
time_step = 1  # seconds
total_time = 3600  # seconds (1 hour)

# Create Simulator instance
simulator = Simulator(cubesat, time_step, total_time)

# Run Simulator
sim_results = simulator.run_simulation(total_time)
print("Simulation complete")

# Visualisation 





