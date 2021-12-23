from main import Reader


def part01(filename: str) -> int:
    depths = Reader(filename).getLinesAsInts()
    return count_greaterthan_prev(depths)


def part02(filename: str) -> int:
    depths = Reader(filename).getLinesAsInts()
    return count_greaterthan_prev(sum_by_width(depths, 2))


def count_greaterthan_prev(values: list):
    return sum(1 for first, second in zip(values[:-1], values[1:]) if second > first)


def sum_by_width(values: list, widen_by: int) -> list:
    summed = []
    leftIndexMax = len(values) - widen_by
    for leftIndex in range(leftIndexMax):
        rightIndex = leftIndex + 1 + widen_by
        sumBetween = sum(values[leftIndex:rightIndex])
        summed.append(sumBetween)
    return summed


if __name__ == '__main__':
    assert part01('day01_example.txt') == 7
    assert part01('day01_input.txt') == 1215

    assert part02('day01_example.txt') == 5
    assert part02('day01_input.txt') == 1150
