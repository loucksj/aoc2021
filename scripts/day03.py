from scripts.input_manager import strip_lines


def part_one(filename: str) -> int:
    majority = majority_bits(strip_lines(filename))
    return int(majority, 2) * int(flip(majority), 2)


def part_two(filename: str) -> int:
    binaries = strip_lines(filename)
    return int(major_path(binaries), 2) * int(minor_path(binaries), 2)


def flip(binary: str) -> str:
    return ''.join(['1' if i == '0' else '0' for i in binary])


def majority_bits(binaries: list) -> str:
    return ''.join(majority_bit(binaries, i) for i in range(len(binaries[0])))


def majority_bit(binaries: list, i: int) -> str:
    return '1' if sum_index(binaries, i) >= len(binaries)/2 else '0'


def sum_index(values: list, i: int) -> int:
    return sum(int(value[i]) for value in values)


def major_path(binaries: list) -> str:
    i = 0
    while len(binaries) > 1:
        binaries = index_majorities(binaries, i)
        i += 1
    return binaries[0]


def minor_path(binaries: list) -> str:
    i = 0
    while len(binaries) > 1:
        binaries = index_minorities(binaries, i)
        i += 1
    return binaries[0]


def index_majorities(binaries: list, i: int) -> list:
    majority = majority_bit(binaries, i)
    return [binary for binary in binaries if binary[i] == majority]


def index_minorities(binaries: list, i: int) -> list:
    majority = majority_bit(binaries, i)
    return [binary for binary in binaries if binary[i] != majority]
