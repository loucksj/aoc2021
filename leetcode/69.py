def mySqrt(x: int) -> int:
    return int(x**(1/2))

if __name__ == '__main__':
    assert 2 == mySqrt(4)
    assert 2 == mySqrt(8)
    assert 1 == mySqrt(1)
    assert 3 == mySqrt(9)
    assert 1 == mySqrt(2)