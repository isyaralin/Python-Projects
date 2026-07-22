# Reinforcement Learning using Neuroevolution

## Overview
This project focuses on solving reinforcement learning (RL) environments from the `gymnasium` library using a technique called **Neuroevolution**. 

Instead of using standard RL algorithms that rely on gradient descent (like Deep Q-Networks), this approach uses evolutionary algorithms to train an agent. Basically, the system evolves a population of neural networks over multiple generations to find the best policy for environments like **CartPole-v1** and **Acrobot-v1**.

---

## How It Works

### 1. The Neural Network Policy
* The agent makes decisions using a neural network. It takes the current state of the environment as input and outputs the action the agent should take.
* Instead of backpropagation, the network's weights are optimized using genetic operators (like crossover and mutation). 

### 2. Fitness and Evolution
* Each neural network (individual) plays the game, and its "fitness" score is simply the total reward it accumulates before the episode ends.
* The networks that perform the best are selected as parents. Their weights are combined and mutated to create the next generation of agents, which gradually improves the overall performance.

### 3. Testing and Validation
Because reinforcement learning environments can be highly random, it's important to prove that the agent actually learned a good strategy and didn't just get lucky. 
* The algorithm is run multiple times using different **random seeds**.
* The system tracks execution times, fitness caps, and calculates the average performance of the best individual in each generation across all runs to show true, stable learning.

---

## Repository Structure

```text
neuroevolution_rl/
├── README.md                 # Setup instructions and hyperparameter details
├── task.md                   # Project description (This file)
├── neuroevolution_agent.py   # Main code for the evolutionary loop and gym environments
└── visualizations/           # Graphs showing the fitness performance across multiple seeds
