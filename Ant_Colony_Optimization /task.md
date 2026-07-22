# Swarm Intelligence: Vehicle Routing Problem via Ant Colony Optimization

## System Overview
This notebook implements an **Ant Colony Optimization (ACO)** algorithm to solve a constrained version of the **Vehicle Routing Problem (VRP)**. 

The VRP is a computationally complex generalization of the Traveling Salesman Problem (TSP) heavily utilized in commercial logistics. The objective of this system is to optimize the delivery of shipments from a central depot to various customer locations. The algorithm must find a set of delivery routes that strictly fulfills all customer demands while mathematically minimizing both the total number of distribution vehicles deployed and the cumulative physical distance traveled.

---

## Algorithmic Architecture & Constraints

### 1. Environment & Constraints
The state-space is instantiated via XML datasets containing geographical and logistical parameters:
* **Graph Nodes:** 2D Cartesian coordinates defining the central depot (Type 0) and customer delivery locations (Type 1).
* **Fleet Constraints:** The system assumes a single central depot operating an unlimited fleet of identical vehicles, each bounded by a strict maximum cargo capacity.
* **Demand Fulfillment:** Every customer node possesses a specific shipment demand that must be completely satisfied without exceeding the assigned vehicle's capacity constraint on any given route.

### 2. Swarm Mechanics (ACO)
Because exhaustively searching the state-space of all possible multi-vehicle routes is computationally unfeasible, this system utilizes a probabilistic, biology-inspired swarm algorithm:
* **Pheromone Matrix:** "Ants" (agents) construct delivery routes probabilistically, weighted by heuristic desirability (inverse distance) and simulated pheromone trails left by previous successful agents.
* **Pheromone Update & Evaporation:** After each generation, routes with lower total costs (fewer vehicles and shorter distances) receive higher pheromone deposits, reinforcing optimal paths. A decay factor (evaporation) prevents the swarm from converging prematurely on local optima.
* **Route Termination:** An agent returns to the central depot to deploy a new vehicle whenever its current capacity cannot fulfill the next target node's demand.

---

## Benchmark Results & Telemetry
The algorithmic stability and optimization capabilities are systematically evaluated across three escalating XML datasets (two small instances, one large instance).

* **Convergence Tracking:** The system utilizes `matplotlib` to track generational progression, visualizing how the swarm's best-found routing cost dynamically minimizes over time.
* **Optimal Discoveries:** The notebook logs the absolute best state-configuration (minimum vehicles used and shortest route configuration) discovered for each of the three dataset instances.

---

## Execution Instructions
1. Ensure the three target `XML` instance files are located in the same working directory as this `.ipynb` file.
2. Run the execution blocks sequentially. The script will dynamically parse the XML environments, execute the Ant Colony optimization pipeline, and generate matplotlib convergence graphs alongside the final optimized routing logs.
