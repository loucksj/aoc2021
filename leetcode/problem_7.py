def reverse(x: int) -> int:
    neg = x < 0
    x = abs(x)
    n = 0
    i = 0
    while x != 0:
        n = 10 * n + (x % 10)
        x = x//10
        i += 1
    if neg :
        n *= -1
    if abs(n) < 2**31 and n != 2**31 - 1:
        return n
    return 0 # n outside signed 32-bit integer range