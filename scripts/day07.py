from scripts.main import Reader


def part_one(filename: str) -> int:
    return Crabs(filename).merge()


def part_two(filename: str) -> int:
    return Crabs(filename).cumulative_merge()


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
            if self.crabs[0][0] < self.crabs[-1][0]:
                self.cost += self.crabs[0][0]
                self.crabs[1][0] += self.crabs[0][0]
                del self.crabs[0]
            else:
                self.cost += self.crabs[-1][0]
                self.crabs[-2][0] += self.crabs[-1][0]
                del self.crabs[-1]
        return self.cost

    def cumulative_merge(self) -> int:
        while len(self.crabs) > 1:
            if self.cost_at_cumulative(0) < self.cost_at_cumulative(-1):
                self.cost += self.cost_at_cumulative(0)
                for i, crab in enumerate(self.crabs[0][:-1]):
                    self.crabs[1][i+1] += crab
                del self.crabs[0]
            else:
                self.cost += self.cost_at_cumulative(-1)
                for i, crab in enumerate(self.crabs[-1][:-1]):
                    self.crabs[-2][i+1] += crab
                del self.crabs[-1]
        return self.cost

    def cost_at_cumulative(self, index: int) -> int:
        fuel = 0
        for i, crab in enumerate(self.crabs[index]):
            fuel += (i+1) * crab
        return fuel
