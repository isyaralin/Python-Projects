# Python Engineering & AI Portfolio

These projects reflect my focus on writing clean, efficient code to solve complex, NP-hard problems.

## Technical Highlights & Domains

### 1. Reinforcement Learning & Evolutionary Algorithms
* **Neuroevolution for RL:** Instead of using standard backpropagation, I wrote an evolutionary algorithm to directly optimize neural network weights to solve Gymnasium control environments (CartPole-v1, Acrobot-v1).
* **Swarm Intelligence Logistics:** Built an Ant Colony Optimization (ACO) algorithm to solve the Vehicle Routing Problem (VRP). It figures out the best way to route multiple delivery vehicles while minimizing the fleet size and total travel distance.
* **Knapsack Optimization:** A stochastic solver for the 0/1 Knapsack problem. I used single-point crossover, bit-flip mutation, and a custom repair function to handle strict weight constraints on high-dimensional datasets.

### 2. Artificial Intelligence & Heuristic Search
* **A* Pathfinding & Custom Heuristics:** Implemented consistent, monotone A* heuristics to navigate infinite 2D and 3D grids, handling specific movement rules like diagonal, rook, and jumper steps.
* **Probabilistic Minesweeper Agent:** An autonomous solver that plays Minesweeper by combining Constraint Satisfaction (CSP) for deterministic safe moves with exact conditional probabilities for the risky ones.

### 3. Constraint Satisfaction & Logic Solvers
* **3-Partition to SAT:** Encoded the NP-complete 3-Partition problem into Boolean satisfiability (SAT) clauses so it could be evaluated by a standard SAT solver (`python-sat`).
* **Graph Total Coloring:** Wrote a CSP solver using `python-constraint` and `networkx` to calculate the total chromatic number for arbitrary undirected graphs.

### 4. Machine Learning
* **Decision Tree Classification:** Built a binary classifier using `scikit-learn` to predict medical outcomes. The project heavily focuses on hyperparameter tuning and checking model stability across different train/test splits.

## Technical Stack & Libraries
* **Languages:** Python
* **Machine Learning & RL:** `scikit-learn`, `gymnasium`
* **AI & Optimization:** `python-sat`, `python-constraint`, `networkx`
* **Data Processing & Plotting:** `matplotlib`, `numpy`, `pandas`
* **Testing:** Multi-seed statistical validations, unit test suites, and strict runtime benchmarking

## Directory Overview
Each directory contains its own `task.md` detailing the problem architecture, performance bounds, and execution guidelines.

* **[`neuroevolution_rl/`](./neuroevolution_rl)** – Neuroevolutionary agent for Gymnasium control environments.
* **[`Ant_Colony_Optimization/`](./Ant_Colony_Optimization)** – ACO solver for the Vehicle Routing Problem.
* **[`Knapsack/`](./Knapsack)** – Evolutionary Algorithm for the 0/1 Knapsack Problem.
* **[`Minesweeper Solver/`](./Minesweeper%20Solver)** – Probabilistic and CSP-based Minesweeper solver.
* **[`A* Search Algorithm/`](./A*%20Search%20Algorithm)** – Monotone heuristic pathfinding engine.
* **[`DesicionTree_ML/`](./DesicionTree_ML)** – Decision tree classifier and parameter stability analysis.
* **[`CSP_Graph/`](./CSP_Graph)** – Constraint Satisfaction solver for graph total coloring.
* **[`Partition_SAT/`](./Partition_SAT)** – 3-Partition reduction to Boolean Satisfiability (SAT).
