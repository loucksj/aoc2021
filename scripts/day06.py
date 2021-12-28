from scripts.main import Reader


def part_one(filename: str) -> int:
    return final_total(get_fish_from_file(filename), 80)


def part_two(filename: str) -> int:
    return final_total(get_fish_from_file(filename), 256)


def final_total(fish: list, days: int) -> int:
    for _ in range(0, days):
        fish_next = [0]*9
        for i in range(0, 9):
            if i == 0:
                fish_next[8] = fish[i]
                fish_next[6] = fish[i]
            else:
                fish_next[i-1] += fish[i]
        fish = fish_next
    return sum(fish)


def get_fish_from_file(filename: str) -> list:
    fishes = Reader(filename).split_firstline_ints(',')
    return [fishes.count(i) for i in range(10)]
