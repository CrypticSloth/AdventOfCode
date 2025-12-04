from typing import Tuple
import numpy as np
from scipy import signal

class InputReader:
    def __init__(self, input_path:str):
        self.input_path = input_path

        with open(self.input_path, 'r') as f:
            self.lines = f.readlines()

        self.input_array = []
        for l in self.lines:
            line = l.strip()
            line_list = []
            for c in line:
                if c == '@':
                    line_list.append(1)
                else:
                    line_list.append(0)
            self.input_array.append(line_list)

        self.input_array = np.array(self.input_array)


class RollFinder:
    def __init__(self, input_array:np.array):
        self.input_array = input_array

    
    def solution_1(self, input_array:np.array) -> Tuple[int, np.array]:
        kernel = np.ones((3,3), dtype=int)
        kernel[1,1] = 0
        roll_counts = signal.convolve2d(input_array, kernel, mode='same')

        # Set any areas where there were no rolls to 10 to ignore
        roll_counts = np.where(input_array == 0, 10, roll_counts)
        # Count the number of values less than 4
        less_than_4_mask = np.where(roll_counts < 4, 1, 0)
        return np.sum(less_than_4_mask), np.where(roll_counts < 4, 0, input_array)


    def solution_2(self) -> int:
        roll_count = 0
        input_array = self.input_array
        while True:
            count, new_array = self.solution_1(input_array)
            roll_count += count
            # If no changes to the grid have been made we are done
            if (input_array == new_array).all():
                break
            input_array = new_array

        return roll_count



if __name__ == '__main__':

    reader = InputReader('input.txt')
    print(reader.input_array)

    solver = RollFinder(reader.input_array)
    print(solver.solution_1(reader.input_array))
    print(solver.solution_2())
