# Evolutionary Knapsack Solver

## Description of the Algorithm
I implemented the evolutionary algorithm to solve the Knapsack problem. 

### Encoding of Individuals
I represented the solutions as binary strings of length *n*. A value of 1 indicates that the corresponding item is included in the knapsack, and 0 indicates it is not.

### Fitness Function and Repair Mechanism
The aim is to maximize the cumulative price. The fitness function calculates the sum of the prices of the selected items. 

However, to improve the algorithm's performance, I implemented a repair function. If an individual exceeds the weight capacity, it removes the item with the lowest price-to-weight ratio until the capacity constraint is met.

### Selection Method
I selected the individuals for a mating pool with a probability proportional to their fitness scores.

### Genetic Operators
* **Crossover:** I applied a single-point crossover. The code recombined pairs of parents at a randomly selected split point.
* **Mutation:** I also applied a bit-flip mutation. If an offspring is selected for mutation, each bit in the string has a small probability of flipping.

The algorithm is implemented in Python.

---

## Steps to Run

All `.txt` benchmark files must be placed in the same directory as `Knapsack.py`.

Run the script in your terminal:
```bash
python3 Knapsack.py
