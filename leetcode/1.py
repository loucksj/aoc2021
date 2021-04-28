def twoSums(nums: list[int], target: int) -> list[int]:
    d = {}

    for i in range(0, len(nums)):
        if nums[i] in d:
            return [d[nums[i]], i] # return saved index and this index
        else:
            d[target - nums[i]] = i # save this index at the other number

if __name__ == '__main__':
    assert twoSums([2, 7, 11, 15], 9) == [0, 1]