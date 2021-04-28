def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    mut_x = x
    n = 0
    i = 0
    while mut_x != 0:
        n = 10 * n + (mut_x % 10)
        mut_x = mut_x//10
        i += 1
    return n == x

if __name__ == '__main__':
    assert True == isPalindrome(121)
    assert False == isPalindrome(-121)
    assert False == isPalindrome(10)
    assert False == isPalindrome(-101)
    assert False == isPalindrome(1000021)