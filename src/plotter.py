"""
Visualization utilities.

This module handles plotting and saving simulation results.
"""

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


def plot_results(times, theta, omega, show_plots=True):
    """
    Plot and save angular position and angular velocity versus time.

    Args:
        times: Time vector [s]
        theta: Angular position history [rad]
        omega: Angular velocity history [rad/s]
        show_plots: If True, display plots on screen
    """
    results_dir = Path("results")
    results_dir.mkdir(exist_ok=True)

    theta_deg = np.degrees(theta)

    # Angular position in radians
    plt.figure()
    plt.plot(times, theta)
    plt.title("Angular Position vs Time (Radians)")
    plt.xlabel("Time [s]")
    plt.ylabel("Theta [rad]")
    plt.grid()
    plt.tight_layout()
    plt.savefig(results_dir / "angular_position_rad.png", dpi=300)

    if show_plots:
        plt.show(block=False)

    # Angular position in degrees
    plt.figure()
    plt.plot(times, theta_deg)
    plt.title("Angular Position vs Time (Degrees)")
    plt.xlabel("Time [s]")
    plt.ylabel("Theta [deg]")
    plt.grid()
    plt.tight_layout()
    plt.savefig(results_dir / "angular_position_deg.png", dpi=300)

    if show_plots:
        plt.show(block=False)

    # Angular velocity
    plt.figure()
    plt.plot(times, omega)
    plt.title("Angular Velocity vs Time")
    plt.xlabel("Time [s]")
    plt.ylabel("Omega [rad/s]")
    plt.grid()
    plt.tight_layout()
    plt.savefig(results_dir / "angular_velocity.png", dpi=300)

    if show_plots:
        plt.show(block=False)
        plt.pause(0.1)

    plt.close("all")