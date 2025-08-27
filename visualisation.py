# File: visualisation
# This file contains functions for the visualisation of simulation results

import numpy as np
import matplotlib.pyplot as plt
import constants as const

def plot_trajectory(sim_results):
  """
  Plots the trajectory of the spacecraft from the simulation results.
  
  Args:
    sim_results: Data structure containing the simulation results.
    
  Returns:
    None
  """

  # Unpacked simualation results
  time = sim_results['time']
  position = sim_results['position']
  velocity = sim_results['velocity']
  attitude = sim_results['attitude']
  angular_velocity = sim_results['angular_velocity']

  # Plotting the trajectory in 3D
  fig = plt.figure()
  ax = fig.add_subplot(111, projection='3d')
  ax.plot(position[:,0], position[:,1], position[:,2])
  ax.set_title('Spacecraft Trajectory')
  ax.set_xlabel('X (m)')
  ax.set_ylabel('Y (m)')
  ax.set_zlabel('Z (m)')
  plt.show()

  # Add Earth to plot
  u = np.linspace(0, 2 * np.pi, 100)
  v = np.linspace(0, np.pi, 100)
  x = const.R_earth * np.outer(np.cos(u), np.sin(v))
  y = const.R_earth * np.outer(np.sin(u), np.sin(v))
  z = const.R_earth * np.outer(np.ones(np.size(u)), np.cos(v))
  ax.plot_surface(x, y, z, color='b', alpha=0.3)
  plt.show()


