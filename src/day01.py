from src.main import Reader


def part_one(filename: str) -> int:
    return count_greaterthan_prev(Reader(filename).integers())


def part_two(filename: str) -> int:
    return count_greaterthan_prev(add_neighbors(Reader(filename).integers(), 2))


def count_greaterthan_prev(values: list):
    return sum(1 for first, second in zip(values[:-1], values[1:]) if second > first)


def add_neighbors(values: list, neighbors: int) -> list:
    return [sum(values[i:i + 1 + neighbors]) for i in range(len(values) - neighbors)]
