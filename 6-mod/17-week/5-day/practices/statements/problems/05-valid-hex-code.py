# Create a function that determines whether a string is a valid hex code.

# A hex code must begin with a pound key # and is exactly 6 characters in
# length. Each character must be a digit from 0-9 or an alphabetic character
# from A-F. All alphabetic characters may be uppercase or lowercase.

# Write your function here.

#!!START SILENT
def is_valid_hex_code(code):
    if code[0] != "#" or len(code) != 7:
       return False

    i = 1
    while i < len(code):
        c = code[i].lower()
        if not c.isdigit():
            if c != 'a' and c != 'b' and c != 'c' and c != 'd' and c != 'e' and c != 'f':
               return False
        i += 1
    return True

## Here's another variant, with the for loop.
## You'll learn more about this tomorrow.
def is_valid_hex_code_with_for(color):
  if color[0] != '#' or len(color) != 7:
    return False

  color_chars = list('abcdef0123456789')
  for char in color[1:].lower():
    if char not in color_chars:
      return False
  return True
#!!END

print(is_valid_hex_code("#CD5C5C"))  #> True
print(is_valid_hex_code("#EAECEE"))  #> True
print(is_valid_hex_code("#eaecee"))  #> True

print(is_valid_hex_code("#CD5C58C"))
# Prints False
# Length exceeds 6

print(is_valid_hex_code("#CD5C5Z"))
# Prints False
# Not all alphabetic characters in A-F

print(is_valid_hex_code("#CD5C&C"))
# Prints false
# Contains unacceptable character

print(is_valid_hex_code("CD5C5C"))
# Prints False
# Missing #
