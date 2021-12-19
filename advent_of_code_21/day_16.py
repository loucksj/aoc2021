def part_1(file: str) -> int:
    lines = open(file, 'r').readlines()
    lines = [s.strip() for s in lines]

    return 0

if __name__ == '__main__':
    assert part_1('day_16_test.txt') == 0
    #assert part_1('day_16.txt') == 0

    #assert part_2('day_16_test.txt') == 0
    #assert part_2('day_16.txt') == 0