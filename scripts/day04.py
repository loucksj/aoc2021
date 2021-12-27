from scripts.main import Reader, transpose


def part_one(filename: str) -> int:
    return BingoGame(filename).winners[0].score()


def part_two(filename: str) -> int:
    return BingoGame(filename).winners[-1].score()


class BingoGame():
    def __init__(self, filename: str) -> None:
        self.draws = self.get_draws_from_file(filename)
        self.boards = self.get_boards_from_file(filename)
        self.drawn = []
        self.winners = []
        self.run()

    def get_draws_from_file(self, filename: str) -> list:
        return [int(val) for val in Reader(filename).lines()[0].split(',')]

    def get_boards_from_file(self, filename: str) -> list:
        return [self.board_from_string(board_str) for board_str in Reader(filename).read().split('\n\n')[1:]]

    def board_from_string(self, string: str):
        return Board([list(map(int, line.split())) for line in string.split('\n')])

    def run(self):
        while len(self.boards) > 0 and len(self.draws) > 0:
            self.drawn.append(self.draws.pop(0))
            self.mark_last_drawn()
            self.remove_winners()

    def mark_last_drawn(self):
        for board in self.boards:
            board.mark(self.drawn[-1])
            if board.is_winner():
                self.winners.append(board)

    def remove_winners(self):
        for board in self.boards:
            if board.is_winner():
                self.boards.remove(board)


class Board:
    def __init__(self, rows: str):
        self.rows = rows
        self.won_on = -1

    def mark(self, draw: str):
        self.rows = [[-1 if draw == value else value for value in row]
                     for row in self.rows]
        if self.is_winner():
            self.won_on = draw

    def is_winner(self) -> bool:
        if self.won_on > 0:
            return True
        for line in self.rows + transpose(self.rows):
            if line.count(-1) == len(line):
                return True
        return False

    def score(self) -> int:
        board = sum([sum([n for n in row if n != -1]) for row in self.rows])
        return board * self.won_on
