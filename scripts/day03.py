from scripts.input_manager import char_lines, strip_lines


def part_one(filename: str) -> int:
    binary = majority_binary(filename)
    return int(binary, 2) * int(flip(binary), 2)


def part_two(filename: str) -> int:
    major_binaries = Binaries().from_file(filename)
    minor_binaries = Binaries().from_file(filename)
    return int(major_binaries.major_path(), 2) * int(minor_binaries.minor_path(), 2)

def majority_binary(filename: str):
    return ''.join([commonest_element(line) for line in transpose(char_lines(filename))])

def transpose(values: list):
    return [list(x) for x in zip(*values)]

def commonest_element(values: list):
    return max(set(values), key=values.count)

class Binaries:
    def from_file(self, filename: str):
        self.binaries = strip_lines(filename)
        self.digits = len(self.binaries[0])
        return self

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
