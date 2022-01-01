from scripts.main import Reader

PAIRS = {'(': ')', '[': ']', '{': '}', '<': '>', }


def part_one(filename: str) -> int:
    return score_corrupted(filename)


def part_two(filename: str) -> int:
    return score_incomplete(incomplete_chars(filename))


def score_corrupted(filename: str) -> int:
    errors = corrupt_chars(filename)
    points = {')': 3, ']': 57, '}': 1197, '>': 25137}
    return sum(points[char] for char in errors)


def corrupt_chars(filename: str) -> list:
    return [char for _, char in line_data(filename)[0]]


def incomplete_chars(filename: str) -> list:
    # The missing closing characters.
    return [chars for _, chars in line_data(filename)[1]]


def line_data(filename: str) -> list:
    # The first incorrect closing characters.
    lines = Reader(filename).char_lines()
    corrupted = []
    incomplete = []
    for line in lines:
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
