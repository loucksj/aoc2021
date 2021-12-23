from main import Reader


def part01(filename: str) -> int:
    L = Reader(filename).getLinesAsInts()
    return count_greaterthan_prev(L)


def part02(filename: str) -> int:
    L = Reader(filename).getLinesAsInts()
    return count_greaterthan_prev(sum_by_width(L, 2))


def count_greaterthan_prev(L: list):
    count = 0
    adjacentElements = zip(L[:-1], L[1:])
    for first, second in adjacentElements:
        if second > first:
            count += 1
    return count


def sum_by_width(L: list, widen_by: int) -> list:
    summed = []
    leftIndexMax = len(L) - widen_by
    for leftIndex in range(leftIndexMax):
        rightIndex = leftIndex + 1 + widen_by
        sumBetween = sum(L[leftIndex:rightIndex])
        summed.append(sumBetween)
    return summed


if __name__ == '__main__':
    assert part01('day01_example.txt') == 7
    assert part01('day01_input.txt') == 1215

    assert part02('day01_example.txt') == 5
    assert part02('day01_input.txt') == 1150
