from scripts.main import Reader


def part_one(filename: str) -> int:
    vents = Vents(filename)
    vents.mark_vertical()
    vents.mark_horizontal()
    return vents.score()


def part_two(filename: str) -> int:
    vents = Vents(filename)
    vents.mark_vents()
    return vents.score()

class Vents:
    def __init__(self, filename: str):
        self.coordinates = self.coordinates_from_file(filename)
        self.rows = []
        maximums = self.get_max_xy()
        for _ in range(maximums[0]+1):
            self.rows.append([0]*(maximums[1]+1))
    
    def mark_vents(self):
        self.mark_vertical()
        self.mark_horizontal()
        self.mark_down_diagonal()
        self.mark_up_diagonal()

    def mark_vertical(self):
        for pair in self.coordinates:
            start = pair[0]
            end = pair[1]
            if start[0] == end[0]:
                col = start[0]
                row = min(start[1], end[1])
                diff = abs(start[1]-end[1])
                for i in range(0, diff+1):
                    self.rows[row+i][col] += 1

    def mark_horizontal(self):
        for pair in self.coordinates:
            start = pair[0]
            end = pair[1]
            if start[1] == end[1]:
                col = min(start[0], end[0])
                row = start[1]
                diff = abs(start[0]-end[0])
                for i in range(0, diff+1):
                    self.rows[row][col+i] += 1

    def mark_down_diagonal(self):
        for pair in self.coordinates:
            start = pair[0]
            end = pair[1]
            if start[0] - end[0] == start[1] - end[1]:
                col = min(start[0], end[0])
                row = min(start[1], end[1])
                diff = abs(start[0]-end[0])
                for i in range(0, diff+1):
                    self.rows[row+i][col+i] += 1

    def mark_up_diagonal(self):
        for pair in self.coordinates:
            start = pair[0]
            end = pair[1]
            if start[0] - end[0] == -(start[1] - end[1]):
                col = min(start[0], end[0])
                row = max(start[1], end[1])
                diff = abs(start[0]-end[0])
                for i in range(0, diff+1):
                    self.rows[row-i][col+i] += 1

    def score(self) -> int:
        return sum([sum([1 if num > 1 else 0 for num in row]) for row in self.rows])


    def get_max_xy(self) -> tuple:
        max_xy = [0, 0]
        for pair in self.coordinates:
            for x, y in pair:
                max_xy[0] = max(max_xy[0], x)
                max_xy[1] = max(max_xy[1], y)
        return (max_xy[0], max_xy[1])

    def coordinates_from_file(self, filename: str) -> list:
        return [[list(map(int, pair.split(','))) for pair in coordinate] for coordinate in Reader(filename).split_lines(' -> ')]
