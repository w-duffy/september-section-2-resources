import unittest
from inspect import getsourcelines
import re

class TestPolymorphism(unittest.TestCase):
    def test_function_returns_proper_value(self):
        from problem_06_poly import StrNumeric
        test = StrNumeric("1").val
        self.assertEqual(test, '1')

    def test_can_add_values(self):
        from problem_06_poly import StrNumeric
        test = StrNumeric("1").__add__(2)
        test2 = StrNumeric("44").__add__(6)
        test3 = 44
        self.assertEqual(test, 3)
        self.assertEqual(test2, 50)
        self.assertEqual(test3.__add__(6), 50)

    def test_appears_to_use_exception(self):
        from problem_06_poly import StrNumeric
        exception_re = re.compile("Exception")
        strip_comments = re.compile("#.*")
        lines = getsourcelines(StrNumeric)[0][1:]
        lines = [strip_comments.sub("", line).strip()
                 for line in lines]
        lines = [line for line in lines if exception_re.findall(line)]
        self.assertGreaterEqual(len(lines), 1)
