def part_1(file: str) -> int:
    lines = open(file, 'r').readlines()
    lines = [s.strip() for s in lines]

    positions = list(map(int, lines[0].split(',')))

    crabs = [0]*(max(positions)+1)
    for p in positions:
        crabs[p] += 1

    fuel = 0
    start = 0
    end = len(crabs)-1
    while start != end:
        if crabs[start] == 0:
            start += 1
            continue
        if crabs[end] == 0:
            end -= 1
            continue
        if crabs[start] <= crabs[end]:
            fuel += crabs[start]
            crabs[start+1] += crabs[start]
            crabs[start] = 0
        else:
            fuel += crabs[end]
            crabs[end-1] += crabs[end]
            crabs[end] = 0

    return fuel

if __name__ == '__main__':
    assert part_1('day_7_test.txt') == 37
    assert part_1('day_7.txt') == 355989

    #assert part_2('day_7_test.txt') == 0
    #assert part_2('day_7.txt') == 0