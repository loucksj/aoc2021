def part_1(file: str) -> int:
    lines = open(file, 'r').readlines()
    lines = [s.strip() for s in lines]

if __name__ == '__main__':
    assert part_1('day_5_test.txt') == 5
    #assert part_1('day_5.txt') == 0

    #assert part_2('day_5_test.txt') == 0
    #assert part_2('day_5.txt') == 0