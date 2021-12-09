def part_1(file: str) -> int:
    lines = open(file, 'r').readlines()
    lines = [s.strip() for s in lines]
    
    fish = list(map(int, lines[0].split(',')))

    for _ in range(0, 80): #80 days
        count = len(fish)
        for i in range(0, count):
            if fish[i] == 0:
                fish[i] = 6
                fish.append(8)
            else:
                fish[i] -= 1

    return len(fish)

def part_2(file: str) -> int:
    lines = open(file, 'r').readlines()
    lines = [s.strip() for s in lines]
    
    fish = list(map(int, lines[0].split(',')))

    for _ in range(0, 256):
        count = len(fish)
        for i in range(0, count):
            if fish[i] == 0:
                fish[i] = 6
                fish.append(8)
            else:
                fish[i] -= 1

    return len(fish)

if __name__ == '__main__':
    assert part_1('day_6_test.txt') == 5934
    assert part_1('day_6.txt') == 374994

    #assert part_2('day_6_test.txt') == 26984457539
    #assert part_2('day_6.txt') == 0