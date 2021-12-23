from main import Reader


def part01(filename: str) -> int:
    return Sonar.from_file(filename).count_increases()


def part02(filename: str) -> int:
    return Sonar.from_file(filename).count_increases_wide(2)


class Sonar():
    def __init__(self, depths: list):
        self.depths = depths

    @classmethod
    def from_file(cls, filename: str):
        linesAsInts = Reader(filename).getLinesAsInts()
        return cls(linesAsInts)

    def count_increases_wide(self, widen_by: int) -> int:
        return Sonar(self.wide_depths(widen_by)).count_increases()

    def count_increases(self) -> int:
        count = 0
        adjacentDepths = zip(self.depths[:-1], self.depths[1:])
        for first, second in adjacentDepths:
            if second > first:
                count += 1
        return count

    def wide_depths(self, widen_by: int):
        new_depths = []
        leftIndexMax = len(self.depths) - widen_by
        for leftIndex in range(leftIndexMax):
            rightIndex = leftIndex + 1 + widen_by
            sumBetween = sum(self.depths[leftIndex:rightIndex])
            new_depths.append(sumBetween)
        return new_depths


if __name__ == '__main__':
    assert part01('day01_example.txt') == 7
    assert part01('day01_input.txt') == 1215

    assert part02('day01_example.txt') == 5
    assert part02('day01_input.txt') == 1150
