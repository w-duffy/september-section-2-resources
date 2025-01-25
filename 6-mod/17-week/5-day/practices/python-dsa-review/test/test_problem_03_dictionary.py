import unittest


class TestCharacterCount(unittest.TestCase):
    def test_function_returns_proper_value(self):
        from problem_03_dictionary import majority_char
        str1 = 'all'
        str2 = 'welcome to the jungle'
        str3 = 'App Academy'
        str4 = 'AAAro'
        str5 = ''
        str6 = '+++-*'
        self.assertEqual((majority_char(str1)), 'l')
        self.assertEqual((majority_char(str2)), None)
        self.assertEqual((majority_char(str3)), None)
        self.assertEqual((majority_char(str4)), 'A')
        self.assertEqual((majority_char(str5)), None)
        self.assertEqual((majority_char(str6)), '+')
