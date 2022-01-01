from scripts.main import Reader


def part_one(filename: str) -> int:
    return Caves(filename).explore()


def part_two(filename: str) -> int:
    return Caves(filename).delve()


class Caves:
    def __init__(self, filename: str):
        self.caves = []
        lines = Reader(filename).split_lines('-')
        for line in lines:
            self.add(line[0], line[1])

    class Cave:
        def __init__(self, name: str):
            self.name = name
            self.caves = []
            self.is_big = True if self.name.isupper() else False

    def start(self) -> Cave:
        for cave in self.caves:
            if cave.name == "start":
                return cave

    def end(self) -> Cave:
        for cave in self.caves:
            if cave.name == "end":
                return cave

    def explore(self, cave=[], path=[]) -> int:
        if cave == []:
            cave = self.start()
        path.append(cave.name)
        if cave == self.end():
            return 1
        count = 0
        for c in cave.caves:
            if c.name not in path or c.is_big:
                count += self.explore(c, path.copy())
        return count

    def delve(self, cave=[], path=[], boost=True) -> int:
        if cave == []:
            cave = self.start()
        path.append(cave.name)
        if cave == self.end():
            return 1
        count = 0
        for c in cave.caves:
            if c == self.start():
                continue
            if c.name in path and not c.is_big and boost:
                count += self.delve(c, path.copy(), False)
            if c.name not in path or c.is_big:
                count += self.delve(c, path.copy(), boost)
        return count

    def add(self, start: str, end: str):
        start_cave = self.Cave(start)
        end_cave = self.Cave(end)
        new_start = True
        new_end = True
        for node in self.caves:
            if node.name == start:
                start_cave = node
                new_start = False
                break
        for node in self.caves:
            if node.name == end:
                end_cave = node
                new_end = False
                continue
        start_cave.caves.append(end_cave)
        end_cave.caves.append(start_cave)
        if new_start:
            self.caves.append(start_cave)
        if new_end:
            self.caves.append(end_cave)
