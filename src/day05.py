from src.main import Reader


def part_one(filename: str) -> int:
    return Vents(filename).mark_orthogonal().score()


def part_two(filename: str) -> int:
    return Vents(filename).mark_all().score()


class Vents:
    def __init__(self, filename: str):
        self.paths = self.paths_from_file(filename)
        self.rows = [[0] * (self.max_y() + 1) for _ in range(self.max_x() + 1)]

    def paths_from_file(self, filename: str) -> list:
        return [[list(map(int, pair.split(','))) for pair in path] for path in Reader(filename).split_lines(' -> ')]

    def score(self) -> int:
        return sum([sum([1 if num > 1 else 0 for num in row]) for row in self.rows])

    def mark_all(self):
        for start, end in self.paths:
            self.mark_line(start, end)
        return self

    def mark_orthogonal(self):
        for start, end in self.paths:
            if start[0] == end[0] or start[1] == end[1]:
                self.mark_line(start, end)
        return self

    def mark_line(self, start: list, end: list):
        for col, row in self.linepoints(start, end):
            self.rows[row][col] += 1

    def linepoints(self, startpoint: list, endpoint: list) -> list:
        x_start, y_start = startpoint
        x_end, y_end = endpoint
        length = max(abs(x_start - x_end), abs(y_start - y_end)) + 1
        return list(zip(self.make_range(x_start, x_end, length), self.make_range(y_start, y_end, length)))

    def make_range(self, start: int, end: int, length: int):
        values = list(range(min(start, end), max(start, end) + 1))
        if start > end:
            values = list(reversed(values))
        if len(values) == 1:
            values = [start] * length
        return values

    def max_x(self) -> int:
        return max([max([x for x, _ in pair]) for pair in self.paths])

    def max_y(self) -> int:
        return max([max([y for _, y in pair]) for pair in self.paths])
