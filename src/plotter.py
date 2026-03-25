"""
Visualization utilities.

This module handles plotting of simulation results.
"""

import matplotlib.pyplot as plt


def plot_results(times, theta, omega):
    """
    Plot angular position and angular velocity versus time.
    """
    plt.figure()
    plt.plot(times, theta)
    plt.title("Angular Position vs Time")
    plt.xlabel("Time [s]")
    plt.ylabel("Theta [rad]")
    plt.grid()

    plt.figure()
    plt.plot(times, omega)
    plt.title("Angular Velocity vs Time")
    plt.xlabel("Time [s]")
    plt.ylabel("Omega [rad/s]")
    plt.grid()

    plt.show()