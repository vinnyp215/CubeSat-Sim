#File: ADCS
# This file contains the ADCS (Attitude Determination and Control System) class for the CubeSat simulation.

import numpy as np

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
      q (no.array): Current attitude quaternion.
      w (np.array): Current angular velocity vector.
    
    Returns:
      rw_torque (np.array): Torque from reaction wheels.
      mt_torque (np.array): Torque from magnetorquers.      
    """

    if 'reaction_wheel' in self.actuators:
      # Simple PD controller for reaction wheels
      Kp = 0.1  # Proportional gain
      Kd = 0.05  # Derivative gain  

      attitude_error = q - np.array([1, 0, 0, 0])  # Assuming desired quaternion is [1,0,0,0]
      rw_torque = -Kp * attitude_error[1:4] - Kd * w
    else:
      pass
  
    if 'magnetorquer' in self.actuators:
      # Simple B-dot algorithm
      dBdt = np.cross(B_earth, w)
      K_mt = 100 # Control gain factor
      mag_moment = np.dot(-K_mt, dBdt) # Magnetic dipole moment according to B-dot algorithm

      mt_torque = np.cross(mag_moment, B_earth)
    else:
      pass

    return rw_torque, mt_torque
  
