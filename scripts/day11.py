from scripts.main import Reader

# up-left, up, up-right, left
# right, down-left, down, down-right
DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
              (0, 1), (1, -1), (1, 0), (1, 1)]


def part_one(filename: str) -> int:
    return Board(filename).step(100).flashes


def part_two(filename: str) -> int:
    return Board(filename).sync().steps


class Board:
    def __init__(self, filename: str):
        self.rows = Reader(filename).integer_lines()
        self.steps = 0
        self.flashes = 0

    def step(self, times: int) -> int:
        for _ in range(times):
            self.energize_all()
        return self

    def sync(self) -> int:
        while sum(sum(col for col in row) for row in self.rows) != 0:
            self.energize_all()
        return self

    def energize_all(self):
        self.steps += 1
        for ri, row in enumerate(self.rows):
            for ci, _ in enumerate(row):
                self.energize(ri, ci)
        self.reset_nines()

    def energize(self, row: int, col: int):
        if 0 <= row < len(self.rows) and 0 <= col < len(self.rows[0]):
            self.rows[row][col] += 1
            if self.rows[row][col] == 10:
                for r, c in DIRECTIONS:
                    self.energize(row + r, col + c)

    def reset_nines(self):
        for ri, row in enumerate(self.rows):
            for ci, val in enumerate(row):
                if val > 9:
                    self.rows[ri][ci] = 0
                    self.flashes += 1
