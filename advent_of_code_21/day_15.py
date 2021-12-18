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
    row = 0
    col = 0
    distance[row][col] = 0
    end_row = len(rows) - 1
    end_col = width - 1
    
    run = True
    while run:
        if row == end_row and col == end_col:
            return distance[end_row][end_col]
        update_neighbors(rows, distance, row, col)
        distance[row][col] = 0
        goto = get_next(distance, row, col)
        row = goto[0]
        col = goto[1]
    return 0

def get_next(distance: list, row: int, col: int) -> list:
    point = [0, 0]
    smallest = 0
    for row in range(0 , len(distance)):
        for col in range(0, len(distance[0])):
            d = distance[row][col]
            if d > 0 and (smallest == 0 or d < smallest):
                point = [row, col]
                smallest = distance[point[0]][point[1]]
    return point

def update_neighbors(rows: list, distance: list, row: int, col: int):
    update(rows, distance, row, col, row-1, col) #up
    update(rows, distance, row, col, row+1, col) #down
    update(rows, distance, row, col, row, col-1) #left
    update(rows, distance, row, col, row, col+1) #right

def update(rows: list, distance: list, row_start: int, col_start: int, row_end: int, col_end: int):
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