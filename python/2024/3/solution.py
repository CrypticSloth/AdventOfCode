import re

class Solver:

    def __init__(self):

        with open('input.txt', 'r') as f:
            self.txt = f.read().strip()

    def find_valid_multiply_instructions(self, input:str)->list[str]:
        r_match = r"mul\(\d{1,3},\d{1,3}\)"

        matches = re.findall(r_match, input)
        return matches
    
    def multiply_instructions(self, instruction:str)->int:
        first_digit = int(instruction.split('(')[1].split(',')[0])
        second_digit = int(instruction.split('(')[1].split(',')[1].split(')')[0])
        return first_digit*second_digit

    def find_location_of_dos_and_donts(self) -> tuple[list[int], list[int]]:
        do_matching = r"do\(\)"
        dont_matching = r"don't\(\)"

        do_locations = [(m.start(0), m.end(0)) for m in re.finditer(do_matching, self.txt)]
        dont_locations = [(m.start(0), m.end(0)) for m in re.finditer(dont_matching, self.txt)]

        return [l[0] for l in do_locations], [l[1] for l in dont_locations]

    def solution_1(self)->int:
        valid_multiply_instructions = self.find_valid_multiply_instructions(self.txt)
        sum = 0
        for instruction in valid_multiply_instructions:
            sum += self.multiply_instructions(instruction)
        return sum
    
    def solution_2(self)->int:
        do_locations, dont_locations = self.find_location_of_dos_and_donts()
        do_locations = [0] + do_locations

        # General idea is to index the substrings of the input based on the location of do's and don'ts. 
        # Alternate searching through the previous index for the next largest index in the other list.
        valid_substrings = []
        for do in do_locations:
            for dont in dont_locations:
                if (dont > do):
                    valid_substrings.append((do, dont))
                    break
        
        # Remove duplicate dont indexes
        cleaned_valid_substrings = [valid_substrings[0]]
        for i in range(len(valid_substrings)-1):
            if cleaned_valid_substrings[-1][1] != valid_substrings[i][1]:
                cleaned_valid_substrings.append(valid_substrings[i])
        
        # Add in the last do segment in the input text
        cleaned_valid_substrings.append((do_locations[-1], len(self.txt)))

        # Parse through all of the valid substrings like I did before
        sum = 0
        for ind in cleaned_valid_substrings:
            substr = self.txt[ind[0]:ind[1]]
            valid_multiply_instructions = self.find_valid_multiply_instructions(substr)
            for instruction in valid_multiply_instructions:
                sum += self.multiply_instructions(instruction)

        return sum
        

if __name__ == "__main__":

    solver = Solver()
    print(f"Solution to problem 1: {solver.solution_1()}")
    print(f"Solution to problem 2: {solver.solution_2()}")
