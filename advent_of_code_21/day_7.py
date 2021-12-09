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

def part_2(file: str) -> int:
    lines = open(file, 'r').readlines()
    lines = [s.strip() for s in lines]

    positions = list(map(int, lines[0].split(',')))
    size = max(positions)+1
    
    crabs = [[0]*size]
    for _ in range(1, size):
        crabs.append([0]*size)
    for p in positions:
        crabs[0][p] += 1

    fuel = 0
    start = 0
    end = len(crabs[0])-1
    while start != end:
        startsum = 0
        endsum = 0
        i = 1
        for line in crabs:
            startsum += line[start]*i
            endsum += line[end]*i
            i += 1

        if startsum == 0:
            start += 1
            continue
        if endsum == 0:
            end -= 1
            continue
        
        if startsum <= endsum:
            fuel += startsum
            for i in range(0, len(crabs)-1):
                crabs[i+1][start+1] += crabs[i][start]
                crabs[i][start] = 0
        else:
            fuel += endsum
            for i in range(0, len(crabs)-1):
                crabs[i+1][end-1] += crabs[i][end]
                crabs[i][end] = 0

    return fuel

if __name__ == '__main__':
    assert part_1('day_7_test.txt') == 37
    assert part_1('day_7.txt') == 355989

    assert part_2('day_7_test.txt') == 168
    assert part_2('day_7.txt') == 102245489