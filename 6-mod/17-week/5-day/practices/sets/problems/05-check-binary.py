# Given a string, `str`, write a function, `check_binary`, that returns whether
# or not `str` is a valid binary string. While there are many ways to solve
# this, try to implement a solution using a set.

# Write your code here.
#!!ADD
def check_binary(str):
    pass
#!!END_ADD
#!!START SILENT
# One possible solution
def check_binary(str):
    str_set = set(str)
    return str_set == { '0', '1' } or str_set == { '1' } or str_set == { '0' }

# Using .issubset
def check_binary2(str):
    str_set = set(str)
    return str_set.issubset({ '0', '1' })
#!!END

str1 = '1010001010010100101'
str2 = '1010010015010101010'

print(check_binary(str1))       # True
print(check_binary(str2))       # False