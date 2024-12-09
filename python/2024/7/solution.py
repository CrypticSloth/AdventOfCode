import itertools
import tqdm

class Solver:

    def __init__(self):

        with open('input.txt', 'r') as f:
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

    def operator_combinations(self, length:int, operators:list[str] = None) -> list[str]:
        if not operators:
            operators = self.operators
        return list(itertools.product(*([operators] * length)))

    def concat_integer(self, int1:int, int2:int)->str:
        return str(int1) + str(int2)
    

    def solution_1(self) -> int:
        final_sum = 0
        for s in tqdm.tqdm(range(len(self.sums))):
            total = self.sums[s]
            ints = self.integers[s]

            for operations in self.operator_combinations(len(ints)-1):
                k = 0
                for i in range(len(ints) - 1):
                    op = operations[i]
                    if i == 0:
                        x = ints[i]
                        y = ints[i+1]
                        k = eval(str(x) + op + str(y))
                    else:
                        k = eval(str(k) + op + str(ints[i+1]))
                # print(ints)
                # print(operations)
                # print(k)
                if k == total:
                    final_sum += total
                    break
        return final_sum

    def solution_2(self) -> int:
        final_sum = 0
        for s in tqdm.tqdm(range(len(self.sums))):
            total = self.sums[s]
            ints = self.integers[s]

            new_operators = self.operators + ['||']
            new_operator_combos = self.operator_combinations(len(ints)-1, new_operators)
            for operations in new_operator_combos:
                k = 0
                for i in range(len(ints) - 1):
                    op = operations[i]
                    if i == 0:
                        x = ints[i]
                        y = ints[i+1]
                        if op == '||':
                            k = int(self.concat_integer(x, y))
                        else: 
                            k = eval(str(x) + op + str(y))
                    else:
                        if op == '||':
                            k = int(self.concat_integer(k, ints[i+1]))
                        else:
                            k = eval(str(k) + op + str(ints[i+1]))
                if k == total:
                    final_sum += total
                    break
        return final_sum       


            


if __name__ == "__main__":

    solver = Solver()

    print(solver.solution_1())
    print(solver.solution_2())
