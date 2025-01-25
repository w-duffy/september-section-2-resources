import unittest

class TestEmployeesAndManagers(unittest.TestCase):
    def test_inheritance(self):
        from problem_03_inheritance import Employee, Manager

        manager = Manager(1)

        self.assertIsInstance(manager, Employee)
