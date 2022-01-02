from scripts.main import Reader


def part_one(filename: str) -> int:
    return Polymer(filename).do_steps(10).score()


def part_two(filename: str) -> int:
    polymer = Polymer(filename)

    pairs = get_pairs(polymer.chain)
    for _ in range(40):
        pairs = pair_insert(polymer.rules, pairs)

    return pair_score(pairs, polymer.chain[0], polymer.chain[-1])


class Polymer():
    def __init__(self, filename: str) -> None:
        lines = Reader(filename).halves_lined()
        self.chain = lines[0][0]
        self.rules = dict(line.split(' -> ') for line in lines[1])

    def do_steps(self, steps):
        for _ in range(steps):
            self.chain = self.insert()
        return self

    def insert(self) -> str:
        new_polymer = ''
        for i in range(len(self.chain)-1):
            a = self.chain[i]
            b = self.chain[i+1]
            ab = a+b
            new_polymer += a
            if ab in self.rules.keys():
                new_polymer += self.rules[ab]
        new_polymer += self.chain[-1]
        return new_polymer

    def score(self) -> int:
        counts = {}
        for s in self.chain:
            if s in counts.keys():
                counts[s] += 1
            else:
                counts[s] = 1
        least = min(counts.values())
        most = max(counts.values())
        return most - least


def pair_score(pairs: dict, first: str, last: str):
    scores = {}
    for key in pairs.keys():
        magnitude = pairs[key]
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


def pair_insert(rules: dict, pairs: dict) -> dict:
    new_pairs = {}
    for pair in pairs:
        if pair in rules.keys():
            magnitude = pairs[pair]
            b = rules[pair]
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
    return new_pairs


def get_pairs(polymer: str) -> dict:
    pairs = {}
    for i in range(len(polymer)-1):
        a = polymer[i]
        b = polymer[i+1]
        ab = a+b
        if ab in pairs.keys():
            pairs[ab] += 1
        else:
            pairs[ab] = 1
    return pairs
