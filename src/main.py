"""
Application entry point.

This module coordinates configuration, simulation, and visualization.
"""

from src.config import (
    INERTIA_KGM2,
    THETA0_RAD,
    OMEGA0_RAD_S,
    THETA_TARGET_RAD,
    KP,
    KD,
    DT_S,
    T_FINAL_S,
)
from src.simulator import run_simulation
from src.plotter import plot_results


def main():
    times, theta, omega, torque_cmd, error_hist = run_simulation(
        inertia_kgm2=INERTIA_KGM2,
        theta_target_rad=THETA_TARGET_RAD,
        kp=KP,
        kd=KD,
        theta0_rad=THETA0_RAD,
        omega0_rad_s=OMEGA0_RAD_S,
        dt_s=DT_S,
        t_final_s=T_FINAL_S,
    )

    plot_results(times, theta, omega, show_plots=True)


if __name__ == "__main__":
    main()