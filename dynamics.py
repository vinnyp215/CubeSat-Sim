import numpy as np 
import scipy as sp

# File: dynamics
# This file contains the dynamics equations for the CubeSat simulation.

import constants 
mu_earth = constants.mu_earth

def calculate_gravity(r):
    """
    Calculates the central body gravitational force on a body
    at a given position, neglecting perturbations.
    
    Args:
        r (np.array): Position vector in meters [x, y, z].
        
    Returns:
        np.array: The acceleration vector [ax, ay, az] in m/s^2.
    """
    r_mag = np.linalg.norm(r)
    
    # Gravitational acceleration (inverse square law)
    a_g = -mu_earth / r_mag**3 * r

    return a_g

