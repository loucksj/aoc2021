def romanToInt(s: str) -> int:
    symbols = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000,
    }

    s = list(s)

    sum = 0

    i = 0
    while i < len(s): #skip last
        a = s[i]
        
        if i == len(s)-1:
            sum += symbols[a]
            break
        
        b = s[i+1]
        
        if a == "I":
            if b == "V":
                sum += 4
                i += 2
                continue
            if b == "X":
                sum += 9
                i += 2
                continue
        elif a == "X":
            if b == "L":
                sum += 40
                i += 2
                continue
            if b == "C":
                sum += 90
                i += 2
                continue
        elif a == "C":
            if b == "D":
                sum += 400
                i += 2
                continue
            if b == "M":
                sum += 900
                i += 2
                continue
        sum += symbols[a]
        i += 1
    return sum

if __name__ == '__main__':
    assert 3 == romanToInt("III")
    assert 4 == romanToInt("IV")
    assert 9 == romanToInt("IX")
    assert 58 == romanToInt("LVIII")
    assert 1994 == romanToInt("MCMXCIV")
    assert 1695 == romanToInt("MDCXCV")