from scripts.get_input import strip_lines

def part_one(filename: str) -> int:
    lines = strip_lines(filename)

    pairs = {'(' : ')', '[' : ']', '{' : '}', '<' : '>',}

    corrupted = []
    for line in lines:
        next = []
        line = [char for char in line]
        for char in line:
            if char in pairs.keys():
                next.append(pairs[char])
                continue
            if char == next.pop():
                continue
            corrupted.append(char)
            break

    return score_corrupted(corrupted)

def part_two(filename: str) -> int:
    lines = strip_lines(filename)

    pairs = {'(' : ')', '[' : ']', '{' : '}', '<' : '>',}

    incomplete = []
    for line in lines:
        next = []
        line = [char for char in line]
        corrupt = False
        for char in line:
            if char in pairs.keys():
                next.append(pairs[char])
                continue
            if char == next.pop():
                continue
            corrupt = True
            break
        if corrupt:
            continue
        incomplete.append(reversed(next))

    return score_incomplete(incomplete)

def score_incomplete(errors: list) -> int:
    points = {')':1, ']':2, '}':3, '>':4}
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
    score = 0
    points = {')':3, ']':57, '}':1197, '>':25137}
    for char in errors:
        score += points[char]
    return score
