def twoSums(nums: list[int], target: int) -> list[int]:
    d = {}

    for i in range(0, len(nums)):
        if nums[i] in d and nums[d[nums[i]]] + nums[i] == target:
            return [d[nums[i]], i]    
        else:
            d[target - nums[i]] = i

if __name__ == '__main__':
    assert twoSums([2, 7, 11, 15], 9) == [0, 1]