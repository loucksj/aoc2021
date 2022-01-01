from scripts.main import Reader

PAIRS = {'(': ')', '[': ']', '{': '}', '<': '>', }

# The first incorrect closing characters are corrupt.
CORRUPT_POINTS = {')': 3, ']': 57, '}': 1197, '>': 25137}

# The missing closing characters are incomplete.
INCOMPLETE_POINTS = {')': 1, ']': 2, '}': 3, '>': 4}


def part_one(filename: str) -> int:
    return score_corrupted(filename)


def part_two(filename: str) -> int:
    return score_incomplete(filename)


def score_corrupted(filename: str) -> int:
    return sum(CORRUPT_POINTS[char] for char in corrupt_chars(filename))


def corrupt_chars(filename: str) -> list:
    return [char for _, char in line_data(filename)[0]]


def score_incomplete(filename: str) -> int:
    scores = incomplete_scores(filename)
    middle_index = int((len(scores) - 1) / 2)
    return sorted(scores)[middle_index]


def incomplete_scores(filename: str) -> int:
    return [incomplete_line_score(line) for line in incomplete_chars(filename)]


def incomplete_chars(filename: str) -> list:
    return [chars for _, chars in line_data(filename)[1]]


def incomplete_line_score(line: list):
    score = 0
    for error in line:
        score = score * 5 + INCOMPLETE_POINTS[error]
    return score


def line_data(filename: str) -> list:
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
