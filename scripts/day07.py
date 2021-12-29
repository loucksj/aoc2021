from scripts.main import Reader


def part_one(filename: str) -> int:
    return Crabs(filename).cost()


def part_two(filename: str) -> int:
    return Crabs(filename).cumulative_cost()


class Crabs():
    def __init__(self, filename: str) -> None:
        positions = Reader(filename).split_firstline_ints(',')
        size = max(positions) + 1
        self.crabs = [[0]*size for _ in range(size)]
        self.crabs[0] = [positions.count(i) for i in range(len(self.crabs[0]))]

    def cost(self) -> int:
        fuel = 0
        start = 0
        end = len(self.crabs[0])-1
        while start != end:
            if self.crabs[0][start] == 0:
                start += 1
                continue
            if self.crabs[0][end] == 0:
                end -= 1
                continue
            if self.crabs[0][start] <= self.crabs[0][end]:
                fuel += self.crabs[0][start]
                self.crabs[0][start+1] += self.crabs[0][start]
                self.crabs[0][start] = 0
            else:
                fuel += self.crabs[0][end]
                self.crabs[0][end-1] += self.crabs[0][end]
                self.crabs[0][end] = 0
        return fuel

    def cumulative_cost(self) -> int:
        fuel = 0
        start = 0
        end = len(self.crabs[0])-1
        while start != end:
            startsum = 0
            endsum = 0
            i = 1
            for line in self.crabs:
                startsum += line[start]*i
                endsum += line[end]*i
                i += 1
            if startsum == 0:
                start += 1
                continue
            if endsum == 0:
                end -= 1
                continue
            if startsum <= endsum:
                fuel += startsum
                for i in range(0, len(self.crabs)-1):
                    self.crabs[i+1][start+1] += self.crabs[i][start]
                    self.crabs[i][start] = 0
            else:
                fuel += endsum
                for i in range(0, len(self.crabs)-1):
                    self.crabs[i+1][end-1] += self.crabs[i][end]
                    self.crabs[i][end] = 0
        return fuel
