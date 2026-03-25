"""
Attitude dynamics equations.

This module contains the physical model of the system.
For version 1, a simple 1-axis rigid body rotational model is used.
"""

def compute_angular_acceleration(torque_nm: float, inertia_kgm2: float) -> float:
    """
    Compute angular acceleration from applied torque and inertia.

    Equation:
        alpha = torque / inertia

    Args:
        torque_nm: Applied torque [N*m]
        inertia_kgm2: Moment of inertia [kg*m^2]

    Returns:
        Angular acceleration [rad/s^2]
    """
    return torque_nm / inertia_kgm2