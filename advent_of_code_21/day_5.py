def part_1(file: str) -> int:
    lines = open(file, 'r').readlines()
    lines = [s.strip() for s in lines]

    coordinates = get_coordinates(lines)
    size = max(get_size(coordinates)) + 1

    vents = []
    for i in range(0, size):
        vents.append([0]*size)

    for pair in coordinates:
        start = pair[0]
        end = pair[1]

        #vertical lines
        if start[0] == end[0]:
            col = start[0]
            row = min(start[1], end[1])
            diff = abs(start[1]-end[1])
            for i in range(0, diff+1):
                vents[row+i][col] += 1
        
        #horizontal lines
        if start[1] == end[1]:
            col = min(start[0], end[0])
            row = start[1]
            diff = abs(start[0]-end[0])
            for i in range(0, diff+1):
                vents[row][col+i] += 1

    total = 0
    for row in vents:
        for num in row:
            if num > 1:
                total += 1

    return total

def get_size(coordinates: list) -> list:
    size = [0, 0]
    for pair in coordinates:
        for xy in pair:
            size[0] = max(size[0], xy[0])
            size[1] = max(size[1], xy[1])
    return size

def get_coordinates(lines: list) -> list:
    pairs = []
    for line in lines:
        pairs.append(line.split(' -> '))
    
    for pair in pairs:
        pair[0] = pair[0].split(',')
        pair[1] = pair[1].split(',')
    
    for pair in pairs:
        for xy in pair:
            xy[0] = int(xy[0])
            xy[1] = int(xy[1])
    
    return pairs

if __name__ == '__main__':
    assert part_1('day_5_test.txt') == 5
    assert part_1('day_5.txt') == 5608

    #assert part_2('day_5_test.txt') == 0
    #assert part_2('day_5.txt') == 0