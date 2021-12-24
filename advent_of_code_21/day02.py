from main import Reader


def part_1(filename: str) -> int:
    return HorizontalSubmarine().navigate_from_file(filename).vector()


def part_2(filename: str) -> int:
    return AimSubmarine().navigate_from_file(filename).vector()


class Submarine():
    def __init__(self):
        self.aim = 0
        self.depth = 0
        self.horizontal = 0

    def navigate_from_file(self, filename: str):
        directions = Reader(filename).getLinesSplit(' ')
        directions = [[direction, int(magnitude)]
                      for direction, magnitude in directions]
        return self.navigate(directions)

    def navigate(self, directions: list):
        for direction, magnitude in directions:
            match direction:
                case "forward":
                    self.forward(magnitude)
                case "down":
                    self.down(magnitude)
                case "up":
                    self.up(magnitude)
        return self

    def vector(self):
        return self.horizontal * self.depth

    def forward(self, magnitude):
        self.horizontal += magnitude
        self.depth += magnitude * self.aim


class HorizontalSubmarine(Submarine):
    def up(self, magnitude):
        self.depth -= magnitude

    def down(self, magnitude):
        self.depth += magnitude


class AimSubmarine(Submarine):
    def up(self, magnitude):
        self.aim -= magnitude

    def down(self, magnitude):
        self.aim += magnitude


if __name__ == '__main__':
    assert part_1('day02_example.txt') == 150
    assert part_1('day02_input.txt') == 1480518

    assert part_2('day02_example.txt') == 900
    assert part_2('day02_input.txt') == 1282809906
