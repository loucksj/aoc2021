def part_1(file: str) -> int:
    lines = open(file, 'r').readlines()
    lines = [s.strip() for s in lines]

    map = Map(lines)
    risk = map.find_path()

    return risk

class Map():
    def __init__(self, lines: list):
        self.point = [0, 0]
        self.rows = []
        self.open = [[0, 0]]
        for i in range(0, len(lines)):
            self.rows.append([])
            for char in lines[i]:
                self.rows[i].append([int(char), -1])

    def find_path(self):
        height = len(self.rows)
        width = len(self.rows[0])
        self.rows[0][0][1] = 0
        while True:
            self.open.remove([self.point[0], self.point[1]])
            self.update()
            self.move()
            if self.point[0] == height-1 and self.point[1] == width-1:
                return self.rows[height-1][width-1][1]

    def move(self) -> list:
        self.rows[self.point[0]][self.point[1]][1] = 0
        smallest = 0
        for point in self.open:
            d = self.rows[point[0]][point[1]][1]
            if d > 0 and (smallest == 0 or d < smallest):
                self.point = [point[0], point[1]]
                smallest = self.rows[self.point[0]][self.point[1]][1]

    def update(self):
        directions = [[-1, 0], [+1, 0], [0, -1], [0, +1]] #up, down, left, right
        for direction in directions:
            row = self.point[0]+direction[0]
            col = self.point[1]+direction[1]
            if row < 0 or row >= len(self.rows) or col < 0 or col >= len(self.rows[0]):
                continue #edge
            risk = self.rows[row][col][1]
            if risk == 0:
                continue #visited
            distance = self.rows[row][col][0] + self.rows[self.point[0]][self.point[1]][1]
            if risk == -1 or distance < risk:
                if risk == -1:
                    self.open.append([row, col])
                self.rows[row][col][1] = distance

if __name__ == '__main__':
    assert part_1('day_15_test.txt') == 40
    assert part_1('day_15.txt') == 456

    #assert part_2('day_15_test.txt') == 315
    #assert part_2('day_15.txt') == 0