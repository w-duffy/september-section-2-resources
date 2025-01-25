import unittest
from inspect import getsourcelines

class TestBubbleSum(unittest.TestCase):
    def test_function_returns_proper_value(self):
        from problem_02_tuple import bubble_sum
        self.assertEqual(bubble_sum([(3, 5), (1, 3), (6, 5), (2, 8)]), [(1, 3), (3, 5), (2, 8), (6, 5)])
        self.assertEqual(bubble_sum([(2, 5), (2, 5), (7, 8), (2, 6)]), [(2, 5), (2, 5), (2, 6), (7, 8)])
        self.assertEqual(bubble_sum([(5, 6), (1, 2), (3, 0), (2, 4)]), [(1, 2), (3, 0), (2, 4), (5, 6)])
        self.assertEqual(bubble_sum([(5, 4), (1, 0), (2, 1), (4, 1)]), [(1, 0), (2, 1), (4, 1), (5, 4)])
        self.assertEqual(bubble_sum([(-1, 3), (7, 9), (0, -9), (-5, -1)]), [(0, -9), (-5, -1), (-1, 3), (7, 9)])
        self.assertEqual(bubble_sum([]), [])

    def test_function_appears_to_use_range(self):
        from problem_02_tuple import bubble_sum
        lines = [line
                 for line in getsourcelines(bubble_sum)[0]
                 if line.strip().__contains__("range")]
        self.assertTrue(len(lines) > 0)
