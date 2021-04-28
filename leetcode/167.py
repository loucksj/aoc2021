def twoSum(numbers: list[int], target: int) -> list[int]:
    for end in range(len(numbers)-1, -1, -1):
        if target > 0 and numbers[end] > target:
            continue
        for start in range(end):
            if target < 0 and numbers[start] < target:
                break
            if numbers[start] + numbers[end] == target:
                return [start+1, end+1]

if __name__ == '__main__':
    assert [1, 2] == twoSum([2, 7, 11, 15], 9)