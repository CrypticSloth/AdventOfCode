import numpy as np

class Solver:

    def __init__(self):

        with open('input.txt', 'r') as f:
            lines = f.readlines()

        self.input = [l.strip().split('   ') for l in lines]
        self.input_arr = np.array(self.input).astype(np.int32)

    def sort_array(self):
        col1 = np.flip(np.sort(self.input_arr[:,0])).reshape(-1,1)
        col2 = np.flip(np.sort(self.input_arr[:,1])).reshape(-1,1)
        return np.concatenate([col1,col2], axis=1)

    def solution_1(self, input=None):
        if not input:
            sorted_array = self.sort_array()
        diff = np.abs(sorted_array[:,0] - sorted_array[:,1])
        distance = np.sum(diff)
        return distance

    def solution_2(self):
        col1 = [r[0] for r in self.input_arr]
        col2 = [r[1] for r in self.input_arr]

        sum = 0
        for v in col1:
            sum += v * col2.count(v)
        return sum


if __name__ == "__main__":

    solver = Solver()
    
    print(f"Solution to problem 1: {solver.solution_1()}")
    print(f"Solution to problem 2: {solver.solution_2()}")

