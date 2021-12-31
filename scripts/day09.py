from scripts.main import Reader


def part_one(filename: str) -> int:
    lines = Reader(filename).integer_lines()
    total = 0
    for row, col in lowpoints(lines):
        total += 1 + lines[row][col]
    return total


def part_two(filename: str) -> int:
    lines = Reader(filename).integer_lines()
    lows = lowpoints(lines)
    sizes = []
    for row, col in lows:
        sizes.append(size(lines, row, col))
    sizes = sorted(sizes)
    return sizes[-1] * sizes[-2] * sizes[-3]


def size(cells: list, row: int, col: int) -> int:
    count = 1
    cells[row][col] = 0
    if col > 0:
        left = cells[row][col-1]
        if left > 0 and left < 9:
            count += size(cells, row, col-1)
    if col < len(cells[0])-1:
        right = cells[row][col+1]
        if right > 0 and right < 9:
            count += size(cells, row, col+1)
    if row > 0:
        up = cells[row-1][col]
        if up > 0 and up < 9:
            count += size(cells, row-1, col)
    if row < len(cells)-1:
        down = cells[row+1][col]
        if down > 0 and down < 9:
            count += size(cells, row+1, col)
    return count


def lowpoints(matrix: list):
    width = len(matrix[0])
    height = len(matrix)
    lows = []
    for row in range(0, height):
        for col in range(0, width):
            point = matrix[row][col]
            if col > 0 and matrix[row][col-1] <= point:
                continue  # left
            if col < width-1 and matrix[row][col+1] <= point:
                continue  # right
            if row > 0 and matrix[row-1][col] <= point:
                continue  # up
            if row < height-1 and matrix[row+1][col] <= point:
                continue  # down
            lows.append((row, col))
    return lows
