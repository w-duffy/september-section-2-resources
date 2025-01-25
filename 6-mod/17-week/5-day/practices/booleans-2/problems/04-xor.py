# Create a function that returns the `xor` result of two values.

# Are the results a bit confusing when integer values are passed in? You can
# learn more about Python's bitwise operators in the python wiki.
# https://wiki.python.org/moin/BitwiseOperators

# Write your function here.

#!!START SILENT
def xor(x, y):
  return x ^ y
#!!END

print(xor(False, False))   #>  False
print(xor(True, False))   #>  True
print(xor(True, True)) #>  False
print(xor(5, 3))  #> 6
print(xor(8, 4))  #> 12
print(xor(2, 2))  #> 0
print(xor(1, 2))  #> 3
print(xor(4, 4))  #> 0
