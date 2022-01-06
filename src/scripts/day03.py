from src.scripts.main import Reader, transpose


def part_one(filename: str) -> int:
    bits = average_columns(Reader(filename).matrix())
    return as_int(bits) * as_int(flip(bits))


def part_two(filename: str) -> int:
    bitmatrix = Reader(filename).matrix()
    return as_int(average_seive(bitmatrix)) * as_int(average_seive(bitmatrix, invert=True))


def as_int(bits: list) -> int:
    return int(''.join(bits), 2)


def flip(bits: list) -> list:
    return ['1' if digit == '0' else '0' for digit in bits]


def average_seive(bitmatrix: list, invert=False) -> list:
    matrix = bitmatrix.copy()
    i = 0
    while len(matrix) > 1:
        average_bits = average_columns(matrix) if not invert else flip(
            average_columns(matrix))
        matrix = [bits for bits in matrix if bits[i] == average_bits[i]]
        i += 1
    return matrix[0]


def average_columns(bitmatrix: list) -> list:
    return [average_bit(column) for column in transpose(bitmatrix)]


def average_bit(bits: list) -> str:
    # spec: tie favors '1'
    return '1' if bits.count('1') >= bits.count('0') else '0'
