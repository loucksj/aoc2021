def part_1(file: str) -> int:
    lines = open(file, 'r').readlines()
    nums = lines.pop(0).strip().split(',')
    lines = [s.strip() for s in lines]

    boards = []
    line_index = 0
    for line in lines:
        if line == '':
            boards.append(Board(lines[line_index+1:line_index+6]))
        line_index += 1

    last_num = 0
    winner = []
    for num in nums:
        last_num = num
        for board in boards:
            board.mark(num)
        winner = get_winner(boards)
        if winner != []:
            break

    return int(last_num) * winner.score()

def get_winner(boards: list):
    winner = []
    for board in boards:
        for row in board.rows:
            if row.count('X') == 5:
                winner = board
                break
        columns = [list(i) for i in zip(*board.rows)]
        for column in columns:
            if column.count('X') == 5:
                winner = board
                break
    return winner

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

if __name__ == '__main__':
    assert part_1('day_4_test.txt') == 4512
    assert part_1('day_4.txt') == 87456

    #assert part_2('day_4_test.txt') == 0
    #assert part_2('day_4.txt') == 0