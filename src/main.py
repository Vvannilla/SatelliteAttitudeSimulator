"""
Application entry point.

This module coordinates configuration, simulation, and visualization.
"""

from src.config import (
    INERTIA_KGM2,
    TORQUE_NM,
    THETA0_RAD,
    OMEGA0_RAD_S,
    DT_S,
    T_FINAL_S,
)
from src.simulator import run_simulation
from src.plotter import plot_results


def main():
    times, theta, omega = run_simulation(
        inertia_kgm2=INERTIA_KGM2,
        torque_nm=TORQUE_NM,
        theta0_rad=THETA0_RAD,
        omega0_rad_s=OMEGA0_RAD_S,
        dt_s=DT_S,
        t_final_s=T_FINAL_S,
    )

    plot_results(times, theta, omega)


if __name__ == "__main__":
    main()