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
        #self.assertEqual(True, p._9.isPalindrome(121))
        self.assertEqual(False, p._9.isPalindrome(-121))
        #self.assertEqual(False, p._9.isPalindrome(10))
        self.assertEqual(False, p._9.isPalindrome(-101))

    def test_167(self):
        self.assertEqual([1, 2], p._167.twoSum([2, 7, 11, 15], 9))