import unittest
from inspect import getsourcelines

class TestBinary(unittest.TestCase):
    def test_function_returns_proper_value(self):
        from problem_04_sets import check_binary
        str1 = '1010001010010100101'
        str2 = '1010010015010101010'
        str3 = ''
        str4 = '12345'
        str5 = '1010101111001010110101100101010'
        str6 = 'abc123+_*()'
        self.assertEqual((check_binary(str1)), True)
        self.assertEqual((check_binary(str2)), False)
        self.assertEqual((check_binary(str3)), False)
        self.assertEqual((check_binary(str4)), False)
        self.assertEqual((check_binary(str5)), True)
        self.assertEqual((check_binary(str6)), False)
