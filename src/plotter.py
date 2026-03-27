"""
Visualization utilities.

This module handles plotting and saving simulation results.
"""

from pathlib import Path
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

    # Plot 1: Angular position
    plt.figure()
    plt.plot(times, theta)
    plt.title("Angular Position vs Time")
    plt.xlabel("Time [s]")
    plt.ylabel("Theta [rad]")
    plt.grid()
    plt.tight_layout()
    plt.savefig(results_dir / "angular_position.png", dpi=300)

    if show_plots:
        plt.show(block=False)

    # Plot 2: Angular velocity
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

    if show_plots:
        plt.pause(0.1)

    plt.close("all")