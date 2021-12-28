from scripts.main import Reader


def part_one(filename: str) -> int:
    return Fishes(filename).after(80)


def part_two(filename: str) -> int:
    return Fishes(filename).after(256)


class Fishes():
    def __init__(self, filename: str) -> None:
        fishes = Reader(filename).split_firstline_ints(',')
        self.fish = [fishes.count(i) for i in range(9)]

    def after(self, days: int) -> int:
        for _ in range(days):
            self.next_day()
        return sum(self.fish)

    def next_day(self):
        birth = self.fish.pop(0)
        self.fish.append(birth)
        self.fish[6] += birth
