# Recursive Prime Numbers

# Create a function called is_prime that takes in a number and a variable. That
# variable will equate to 2, the lowest prime number, which will be used as the
# base case of the recursion. The function should return True/False if the
# number is a prime number. Do this recursively.

#!!START
def is_prime(num, i = 2):
    if (num <= 2):
        return True if (num == 2) else False
    if (num % i == 0):
        return False
    if (num < i * i):
        return True

    return is_prime(num, i + 1)
#!!END

print(is_prime(1))  #> False
print(is_prime(2))  #> True
print(is_prime(3))  #> True
print(is_prime(5))  #> True
print(is_prime(9))  #> False
