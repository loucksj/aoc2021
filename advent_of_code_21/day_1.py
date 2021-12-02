def part_1(file: str) -> int:
    lines = open(file, 'r').readlines()
    count = 0
    i = 0
    current = 0
    last = 0
    for line in lines:
        if i == 0:
            current = int(line)
        else:
            last = current
            current = int(line)
            if current > last:
                count += 1
        i += 1
    return count

def part_2(file: str, size: int) -> int:
    lines = open(file, 'r').readlines()
    count = 0
    index = 0
    current = 0
    previous = 0

    for line in lines:
        current += int(line)
        if index >= size:
            current -= int(lines[index-size])
            if current > previous:
                count += 1
        previous = current
        index += 1

    return count

if __name__ == '__main__':
    assert part_1('day_1_test.txt') == 7
    assert part_1('day_1.txt') == 1215

    assert part_2('day_1_test.txt', 1) == 7
    assert part_2('day_1.txt', 1) == 1215
    assert part_2('day_1_test.txt', 3) == 5
    assert part_2('day_1.txt', 3) == 1150