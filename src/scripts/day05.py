from scripts.input_manager import strip_lines


def part_one(filename: str) -> int:
    lines = strip_lines(filename)

    coordinates = make_coordinates(lines)
    vents = Vents(get_size(coordinates))

    vents.mark_vertical(coordinates)
    vents.mark_horizontal(coordinates)

    return vents.score()


def part_two(filename: str) -> int:
    lines = strip_lines(filename)

    coordinates = make_coordinates(lines)
    vents = Vents(get_size(coordinates))

    vents.mark_vertical(coordinates)
    vents.mark_horizontal(coordinates)
    vents.mark_down_diagonal(coordinates)
    vents.mark_up_diagonal(coordinates)

    return vents.score()


class Vents:
    def __init__(self, size: int):
        self.rows = []
        for _ in range(0, size):
            self.rows.append([0]*size)

    def mark_vertical(self, coordinates: list):
        for pair in coordinates:
            start = pair[0]
            end = pair[1]
            if start[0] == end[0]:
                col = start[0]
                row = min(start[1], end[1])
                diff = abs(start[1]-end[1])
                for i in range(0, diff+1):
                    self.rows[row+i][col] += 1

    def mark_horizontal(self, coordinates: list):
        for pair in coordinates:
            start = pair[0]
            end = pair[1]
            if start[1] == end[1]:
                col = min(start[0], end[0])
                row = start[1]
                diff = abs(start[0]-end[0])
                for i in range(0, diff+1):
                    self.rows[row][col+i] += 1

    def mark_down_diagonal(self, coordinates: list):
        for pair in coordinates:
            start = pair[0]
            end = pair[1]
            if start[0] - end[0] == start[1] - end[1]:
                col = min(start[0], end[0])
                row = min(start[1], end[1])
                diff = abs(start[0]-end[0])
                for i in range(0, diff+1):
                    self.rows[row+i][col+i] += 1

    def mark_up_diagonal(self, coordinates: list):
        for pair in coordinates:
            start = pair[0]
            end = pair[1]
            if start[0] - end[0] == -(start[1] - end[1]):
                col = min(start[0], end[0])
                row = max(start[1], end[1])
                diff = abs(start[0]-end[0])
                for i in range(0, diff+1):
                    self.rows[row-i][col+i] += 1

    def score(self) -> int:
        total = 0
        for row in self.rows:
            for num in row:
                if num > 1:
                    total += 1
        return total


def get_size(coordinates: list) -> list:
    size = [0, 0]
    for pair in coordinates:
        for xy in pair:
            size[0] = max(size[0], xy[0])
            size[1] = max(size[1], xy[1])
    return max(size) + 1


def make_coordinates(lines: list) -> list:
    pairs = []
    for line in lines:
        pairs.append(line.split(' -> '))
    for pair in pairs:
        pair[0] = pair[0].split(',')
        pair[1] = pair[1].split(',')
    for pair in pairs:
        for xy in pair:
            xy[0] = int(xy[0])
            xy[1] = int(xy[1])
    return pairs
