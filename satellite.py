# File: satellite
# This file contains the CubeSat class definition 

import numpy as np

class CubeSat: 
  """
  Represents a CubeSat with its physical properties and state vectors.

  Attributes:
    mass (float): Mass of the CubeSat in kilograms.
    dimensions (tuple): Dimensions of the CubeSat in meters (length, width, height).
    position (np.array): Position vector of the CubeSat in meters.
    attitude (np.array): Attitude quaternion of the CubeSat.
    velocity (np.array): Velocity vector of the CubeSat in meters per second.
    angular_velocity (np.array): Angular velocity vector of the CubeSat in radians per second.

  Subsystems:
    adcs (ADCS): Attitude Determination and Control System instance.
    power (Power): Power subsystem instance.
    comms (Comms): Communications subsystem instance.
    thermal (Thermal): Thermal subsystem instance.

  Time Properties:
    time (float): Current simulation time in seconds.
    time_step (float): Time step for the simulation in seconds.
    total_time (float): Total simulation time in seconds.

  Methods:
    __init__: Initializes the CubeSat with given parameters.
  """

  def __init__ (self, mass, dimensions, r0, v0, q0, w0, I, I_inv):
    """
    Initializes the CubeSat with given parameters.

    Args:
      mass (float): Mass of the CubeSat in kilograms.
      dimensions (tuple): Dimensions of the CubeSat in meters (length, width, height).
      r0 (np.array): Initial position vector in meters.
      v0 (np.array): Initial velocity vector in meters per second.
      q0 (np.array): Initial attitude quaternion.
      w0 (np.array): Initial angular velocity vector in radians per second.
    """

    self.mass = mass  # Mass of the Cube
    self.dimensions = dimensions  # Dimensions (length, width, height) in meters
    self.r = np.array(r0)  # Position vector in meters
    self.v = np.array(v0)  # Velocity vector in meters per second
    self.q = np.array(q0)  # Attitude quaternion
    self.w = np.array(w0)  # Angular velocity vector in radians per second
    self.I = I   # Inertia matrix
    self.I_inv = I_inv # Inverse of inertia matrix


