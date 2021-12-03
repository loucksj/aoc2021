def part_1(file: str) -> int:
    lines = open(file, 'r').readlines()
    gamma = ""
    epsilon = ""
    size = len(lines[0].strip('\n'))
    length = len(lines)
    for index in range(0, size):
        sum = 0
        for line in lines:
            line = line.strip('\n')
            digit = int(line[index])
            sum += int(digit)
        if sum > length/2:
            gamma += str(1)
            epsilon += str(0)
        else:
            gamma += str(0)
            epsilon += str(1)
    
    return int(gamma, 2) * int(epsilon, 2)

def to_num(binary: str) -> int:
    return int(binary, 2)

if __name__ == '__main__':
    assert part_1('day_3_test.txt') == 198
    assert part_1('day_3.txt') == 3242606