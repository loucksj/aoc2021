from scripts.main import Reader

# up-left, up, up-right, left, right, down-left, down, down-right
DIRECTIONS = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

def part_one(filename: str) -> int:
    board = Board(filename)
    flashes = 0
    for _ in range(0, 100):
        for row in range(0, 10):
            for col in range(0, 10):
                board.energize(row, col)
        flashes += board.reset()
    return flashes

def part_two(filename: str) -> int:
    board = Board(filename)
    step = 0
    while True:
        step += 1
        for row in range(0, 10):
            for col in range(0, 10):
                board.energize(row, col)
        if board.reset() == 100:
            return step

class Board:
    def __init__(self, filename: str):
        self.rows = []
        for line in Reader(filename).lines():
            self.rows.append([int(x) for x in line])

    def energize(self, row: int, col: int):
        if 0 <= row < 10 and 0 <= col < 10:
            self.rows[row][col] += 1
            if self.rows[row][col] == 10:
                for r, c in DIRECTIONS:
                    self.energize(row + r, col + c)
    
    def reset(self) -> int:
        flashes = 0
        for row in range(0, 10):
            for col in range(0, 10):
                if self.rows[row][col] > 9:
                    self.rows[row][col] = 0
                    flashes += 1
        return flashes
