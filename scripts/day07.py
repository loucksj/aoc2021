from scripts.main import Reader


def part_one(filename: str) -> int:
    return Crabs(filename).merge()


def part_two(filename: str) -> int:
    return Crabs(filename).merge(True)


class Crabs():
    def __init__(self, filename: str) -> None:
        self.crabs = self.make_crabs(Reader(filename).split_firstline_ints(','))
        self.spent_fuel = 0

    def make_crabs(self, positions: list) -> list:
        size = max(positions) + 1
        crabs = [[0]*size for _ in range(size)]
        for i in range(len(crabs)):
            crabs[i][0] = positions.count(i)
        return crabs

    def merge(self, cumulative=False) -> int:
        while len(self.crabs) > 1:
            self.move_next_crab(cumulative)
        return self.spent_fuel

    def move_next_crab(self, cumulative=False) -> int:
        bump = 1 if cumulative else 0
        startcost, endcost = self.cost_at(0), self.cost_at(-1)
        at, to = (0, 1) if startcost < endcost else (-1, -2)
        self.spent_fuel += min(startcost, endcost)
        for i, val in enumerate(self.crabs[at][:-1]):
            self.crabs[to][i + bump] += val
        del self.crabs[at]

    def cost_at(self, index: int) -> int:
        return sum([(i + 1) * crab for i, crab in enumerate(self.crabs[index])])
