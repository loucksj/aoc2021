def pascalsTriangle(rowIndex: int) -> list[int]:
    prev = [1]
    for r in range(1, rowIndex+1):
        row = []
        row.append(1)
        for n in range(1, r):
            row.append(prev[n-1] + prev[n])
        row.append(1)
        prev = row
    return prev

if __name__ == '__main__':
    assert [1, 3, 3, 1] == pascalsTriangle(3)
    assert [1] == pascalsTriangle(0)
    assert [1,1] == pascalsTriangle(1)