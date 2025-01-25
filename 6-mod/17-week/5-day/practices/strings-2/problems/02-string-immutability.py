# Declare a variable that contains a string. Then try to change the first letter
# of the string and `print` your string.

# Write your function here.

#!!START SILENT
string = "hello"
string[0] = "m"

print(string)  #> TypeError: 'str' object does not support item assignment. 
# (This occurs because strings are immutable in Python)
#!!END
