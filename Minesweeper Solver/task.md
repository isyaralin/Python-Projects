# Artificial Intelligence: Autonomous Minesweeper Solver

## Overview
This project focuses on building an AI agent to automatically play and solve Minesweeper. 

Minesweeper is a great game for testing AI techniques because it combines deterministic logic with probabilistic guessing. Since some board layouts force you to make a guess (like a 50/50 chance), the AI cannot win 100% of the time. However, by combining logical deduction with conditional probability calculations, the agent can make the best possible decisions to maximize its overall win rate.

---

## Technical Approach

The solver uses a combination of logical inference and probability estimation to pick the best moves:

### 1. Constraint Satisfaction & Logic
* Uses Constraint Satisfaction (CSP) and logic rules to evaluate the numbers revealed on the board.
* Instantly identifies completely safe cells (0% mine chance) and confirmed mines (100% mine chance) to make immediate moves without doing extra math.

### 2. Probability Estimation
* When pure logic isn't enough to find a guaranteed safe move, the AI looks at the "frontier" (the unrevealed cells adjacent to revealed numbers).
* It groups connected cells and calculates the exact conditional probability of each cell containing a mine.
* If a guess is required, the agent picks the cell with the absolute lowest calculated risk.

---

## Requirements & Constraints

* **Interface:** The core logic is implemented inside `minesweeper_player.py` and maintains compatibility with the provided test suite.
* **Performance:** Decisions are made efficiently to ensure full board runs complete within the 60-second time limit per test suite.
* **Code Documentation:** Core logic, frontier calculations, and probability functions are documented inline to keep the code clear and easy to follow.

---

## Repository Structure

```text
minesweeper_ai/
├── README.md                # Overview and instructions on how to run the player
├── task.md                  # Project description and technical constraints (This file)
├── minesweeper_player.py    # Main AI player code (Logic, CSP, and probability logic)
├── minesweeper_test.py      # Test script to benchmark win rates and runtime
├── probability_test.py      # Test suite to verify probability calculations
└── LICENSE                  # Project license
