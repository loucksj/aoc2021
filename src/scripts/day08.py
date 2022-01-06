from src.scripts.main import Reader

# Each number 0-9 has a (luckily) unique sum of the frequencies of each letter in it.
# Ex: 1 is made of two letters, which in total appear 17 (8+9) times each signal.
# Ex: 8 is made of all seven letters, which in total appear 49 (6+8+8+7+4+7+9) times each signal.
SUM_KEY = {42: 0, 17: 1, 34: 2, 39: 3,
           30: 4, 37: 5, 41: 6, 25: 7, 49: 8, 45: 9}


def part_one(filename: str) -> int:
    lines = Reader(filename).split_lines(' | ')
    return sum(sumif_2347(output) for _, output in lines)


def part_two(filename: str) -> int:
    return Decoder(filename).sum_outputs()


def sumif_2347(strings: list):
    return sum(1 for digit in strings.split() if len(digit) in [2, 3, 4, 7])


class Decoder():
    def __init__(self, filename: str):
        lines = Reader(filename).split_lines(' | ')
        self.outputs = [sorted_elements(output) for _, output in lines]
        configs = [sorted_elements(config) for config, _ in lines]
        self.decoders = [self.decode(config) for config in configs]

    def sum_outputs(self) -> int:
        total = 0
        for decoder, output in zip(self.decoders, self.outputs):
            total += int("".join(str(decoder[digit]) for digit in output))
        return total

    def decode(self, signals: list) -> dict:
        sums = letter_sums(signals)
        return {signal: SUM_KEY[sums[signal]] for signal in signals}


def letter_sums(strings: list) -> dict:
    combined = "".join(strings)
    return {string: sum(combined.count(letter) for letter in string) for string in strings}


def sorted_elements(string: str) -> list:
    return ["".join(sorted(s)) for s in string.split()]
