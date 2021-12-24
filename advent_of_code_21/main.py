class Reader:
    def __init__(self, filename: list):
        self.lines = open(filename, 'r').readlines()
    
    def get_lines_stripped(self) -> list:
        return [s.strip() for s in self.lines]

    def get_lines_split(self, split_at: str):
        return [line.split(split_at) for line in self.get_lines_stripped()]
    
    def get_lines_split_str_int(self, split_at: str):
        return [[_, int(n)] for _, n in self.get_lines_split(split_at)]

    def get_lines_ints(self) -> list:
        return [int(s) for s in self.get_lines_stripped()]