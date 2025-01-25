# Create a function that takes a list and returns the sum of all numbers in the
# list.

# Write your function, here.
#!!START SILENT
def get_sum_of_elements(lst):
  total = 0
  for l in lst:
    total += l
  return total
#!!END

print(get_sum_of_elements([2, 7, 4]))     #> 13
print(get_sum_of_elements([45, 3, 0]))    #> 48
print(get_sum_of_elements([-2, 84, 23]))  #> 105