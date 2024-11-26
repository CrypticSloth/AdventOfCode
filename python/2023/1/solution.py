class Solver():

    def __init__(self):

        self.string_digit_mapper = {
            'one': '1',
            'two': '2',
            'three': '3',
            'four': '4',
            'five': '5',
            'six': '6',
            'seven': '7',
            'eight': '8',
            'nine': '9'
        }

    def get_first_digit(self, l:str) -> str:
        for c in l:
            if c.isnumeric():
                return str(c)

    def get_last_digit(self, l:str) -> str:
        for c in l[::-1]:
            if c.isnumeric():
                return str(c)

    def find_substring_locations(self, s: str, substring:str) -> list[str]:
        return [i for i in range(len(s)) if s.startswith(substring, i)]

    def get_min_value_in_list_of_tuples(self, d: list) -> str:
        k,v = [t[0] for t in d], [t[1] for t in d]
        min_key = k[0]
        min_value = v[0]
        for i in range(len(v)):
            if v[i] < min_value:
                min_key = k[i]
                min_value = v[i]
        return min_key
    
    def get_max_value_in_list_of_tuples(self, d: list) -> str:
        k,v = [t[0] for t in d], [t[1] for t in d]
        min_key = k[0]
        min_value = v[0]
        for i in range(len(v)):
            if v[i] > min_value:
                min_key = k[i]
                min_value = v[i]
        return min_key

    def get_first_and_last_digits(self, l:str) -> tuple[str,str]:
        indexes = []
        for k,v in self.string_digit_mapper.items():
            ss_locs_k = self.find_substring_locations(l, k)
            ss_locs_v = self.find_substring_locations(l, v)
            for loc in ss_locs_k:
                indexes.append((k, loc))
            for loc in ss_locs_v:
                indexes.append((v, loc))
            
        # Get the first and last digits
        first_digit = self.get_min_value_in_list_of_tuples(indexes)
        last_digit = self.get_max_value_in_list_of_tuples(indexes)

        if not first_digit.isnumeric():
            first_digit = self.string_digit_mapper[first_digit]
        if not last_digit.isnumeric():
            last_digit = self.string_digit_mapper[last_digit]    

        return (first_digit, last_digit)


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    lines = [s.strip() for s in lines]

    solver = Solver()

    sum_1 = 0
    sum_2 = 0
    for line in lines:
        sum_1 += int(solver.get_first_digit(line) + solver.get_last_digit(line))

        first_digit, last_digit = solver.get_first_and_last_digits(line)
        sum_2 += int(first_digit + last_digit)

    print(f"Part one solution: {sum_1}")
    print(f"Part two solution: {sum_2}")