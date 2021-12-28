PATH = './input/'


class Reader():
    def __init__(self, filename: str):
        self.filename = filename

    def read(self) -> str:
        file_ = open(PATH + self.filename, 'r')
        string = file_.read().strip()
        file_.close()
        return string

    def lines(self) -> list:
        return self.read().split('\n')

    def split_lines(self, at=' '):
        return [line.split(at) for line in self.lines()]
    
    def split_firstline_ints(self, at=' '):
        return [int(val) for val in self.lines()[0].split(at)]

    def str_int_pairs(self):
        return [[string, int(val)] for string, val in self.split_lines()]

    def integers(self) -> list:
        return [int(s) for s in self.lines()]

    def matrix(self) -> list:
        return [list(line) for line in self.lines()]


def transpose(matrix: list) -> list:
    return list(map(list, zip(*matrix)))
