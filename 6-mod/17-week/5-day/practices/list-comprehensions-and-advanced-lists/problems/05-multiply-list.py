# Create a function that takes in two `lists` that returns the results of all
# the values in the first list multiplied by all the values in the second list.

# Write your function here.
#!!START SILENT
def multiply_lists(num1, num2):
  return [(n * x) for n in num1 for x in num2]
#!!END

print(multiply_lists([1, 2 ,3], [1, 5, 7])) #> [1, 5, 7, 2, 10, 14, 3, 15, 21]
print(multiply_lists([5, 6 ,2], [1, 4, 3])) #> [5, 20, 15, 6, 24, 18, 2, 8, 6]
print(multiply_lists([0, 2, 3], [8, 5, 2])) #> [0, 0, 0, 16, 10, 4, 24, 15, 6]