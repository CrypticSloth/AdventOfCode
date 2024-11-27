import re

class Solver():

    def __init__(self):
        with open('input.txt', 'r') as f:
            lines = f.readlines()
        self.input = [l.strip() for l in lines]
        self.special_chars_list = self.identify_characters(self.input)

    def identify_characters(self, lines:list[str]) -> list[str]:
        chars = []
        for line in lines:
            s = line.replace('.', '')
            special_chars = ''.join([i for i in s if not i.isdigit()])
            chars.append(special_chars)
        individual_chars = [s for c in chars for s in c]
        individual_chars = list(set(individual_chars))
        return individual_chars

    def identify_location_of_digits(self, line:str) -> list[tuple[int,int]]:
        r = r".(\d+)"
        digits_iter = re.finditer(r, line)
        digit_locations = [(m.start(0), m.end(0)) for m in digits_iter]
        return digit_locations
    
    def identify_location_of_characters(self, line:str) -> list[tuple[int,int]]:
        r = r"([^\d.])"
        char_iter = re.finditer(r, line)
        char_locations = [(m.start(0), m.end(0)) for m in char_iter]
        return char_locations
    

if __name__ == '__main__':

    solver = Solver()

    print(solver.special_chars_list)
    i = 1
    print(solver.input[i])
    print(solver.identify_location_of_digits(solver.input[i]))
    print(solver.identify_location_of_characters(solver.input[i]))
