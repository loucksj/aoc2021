def reverse(x: int) -> int:
    neg = x < 0
    x = abs(x)
    n = 0
    while x != 0:
        n = 10 * n + (x % 10)
        x = x//10
    if neg:
        n *= -1
    if abs(n) < 2**31 and n != 2**31 - 1:
        return n
    return 0 # n outside signed 32-bit integer range

if __name__ == '__main__':
    assert 321 == reverse(123)
    assert -321 == reverse(-123)
    assert 21 == reverse(120)
    assert 0 == reverse(0)    
    assert 0 == reverse(1534236469)