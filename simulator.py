import numpy as np 
import scipy as sp

# File: simulator
# This file contains the simulation loop and time integration methods for the CubeSat.

class Simulator:
  """
  Manages the simulation loop and updates state of spacecraft
  """
  def __init__ (self, spacecraft, time_step, total_time):
    """
    Initializes the simulator with a CubeSat instance and simulation parameters.

    Args:
      spacecraft: Instance of a spacecraft class.
      time_step (float): Time step for the simulation in seconds.
      total_time (float): Total simulation time in seconds.
    """
    self.spacecraft = spacecraft
    self.time_step = time_step
    self.total_time = total_time
    self.current_time = 0

  def run_simulation(self, duration):
    """
    Runs the simulation for the specified duration.

    Args:
      duration (float): Duration to run the simulation in seconds.

    Returns: 
      sim_results: Data structure containing the simulation results. 
    """
    num_steps = int(duration / self.time_step)
    print(f"Running simulation for {duration} seconds with {num_steps} steps")
    
    # Integrate using Runge-Kutta method
    self.sim_results = {
        'time': np.zeros(num_steps),
        'position': np.zeros((num_steps, 3)),
        'velocity': np.zeros((num_steps, 3)),
        'attitude': np.zeros((num_steps, 4)),
        'angular_velocity': np.zeros((num_steps, 3))
    }

    print(f"Simulation finished")
    return self.sim_results 
   

      

