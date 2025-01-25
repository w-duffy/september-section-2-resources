# Create a function that takes in a list, `lst`. The function should return a
# list including all the values divisible by both 3 and 5. Hint: This can be
# done in a single line of code.

# Write your function here.
#!!START SILENT
def fizzbuzz(lst):
  return [i for i in lst if i % 3 == 0 and i % 5 == 0]
#!!END

print(fizzbuzz([15, 5, 10, 30])) #> [15, 30]
print(fizzbuzz([60, 20, 90, 20])) #> [60, 90]
print(fizzbuzz([-15, 120, 35, -30])) #> [-15, 120, -30]