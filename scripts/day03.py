from scripts.main import Reader


def part_one(filename: str) -> int:
    bits = majority(Reader(filename).matrix())
    return as_int(bits) * as_int(flip(bits))


def part_two(filename: str) -> int:
    bitmatrix = Reader(filename).matrix()
    return as_int(average_bits(bitmatrix)) * as_int(average_bits(bitmatrix, opposite=True))


def as_int(bits: list) -> int:
    return int(''.join(bits), 2)


def flip(bits: list) -> list:
    return ['1' if digit == '0' else '0' for digit in bits]


def most(bits: list) -> str:
    return '1' if bits.count('1') >= bits.count('0') else '0'


def majority(bitmatrix: list) -> list:
    return [most(column) for column in transposed(bitmatrix)]


def transposed(bitmatrix: list) -> list:
    return [list(x) for x in zip(*bitmatrix)]


def average_bits(bitmatrix: list, opposite=False) -> list:
    filtered = bitmatrix.copy()
    i = 0
    while len(filtered) > 1:
        targets = majority(filtered) if not opposite else flip(
            majority(filtered))
        filtered = [bits for bits in filtered if bits[i] == targets[i]]
        i += 1
    return filtered[0]
