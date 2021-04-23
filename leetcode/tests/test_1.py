import unittest
from solutions import problem_1

class TestSolutions(unittest.TestCase):
    def test_1(self):
        self.assertEqual([0, 1], problem_1.twoSums([2, 7, 11, 15], 9))

if __name__ == '__main__':
    unittest.main()