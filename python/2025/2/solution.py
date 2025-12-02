from typing import List

class InputReader:
    def __init__(self, input_path:str):
        self.input_path = input_path

        with open(self.input_path, 'r') as f:
            self.lines = f.readlines()

        self.input = self.lines[0]


class PasswordReader(InputReader):
    def __init__(self, input_path:str):
        super().__init__(input_path)
    
    def parse_ranges(self) -> List[str]:
        return [g.split('-') for g in self.input.split(',')]


class InvalidIdFinder:
    def __init__(self, id_ranges:List[str]):
        self.id_ranges = id_ranges


    def get_all_ids_from_range(self, id_range:List[str]) -> List[str]:
        start = int(id_range[0])
        end = int(id_range[1])
        unwrapped_ids = [str(i) for i in range(start, end+1)]
        return unwrapped_ids


    def is_invalid_id_part1(self, target_id:str) -> bool:
        # An invalid id is one that is made only of some sequence of digits repeated twice
        # e.g. 55, 6464, 123123
        num_digits = len(target_id) 
        first_half = target_id[num_digits//2:]
        second_half = target_id[:num_digits//2]
        return first_half == second_half


    def solution_1(self) -> int:
        invalid_ids = []
        for id_range in self.id_ranges:
            ids_in_range = self.get_all_ids_from_range(id_range)
            for target_id in ids_in_range:
                if self.is_invalid_id_part1(target_id):
                    invalid_ids.append(int(target_id))
        # print(invalid_ids)
        return sum(invalid_ids)
        
        


if __name__ == '__main__':
    
    reader = PasswordReader('input.txt')
    id_finder = InvalidIdFinder(reader.parse_ranges())  

    print(id_finder.solution_1())

    example_id_range = id_finder.get_all_ids_from_range(id_finder.id_ranges[0])
    print(id_finder.is_invalid_id_part1('121'))

