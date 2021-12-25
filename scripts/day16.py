from scripts.main import Reader

def part_one(filename: str) -> int:
    lines = Reader(filename).lines

    binary = bin(int(lines[0], 16))
    binary = binary[2:]
    while len(binary) % 4 != 0:
        binary = '0' + binary

    packet = Packet(binary)

    return packet.sum_versions()


class Packet():
    def __init__(self, binary):
        self.binary = binary
        self.packets = []
        self.version = 0
        while len(self.binary) > 0:
            self.version = int(self.pull(3), 2)
            t = int(self.pull(3), 2)
            if t == 4:
                sub = ''
                while int(self.pull(1), 2) == 1:
                    sub += self.pull(4)
                sub += self.pull(4)
                self.value = int(sub, 2)
            else:
                i = int(self.pull(1), 2)
                if i == 0:
                    length = int(self.pull(15), 2)
                    packet = Packet(self.pull(length))
                    self.packets.append(packet)
                else:
                    n = int(self.pull(11), 2)
                    for _ in range(n):
                        packet = Packet(self.pull(11))
                        self.packets.append(packet)
            self.cleanup()

    def pull(self, end: int) -> int:
        binary = self.binary[:end]
        self.binary = self.binary[end:]
        return binary

    def cleanup(self):
        while len(self.binary) > 0 and self.binary[0] == '0':
            self.pull(1)

    def sum_versions(self):
        total = self.version
        for p in self.packets:
            total += p.sum_versions()
        return total
