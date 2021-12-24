from main import Reader

def part_1(filename: str) -> int:
    directions = [line.split(' ') for line in Reader(filename).getLinesStripped()]
    directions = [[direction, int(magnitude)] for direction, magnitude in directions]
    submarine = HorizontalSubmarine()
    submarine.navigate(directions)
    return submarine.horizontal * submarine.depth


def part_2(filename: str) -> int:
    directions = [line.split(' ') for line in Reader(filename).getLinesStripped()]
    directions = [[direction, int(magnitude)] for direction, magnitude in directions]
    submarine = AimSubmarine()
    submarine.navigate(directions)
    return submarine.horizontal * submarine.depth

class HorizontalSubmarine():
    def __init__(self):
        self.depth = 0
        self.horizontal = 0
    
    def navigate(self, directions: list):
        for direction, magnitude in directions:
            if direction == "forward":
                self.move_forward(magnitude)
            if direction == "down":
                self.move_down(magnitude)
            if direction == "up":
                self.move_up(magnitude)
            
    def move_forward(self, magnitude):
        self.horizontal += magnitude

    def move_up(self, magnitude):
        self.depth -= magnitude

    def move_down(self, magnitude):
        self.depth += magnitude

class AimSubmarine():
    def __init__(self):
        self.depth = 0
        self.horizontal = 0
        self.aim = 0
    
    def navigate(self, directions: list):
        for direction, magnitude in directions:
            if direction == "forward":
                self.move_forward(magnitude)
            if direction == "down":
                self.aim_down(magnitude)
            if direction == "up":
                self.aim_up(magnitude)
            
    def move_forward(self, magnitude):
        self.horizontal += magnitude
        self.depth += magnitude * self.aim

    def aim_up(self, magnitude):
        self.aim -= magnitude

    def aim_down(self, magnitude):
        self.aim += magnitude

if __name__ == '__main__':
    assert part_1('day02_example.txt') == 150
    assert part_1('day02_input.txt') == 1480518

    assert part_2('day02_example.txt') == 900
    assert part_2('day02_input.txt') == 1282809906