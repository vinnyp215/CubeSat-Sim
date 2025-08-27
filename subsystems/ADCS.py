#File: ADCS
# This file contains the ADCS (Attitude Determination and Control System) class for the CubeSat simulation.

class ADCS:
  """
  Represents an Attitude Determination and Control System for a spacecraft.
  
  Attributes:
    sensors (list): List of sensors used for attitude determination.
    actuators (list): List of actuators used for attitude control.

  Methods:
    __init__: Initialises the ADCS with given sensors and actuators.
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