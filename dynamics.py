# File: dynamics
# This file contains the dynamics equations for the CubeSat simulation.

import numpy as np 
import scipy as sp
import constants

from subsystems.ADCS import ADCS

def dynamics(t, state):
    """
    Computes the time derivative of the state vector for the CubeSat.
    
    Args:
        t (float): Current time in seconds.
        state (np.array): Current state vector [x, y, z, vx, vy, vz, q0, q1, q2, q3, wx, wy, wz].
        
    Returns:
        state_derivative (np.array): Time derivative of the state vector.
    """

    # Unpack state vector
    r = state[0:3]    # Position [x, y, z]
    v = state[3:6]    # Velocity [vx, vy, vz]
    q = state[6:10]   # Attitude quaternion [q0, q1, q2, q3]
    w = state[10:13]  # Angular velocity [wx, wy, wz]
    
    # Translational dynamics (position and velocity)
    drdt = v
    dvdt = calculate_a_g(r) # Gravitational acceleration
        
    # Calculate quaternion derivative
    dqdt = quaternion_derivative(q, w)
    
    # # Calculate torque from ADCS (if any)
    # adcs = ADCS(sensors=['sun_sensor', 'magnetometer'], actuators=['reaction_wheel', 'magnetorquer'])
    # rw_torque, mt_torque = adcs.control_algorithms(q, w)
    # total_torque = rw_torque + mt_torque

    # # Rotational dynamics (Euler's equation)
    # dwdt = np.linalg.inv(constants.I) @ (total_torque - np.cross(w, constants.I @ w))

    dwdt = np.zeros(3)  # Placeholder for angular acceleration (no control torques applied)
    
    # Pack derivatives into a single state derivative vector
    state_derivative = np.zeros(13)
    state_derivative[0:3] = drdt    # dr/dt = v
    state_derivative[3:6] = dvdt    # dv/dt = a
    state_derivative[6:10] = dqdt   # dq/dt
    state_derivative[10:13] = dwdt  # dω/dt
    
    return state_derivative

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
