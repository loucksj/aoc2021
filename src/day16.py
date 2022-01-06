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
    def __init__(self, binary: list):
        self.binary = binary
        self.version = int_from(self.binary[:3])
        self.type = int_from(self.binary[3:6])
        self.value = None  # literals
        self.subpackets = []  # operators
        self.process()

    def process(self):
        if self.type == 4:  # Spec: Type of '4' is literal.
            self.value = self.as_literal()
        else:
            self.as_operator()

    def as_operator(self):
        length_id = self.binary[6]
        if length_id == 0:
            self.operator_15bit()
        else:
            self.operator_11bit()

    def operator_15bit(self):
        subpacket_length = int_from(self.binary[7:23])
        packages = self.binary[23:23 + subpacket_length]
        #todo: process

    def operator_11bit(self):
        subpacket_count = int_from(self.binary[7:18])
        #todo process

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
