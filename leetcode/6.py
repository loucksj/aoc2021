def convert(s: str, numRows: int) -> str:
    grid = []
    for n in range(0, numRows):
        grid.append([])
    
    row = 0
    down = True
    for i in range(0, len(s)):
        grid[row].append(s[i])
        if down and row < numRows - 1: 
            # go down
            row += 1
        elif down and row == numRows - 1:
            # at bottom, go up
            down = False
            row -= 1
        elif not down and row > 0:
            # go up
            row -= 1
        elif not down and row == 0:
            # at top, go down
            down = True
            row += 1
    
    # create solution from indexes
    solution = ""
    for row in grid:
        for c in row:
            solution += c
    
    return solution

if __name__ == '__main__':
    assert "PAHNAPLSIIGYIR" == convert("PAYPALISHIRING", 3)
    assert "PINALSIGYAHRPI" == convert("PAYPALISHIRING", 4)
    assert "A" == convert("A", 1)
    assert "ABDC" == convert("ABCD", 3)
    assert convert("hjouvsuyoypayulyeimuotehzriicfskpggkbbipzzrzucxamludfykgruowzgiooobppleqlwphapjnadqhdcnvwdtxjbmyppphauxnspusgdhiixqmbfjxjcvudjsuyibyebmwsiqyoygyxymzevypzvjegebeocfuftsxdixtigsieehkchzdflilrjqfnxztqrsvbspkyhsenbppkqtpddbuotbbqcwivrfxjujjddntgeiqvdgaijvwcyaubwewpjvygehljxepbpiwuqzdzubdubzvafspqpqwuzifwovyddwyvvburczmgyjgfdxvtnunneslsplwuiupfxlzbknhkwppanltcfirjcddsozoyvegurfwcsfmoxeqmrjowrghwlkobmeahkgccnaehhsveymqpxhlrnunyfdzrhbasjeuygafoubutpnimuwfjqsjxvkqdorxxvrwctdsneogvbpkxlpgdirbfcriqifpgynkrrefx", 503)