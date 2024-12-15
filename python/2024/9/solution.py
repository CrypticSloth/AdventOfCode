import re
import tqdm

class Solver:

    def __init__(self):
        with open('input.txt', 'r') as f:
            self.line = f.readlines()[0].strip()
        self.block_count = {}
        self.space_representation = self.convert_input_to_space_representation()
        print(self.space_representation)

    def convert_input_to_space_representation(self) -> str:
        space_representation = ''
        counter = 0
        for i in range(len(self.line)):
            c = int(self.line[i])
            if i % 2 == 0: # Characters at even spacing represent the number of blocks in the file
                space_representation = space_representation + (str(counter) * c)
                self.block_count[str(counter)] = c
                counter += 1
            else: # Characters at odd spacing represent the amount of free space
                space_representation = space_representation + ('.' * c)
        return space_representation

    def replace_last(self, source_string, replace_what, replace_with):
        head, _sep, tail = source_string.rpartition(replace_what)
        return head + replace_with + tail

    def check_if_done(self, string:str, ind:int) -> bool:
        # If all characters to the left of the indice are not '.' and all to the right are '.' then we are done
        left_substring = string[0:ind]
        right_substring = string[ind:]
        flag = True

        # If there are any non '.' characters return False
        for c in right_substring:
            if c != '.':
                flag = False
        return flag

    def solution_1(self)->int:
        # I think we need to handle integers >= 10, so we need to keep track of which group we are at at the end?
        # The challenge is that the integer 10 would take up just one "." in the system, so our indexing will get all outta wack.
        # Maybe we just create a new list, where we iterate from the front, find the first ".", then find the first largest integer
        # in the back and replace the "." with it and remove it from the back. We would need an integer counter to keep track of what integers
        # are available in the list. Once there are no more of the largest value, we move to the next largest value.
        sorted_mem = []
        # sr = str(self.space_representation)
        for s in tqdm.tqdm(range(len(self.space_representation))):
            if not self.check_if_done(self.space_representation, s):
                if self.space_representation[s] == '.':
                    # if self.check_if_done(self.space_representation)
                    # Check for the last available digit with >0 block_count and insert it in the '.' and reduce the count.
                    last_key = list(self.block_count.keys())[-1]
                    self.block_count[last_key] -= 1
                    if self.block_count[last_key] == 0:
                        self.block_count.pop(last_key, None)
                    sorted_mem.append(last_key)
                    # Remove the key from the space representation at the end and replace it with a period)
                    self.space_representation = self.replace_last(self.space_representation, last_key, '.')
                else:
                    # If it isn't a period, then append the digit
                    sorted_mem.append(self.space_representation[s])
            else:
                sorted_mem.append('.')

            # print(sorted_mem)
            # print(self.space_representation)
            # print()
        print(sorted_mem)

        # Evaluate the checksum
        checksum = 0
        for i in range(len(sorted_mem)):
            if sorted_mem[i] != '.':
                checksum += i * int(sorted_mem[i])
        return checksum


            

if __name__ == "__main__":

    solver = Solver()

    print(solver.solution_1())
    # print(solver.check_if_done('000000......', 7))