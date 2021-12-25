from scripts.get_input import strip_lines


def part_one(filename: str) -> int:
    lines = strip_lines(filename)
    gamma = ""
    epsilon = ""
    places = len(lines[0])
    for index in range(0, places):
        sum = 0
        for line in lines:
            line = line
            digit = int(line[index])
            sum += digit
        if sum > len(lines)/2:
            gamma += str(1)
            epsilon += str(0)
        else:
            gamma += str(0)
            epsilon += str(1)

    return int(gamma, 2) * int(epsilon, 2)


def part_two(filename: str) -> int:
    lines = strip_lines(filename)
    lines_copy = lines

    generator = find_line(lines, False)
    scrubber = find_line(lines_copy, True)

    return int(generator, 2) * int(scrubber, 2)


def find_line(lines: list, scrubber: bool) -> str:
    index = 0
    while len(lines) > 1:
        common = most_common(lines, index)
        if scrubber:
            if common == '1':
                common = '0'
            else:
                common = '1'
        lines = trim_lines(lines, index, common)
        index += 1
    return lines[0]


def trim_lines(lines: list, index: int, target: str) -> list:
    new_lines = []
    for line in lines:
        if line[index] == target:
            new_lines.append(line)
    return new_lines


def most_common(lines: list, index: int) -> str:
    sum = 0
    for line in lines:
        sum += int(line[index])
    if sum >= len(lines)/2:
        # ties go to '1'
        return '1'
    return '0'
