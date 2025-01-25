# Try to explore the difference between equality operators in JavaScript and
# Python. Try comparing primitive data types using `==` and then reference data
# types.

x = 1
y = '1'
list1 = [1, 2]
list2 = [1, 2]
list3 = [2, 3]

# Use "==" to compare these values and see what gets printed! How does this
# compare with JavaScripts "==="?

# Compare "x" with itself
# Compare "x" with "y"
# Compare "list1" with "list2"
# Compare "list1" with "list3"

#!!START SILENT
print(x == x) # True
print(x == y) # False
print(list1 == list2) # True
print(list1 == list3) # False
#!!END