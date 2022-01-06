from src.scripts.main import Reader


def part_one(filename: str) -> int:
    return Crabs(filename).merge().spent_fuel


def part_two(filename: str) -> int:
    return Crabs(filename).merge(True).spent_fuel


class Crabs():
    def __init__(self, filename: str) -> None:
        self.crabs = self.make_crabs(Reader(filename).split_first_ints(','))
        self.spent_fuel = 0

    def make_crabs(self, positions: list) -> list:
        return [[positions.count(i)] for i in range(max(positions)+1)]

    def merge(self, cumulative=False) -> int:
        bump = 1 if cumulative else 0
        while len(self.crabs) > 1:
            at, to = (0, 1) if self.cost_at(0) < self.cost_at(-1) else (-1, -2)
            self.spent_fuel += self.cost_at(at)
            self.move_crabs(at, to, bump)
        return self

    def move_crabs(self, at: int, to: int, bump: int):
        for i, crab in enumerate(self.crabs[at]):
            if i + bump < len(self.crabs[to]):
                self.crabs[to][i + bump] += crab
            else:
                self.crabs[to].append(crab)
        del self.crabs[at]

    def cost_at(self, index: int) -> int:
        return sum([(i + 1) * crab for i, crab in enumerate(self.crabs[index])])
