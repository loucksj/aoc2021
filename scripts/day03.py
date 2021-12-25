from scripts.main import Reader


def part_one(filename: str) -> int:
    majority = Bitmatrix().from_file(filename).majority_bits()
    return as_int(majority) * as_int(flip(majority))


def part_two(filename: str) -> int:
    bitmatrix = Bitmatrix().from_file(filename)
    return as_int(bitmatrix.path(True)) * as_int(bitmatrix.path(False))


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
        return [most(column) for column in self.transposed()]

    def transposed(self):
        return [list(x) for x in zip(*self.matrix)]

    def path(self, up):
        i = 0
        sift = Bitmatrix(self.matrix)
        while len(sift.matrix) > 1:
            sift.matrix = [bits for bits in sift.matrix if up ==
                           (bits[i] == sift.majority_bits()[i])]
            i += 1
        return sift.matrix[0]
