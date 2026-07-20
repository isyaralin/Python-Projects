# A* Search Algorithm: Monotone Heuristics over Infinite Grids

## Business Context & Overview
This project focuses on advanced pathfinding algorithms within an Artificial Intelligence context. The objective is to design and implement highly optimized, **monotone (consistent) heuristics** for the A* search algorithm. 

The algorithm navigates through various complex, infinite grid environments. Because the state space is technically infinite and dynamically generated via an oracle (which determines if specific edges are present or removed to create subgraphs), the efficiency and mathematical correctness of the heuristic functions are critical. An inconsistent or overestimating heuristic will break optimal path guarantees, while an inefficient one will cause state-space explosions.

---

## Grid Environments & Movement Models
The A* algorithm must be equipped with custom heuristic functions capable of optimally navigating the following graph topologies:

* **Grid2D:** The classic two-dimensional orthogonal grid.
* **Grid3D:** The classic three-dimensional orthogonal grid.
* **GridDiagonal2D:** A 2D grid permitting diagonal traversal (e.g., movement between `(0,0)` and `(1,1)`).
* **GridAllDiagonal3D:** A 3D grid permitting both face diagonals and full space diagonals (e.g., movement between `(0,0,0)` and `(1,1,1)`).
* **GridFaceDiagonal3D:** A 3D grid permitting face diagonals but strictly restricting space diagonals.
* **GridRook2D:** Movement mimics a chess Rook, allowing orthogonal sliding up to a maximum distance of 8 cells per turn (e.g., `(0,0)` to `(0,8)` is valid, `(0,9)` is invalid).
* **GridGreatKing2D:** Movement mimics a modified chess King, capable of moving up to 8 cells across both coordinates simultaneously (e.g., `(0,0)` to `(-5,4)` is valid).
* **GridJumper2D:** An 8-regular graph utilizing an elongated Knight's jump. It moves exactly 3 cells along one coordinate axis and 2 cells along the other (e.g., `(0,0)` to `(2,-3)`).

---

## Engineering Constraints & Optimization
The heuristics must be strictly monotone and highly optimized to prevent excessive node expansion. The implementation must adhere to the following performance bounds:

* **State-Space Limits:** The algorithm must find the optimal path while visiting no more than **1,000,000 vertices** per test case.
* **Time Complexity:** Execution is hard-capped at **60 seconds** per grid topology. 
* **Memory Complexity:** Maximum memory footprint is capped at **1 GB**.
* **Mathematical Property:** *Hint utilized for jump-based grids:* Due to the discrete nature of the grid, fractional geometric distances map to integer boundaries (e.g., if a continuous calculation yields $> 5.5$, the discrete required steps jump to at least $6$).

---

## Repository Structure & Deliverables

```text
a_star_heuristics/
├── README.md                 # Project overview and execution instructions
├── task.md                   # Assignment constraints and grid specifications (This file)
├── heuristics.py             # Core implementation containing all 8 custom monotone heuristic functions
├── informed_search_tests.py  # Unit tests evaluating time limits, memory bounds, and expansion efficiency
├── monotonicity_tests.py     # Mathematical validation suite strictly checking heuristic consistency
└── LICENSE                   # Open-source licensing parameters
