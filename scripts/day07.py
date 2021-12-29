from scripts.main import Reader


def part_one(filename: str) -> int:
    return Crabs(filename).cost()


def part_two(filename: str) -> int:
    return Crabs(filename).cumulative_cost()


class Crabs():
    def __init__(self, filename: str) -> None:
        self.positions = Reader(filename).split_firstline_ints(',')
        self.crabs = [0]*(max(self.positions) + 1)
        for p in self.positions:
            self.crabs[p] += 1

    def cost(self) -> int:
        fuel = 0
        start = 0
        end = len(self.crabs)-1
        while start != end:
            if self.crabs[start] == 0:
                start += 1
                continue
            if self.crabs[end] == 0:
                end -= 1
                continue
            if self.crabs[start] <= self.crabs[end]:
                fuel += self.crabs[start]
                self.crabs[start+1] += self.crabs[start]
                self.crabs[start] = 0
            else:
                fuel += self.crabs[end]
                self.crabs[end-1] += self.crabs[end]
                self.crabs[end] = 0
        return fuel

    def cumulative_cost(self) -> int:
        size = max(self.positions)+1
        crabs = [[0]*size]
        for _ in range(1, size):
            crabs.append([0]*size)
        for p in self.positions:
            crabs[0][p] += 1
        fuel = 0
        start = 0
        end = len(crabs[0])-1
        while start != end:
            startsum = 0
            endsum = 0
            i = 1
            for line in crabs:
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
                for i in range(0, len(crabs)-1):
                    crabs[i+1][start+1] += crabs[i][start]
                    crabs[i][start] = 0
            else:
                fuel += endsum
                for i in range(0, len(crabs)-1):
                    crabs[i+1][end-1] += crabs[i][end]
                    crabs[i][end] = 0
        return fuel
