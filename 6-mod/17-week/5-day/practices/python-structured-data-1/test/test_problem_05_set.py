import unittest
from inspect import getsourcelines

class TestSets(unittest.TestCase):
    def test_function_returns_proper_value(self):
        from problem_05_set import remove_repeats
        self.assertEqual((remove_repeats('aloha', 'bonjour')), {'r', 'a', 'l', 'h', 'n', 'b', 'j', 'u'})
        self.assertEqual((remove_repeats('supreme', 'team')), {'t', 'u', 'a', 'r', 's', 'p'})

    def test_function_appears_to_use_xor(self):
        from problem_05_set import remove_repeats
        lines = [line
                 for line in getsourcelines(remove_repeats)[0]
                 if line.strip().startswith("^" or "xor")]
        self.assertFalse(len(lines) > 0)
