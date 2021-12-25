from scripts.input_manager import strip_lines


def part_one(filename: str) -> int:
    majority = majority_bits(strip_lines(filename))
    return int(majority, 2) * int(flip(majority), 2)


def part_two(filename: str) -> int:
    binary = strip_lines(filename)
    major = binary_major(binary)
    minor = binary_minor(binary)
    return int(major, 2) * int(minor, 2)


def flip(binary: str):
    return ''.join(['1' if i == '0' else '0' for i in binary])


def majority_bits(binaries: list) -> list:
    return ''.join([majority_bit(binaries, i) for i in range(len(binaries[0]))])


def majority_bit(binaries: list, index: int) -> str:
    return '1' if index_sums(binaries)[index] >= len(binaries)/2 else '0'


def index_sums(values: list) -> list:
    sum_by_index = [0]*len(values[0])
    for value in values:
        for i in range(len(sum_by_index)):
            sum_by_index[i] += int(value[i])
    return sum_by_index


def binary_major(binaries: list) -> str:
    blist = binaries.copy()
    i = 0
    while len(blist) > 1:
        majority = majority_bit(blist, i)
        blist = [binary for binary in blist if binary[i] == majority]
        i += 1
    return blist[0]


def binary_minor(binaries: list) -> str:
    blist = binaries.copy()
    for i in range(len(binaries[0])):
        if len(blist) == 1:
            return blist[0]
        majority = majority_bit(blist, i)
        blist = [binary for binary in blist if binary[i] != majority]
