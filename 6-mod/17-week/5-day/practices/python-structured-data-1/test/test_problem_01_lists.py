import unittest

class TestList(unittest.TestCase):
    def test_function_returns_proper_value(self):
        from problem_01_lists import get_indices
        self.assertEqual(get_indices(["a", "a", "b", "a", "b", "a"], "a"), [0, 1 , 3, 5])
        self.assertEqual(get_indices([1, 5, 5, 2, 7], 8), [])
        self.assertEqual(get_indices([1, 5, 5, 2, 7], 5), [1, 2])
        self.assertIsNot(get_indices([0, 9, 8, 2, 4], 8), [1])
