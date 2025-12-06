from typing import List
from itertools import combinations

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


    def any_items_overlap(self,l):

        # For each possible pair of lists in l
        for item1, item2 in combinations(l, 2):

            min1, max1 = item1
            min2, max2 = item2

            if min1 > max2 or max1 < min2:
                # no overlap so ignore this pair
                continue

            else:  # One of the combinations overlaps, so return them
                return item1, item2

        return None


    def ingredient_merger(self):

        l = self.fresh_ranges.copy()

        while True:

            if not self.any_items_overlap(l):
                # No items overlapped - break the loop and finish
                print(l)
                break

            else:  # There are still overlaps
                item1, item2 = self.any_items_overlap(l)

                # Remove the items from the main list
                l.remove(item1)
                l.remove(item2)

                # Replace them with a merged version
                item_values = item1 + item2
                l.append((min(item_values), max(item_values)))
                # Start the loop again to check for any other overlaps
        return l
    

    def solution_2(self) -> int:
        merged_ingredients = self.ingredient_merger()
        num_ingredients = 0
        for i in merged_ingredients:
            num_ingredients += (i[1] - i[0]) + 1
        return num_ingredients
    
if __name__ == '__main__':

    reader = InputReader('input.txt')
    print(reader.fresh_ranges)
    print(reader.available_ingredients)

    fic = FreshIngredientChecker(reader.fresh_ranges, reader.available_ingredients)

    print(fic.solution_1())
    print(fic.solution_2())