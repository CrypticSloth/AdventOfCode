class InputReader:
    def __init__(self, input_path:str):
        self.input_path = input_path

        with open(self.input_path, 'r') as f:
            self.lines = f.readlines()

        # Remove new line characters "\n"
        self.lines = [l.strip() for l in self.lines]


class DialReader(InputReader):
    def __init__(self, input_path:str):
        super().__init__(input_path)
    
    def get_direction(self, line:str) -> str:
        direction = line[0]
        assert direction in ['L', 'R'], "direction found was not either 'L' or 'R'"
        return direction

    def get_turn_amount(self, line:str) -> int:
        turn_amount = int(line[1:])
        return turn_amount


class Dial:
    def __init__(self, initial_value:int = 50):
        self.dial_value = initial_value
        self.zero_counter = 0
        self.click_counter = 0

    @property
    def dial_value(self) -> int:
        return self._dial_value

    @dial_value.setter
    def dial_value(self, value: int) -> None:
        # enforce 0-99 on any assignment
        self._dial_value = value % 100

    def turn_dial(self, turn_direction: str, turn_amount: int) -> int:
        assert turn_direction in ['L', 'R'], "Turn direction can either be 'L' or 'R'"

        if turn_direction == 'L':
            delta = (self.dial_value - turn_amount)
        else:
            delta = (self.dial_value + turn_amount)

        # How many *full* circles did you do?
        self.click_counter += turn_amount // 100

        # Did you cross the boundary once?
        if (delta <= 0) | (delta >= 100):
            # if position was zero do not count
            if self.dial_value != 0:
                self.click_counter += 1

        self.dial_value = delta % 100
        
        if self.dial_value == 0:
            self.zero_counter += 1

        return self.dial_value


if __name__ == '__main__':

    reader = DialReader('input_test.txt')
    input_lines = reader.lines

    dial = Dial(initial_value=50)
    for line in input_lines:
        turn_direction, turn_amount = reader.get_direction(line), reader.get_turn_amount(line)
        dial.turn_dial(turn_direction, turn_amount)
        # print(line)
        # print(dial.dial_value, dial.click_counter)
    
    print(dial.dial_value)
    print(dial.zero_counter)
    print(dial.click_counter)


    dial = Dial(initial_value=1)
    dial.turn_dial('L', 1000)
    # dial.turn_dial('R', 52)
    print(dial.dial_value)
    print(dial.click_counter)

    print()
    dial = Dial(initial_value=0)
    dial.turn_dial('L', 10)
    # dial.turn_dial('R', 52)
    print(dial.dial_value)
    print(dial.click_counter)

    
