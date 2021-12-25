from scripts.get_input import int_lines


def part_one(filename: str) -> int:
    return count_greaterthan_prev(int_lines(filename))


def part_two(filename: str) -> int:
    return count_greaterthan_prev(add_neighbors(int_lines(filename), 2))


def count_greaterthan_prev(values: list):
    return sum(1 for first, second in zip(values[:-1], values[1:]) if second > first)


def add_neighbors(values: list, neighbors: int) -> list:
    return [sum(values[i:i+1+neighbors]) for i in range(len(values)-neighbors)]