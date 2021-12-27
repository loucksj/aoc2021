from scripts.main import Reader, transpose


def part_one(filename: str) -> int:
    draws = [int(s) for s in Reader(filename).lines[0].split(',')]
    boards = make_boards(Reader(filename).lines[1:])
    winner, draw = winning_board_draw(boards, draws)
    return draw * winner.score()


def part_two(filename: str) -> int:
    draws = [int(s) for s in Reader(filename).lines[0].split(',')]
    boards = make_boards(Reader(filename).lines[1:])
    loser, draw = losing_board_draw(boards, draws)
    return draw * loser.score()


def make_boards(lines: list) -> list:
    boards = []
    for i, numbers in enumerate(lines):
        if numbers == '':  # blank line marks new board
            values = [[int(s) for s in line.split()]
                      for line in lines[i+1:i+6]]
            boards.append(Board(values))
    return boards


def winning_board_draw(boards: list, draws: list) -> tuple:
    for draw in draws:
        for board in boards:
            board.mark(draw)
            if board.is_winner():
                return board, draw


def losing_board_draw(boards: list, draws: list) -> tuple:
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

    def from_file(filename: str):
        return Reader(filename).lines

    def mark(self, draw: str):
        for row in self.rows:
            for index in range(0, len(row)):
                if row[index] == draw:
                    row[index] = -1

    def score(self) -> int:
        return sum([sum([n for n in row if n != -1]) for row in self.rows])

    def is_winner(self) -> bool:
        for line in self.rows + transpose(self.rows):
            if line.count(-1) == len(line):
                return True
        return False