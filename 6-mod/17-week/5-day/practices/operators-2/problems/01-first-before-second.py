# You are given three inputs: a string, one letter, and a second letter.

# Write a function that returns `True` if every instance of the first letter
# occurs before every instance of the second letter.

# Look at the String Methods to possibly help you find some methods that can
# make this easier.
# https://docs.python.org/3.9/library/stdtypes.html?highlight=strings#string-methods

# Write your function here.

#!!START SILENT
def first_before_second(s, first, second):
    return s.rindex(first) < s.index(second)

## Here's another variant, with the while loop
def first_before_second_while(s, first, second):
    first_last_index = 0
    second_first_index = 0
    i = 0
    while i < len(s):
        if s[i] == first:
            first_last_index = i
        i += 1
    i = 0
    while i < len(s):
        if s[i] == second:
            second_first_index = i
            break
        i += 1
    return first_last_index < second_first_index
#!!END

print(first_before_second("a rabbit jumps joyfully", "a", "j"))
#> True
# Every instance of "a" occurs before every instance of "j".

print(first_before_second("knaves knew about waterfalls", "k", "w"))
#> True

print(first_before_second("happy birthday", "a", "y"))
#> False
# The "a" in "birthday" occurs after the "y" in "happy".

print(first_before_second("precarious kangaroos", "k", "a"))
#> False

#!!START SILENT
print(first_before_second_while("a rabbit jumps joyfully", "a", "j"))
print(first_before_second_while("knaves knew about waterfalls", "k", "w"))
print(first_before_second_while("happy birthday", "a", "y"))
print(first_before_second_while("precarious kangaroos", "k", "a"))
#!!END