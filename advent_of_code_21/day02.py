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

class Submarine():
    def __init__(self):
        self.depth = 0
        self.horizontal = 0
    
    def navigate(self, directions: list):
        for direction, magnitude in directions:
            match direction:
                case "forward":
                    self.forward(magnitude)
                case "down":
                    self.down(magnitude)
                case "up":
                    self.up(magnitude)

class HorizontalSubmarine(Submarine):   
    def forward(self, magnitude):
        self.horizontal += magnitude

    def up(self, magnitude):
        self.depth -= magnitude

    def down(self, magnitude):
        self.depth += magnitude

class AimSubmarine(Submarine):
    def __init__(self):
        super().__init__()
        self.aim = 0
            
    def forward(self, magnitude):
        self.horizontal += magnitude
        self.depth += magnitude * self.aim

    def up(self, magnitude):
        self.aim -= magnitude

    def down(self, magnitude):
        self.aim += magnitude

if __name__ == '__main__':
    assert part_1('day02_example.txt') == 150
    assert part_1('day02_input.txt') == 1480518

    assert part_2('day02_example.txt') == 900
    assert part_2('day02_input.txt') == 1282809906