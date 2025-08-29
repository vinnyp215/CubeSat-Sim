# File: dynamics
# This file contains the dynamics equations for the CubeSat simulation.

import numpy as np 
# from spacecraft_config import I, I_inv

from helper_functions import calculate_a_g, quaternion_derivative, cross_product
# from subsystems.ADCS import rw_control, mt_control

def dynamics(t, state, spacecraft):
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

    # Normalize the quaternion to prevent drift
    q = q / np.linalg.norm(q)
    
    # Translational dynamics (position and velocity)
    drdt = v
    dvdt = calculate_a_g(r) # Gravitational acceleration
        
    # Rotational dynamics (attitude and angular velocity)
    dqdt = quaternion_derivative(q, w) # Calculate quaternion derivative
    
    # Calculate torque from ADCS (if any)    
    rw_torque = spacecraft.adcs.rw_control(q, w)
    mt_torque = spacecraft.adcs.mt_control(w)
    total_torque = rw_torque + mt_torque

    dwdt = spacecraft.I_inv @ (total_torque - cross_product(w, spacecraft.I @ w)) # Euler's equation
    
    # Pack derivatives into a single state derivative vector
    state_derivative = np.zeros(13)
    state_derivative[0:3] = drdt    # dr/dt = v
    state_derivative[3:6] = dvdt    # dv/dt = a
    state_derivative[6:10] = dqdt   # dq/dt
    state_derivative[10:13] = dwdt  # dω/dt
    
    return state_derivative
