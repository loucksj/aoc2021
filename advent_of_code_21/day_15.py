def part_1(file: str) -> int:
    lines = open(file, 'r').readlines()
    lines = [s.strip() for s in lines]

    map = Map(lines)
    risk = map.find_path()

    return risk

class Map():
    def __init__(self, lines: list):
        self.point = [0, 0] #start
        self.rows = []
        self.distance = []
        for line in lines:
            row = []
            for char in line:
                row.append(int(char))
            self.rows.append(row)
            self.distance.append([-1]*len(self.rows[0]))

    def find_path(self):
        end_point = [len(self.rows)-1, len(self.rows[0])-1]
        self.distance[self.point[0]][self.point[1]] = 0
        while True:
            if self.point == end_point:
                return self.distance[end_point[0]][end_point[1]]
            update_neighbors(self.rows, self.distance, self.point)
            self.distance[self.point[0]][self.point[1]] = 0
            self.get_next()

    def get_next(self) -> list:
        smallest = 0
        for row in range(0 , len(self.distance)):
            for col in range(0, len(self.distance[0])):
                d = self.distance[row][col]
                if d > 0 and (smallest == 0 or d < smallest):
                    self.point = [row, col]
                    smallest = self.distance[self.point[0]][self.point[1]]

def update_neighbors(rows: list, distance: list, point: list):
    update(rows, distance, point, [point[0]-1, point[1]]) #up
    update(rows, distance, point, [point[0]+1, point[1]]) #down
    update(rows, distance, point, [point[0], point[1]-1]) #left
    update(rows, distance, point, [point[0], point[1]+1]) #right

def update(rows: list, distance: list, point_start: list, point_end: list):
    row_start, col_start = point_start[0], point_start[1]
    row_end, col_end = point_end[0], point_end[1]
    
    if row_end < 0 or row_end >= len(rows) or col_end < 0 or col_end >= len(rows[0]):
        return #off the edge
    if distance[row_end][col_end] == 0:
        return #visited
    
    d_start = distance[row_start][col_start]
    d_end = distance[row_end][col_end]
    end = rows[row_end][col_end]
    end_try = d_start + end
    if d_end == -1 or end_try < d_end:
        distance[row_end][col_end] = end_try

if __name__ == '__main__':
    assert part_1('day_15_test.txt') == 40
    assert part_1('day_15.txt') == 456

    #assert part_2('day_15_test.txt') == 315
    #assert part_2('day_15.txt') == 0