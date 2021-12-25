PATH = './input/'


class Reader:
    def __init__(self, filename: str):
        self.lines = [s.strip() for s in open(PATH + filename, 'r').readlines()]

    def split_lines(self, at=' '):
        return [line.split(at) for line in self.lines]

    def split_str_int_pairs(self):
        return [[_, int(n)] for _, n in self.split_lines()]

    def int_lines(self) -> list:
        return [int(s) for s in self.lines]

    def char_lines(self) -> list:
        return [list(line) for line in self.lines]


class Tools:
    def transpose(matrix: list):
        return [list(x) for x in zip(*matrix)]
