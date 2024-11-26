import re

class Solver():

    def __init__(self):
        with open('input.txt', 'r') as f:
            lines = f.readlines()
        self.lines = [s.strip() for s in lines]

    def parse_game_number(self, line:str) -> int:
        game_number = re.findall(r"Game (\d*)", line)
        return int(game_number[0])

    def parse_game_set(self, line:str) -> str:
        sets = line.split(':')[1].split(';')
        return [s.strip() for s in sets]
    
    def parse_set(self, set_str:str) -> dict:
        set_dict = {}
        pulls = set_str.split(',')
        for pull in pulls:
            t = pull.strip().split(' ')
            num = int(t[0])
            color = t[1]
            set_dict[color] = num
        return set_dict
    
    def parse_input(self, line:str) -> tuple:

        game_number = self.parse_game_number(line)
        parsed_sets = self.parse_game_set(line)
        parsed_pulls = [self.parse_set(ps) for ps in parsed_sets]

        return game_number, parsed_pulls


if __name__ == "__main__":

    solver = Solver()

    test_line = solver.lines[0]
    print(test_line)
    print(solver.parse_game_number(test_line))
    print(solver.parse_game_set(test_line))
    print(solver.parse_set(solver.parse_game_set(test_line)[0]))
    print(solver.parse_input(test_line))