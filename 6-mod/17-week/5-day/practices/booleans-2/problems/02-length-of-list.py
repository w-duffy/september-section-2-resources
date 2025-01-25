# Create a function that returns `True` if the length of the list is equal to
# the given value; otherwise return `False`.

# Write your function here.

#!!START SILENT
def length_list(list, n):
  return len(list) == n
#!!END

print(length_list([], 1))   #>  False
print(length_list([], 0))   #>  True
print(length_list([5, 2], 2))   #>  True
print(length_list([1, 4, 3], 4))   #>  False
print(length_list([0, 2, "i", 0.9], 4))   #>  True
