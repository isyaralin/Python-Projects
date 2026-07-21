import numpy
from minesweeper_common import UNKNOWN, MINE, get_neighbors

class Player:
    def __init__(self, rows, columns, game, mine_prb):
        self.rows = rows
        self.columns = columns
        self.mine_prb = mine_prb
        self.game = game
        self.neighbors = get_neighbors(rows, columns)

        self.mines = numpy.full((rows, columns), -1)
        self.unknown = numpy.full((rows, columns), 0)
        for i in range(self.rows):
            for j in range(self.columns):
                self.unknown[i,j] = len(self.neighbors[i,j])
        self.invalid = set()

    def turn(self):
        pos = self.preprocessing()
        if not pos:
            pos = self.probability_player()
        
        if pos:
            self.invalidate_with_neighbors(pos)
        return pos        

    def probability_player(self):
        prb = self.get_each_mine_probability()
        best_pos = None
        min_p = 1.1 

        for i in range(self.rows):
            for j in range(self.columns):
                if self.game[i,j] == UNKNOWN:
                    if prb[i,j] > 0.9999:
                        self.game[i,j] = MINE
                        self.invalidate_with_neighbors((i,j))
                    
                    if prb[i,j] < min_p:
                        min_p = prb[i,j]
                        best_pos = (i,j)
        
        if not best_pos:
            for i in range(self.rows):
                for j in range(self.columns):
                    if self.game[i,j] == UNKNOWN: return (i,j)
        return best_pos

    def invalidate_with_neighbors(self, pos):
        self.invalid.add(pos)
        for neigh in self.neighbors[pos]:
            self.invalid.add(neigh)

    def preprocess_all(self):
        self.invalid = set((i,j) for i in range(self.rows) for j in range(self.columns))
        self.preprocessing()

    def preprocessing(self):
        while self.invalid:
            pos = self.invalid.pop()
            self.unknown[pos] = sum(1 if self.game[n] == UNKNOWN else 0 for n in self.neighbors[pos])

            if self.game[pos] >= 0:
                self.mines[pos] = self.game[pos] - sum(1 if self.game[n] == MINE else 0 for n in self.neighbors[pos])
                
                if self.unknown[pos] > 0:
                    if self.mines[pos] == self.unknown[pos]:
                        for n in self.neighbors[pos]:
                            if self.game[n] == UNKNOWN:
                                self.game[n] = MINE
                                self.invalidate_with_neighbors(n)
                    elif self.mines[pos] == 0:
                        self.invalid.add(pos)
                        for n in self.neighbors[pos]:
                            if self.game[n] == UNKNOWN: return n
        return None

    def get_each_mine_probability(self):
        probability = numpy.full((self.rows, self.columns), float(self.mine_prb))
        
        for i in range(self.rows):
            for j in range(self.columns):
                if self.game[i,j] == MINE: probability[i,j] = 1.0
                elif self.game[i,j] >= 0: probability[i,j] = 0.0

        frontier_cells = []
        cell_to_clues = {} 
        for i in range(self.rows):
            for j in range(self.columns):
                if self.game[i,j] >= 0 and self.unknown[i,j] > 0:
                    for n in self.neighbors[i,j]:
                        if self.game[n] == UNKNOWN:
                            if n not in cell_to_clues:
                                frontier_cells.append(n)
                                cell_to_clues[n] = []
                            cell_to_clues[n].append((i,j))

        if not frontier_cells:
            return probability

        visited = set()
        for cell in frontier_cells:
            if cell in visited: continue
            
            island_cells = []
            queue = [cell]
            visited.add(cell)
            
            while queue:
                curr = queue.pop(0)
                island_cells.append(curr)
                for clue_pos in cell_to_clues[curr]:
                    for potential_neighbor in self.neighbors[clue_pos]:
                        if self.game[potential_neighbor] == UNKNOWN and potential_neighbor not in visited:
                            visited.add(potential_neighbor)
                            queue.append(potential_neighbor)
            
            self._solve_island(island_cells, cell_to_clues, probability)

        return probability

    def _solve_island(self, cells, cell_to_clues, prob_matrix):
        solutions = []
        n = len(cells)

        def check_constraints(assignment, cell):
            for clue in cell_to_clues[cell]:
                m_count = 0 
                u_count = 0 
                for n_pos in self.neighbors[clue]:
                    val = assignment.get(n_pos)
                    if self.game[n_pos] == MINE or val == 1:
                        m_count += 1
                    elif self.game[n_pos] == UNKNOWN and val is None:
                        u_count += 1
                
                if m_count > self.game[clue] or (m_count + u_count) < self.game[clue]:
                    return False
            return True

        def backtrack(idx, current):
            if idx == n:
                solutions.append(current.copy())
                return

            c = cells[idx]
            for value in [0, 1]:
                current[c] = value
                if check_constraints(current, c):
                    backtrack(idx + 1, current)
                del current[c]

        backtrack(0, {})

        if solutions:
            total_weight = 0.0
            cell_weights = {c: 0.0 for c in cells}
            
            for sol in solutions:
                k = sum(sol.values())
                weight = (self.mine_prb ** k) * ((1.0 - self.mine_prb) ** (n - k))
                total_weight += weight
                for c in cells:
                    if sol[c] == 1:
                        cell_weights[c] += weight
            
            if total_weight > 0:
                for c in cells:
                    prob_matrix[c] = cell_weights[c] / total_weight
