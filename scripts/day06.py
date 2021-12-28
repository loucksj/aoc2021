from scripts.main import Reader


def part_one(filename: str) -> int:
    return Fishes(filename).after_days(80)


def part_two(filename: str) -> int:
    return Fishes(filename).after_days(256)

class Fishes():
    def __init__(self, filename: str) -> None:
        fishes = Reader(filename).split_firstline_ints(',')
        self.fish = [fishes.count(i) for i in range(10)]

    def after_days(self, days: int) -> int:
        for _ in range(days):
            next_fish = [0]*9
            next_fish[8] = self.fish[0]
            next_fish[6] = self.fish[0]
            for i in range(1, 9):
                next_fish[i-1] += self.fish[i]
            self.fish = next_fish
        return sum(self.fish)
