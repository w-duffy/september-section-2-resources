# Concatenate Strings

# Given two strings, first_name and last_name, return a single string in the
# format "last, first".

#!!START
def concat_name(first_name, last_name):
    return last_name + ", " + first_name

# Here's a version that uses string formatting
def concat_name(first_name, last_name):
    return f"{last_name}, {first_name}"
#!!END

print(concat_name("First", "Last"))  #> "Last, First"
print(concat_name("John", "Doe"))    #> "Doe, John"
print(concat_name("App", "Academy"))   #> "Academy, App"
