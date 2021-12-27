from scripts.main import Reader


def part_one(filename: str) -> int:
    return Vents(filename).mark_orthogonal().score()


def part_two(filename: str) -> int:
    return Vents(filename).mark_all().score()


class Vents:
    def __init__(self, filename: str):
        self.paths = self.paths_from_file(filename)
        self.rows = [[0]*(self.max_y() + 1) for _ in range(self.max_x() + 1)]

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
        for col, row in self.line_points(start, end):
            self.rows[row][col] += 1

    def line_points(self, start: list, end: list) -> list:
        x_range = range(min(start[0], end[0]), max(start[0], end[0]) + 1)
        y_range = range(min(start[1], end[1]), max(start[1], end[1]) + 1)
        if start[0] > end[0]:
            x_range = list(reversed(x_range))
        if start[1] > end[1]:
            y_range = list(reversed(y_range))
        if len(x_range) == 1:
            x_range = [x_range[0]]*len(y_range)
        if len(y_range) == 1:
            y_range = [y_range[0]]*len(x_range)
        return list(zip(x_range, y_range))

    def max_x(self) -> int:
        return max([max([x for x, _ in pair]) for pair in self.paths])

    def max_y(self) -> int:
        return max([max([y for _, y in pair]) for pair in self.paths])
