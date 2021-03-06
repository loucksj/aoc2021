from src.main import Reader, transpose


def part_one(filename: str) -> int:
    return Paper(filename).fold_first().dot_count()


def part_two(filename: str):
    return Paper(filename).fold_all().printstring()


class Paper:
    def __init__(self, filename: str):
        self.folds = get_folds(filename)
        self.points = get_points(filename)
        self.matrix = self.make_rows()

    def fold_first(self):
        self.do_fold(self.folds[0])
        return self

    def fold_all(self):
        for fold in self.folds:
            self.do_fold(fold)
        return self

    def do_fold(self, fold: tuple):
        way, at = fold
        self.matrix = fold_x(self.matrix, at) if way == 'x' \
            else fold_y(self.matrix, at)

    def make_rows(self) -> list:
        rows = []
        rowmax, colmax = self.get_max_xy()
        columns = colmax + 1
        for _ in range(columns):
            rows.append([0] * (rowmax + 1))
        for x, y in self.points:
            rows[y][x] += 1
        return rows

    def get_max_xy(self):
        max_x = 0
        max_y = 0
        for x, y in self.points:
            max_x = max(x, max_x)
            max_y = max(y, max_y)
        return max_x, max_y

    def dot_count(self) -> int:
        return sum(sum(1 for val in row if val > 0) for row in self.matrix)

    def printstring(self):
        string = ''
        for row in self.matrix:
            for col in row:
                string += '#' if col > 0 else '.'
            string += '\n'
        return string


def fold_x(matrix: list, at_x: int) -> list:
    return transpose(fold_y(transpose(matrix), at_x))


def fold_y(matrix: list, at_y: int) -> list:
    matrix = matrix.copy()
    new = []
    for row in range(len(matrix)):
        if row < at_y:
            new.append(matrix[row])
        if row > at_y:
            for col in range(len(matrix[0])):
                fold_row = at_y - (row - at_y)
                if fold_row < 0:
                    matrix.insert(0, matrix[row])
                new[fold_row][col] += matrix[row][col]
    return new


def get_points(filename: str) -> list:
    lines = Reader(filename).halves_lined()[0]
    points = []
    for line in lines:
        x, y = line.split(',')
        points.append((int(x), int(y)))
    return points


def get_folds(filename: str) -> list:
    lines = Reader(filename).halves_lined()[1]
    folds = []
    for line in lines:
        left, right = line.split('=')
        folds.append((left[-1], int(right)))
    return folds
