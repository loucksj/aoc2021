def part_1(file: str) -> int:
    lines = open(file, 'r').readlines()
    lines = [s.strip() for s in lines]

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

def part_2(file: str) -> int:
    lines = open(file, 'r').readlines()
    lines = [s.strip() for s in lines]

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

if __name__ == '__main__':
    assert part_1('day_10_test.txt') == 26397
    assert part_1('day_10.txt') == 415953

    assert part_2('day_10_test.txt') == 288957
    assert part_2('day_10.txt') == 2292863731