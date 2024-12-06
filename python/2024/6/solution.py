import tqdm
from multiprocessing import Pool, cpu_count

class Solver:

    def __init__(self):

        with open('input.txt', 'r') as f:
            self.grid = f.readlines()
        
        self.guard_position, self.guard_orientation = self.find_guard()
        self.steps_counter = 0
        self.visited_locations = [self.guard_position]

    def find_guard(self) -> tuple[tuple[int,int], str]:
        for r in range(len(self.grid)):
            for c in range(len(self.grid[r])):
                if self.grid[r][c] == "^":
                    return (r,c), "^"
                if self.grid[r][c] == "<":
                    return (r,c), "<"
                if self.grid[r][c] == ">":
                    return (r,c), ">"
                if self.grid[r][c] == "v":
                    return (r,c), "v"
                
    def walk_guard(self, grid:list[list[str]]) -> tuple[int,int]:
        # Walk guard until a '#' is found in the orientation he is in
        # Return the final guard position
        guard_pos = self.guard_position
        guard_orientation = self.guard_orientation
        n_grid = grid.copy()
        reps = 0
        while True:
            # n_grid[guard_pos[0]] = n_grid[guard_pos[0]][:guard_pos[1]] + 'X' + n_grid[guard_pos[0]][guard_pos[1]+1:]
            # for l in n_grid:
            #     print(l)
            # print()
            # print()
            if guard_orientation == "^":
                if guard_pos[0]-1 < 0:
                    self.steps_counter += 1
                    return guard_pos
                elif grid[guard_pos[0]-1][guard_pos[1]] == '#':
                    guard_orientation = ">"
                else:
                    guard_pos = (guard_pos[0]-1, guard_pos[1])
                    if guard_pos not in self.visited_locations:
                        self.steps_counter += 1
                        self.visited_locations.append(guard_pos)
            if guard_orientation == "v":
                if guard_pos[0]+1 > len(grid)-1:
                    self.steps_counter += 1
                    return guard_pos
                elif grid[guard_pos[0]+1][guard_pos[1]] == '#':
                    guard_orientation = "<"
                else:
                    guard_pos = (guard_pos[0]+1, guard_pos[1])
                    if guard_pos not in self.visited_locations:
                        self.steps_counter += 1
                        self.visited_locations.append(guard_pos)
            if guard_orientation == "<":
                if guard_pos[1]-1 < 0:
                    self.steps_counter += 1
                    return guard_pos
                elif grid[guard_pos[0]][guard_pos[1]-1] == '#':
                    guard_orientation = "^"
                else:
                    guard_pos = (guard_pos[0], guard_pos[1]-1)
                    if guard_pos not in self.visited_locations:
                        self.steps_counter += 1
                        self.visited_locations.append(guard_pos)
            if guard_orientation == ">":
                if guard_pos[1]+1 > len(grid[0])-1:
                    self.steps_counter += 1
                    return guard_pos
                elif grid[guard_pos[0]][guard_pos[1]+1] == '#':
                    guard_orientation = "v"
                else:
                    guard_pos = (guard_pos[0], guard_pos[1]+1)
                    if guard_pos not in self.visited_locations:
                        self.steps_counter += 1
                        self.visited_locations.append(guard_pos)
            reps += 1
            # If it doesn't finish in this many reps then it is stuck
            if reps > 10000:
                return False, False

    def solution_1(self)->int:  
        final_guard_pos = self.walk_guard(self.grid)
        print(final_guard_pos)
        return self.steps_counter
    
    def solution_2_parallelized(self)->int:
        func_inputs = []
        for r in tqdm.tqdm(range(len(self.grid))):
            for c in range(len(self.grid[r])):
                new_grid = self.grid.copy()
                new_grid[r] = new_grid[r][:c] + '#' + new_grid[r][c+1:]
                func_inputs.append(new_grid)
        
        with Pool(processes=cpu_count()-1) as p:
            results = list(tqdm.tqdm(p.imap(self.walk_guard, func_inputs), total=len(func_inputs)))

        num_obstructions = 0
        for r in results:
            if r == (False, False):
                num_obstructions += 1
        return num_obstructions

    def solution_2(self)->int:
        num_obstructions = 0
        for r in tqdm.tqdm(range(len(self.grid))):
            for c in range(len(self.grid[r])):
                new_grid = self.grid.copy()
                new_grid[r] = new_grid[r][:c] + '#' + new_grid[r][c+1:]
                result = self.walk_guard(new_grid)
                if result == (False, False):
                    num_obstructions += 1
        return num_obstructions




if __name__ == "__main__":

    solver = Solver()   

    print(solver.find_guard())
    print(solver.solution_1())
    # print(solver.solution_2())
    print(solver.solution_2_parallelized())