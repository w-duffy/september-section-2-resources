# Create a function that recursively prints a countdown from 5 to 1.

# Write your function here.

#!!START SILENT
def recursive_countdown(n):
  if n <= 0:
    return
  else:
    print(n)
    recursive_countdown(n-1)
#!!END

recursive_countdown(5) #> 5 4 3 2 1