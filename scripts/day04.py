from scripts.main import Reader, transpose


def part_one(filename: str) -> int:
    first_winner, on_draw = BingoGame().from_file(filename).run().winners[0]
    return first_winner.score() * on_draw


def part_two(filename: str) -> int:
    last_winner, on_draw = BingoGame().from_file(filename).run().winners[-1]
    return last_winner.score() * on_draw


class BingoGame():
    def __init__(self) -> None:
        self.draws = []
        self.drawn = []
        self.boards = []
        self.winners = []

    def from_file(self, filename: str):
        self.add_draws_from_file(filename)
        self.add_boards_from_file(filename)
        return self

    def add_boards_from_file(self, filename: str) -> list:
        for board_str in Reader(filename).read().split('\n\n')[1:]:
            matrix = []
            for line in board_str.split('\n'):
                integers = list(map(int, line.split()))
                matrix.append(integers)
            self.boards.append(Board(matrix))

    def add_draws_from_file(self, filename: str) -> list:
        for val in Reader(filename).lines()[0].split(','):
            self.draws.append(int(val))

    def run(self):
        while len(self.boards) > 0 and len(self.draws) > 0:
            self.drawn.append(self.draws.pop(0))
            self.mark_last_drawn()
            self.remove_winners()
        return self

    def mark_last_drawn(self):
        for board in self.boards:
            board.mark(self.drawn[-1])
            if board.is_winner():
                self.winners.append((board, self.drawn[-1]))

    def remove_winners(self):
        for board in self.boards:
            if board.is_winner():
                self.boards.remove(board)


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
