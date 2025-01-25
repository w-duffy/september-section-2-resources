import unittest

class TestSplitCapitals(unittest.TestCase):
    def test_07_split_capitals(self):
        from problem_07_split_capitals import split_capitals
        self.assertEqual(split_capitals("helloWorld"), "hello world")
        self.assertEqual(split_capitals("iLoveMyTeapot"), "i love my teapot")
        self.assertEqual(split_capitals("stayIndoors"), "stay indoors")
        self.assertEqual(split_capitals("iLOVENY"), "i l o v e n y")
        self.assertEqual(split_capitals("IloveLA"),  " ilove l a")
