class Reader:
    def __init__(self, filename: list):
        self.lines = open(filename, 'r').readlines()
    
    def getLinesStripped(self) -> list:
        linesStripped = [s.strip() for s in self.lines]
        return linesStripped