import re
from typing import Dict

class GameSet(Dict):
    red: int
    green: int
    blue: int

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

    def identify_possible_games(self, num_red:int, num_green:int, num_blue:int) -> list[int]:
        possible_games = []
        for line in self.lines:
            game_id, sets = self.parse_input(line)
            possible_game_flag = True
            for set in sets:
                if (set.get('red', 0) > num_red) or (set.get('green', 0) > num_green) or (set.get('blue', 0) > num_blue):
                    possible_game_flag = False
            if possible_game_flag:
                possible_games.append(game_id)
        
        return possible_games

    def identify_minimum_possible_cubes_for_each_game(self) -> list[GameSet]:
        min_possible_items = []
        for line in self.lines:
            game_id, sets = self.parse_input(line)
            min_set = {}
            for set in sets:
                for color in ['red', 'green', 'blue']:
                    if color in set:
                        if set.get(color) > min_set.get(color, 0):
                            min_set[color] = set.get(color)
            min_possible_items.append(min_set)
        return min_possible_items

if __name__ == "__main__":

    solver = Solver()

    # test_line = solver.lines[0]
    # print(test_line)
    # print(solver.parse_game_number(test_line))
    # print(solver.parse_game_set(test_line))
    # print(solver.parse_set(solver.parse_game_set(test_line)[0]))
    # print(solver.parse_input(test_line))

    possible_games = solver.identify_possible_games(num_red=12, num_green=13, num_blue=14)
    print(f"Solution to problem 1: {sum(possible_games)}")

    min_items = solver.identify_minimum_possible_cubes_for_each_game()
    sum_of_powers = 0
    for m in min_items:
        power = 1
        for v in m.values():
            power *= v
        sum_of_powers += power
    print(f"Solution to problem 2: {sum_of_powers}")