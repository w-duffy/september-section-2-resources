import unittest

class TestMatrixList(unittest.TestCase):
    def test_function_returns_proper_value(self):
        from problem_06_list_comp import matrix_rows
        test1 = [[8, 2], [6, 3], [3, 7], [1, 2]]
        test2 = [[1, 4], [3, 2], [1, 0], [9, 7]]
        test3 = [[5, 6], [2, 8], [5, 2], [1, 0]]
        test4 = [['a', 'b'], ['c', 'd'], ['e', 'f'], ['g', 'h']]
        test5 = [[1, 'z'], [2, 't'], ['p', 0], ['l', 3]]
        self.assertEqual((matrix_rows(test1)), [[8, 6, 3, 1], [2, 3, 7, 2]])
        self.assertEqual((matrix_rows(test2)), [[1, 3, 1, 9], [4, 2, 0, 7]])
        self.assertEqual((matrix_rows(test3)), [[5, 2, 5, 1], [6, 8, 2, 0]])
        self.assertEqual((matrix_rows(test4)), [['a', 'c', 'e', 'g'], ['b', 'd', 'f', 'h']] )
        self.assertEqual((matrix_rows(test5)), [[1, 2, 'p', 'l'], ['z', 't', 0, 3]])
