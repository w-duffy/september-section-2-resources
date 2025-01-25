# Create a function that returns the string "Burp" with the amount of "r's" determined by the input parameters of the function.

# Write your function here.

#!!START SILENT
def long_burp(n):
  return "Bu" + ("r" * n) + "p"
#!!END

print(long_burp(3))  #> "Burrrp"
print(long_burp(5))  #> "Burrrrrp"
print(long_burp(9))  #> "Burrrrrrrrrp"