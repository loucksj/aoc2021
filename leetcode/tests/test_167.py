import unittest
from solutions import problem_167

class TestSolutions(unittest.TestCase):
    def test_1(self):
        self.assertEqual([1, 2], problem_167.twoSum([2, 7, 11, 15], 9))

if __name__ == '__main__':
    unittest.main()