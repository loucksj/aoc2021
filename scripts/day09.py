from scripts.main import Reader


def part_one(filename: str) -> int:
    return IntMatrix(filename).risksum()


def part_two(filename: str) -> int:
    return IntMatrix(filename).basinproduct()


class IntMatrix():
    def __init__(self, filename) -> None:
        self.matrix = Reader(filename).integer_lines()

    def risksum(self):
        return sum(self.matrix[row][col] + 1 for row, col in self.lowpoints())

    def lowpoints(self) -> list:
        # There are no adjacent lowpoints in the inputs.
        lows = []
        for row, _ in enumerate(self.matrix):
            for col, _ in enumerate(self.matrix[0]):
                if self.matrix[row][col] < min(self.neighbors(row, col)):
                    lows.append((row, col))
        return lows

    def neighbors(self, row: int, col: int) -> list:
        neighbors = []
        if col > 0:
            neighbors.append(self.matrix[row][col - 1])
        if col < len(self.matrix[0]) - 1:
            neighbors.append(self.matrix[row][col + 1])
        if row > 0:
            neighbors.append(self.matrix[row - 1][col])
        if row < len(self.matrix) - 1:
            neighbors.append(self.matrix[row + 1][col])
        return neighbors

    def basinproduct(self) -> list:
        sizes = sorted(self.basin_sizes())
        return sizes[-1] * sizes[-2] * sizes[-3]

    def basin_sizes(self) -> list:
        return [self.basin_size(row, col) for row, col in self.lowpoints()]

    def basin_size(self, row: int, col: int) -> int:
        count = 1
        matrix = self.matrix.copy()
        matrix[row][col] = 0
        if col > 0:
            left = matrix[row][col-1]
            if left > 0 and left < 9:
                count += self.basin_size(row, col-1)
        if col < len(matrix[0])-1:
            right = matrix[row][col+1]
            if right > 0 and right < 9:
                count += self.basin_size(row, col+1)
        if row > 0:
            up = matrix[row-1][col]
            if up > 0 and up < 9:
                count += self.basin_size(row-1, col)
        if row < len(matrix)-1:
            down = matrix[row+1][col]
            if down > 0 and down < 9:
                count += self.basin_size(row+1, col)
        return count
