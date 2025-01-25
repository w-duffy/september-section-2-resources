import unittest

class TestMyString(unittest.TestCase):
    def test_01_string(self):
        from problem_01_string import concat_name
        self.assertEqual(concat_name("First", "Last"), "Last, First")
        self.assertEqual(concat_name("John", "Doe"), "Doe, John")
        self.assertEqual(concat_name("App", "Academy"), "Academy, App")
