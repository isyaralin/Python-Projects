from pysat.solvers import Minisat22


def solve_3partition(numbers):
    n = len(numbers) // 3
    targetedSum = sum(numbers) // n
    numbers = list(numbers)

    triplets = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            for k in range(j + 1, len(numbers)):
                if numbers[i] + numbers[j] + numbers[k] == targetedSum:
                    triplets.append((i, j, k))

    if not triplets:
        return []

    tripleToSatVariable = {triplets[i]: i + 1 for i in range(len(triplets))}
    variableToSat = {i + 1: triplets[i] for i in range(len(triplets))}

    solver = Minisat22()

    for i in range(len(numbers)):
        relevantVariables = [tripleToSatVariable[t] for t in triplets if i in t]

        if not relevantVariables:
            return []

        solver.add_clause(relevantVariables)

        for v1 in range(len(relevantVariables)):
            for v2 in range(v1 + 1, len(relevantVariables)):
                solver.add_clause([-relevantVariables[v1], -relevantVariables[v2]])

    if not solver.solve():
        return []

    model = solver.get_model()

    if model is None:
        return []

    solution = []
    for var in model:
        if var > 0 and var in variableToSat:
            triplet = variableToSat[var]
            solution.append([numbers[i] for i in triplet])

    return solution
