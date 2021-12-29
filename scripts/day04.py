from scripts.main import Reader, transpose


def part_one(filename: str) -> int:
    return BingoGame(filename).winners[0].score()


def part_two(filename: str) -> int:
    return BingoGame(filename).winners[-1].score()


class BingoGame():
    def __init__(self, filename: str) -> None:
        self.draws = Reader(filename).split_first_ints(',')
        self.active = self.get_boards_from_file(filename)
        self.winners = []
        self.run()

    def get_boards_from_file(self, filename: str) -> list:
        return [self.board_from_string(board_str) for board_str in Reader(filename).read().split('\n\n')[1:]]

    def board_from_string(self, string: str):
        return Board([list(map(int, line.split())) for line in string.split('\n')])

    def run(self):
        while len(self.active) > 0 and len(self.draws) > 0:
            self.mark_boards(self.draws.pop(0))

    def mark_boards(self, draw: int):
        for board in self.active.copy():
            board.mark(draw)
            if board.is_winner():
                self.active.remove(board)
                self.winners.append(board)


class Board:
    def __init__(self, matrix: str):
        self.numbers = matrix
        self.won_on = -1

    def mark(self, draw: str):
        self.numbers = [[-1 if draw == num else num for num in row]
                        for row in self.numbers]
        if not self.is_winner() and self.win_check():
            self.won_on = draw

    def win_check(self):
        for line in self.numbers + transpose(self.numbers):
            if line.count(-1) == len(line):
                return True

    def is_winner(self) -> bool:
        return self.won_on > 0

    def score(self) -> int:
        board = sum([sum([n for n in row if n != -1]) for row in self.numbers])
        return board * self.won_on
