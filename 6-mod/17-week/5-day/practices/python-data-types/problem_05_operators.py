# Operators

# Create three functions: remainder_of_two_numbers, calculate_exponents, and
# divisible_by_5.


# 1. There is a single operator in Python, capable of providing the remainder
# of a division operation. Two numbers are passed as parameters. The first
# parameter divided by the second parameter will have a remainder, possibly
# zero.Return that value. You should be able to do this with one line in the
# body of your function.

#!!START
def remainder_of_two_numbers(num1, num2):
    return num1 % num2
#!!END

print(remainder_of_two_numbers(1, 3))  #> 1
print(remainder_of_two_numbers(3, 4))  #> 3
print(remainder_of_two_numbers(5, 5))  #> 0
print(remainder_of_two_numbers(-8, 7))  #> 6


# 2. Create a function that takes a base number and an exponent number and
# returns the calculation. You should be able to do this with one line in the
# body of your function.

#!!START
def calculate_exponents(x, y):
    return x**y
#!!END

print(calculate_exponents(5, 5))     #> 3125
print(calculate_exponents(10, 10))   #> 10000000000
print(calculate_exponents(3, 3))     #> 27


# 3. Create a function that returns True if an integer is evenly divisible by 5,
# and False otherwise.

#!!START
def divisible_by_5(num):
    return num % 5 == 0
#!!END

print(divisible_by_5(5))    #> True
print(divisible_by_5(-55))  #> True
print(divisible_by_5(37))   #> False
