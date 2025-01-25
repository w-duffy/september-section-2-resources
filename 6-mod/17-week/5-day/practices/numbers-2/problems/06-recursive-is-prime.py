# Create a function called `is_prime` that takes in a number and a variable that
# equates to 2. The function should return True/False if the number is a prime
# number. Bonus: Try to do this recursively.

# Write your solution here.

#!!START SILENT
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
print(is_prime(15)) #> False