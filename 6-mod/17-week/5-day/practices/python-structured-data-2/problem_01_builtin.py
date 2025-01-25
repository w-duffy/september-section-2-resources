# Nested Sort

# Say you have a relational database with two tables, Teacher and Classroom,
# which are related by a one-to-one relationship, so each teacher has a
# classroom.

# You've fetched the teachers, and joined with their classroom data.

# Write a function, sort_teachers_by_classroom_capacity, that sorts the results
# in ascending order based on their classroom's capacity and returns a list of
# just the teacher's names in that sorted order.

# Do the sort out-of place without mutating the original list, using the sorted
# built in function.

# Sorting function
def sorter(teacher):
    return teacher['classroom']['capacity']

#!!START
def sort_teachers_by_classroom_capacity(teacher_list):
    teacher_list.sort(key=sorter)
    return list(map(lambda teacher: teacher['name'], teacher_list))
#!!END

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

print(sort_teachers_by_classroom_capacity(teachers))
# Richly Emiardson, Emily Richardson, Richard Emilyson
