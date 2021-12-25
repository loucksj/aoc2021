def part_1(file: str) -> int:
    lines = open(file, 'r').readlines()
    line = lines[0].strip()

    binary = bin(int(line, 16))
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

if __name__ == '__main__':
    assert part_1('day_16_literal.txt') == 6
    assert part_1('day_16_operator.txt') == 1
    assert part_1('day_16_test1.txt') == 16
    assert part_1('day_16_test2.txt') == 12
    assert part_1('day_16_test3.txt') == 23
    assert part_1('day_16_test4.txt') == 31
    #assert part_1('day_16.txt') == 0

    #assert part_2('day_16_test.txt') == 0
    #assert part_2('day_16.txt') == 0
