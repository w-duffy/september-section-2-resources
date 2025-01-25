import unittest

class TestMyPerfectSquare(unittest.TestCase):
    def test_03_perfect_square(self):
        from problem_03_perfect_square import perfect_square
        self.assertEqual(perfect_square(15, 5), False)
        self.assertEqual(perfect_square(25, 5), True)
        self.assertEqual(perfect_square(81, 9), True)
        self.assertEqual(perfect_square(9, 2), False)
        self.assertEqual(perfect_square(1, 1), True)
        self.assertEqual(perfect_square(0, 3), False)
