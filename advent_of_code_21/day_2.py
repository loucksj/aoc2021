def part_1(file: str) -> list[int]:
    lines = open(file, 'r').readlines()
    horizontal = 0
    depth = 0
    for line in lines:
        line = line.split()
        direction = line[0]
        amount = int(line[1])
        if direction == "forward":
            horizontal += amount
        if direction == "down":
            depth += amount
        if direction == "up":
            depth -= amount
    return horizontal * depth

if __name__ == '__main__':
    assert part_1('day_2_test.txt') == 150
    assert part_1('day_2.txt') == 1480518