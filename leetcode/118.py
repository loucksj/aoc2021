def pascalsTriangle(numRows: int) -> list[list[int]]:
    rows = []
    for r in range(numRows):
        row = []
        row.append(1)
        if r == 0:
            rows.append(row)
            continue
        for n in range(1, r):
            row.append(rows[r-1][n-1] + rows[r-1][n])
        row.append(1)
        rows.append(row)
    return rows

if __name__ == '__main__':
    assert [[1]] == pascalsTriangle(1)
    assert [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]] == pascalsTriangle(5)