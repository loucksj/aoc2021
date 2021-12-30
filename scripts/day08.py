from scripts.main import Reader


def part_one(filename: str) -> int:
    lines = Reader(filename).split_lines(' | ')
    return sum([sum([1 for digit in out.split() if len(digit) in [2, 3, 4, 7]]) for _, out in lines])


def part_two(filename: str) -> int:
    return Decoder(filename).sum_outputs()


class Decoder():
    def __init__(self, filename: str):
        lines = Reader(filename).split_lines(' | ')
        configs = [["".join(sorted(config))
                    for config in line[0].split()] for line in lines]
        self.outputs = [["".join(sorted(con))
                         for con in line[1].split()] for line in lines]
        self.decoders = [self.decoded(config) for config in configs]

    def sum_outputs(self) -> int:
        total = 0
        for decoder, output in zip(self.decoders, self.outputs):
            total += sum(decoder[digit] * 10**(len(output)-1-i)
                         for i, digit in enumerate(output))
        return total

    def decode1478(self, signals) -> dict:
        code = {}
        for digit in signals:
            if len(digit) == 2:
                code[1] = digit
                signals.remove(digit)
                break
        for digit in signals:
            if len(digit) == 3:
                code[7] = digit
                signals.remove(digit)
                break
        for digit in signals:
            if len(digit) == 4:
                code[4] = digit
                signals.remove(digit)
                break
        for digit in signals:
            if len(digit) == 7:
                code[8] = digit
                signals.remove(digit)
                break
        return code

    def decoded(self, signals: list) -> dict:
        code = self.decode1478(signals)
        # 0
        for letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
            count = 0
            for digit in signals:
                if letter in digit:
                    count += 1
            if count == 5:
                for digit in signals:
                    if letter not in digit and len(digit) == 6:
                        code[0] = digit
                        signals.remove(digit)
                        break
            if 0 in code.keys():
                break
        # 5
        for digit in signals:
            if len(digit) == 5:
                found = True
                for other in signals:
                    if len(other) == 6:
                        for char in digit:
                            if char not in other:
                                found = False
                                break
                if found:
                    code[5] = digit
                    signals.remove(digit)
                    break
        # 2, 3
        for digit in signals:
            if len(digit) == 5:
                diff = 0
                for char in digit:
                    if char not in code[5]:
                        diff += 1
                if diff == 1:
                    code[3] = digit
                else:
                    code[2] = digit
        signals.remove(code[2])
        signals.remove(code[3])
        # 6
        for digit in signals:
            for char in code[3]:
                if char not in digit:
                    code[6] = digit
                    signals.remove(digit)
                    break
        # 9
        code[9] = signals.pop()
        code = {v: k for k, v in code.items()}
        return code
