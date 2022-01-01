from scripts.main import Reader
import re


def part_one(filename: str) -> int:
    return Paper(filename).fold_once().dot_count()


def part_two(filename: str):
    return Paper(filename).fold_all().printstring()


class Paper():
    def __init__(self, filename: str):
        self.folds = get_folds(filename)
        self.rows = []
        self.points = get_points(filename)
        row, col = self.get_max_xy()
        columns = col + 1
        for _ in range(columns):
            rows = row + 1
            self.rows.append([0]*(rows))
        for x, y in self.points:
            self.rows[y][x] += 1

    def fold_once(self):
        if self.folds[0][0] == 'x':
            self.fold_x(self.folds[0][1])
        if self.folds[0][0] == 'y':
            self.fold_y(self.folds[0][1])
        return self

    def fold_all(self):
        for fold in self.folds:
            if fold[0] == 'x':
                self.fold_x(fold[1])
            if fold[0] == 'y':
                self.fold_y(fold[1])
        return self

    def printstring(self):
        string = ''
        for row in self.rows:
            for col in row:
                if col > 0:
                    string += '#'
                else:
                    string += '.'
            string += '\n'
        return string

    def dot_count(self) -> int:
        count = 0
        for row in self.rows:
            for col in row:
                if col > 0:
                    count += 1
        return count

    def fold_y(self, y: int):
        new = []
        for row in range(len(self.rows)):
            if row < y:
                new.append(self.rows[row])
            if row > y:
                for col in range(len(self.rows[0])):
                    fold_row = y-(row-y)
                    if fold_row < 0:
                        self.rows.insert(0, self.rows[row])
                    new[fold_row][col] += self.rows[row][col]
        self.rows = new

    def fold_x(self, x: int):
        new = []
        for row in range(len(self.rows)):
            new.append([0]*x)
            for col in range(len(self.rows[row])):
                if col < x:
                    new[row][col] += self.rows[row][col]
                if col > x:
                    fold_col = x-(col-x)
                    new[row][fold_col] += self.rows[row][col]
        self.rows = new

    def get_max_xy(self):
        max_x = 0
        max_y = 0
        for x, y in self.points:
            max_x = max(x, max_x)
            max_y = max(y, max_y)
        return (max_x, max_y)


def get_points(filename: list) -> list:
    lines = Reader(filename).halves()[0].split('\n')
    xy = []
    for line in lines:
        x, y = line.split(',')
        xy.append((int(x), int(y)))
    return xy


def get_folds(filename: str) -> list:
    lines = Reader(filename).lines()
    folds = []
    for line in lines:
        result = re.search('(\w)=(\d*)$', line)
        if result:
            folds.append((result.group(1), int(result.group(2))))
    return folds
