# Create a function that takes a string (a random name). If the last character
# of the name is an "n", return `True`, otherwise return `False`.

# Write your function here.

#!!START SILENT
def is_last_character_n(name):
  return name[-1] == "n"
#!!END

print(is_last_character_n("Aiden"))  #> True
print(is_last_character_n("Piet"))   #> False
print(is_last_character_n("Bert"))   #> False
print(is_last_character_n("Dean"))   #> True