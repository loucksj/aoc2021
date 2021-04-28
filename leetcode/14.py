def longestCommonPrefix(strs: list[str]) -> str:
    if len(strs) == 1:
        return strs[0]
    highest = ""
    for i in range(1, 201):
        common = True
        for j in range(1, len(strs)):
            if strs[0][0:i] != strs[j][0:i]:
                common = False
                break
        if common:
            highest = strs[0][0:i]
        else:
            break
    return highest

if __name__ == '__main__':
    assert "fl" == longestCommonPrefix(["flower","flow","flight"])
    assert "" == longestCommonPrefix(["dog","racecar","car"])
    assert "a" == longestCommonPrefix(["a"])
    assert "" == longestCommonPrefix(["reflower","flow","flight"])
    assert "flower" == longestCommonPrefix(["flower","flower","flower","flower"])
    assert "aa" == longestCommonPrefix(["aaa","aa","aaa"])