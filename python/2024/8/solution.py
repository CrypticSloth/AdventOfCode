import numpy as np
from collections import defaultdict

class Solver:

    def __init__(self):

        with open('input_test.txt', 'r') as f:
            self.lines = f.readlines()
            
        lines_reshaped = []
        for line in self.lines:
            lr = []
            for c in line.strip():
                lr.append(c)
            lines_reshaped.append(lr)
        
        self.grid = np.array(lines_reshaped)
        self.antenna_locations = self.find_location_of_antennas()
        self.antenna_ids = list(self.antenna_locations.keys())
        self.antinode_locations = []


    def find_location_of_antennas(self) -> dict[str:list[tuple[str,int,int]]]:
        # Identify location of all antennas
        # Return a dict of the antenna identifier as keys with all locations of that antenna as values
        antenna_locations = defaultdict(list)
        for r in range(self.grid.shape[0]):
            for c in range(self.grid.shape[1]):
                if self.grid[r,c] != '.':
                    antenna_locations[str(self.grid[r,c])].append((r, c))
        return antenna_locations

    def antinode_plotter(self) -> None:
        ng = self.grid.copy()
        for al in self.antinode_locations:
            ng[al[0], al[1]] = '#'
        
        for row in ng:
            print(row)
            
    def solution_1(self)->int:
        # Idea is that for each antenna_id, find all antenna_id locations. Calculate the rowise and column wise distance 
        # between each antenna with the same id, then add that distance in the opposite direction and see if it lands in the grid
        # If it does, then iterate the counter.
        counter = 0
        for id in self.antenna_ids:
            locs = self.antenna_locations[id]
            for loc1 in locs:
                for loc2 in locs:
                    if loc1 != loc2:
                        row_dist = loc1[0] - loc2[0]
                        col_dist = loc1[1] - loc2[1]
                        antinode_row = loc1[0]+row_dist
                        antinode_col = loc1[1]+col_dist
                        if ((antinode_row >= 0) & (antinode_row < self.grid.shape[0])) & ((antinode_col >= 0) & (antinode_col < self.grid.shape[1])):
                            counter += 1
                            self.antinode_locations.append((antinode_row, antinode_col))
        return counter

if __name__ == "__main__":

    solver = Solver()
    print(solver.grid.shape)
    # print(solver.find_location_of_antennas())
    # print(solver.antenna_ids)
    print(solver.solution_1())
    print(solver.antinode_plotter())