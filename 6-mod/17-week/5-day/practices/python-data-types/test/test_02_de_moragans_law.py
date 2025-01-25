import unittest

class TestDeMorgansLaw(unittest.TestCase):
    def test_02_de_morgans_law(self):
        from problem_02_de_morgans_law import de_morgans_law
        self.assertEqual(de_morgans_law(True, True), False)
        self.assertEqual(de_morgans_law(True, False), True)
        self.assertEqual(de_morgans_law(False, False), True)
        self.assertEqual(de_morgans_law("", []), True)
        self.assertEqual(de_morgans_law(2, 2), False)
        self.assertEqual(de_morgans_law(2, 0), True)
