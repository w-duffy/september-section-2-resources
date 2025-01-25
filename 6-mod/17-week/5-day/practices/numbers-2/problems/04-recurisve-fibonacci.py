# Create a function that returns the Fibonacci sequence of the given value.

# Write your function here.

#!!START SILENT
def recursive_fib(n):
  if n <= 1:
    return n
  else:
    return (recursive_fib(n-1) + recursive_fib(n-2))
#!!END

print(recursive_fib(1))     #> 1
print(recursive_fib(2))     #> 1
print(recursive_fib(4))     #> 3
print(recursive_fib(6))     #> 8
print(recursive_fib(12))    #> 144