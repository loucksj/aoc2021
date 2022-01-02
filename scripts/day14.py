from scripts.main import Reader


def part_one(filename: str) -> int:
    return Polymer(filename).steps(10).score()


def part_two(filename: str) -> int:
    return Polymer(filename).steps(40).score()


class Polymer():
    # The polymer is tracked as the count of each unique pair of letters.
    # With each step, each pair with a rule doubles into two new pairs.
    def __init__(self, filename: str) -> None:
        lines = Reader(filename).halves_lined()
        self.original_chain = lines[0][0]
        self.rules = dict(line.split(' -> ') for line in lines[1])
        self.pair_counts = self.count_pairs()

    def steps(self, steps):
        for _ in range(steps):
            self.step()
        return self

    def step(self) -> dict:
        pair_counts = {}
        for pair in [pair for pair in self.pair_counts if pair in self.rules]:
            left = pair[0] + self.rules[pair]
            right = self.rules[pair] + pair[1]
            count = self.pair_counts[pair]
            pair_counts[left] = pair_counts.get(left, 0) + count
            pair_counts[right] = pair_counts.get(right, 0) + count
        self.pair_counts = pair_counts

    def score(self):
        scores = self.letter_scores()
        return max(scores) - min(scores)

    def letter_scores(self):
        scores = {}
        for pair in self.pair_counts:
            for char in pair:
                # Each letter is part of two pairs, so its count is halved...
                scores[char] = scores.get(char, 0) + self.pair_counts[pair] / 2
        # ...except the first and last letter, which are un-halved
        scores[self.original_chain[0]] += 0.5
        scores[self.original_chain[-1]] += 0.5
        return scores.values()

    def count_pairs(self) -> dict:
        pairs = {}
        for i, _ in enumerate(self.original_chain[:-1]):
            pair = self.original_chain[i] + self.original_chain[i + 1]
            pairs[pair] = pairs.get(pair, 0) + 1
        return pairs
