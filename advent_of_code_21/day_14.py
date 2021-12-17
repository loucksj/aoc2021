def part_1(file: str) -> int:
    lines = open(file, 'r').readlines()
    lines = [s.strip() for s in lines]
    #10 steps
    return 0

if __name__ == '__main__':
    assert part_1('day_13_test.txt') == 1588
    #assert part_1('day_13.txt') == 0