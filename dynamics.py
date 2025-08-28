# File: dynamics
# This file contains the dynamics equations for the CubeSat simulation.

import numpy as np 
import scipy as sp
import constants

from helper_functions import calculate_a_g, quaternion_derivative

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

    dwdt = [0.1, 0.1, 0]  # Placeholder for angular acceleration
    
    # Pack derivatives into a single state derivative vector
    state_derivative = np.zeros(13)
    state_derivative[0:3] = drdt    # dr/dt = v
    state_derivative[3:6] = dvdt    # dv/dt = a
    state_derivative[6:10] = dqdt   # dq/dt
    state_derivative[10:13] = dwdt  # dω/dt
    
    return state_derivative
