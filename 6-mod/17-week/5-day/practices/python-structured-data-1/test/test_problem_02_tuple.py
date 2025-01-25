import unittest

class TestTuple(unittest.TestCase):
    def test_function_returns_proper_value(self):
        from problem_02_tuple import fill_tuple
        self.assertEqual(fill_tuple(((58, 1, 5), (0, 3), (45, ), (24, 23)), 2, 3), ((58, 1, 5), (0, 3, 2), (45, 2, 2), (24, 23, 2)))
        self.assertEqual(fill_tuple(((1, ), (5, 7), (55, 22), (80, 52, 20)), 5, 4), ((1, 5, 5, 5), (5, 7, 5, 5), (55, 22, 5, 5), (80, 52, 20, 5)))
        self.assertEqual(fill_tuple(((), (0, 14), (5, 2, 8), (2, 4, 2, 3)), 0, 5), ((0, 0, 0, 0, 0), (0, 14, 0, 0, 0), (5, 2, 8, 0, 0), (2, 4, 2, 3, 0)))
