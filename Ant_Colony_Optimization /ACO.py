import xml.etree.ElementTree as ET
import math
import numpy as np
from collections import namedtuple

# Use 'Agg' backend so Matplotlib can save plots without needing a GUI pop-up
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

Node = namedtuple('Node', ['id', 'type', 'x', 'y', 'demand'])

def load_vrp_xml(filepath):
    tree = ET.parse(filepath)
    root = tree.getroot()

    nodes = {}
    depot_id = None
    capacity = float(root.find('fleet').find('vehicle_profile').find('capacity').text)

    for n in root.find('network').find('nodes'):
        n_id = int(n.attrib['id'])
        n_type = int(n.attrib['type'])
        cx = float(n.find('cx').text)
        cy = float(n.find('cy').text)
        nodes[n_id] = Node(id=n_id, type=n_type, x=cx, y=cy, demand=0.0)
        if n_type == 0:
            depot_id = n_id

    for req in root.find('requests'):
        node_id = int(req.attrib['node'])
        quant = float(req.find('quantity').text)
        old = nodes[node_id]
        nodes[node_id] = Node(id=old.id, type=old.type, x=old.x, y=old.y, demand=quant)

    return nodes, depot_id, capacity

def distance(v1, v2):
    return math.sqrt((v1.x - v2.x)**2 + (v1.y - v2.y)**2)

def fitness(nodes, dist, sol):
    sd = 0
    for x, y in zip(sol, sol[1:]):
        sd += dist(nodes[x], nodes[y])
    return sd

def initialize_pheromone(N):
    return 0.01 * np.ones(shape=(N, N))

def generate_solutions(nodes, depot_id, capacity, P, dist, N, alpha=1, beta=3):
    def compute_prob(v1, v2):
        d = max(dist(nodes[v1], nodes[v2]), 0.00001)
        nu = 1 / d
        tau = P[v1, v2]
        ret = pow(tau, alpha) * pow(nu, beta)
        return ret if ret > 0.000001 else 0.000001

    for i in range(N):
        available = [n.id for n in nodes.values() if n.type == 1]
        sol = [depot_id]
        current_capacity = capacity

        while available:
            feasible = [x for x in available if nodes[x].demand <= current_capacity]

            if not feasible:
                sol.append(depot_id)
                current_capacity = capacity
                continue

            probs = np.array(list(map(lambda x: compute_prob(sol[-1], x), feasible)))
            prob_sum = sum(probs)

            selected = np.random.choice(feasible, p=probs/prob_sum)
            sol.append(selected)
            available.remove(selected)
            current_capacity -= nodes[selected].demand

        sol.append(depot_id)
        yield sol

def update_pheromone(P, sols, fits, Q=100, rho=0.8):
    ph_update = np.zeros(shape=P.shape)
    for s, f in zip(sols, fits):
        for x, y in zip(s, s[1:]):
            ph_update[x][y] += Q/f
            ph_update[y][x] += Q/f

    return (1-rho)*P + ph_update

def ant_solver(nodes, depot_id, capacity, dist, ants=10, max_iter=100, alpha=1, beta=3, Q=100, rho=0.8):
    max_id = max(nodes.keys())
    P = initialize_pheromone(max_id + 1)
    best_sol = None
    best_fit = float('inf')

    log_min = []

    for it in range(max_iter):
        sols = list(generate_solutions(nodes, depot_id, capacity, P, dist, ants, alpha=alpha, beta=beta))
        fits = list(map(lambda x: fitness(nodes, dist, x), sols))
        P = update_pheromone(P, sols, fits, Q=Q, rho=rho)

        for s, f in zip(sols, fits):
            if f < best_fit:
                best_fit = f
                best_sol = s

        min_fit = np.min(fits)
        log_min.append(best_fit)

        if it % 10 == 0 or it == max_iter - 1:
            print(f'Iter {it:4}, Min: {min_fit:.4f}, Mean: {np.mean(fits):.4f}, Max: {np.max(fits):.4f}')

    return best_sol, best_fit, log_min

if __name__ == '__main__':
    files = ['data_32.xml', 'data_72.xml', 'data_422.xml']

    for file in files:
        try:
            nodes, depot_id, capacity = load_vrp_xml(file)
            print(f"\n{'='*50}\nSolving {file} (Nodes: {len(nodes)})\n{'='*50}")

            if len(nodes) < 50:
                iters = 100
                ant_count = 20
                a = 1.0
                b = 3.0
                q_val = 100
                evap = 0.8
            elif len(nodes) < 100:
                iters = 1000
                ant_count = 50
                a = 1.0
                b = 3.0
                q_val = 100
                evap = 0.8
            else:
                iters = 50
                ant_count = 20
                a = 1.0
                b = 3.0
                q_val = 100
                evap = 0.8

            best_sol, best_fit, log_min = ant_solver(
                nodes, depot_id, capacity, distance,
                ants=ant_count, max_iter=iters, alpha=a, beta=b, Q=q_val, rho=evap
            )

            routes = []
            current_route = [depot_id]
            for node in best_sol[1:]:
                current_route.append(node)
                if node == depot_id:
                    if len(current_route) > 2:
                        routes.append(current_route)
                    current_route = [depot_id]

            print(f"\nTotal Distance (Cost): {best_fit:.2f}")
            print(f"Total Vehicles Used: {len(routes)}\n")

            for i, route in enumerate(routes, 1):
                clean_route = [int(n) for n in route]
                print(f"Route {i}: {clean_route}")

            # Plot and save figure to disk
            plt.figure(figsize=(8, 4))
            plt.plot(log_min, 'b-', label="Best Route Length (Generation)")
            plt.title(f"ACO Convergence for {file}")
            plt.xlabel("Iterations")
            plt.ylabel("Distance")
            plt.grid(True)
            plt.legend(loc="best")
            
            # Save plot image dynamically based on input filename
            image_filename = f"aco_convergence_{file.split('.')[0]}.png"
            plt.savefig(image_filename, dpi=300, bbox_inches="tight")
            plt.close()  
            print(f"Saved convergence plot as: {image_filename}\n")

        except FileNotFoundError:
            print(f"Warning: {file} not found. Please ensure it is in the same directory.")
