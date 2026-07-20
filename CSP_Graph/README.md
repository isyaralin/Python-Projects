# Constraint Satisfaction Problems: Total Graph Coloring

## Mathematical Context & Overview
Total coloring of a graph is the coloring of its vertices and edges such that:
1. Vertices connected by an edge have different colors.
2. Edges sharing a common vertex have different colors.
3. Edges and their end-vertices have different colors.

The total chromatic number of a graph is the minimum number of colors required to achieve a valid total coloring. Finding this number for arbitrary graphs is a complex combinatorial problem.

---

## Project Objectives & Architecture
This project implements a dynamic algorithmic solver capable of finding the total chromatic number of arbitrary undirected graphs using Constraint Satisfaction Problems (CSP). 

The core logic is engineered to dynamically generalize to any given graph topology, generating optimal color mappings without relying on precomputed heuristics or hardcoded topological assumptions.

### Core Technical Specs
* **CSP Engine:** The constraint propagation logic and state-space search are implemented using the `python-constraint` library.
* **Graph Modeling:** Input graphs and network topologies are mapped, traversed, and manipulated using the `networkx` library.
* **Variable Optimization:** CSP variable identifiers are optimized as simple integer objects to minimize the solver's state-space search overhead and memory allocation.
* **Performance Bounds:** To ensure the constraint satisfaction algorithm is efficient and scalable, the implementation adheres to strict performance thresholds:
  * **Execution Limit:** Computations are capped at 60 seconds per complex graph suite.
  * **Memory Limit:** Maximum memory footprint is strictly capped at 1 GB to prevent state-space explosion.

---

## Repository Structure

```text
total_coloring_csp/
├── README.md               # Environment setup and dependencies (networkx, python-constraint)
├── task.md                 # Mathematical constraints and algorithmic specifications (This file)
├── total_csp.py            # Core CSP algorithm implementation calculating the total chromatic number
└── LICENSE                 # Open-source licensing parameters
