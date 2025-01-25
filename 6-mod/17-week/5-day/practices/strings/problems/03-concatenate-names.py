# Given two strings, `first_name` and `last_name`, return a single string in the
# format "last, first".

# Write your function here.

#!!START SILENT
def concat_name(first_name, last_name):
  return last_name + ", " + first_name

# Here's a version that uses string formatting
def concat_name_f(first_name, last_name):
  return f"{last_name}, {first_name}"
#!!END

print(concat_name("First", "Last"))  #> "Last, First"
print(concat_name("John", "Doe"))    #> "Doe, John"
print(concat_name("Mary", "Jane"))   #> "Jane, Mary"

#!!START SILENT
print(concat_name_f("First", "Last"))  #> "Last, First"
print(concat_name_f("John", "Doe"))    #> "Doe, John"
print(concat_name_f("Mary", "Jane"))   #> "Jane, Mary"
#!!END
