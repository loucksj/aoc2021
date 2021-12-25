from scripts.input_manager import strip_lines

def part_one(filename: str) -> int:
    lines = strip_lines(filename)

    fish = list(map(int, lines[0].split(',')))

    for _ in range(0, 80): #80 days
        count = len(fish)
        for i in range(0, count):
            if fish[i] == 0:
                fish[i] = 6
                fish.append(8)
            else:
                fish[i] -= 1

    return len(fish)

def part_two(filename: str) -> int:
    lines = strip_lines(filename)
    
    fish = list(map(int, lines[0].split(',')))

    today = [0]*9
    for i in range(0, 9):
        for f in fish:
            if f == i:
                today[i] += 1

    for _ in range(0, 256):
        tomor = [0]*9
        for i in range(0, 9):
            if i == 0:
                tomor[8] = today[i]
                tomor[6] = today[i]
            else:
                tomor[i-1] += today[i]
        today = tomor

    return sum(today)