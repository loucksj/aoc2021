from scripts.main import Reader


def part_one(filename: str) -> int:
    bitmatrix = Bitmatrix().from_file(filename)
    return Bits.as_int(bitmatrix.majority_bits()) * Bits.as_int(Bits.flip(bitmatrix.majority_bits()))


def part_two(filename: str) -> int:
    bitmatrix = Bitmatrix().from_file(filename)
    return Bits.as_int(bitmatrix.most_path()) * Bits.as_int(bitmatrix.least_path())


class Bits():
    def as_int(bits: list):
        return int(''.join(bits), 2)

    def most(bits: list) -> str:
        return '1' if bits.count('1') >= bits.count('0') else '0'

    def flip(bits: list) -> str:
        return ['1' if digit == '0' else '0' for digit in bits]


class Bitmatrix():
    def __init__(self, bitmatrix=[[]]) -> None:
        self.matrix = bitmatrix

    def from_file(self, filename: str):
        self.matrix = Reader(filename).matrix()
        return self

    def majority_bits(self) -> list:
        return [Bits.most(column) for column in self.transposed()]

    def most_path(self) -> list:
        i = 0
        sift = Bitmatrix(self.matrix)
        while len(sift.matrix) > 1:
            sift.matrix = sift.common_index_elements(i)
            i += 1
        return sift.matrix[0]

    def least_path(self) -> list:
        i = 0
        sift = Bitmatrix(self.matrix)
        while len(sift.matrix) > 1:
            sift.matrix = sift.rare_index_elements(i)
            i += 1
        return sift.matrix[0]

    def common_index_elements(self, i: int) -> list:
        return [bits for bits in self.matrix if bits[i] == self.majority_bits()[i]]

    def rare_index_elements(self, i: int) -> list:
        return [bits for bits in self.matrix if bits[i] != self.majority_bits()[i]]

    def transposed(self):
        return [list(x) for x in zip(*self.matrix)]
