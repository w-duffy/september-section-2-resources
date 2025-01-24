# Given a string, `str`, write a function, `check_binary`, that returns whether
# or not `str` is a valid binary string. While there are many ways to solve
# this, try to implement a solution using a set.


def check_binary(str):
    return len(set("10") | set(str)) == 2


# def check_binary(str):
#     return not len(set("01").symmetric_difference(set(str)))


# def check_binary(str):
#     sett = {"1", "0"}
#     for i in range(len(str)):
#         sett.add(str[i])
#     if len(sett) > 2:
#         return False
#     else:
#         return True


# def check_binary(str):
#     st = set(str)
#     return st <= {"0", "1"}


# def check_binary(str):
#     st = set(str)
#     return st == {"0", "1"} or st == {"0"} or st == {"1"}


str1 = "1010001010010100101"
str2 = "1010010015010101010"
str3 = "1111111115111111111"
str4 = "111111111111111111"
str5 = "000000000000000000"

print(check_binary(str1))  # True
print(check_binary(str2))  # False
print(check_binary(str3))  # False
print(check_binary(str4))  # True
print(check_binary(str5))  # True
