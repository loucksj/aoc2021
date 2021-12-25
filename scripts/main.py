PATH = './input/'


class Reader:
    def __init__(self, filename: str):
        self.lines = [s.strip() for s in open(PATH + filename, 'r').readlines()]

    def split_lines(self, at=' '):
        return [line.split(at) for line in self.lines]

    def str_int_pairs(self):
        return [[_, int(n)] for _, n in self.split_lines()]

    def integers(self) -> list:
        return [int(s) for s in self.lines]

    def matrix(self) -> list:
        return [list(line) for line in self.lines]