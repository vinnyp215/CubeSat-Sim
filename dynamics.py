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

def quaternion_derivative(q, omega):
    """
    Calculates the time derivative of the attitude quaternion.
    
    Args:
        q (np.array): Attitude quaternion [q0, q1, q2, q3].
        omega (np.array): Angular velocity vector [wx, wy, wz] in rad/s.
        
    Returns:
        np.array: Time derivative of the quaternion [dq0/dt, dq1/dt, dq2/dt, dq3/dt].
    """
    q0, q1, q2, q3 = q
    wx, wy, wz = omega
    
    dqdt = 0.5 * np.array([
        -q1*wx - q2*wy - q3*wz,
         q0*wx + q2*wz - q3*wy,
         q0*wy - q1*wz + q3*wx,
         q0*wz + q1*wy - q2*wx
    ])
    
    return dqdt

def dynamics(t, state):
    """
    Computes the time derivative of the state vector for the CubeSat.
    
    Args:
        t (float): Current time in seconds.
        state (np.array): Current state vector [x, y, z, vx, vy, vz, q0, q1, q2, q3, wx, wy, wz].
        
    Returns:
        np.array: Time derivative of the state vector.
    """
    # Unpack state vector
    r = state[0:3]      # Position [x, y, z]
    v = state[3:6]      # Velocity [vx, vy, vz]
    q = state[6:10]     # Attitude quaternion [q0, q1, q2, q3]
    omega = state[10:13] # Angular velocity [wx, wy, wz]
    
    # Translational dynamics (position and velocity)
    dr_dt = v
    dv_dt = calculate_gravity(r)
        
    # Calculate quaternion derivative
    dqdt = quaternion_derivative(q, omega)
    
    # Assume no external torques for now (can be expanded later)
    domegadt = np.zeros(3)
    
    # Pack derivatives into a single state derivative vector
    state_derivative = np.zeros(13)
    state_derivative[0:3] = v          # dr/dt = v
    state_derivative[3:6] = a          # dv/dt = a
    state_derivative[6:10] = dqdt      # dq/dt
    state_derivative[10:13] = domegadt  # dω/dt
    
    return state_derivative

