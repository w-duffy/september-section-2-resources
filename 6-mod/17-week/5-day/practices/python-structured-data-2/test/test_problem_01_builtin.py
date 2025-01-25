import unittest

class TestSorter(unittest.TestCase):
    def test_function_returns_proper_value(self):
        from problem_01_builtin import sort_teachers_by_classroom_capacity
        teachers = [
            {
                "name": "Emily Richardson",
                "subjects": ["Geometry", "Geometry Honors"],
                "years_active": 5,
                "classroom": {
                    "building_id": "A",
                    "room_number": 12,
                    "capacity": 45
                }
            },
            {
                "name": "Richard Emilyson",
                "subjects": ["English 11", "AP English Language"],
                "years_active": 12,
                "classroom": {
                    "building_id": "J",
                    "room_number": 42,
                    "capacity": 60
                }
            },
            {
                "name": "Richly Emiardson",
                "subjects": ["Chemistry", "Chemistry Honors", "AP Chemistry"],
                "years_active": 8,
                "classroom": {
                    "building_id": "C",
                    "room_number": 5,
                    "capacity": 32
                }
            },
        ]

        test = [
            {
                "name": "James",
                "subjects": ["Geometry", "Geometry Honors"],
                "years_active": 5,
                "classroom": {
                    "building_id": "A",
                    "room_number": 12,
                    "capacity": 1
                }
            },
            {
                "name": "Jacob",
                "subjects": ["English 11", "AP English Language"],
                "years_active": 12,
                "classroom": {
                    "building_id": "J",
                    "room_number": 42,
                    "capacity": 0
                }
            },
            {
                "name": "Johnson",
                "subjects": ["Chemistry", "Chemistry Honors", "AP Chemistry"],
                "years_active": 8,
                "classroom": {
                    "building_id": "C",
                    "room_number": 5,
                    "capacity": -3
                }
            },
        ]
        self.assertEqual(sort_teachers_by_classroom_capacity(teachers), ['Richly Emiardson', 'Emily Richardson', 'Richard Emilyson'])
        self.assertEqual(sort_teachers_by_classroom_capacity(test), ['Johnson', 'Jacob', 'James'])
