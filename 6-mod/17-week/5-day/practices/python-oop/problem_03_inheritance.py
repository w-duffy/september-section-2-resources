# INHERITANCE
#
# Define two classes in this file.
#
# The "Employee" class that takes in one value, an id.
#
# The "Manager" class should inherit from the "Employee" class. It should have
# the same constructor as the "Employee" class. The manager should have an
# empty list of employees

#!!START
class Employee:
    def __init__(self, id):
        self.id = id

class Manager(Employee):
    def __init__(self, id):
        super().__init__(id)
        self.employees = []
#!!END


manager = Manager(0)
print(isinstance(manager, Employee))
