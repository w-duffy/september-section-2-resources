import unittest

class TestInsertionSort(unittest.TestCase):
    def test_function_returns_proper_value(self):
        from problem_01_list import insertion_sort
        self.assertEqual(insertion_sort([55, 21, 5, 3, 6, 95]), [3, 5, 6, 21, 55, 95])
        self.assertEqual(insertion_sort([4, 1, 0, 3, 8, 9]), [0, 1, 3, 4, 8, 9])
        self.assertEqual(insertion_sort([1, 4, 3, 0, 3, 0, 2, 8]), [0, 0, 1, 2, 3, 3, 4, 8])
        self.assertEqual(insertion_sort([-1, 4, -3, 0, 3, 0, 2, 8]),  [-3, -1, 0, 0, 2, 3, 4, 8])
        self.assertEqual(insertion_sort([]), [])
