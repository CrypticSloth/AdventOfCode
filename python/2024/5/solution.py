
class Solver:

    def __init__(self):

        with open('input.txt', 'r') as f:
            self.lines = f.readlines()
        
        self.ordering_rules = self.parse_ordering_rules()
        self.update_pages = self.parse_update_pages()

    def parse_ordering_rules(self) -> list[tuple[int,int]]:
        order_vals = []
        for line in self.lines:
            if "|" in line:
                s = line.split("|")
                order_vals.append((int(s[0]), int(s[1])))
        return order_vals

    def parse_update_pages(self) -> list[list[int]]:
        update_pages = []
        for line in self.lines:
            if "," in line:
                s = line.split(",")
                s = [int(i) for i in s]
                update_pages.append(s)
        return update_pages
    
    def find_location_of_items(self, search:int, l:list[int]) -> int:
        indices = [i for i, e in enumerate(l) if e == search]
        if len(indices) > 0:
            return indices[0]
        else:
            return None

    def check_if_page_is_valid(self, page:list[int], rules:list[tuple[int,int]]) -> bool:
        flag = True
        for r in rules:
            min_page = self.find_location_of_items(r[0], page)
            max_page = self.find_location_of_items(r[1], page)
            if (min_page is not None) & (max_page is not None):
                if min_page > max_page:
                    flag = False
        return flag

    def order_page_using_rule(self, page:list[int], rules: list[tuple[int,int]]) -> list[int]:
        page_sorted = False
        while not page_sorted:
            old_page = page.copy()
            for r in rules:
                # print(old_page)
                min_page = self.find_location_of_items(r[0], page)
                max_page = self.find_location_of_items(r[1], page)
                if (min_page is not None) & (max_page is not None):
                    if min_page > max_page:
                        # Put the min_page right before the max_page in the list
                        page.insert(max_page, page.pop(min_page))
                # print(page)
            if page == old_page:
                # No changes were made and the page is now sorted
                page_sorted = True

        return page

    def solution_1(self) -> int:
        valid_indices = []
        for page in self.update_pages:
            if self.check_if_page_is_valid(page, self.ordering_rules):
                middle_indice = page[int(len(page)//2)]
                valid_indices.append(middle_indice)
        return sum(valid_indices)

    def solution_2(self) -> int:
        invalid_indices = []
        for page in self.update_pages:
            if not self.check_if_page_is_valid(page, self.ordering_rules):
                ordered_page = self.order_page_using_rule(page=page, rules=self.ordering_rules)
                middle_indice = ordered_page[int(len(ordered_page)//2)]
                invalid_indices.append(middle_indice)
        return sum(invalid_indices)
        

if __name__ == "__main__":

    solver = Solver()
    print(f"Solution to problem 1: {solver.solution_1()}")
    print(f"Solution to problem 2: {solver.solution_2()}")