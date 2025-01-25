import unittest


class TestFreeShoes(unittest.TestCase):
    def test_constructor_accepts_name_and_number_of_available_copies(self):
        from problem_02_class import FreeShoes
        FreeShoes("Supreme Shoes", 5)


    def test_repr_returns_proper_string_representation(self):
        from problem_02_class import FreeShoes
        shoes = FreeShoes("Supreme Shoes", 5)
        self.assertEqual(str(shoes), "<Supreme Shoes (5)>")

    def test_can_give_away_until_gone(self):
        from problem_02_class import FreeShoes
        shoes = FreeShoes("Supreme Shoes", 5)
        self.assertEqual(str(shoes), "<Supreme Shoes (5)>")
        shoes.give_away()
        self.assertEqual(str(shoes), "<Supreme Shoes (4)>")
        shoes.give_away()
        self.assertEqual(str(shoes), "<Supreme Shoes (3)>")
        shoes.give_away()
        self.assertEqual(str(shoes), "<Supreme Shoes (2)>")
        shoes.give_away()
        self.assertEqual(str(shoes), "<Supreme Shoes (1)>")
        shoes.give_away()
        self.assertEqual(str(shoes), "<Supreme Shoes (0)>")
        shoes.give_away()
        self.assertEqual(str(shoes), "<Supreme Shoes (0)>")
