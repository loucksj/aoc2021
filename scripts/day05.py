from scripts.main import Reader


def part_one(filename: str) -> int:
    vents = Vents(filename)
    vents.mark_vertical()
    vents.mark_horizontal()
    return vents.score()


def part_two(filename: str) -> int:
    vents = Vents(filename)
    vents.mark_vents()
    return vents.score()


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

    def mark_vents(self):
        self.mark_vertical()
        self.mark_horizontal()
        self.mark_down_diagonal()
        self.mark_up_diagonal()

    def mark_vertical(self):
        for pair in self.paths:
            start = pair[0]
            end = pair[1]
            if start[0] == end[0]:
                col = start[0]
                row = min(start[1], end[1])
                diff = abs(start[1]-end[1])
                for i in range(0, diff+1):
                    self.rows[row+i][col] += 1

    def mark_horizontal(self):
        for pair in self.paths:
            start = pair[0]
            end = pair[1]
            if start[1] == end[1]:
                col = min(start[0], end[0])
                row = start[1]
                diff = abs(start[0]-end[0])
                for i in range(0, diff+1):
                    self.rows[row][col+i] += 1

    def mark_down_diagonal(self):
        for pair in self.paths:
            start = pair[0]
            end = pair[1]
            if start[0] - end[0] == start[1] - end[1]:
                col = min(start[0], end[0])
                row = min(start[1], end[1])
                diff = abs(start[0]-end[0])
                for i in range(0, diff+1):
                    self.rows[row+i][col+i] += 1

    def mark_up_diagonal(self):
        for pair in self.paths:
            start = pair[0]
            end = pair[1]
            if start[0] - end[0] == -(start[1] - end[1]):
                col = min(start[0], end[0])
                row = max(start[1], end[1])
                diff = abs(start[0]-end[0])
                for i in range(0, diff+1):
                    self.rows[row-i][col+i] += 1

    def score(self) -> int:
        return sum([sum([1 if num > 1 else 0 for num in row]) for row in self.rows])

    def get_max_xy(self) -> tuple:
        max_x, max_y = 0, 0
        for pair in self.paths:
            for x, y in pair:
                max_x = max(max_x, x)
                max_y = max(max_y, y)
        return (max_x, max_y)

    def paths_from_file(self, filename: str) -> list:
        return [[list(map(int, pair.split(','))) for pair in path] for path in Reader(filename).split_lines(' -> ')]
