# Create a function `add_upper` that takes a string and returns all of the
# uppercase characters in the string.

# Write your solution here.

#!!START SILENT
def add_upper(string):
    a = ""
    for x in string:
        if x == x.upper():
            a += x
    return a
#!!END

print(add_upper("ApPlE"))        #> APE
print(add_upper("Coding"))       #> C
print(add_upper("PIano"))        #> PI
print(add_upper("SUPREME"))      #> SUPREME