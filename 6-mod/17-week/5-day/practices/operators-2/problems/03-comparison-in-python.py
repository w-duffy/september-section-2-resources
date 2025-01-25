# Try to explore the difference between comparison operators in JavaScript and
# Python. Mainly, compare variables using `==` and `is` and see how they differ.
# Try using the `not` keyword and the `!` operator as well.

x = 1
y = '1'
list1 = [1, 2]
list2 = [1, 2]

#!!ADD
print(x == x)
print(x is x)
#!!END_ADD

# Use the equality and identity comparison operators to compare:
# 1. x with itself
# 2. x with y
# 3. list1 with list2

#!!START SILENT
print(x == x) # True
print(x is x) # True
print(x != y) # True
print(x is not y) # True
print(list1 == list2) # True
print(list1 is list2) # False
print(list1 != list2) # False
print(list1 is not list2) # True
#!!END