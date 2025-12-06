from typing import List
import tqdm

class InputReader:
    def __init__(self, input_path:str):
        self.input_path = input_path

        with open(self.input_path, 'r') as f:
            self.lines = f.readlines()

        self.fresh_ranges = []
        self.available_ingredients = []
        no_line_flag = False
        for line in self.lines:
            line = line.strip()
            if line == '':
                no_line_flag = True
                continue
            
            if not no_line_flag:
                tup = line.split('-')
                tup[0] = int(tup[0])
                tup[1] = int(tup[1])
                self.fresh_ranges.append(tuple(tup))
            else:

                self.available_ingredients.append(int(line))

class FreshIngredientChecker():

    def __init__(self, fresh_ranges:List[str], available_ingredients:List[str]):
        self.fresh_ranges = fresh_ranges
        self.available_ingredients = available_ingredients

    def solution_1(self) -> int:
        fresh_ingredients = set()
        for r in self.fresh_ranges:
            for i in self.available_ingredients:
                if (i >= r[0]) & (i <= r[1]):
                    fresh_ingredients.add(i)
        return len(list(fresh_ingredients))

    def ingredient_merger(self) -> List[tuple]:
        merged_ingredients = [self.fresh_ranges[0]]
        for r in self.fresh_ranges[1:]:
            merged_flag = False
            for i in range(len(merged_ingredients)):
                m = merged_ingredients[i]
                if ((r[0] >= m[0]) & (r[0] <= m[1])) & (r[1] >= m[1]):
                    merged_ingredients.append((m[0], r[1]))
                    merged_ingredients.pop(i)
                    merged_flag = True
                elif ((r[1] >= m[0]) & (r[1] <= m[1])) & (r[0] <= m[1]):
                    merged_ingredients.append((r[0], m[1]))
                    merged_ingredients.pop(i)
                    merged_flag = True

                print(r, m)
                print(merged_ingredients)
                print(merged_flag)
                print('---')
            if not merged_flag:
                merged_ingredients.append(r)
        return merged_ingredients

    def ingredient_merger_v2(self) -> List[tuple]:
        merged_ingredients = self.fresh_ranges.copy()
        # while True:
        for y in range(len(merged_ingredients)):
            r = merged_ingredients[y]
            merged_flag = False
            for i in range(len(merged_ingredients)):
                m = merged_ingredients[i]
                if ((r[0] >= m[0]) & (r[0] <= m[1])) & (r[1] >= m[1]):
                    merged_ingredients[i] = (m[0], r[1])
                    # merged_ingredients.pop(i)
                    merged_flag = True
                elif ((r[1] >= m[0]) & (r[1] <= m[1])) & (r[0] <= m[1]):
                    merged_ingredients[i] = (r[0], m[1])
                    # merged_ingredients.pop(i)
                    merged_flag = True
            # print(r, m)
            # print(merged_ingredients)
            # print(merged_flag)
            # print('---')
            # break
            # if not merged_flag:
            #     break
            # if not merged_flag:
            #     merged_ingredients.append(r)
        return list(set(merged_ingredients))

    def solution_2(self) -> int:
        merged_ingredients = self.ingredient_merger_v2()
        num_ingredients = 0
        for i in merged_ingredients:
            num_ingredients += (i[1] - i[0]) + 1
        return num_ingredients
    
if __name__ == '__main__':

    reader = InputReader('input.txt')
    print(reader.fresh_ranges)
    print(reader.available_ingredients)

    fic = FreshIngredientChecker(reader.fresh_ranges, reader.available_ingredients)

    # print(fic.ingredient_merger_v2())

    print(fic.solution_1())
    print(fic.solution_2())