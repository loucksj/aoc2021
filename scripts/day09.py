from scripts.main import Reader

def part_one(filename: str) -> int:
    lines = Reader(filename).lines

    total = 0
    for low in get_lows(lines):
        total += 1 + int(lines[low[0]][low[1]])
    return total

def part_two(filename: str) -> int:
    lines = Reader(filename).lines

    lows = get_lows(lines)

    cells = []
    for line in lines:
        cells.append([int(x) for x in line])

    sizes = []
    for low in lows:
        sizes.append(get_size(cells, low[0], low[1]))

    sizes = sorted(sizes)

    return sizes[-1] * sizes[-2] * sizes[-3]

def get_size(cells: list, row: int, col: int) -> int:
    count = 1
    cells[row][col] = 0

    if col > 0:
        left = cells[row][col-1]
        if left > 0 and left < 9:
            count += get_size(cells, row, col-1)
    if col < len(cells[0])-1:
        right = cells[row][col+1]
        if right > 0 and right < 9:
            count += get_size(cells, row, col+1)
    if row > 0:
        up = cells[row-1][col]
        if up > 0 and up < 9:
            count += get_size(cells, row-1, col)
    if row < len(cells)-1:
        down = cells[row+1][col]
        if down > 0 and down < 9:
            count += get_size(cells, row+1, col)
    
    return count

def get_lows(lines):
    width = len(lines[0])
    height = len(lines)
    lows = []
    for row in range(0, height):
        for col in range(0, width):
            point = int(lines[row][col])
            if col > 0 and int(lines[row][col-1]) <= point:
                continue #left
            if col < width-1 and int(lines[row][col+1]) <= point:
                continue #right
            if row > 0 and int(lines[row-1][col]) <= point:
                continue #up
            if row < height-1 and int(lines[row+1][col]) <= point:
                continue #down
            lows.append((row, col))
    return lows