from scripts.main import Reader


def part_one(filename: str) -> int:
    majority = Bitmatrix().from_file(filename).majority_per_index()
    return as_int(majority) * as_int(flip(majority))


def part_two(filename: str) -> int:
    bitmatrix = Bitmatrix().from_file(filename)
    return as_int(bitmatrix.most_path()) * as_int(bitmatrix.least_path())


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

    def majority_per_index(self) -> list:
        return [most(column) for column in self.transposed()]

    def transposed(self):
        return [list(x) for x in zip(*self.matrix)]

    def most_path(self) -> list:
        return self.path(True)
    
    def least_path(self) -> list:
        return self.path(False)

    def path(self, most):
        i = 0
        sift = Bitmatrix(self.matrix)
        while len(sift.matrix) > 1:
            if most:
                sift.matrix = sift.majority_at_index(i)
            else:
                sift.matrix = sift.minority_at_index(i)
            i += 1
        return sift.matrix[0]

    def majority_at_index(self, i: int) -> list:
        return [bits for bits in self.matrix if bits[i] == self.majority_per_index()[i]]

    def minority_at_index(self, i: int) -> list:
        return [bits for bits in self.matrix if bits[i] != self.majority_per_index()[i]]
