from scripts.main import Reader


def part_one(filename: str) -> int:
    return Bitmatrix(Reader(filename).matrix()).rarity_vector()


def part_two(filename: str) -> int:
    return Bitmatrix(Reader(filename).matrix()).path_vector()


class Bits:
    def flip(bits: list) -> str:
        return ['1' if digit == '0' else '0' for digit in bits]

    def majority(bits: list) -> str:
        return '1' if bits.count('1') >= bits.count('0') else '0'


class Bitmatrix:
    def __init__(self, bitmatrix: list) -> None:
        self.matrix = bitmatrix

    def rarity_vector(self) -> int:
        return self.common_index_value() * self.rare_index_value()

    def to_int(self, bits: list):
        return int(''.join(bits), 2)

    def common_index_value(self) -> int:
        return self.to_int(self.common_index_bits())

    def rare_index_value(self) -> int:
        return self.to_int(self.rare_index_bits())

    def common_index_bits(self) -> list:
        return [Bits.majority(column) for column in self.transposed()]

    def rare_index_bits(self) -> list:
        return Bits.flip(self.common_index_bits())

    def path_vector(self) -> int:
        return self.to_int(self.common_path_bits()) * self.to_int(self.minor_path_bits())

    def common_path_bits(self) -> list:
        i = 0
        sift = Bitmatrix(self.matrix)
        while len(sift.matrix) > 1:
            sift.matrix = sift.common_index_elements(i)
            i += 1
        return sift.matrix[0]

    def minor_path_bits(self) -> list:
        i = 0
        sift = Bitmatrix(self.matrix)
        while len(sift.matrix) > 1:
            sift.matrix = sift.rare_index_elements(i)
            i += 1
        return sift.matrix[0]

    def common_index_elements(self, i: int) -> list:
        return [bits for bits in self.matrix if bits[i] == self.common_index_bits()[i]]

    def rare_index_elements(self, i: int) -> list:
        return [bits for bits in self.matrix if bits[i] != self.common_index_bits()[i]]

    def transposed(self):
        return [list(x) for x in zip(*self.matrix)]
