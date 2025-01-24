# Create a function that takes in a list, `lst`. The function should return a
# list including all the values divisible by both 3 and 5. Hint: This can be
# done in a single line of code.


def fizz_buzz(lst):
    return [el for el in lst if el % 15 == 0]


print(fizz_buzz([15, 5, 10, 30]))  # > [15, 30]
print(fizz_buzz([60, 20, 90, 20]))  # > [60, 90]
print(fizz_buzz([-15, 120, 35, -30]))  # > [-15, 120, -30]
