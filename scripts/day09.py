from scripts.main import Reader

# left, right, up, down
DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def part_one(filename: str) -> int:
    return IntMatrix(filename).risksum()


def part_two(filename: str) -> int:
    return IntMatrix(filename).basinproduct()


class IntMatrix():
    def __init__(self, filename) -> None:
        self.matrix = Reader(filename).integer_lines()

    def risksum(self):
        return sum(self.matrix[row][col] + 1 for row, col in self.lowpoints())

    def basinproduct(self) -> list:
        sizes = sorted(self.basin_sizes())
        return sizes[-1] * sizes[-2] * sizes[-3]

    def basin_sizes(self) -> list:
        return [self.basin_size(row, col) for row, col in self.lowpoints()]

    def lowpoints(self) -> list:
        # Inputs include no adjacent lowpoints.
        lows = []
        for row, _ in enumerate(self.matrix):
            for col, _ in enumerate(self.matrix[0]):
                if self.matrix[row][col] < min(self.neighbors(row, col)):
                    lows.append((row, col))
        return lows

    def neighbors(self, row: int, col: int) -> list:
        neighbors = [9, 9, 9, 9]  # left, right, up, down
        for i, direction in enumerate(DIRECTIONS):
            neighbor_row = row + direction[0]
            neighbor_col = col + direction[1]
            if 0 <= neighbor_row < len(self.matrix) and 0 <= neighbor_col < len(self.matrix[0]):
                neighbors[i] = self.matrix[neighbor_row][neighbor_col]
        return neighbors

    def basin_size(self, row: int, col: int, matrix=[]) -> int:
        if matrix == []:
            matrix = self.matrix.copy()
        count = 1
        matrix[row][col] = 0
        if 0 < self.neighbors(row, col)[0] < 9:
            count += self.basin_size(row, col - 1, matrix)
        if 0 < self.neighbors(row, col)[1] < 9:
            count += self.basin_size(row, col + 1, matrix)
        if 0 < self.neighbors(row, col)[2] < 9:
            count += self.basin_size(row - 1, col, matrix)
        if 0 < self.neighbors(row, col)[3] < 9:
            count += self.basin_size(row + 1, col, matrix)
        return count
