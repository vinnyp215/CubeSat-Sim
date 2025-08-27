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

    y0 = np.hstack([
      self.spacecraft.r0,
      self.spacecraft.v0,
      self.spacecraft.q0,
      self.spacecraft.w0
    ])

    #def rhs(t, y):
    #  return dynamics(t, y, self.spacecraft)

    rk45 = sp.integrate.RK45(
      dynamics,
      t0=0,
      y0=y0,
      t_bound=duration,
      max_step=self.time_step
    )

    step = 0
    while rk45.status == 'running' and step < num_steps:
      rk45.step()
      self.sim_results['time'][step] = rk45.t
      self.sim_results['position'][step] = rk45.y[0:3]
      self.sim_results['velocity'][step] = rk45.y[3:6]
      self.sim_results['attitude'][step] = rk45.y[6:10]
      self.sim_results['angular_velocity'][step] = rk45.y[10:13]
      step += 1

    # Update spacecraft state to last value
    self.spacecraft.position = rk45.y[0:3]
    self.spacecraft.velocity = rk45.y[3:6]
    self.spacecraft.attitude = rk45.y[6:10]
    self.spacecraft.angular_velocity = rk45.y[10:13]

    print(f"Simulation finished")
    return self.sim_results 
   

      

