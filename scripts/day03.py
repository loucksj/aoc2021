from scripts.input_manager import strip_lines


def part_one(filename: str) -> int:
    majority_bits = Binaries().from_file(filename).majority_bits()
    return int(majority_bits, 2) * int(flip(majority_bits), 2)


def part_two(filename: str) -> int:
    major_binaries = Binaries().from_file(filename)
    minor_binaries = Binaries().from_file(filename)
    return int(major_binaries.major_path(), 2) * int(minor_binaries.minor_path(), 2)


class Binaries:
    def from_file(self, filename: str):
        self.binaries = strip_lines(filename)
        self.digits = len(self.binaries[0])
        return self

    def majority_bits(self) -> str:
        return ''.join(self.majority_bit(i) for i in range(self.digits))

    def majority_bit(self, i: int) -> str:
        return '1' if self.sum_index(i) >= len(self.binaries)/2 else '0'

    def sum_index(self, i: int) -> int:
        return sum(int(binary[i]) for binary in self.binaries)

    def major_path(self) -> str:
        i = 0
        while len(self.binaries) > 1:
            self.binaries = self.index_majorities(i)
            i += 1
        return self.binaries[0]

    def minor_path(self) -> str:
        i = 0
        while len(self.binaries) > 1:
            self.binaries = self.index_minorities(i)
            i += 1
        return self.binaries[0]

    def index_majorities(self, i: int) -> list:
        majority = self.majority_bit(i)
        return [binary for binary in self.binaries if binary[i] == majority]

    def index_minorities(self, i: int) -> list:
        majority = self.majority_bit(i)
        return [binary for binary in self.binaries if binary[i] != majority]


def flip(binary: str) -> str:
    return ''.join(['1' if i == '0' else '0' for i in binary])
