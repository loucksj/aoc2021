from src.main import Reader


def part_one(filename: str) -> int:
    packet = Packet(get_binary_list(filename))
    return packet.sum_all_versions()


def get_binary_list(filename: str) -> list:
    binary = bin(int(Reader(filename).lines()[0], 16))
    binary = binary[2:]  # remove leading 0b
    binary_list = [int(digit) for digit in str(binary)]
    # Spec: Round up to 4-bit increments.
    while len(binary_list) % 4 != 0:
        binary_list.insert(0, 0)
    return binary_list


def int_from(binary: list) -> int:
    return int(''.join([str(digit) for digit in binary]), 2)


class Packet:
    def __init__(self, binary):
        self.binary = binary
        self.version = int_from(self.binary[:3])
        self.type = int_from(self.binary[3:6])
        self.subpackets = []
        self.value = None
        self.process()

    def process(self):
        if self.type == 4:  # Spec: Type of '4' is literal.
            self.value = self.as_literal()

    def as_literal(self):
        binary = []
        i = 6
        while True:
            binary += self.binary[i + 1: i + 5]
            if self.binary[i] == 0:
                break
            i += 5
        return int_from(binary)

    def sum_all_versions(self) -> int:
        return self.version + sum(packet.version for packet in self.subpackets)
