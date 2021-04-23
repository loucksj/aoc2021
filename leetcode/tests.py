import unittest
import problem_1
import problem_7
import problem_167

class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual([0, 1], problem_1.twoSums([2, 7, 11, 15], 9))
    
    def test_7(self):
        self.assertEqual(321, problem_7.reverse(123))
        self.assertEqual(-321, problem_7.reverse(-123))
        self.assertEqual(21, problem_7.reverse(120))
        self.assertEqual(0, problem_7.reverse(0))
        self.assertEqual(0, problem_7.reverse(1534236469))

    def test_167(self):
        self.assertEqual([1, 2], problem_167.twoSum([2, 7, 11, 15], 9))