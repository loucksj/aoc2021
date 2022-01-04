from scripts.main import Reader


def part_one(filename: str) -> int:
    packet = Packet(get_binary_list(filename))
    return packet.sum_versions()


def get_binary_list(filename: str) -> list:
    binary = bin(int(Reader(filename).lines()[0], 16))
    binary = binary[2:] #remove leading 0b
    binary_list = [int(digit) for digit in str(binary)]
    # Spec: Round up to 4-bit increments.
    while len(binary_list) % 4 != 0:
        binary_list.insert(0, 0)
    return binary_list


class Packet():
    def __init__(self, binary):
        self.binary = binary

    def sum_versions(self) -> int:
        return 0
