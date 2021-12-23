from main import Reader


def part01(filename: str) -> int:
    sonar = Sonar.from_file(filename)
    return sonar.count_depth_increases()


def part02(filename: str) -> int:
    sonar = Sonar.from_file(filename)
    sonar.widen_by(2)
    return sonar.count_depth_increases()


class Sonar():
    def __init__(self, depths: list):
        self.depths = depths
    
    @classmethod
    def from_file(cls, filename: str):
        linesAsInts = Reader(filename).getLinesAsInts()
        return cls(linesAsInts)

    def count_depth_increases(self) -> int:
        count = 0
        adjacentDepths = zip(self.depths[:-1], self.depths[1:])
        for first, second in adjacentDepths:
            if second > first:
                count += 1
        return count

    def widen_by(self, widenBy: int):
        newDepths = []
        leftIndexMax = len(self.depths) - widenBy
        for leftIndex in range(leftIndexMax):
            rightIndex = leftIndex + 1 + widenBy
            sumBetween = sum(self.depths[leftIndex:rightIndex])
            newDepths.append(sumBetween)
        self.depths = newDepths


if __name__ == '__main__':
    assert part01('day01_example.txt') == 7
    assert part01('day01_input.txt') == 1215

    assert part02('day01_example.txt') == 5
    assert part02('day01_input.txt') == 1150
