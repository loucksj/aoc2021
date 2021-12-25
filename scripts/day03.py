from scripts.main import Reader, Tools


def part_one(filename: str) -> int:
    bitmatrix = Reader(filename).matrix()
    return common_value(bitmatrix) * rare_value(bitmatrix)


def part_two(filename: str) -> int:
    digits = Reader(filename).matrix()
    return to_int(major_path(digits)) * to_int(minor_path(digits))


def to_int(bits: list):
    return int(''.join(bits), 2)


def flip_digits(bits: list) -> str:
    return ['1' if digit == '0' else '0' for digit in bits]


def common_value(bitmatrix: list) -> int:
    return to_int(common_bits(bitmatrix))


def rare_value(bitmatrix: list) -> int:
    return to_int(rare_bits(bitmatrix))


def common_bits(bitmatrix: list) -> list:
    return [common_element(column) for column in Tools.transpose(bitmatrix)]


def rare_bits(bitmatrix: list) -> list:
    return flip_digits(common_bits(bitmatrix))


def common_element(bits: list) -> str:
    # spec: ties in favor of '1'
    return '1' if bits.count('1') >= bits.count('0') else '0'


def major_path(bitmatrix: list) -> str:
    i = 0
    while len(bitmatrix) > 1:
        bitmatrix = majority_elements(bitmatrix, i)
        i += 1
    return bitmatrix[0]


def minor_path(bitmatrix) -> str:
    i = 0
    while len(bitmatrix) > 1:
        bitmatrix = minority_elements(bitmatrix, i)
        i += 1
    return bitmatrix[0]


def majority_elements(bitmatrix: list, i: int) -> list:
    return [bits for bits in bitmatrix if bits[i] == common_bits(bitmatrix)[i]]


def minority_elements(bitmatrix, i: int) -> list:
    return [bits for bits in bitmatrix if bits[i] != common_bits(bitmatrix)[i]]
