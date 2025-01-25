import unittest

class TestValidHex(unittest.TestCase):
    def test_08_valid_hex(self):
        from problem_08_valid_hex import is_valid_hex
        self.assertEqual(is_valid_hex("#CD5C5C"), True)
        self.assertEqual(is_valid_hex("#eabead"), True)
        self.assertEqual(is_valid_hex("#CD5C58C"), False)
        self.assertEqual(is_valid_hex("#CD5C&C"), False)
        self.assertEqual(is_valid_hex("CD5C5C"),  False)
