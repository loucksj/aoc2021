from main import Reader


def part01(filename: str) -> int:
    sonar = Sonar(filename)
    increases = sonar.increaseCount(width=1)
    return increases


def part02(filename: str) -> int:
    sonar = Sonar(filename)
    increases = sonar.increaseCount(width=3)
    return increases


class Sonar():
    def __init__(self, filename: str):
        reader = Reader(filename)
        self.sweep = reader.getLinesAsInts()

    def increaseCount(self, width: int) -> int:
        count = 0
        index = 0
        current = 0
        previous = 0
        for line in self.sweep:
            current += line
            if index >= width:
                current -= self.sweep[index-width]
                if current > previous:
                    count += 1
            previous = current
            index += 1
        return count


if __name__ == '__main__':
    assert part01('day01input_example.txt') == 7
    assert part01('day01input.txt') == 1215

    assert part02('day01input_example.txt') == 5
    assert part02('day01input.txt') == 1150
