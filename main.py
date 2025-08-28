# File: main 
# Main entry point for the CubeSat simulation.
# This file initialises the CubeSat, sets up the simulation parameters, and runs the simulation loop

from satellite import CubeSat
from simulator import Simulator   
from ground_station import GroundStation

import constants
import simulator
import visualisation
import spacecraft_config as sc

# Import CubeSat Parameters from spacecraft_config.py
mass = sc.mass  # kg     
dimensions = sc.dimensions  # meters (1U CubeSat)
r0 = sc.r0  # Initial position
v0 = sc.v0  # Initial velocity
q0 = sc.q0  # Initial attitude quaternion
w0 = sc.w0  # Initial angular velocity
I = sc.I  # Inertia matrix diagonal elements

# Define CubeSat functionality

# ADCS Parameters
sensors = ['sun_sensor', 'magnetometer']
actuators = ['reaction_wheel', 'magnetorquer']
K_mt = sc.K_mt # Magnetorquer control gain factor
K_p = sc.K_p  # Reaction wheel proportional gain
K_d = sc.K_d  # Reaction wheel derivative gain

# Power System Parameters


# Define simulation parameters
time_step = 10  # seconds
total_time = 3600  # seconds 

# Create CubeSat instance
cubesat = CubeSat(mass, dimensions, r0, v0, q0, w0, I)

# Create Subsystems instances and attach to CubeSat
from subsystems.ADCS import ADCS
# from subsystems.power import Power  
# from subsystems.Comms import Comms
# from subsystems.Thermal import Thermal
# from subsystems.Payload import Payload
# from subsystems.Propulsion import Propulsion

# Create ADCS instance
adcs = ADCS(sensors, actuators)
cubesat.adcs = adcs

# # Create Power instance
# power = Power(battery_capacity=10, solar_panel_area=0.01, solar_panel_efficiency=0.3)
# cubesat.power = power

# Create Ground Station instance
ground_station = GroundStation("GS1", 0.0, 0.0, 0) 

# Create Simulator instance
simulator = Simulator(cubesat, time_step, total_time)

# Run Simulator
sim_results = simulator.run_simulation(total_time)
print("Simulation complete")

# Visualisation 
visualisation.plot_trajectory_3D(sim_results)
print("Trajectory plotted")

visualisation.plot_attitude(sim_results)
print("Attitude plotted")










