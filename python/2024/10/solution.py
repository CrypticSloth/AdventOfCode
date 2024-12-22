import numpy as np
import tqdm

class Solver:

    def __init__(self):
        with open('input_test4.txt', 'r') as f:
            self.lines = f.readlines()
    
        lines_reshaped = []
        for line in self.lines:
            lr = []
            for c in line.strip():
                lr.append(int(c))
            lines_reshaped.append(lr)
        
        self.grid = np.array(lines_reshaped)
        self.trailheads = self.find_trailheads()

    def find_trailheads(self) -> list[tuple[int,int]]:
        return [[int(g[0]), int(g[1])] for g in np.argwhere(self.grid == 0)]

    def find_valid_moves(self, pos:tuple[int, int]) -> list[tuple[int,int]]:
        val = self.grid[pos[0], pos[1]]
        valid_moves = []
        if val != 9:
            if pos[0]+1 < self.grid.shape[0]:
                if self.grid[pos[0]+1, pos[1]] - val == 1:
                    nv = self.grid[pos[0]+1, pos[1]]
                    if (nv != 0):
                        valid_moves.append([pos[0]+1, pos[1]])
            if pos[0]-1 >= 0:
                if self.grid[pos[0]-1, pos[1]] - val == 1:
                    nv = self.grid[pos[0]-1, pos[1]]
                    if (nv != 0):
                        valid_moves.append([pos[0]-1, pos[1]])
            if pos[1]+1 < self.grid.shape[1]:
                if self.grid[pos[0], pos[1]+1] - val == 1:
                    nv = self.grid[pos[0], pos[1]+1]
                    if (nv != 0):
                        valid_moves.append([pos[0], pos[1]+1])
            if pos[1]-1 >= 0:
                if self.grid[pos[0], pos[1]-1] - val == 1:
                    nv = self.grid[pos[0], pos[1]-1]
                    if (nv != 0):
                        valid_moves.append([pos[0], pos[1]-1])
        return valid_moves

    def dfs(self, pos, visited, plot=False):
        if plot:
            if pos not in visited:
                n_grid = self.grid.copy()
                n_grid = n_grid.astype(str)
                for v in visited:
                    n_grid[v[0], v[1]] = '.'
                n_grid[pos[0], pos[1]] = '*'
                print(n_grid)
                print()

        if pos not in visited:
            visited.append([pos[0], pos[1]])
            for n in self.find_valid_moves(pos):
                self.dfs(n, visited, plot=plot)
        return visited
    
    def solution_1(self) -> int:
        trail_score = 0
        for pos in self.trailheads:
            visited = self.dfs(pos, [])
            vals = []
            for l in visited:
                vals.append(int(self.grid[l[0], l[1]]))
            # Count the number of 9s reachable for each zero and add that to the total score
            trail_score += vals.count(9)
        return trail_score
    
    def solution_2(self) -> int:
        ## For solution 2, perhaps we can count the number of times we run dfs when there is a fork in the road?
        # But we would only count those that reach a final solution
        pass
    
if __name__ == "__main__":
    
    solver = Solver()

    # print(solver.grid.shape)
    # print(solver.trailheads)
    # print(solver.find_valid_moves((0,1)))
    print(solver.dfs([0,5], [], True))
    print(solver.solution_1())
    
