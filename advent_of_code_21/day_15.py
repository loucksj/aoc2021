def part_1(file: str) -> int:
    lines = open(file, 'r').readlines()
    lines = [s.strip() for s in lines]

    rows = get_rows(lines)
    risk = find_path(rows)

    return risk

def find_path(rows: list):
    distance = []
    width = len(rows[0])
    for row in rows:
        distance.append([-1]*width)
    
    point = [0, 0]
    end_point = [len(rows)-1, width-1]
    distance[point[0]][point[1]] = 0

    while True:
        if point == end_point:
            return distance[end_point[0]][end_point[1]]
        update_neighbors(rows, distance, point)
        distance[point[0]][point[1]] = 0
        next_point = get_next(distance)
        point = [next_point[0], next_point[1]]

def get_next(distance: list) -> list:
    point = [0, 0]
    smallest = 0
    for row in range(0 , len(distance)):
        for col in range(0, len(distance[0])):
            d = distance[row][col]
            if d > 0 and (smallest == 0 or d < smallest):
                point = [row, col]
                smallest = distance[point[0]][point[1]]
    return point

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

def get_rows(lines) -> list:
    rows = []
    for line in lines:
        row = []
        for char in line:
            row.append(int(char))
        rows.append(row)
    return rows

if __name__ == '__main__':
    assert part_1('day_15_test.txt') == 40
    assert part_1('day_15.txt') == 456

    #assert part_2('day_15_test.txt') == 315
    #assert part_2('day_15.txt') == 0