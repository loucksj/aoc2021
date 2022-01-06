from src.main import Reader

# left, right, up, down
ORTHOGONALS = [(0, -1), (0, 1), (-1, 0), (1, 0)]


def part_one(filename: str) -> int:
    return IntMatrix(filename).risksum()


def part_two(filename: str) -> int:
    return IntMatrix(filename).basinproduct()


class IntMatrix:
    def __init__(self, filename) -> None:
        self.matrix = Reader(filename).integer_lines()

    def risksum(self):
        return sum(1 + val for val in self.lowpoint_values())

    def basinproduct(self) -> int:
        sizes = sorted(self.basin_sizes())
        return sizes[-1] * sizes[-2] * sizes[-3]

    def basin_sizes(self) -> list:
        return [self.basin_size(row, col) for row, col in self.lowpoints()]

    def lowpoint_values(self) -> list:
        return [self.matrix[row][col] for row, col in self.lowpoints()]

    # Inputs include no adjacent lowpoints.
    def lowpoints(self) -> list:
        lows = []
        for row, _ in enumerate(self.matrix):
            for col, _ in enumerate(self.matrix[0]):
                if self.matrix[row][col] < min(self.neighbor_values(row, col)):
                    lows.append((row, col))
        return lows

    def basin_size(self, row: int, col: int, matrix=None) -> int:
        if not matrix:
            matrix = self.matrix.copy()
        count = 1
        matrix[row][col] = 0
        for i, (dr, dc) in enumerate(ORTHOGONALS):
            if 0 < self.neighbor_values(row, col)[i] < 9:
                count += self.basin_size(row + dr, col + dc, matrix)
        return count

    def neighbor_values(self, row: int, col: int) -> list:
        values = []
        for delta in ORTHOGONALS:
            if self.is_neighbor(row, col, delta):
                values.append(self.matrix[row + delta[0]][col + delta[1]])
            else:
                values.append(9)
        return values

    def is_neighbor(self, row: int, col: int, delta: tuple) -> bool:
        if 0 <= row + delta[0] < len(self.matrix) \
                and 0 <= col + delta[1] < len(self.matrix[0]):
            return True
        return False
