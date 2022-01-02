from scripts.main import Reader


def part_one(filename: str) -> int:
    return Polymer(filename).do_steps(10).score()


def part_two(filename: str) -> int:
    return Polymer(filename).do_steps(40).score()


class Polymer():
    # The polymer is tracked as the count of each unique pair of letters.
    # With each step, each pair (with a rule) doubles into two new pairs.
    def __init__(self, filename: str) -> None:
        lines = Reader(filename).halves_lined()
        self.original_chain = lines[0][0]
        self.rules = dict(line.split(' -> ') for line in lines[1])
        self.pair_counts = self.count_pairs()

    def do_steps(self, steps):
        for _ in range(steps):
            self.step()
        return self

    def score(self):
        scores = self.letter_scores()
        return max(scores) - min(scores)

    def letter_scores(self):
        # Each letter is part of two pairs, so its count is halved...
        scores = {}
        for key in self.pair_counts.keys():
            for char in key:
                scores[char] = scores.get(char, 0) + self.pair_counts[key] / 2
        # ...except the first and last letter, which are un-halved
        first, last = self.original_chain[0], self.original_chain[-1]
        scores[first] += 0.5
        scores[last] += 0.5
        return scores.values()

    def step(self) -> dict:
        next_pairs = {}
        for pair in self.pair_counts:
            if pair in self.rules.keys():
                count = self.pair_counts[pair]
                left = pair[0] + self.rules[pair]
                right = self.rules[pair] + pair[1]
                next_pairs[left] = next_pairs.get(left, 0) + count
                next_pairs[right] = next_pairs.get(right, 0) + count
        self.pair_counts = next_pairs

    def count_pairs(self) -> dict:
        pairs = {}
        for i in range(len(self.original_chain)-1):
            pair = self.original_chain[i] + self.original_chain[i + 1]
            pairs[pair] = pairs.get(pair, 0) + 1
        return pairs
