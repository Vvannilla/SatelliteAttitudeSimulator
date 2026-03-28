"""
Simulation execution loop.

This module is responsible for propagating the system state over time.
Discrete-time implementation of rotational physics using Euler integration.
"""

import numpy as np
from src.dynamics import compute_angular_acceleration


def run_simulation(
    inertia_kgm2: float,
    theta_target_rad: float,
    kp: float,
    kd: float,
    theta0_rad: float,
    omega0_rad_s: float,
    dt_s: float,
    t_final_s: float
):
    """
    Run a 1-axis satellite attitude simulation.

    Args:
        inertia_kgm2: Moment of inertia [kg*m^2]
        theta_target_rad: Desired angular position [rad]
        kp: Proportional gain
        theta0_rad: Initial angular position [rad]
        omega0_rad_s: Initial angular velocity [rad/s]
        dt_s: Simulation step [s]
        t_final_s: End time [s]

    Returns:
        times: Time vector [s]
        theta: Angular position history [rad]
        omega: Angular velocity history [rad/s]
        torque_cmd: Control torque history [N*m]
        error_hist: Error history [rad]
    """
    times = np.arange(0.0, t_final_s + dt_s, dt_s)
    
    theta = np.zeros_like(times)
    omega = np.zeros_like(times)
    torque_cmd = np.zeros_like(times)
    error_hist = np.zeros_like(times)
    
    theta[0] = theta0_rad
    omega[0] = omega0_rad_s
    
    error_hist[0] = theta_target_rad - theta[0]
    torque_cmd[0] = kp * error_hist[0] - kd * omega[0]

    for k in range(1, len(times)):
        error = theta_target_rad - theta[k - 1]
        torque = kp * error - kd * omega[k - 1]

        alpha = compute_angular_acceleration(torque, inertia_kgm2)

        omega[k] = omega[k - 1] + alpha * dt_s
        theta[k] = theta[k - 1] + omega[k - 1] * dt_s
        error_hist[k] = error
        torque_cmd[k] = torque

    return times, theta, omega, torque_cmd, error_hist