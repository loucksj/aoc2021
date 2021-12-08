def part_1(file: str) -> int:
    lines = open(file, 'r').readlines()
    nums = lines.pop(0).strip().split(',')
    lines = [s.strip() for s in lines]

    boards = make_boards(lines)

    for num in nums:
        for board in boards:
            board.mark(num)
            if board.winner():
                return int(num) * board.score()
    return -1

def part_2(file: str) -> int:
    lines = open(file, 'r').readlines()
    nums = lines.pop(0).strip().split(',')
    lines = [s.strip() for s in lines]

    boards = make_boards(lines)

    last_num = 0
    last_winner = []
    for num in nums:
        for board in boards:
            board.mark(num)
        for board in boards:
            if board.winner():
                last_num = num
                last_winner = board
                boards.remove(board)
    return int(last_num) * last_winner.score()

def make_boards(lines: list) -> list:
    boards = []
    line_index = 0
    for line in lines:
        if line == '':
            boards.append(Board(lines[line_index+1:line_index+6]))
        line_index += 1
    return boards

class Board:
    def __init__(self, data: str):
        self.rows = []
        row = 0
        for line in data:
            self.rows.append([])
            for num in line.split():
                self.rows[row].append(num)
            row += 1
    
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

if __name__ == '__main__':
    assert part_1('day_4_test.txt') == 4512
    assert part_1('day_4.txt') == 87456

    assert part_2('day_4_test.txt') == 1924
    assert part_2('day_4.txt') == 15561