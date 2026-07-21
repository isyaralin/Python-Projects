# Boolean Satisfiability (SAT): The 3-Partition Problem

## Mathematical Context & Overview
The 3-partition problem is a well-known, strongly NP-complete combinatorial decision problem. The objective is to determine whether a given multiset of integers can be perfectly partitioned into distinct triplets, such that every triplet shares the exact same sum.

For this implementation, the scope is focused on a special case where the given integers are strictly positive and pair-wise distinct. The strict partitioning constraint requires that every single given integer is assigned to exactly one triplet.

---

## Project Objectives & Architecture
This project engineers an algorithmic solver capable of resolving general instances of the 3-partition problem. Because naive greedy algorithms fail on complex distributions (e.g., locking sub-optimal triplets early and leaving unpartitionable remainders), the solution strictly relies on Boolean Satisfiability (SAT) encoding.

The architecture dynamically formulates the mathematical constraints of the partition problem into a boolean formula, delegating the state-space search to a highly optimized SAT solver to extract the exact triplet configuration.

### Core Technical Specs
* **SAT Engine:** The boolean constraint logic and satisfiability modeling are implemented using the `python-sat` library.
* **Algorithmic Generalization:** The solver systematically finds the correct partition for any arbitrary instance (assuming sufficient time and memory limits), without relying on localized or greedy heuristics.
* **Complexity Optimization:** For any given $3n$ distinct integers, there is a theoretical upper bound of at most $4.5n^2$ valid triplets that match the target sum. Because the actual number of valid sum-matching combinations is typically much smaller than this bound, the algorithm pre-computes and stores these viable triplets in memory before encoding the exact-cover SAT clauses, heavily optimizing the solver's execution time.

---

## Repository Structure

```text
3_partition_sat/
├── README.md               # Environment setup and dependencies (python-sat)
├── task.md                 # Mathematical constraints and architectural specifications (This file)
├── partition_sat.py        # Core algorithm implementation containing the SAT encoding logic
└── LICENSE                 # Open-source licensing parameters
