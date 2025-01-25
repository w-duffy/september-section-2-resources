import unittest

class TestMergeSort(unittest.TestCase):
    def test_function_returns_proper_value(self):
        from problem_10_merge_sort import merge_sort
        self.assertEqual((merge_sort([5, 2, 38, 91, 16, 427])), [2, 5, 16, 38, 91, 427])
        self.assertEqual((merge_sort([0, -5, 88, -1, 90, 4])), [-5, -1, 0, 4, 88, 90])
        self.assertEqual((merge_sort([5, 4, 3, 2, -2, 5, 4, -1])), [-2, -1, 2, 3, 4, 4, 5, 5])
