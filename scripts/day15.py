from scripts.main import Reader


def part_one(filename: str) -> int:
    return Map(filename).lowest_path()


def part_two(filename: str) -> int:
    return Map(filename).expand().lowest_path()


class Map():
    def __init__(self, filename: str):
        self.point = [0, 0]
        self.matrix = Reader(filename).integer_lines()
        self.distances = [[-1 for _ in row] for row in self.matrix]
        self.current = [[0, 0]]

    def lowest_path(self):
        self.distances[0][0] = 0  # start
        endpoint = [len(self.matrix) - 1, len(self.matrix[0]) - 1]
        while True:
            self.current.remove([self.point[0], self.point[1]])
            self.update()
            self.move()
            if self.point == endpoint:
                return self.distances[-1][-1]

    # Add unexplored neighbors to current
    # Update neighbor's distance
    def update(self):
        directions = [[-1, 0], [+1, 0],  # up, down
                      [0, -1], [0, +1]]  # left, right
        for d_row, d_col in directions:
            row, col = self.point[0] + d_row, self.point[1] + d_col
            if row < 0 or row >= len(self.matrix) or col < 0 or col >= len(self.matrix[0]):
                continue  # edge
            risk = self.distances[row][col]
            if risk == 0:
                continue  # visited
            distance = self.matrix[row][col] + \
                self.distances[self.point[0]][self.point[1]]
            if risk == -1 or distance < risk:
                if risk == -1:
                    self.current.append([row, col])
                self.distances[row][col] = distance

    def move(self) -> list:
        self.distances[self.point[0]][self.point[1]] = 0
        smallest = 0
        for point in self.current:
            d = self.distances[point[0]][point[1]]
            if d > 0 and (smallest == 0 or d < smallest):
                self.point = [point[0], point[1]]
                smallest = self.distances[self.point[0]][self.point[1]]

    def expand(self):
        width, height = len(self.matrix), len(self.matrix[0])
        new_height, new_width = len(self.matrix) * 5, len(self.matrix[0]) * 5
        new_map = [[0 for _ in range(new_width)] for _ in range(new_height)]
        for row in range(new_height):
            for col in range(new_width):
                r = row % height
                c = col % width
                bonus = int(row/height) + int(col/width)
                new_map[row][col] = self.matrix[r][c] + bonus
                while new_map[row][col] > 9:
                    new_map[row][col] -= 9
        self.matrix = new_map
        self.distances = [[-1 for _ in row] for row in self.matrix]
        return self
