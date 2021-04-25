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

    def test_69(self):
        self.assertEqual(2, p._69.mySqrt(4))
        self.assertEqual(2, p._69.mySqrt(8))
        self.assertEqual(1, p._69.mySqrt(1))
        self.assertEqual(3, p._69.mySqrt(9))
        self.assertEqual(1, p._69.mySqrt(2))

    def test_118(self):
        self.assertEqual([[1]], p._118.pascalsTriangle(1))
        self.assertEqual([[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]], p._118.pascalsTriangle(5))

    def test_167(self):
        self.assertEqual([1, 2], p._167.twoSum([2, 7, 11, 15], 9))