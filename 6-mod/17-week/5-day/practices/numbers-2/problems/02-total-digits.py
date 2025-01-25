# Create a function that takes an integer as an argument and returns the amount
# of digits it has.

# Write your function here.

#!!START SILENT
def find_digit_amount(n):
  l = len(str(n))
  if n < 0:
    return l - 1
  return l
#!!END

print(find_digit_amount(123))           #> 3
print(find_digit_amount(-56))           #> 2
print(find_digit_amount(7154))          #> 4
print(find_digit_amount(61217311514))   #> 11
print(find_digit_amount(0))             #> 1