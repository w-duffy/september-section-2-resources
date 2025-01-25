import unittest

class TestDecorators(unittest.TestCase):
    def test_function_returns_proper_value(self):
        from problem_08_decorators import num
        self.assertEqual((num(5, 2)), 441)
        self.assertEqual((num(8, 2)), 900)
        self.assertEqual((num(4, 9)), 1521)
        self.assertEqual((num(0, 9)), 729)
        self.assertEqual((num(0, 0)), 0)
