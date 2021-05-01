def lengthOfLongestSubstring(s: str) -> int:
    d = {}
    left = 0
    count = 0
    longest = 0
    for i in range(0, len(s)):
        c = s[i]
        if c in d and d[c] >= left:
            count = count - (d[c] + 1 - left)
            left = d[c] + 1
        d[c] = i
        count += 1
        longest = max(count, longest)
    return longest

if __name__ == '__main__':
    assert 2 == lengthOfLongestSubstring("abba")
    assert 3 == lengthOfLongestSubstring("pwwkew")
    assert 2 == lengthOfLongestSubstring("aab")
    assert 3 == lengthOfLongestSubstring("abcabcbb")
    assert 1 == lengthOfLongestSubstring("bbbbb")
    assert 0 == lengthOfLongestSubstring("")