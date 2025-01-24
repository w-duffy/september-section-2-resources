# Create a function that returns a list of 100 randomly generated numbers.

import random


def rng(lst):
    for _ in range(100):
        lst.append(random.randint(0, 10000))
    return lst


random_list = rng([])
print(len(random_list))
print(random_list)
