def part_1(file: str) -> int:
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

def part_2(file: str) -> int:
    lines = open(file, 'r').readlines()
    horizontal = 0
    depth = 0
    aim = 0
    for line in lines:
        line = line.split()
        direction = line[0]
        amount = int(line[1])
        if direction == "forward":
            horizontal += amount
            depth += amount * aim
        if direction == "down":
            aim += amount
        if direction == "up":
            aim -= amount
    return horizontal * depth

if __name__ == '__main__':
    assert part_1('day_2_test.txt') == 150
    assert part_1('day_2.txt') == 1480518

    assert part_2('day_2_test.txt') == 900
    assert part_2('day_2.txt') == 1282809906