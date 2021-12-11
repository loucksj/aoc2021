def part_1(file: str) -> int:
    lines = open(file, 'r').readlines()
    lines = [s.strip() for s in lines]

    width = len(lines[0])
    height = len(lines)

    total = 0
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
            total += 1 + point
    return total

if __name__ == '__main__':
    assert part_1('day_9_test.txt') == 15
    assert part_1('day_9.txt') == 522

    #assert part_2('day_9_test.txt') == 1134
    #assert part_2('day_9.txt') == 0