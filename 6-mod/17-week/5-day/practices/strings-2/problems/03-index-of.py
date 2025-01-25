# Create a function that returns the index of a given letter in the string.

# Write your function here.

#!!START SILENT
def index_of(str, n):
  return str.lower().index(n)
#!!END

print(index_of("Arm", "a"))  #> 0
print(index_of("Pie", "e"))  #> 2
print(index_of("Lucid", "i"))  #> 3
print(index_of("Obvious","u"))  #> 5
