#File: ADCS
# This file contains the ADCS (Attitude Determination and Control System) class for the CubeSat simulation.

import numpy as np

from helper_functions import quaternion_multiply

from constants import B_earth
from spacecraft_config import K_mt, K_p, K_d

class ADCS:
  """
  Represents an Attitude Determination and Control System for a spacecraft.
  
  Attributes:
    sensors (list): List of sensors used for attitude determination.
    actuators (list): List of actuators used for attitude control.

  Methods:
    __init__: Initialises the ADCS with given sensors and actuators.
    determine_attitude: Placeholder for attitude determination logic.
    control_algorithms: Determines control torques based on attitude error and available actuators.
  """

  def __init__(self, sensors, actuators):
    """
    Initisalises the ADCS with given sensors and actuators
    
    Args:
      sensors (list): List of sensors used for attitude determination.
      actuators (list): List of actuators used for attitude control.
    
    Returns:
      None
    """

    self.sensors = sensors
    self.actuators = actuators

    return None
  
  def determine_attitude(self):
    # Placeholder for attitude determination logic

    return None
    """
    Function to determine control torques based on attitude error and available actuators.
    
    Args:
      q (np.array): Current attitude quaternion.
      w (np.array): Current angular velocity vector.
    
    Returns:
      rw_torque (np.array): Torque from reaction wheels.
      mt_torque (np.array): Torque from magnetorquers.      
    """
  
    if 'magnetorquer' in self.actuators:
      # Simple B-dot algorithm
      dBdt = np.cross(B_earth, w)
      K_mt = 100 # Control gain factor
      mag_moment = np.dot(-K_mt, dBdt) # Magnetic dipole moment according to B-dot algorithm

      mt_torque = np.cross(mag_moment, B_earth)
    else:
      mt_torque = np.zeros(3)
      pass

    return rw_torque, mt_torque

def rw_control(q, w):
  """
  Function to determine reaction wheel torque

  Args:
    q (np.array): Current attitude quaternion
    w (np.array): Current angular velocity vector

  Returns:
    rw_torque (np.array): Torque from reaction wheels
  """
  # Simple PD controller for reaction wheels
  # K_p = 0.1  # Proportional gain
  # K_d = 0.1  # Derivative gain  

  q_t = np.array([1, 0, 0, 0]) # Target quaternion

  q_inv = np.array([q[0], -q[1], -q[2], -q[3]]) # Inverse of current quaternion

  q_e = quaternion_multiply(q_t, q_inv) # Calculate quaternion error

  rw_torque = (-K_p * np.sign(q_e[0]) * q_e[1:]) - (K_d * w) # Control law

  # Enforce maximum torque
  max_rw_torque = 0.001 # Max torque value in both directions

  for i in range(3):
    if rw_torque[i] > max_rw_torque:
      rw_torque[i] = max_rw_torque
    elif rw_torque[i] < -max_rw_torque:
      rw_torque[i] = -max_rw_torque
 
  return rw_torque
  
def mt_control(w):
  """
  Function to determine magnetorque torque

  Args:
    w (np.array): Current angular velocity vector

  Returns:
    mt_torque (np.array): Torque from magnetorquer
  """
  # Simple B-dot algorithm
  dBdt = np.cross(B_earth, w)
  #K_mt = 100 # Control gain factor
  mag_moment = np.dot(-K_mt, dBdt) # Magnetic dipole moment according to B-dot algorithm

  # Enforce maximum dipole moment
  max_mag_moment = 1 # Max dipole moment in both directions

  for i in range(3):
    if mag_moment[i] > max_mag_moment:
      mag_moment[i] = max_mag_moment
    elif mag_moment[i] < -max_mag_moment:
      mag_moment[i] = max_mag_moment

  mt_torque = np.cross(mag_moment, B_earth) 

  return mt_torque