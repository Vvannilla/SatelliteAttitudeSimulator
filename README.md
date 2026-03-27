## Satellite Attitude Simulator

This project implements a modular simulation of satellite rotational dynamics (attitude) using a rigid body model and discrete-time numerical integration.

It serves as a foundation for understanding and developing Guidance, Navigation, and Control (GNC) systems.

The simulator is structured to keep configuration, dynamics, simulation flow, and visualization separated, following a clean and scalable engineering approach.

## Current Features
- 1-axis rotational dynamics
- Modular project structure
- Angular position and angular velocity plots

## System Overview

The system models 1-axis rotational motion using:

- Torque input
- Moment of inertia
- Angular velocity
- Angular position

The simulation uses Euler integration to propagate system states over time.

## How to Run

```bash
pip install -r requirements.txt
python -m src.main

## Next Steps
- PID attitude control
- 3-axis dynamics
- Reaction wheel modeling
- State estimation

