from scripts.main import Reader


def part_one(filename: str) -> int:
    return Polymer(filename).do_steps(10).score()


def part_two(filename: str) -> int:
    return Polymer(filename).do_steps(40).score()


class Polymer():
    def __init__(self, filename: str) -> None:
        lines = Reader(filename).halves_lined()
        self.original_chain = lines[0][0]
        self.rules = dict(line.split(' -> ') for line in lines[1])
        self.pairs = self.get_pairs()

    def do_steps(self, steps):
        for _ in range(steps):
            self.process()
        return self

    def score(self):
        first, last = self.original_chain[0], self.original_chain[-1]
        scores = {}
        for key in self.pairs.keys():
            magnitude = self.pairs[key]
            for s in key:
                if s in scores:
                    scores[s] += magnitude / 2
                else:
                    scores[s] = magnitude / 2
        scores[first] += 0.5
        scores[last] += 0.5
        largest = max(scores.values())
        smallest = min(scores.values())
        score = largest - smallest
        return int(score)

    def process(self) -> dict:
        new_pairs = {}
        for pair in self.pairs:
            if pair in self.rules.keys():
                magnitude = self.pairs[pair]
                b = self.rules[pair]
                ab = pair[0] + b
                if ab in new_pairs:
                    new_pairs[ab] += magnitude
                else:
                    new_pairs[ab] = magnitude
                bc = b + pair[1]
                if bc in new_pairs:
                    new_pairs[bc] += magnitude
                else:
                    new_pairs[bc] = magnitude
        self.pairs = new_pairs

    def get_pairs(self) -> dict:
        pairs = {}
        for i in range(len(self.original_chain)-1):
            a = self.original_chain[i]
            b = self.original_chain[i+1]
            ab = a+b
            if ab in pairs.keys():
                pairs[ab] += 1
            else:
                pairs[ab] = 1
        return pairs
