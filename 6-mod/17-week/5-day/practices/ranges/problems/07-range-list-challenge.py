# Create a function that returns a list of 100 randomly generated numbers.

import random
# Write your function here.
#!!START SILENT
def rng(lst):
  for i in range(0, 100):
    x = random.randint(0,100)
    lst.append(x)
  return lst
#!!END

print(rng([]))