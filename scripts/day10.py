from scripts.main import Reader

PAIRS = {'(': ')', '[': ']', '{': '}', '<': '>', }


def part_one(filename: str) -> int:
    return score_corrupted(corrupt_chars(filename))


def part_two(filename: str) -> int:
    return score_incomplete(incomplete_chars(filename))


# First incorrect closing chars.
def corrupt_chars(filename: str) -> list:
    lines = Reader(filename).char_lines()
    corrupted = []
    for line in lines:
        next = []
        for char in line:
            if char in PAIRS.keys():
                next.append(PAIRS[char])
            elif char != next.pop():
                corrupted.append(char)
                break
    return corrupted

# Missing closing chars.
def incomplete_chars(filename: str) -> list:
    lines = Reader(filename).char_lines()
    incomplete = []
    for line in lines:
        next = []
        corrupt = False
        for char in line:
            if char in PAIRS.keys():
                next.append(PAIRS[char])
                continue
            if char == next.pop():
                continue
            corrupt = True
            break
        if corrupt:
            continue
        incomplete.append(list(reversed(next)))
    return incomplete


def score_incomplete(errors: list) -> int:
    points = {')': 1, ']': 2, '}': 3, '>': 4}
    scores = []
    for line in errors:
        score = 0
        for error in line:
            score *= 5
            score += points[error]
        scores.append(score)
    scores = sorted(scores)
    middle = int((len(scores) - 1)/2)
    return scores[middle]


def score_corrupted(errors: list) -> int:
    points = {')': 3, ']': 57, '}': 1197, '>': 25137}
    return sum(points[char] for char in errors)
