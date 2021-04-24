import unittest
import problems as p

class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual([0, 1], p._1.twoSums([2, 7, 11, 15], 9))
    
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

    def test_167(self):
        self.assertEqual([1, 2], p._167.twoSum([2, 7, 11, 15], 9))