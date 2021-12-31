from scripts.main import Reader


def part_one(filename: str) -> int:
    intmatrix = IntMatrix(filename)
    return sum(1 + intmatrix.matrix[row][col] for row, col in intmatrix.lowpoints())


def part_two(filename: str) -> int:
    intmatrix = IntMatrix(filename)
    lows = intmatrix.lowpoints()
    sizes = []
    for row, col in lows:
        sizes.append(intmatrix.size(row, col))
    sizes = sorted(sizes)
    return sizes[-1] * sizes[-2] * sizes[-3]


class IntMatrix():
    def __init__(self, filename) -> None:
        self.matrix = Reader(filename).integer_lines()

    def lowpoints(self):
        width = len(self.matrix[0])
        height = len(self.matrix)
        lows = []
        for row in range(height):
            for col in range(width):
                point = self.matrix[row][col]
                if col > 0 and self.matrix[row][col-1] <= point:
                    continue  # left
                if col < width-1 and self.matrix[row][col+1] <= point:
                    continue  # right
                if row > 0 and self.matrix[row-1][col] <= point:
                    continue  # up
                if row < height-1 and self.matrix[row+1][col] <= point:
                    continue  # down
                lows.append((row, col))
        return lows


    def size(self, row: int, col: int) -> int:
        count = 1
        self.matrix[row][col] = 0
        if col > 0:
            left = self.matrix[row][col-1]
            if left > 0 and left < 9:
                count += self.size(row, col-1)
        if col < len(self.matrix[0])-1:
            right = self.matrix[row][col+1]
            if right > 0 and right < 9:
                count += self.size(row, col+1)
        if row > 0:
            up = self.matrix[row-1][col]
            if up > 0 and up < 9:
                count += self.size(row-1, col)
        if row < len(self.matrix)-1:
            down = self.matrix[row+1][col]
            if down > 0 and down < 9:
                count += self.size(row+1, col)
        return count
