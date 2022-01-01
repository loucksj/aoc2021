from scripts.main import Reader

# up-left, up, up-right, left, right, down-left, down, down-right
DIRECTIONS = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

def part_one(filename: str) -> int:
    return Board(filename).step(100)

def part_two(filename: str) -> int:
    board = Board(filename)
    step = 0
    while True:
        step += 1
        for row in range(10):
            for col in range(10):
                board.energize(row, col)
        if board.reset_nines() == 100:
            return step

class Board:
    def __init__(self, filename: str):
        self.rows = []
        for line in Reader(filename).lines():
            self.rows.append([int(x) for x in line])
    
    def step(self, times: int) -> int:
        flashes = 0
        for _ in range(times):
            for row in range(10):
                for col in range(10):
                    self.energize(row, col)
            flashes += self.reset_nines()
        return flashes

    def energize(self, row: int, col: int):
        if 0 <= row < 10 and 0 <= col < 10:
            self.rows[row][col] += 1
            if self.rows[row][col] == 10:
                for r, c in DIRECTIONS:
                    self.energize(row + r, col + c)
    
    def reset_nines(self) -> int:
        resets = 0
        for row in range(10):
            for col in range(10):
                if self.rows[row][col] > 9:
                    self.rows[row][col] = 0
                    resets += 1
        return resets
