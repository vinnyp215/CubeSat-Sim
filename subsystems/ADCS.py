#File: ADCS
# This file contains the ADCS (Attitude Determination and Control System) class for the CubeSat simulation.

import numpy as np

from helper_functions import quaternion_multiply

from constants import B_earth

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
  
  def control_algorithms(self, q, w):
    """
    Function to determine control torques based on attitude error and available actuators.
    
    Args:
      q (np.array): Current attitude quaternion.
      w (np.array): Current angular velocity vector.
    
    Returns:
      rw_torque (np.array): Torque from reaction wheels.
      mt_torque (np.array): Torque from magnetorquers.      
    """

    if 'reaction_wheel' in self.actuators:
      # Simple PD controller for reaction wheels
      Kp = 0.1  # Proportional gain
      Kd = 0.05  # Derivative gain  

      q_t = np.array([1, 0, 0, 0]) # Target quaternion

      q_inv = np.array([q[0], -q[1], -q[2], -q[3]]) # Inverse of current quaternion

      q_e = quaternion_multiply(q_t, q_inv) # Calculate quaternion error

      rw_torque = (-Kp * np.sign(q_e[0]) * q_e[1:]) - (Kd * w) # Control law
    else:
      rw_torque = np.zeros(3)
      pass
  
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
  
def quaternion_multiply(q1, q2):
    """
    Performs Hamilton product of two quaternions.
    """
    w1, x1, y1, z1 = q1
    w2, x2, y2, z2 = q2
    
    w = w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2
    x = w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2
    y = w1 * y2 - x1 * z2 + y1 * w2 + z1 * x2
    z = w1 * z2 + x1 * y2 - y1 * x2 + z1 * w2

    return np.array([w, x, y, z])