def longestPalindrome(s: str) -> str:
    longest = -1
    length = 0
    for i in range(0, len(s)):
        odd = longest_mid_odd(s, i)
        even = longest_mid_even(s, i)
        if len(odd) > length:
            length = len(odd)
            longest = odd
        if len(even) > length:
            length = len(even)
            longest = even
    return longest

# longest odd-length palindrome from index of the middle element
def longest_mid_odd(s: str, i: int) -> str:
    pal = ""
    while True:
        left = i - int(len(pal)/2)
        right = i + int(len(pal)/2) + 1
        if left < 0 or right >= len(s):
            break
        if s[left] != s[right]:
            break
        pal = s[left] + pal + s[right]
    return pal

# longest even-length palindrome from index of the left element of middle pair
def longest_mid_even(s: str, i: int) -> str:
    pal = s[i]
    while True:
        left = i - int(len(pal)/2) - 1
        right = i + int(len(pal)/2) + 1
        if left < 0 or right >= len(s):
            break
        if s[left] != s[right]:
            break
        pal = s[left] + pal + s[right]
    return pal

if __name__ == '__main__':
    assert "bab" == longestPalindrome("babad") or "aba" == longestPalindrome("babad")
    assert "bb" == longestPalindrome("cbbd")
    assert "a" == longestPalindrome("a")
    assert "a" == longestPalindrome("ac") or "c" == longestPalindrome("ac")