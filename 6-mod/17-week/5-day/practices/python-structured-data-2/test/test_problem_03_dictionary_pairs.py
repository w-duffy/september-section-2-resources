import unittest

class TestDictionaryPairs(unittest.TestCase):
    def test_function_returns_proper_value(self):
        from problem_03_dictionary_pairs import dictionary_pairs
        result = dictionary_pairs(["0", "2", "Z"], [None, 5, "yes"])
        self.assertEqual(dictionary_pairs(["name", "age", "food"], ["James", 24, "steak"]), {'Name': 'James', 'Age': 24, 'Food': 'steak'})
        self.assertEqual(dictionary_pairs(["name", "age", "food"], ["Vivian", 21, "sushi"]), {'Name': 'Vivian', 'Age': 21, 'Food': 'sushi'})
        self.assertEqual(dictionary_pairs(["name", "age", "food"], ["Alex", 6, "chocolate"]), {'Name': 'Alex', 'Age': 6, 'Food': 'chocolate'})
        self.assertEqual((result), {"0": None, "2": 5, 'Z': 'yes'})
    def test_empty_dictionary_pairs(self):
        from problem_03_dictionary_pairs import dictionary_pairs
        result = dictionary_pairs([], [])
        self.assertEqual(len(result), 0)
