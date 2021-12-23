from main import Reader


def part01(filename: str) -> int:
    sonar = Sonar.fromFilename(filename)
    return sonar.countDepthIncreases()


def part02(filename: str) -> int:
    sonar = Sonar.fromFilename(filename)
    sonar.widenBy(2)
    return sonar.countDepthIncreases()


class Sonar():
    def __init__(self, depths: list):
        self.depths = depths
    
    @classmethod
    def fromFilename(cls, filename: str):
        linesAsInts = Reader(filename).getLinesAsInts()
        return cls(linesAsInts)

    def countDepthIncreases(self) -> int:
        count = 0
        adjacentDepths = zip(self.depths[:-1], self.depths[1:])
        for first, second in adjacentDepths:
            if second > first:
                count += 1
        return count

    def widenBy(self, widenBy: int):
        newDepths = []
        leftIndexMax = len(self.depths) - widenBy
        for leftIndex in range(leftIndexMax):
            rightIndex = leftIndex + 1 + widenBy
            sumBetween = sum(self.depths[leftIndex:rightIndex])
            newDepths.append(sumBetween)
        self.depths = newDepths


if __name__ == '__main__':
    assert part01('day01input_example.txt') == 7
    assert part01('day01input.txt') == 1215

    assert part02('day01input_example.txt') == 5
    assert part02('day01input.txt') == 1150
