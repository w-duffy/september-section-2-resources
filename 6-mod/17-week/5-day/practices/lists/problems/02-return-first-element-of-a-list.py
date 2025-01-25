# Create a function that takes a list and returns the first element.

# Write your function, here.
#!!START SILENT
def get_first_value(l):
  return l[0]
#!!END

print(get_first_value([1, 2, 3]))        #> 1
print(get_first_value([80, 5, 100]))     #> 80
print(get_first_value([-500, 0, 50]))    #> -500