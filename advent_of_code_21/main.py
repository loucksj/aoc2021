class Reader:
    def __init__(self, filename: list):
        self.lines = open(filename, 'r').readlines()
    
    def getLinesStripped(self) -> list:
        linesStripped = [s.strip() for s in self.lines]
        return linesStripped

    def getLinesSplit(self, at: str):
        return [line.split(at) for line in self.getLinesStripped()]

    def getLinesAsInts(self) -> list:
        linesStripped = [int(s.strip()) for s in self.lines]
        return linesStripped