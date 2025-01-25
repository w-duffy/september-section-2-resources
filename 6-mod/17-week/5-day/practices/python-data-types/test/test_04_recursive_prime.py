import unittest
from random import randint
from inspect import getsourcelines

class TestRecursivePrime(unittest.TestCase):
    def test_04_recursive_prime(self):
        from problem_04_recursive_prime import is_prime
        self.assertEqual(is_prime(1), False)
        self.assertEqual(is_prime(2), True)
        self.assertEqual(is_prime(3), True)
        self.assertEqual(is_prime(5), True)
        self.assertEqual(is_prime(9), False)
        self.assertEqual(is_prime(57), False)

    def test_function_appears_to_be_recursive(self):
        from problem_04_recursive_prime import is_prime
        lines = [line
                 for line in getsourcelines(is_prime)[0]
                 if line.strip().startswith("return is_prime")]
        self.assertTrue(len(lines)>0)
