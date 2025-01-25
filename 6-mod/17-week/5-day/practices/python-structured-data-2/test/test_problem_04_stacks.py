import unittest

class TestDictionaryPairs(unittest.TestCase):
    def test_function_returns_proper_value(self):
        from problem_04_stacks import stack
        self.assertEqual(stack(["10","5","P","T","+"]), 80)
        self.assertEqual(stack(["0","7","-4","P","T","9","+","+"]), 106)
        self.assertEqual(stack(["1", "P"]), 0)
        self.assertEqual(stack(["2", "T"]), 8)
        self.assertEqual(stack(["2", "1", "+"]), 6)
