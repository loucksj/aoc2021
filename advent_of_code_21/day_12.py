def part_1(file: str) -> int:
    lines = open(file, 'r').readlines()
    lines = [s.strip() for s in lines]
    lines = [s.split('-') for s in lines]

    caves = Caves()
    for line in lines:
        caves.add(line[0], line[1])
    
    paths = caves.explore(caves.start())

    return paths

def part_2(file: str) -> int:
    lines = open(file, 'r').readlines()
    lines = [s.strip() for s in lines]
    lines = [s.split('-') for s in lines]

    caves = Caves()
    for line in lines:
        caves.add(line[0], line[1])
    
    paths = caves.delve(caves.start())

    return paths

class Cave:
    def __init__(self, name: str):
        self.name = name
        self.caves = []
        self.small = True
        if self.name.isupper():
            self.small = False
            
class Caves:
    def __init__(self):
        self.caves = []
    
    def start(self) -> Cave:
        for cave in self.caves:
            if cave.name == "start":
                return cave

    def end(self) -> Cave:
        for cave in self.caves:
            if cave.name == "end":
                return cave
    
    def explore(self, cave: Cave, path=[]) -> int:
        path.append(cave.name)
        if cave == self.end():
            return 1
        count = 0
        for c in cave.caves:
            if c.name not in path or not c.small:
                count += self.explore(c, path.copy())
        return count
    
    def delve(self, cave: Cave, path=[], boost=True) -> int:
        path.append(cave.name)
        if cave == self.end():
            return 1
        count = 0
        for c in cave.caves:
            if c == self.start():
                continue
            if c.name in path and c.small and boost:
                count += self.delve(c, path.copy(), False)
            if c.name not in path or not c.small:
                count += self.delve(c, path.copy(), boost)
        return count

    def add(self, start: str, end: str):
        start_cave = Cave(start)
        end_cave = Cave(end)
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

if __name__ == '__main__':
    assert part_1('day_12_short.txt') == 10
    assert part_1('day_12_test.txt') == 19
    assert part_1('day_12_long.txt') == 226
    assert part_1('day_12.txt') == 4691

    assert part_2('day_12_short.txt') == 36
    assert part_2('day_12_test.txt') == 103
    assert part_2('day_12_long.txt') == 3509
    assert part_2('day_12.txt') == 140718