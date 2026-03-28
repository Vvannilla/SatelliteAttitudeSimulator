"""
Visualization utilities.

This module handles plotting and saving simulation results.
"""

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


def plot_results(times, theta, omega, torque_cmd, error_hist, theta_target, show_plots=True):
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
    plt.plot(times, theta, label="Theta")
    plt.axhline(y=theta_target, linestyle="--", label="Target")
    plt.title("Angular Position vs Time (Radians)")
    plt.xlabel("Time [s]")
    plt.ylabel("Theta [rad]")
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.savefig(results_dir / "angular_position_rad.png", dpi=300)

    if show_plots:
        plt.show(block=False)

    # Angular position in degrees
    plt.figure()
    plt.plot(times, theta_deg, label="Theta")
    plt.axhline(y=np.degrees(theta_target), linestyle="--", label="Target")
    plt.title("Angular Position vs Time (Degrees)")
    plt.xlabel("Time [s]")
    plt.ylabel("Theta [deg]")
    plt.legend()
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

    # Error vs Time
    plt.figure()
    plt.plot(times, error_hist)
    plt.title("Attitude Error vs Time")
    plt.xlabel("Time [s]")
    plt.ylabel("Error [rad]")
    plt.grid()
    plt.savefig(results_dir / "attitude_error.png", dpi=300)
    if show_plots:
        plt.show(block=False)

    # Torque vs Time
    plt.figure()
    plt.plot(times, torque_cmd)
    plt.title("Control Torque vs Time")
    plt.xlabel("Time [s]")
    plt.ylabel("Torque [Nm]")
    plt.grid()
    plt.savefig(results_dir / "control_torque.png", dpi=300)
    if show_plots:
        plt.show(block=False)

    plt.close("all")

