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

    pairs = {}
    for line in lines:
        pair = line.split(' -> ')
        pairs[pair[0]] = pair[1]

    for i in range(0, 40):
        polymer = insert(pairs, polymer)
    
    return score(polymer)

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

    #assert part_2('day_14_test.txt') == 2188189693529
    #assert part_2('day_14.txt') == 0