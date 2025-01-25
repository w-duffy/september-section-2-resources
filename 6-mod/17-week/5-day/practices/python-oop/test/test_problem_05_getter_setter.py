from random import randint
import unittest


class TestGameScore(unittest.TestCase):
    def test_has_score_passed_in(self):
        from problem_05_getter_setter import Game
        test = Game()
        self.assertEqual(test.score, 0)

    def test_can_set_and_retrieve_score(self):
        from problem_05_getter_setter import Game
        test = Game()
        value = (randint(1, 10))
        test.score = value
        self.assertEqual(test.score, value*10)
