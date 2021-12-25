from scripts.input_manager import strip_lines


def part_one(filename: str) -> int:
    mb = majority_bits(strip_lines(filename))
    return int(mb, 2) * int(flip(mb), 2)


def part_two(filename: str) -> int:
    lines = strip_lines(filename)
    lines_copy = lines

    generator = find_line(lines, False)
    scrubber = find_line(lines_copy, True)

    return int(generator, 2) * int(scrubber, 2)

def flip(binary: str):
    return ''.join(['1' if i == '0' else '0' for i in binary])

def majority_bits(binaries: list) -> list:
    majority_bits = ''
    bit_sums = index_sums(binaries)
    for i in range(len(binaries[0])):
        if bit_sums[i] >= len(binaries)/2:
            majority_bits += '1'
        else:
            majority_bits += '0'
    return majority_bits

def index_sums(values: list) -> list:
    sum_by_index = [0]*len(values[0])
    for value in values:
        for i in range(len(sum_by_index)):
            sum_by_index[i] += int(value[i])
    return sum_by_index

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
        return '1' #spec: ties favor '1'
    return '0'