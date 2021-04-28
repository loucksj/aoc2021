def threeSum(nums: list[int]) -> list[list[int]]:
    triplets = []
    size = len(nums)
    if size < 3:
        return triplets
    nums.sort()
    for x in range(0, size-2):
        if nums[x] > 0:
            break
        if x >= 1 and nums[x] == nums[x-1]:
            continue #skip duplicate
        y = x + 1
        z = size-1
        while True:
            if nums[z] < 0:
                break
            if y == z or y == size-1:
                break
            sum = nums[x] + nums[y] + nums[z]
            if sum == 0:
                triplets.append([nums[x], nums[y], nums[z]])
            if sum <= 0:
                y = nextIndex(nums, y, z, 1)
            if sum > 0:
                z = nextIndex(nums, z, y, -1)
    return triplets

def nextIndex(nums: list[int], current: int, limit: int, move: int) -> int:
    while True:
        current += move
        if nums[current] != nums[current-move] or current == limit:
            break
    return current

if __name__ == '__main__':
    assert [] == threeSum([])
    assert [] == threeSum([0])
    assert [[-1,-1,2], [-1,0,1]] == threeSum([-1,0,1,2,-1,-4])
    assert [[0,0,0]] == threeSum([0,0,0,0])
    assert [[0,0,0]] == threeSum([0,0,0])
    assert [[-1,0,1]] == threeSum([1,-1,-1,0])
    assert [[-4,-3,7],[-4,-2,6],[-4,-1,5],[-4,1,3],[-4,2,2],[-3,-2,5],[-3,-1,4],[-3,1,2],[-2,-1,3]] == threeSum([6,2,2,1,-1,3,5,-4,-4,3,-4,4,9,-2,5,7,-3])
    assert [[-4,-2,6],[-4,0,4],[-4,1,3],[-4,2,2],[-2,-2,4],[-2,0,2]] == threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6])