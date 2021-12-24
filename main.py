PATH = './inputs/'

class Reader:
    def __init__(self, filename: list):
        self.lines = open(PATH + filename, 'r').readlines()
    
    def strip_lines(self) -> list:
        return [s.strip() for s in self.lines]

    def split_lines(self, split_at: str):
        return [line.split(split_at) for line in self.strip_lines()]
    
    def split_str_int_pairs(self, split_at: str):
        return [[_, int(n)] for _, n in self.split_lines(split_at)]

    def int_lines(self) -> list:
        return [int(s) for s in self.strip_lines()]