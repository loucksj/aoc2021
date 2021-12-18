def part_1(file: str) -> int:
    lines = open(file, 'r').readlines()
    lines = [s.strip() for s in lines]

    polymer = lines.pop(0)
    lines.pop(0)

    pairs = {}
    for line in lines:
        pair = line.split(' -> ')
        pairs[pair[0]] = pair[1]

    for i in range(0, 10):
        polymer = insert(pairs, polymer)
    
    return score(polymer)

def part_2(file: str) -> int:
    lines = open(file, 'r').readlines()
    lines = [s.strip() for s in lines]

    polymer = lines.pop(0)
    lines.pop(0)

    rules = {}
    for line in lines:
        pair = line.split(' -> ')
        rules[pair[0]] = pair[1]

    pairs = get_pairs(polymer)
    for i in range(0, 40):
        pairs = pair_insert(rules, pairs)
    
    return pair_score(pairs, polymer[0], polymer[-1])

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
    for i in range(0, len(polymer)-1):
        a = polymer[i]
        b = polymer[i+1]
        ab = a+b
        if ab in pairs.keys():
            pairs[ab] += 1
        else:
            pairs[ab] = 1
    return pairs

def score(polymer: str) -> int:
    counts = {}
    for s in polymer:
        if s in counts.keys():
            counts[s] += 1
        else:
            counts[s] = 1
    least = min(counts.values())
    most = max(counts.values())
    return most - least

def insert(pairs: dict, polymer: str) -> str:
    new_polymer = ''
    for i in range(0, len(polymer)-1):
        a = polymer[i]
        b = polymer[i+1]
        ab = a+b
        new_polymer += a
        if ab in pairs.keys():
            new_polymer += pairs[ab]
    new_polymer += polymer[-1]
    return new_polymer

if __name__ == '__main__':
    assert part_1('day_14_test.txt') == 1588
    assert part_1('day_14.txt') == 2602

    #off by one errors
    assert part_2('day_14_test.txt') == 2188189693529
    assert part_2('day_14.txt') == 2942885922173