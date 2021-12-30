from scripts.main import Reader


def part_one(filename: str) -> int:
    lines = Reader(filename).split_lines(' | ')
    return sum([sum([1 for digit in out.split() if len(digit) in [2, 3, 4, 7]]) for _, out in lines])

def part_two(filename: str) -> int:
    return Decoder(filename).decode()

class Decoder():
    def __init__(self, filename: str):
        lines = Reader(filename).split_lines(' | ')
        self.configs = [["".join(sorted(string)) for string in line[0].split()] for line in lines]
        self.outputs = [["".join(sorted(string)) for string in line[1].split()] for line in lines]
    
    def decode(self) -> int:
        total = 0
        for config, output in zip(self.configs, self.outputs):
            decoded = self.decode_old(config)
            value = 0
            for digit in output:
                value *= 10
                value += decoded[digit]
            total += value
        return total     

    def decode_old(self, signals: list) -> dict:
        decoded = {}
        # 1, 4, 7, 8
        for digit in signals:
            if len(digit) == 2:
                decoded[1] = digit
                signals.remove(digit)
                break
        for digit in signals:
            if len(digit) == 3:
                decoded[7] = digit
                signals.remove(digit)
                break
        for digit in signals:
            if len(digit) == 4:
                decoded[4] = digit
                signals.remove(digit)
                break
        for digit in signals:
            if len(digit) == 7:
                decoded[8] = digit
                signals.remove(digit)
                break
        # 0
        for letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
            count = 0
            for digit in signals:
                if letter in digit:
                    count += 1
            if count == 5:
                for digit in signals:
                    if letter not in digit and len(digit) == 6:
                        decoded[0] = digit
                        signals.remove(digit)
                        break
            if 0 in decoded.keys():
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
                    decoded[5] = digit
                    signals.remove(digit)
                    break
        # 2, 3
        for digit in signals:
            if len(digit) == 5:
                diff = 0
                for char in digit:
                    if char not in decoded[5]:
                        diff += 1
                if diff == 1:
                    decoded[3] = digit
                else:
                    decoded[2] = digit
        signals.remove(decoded[2])
        signals.remove(decoded[3])
        # 6
        for digit in signals:
            for char in decoded[3]:
                if char not in digit:
                    decoded[6] = digit
                    signals.remove(digit)
                    break
        # 9
        decoded[9] = signals.pop()
        decoded = {v: k for k, v in decoded.items()}
        return decoded