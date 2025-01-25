# DeMorgan's Law

# Create a function that uses DeMorgan's Law to get the expected True/False
# statement.

#!!START
def de_morgans_law(val1, val2):
    return not (val1 and val2)
#!!END

print(de_morgans_law(True, True)) # False
print(de_morgans_law(True, False)) # True
print(de_morgans_law(False, False)) # True
print(de_morgans_law("", [])) # True
print(de_morgans_law(2, 2)) # False
print(de_morgans_law(2, 0)) # True
