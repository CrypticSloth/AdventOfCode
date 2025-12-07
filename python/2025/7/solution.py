from typing import Tuple
import numpy as np

class InputReader:
    def __init__(self, input_path:str):
        self.input_path = input_path

        with open(self.input_path, 'r') as f:
            self.lines = f.readlines()

        self.input_array = []
        for l in self.lines:
            line = l.strip()
            items = []
            for c in line:
                items.append(c)
            self.input_array.append(items)

        self.input_array = np.array(self.input_array)

        self.start_loc = np.argwhere(self.input_array == 'S')[0]


class TachyonWalker:

    def __init__(self, input_array, loc: Tuple[int]):
        self.input_array = input_array
        self.loc = loc


class Solution1:

    def __init__(self, input_file:str):
        self.reader = InputReader(input_file)
    

    def check_duplicate_beam(self, tw_list, tw):
        for b in tw_list:
            if b.loc == tw.loc:
                return True
        return False
    

    def solve(self):
        split_counter = 0
        tachyon_beams = [TachyonWalker(self.reader.input_array, self.reader.start_loc)]
        end = False
        arr_output = self.reader.input_array.copy()
        while True:
            beam_locs_to_remove = []
            beams_to_process = len(tachyon_beams)
            for i in range(beams_to_process):
                beam = tachyon_beams[i]
                beam.loc = [int(beam.loc[0]+1), int(beam.loc[1])]
                if self.reader.input_array[*beam.loc] == '^':
                    beam_locs_to_remove.append(beam.loc)
                    loc_l = [beam.loc[0], beam.loc[1]-1]
                    loc_r = [beam.loc[0], beam.loc[1]+1]

                    w1 = TachyonWalker(self.reader.input_array, loc_l)
                    w2 = TachyonWalker(self.reader.input_array, loc_r)
                    tachyon_beams.append(w1)
                    tachyon_beams.append(w2)
                    split_counter += 1
                else:
                    if beam.loc[0] >= self.reader.input_array.shape[0]-1:
                        end = True

            tachyon_beams = [beam for beam in tachyon_beams if beam.loc not in beam_locs_to_remove]
            
            # Remove any duplicate beams
            tachyon_beams_c = []
            tachyon_beams_locs = []
            for i, beam in enumerate(tachyon_beams):
                if beam.loc not in tachyon_beams_locs:
                    tachyon_beams_c.append(beam)
                    tachyon_beams_locs.append(beam.loc)

            tachyon_beams = tachyon_beams_c

            for i, b in enumerate(tachyon_beams):
                print(i, b.loc)

            # locs = [tuple(b.loc) for b in tachyon_beams]
            # if len(list(set(locs))) != len(locs):
            #     print("DUPLICATE BEAMS")
            
            # for x in range(len(tachyon_beams)):
            #     l = tachyon_beams[x]
            #     print(x, l.loc)

            c = self.reader.input_array.copy()[beam.loc[0]]
            for i, b in enumerate(tachyon_beams):
                c[b.loc[1]] = '|'
            arr_output[b.loc[0], :] = c

            # Print entire tree
            # for i in range(arr_output.shape[0]):
            #     s = ''
            #     for c in arr_output[i,:]:
            #         s = s + str(c)
            #     print(s)
            # # print(arr_output)
            # print()
            # input()

            if end:
                return split_counter


class TachyonWalkerQuantum:

    def __init__(self, input_array, loc: Tuple[int], direction:bool):
        self.input_array = input_array
        self.loc = loc


class Solution2:

    def __init__(self, input_file:str):
        self.reader = InputReader(input_file)
    

    def check_duplicate_beam(self, tw_list, tw):
        for b in tw_list:
            if b.loc == tw.loc:
                return True
        return False
    

    def solve(self):
        split_counter = 0
        tachyon_beams = [TachyonWalker(self.reader.input_array, self.reader.start_loc)]
        end = False
        arr_output = self.reader.input_array.copy()
        while True:
            beam_locs_to_remove = []
            beams_to_process = len(tachyon_beams)
            for i in range(beams_to_process):
                beam = tachyon_beams[i]
                beam.loc = [int(beam.loc[0]+1), int(beam.loc[1])]
                if self.reader.input_array[*beam.loc] == '^':
                    beam_locs_to_remove.append(beam.loc)
                    loc_l = [beam.loc[0], beam.loc[1]-1]
                    loc_r = [beam.loc[0], beam.loc[1]+1]

                    w1r = TachyonWalkerQuantum(self.reader.input_array, loc_l, direction=1)
                    w2r = TachyonWalkerQuantum(self.reader.input_array, loc_r, direction=1)
                    w1l = TachyonWalkerQuantum(self.reader.input_array, loc_l, direction=0)
                    w2l = TachyonWalkerQuantum(self.reader.input_array, loc_r, direction=0)

                    tachyon_beams.append(w1r)
                    tachyon_beams.append(w2r)
                    split_counter += 1
                else:
                    if beam.loc[0] >= self.reader.input_array.shape[0]-1:
                        end = True

            tachyon_beams = [beam for beam in tachyon_beams if beam.loc not in beam_locs_to_remove]
            
            # Remove any duplicate beams
            tachyon_beams_c = []
            tachyon_beams_locs = []
            for i, beam in enumerate(tachyon_beams):
                if beam.loc not in tachyon_beams_locs:
                    tachyon_beams_c.append(beam)
                    tachyon_beams_locs.append(beam.loc)

            tachyon_beams = tachyon_beams_c

            for i, b in enumerate(tachyon_beams):
                print(i, b.loc)

            # locs = [tuple(b.loc) for b in tachyon_beams]
            # if len(list(set(locs))) != len(locs):
            #     print("DUPLICATE BEAMS")
            
            # for x in range(len(tachyon_beams)):
            #     l = tachyon_beams[x]
            #     print(x, l.loc)

            c = self.reader.input_array.copy()[beam.loc[0]]
            for i, b in enumerate(tachyon_beams):
                c[b.loc[1]] = '|'
            arr_output[b.loc[0], :] = c

            # Print entire tree
            # for i in range(arr_output.shape[0]):
            #     s = ''
            #     for c in arr_output[i,:]:
            #         s = s + str(c)
            #     print(s)
            # # print(arr_output)
            # print()
            # input()

            if end:
                return split_counter


if __name__ == '__main__':

    input_file = 'input.txt'

    r = InputReader(input_file)

    s1 = Solution1(input_file)
    print(s1.solve())
