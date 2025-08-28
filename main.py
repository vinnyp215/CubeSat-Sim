# File: main 
# Main entry point for the CubeSat simulation.
# This file initialises the CubeSat, sets up the simulation parameters, and runs the simulation loop

from satellite import CubeSat
from simulator import Simulator   
from ground_station import GroundStation

from subsystems.ADCS import ADCS
from subsystems.power import Power  
# from subsystems.Comms import Comms
# from subsystems.Thermal import Thermal
# from subsystems.Payload import Payload
# from subsystems.Propulsion import Propulsion

import constants
import simulator
import visualisation
import spacecraft_config as scc

# Import CubeSat Parameters from spacecraft_config.py

# Physical Parameters
mass = scc.mass  # kg     
dimensions = scc.dimensions  # meters (1U CubeSat)
r0 = scc.r0  # Initial position
v0 = scc.v0  # Initial velocity
q0 = scc.q0  # Initial attitude quaternion
w0 = scc.w0  # Initial angular velocity
I = scc.I  # Inertia matrix diagonal elements
I_inv = scc.I_inv # Inverse of inertia matrix

# ADCS Parameters
sensors = ['sun_sensor', 'magnetometer']
actuators = ['reaction_wheel', 'magnetorquer']
K_mt = scc.K_mt # Magnetorquer control gain factor
K_p = scc.K_p  # Reaction wheel proportional gain
K_d = scc.K_d  # Reaction wheel derivative gain

# Power System Parameters
battery_capacity = scc.battery_capacity #Wh
solar_panel_area = scc.solar_panel_area #m^2
solar_panel_efficiency = scc.solar_panel_efficiency #%

# Define simulation parameters
time_step = 10  # seconds
total_time = 3600  # seconds 

# Create CubeSat instance & Subsystem instances
cubesat = CubeSat(mass, dimensions, r0, v0, q0, w0, I, I_inv)

# Create ADCS instance
adcs = ADCS(sensors, actuators)
cubesat.adcs = adcs

# Create Power instance
power = Power(battery_capacity, solar_panel_area, solar_panel_efficiency)
cubesat.power = power

# Create Ground Station instance
ground_station = GroundStation("GS1", 0.0, 0.0, 0) 

# Create Simulator instance
simulator = Simulator(cubesat, time_step, total_time)

# Run Simulator
sim_results = simulator.run_simulation(total_time)
print("Simulation complete")

# Visualisation 
visualisation.plot_trajectory_3D(sim_results)
visualisation.plot_attitude(sim_results)











