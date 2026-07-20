import constraint


def total_coloring(graph):
    nodes = list(graph.nodes())
    edges = [(u, v) if u <= v else (v, u) for u, v in graph.edges()]

    if not nodes:
        return 0

    max_degree = max(d for _, d in graph.degree()) if edges else 0

    for num_colors in range(max_degree + 1, max_degree + 3):
        problem = constraint.Problem()

        # add node-edge variable
        for node in nodes:
            problem.addVariable(('v', node), range(num_colors))
        for u, v in edges:
            problem.addVariable(('e', u, v), range(num_colors))

        # endpoints of each edge has to be different
        for u, v in edges:
            problem.addConstraint(constraint.AllDifferentConstraint(), [('v', u), ('e', u, v), ('v', v)])

        # 2 edges with same vertex has to be different colors
        for node in nodes:
            incident = []
            for u, v in graph.edges(node):
                a, b = (u, v) if u <= v else (v, u)
                incident.append(('e', a, b))
            if len(incident) >= 2:
                problem.addConstraint(constraint.AllDifferentConstraint(), incident)

        for u, v in edges:
            problem.addConstraint(constraint.AllDifferentConstraint(), [('v', u), ('v', v)])

        solution = problem.getSolution()
        if solution:
            for node in nodes:
                graph.nodes[node]["color"] = solution[('v', node)]
            for u, v in edges:
                graph.edges[u, v]["color"] = solution[('e', u, v)]
            return num_colors
