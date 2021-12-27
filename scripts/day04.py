from scripts.main import Reader


def part_one(filename: str) -> int:
    draws = Reader(filename).lines[0].split(',')
    boards = make_boards(Reader(filename).lines[2:])
    winner, draw = winning_board_draw(boards, draws)
    return int(draw) * winner.score()


def part_two(filename: str) -> int:
    draws = Reader(filename).lines[0].split(',')
    boards = make_boards(Reader(filename).lines[2:])
    loser, draw = losing_board_draw(boards, draws)
    return int(draw) * loser.score()


def make_boards(lines: list) -> list:
    boards = []
    line_index = 0
    for line in lines:
        if line == '':
            boards.append(Board(lines[line_index+1:line_index+6]))
        line_index += 1
    return boards


def winning_board_draw(boards: list, draws: list) -> tuple:
    for draw in draws:
        for board in boards:
            board.mark(draw)
            if board.winner():
                return board, draw


def losing_board_draw(boards: list, draws: list) -> tuple:
    last_num = 0
    last_winner = []
    for num in draws:
        for board in boards:
            board.mark(num)
        for board in boards:
            if board.winner():
                last_num = num
                last_winner = board
                boards.remove(board)
    return last_winner, last_num

class Board:
    def __init__(self, data: str):
        self.rows = []
        row = 0
        for line in data:
            self.rows.append([])
            for num in line.split():
                self.rows[row].append(num)
            row += 1

    def from_file(filename: str):
        return Reader(filename).lines

    def mark(self, target: str):
        for row in self.rows:
            for index in range(0, len(row)):
                if row[index] == target:
                    row[index] = 'X'

    def score(self) -> int:
        score = 0
        for row in self.rows:
            for num in row:
                if num != 'X':
                    score += int(num)
        return score

    def winner(self) -> bool:
        for row in self.rows:
            if row.count('X') == 5:
                return True
        columns = [list(i) for i in zip(*self.rows)]
        for column in columns:
            if column.count('X') == 5:
                return True
        return False