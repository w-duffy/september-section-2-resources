# All Occurrences Of A Value In A List

# Create a function name `get_indices` that takes in a list and a value.
# This function should return the indices of all occurrences of the value
# in the list.

#!!START
def get_indices(lst,val):
  indices = []
  for i in range(0, len(lst)):
    if val == lst[i]:
      indices.append(i)
  return indices
#!!END


print(get_indices(["a", "a", "b", "a", "b", "a"], "a"))
#> [0, 1, 3, 5]

print(get_indices([1, 5, 5, 2, 7], 5))
#> [1, 2]

print(get_indices([1, 5, 5, 2, 7], 8))
#> []
