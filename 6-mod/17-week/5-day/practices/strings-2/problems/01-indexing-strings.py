# Create a function called `index_string` that takes a string as an argument and
# returns that string from the index of 3 to the end of the string.

# Write your function here.

#!!START SILENT
def index_string(string):
    return string[3:]
#!!END

print(index_string("Alchemy"))     #> hemy
print(index_string("Ridiculous"))  #> iculous
print(index_string("Serendipity")) #> endipity
