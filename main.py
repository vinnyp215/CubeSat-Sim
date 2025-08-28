# File: main 
# Main entry point for the CubeSat simulation.
# This file initialises the CubeSat, sets up the simulation parameters, and runs the simulation loop

from satellite import CubeSat
from simulator import Simulator   
from ground_station import GroundStation

import constants
import simulator
import visualisation

# Define CubeSat parameters
mass = 1.33  # kg     
dimensions = (0.1, 0.1, 0.1)  # meters (1U CubeSat)
r0 = [7000e3, 0, 0]  # Initial position
v0 = [0, 7.5e3, 0]  # Initial velocity
q0 = [1, 0, 0, 0]  # Initial attitude quaternion
w0 = [0.1, 0, 0]  # Initial angular velocity
I = constants.I  # Inertia matrix diagonal elements

# Define CubeSat functionality
sensors=['sun_sensor', 'magnetometer']
actuators=['reaction_wheel', 'magnetorquer']

# Define simulation parameters
time_step = 5  # seconds
total_time = 1000  # seconds 

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










