
# Data Driven Autonomy
### - AI Car Simulation with NEAT

## Project Overview

This project is a simulation of an AI car driving on circuits without colliding with walls. It utilizes the NEAT (NeuroEvolution of Augmenting Topologies) module in Python to train the AI car. The project serves educational purposes and offers insights into the application of neural networks for autonomous navigation.

## Features

- AI car simulation on circuits.
- Collision avoidance with wall detection.
- NEAT module for training.
- Saving knowledge obtained during training.
- Planned integration of maps for real-world navigation.

## Table of Contents
- [Simulation Environment](#simulation-environment)
- [NEAT Module](#neat-module)
- [Training](#training)
- [Knowledge Base](#knowledge-base)
- [Integration of Maps](#integration-of-maps)
- [Real-World Application](#real-world-application)
- [Educational Purpose](#educational-purpose)
- [Sensors and Outputs](#sensors-and-outputs)
- [Complexities](#complexities)
- [Future Work](#future-work)
- [Acknowledgments](#acknowledgments)
- [Contact Information](#contact-information)

## Simulation Environment

The AI car operates in a simulated circuit environment. The simulation is created using PyGame and some custom made circuits using Photoshop.

## NEAT Module

The NEAT (NeuroEvolution of Augmenting Topologies) module is used to evolve the neural network that controls the AI car. It allows the network to adapt and improve its performance over time.

## Training

The AI car is trained on various tracks using NEAT. The training process involves feeding input data from distance sensors (forward, left, right, forward-left, and forward-right) to the neural network. The network learns to control the car's speed and angle to avoid collisions.

## Knowledge Base

The knowledge obtained during training is saved in a binary file. This knowledge base is used by the AI car during non-training phases to make intelligent decisions.

## Integration of Maps

Future plans include integrating maps to enable the AI car to navigate real-world roads based on map data, similar to applications like Google Maps.

## Real-World Application

The project has the potential for real-world application, such as implementing the neural network on a self-driving car. This, however, would require addressing various challenges and safety considerations.

## Educational Purpose

This project is designed primarily for educational purposes. It provides a simplified demonstration of the concepts involved.

## Sensors and Outputs

The neural network receives input data from five distance sensors (forward, left, right, forward-left, and forward-right) and generates speed and angle as outputs to control the AI car.

## Complexities

The project intentionally avoids excessive complexities to keep it accessible for educational purposes.

## Future Work

- Expand the project to integrate maps for real-world navigation.
- Optimize and improve the neural network's performance.
- Implement additional features for more realistic simulations.

## Acknowledgments

- Python-NEAT
- Neuro-Nine

## Contact Information

- [Naveen Kumar M](mailto:mnkincit22@gmail.com)
- [Arivarasan A](mailto:)

Feel free to reach out regrading any contribution ideas or willingness.

