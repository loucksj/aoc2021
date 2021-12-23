from main import Reader


def part01(filename: str) -> int:
    linesAsInts = Reader(filename).getLinesAsInts()
    sonar = Sonar(linesAsInts)
    return sonar.countDepthIncreases()


def part02(filename: str) -> int:
    linesAsInts = Reader(filename).getLinesAsInts()
    sonar = Sonar(linesAsInts)
    sonar.widen(3)
    return sonar.countDepthIncreases()

class Sonar():
    def __init__(self, depths: list):
        self.depths = depths
    
    def countDepthIncreases(self) -> int:
        count = 0
        depthsAfterFirst = self.depths[1:]
        for i, depth in enumerate(depthsAfterFirst):
            if depth > self.depths[i]:
                count+=1
        return count

    def widen(self, width: int):
        wideDepths = []
        for end in range(width-1, len(self.depths)):
            start = end-width
            wideDepth = sum(self.depths[start:end])
            wideDepths.append(wideDepth)
        self.depths = wideDepths


if __name__ == '__main__':
    assert part01('day01input_example.txt') == 7
    assert part01('day01input.txt') == 1215

    assert part02('day01input_example.txt') == 5
    assert part02('day01input.txt') == 1150