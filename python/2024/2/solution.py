import numpy as np

class Solver:

    def __init__(self):

        with open('input.txt', 'r') as f:
            lines = f.readlines()

        self.input = [l.strip().split(' ') for l in lines]
        self.input = [[int(v) for v in r] for r in self.input]

    def check_monotonicity(self, list_of_ints:list[int], increasing:bool=True) -> bool:
        if increasing:
            for i in range(len(list_of_ints)-1):
                if list_of_ints[i+1] <= list_of_ints[i]:
                    return False
        else:
            for i in range(len(list_of_ints)-1):
                if list_of_ints[i+1] >= list_of_ints[i]:
                    return False
        return True

    def check_gradually_increasing(self, list_of_ints:list[int], increasing_min:int=1, increasing_max:int=3)->bool:
        for i in range(len(list_of_ints)-1):
            diff = abs(list_of_ints[i+1] - list_of_ints[i])
            if (diff < increasing_min) or (diff > increasing_max):
                return False
        return True

    def solution_1(self)->int:
        sum = 0
        for l in self.input:
            if (self.check_monotonicity(l, increasing=True) | self.check_monotonicity(l, increasing=False)) & self.check_gradually_increasing(l):
                sum += 1
        return sum
    
    def solution_2(self)->int:
        sum = 0
        for l in self.input:
            flag = False
            if (self.check_monotonicity(l, increasing=True) | self.check_monotonicity(l, increasing=False)) & self.check_gradually_increasing(l):
                flag = True
            for i in range(len(l)):
                clipped_list = l[:i] + l[i+1:]
                if (self.check_monotonicity(clipped_list, increasing=True) | self.check_monotonicity(clipped_list, increasing=False)) & self.check_gradually_increasing(clipped_list):
                    flag = True
            if flag:
                sum += 1
        return sum

if __name__ == "__main__":

    solver = Solver()

    print(f"Solution to problem 1: {solver.solution_1()}")
    print(f"Solution to problem 2: {solver.solution_2()}")
    