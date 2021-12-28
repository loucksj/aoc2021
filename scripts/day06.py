from scripts.main import Reader


def part_one(filename: str) -> int:
    return fish_after_days(get_fish_from_file(filename), 80)


def part_two(filename: str) -> int:
    return fish_after_days(get_fish_from_file(filename), 256)


def fish_after_days(fish: list, days: int) -> int:
    for _ in range(days):
        next_fish = [0]*9
        next_fish[8] = fish[0]
        next_fish[6] = fish[0]
        for i in range(1, 9):
            next_fish[i-1] += fish[i]
        fish = next_fish
    return sum(fish)


def get_fish_from_file(filename: str) -> list:
    fishes = Reader(filename).split_firstline_ints(',')
    return [fishes.count(i) for i in range(10)]
