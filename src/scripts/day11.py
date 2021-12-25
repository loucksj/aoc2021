def part_1(file: str) -> int:
    lines = open(file, 'r').readlines()
    lines = [s.strip() for s in lines]

    board = Board(lines)

    flashes = 0
    for step in range(0, 100):
        for row in range(0, 10):
            for col in range(0, 10):
                board.energize(row, col)
        flashes += board.reset()
    
    return flashes

def part_2(file: str) -> int:
    lines = open(file, 'r').readlines()
    lines = [s.strip() for s in lines]

    board = Board(lines)

    step = 0
    while True:
        step += 1
        for row in range(0, 10):
            for col in range(0, 10):
                board.energize(row, col)
        if board.reset() == 100:
            return step

class Board:
    def __init__(self, data: list):
        self.rows = []
        for line in data:
            self.rows.append([int(x) for x in line])

    def energize(self, row: int, col: int):
        if 0 <= row < 10 and 0 <= col < 10:
            self.rows[row][col] += 1
            if self.rows[row][col] == 10:
                self.energize(row-1, col-1) #UL
                self.energize(row-1, col) #U
                self.energize(row-1, col+1) #UR
                self.energize(row, col-1) #L
                self.energize(row, col+1) #R
                self.energize(row+1, col-1) #DL
                self.energize(row+1, col) #D
                self.energize(row+1, col+1) #DR
    
    def reset(self) -> int:
        flashes = 0
        for row in range(0, 10):
            for col in range(0, 10):
                if self.rows[row][col] > 9:
                    self.rows[row][col] = 0
                    flashes += 1
        return flashes

if __name__ == '__main__':
    assert part_1('day_11_test.txt') == 1656
    assert part_1('day_11.txt') == 1617

    assert part_2('day_11_test.txt') == 195
    assert part_2('day_11.txt') == 258