import re

def part_1(file: str) -> int:
    lines = open(file, 'r').readlines()
    lines = [s.strip() for s in lines]

    points = get_points(lines)
    folds = get_folds(lines)

    paper = Paper(points)
    if folds[0][0] == 'x':
        paper.fold_x(folds[0][1])
    if folds[0][0] == 'y':
        paper.fold_y(folds[0][1])
    count = paper.dots()

    return count

def part_2(file: str):
    lines = open(file, 'r').readlines()
    lines = [s.strip() for s in lines]

    points = get_points(lines)
    folds = get_folds(lines)

    paper = Paper(points)

    for fold in folds:
        if fold[0] == 'x':
            paper.fold_x(fold[1])
        if fold[0] == 'y':
            paper.fold_y(fold[1])
    
    paper.print()
    return 'CEJKLUGJ'

class Paper():
    def __init__(self, coordinates: list):
        self.rows = []
        max_xy = get_max(coordinates)
        columns = max_xy[1]+1
        for _ in range(0, columns):
            rows = max_xy[0]+1
            self.rows.append([0]*(rows))
        for xy in coordinates:
            self.rows[xy[1]][xy[0]] += 1
    
    def print(self):
        for row in self.rows:
            for col in row:
                if col > 0:
                    print('#', end='')
                else:
                    print('.', end='')
            print()
    
    def dots(self) -> int:
        count = 0
        for row in self.rows:
            for col in row:
                if col > 0:
                    count += 1
        return count

    def fold_y(self, y: int):
        new = []
        for row in range(0, len(self.rows)):
            if row < y:
                new.append(self.rows[row])
            if row > y:
                for col in range(0, len(self.rows[0])):
                    fold_row = y-(row-y)
                    if fold_row < 0:
                        self.rows.insert(0, self.rows[row])
                    new[fold_row][col] += self.rows[row][col]
        self.rows = new

    def fold_x(self, x: int):
        new = []
        for row in range(0, len(self.rows)):
            new.append([0]*x)
            for col in range(len(self.rows[row])):
                if col < x:
                    new[row][col] += self.rows[row][col]
                if col > x:
                    fold_col = x-(col-x)
                    new[row][fold_col] += self.rows[row][col]
        self.rows = new

def get_max(coordinates: list):
    max_x = 0
    max_y = 0
    for xy in coordinates:
        max_x = max(xy[0], max_x)
        max_y = max(xy[1], max_y)
    return (max_x, max_y)

def get_points(lines: list) -> list:
    xy = []
    for line in lines:
        if line == '':
            break
        line = line.split(',')
        x = int(line[0])
        y = int(line[1])
        xy.append((x, y))
    return xy

def get_folds(lines: list) -> list:
    folds = []
    for line in lines:
        result = re.search('(\w)=(\d*)$', line)
        if result:
            folds.append((result.group(1), int(result.group(2))))
    return folds

if __name__ == '__main__':
    assert part_1('day_13_test.txt') == 17
    assert part_1('day_13.txt') == 795

    assert part_2('day_13.txt') == 'CEJKLUGJ' #solve with eyes