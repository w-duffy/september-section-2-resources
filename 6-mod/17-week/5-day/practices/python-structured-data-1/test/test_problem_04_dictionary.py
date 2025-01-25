import unittest

class TestDict(unittest.TestCase):
    def test_function_returns_proper_value(self):
        from problem_04_dictionary import merge_lists
        result = merge_lists(["x", "y", 1, 2], [23, 24, None, "z"])
        self.assertDictEqual(result, { "x": 23, "y": 24, 1: None, 2: "z"})
    def test_empty_list(self):
        from problem_04_dictionary import merge_lists
        result = merge_lists([], [])
        self.assertEqual(result, {})
