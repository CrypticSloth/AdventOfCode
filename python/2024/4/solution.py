import numpy as np

# 1. TO solve this one. I will create a substring searcher to find all instances of either XMAS or SAMX vertically or horizontally. 
# 2. To find the diagonal instances, I will go down the text and shift (both left shift and right shift the next 4 rows as the following: 
# row 1 don't shift, row 2 shift by 1, row 3 shift by 2 and row 4 shift by 2. Fill in any missing gaps with "M". 
# Then I can find any diagonal instances of XMAS using the vertical solver from step 1

class Solver:

    def __init__(self):

        with open('input.txt', 'r') as f:
            lines = f.readlines()
        self.input = [l.strip() for l in lines]
        self.search_terms = ['XMAS', 'SAMX']

    def find_horizontal_instances(self, input:list[str]=None)->int:
        count = 0
        if input:
            inp = input
        else:
            inp = self.input
        for line in inp:
            for search_term in self.search_terms:
                count += line.count(search_term)
        return count

    def transpose_list_of_strings(self, input:list[str]) -> list[str]:
        transposed_input = [''.join(s) for s in zip(*input)]
        return transposed_input

    def find_vertical_instances(self, input:list[str]=None)->int:
        if input:
            inp = input
        else:
            inp = self.input
        
        # Transpose the lists so rows become columns, then perform the find horizontal search
        inp = self.transpose_list_of_strings(inp)
        count = self.find_horizontal_instances(inp)
        return count
    
    def string_shifter(self, input:list[str], shift_right:bool=True)->list[str]:
        if input:
            inp = input
        else:
            inp = self.input
        
        shifted_strings = []
        for i in range(len(inp)):
            string = inp[i]
            if shift_right:
                pad_amt = i
            else:
                pad_amt = len(inp)-1 - i
            shifted_strings.append(("."*pad_amt) + string + ("."*((len(inp)-1)-pad_amt)))
        return shifted_strings
    
    def solution_1(self)->int:
        count = 0
        count += self.find_horizontal_instances(self.input)
        count += self.find_vertical_instances(self.input)
        count += self.find_vertical_instances(self.string_shifter(self.input, shift_right=True))
        count += self.find_vertical_instances(self.string_shifter(self.input, shift_right=False))
        return count

if __name__ == "__main__":

    solver = Solver()

    t = [
        "MMMSXXMASM",
        "MSAMXMSMSA",
        "AMXSXMAAMM",
        "MSAMASMSMX",
        "XMASAMXAMM",
        "XXAMMXXAMA",
        "SMSMSASXSS",
        "SAXAMASAAA",
        "MAMMMXMMMM",
        "MXMXAXMASX",
    ]

    for l in solver.string_shifter(t, shift_right=True):
        print(l)
    print()
    for l in solver.string_shifter(t, shift_right=False):
        print(l)
    print()
    for l in solver.transpose_list_of_strings(solver.string_shifter(t, shift_right=True)):
        print(l)
    print()
    for l in solver.transpose_list_of_strings(solver.string_shifter(t, shift_right=False)):
        print(l)
    print()
    print(solver.find_horizontal_instances(t))
    print(solver.find_vertical_instances(t))
    print(solver.find_vertical_instances(solver.string_shifter(t, shift_right=True)))
    print(solver.find_vertical_instances(solver.string_shifter(t, shift_right=False)))

    print(f"Solution to problem 1: {solver.solution_1()}")