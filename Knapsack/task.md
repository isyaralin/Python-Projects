# Evolutionary Computing: The 0/1 Knapsack Optimization Problem

## Mathematical Context & System Overview
This project tackles the classic 0/1 Knapsack Problem, a well-known NP-hard combinatorial optimization challenge. 

Given a set of $n$ objects, each with a specific weight ($w_i$) and price ($c_i$), the objective is to algorithmically discover the optimal subset of items that maximizes the total cumulative price without exceeding the strict weight capacity limit ($W$) of the knapsack.

The mathematical formulation optimized by the system is:
$$\max \sum_{i=1}^{n} c_i x_i \quad \text{subject to} \quad \sum_{i=1}^{n} w_i x_i \leq W$$
where $x_i \in \{0, 1\}$ dictates the inclusion or exclusion of the $i$-th object.

---

## Algorithmic Architecture & Technical Approach
Because the state space of possible combinations grows exponentially as $O(2^n)$, exhaustive brute-force search is computationally unfeasible for large datasets. To solve this efficiently, the system implements a stochastic **Evolutionary Algorithm (EA)**.

The architecture is built upon the following core genetic operations:
* **Chromosome Encoding:** Candidate solutions are represented as binary bitstrings, where each bit explicitly maps to the inclusion state of a specific item.
* **Genetic Recombination:** The algorithm utilizes **single-point crossover** mechanisms to share high-performing genetic information between parent solutions during reproduction.
* **Exploration & Mutation:** To maintain population diversity and escape local optima, a **bit-flip mutation** strategy is applied across generations.
* **Fitness Evaluation:** The fitness function directly maps to the cumulative price of the knapsack, with heavy penalization applied to any chromosome that exceeds the capacity constraint $W$.

---

## Performance Evaluation & Scalability Boundaries
The algorithm's stability and optimization capabilities are systematically evaluated across increasingly complex environments to verify scalability.

* **Validation Datasets:** Initial algorithmic correctness is verified against known optimal solutions for small search spaces ($n=10$ and $n=20$).
* **Stress Testing:** The engine is deployed against highly complex, high-dimensional datasets ($n=100$ and $n=1000$) to demonstrate the algorithm's ability to converge on near-optimal solutions efficiently.
* **Telemetry & Visualization:** Generational progression, population variance, and fitness convergence rates are tracked and visualized dynamically utilizing `matplotlib`.

---

## Repository Structure

```text
knapsack_evolutionary/
├── README.md                 # System execution instructions and parameter documentation
├── task.md                   # Problem formulation and algorithmic constraints (This file)
├── knapsack_ea.py            # Core evolutionary algorithm implementation
├── data/                     # Dimensional dataset limits (10, 20, 100, and 1000 object files)
└── visualizations/           # Matplotlib convergence graphs mapping fitness over generations
