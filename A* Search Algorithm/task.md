# A* Search Algorithm: Monotone Heuristics over Infinite Grids

## Context & Architecture Overview
This project focuses on advanced pathfinding algorithms within an Artificial Intelligence context. The core objective is the design and implementation of highly optimized, **monotone (consistent) heuristics** for the A* search algorithm. 

The algorithm is engineered to navigate through various complex, infinite grid environments. Because the state space is technically infinite and dynamically generated via an oracle (which determines if specific edges are present or removed to create valid subgraphs), the computational efficiency and mathematical correctness of the heuristic functions are critical. An inconsistent or overestimating heuristic breaks optimal path guarantees, while an inefficient one causes immediate state-space explosions.

---

## Grid Environments & Movement Models
The A* algorithm is equipped with custom heuristic functions designed to optimally navigate the following graph topologies:

* **Grid2D:** The classic two-dimensional orthogonal grid.
* **Grid3D:** The classic three-dimensional orthogonal grid.
* **GridDiagonal2D:** A 2D grid permitting diagonal traversal (e.g., movement between `(0,0)` and `(1,1)`).
* **GridAllDiagonal3D:** A 3D grid permitting both face diagonals and full space diagonals (e.g., movement between `(0,0,0)` and `(1,1,1)`).
* **GridFaceDiagonal3D:** A 3D grid permitting face diagonals but strictly restricting space diagonals.
* **GridRook2D:** Movement mimics a chess Rook, allowing orthogonal sliding up to a maximum distance of 8 cells per turn.
* **GridGreatKing2D:** Movement mimics a modified chess King, capable of moving up to 8 cells across both coordinates simultaneously.
* **GridJumper2D:** An 8-regular graph utilizing an elongated Knight's jump, moving exactly 3 cells along one coordinate axis and 2 cells along the other.

---

## Engineering Constraints & Optimization
To prevent excessive node expansion, the heuristic functions are strictly monotone and highly optimized. The system is designed to adhere to the following strict performance boundaries:

* **State-Space Limits:** The algorithm guarantees optimal pathfinding while expanding no more than **1,000,000 vertices** per complex topology suite.
* **Execution Limit:** Computations are hard-capped at **60 seconds** per grid topology. 
* **Memory Limit:** Maximum memory footprint is strictly capped at **1 GB**.
* **Discrete Math Optimization:** Due to the discrete nature of the grid topologies, continuous fractional geometries are mapped to integer boundaries (e.g., continuous distances yielding > 5.5 force discrete step counts to at least 6) to tightly bound the heuristic estimates.

---

## Repository Structure

```text
a_star_heuristics/
├── README.md                 # Project overview and execution instructions
├── task.md                   # Core constraints and grid specifications (This file)
├── heuristics.py             # Core implementation containing all 8 custom monotone heuristic functions
├── informed_search_tests.py  # Unit tests evaluating time limits, memory bounds, and expansion efficiency
├── monotonicity_tests.py     # Mathematical validation suite strictly checking heuristic consistency
└── LICENSE                   # Open-source licensing parameters
