"""
Simulation execution loop.

This module is responsible for propagating the system state over time.
"""

import numpy as np
from src.dynamics import compute_angular_acceleration


def run_simulation(
    inertia_kgm2: float,
    torque_nm: float,
    theta0_rad: float,
    omega0_rad_s: float,
    dt_s: float,
    t_final_s: float
):
    """
    Run a 1-axis satellite attitude simulation.

    Args:
        inertia_kgm2: Moment of inertia [kg*m^2]
        torque_nm: Applied torque [N*m]
        theta0_rad: Initial angular position [rad]
        omega0_rad_s: Initial angular velocity [rad/s]
        dt_s: Simulation step [s]
        t_final_s: End time [s]

    Returns:
        times: Time vector [s]
        theta: Angular position history [rad]
        omega: Angular velocity history [rad/s]
    """
    times = np.arange(0.0, t_final_s + dt_s, dt_s)
    theta = np.zeros_like(times)
    omega = np.zeros_like(times)

    theta[0] = theta0_rad
    omega[0] = omega0_rad_s

    for k in range(1, len(times)):
        alpha = compute_angular_acceleration(torque_nm, inertia_kgm2)

        omega[k] = omega[k - 1] + alpha * dt_s
        theta[k] = theta[k - 1] + omega[k - 1] * dt_s

    return times, theta, omega