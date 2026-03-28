"""
Simulation configuration parameters.

This module centralizes all tunable values used by the simulator.
"""

INERTIA_KGM2 = 0.05       # Moment of inertia [kg*m^2]

THETA0_RAD = 0.0          # Initial angular position [rad]
OMEGA0_RAD_S = 0.1        # Initial angular velocity [rad/s]

THETA_TARGET_RAD = 1.0    # Desired angular position [rad]
KP = 0.5                  # Propotional gain
KD = 0.3                  # Derivative gain

DT_S = 0.01               # Simulation time step [s]
T_FINAL_S = 50.0          # Total simulation time [s]