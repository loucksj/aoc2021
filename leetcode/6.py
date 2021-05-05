def convert(s: str, numRows: int) -> str:
    indexes = []

    # create first row
    space = max(1, 2 * numRows - 2) # distance between elements
    i = 0
    while i < len(s) + space:
        indexes.append(i)
        i += space

    # create other rows
    rows = 1
    while rows < numRows:
        indexes_copy = indexes
        for i in indexes_copy:
            h = i - 1
            if h > 0 and not h in indexes:
                indexes.append(h)
            j = i + 1
            if j < len(s) + space and not j in indexes:
                indexes.append(j)
        rows += 1
    
    # create solution from indexes
    solution = ""
    for i in indexes:
        if i < len(s):
            solution += s[i]
    
    return solution

if __name__ == '__main__':
    assert "PAHNAPLSIIGYIR" == convert("PAYPALISHIRING", 3)
    assert "PINALSIGYAHRPI" == convert("PAYPALISHIRING", 4)
    assert "A" == convert("A", 1)
    assert "ABDC" == convert("ABCD", 3)
    # assert "ABDC" == convert("hjouvsuyoypayulyeimuotehzriicfskpggkbbipzzrzucxamludfykgruowzgiooobppleqlwphapjnadqhdcnvwdtxjbmyppphauxnspusgdhiixqmbfjxjcvudjsuyibyebmwsiqyoygyxymzevypzvjegebeocfuftsxdixtigsieehkchzdflilrjqfnxztqrsvbspkyhsenbppkqtpddbuotbbqcwivrfxjujjddntgeiqvdgaijvwcyaubwewpjvygehljxepbpiwuqzdzubdubzvafspqpqwuzifwovyddwyvvburczmgyjgfdxvtnunneslsplwuiupfxlzbknhkwppanltcfirjcddsozoyvegurfwcsfmoxeqmrjowrghwlkobmeahkgccnaehhsveymqpxhlrnunyfdzrhbasjeuygafoubutpnimuwfjqsjxvkqdorxxvrwctdsneogvbpkxlpgdirbfcriqifpgynkrrefx", 503)