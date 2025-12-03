from typing import List, Dict
import numpy as np

class InputReader:
    def __init__(self, input_path:str):
        self.input_path = input_path

        with open(self.input_path, 'r') as f:
            self.lines = f.readlines()

        # Remove new line characters "\n"
        self.lines = [l.strip() for l in self.lines]

class JoltageFinder:
    def __init__(self, batteries:List[str]) -> int:
        self.batteries = batteries

    def convert_battery_to_list(self, battery:str) -> List[int]:
        return [int(b) for b in battery]


    def find_largest_joltage_of_size_2(self, battery:str) -> int:
        battery_list = self.convert_battery_to_list(battery)

        # First find the index of the largest joltage ignoring the last value as we can always have 2 digits
        truncated_battery = battery_list[0:-1]
        largest_joltage_idx = np.argmax(truncated_battery)

        # find the index of the second largest joltage after the first one
        joltages_after_largest = battery_list[largest_joltage_idx+1:]
        second_largest_joltage_idx = np.argmax(joltages_after_largest)
        return int(str(battery[largest_joltage_idx]) + str(joltages_after_largest[second_largest_joltage_idx]))


    def find_largest_joltage_of_size_n(self, battery:str, joltage_size:int=12) -> int:
        battery_list = self.convert_battery_to_list(battery)
        largest_joltages = []
        
        idx = 0
        for i in range(0, joltage_size):
            truncated_battery = battery_list[idx:len(battery_list) - (joltage_size - len(largest_joltages) - 1)]
            largest_joltage_idx = np.argmax(truncated_battery)
            largest_joltages.append(truncated_battery[largest_joltage_idx])
            idx = idx + largest_joltage_idx + 1
        
        largest_joltages_str = [str(j) for j in largest_joltages]

        return int(''.join(largest_joltages_str))


    def solution_1(self) -> int:
        sum_joltages = 0
        for battery in self.batteries:
            largest_joltage = self.find_largest_joltage_of_size_2(battery)
            # print(battery, largest_joltage)
            sum_joltages += largest_joltage
        return sum_joltages
    

    def solution_2(self) -> int:
        sum_joltages = 0
        for battery in self.batteries:
            largest_joltage = self.find_largest_joltage_of_size_n(battery, joltage_size=12)
            # print(battery, largest_joltage)
            sum_joltages += largest_joltage
        return sum_joltages



if __name__ == '__main__':
    ir = InputReader('input.txt')

    jf = JoltageFinder(ir.lines)
    print(jf.solution_1())
    print('----')
    print(jf.solution_2())