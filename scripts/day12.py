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
            self.add_connection(line[0], line[1])
        self.start = self.start()
        self.end = self.end()

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
            cave = self.start
        path.append(cave.name)
        if cave == self.end:
            return 1
        count = 0
        for c in cave.caves:
            if c.name not in path or c.is_big:
                count += self.explore(c, path.copy())
        return count

    def delve(self, cave=[], path=[], boost=True) -> int:
        if cave == []:
            cave = self.start
        path.append(cave.name)
        if cave == self.end:
            return 1
        count = 0
        for c in cave.caves:
            if c == self.start:
                continue
            if c.name in path and not c.is_big and boost:
                count += self.delve(c, path.copy(), False)
            if c.name not in path or c.is_big:
                count += self.delve(c, path.copy(), boost)
        return count

    def add_connection(self, from_name: str, to_name: str):
        from_cave = self.get_cave(from_name)
        to_cave = self.get_cave(to_name)
        from_cave.caves.append(to_cave)
        to_cave.caves.append(from_cave)
        if self.is_cave(from_name):
            self.caves.append(from_cave)
        if self.is_cave(to_name):
            self.caves.append(to_cave)

    def get_cave(self, name: str):
        for cave in self.caves:
            if cave.name == name:
                return cave
        return self.Cave(name)

    def is_cave(self, name: str):
        for cave in self.caves:
            if cave.name == name:
                return cave
        return self.Cave(name)