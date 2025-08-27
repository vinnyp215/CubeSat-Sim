# File: ground_station
# This file contains the ground station class for the simulation

class GroundStation:
  """
  Represents a ground station that can communicate with the CubeSat.
  """
  def __init__(self, name, latitude, longitude, altitude):
    """
    Initializes the ground station with its location and name.

    Args:
      name (str): Name of the ground station.
      latitude (float): Latitude in degrees.
      longitude (float): Longitude in degrees.
      altitude (float): Altitude in meters.
    """
    self.name = name
    self.latitude = latitude
    self.longitude = longitude
    self.altitude = altitude

  def get_location(self):
    """
    Returns the location of the ground station.

    Returns:
      tuple: (latitude, longitude, altitude)
    """
    return (self.latitude, self.longitude, self.altitude)