from src.scripts.main import Reader


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

    def count_paths(self, boost=False, cave=[], visited=[]) -> int:
        if cave == []:
            cave = self.get_cave('start')
        if cave.name == 'end':
            return 1
        count = 0
        visited.append(cave)
        for to_cave in cave.caves:
            if to_cave.name == 'start':
                continue
            if to_cave in visited and not to_cave.is_big and boost:
                count += self.count_paths(False, to_cave, visited.copy())
            if to_cave not in visited or to_cave.is_big:
                count += self.count_paths(boost, to_cave, visited.copy())
        return count

    def add_connection(self, from_name: str, to_name: str):
        from_cave = self.get_cave(from_name)
        to_cave = self.get_cave(to_name)
        from_cave.caves.append(to_cave)
        to_cave.caves.append(from_cave)

    def get_cave(self, name: str):
        for cave in self.caves:
            if cave.name == name:
                return cave
        new_cave = self.Cave(name)
        self.caves.append(new_cave)
        return new_cave
