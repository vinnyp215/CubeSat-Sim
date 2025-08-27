# File: visualisation
# This file contains functions for the visualisation of simulation results

import numpy as np
import matplotlib.pyplot as plt
import constants as const

def plot_trajectory_3D(sim_results):
  """
  Plots the trajectory of the spacecraft in 3D from the simulation results.
  
  Args:
    sim_results: Data structure containing the simulation results.
    
  Returns:
    None
  """

  # Unpacked simulation results
  time = sim_results['time']
  position = sim_results['position']
  velocity = sim_results['velocity']
  attitude = sim_results['attitude']
  angular_velocity = sim_results['angular_velocity']

  # Plotting the trajectory in 3D
  fig = plt.figure()
  ax = fig.add_subplot(111, projection='3d')
  ax.plot(position[:,0], position[:,1], position[:,2], color='r')
  ax.set_title('Spacecraft Trajectory')
  ax.set_xlabel('X (m)')
  ax.set_ylabel('Y (m)')
  ax.set_zlabel('Z (m)')

  # Add Earth to plot
  u = np.linspace(0, 2 * np.pi, 100)
  v = np.linspace(0, np.pi, 100)
  x = const.R_earth * np.outer(np.cos(u), np.sin(v))
  y = const.R_earth * np.outer(np.sin(u), np.sin(v))
  z = const.R_earth * np.outer(np.ones(np.size(u)), np.cos(v))
  ax.plot_surface(x, y, z, color='b', alpha=0.3)
  plt.show()

  return None

def plot_ground_station_3D(latitude, longitude, altitude):
 """
 Plots the position of the ground station on a 3D Earth
 
 Args:
   latitude (float): Latitude of the ground station in degrees.
   longitude (float): Longitude of the ground station in degrees.
   altitude (float): Altitude of the ground station in meters.

  Returns:
    None
 """
 # Convert latitude and longitude to 

def plot_attitude(sim_results):
  """
  Plots the attitude of the spacecraft over time using the simulation results.

  Args:
    sim_results: Data structure containing the simulation results.

  Returns:
    None
  """
  
  # Unpacked simulation results
  time = sim_results['time']
  position = sim_results['position']
  velocity = sim_results['velocity']
  attitude = sim_results['attitude']
  angular_velocity = sim_results['angular_velocity']

  # Plotting the attitude over time
  fig, axs = plt.subplots(4, 1, figsize=(10, 8), sharex=True)
  axs[0].plot(time, attitude[:,0], label='q0')    
  axs[0].set_ylabel('q0')
  axs[0].legend()
  axs[1].plot(time, attitude[:,1], label='q1', color='orange')
  axs[1].set_ylabel('q1')
  axs[1].legend()
  axs[2].plot(time, attitude[:,2], label='q2', color='green')
  axs[2].set_ylabel('q2')
  axs[2].legend()
  axs[3].plot(time, attitude[:,3], label='q3', color='red')
  axs[3].set_ylabel('q3')
  axs[3].set_xlabel('Time (s)')
  axs[3].legend()
  plt.suptitle('Spacecraft Attitude Over Time')
  plt.show() 

  return None





