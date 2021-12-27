from scripts.main import Reader


def part_one(filename: str) -> int:
    return Vents(filename).score_orthogonal()


def part_two(filename: str) -> int:
    return Vents(filename).score_all()


class Vents:
    def __init__(self, filename: str):
        self.paths = self.paths_from_file(filename)
        self.rows = self.zero_rows()

    def zero_rows(self):
        rows = []
        max_x, max_y = self.get_max_xy()
        for _ in range(max_x+1):
            rows.append([0]*(max_y+1))
        return rows

    def mark_vents(self, only_orthogonal=False):
        for start, end in self.paths:
            if only_orthogonal and start[0] != end[0] and start[1] != end[1]:
                continue
            self.mark_line(start, end)

    def score_orthogonal(self) -> int:
        self.mark_vents(True)
        return sum([sum([1 if num > 1 else 0 for num in row]) for row in self.rows])

    def score_all(self) -> int:
        self.mark_vents()
        return sum([sum([1 if num > 1 else 0 for num in row]) for row in self.rows])

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

    def get_max_xy(self) -> tuple:
        max_x, max_y = 0, 0
        for pair in self.paths:
            for x, y in pair:
                max_x = max(max_x, x)
                max_y = max(max_y, y)
        return (max_x, max_y)

    def paths_from_file(self, filename: str) -> list:
        return [[list(map(int, pair.split(','))) for pair in path] for path in Reader(filename).split_lines(' -> ')]
