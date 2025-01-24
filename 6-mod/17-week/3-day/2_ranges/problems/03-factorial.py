# Write the factorial function. Remember, for a number n, the factorial is all
# numbers from 1 to n multiplied together.


def factorial(n):
    facto = 1
    for x in range(1, n + 1):
        facto *= x
    return facto


print(factorial(1))  # > 1
print(factorial(8))  # > 40320
print(factorial(12))  # > 479001600
