import unittest

class TestTrackRobot(unittest.TestCase):
    def test_function_returns_proper_value(self):
        from problem_05_builtin import track_robot
        test1 = ["right 10", "up 50", "left 30", "down 10"]
        test2 = []
        test3 = ["right 100", "right 100", "up 500", "up 10000"]
        test4 = ["right 75", "up 10", "left 10", "down 50"]
        test5 = ["right -75", "up 10", "left 20", "down -50"]
        test6 = ["right -15", "up -10", "left -20", "down -50"]
        self.assertEqual((track_robot(test1)), [-20, 40])
        self.assertEqual((track_robot(test2)), [0, 0])
        self.assertEqual((track_robot(test3)), [200, 10500])
        self.assertEqual((track_robot(test4)), [65, -40])
        self.assertEqual((track_robot(test5)), [-95, 60])
        self.assertEqual((track_robot(test6)), [5, 40])
