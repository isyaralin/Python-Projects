# Ant Colony Optimization (ACO) Solver

## Description of the Algorithm
I mainly used the implementation of ACO algorithm. I kept the parameters and the structure of the implementation as similar as possible and modified/adapted the functions and the logic according to the assignment requirements.

## Algorithmic Adaptations

### Node Representation and Data Parsing
I expanded the standard **Vertex** tuple we had in the lab to a **Node** tuple as required in the task. My new node tuple includes `demand` and `type` attributes to detect the difference between a customer and a depot. I also implemented an XML parser to get the coordinates of the nodes, capacities, and requests.

### Route Generation and Capacity Tracking
I changed the way ants work. Now they track their `current_capacity`. They filter the customers so they can find the best stops. If the demand exceeds the remaining capacity, the ant is forced to append the `depot_id` to its route (Penalty).

### Fitness Function and Minimization
The fitness score is now purely based on the total travel distance.

### Pheromone Updates
I adjusted the logic of `update_pheromone` to represent that the undirected edges get equal reinforcement according to the type.


## Prerequisites
Before running the script, you must ensure all `.xml' files in the `xml_files/` directory are places in the same directory as the ACO.py file and you must install the required dependencies to run the math and generate the graphs.

Run the following command in your terminal:
```bash
pip install numpy matplotlib```

## Outcomes 
After running the script, the algorithm will produce 4 `.png` files that show the convergence.
(The `png` files can be found inside `convergence_png/` directory)
