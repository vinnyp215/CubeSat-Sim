# File: helper_functions
# This file contains helper functions for the simulation. Created to avoid circular imports.

import numpy as np
import scipy as sp
import constants

def calculate_a_g(r):
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
    a_g = -constants.mu_earth / r_mag**3 * r

    return a_g

def quaternion_derivative(q, w):
    """
    Calculates the time derivative of the attitude quaternion.
    
    Args:
        q (np.array): Attitude quaternion [q0, q1, q2, q3].
        w (np.array): Angular velocity vector [wx, wy, wz] in rad/s.
        
    Returns:
        dqdt (np.array): Time derivative of the quaternion [dq0/dt, dq1/dt, dq2/dt, dq3/dt].
    """
    q0, q1, q2, q3 = q
    wx, wy, wz = w
    
    dqdt = 0.5 * np.array([
        -q1*wx - q2*wy - q3*wz,
         q0*wx + q2*wz - q3*wy,
         q0*wy - q1*wz + q3*wx,
         q0*wz + q1*wy - q2*wx
    ])
    
    return dqdt

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