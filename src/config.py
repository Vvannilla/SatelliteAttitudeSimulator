"""
Simulation configuration parameters.

This module centralizes all tunable values used by the simulator.
Keeping parameters here makes the project easier to maintain and scale.
"""

INERTIA_KGM2 = 0.05       # Moment of inertia [kg*m^2]
TORQUE_NM = .002          # Applied torque [N*m]

THETA0_RAD = 0.0          # Initial angular position [rad]
OMEGA0_RAD_S = 0.1        # Initial angular velocity [rad/s]

DT_S = 0.01               # Simulation time step [s]
T_FINAL_S = 10.0          # Total simulation time [s]