from scripts.main import Reader


def part_one(filename: str) -> int:
    return Crabs(filename).merge()


def part_two(filename: str) -> int:
    return Crabs(filename).merge_cumulative()


class Crabs():
    def __init__(self, filename: str) -> None:
        self.cost = 0
        crabs = Reader(filename).split_firstline_ints(',')
        size = max(crabs) + 1
        self.crabs = [[0]*size for _ in range(size)]
        for i in range(len(self.crabs)):
            self.crabs[i][0] = crabs.count(i)

    def merge(self) -> int:
        while len(self.crabs) > 1:
            self.move_next_crab(False)
        return self.cost

    def merge_cumulative(self) -> int:
        while len(self.crabs) > 1:
            self.move_next_crab(True)
        return self.cost

    def move_next_crab(self, cumulative=False) -> int:
        startcost, endcost = self.cost_at(0), self.cost_at(-1)
        at, to = (0, 1) if startcost < endcost else (-1, -2)
        self.cost += min(startcost, endcost)
        bump = 1 if cumulative else 0
        for i, crab in enumerate(self.crabs[at][:-1]):
            self.crabs[to][i + bump] += crab
        del self.crabs[at]

    def cost_at(self, index: int) -> int:
        return sum([(i + 1) * crab for i, crab in enumerate(self.crabs[index])])
