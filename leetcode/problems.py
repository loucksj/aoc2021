import math #_2

class _1:
    def twoSums(nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

class ListNode: #_2
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class _2:  
    def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
        a = l1.val
        i = 1
        while l1.next != None:
            l1 = l1.next
            a += l1.val * pow(10, i)
            i += 1
        b = l2.val
        i = 1
        while l2.next != None:
            l2 = l2.next
            b += l2.val * pow(10, i)
            i += 1
        
        sum = a + b
        
        if sum == 0:
            return ListNode(0)

        sum_len = int(math.log10(sum))+1
        
        backsum = 0
        i = 0
        while sum != 0:
            backsum = 10 * backsum + (sum % 10)
            sum = sum//10
            i += 1

        backsum_len = int(math.log10(backsum))+1
        
        l = ListNode(backsum % 10)
        while backsum > 9:
            backsum = backsum // 10
            l = ListNode(backsum % 10, l)
        
        for _ in range(sum_len - backsum_len):
            l = ListNode(0, l)

        return l

class _7:
    def reverse(x: int) -> int:
        neg = x < 0
        x = abs(x)
        n = 0
        while x != 0:
            n = 10 * n + (x % 10)
            x = x//10
        if neg:
            n *= -1
        if abs(n) < 2**31 and n != 2**31 - 1:
            return n
        return 0 # n outside signed 32-bit integer range

class _9:
    def isPalindrome(x: int) -> bool:
        if x < 0:
            return False
        mut_x = x
        n = 0
        i = 0
        while mut_x != 0:
            n = 10 * n + (mut_x % 10)
            mut_x = mut_x//10
            i += 1
        return n == x

class _13:
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

class _14:
    def longestCommonPrefix(strs: list[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        highest = ""
        for i in range(1, 201):
            common = True
            for j in range(1, len(strs)):
                if strs[0][0:i] != strs[j][0:i]:
                    common = False
                    break
            if common:
                highest = strs[0][0:i]
            else:
                break
        return highest

class _15:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
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
                    y = self.nextIndex(nums, y, z, 1)
                if sum > 0:
                    z = self.nextIndex(nums, z, y, -1)
        return triplets

    def nextIndex(self, nums: list[int], current: int, limit: int, move: int) -> int:
        while True:
            current += move
            if nums[current] != nums[current-move] or current == limit:
                break
        return current

class _69:
    def mySqrt(x: int) -> int:
        return int(x**(1/2))

class _118:
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

class _119:
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