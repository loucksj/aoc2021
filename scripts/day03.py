from scripts.main import Reader


def part_one(filename: str) -> int:
    bitmatrix = Bitmatrix(Reader(filename).matrix())
    return Bits.inted(bitmatrix.majority()) * Bits.inted(Bits.flip(bitmatrix.majority()))

def part_two(filename: str) -> int:
    return Bitmatrix(Reader(filename).matrix()).path_vector()


class Bits:
    def flip(bits: list) -> str:
        return ['1' if digit == '0' else '0' for digit in bits]

    def majority(bits: list) -> str:
        return '1' if bits.count('1') >= bits.count('0') else '0'

    def inted(bits: list):
        return int(''.join(bits), 2)


class Bitmatrix:
    def __init__(self, bitmatrix: list) -> None:
        self.matrix = bitmatrix

    def majority(self) -> list:
        return [Bits.majority(column) for column in self.transposed()]

    def path_vector(self) -> int:
        return Bits.inted(self.common_path_bits()) * Bits.inted(self.minor_path_bits())

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
        return [bits for bits in self.matrix if bits[i] == self.majority()[i]]

    def rare_index_elements(self, i: int) -> list:
        return [bits for bits in self.matrix if bits[i] != self.majority()[i]]

    def transposed(self):
        return [list(x) for x in zip(*self.matrix)]
