import unittest

class TestOperator1(unittest.TestCase):
    def test_05_operators(self):
        from problem_05_operators import divisible_by_5
        self.assertEqual(divisible_by_5(5), True)
        self.assertEqual(divisible_by_5(-55), True)
        self.assertEqual(divisible_by_5(37), False)
        self.assertEqual(divisible_by_5(100), True)
        self.assertEqual(divisible_by_5(777), False)
        self.assertEqual(divisible_by_5(8923740), True)


class TestOperator2(unittest.TestCase):
    def test_05_operators(self):
        from problem_05_operators import calculate_exponents
        self.assertEqual(calculate_exponents(5, 5), 3125)
        self.assertEqual(calculate_exponents(10,10), 10000000000)
        self.assertEqual(calculate_exponents(3,3), 27)
        self.assertEqual(calculate_exponents(0, 6), 0)
        self.assertEqual(calculate_exponents(2, 4), 16)

class TestOperator3(unittest.TestCase):
    def test_05_operators(self):
        from problem_05_operators import remainder_of_two_numbers
        self.assertEqual(remainder_of_two_numbers(1, 3), 1)
        self.assertEqual(remainder_of_two_numbers(5, 5), 0)
        self.assertEqual(remainder_of_two_numbers(3, 4), 3)
        self.assertEqual(remainder_of_two_numbers(7, 2), 1)
        self.assertEqual(remainder_of_two_numbers(-8, 7), 6)
        self.assertEqual(remainder_of_two_numbers(2, 4), 2)
