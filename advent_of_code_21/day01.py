from main import Reader


def part01(filename: str) -> int:
    return count_greaterthan_prev(Reader(filename).int_lines())


def part02(filename: str) -> int:
    return count_greaterthan_prev(add_neighbors(Reader(filename).int_lines(), 2))


def count_greaterthan_prev(values: list):
    return sum(1 for first, second in zip(values[:-1], values[1:]) if second > first)


def add_neighbors(values: list, neighbors: int) -> list:
    return [sum(values[i:i+1+neighbors]) for i in range(len(values)-neighbors)]


if __name__ == '__main__':
    assert part01('day01_example.txt') == 7
    assert part01('day01_input.txt') == 1215

    assert part02('day01_example.txt') == 5
    assert part02('day01_input.txt') == 1150
