from scripts.main import Reader

# Each number 0-9 has a unique sum of frequencies of its letters a signal.
# Ex: Number 1 is made of two letters, which appear 17 (8 + 9) times in a signal.
SUM_KEY = {42: 0, 17: 1, 34: 2, 39: 3,
           30: 4, 37: 5, 41: 6, 25: 7, 49: 8, 45: 9}


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
        self.outputs = [["".join(sorted(config))
                         for config in line[1].split()] for line in lines]
        self.decoders = [self.decode(config) for config in configs]

    def sum_outputs(self) -> int:
        total = 0
        for decoder, output in zip(self.decoders, self.outputs):
            total += int("".join(str(decoder[digit]) for digit in output))
        return total

    def decode(self, signals: list) -> dict:
        letter_sums = self.letter_sums(signals)
        return {signal: SUM_KEY[letter_sums[signal]] for signal in signals}

    def letter_sums(self, signals) -> dict:
        combined = "".join(signals)
        return {signal: sum(combined.count(letter) for letter in signal) for signal in signals}
