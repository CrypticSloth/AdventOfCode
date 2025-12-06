import operator

class InputReader:
    def __init__(self, input_path:str):
        self.input_path = input_path

        with open(self.input_path, 'r') as f:
            self.lines = f.readlines()

        self.grid = []
        for line in self.lines:
            line = line.strip()
            nums = line.split(' ')
            nums = [n for n in nums if n != '']
            self.grid.append(nums)

        # Transpose list
        self.grid = [list(row) for row in zip(*self.grid)]

        # Separate operators from grids
        self.grid = [(n[0:-1], n[-1]) for n in self.grid]


class InputReader2:

    def __init__(self, input_path:str):
        with open(input_path) as inputfile:
            self.rows = [line for line in inputfile]
        self.columns = list(zip(*self.rows))

        # print(self.columns)
        self.grid = []
        op = None
        nums = []
        for i in range(len(self.columns)):
            c = self.columns[i]
            if (c[-1] != ' '):
                op = c[-1]
            num = ''
            for n in c[0:-1]:
                if n!= ' ':
                    num = num + n 
            nums.append(num)
            # If column is all empty or at the end of the file, process the next equation
            if len(set(c)) == 1 or i == len(self.columns) - 1:
                self.grid.append(([x for x in nums if x != ''][::-1], op))
                op = None
                nums = []


class CephalopodMathSolver():

    def __init__(self, grid):
        self.grid = grid
        self.operators = {
            '+' : operator.add,
            '-' : operator.sub,
            '*' : operator.mul,
            '/' : operator.truediv,
            '%' : operator.mod,
            '^' : operator.xor,
        }

    def solve(self) -> int:
        total = 0
        for g in self.grid:
            operator = g[1]
            nums = g[0]
            r = nums[0]
            for n in nums[1:]:
                r = self.operators[operator](int(r), int(n))
            total += r
        return total

if __name__ == '__main__':

    reader = InputReader('input.txt')
    print(reader.grid)

    reader2 = InputReader2('input.txt')
    print(reader2.grid)

    cms = CephalopodMathSolver(reader.grid)
    print(cms.solve())

    cms = CephalopodMathSolver(reader2.grid)
    print(cms.solve())
    
