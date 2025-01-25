import unittest

class TestMultiplyList(unittest.TestCase):
    def test_function_returns_proper_value(self):
        from problem_02_mult_list import multiply_lists
        self.assertEqual(multiply_lists([1, 2 ,3], [1, 5, 7]), [1, 5, 7, 2, 10, 14, 3, 15, 21])
        self.assertEqual(multiply_lists([5, 6 ,2], [1, 4, 3]), [5, 20, 15, 6, 24, 18, 2, 8, 6])
        self.assertEqual(multiply_lists([0, 2, 3], [8, 5, 2]), [0, 0, 0, 16, 10, 4, 24, 15, 6])
        self.assertEqual(multiply_lists([0], [1, 2, 3]), [0, 0, 0])
        self.assertEqual(multiply_lists([], [1, 2, 3]), [])
        self.assertEqual(multiply_lists([1, 2], [-1, -2, -3]), [-1, -2, -3, -2, -4, -6])
