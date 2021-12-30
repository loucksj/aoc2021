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
        self.outputs = [["".join(sorted(con))
                         for con in line[1].split()] for line in lines]
        self.decoders = [self.decoded(config) for config in configs]

    def sum_outputs(self) -> int:
        total = 0
        for decoder, output in zip(self.decoders, self.outputs):
            total += sum(decoder[digit] * 10**(len(output)-1-i)
                         for i, digit in enumerate(output))
        return total

    def decoded(self, signals: list) -> dict:
        sums = self.letter_sums(signals)
        code = {}
        for signal in signals:
            code[signal] = SUM_KEY[sums[signal]]
        return code
    
    def letter_sums(self, signals) -> dict:
        sums = {}
        combined = "".join(signals)
        for signal in signals:
            sums[signal] = sum(combined.count(letter) for letter in signal)
        return sums