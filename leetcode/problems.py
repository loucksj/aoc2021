class _1:
    def twoSums(nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

class _7:
    def reverse(x: int) -> int:
        neg = x < 0
        x = abs(x)
        n = 0
        i = 0
        while x != 0:
            n = 10 * n + (x % 10)
            x = x//10
            i += 1
        if neg :
            n *= -1
        if abs(n) < 2**31 and n != 2**31 - 1:
            return n
        return 0 # n outside signed 32-bit integer range

class _9:
    def isPalindrome(x: int) -> bool:
        if x < 0:
            return False
        return True

class _167:
    def twoSum(numbers: list[int], target: int) -> list[int]:
        for end in range(len(numbers)-1, -1, -1):
            if target > 0 and numbers[end] > target:
                continue
            for start in range(end):
                if target < 0 and numbers[start] < target:
                    break
                if numbers[start] + numbers[end] == target:
                    return [start+1, end+1]