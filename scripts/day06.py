from scripts.main import Reader


def part_one(filename: str) -> int:
    return Fishes(filename).after(80)


def part_two(filename: str) -> int:
    return Fishes(filename).after(256)

class Fishes():
    def __init__(self, filename: str) -> None:
        fishes = Reader(filename).split_firstline_ints(',')
        self.fish = [fishes.count(i) for i in range(10)]

    def after(self, days: int) -> int:
        for _ in range(days):
            self.next_day()
        return sum(self.fish)
    
    def next_day(self):
        fish = [0]*9
        fish[8] = self.fish[0]
        fish[6] = self.fish[0]
        for i in range(1, 9):
            fish[i-1] += self.fish[i]
        self.fish = fish
