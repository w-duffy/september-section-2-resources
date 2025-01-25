import unittest

class TestVowelCount(unittest.TestCase):
    def test_06_vowel_count(self):
        from problem_06_vowel_count import vowel_count
        self.assertEqual(vowel_count("App Academy"), 4)
        self.assertEqual(vowel_count("Coding Expert"), 4)
        self.assertEqual(vowel_count("Supreme"), 3)
        self.assertEqual(vowel_count("Chamber of Secrets"), 5)
        self.assertEqual(vowel_count("Pish Posh"), 2)
        self.assertEqual(vowel_count("Qwerty"), 1)
        self.assertEqual(vowel_count("SDFGHJK"), 0)
