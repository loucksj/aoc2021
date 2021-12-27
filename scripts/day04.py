from scripts.main import Reader, transpose


def part_one(filename: str) -> int:
    draws = draws_from_file(filename)
    boards = boards_from_file(filename)
    winner, draw = winner_at(boards, draws)
    return draw * winner.score()


def part_two(filename: str) -> int:
    draws = draws_from_file(filename)
    boards = boards_from_file(filename)
    loser, draw = loser_at(boards, draws)
    return draw * loser.score()


def draws_from_file(filename: str) -> list:
    return [int(s) for s in Reader(filename).lines()[0].split(',')]


def boards_from_file(filename: str) -> list:
    str_boards = Reader(filename).read().split('\n\n')[1:]
    int_boards = [[map(int, line.split())
                   for line in board.split('\n')] for board in str_boards]
    return [Board(board) for board in int_boards]


def winner_at(boards: list, draws: list) -> tuple:
    for draw in draws:
        for board in boards:
            board.mark(draw)
            if board.is_winner():
                return board, draw


def loser_at(boards: list, draws: list) -> tuple:
    last_draw = 0
    last_winner = []
    for num in draws:
        if len(boards) == 0:
            break
        for board in boards:
            board.mark(num)
        for board in boards:
            if board.is_winner():
                last_draw = num
                last_winner = board
                boards.remove(board)
    return last_winner, last_draw


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
