from scripts.main import Reader


def part_one(filename: str) -> int:
    return Caves(filename).count_paths()


def part_two(filename: str) -> int:
    return Caves(filename).count_paths(True)


class Caves:
    def __init__(self, filename: str):
        self.caves = []
        for line in Reader(filename).split_lines('-'):
            self.add_connection(line[0], line[1])

    class Cave:
        def __init__(self, name: str):
            self.name = name
            self.caves = []
            self.is_big = True if self.name.isupper() else False

    def count_paths(self, boost=False, cave=[], path=[]) -> int:
        if cave == []:
            cave = self.get_cave("start")
        if cave == self.get_cave("end"):
            return 1
        count = 0
        path.append(cave.name)
        for to_cave in cave.caves:
            if to_cave == self.get_cave("start"):
                continue
            if to_cave.name in path and not to_cave.is_big and boost:
                count += self.count_paths(False, to_cave, path.copy())
            if to_cave.name not in path or to_cave.is_big:
                count += self.count_paths(boost, to_cave, path.copy())
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
