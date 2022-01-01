from scripts.main import Reader

# up-left, up, up-right, left
# right, down-left, down, down-right
DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
              (0, 1), (1, -1), (1, 0), (1, 1)]


def part_one(filename: str) -> int:
    return Board(filename).step(100).flashes


def part_two(filename: str) -> int:
    return Board(filename).allflash_at()


class Board:
    def __init__(self, filename: str):
        self.rows = Reader(filename).integer_lines()
        self.flashes = 0

    def step(self, times: int) -> int:
        for _ in range(times):
            self.energize_all()
        return self

    def allflash_at(self) -> int:
        step = 0
        while True:
            step += 1
            self.energize_all()
            if sum(sum(col for col in row) for row in self.rows) == 0:
                return step

    def energize_all(self):
        for row in range(10):
            for col in range(10):
                self.energize(row, col)
        self.reset_nines()

    def energize(self, row: int, col: int):
        if 0 <= row < 10 and 0 <= col < 10:
            self.rows[row][col] += 1
            if self.rows[row][col] == 10:
                for r, c in DIRECTIONS:
                    self.energize(row + r, col + c)

    def reset_nines(self):
        for row in range(10):
            for col in range(10):
                if self.rows[row][col] > 9:
                    self.rows[row][col] = 0
                    self.flashes += 1
