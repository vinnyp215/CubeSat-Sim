# File: simulator
# This file contains the simulation loop and time integration methods for the CubeSat.

import numpy as np 
import scipy as sp
from dynamics import dynamics
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

    # Initialize results structure
    self.sim_results = {
        'time': np.zeros(num_steps),
        'position': np.zeros((num_steps, 3)),
        'velocity': np.zeros((num_steps, 3)),
        'attitude': np.zeros((num_steps, 4)),
        'angular_velocity': np.zeros((num_steps, 3))
    }

    # Stack state vector
    y0 = np.hstack([
      self.spacecraft.r,
      self.spacecraft.v,
      self.spacecraft.q,
      self.spacecraft.w
    ])

    # Integration over time using Runge-Kutta 45
    sim_results = sp.integrate.solve_ivp(
      dynamics,
      [0, duration],
      y0,
      t_eval = np.linspace(0, duration, num_steps),
      method = 'RK45',
      rtol = 1e-6,
      atol = 1e-9
    )

    # Update spacecraft state to last value
    self.spacecraft.position = sim_results.y[0:3]
    self.spacecraft.velocity = sim_results.y[3:6]
    self.spacecraft.attitude = sim_results.y[6:10]
    self.spacecraft.angular_velocity = sim_results.y[10:13]

    print(f"Simulation finished")
    
    return self.sim_results 
   

      

