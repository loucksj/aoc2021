from scripts.main import Reader, Tools


def part_one(filename: str) -> int:
    return rarity_vector(Reader(filename).matrix())


def part_two(filename: str) -> int:
    return path_vector(Reader(filename).matrix())


def rarity_vector(bitmatrix: list) -> int:
    return common_index_value(bitmatrix) * rare_index_value(bitmatrix)


def to_int(bits: list):
    return int(''.join(bits), 2)


def common_index_value(bitmatrix: list) -> int:
    return to_int(common_index_bits(bitmatrix))


def rare_index_value(bitmatrix: list) -> int:
    return to_int(rare_index_bits(bitmatrix))


def common_index_bits(bitmatrix: list) -> list:
    return [common_element(column) for column in Tools.transpose(bitmatrix)]


def rare_index_bits(bitmatrix: list) -> list:
    return Tools.flip(common_index_bits(bitmatrix))


def common_element(bits: list) -> str:
    # spec: ties in favor of '1'
    return '1' if bits.count('1') >= bits.count('0') else '0'


def path_vector(bitmatrix: list) -> int:
    return to_int(common_path_bits(bitmatrix)) * to_int(minor_path_bits(bitmatrix))


def common_path_bits(bitmatrix: list) -> list:
    i = 0
    while len(bitmatrix) > 1:
        bitmatrix = common_index_elements(bitmatrix, i)
        i += 1
    return bitmatrix[0]


def minor_path_bits(bitmatrix: list) -> list:
    i = 0
    while len(bitmatrix) > 1:
        bitmatrix = rare_index_elements(bitmatrix, i)
        i += 1
    return bitmatrix[0]


def common_index_elements(bitmatrix: list, i: int) -> list:
    return [bits for bits in bitmatrix if bits[i] == common_index_bits(bitmatrix)[i]]


def rare_index_elements(bitmatrix, i: int) -> list:
    return [bits for bits in bitmatrix if bits[i] != common_index_bits(bitmatrix)[i]]
