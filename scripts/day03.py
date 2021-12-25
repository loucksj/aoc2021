from scripts.input_manager import char_lines


def part_one(filename: str) -> int:
    digits = majority_binary(char_lines(filename))
    return binary_digits_int(digits) * binary_digits_int(flip_digits(digits))


def part_two(filename: str) -> int:
    digits = char_lines(filename)
    return binary_digits_int(major_path(digits)) * binary_digits_int(minor_path(digits))


def binary_digits_int(digits: list):
    return int(''.join(digits), 2)


def majority_binary(binaries: list):
    return [commonest_element(column) for column in transpose(binaries)]


def commonest_element(binary: list) -> str:
    # spec: ties in favor of '1'
    return '1' if binary.count('1') >= binary.count('0') else '0'


def transpose(binaries: list):
    return [list(x) for x in zip(*binaries)]


def major_path(binaries: list) -> str:
    i = 0
    while len(binaries) > 1:
        binaries = majority_elements(binaries, i)
        i += 1
    return binaries[0]


def minor_path(binaries) -> str:
    i = 0
    while len(binaries) > 1:
        binaries = minority_elements(binaries, i)
        i += 1
    return binaries[0]


def majority_elements(binaries: list, i: int) -> list:
    return [binary for binary in binaries if binary[i] == majority_binary(binaries)[i]]


def minority_elements(binaries, i: int) -> list:
    return [binary for binary in binaries if binary[i] != majority_binary(binaries)[i]]


def flip_digits(binary: list) -> str:
    return ['1' if digit == '0' else '0' for digit in binary]
