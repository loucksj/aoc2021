from scripts.main import Reader

PAIRS = {'(': ')', '[': ']', '{': '}', '<': '>', }

# The first incorrect closing characters are corrupt.
CORRUPT_POINTS = {')': 3, ']': 57, '}': 1197, '>': 25137}

# The missing closing characters are incomplete.
INCOMPLETE_POINTS = {')': 1, ']': 2, '}': 3, '>': 4}


def part_one(filename: str) -> int:
    return Syntax(filename).score_corrupted()


def part_two(filename: str) -> int:
    return Syntax(filename).score_incomplete()


class Syntax():
    def __init__(self, filename: str) -> None:
        self.lines = Reader(filename).char_lines()

    def score_corrupted(self) -> int:
        return sum(CORRUPT_POINTS[char] for char in self.corrupt_chars())

    def corrupt_chars(self) -> list:
        return [char for _, char in self.line_data()[0]]

    def score_incomplete(self) -> int:
        scores = self.incomplete_scores()
        middle_index = int((len(scores) - 1) / 2)
        return sorted(scores)[middle_index]

    def incomplete_scores(self) -> int:
        return [self.incomplete_line_score(line) for line in self.incomplete_chars()]

    def incomplete_chars(self) -> list:
        return [chars for _, chars in self.line_data()[1]]

    def incomplete_line_score(self, line: list):
        score = 0
        for error in line:
            score = score * 5 + INCOMPLETE_POINTS[error]
        return score

    def line_data(self) -> list:
        corrupted = []
        incomplete = []
        for line in self.lines:
            stack = []
            corrupt = False
            for char in line:
                if char in PAIRS.keys():
                    stack.append(PAIRS[char])
                elif char != stack.pop():
                    corrupted.append((line, char))
                    corrupt = True
                    break
            if not corrupt:
                incomplete.append((line, list(reversed(stack))))
        return (corrupted, incomplete)
