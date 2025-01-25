import unittest

class TestDifference(unittest.TestCase):
    def test_function_returns_proper_value(self):
        from problem_03_range import difference
        self.assertEqual(difference([10, 15, 20, 2, 10, 6]), 18)
        self.assertEqual(difference([-3, 4, -9, -1, -2, 15]), 24)
        self.assertEqual(difference([4, 17, 12, 2, 10, 2]), 15)
        self.assertEqual(difference([89, -257, 0, 75, 13, 2]), 346)
