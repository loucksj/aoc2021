from scripts.input_manager import split_str_int_pairs


def part_one(filename: str) -> int:
    return Submarine().navigate_from_file(filename).vector()


def part_two(filename: str) -> int:
    return AimSubmarine().navigate_from_file(filename).vector()


class Submarine():
    def __init__(self):
        self.aim = 0
        self.depth = 0
        self.horizontal = 0

    def vector(self):
        return self.horizontal * self.depth

    def navigate_from_file(self, filename: str):
        return self.navigate(split_str_int_pairs(filename))

    def navigate(self, directions: list):
        for direction, amt in directions:
            self.move_controls()[direction](amt)
        return self

    def forward(self, amt):
        self.horizontal += amt
        self.depth += amt * self.aim

    def up(self, amt):
        self.depth -= amt

    def down(self, amt):
        self.depth += amt

    def move_controls(self) -> dict:
        return {'forward': self.forward,
                'up': self.up,
                'down': self.down}


class AimSubmarine(Submarine):
    def up(self, amt):
        self.aim -= amt

    def down(self, amt):
        self.aim += amt
