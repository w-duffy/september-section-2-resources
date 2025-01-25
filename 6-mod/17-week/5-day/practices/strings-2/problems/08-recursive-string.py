# Create a function that reverses the string using recursion.

# Write your function here.

#!!START SILENT
def recursive_string(str):
  if len(string) == 0:
    return string

  return recursive_string(string[1:]) + string[0]
#!!END

print(recursive_string("civic")) # civic
print(recursive_string("refer")) # refer
print(recursive_string("string")) # gnirts
print(recursive_string("avocado")) # odacova
print(recursive_string("application")) # noitacilppa