from itertools import product, permutations

class Solver:

    def __init__(self):

        with open('input_test.txt', 'r') as f:
            self.lines = f.readlines()

        self.lines = [l.strip() for l in self.lines]

        self.sums = self.sum_parser()
        self.integers = self.integer_parser()
        self.operators = ['+', '*']

        assert len(self.sums) == len(self.integers), "Length of lines not the same"

    def sum_parser(self) -> list[str]:
        sums = []
        for line in self.lines:
            sums.append(int(line.split(":")[0]))
        return sums

    def integer_parser(self) -> list[str]:
        integers = []
        for line in self.lines:
            int_list = line.split(":")[1].split(' ')
            int_list.remove('')
            int_list = [int(i) for i in int_list]
            integers.append(int_list)
        return integers
    
    def combinations(self, list1, list2):
        return ([opt1, opt2, opt3]
                for i,opt1 in enumerate(list1)
                for opt2 in list1[i+1:]
                for opt3 in list2)

    def solution_1(self) -> int:
        for i in range(len(self.sums)):
            total = self.sums[i]
            ints = self.integers[i]

            equations = {op:[] for op in self.operators}
            for op1 in self.operators:
                for n in range(len(ints)-1):
                    equations[op1].append(f"{ints[n]} {op1} {ints[n+1]}")
            
            for a in self.combinations(equations['*'], equations['+']):
                print(a)
                        


            


if __name__ == "__main__":

    solver = Solver()

    # print(solver.sum_parser())
    # print(solver.integer_parser())
    print(solver.solution_1())
