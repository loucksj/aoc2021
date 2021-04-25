import unittest
import problems as p

class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual([0, 1], p._1.twoSums([2, 7, 11, 15], 9))
    
    def test_2(self):
        l1 = p.ListNode(2, p.ListNode(4, p.ListNode(3)))
        l2 = p.ListNode(5, p.ListNode(6, p.ListNode(4)))
        l3 = p._2.addTwoNumbers(l1, l2)
        self.assertEqual(7, l3.val)
        self.assertEqual(0, l3.next.val)
        self.assertEqual(8, l3.next.next.val)
        
        self.assertEqual(0, p._2.addTwoNumbers(p.ListNode(0), p.ListNode(0)).val)

        l1 = p.ListNode(5, p.ListNode(6))
        l2 = p.ListNode(5, p.ListNode(4, p.ListNode(9)))
        l3 = p._2.addTwoNumbers(l1, l2)
        self.assertEqual(0, l3.val)
        self.assertEqual(1, l3.next.val)
        self.assertEqual(0, l3.next.next.val)
        self.assertEqual(1, l3.next.next.next.val)

    def test_7(self):
        self.assertEqual(321, p._7.reverse(123))
        self.assertEqual(-321, p._7.reverse(-123))
        self.assertEqual(21, p._7.reverse(120))
        self.assertEqual(0, p._7.reverse(0))
        self.assertEqual(0, p._7.reverse(1534236469))

    def test_9(self):
        self.assertEqual(True, p._9.isPalindrome(121))
        self.assertEqual(False, p._9.isPalindrome(-121))
        self.assertEqual(False, p._9.isPalindrome(10))
        self.assertEqual(False, p._9.isPalindrome(-101))
        self.assertEqual(False, p._9.isPalindrome(1000021))

    def test_13(self):
        self.assertEqual(3, p._13.romanToInt("III"))
        self.assertEqual(4, p._13.romanToInt("IV"))
        self.assertEqual(9, p._13.romanToInt("IX"))
        self.assertEqual(58, p._13.romanToInt("LVIII"))
        self.assertEqual(1994, p._13.romanToInt("MCMXCIV"))
        self.assertEqual(1695, p._13.romanToInt("MDCXCV"))

    def test_14(self):
        self.assertEqual("fl", p._14.longestCommonPrefix(["flower","flow","flight"]))
        self.assertEqual("", p._14.longestCommonPrefix(["dog","racecar","car"]))
        self.assertEqual("a", p._14.longestCommonPrefix(["a"]))
        self.assertEqual("", p._14.longestCommonPrefix(["reflower","flow","flight"]))
        self.assertEqual("flower", p._14.longestCommonPrefix(["flower","flower","flower","flower"]))
        self.assertEqual("aa", p._14.longestCommonPrefix(["aaa","aa","aaa"]))

    def test_15(self):
        self.assertEqual([], p._15.threeSum([]))
        self.assertEqual([], p._15.threeSum([0]))
        self.assertEqual([[-1,-1,2], [-1,0,1]], p._15.threeSum([-1,0,1,2,-1,-4]))
        self.assertEqual([[0,0,0]], p._15.threeSum([0,0,0,0]))
        self.assertEqual([[-4,-2,6],[-4,0,4],[-4,1,3],[-4,2,2],[-2,-2,4],[-2,0,2]], p._15.threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]))
        self.assertEqual([[-82,-11,93],[-82,13,69],[-82,17,65],[-82,21,61],[-82,26,56],[-82,33,49],[-82,34,48],[-82,36,46],[-70,-14,84],[-70,-6,76],[-70,1,69],[-70,13,57],[-70,15,55],[-70,21,49],[-70,34,36],[-66,-11,77],[-66,-3,69],[-66,1,65],[-66,10,56],[-66,17,49],[-49,-6,55],[-49,-3,52],[-49,1,48],[-49,2,47],[-49,13,36],[-49,15,34],[-49,21,28],[-43,-14,57],[-43,-6,49],[-43,-3,46],[-43,10,33],[-43,12,31],[-43,15,28],[-43,17,26],[-29,-14,43],[-29,1,28],[-29,12,17],[-14,-3,17],[-14,1,13],[-14,2,12],[-11,-6,17],[-11,1,10],[-3,1,2]], p._15.threeSum([34,55,79,28,46,33,2,48,31,-3,84,71,52,-3,93,15,21,-43,57,-6,86,56,94,74,83,-14,28,-66,46,-49,62,-11,43,65,77,12,47,61,26,1,13,29,55,-82,76,26,15,-29,36,-29,10,-70,69,17,49]))

    def test_69(self):
        self.assertEqual(2, p._69.mySqrt(4))
        self.assertEqual(2, p._69.mySqrt(8))
        self.assertEqual(1, p._69.mySqrt(1))
        self.assertEqual(3, p._69.mySqrt(9))
        self.assertEqual(1, p._69.mySqrt(2))

    def test_118(self):
        self.assertEqual([[1]], p._118.pascalsTriangle(1))
        self.assertEqual([[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]], p._118.pascalsTriangle(5))

    def test_119(self):
        self.assertEqual([1, 3, 3, 1], p._119.pascalsTriangle(3))
        self.assertEqual([1], p._119.pascalsTriangle(0))
        self.assertEqual([1,1], p._119.pascalsTriangle(1))

    def test_167(self):
        self.assertEqual([1, 2], p._167.twoSum([2, 7, 11, 15], 9))