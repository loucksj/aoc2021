from scripts.main import Reader, transpose


def part_one(filename: str) -> int:
    game = BingoGame().from_file(filename)
    winners, draw = game.winners_at()
    return draw * winners[0].score()


def part_two(filename: str) -> int:
    game = BingoGame().from_file(filename)
    loser, draw = game.loser_at()
    return draw * loser.score()


class BingoGame():
    def from_file(self, filename: str):
        self.draws = self.draws_from_file(filename)
        self.boards = self.boards_from_file(filename)
        return self

    def draws_from_file(self, filename: str) -> list:
        return [int(s) for s in Reader(filename).lines()[0].split(',')]

    def boards_from_file(self, filename: str) -> list:
        board_strings = Reader(filename).read().split('\n\n')[1:]
        boards = []
        for board in board_strings:
            matrix = []
            for line in board.split('\n'):
                matrix.append(list(map(int, line.split())))
            boards.append(Board(matrix))
        return boards

    def winners_at(self) -> tuple:
        for draw in self.draws:
            self.mark_all(draw)
            if len(self.winners()) > 0:
                return self.winners(), draw

    def winners(self):
        return [board for board in self.boards if board.is_winner()]

    def loser_at(self) -> tuple:
        last_draw = 0
        last_board = []
        for draw in self.draws:
            self.mark_all(draw)
            if len(self.winners()) > 0:
                last_board = self.winners()[-1]
                last_draw = draw
            self.remove_winners()
            if len(self.boards) == 0:
                break
        return last_board, last_draw

    def remove_winners(self):
        for board in self.boards:
            if board.is_winner():
                self.boards.remove(board)

    def mark_all(self, draw: int):
        for board in self.boards:
            board.mark(draw)


class Board:
    def __init__(self, rows: str):
        self.rows = rows

    def mark(self, draw: str):
        self.rows = [[-1 if draw == value else value for value in row]
                     for row in self.rows]

    def is_winner(self) -> bool:
        for line in self.rows + transpose(self.rows):
            if line.count(-1) == len(line):
                return True
        return False

    def score(self) -> int:
        return sum([sum([n for n in row if n != -1]) for row in self.rows])
