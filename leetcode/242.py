def isAnagram(s: str, t: str) -> bool:
    return charCount(s) == charCount(t)

def charCount(s: str) -> {}:
    d = {}
    for char in s:
        if not char in d:
            d[char] = 1
        else:
            d[char] += 1
    return d

if __name__ == '__main__':
    assert True == isAnagram("anagram", "nagaram")
    assert False == isAnagram("rat", "car")