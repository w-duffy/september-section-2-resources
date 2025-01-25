# Order Decorator

# Implement a decorator function called order_decorator that will be used to
# print the values 1, 2, 3, 4 in order while the callback is in the middle of
# two print statements. The decorator function should take another function
# argument as a callback, implement an inner wrapper function, and finally
# return the wrapper function object.

# Implement the inner wrapper function with the following:

# 1. Takes in a variable argument
# 2. A print statement of the integer 1
# 3. Initializes a variable of that calls the middle callback function with the
# argument passed into the wrapper
# 4. A print statement of the integer 3
# 5. Returns the variable of the callback function

# Finally, be sure to decorate middle function using the decorator syntax.

#!!START
def order_decorator(func):
  def inner(num):
    print(1)
    x = func(num)
    print(3)
    return x
  return inner

@order_decorator
#!!END
def middle(num):
  print(num)
  return num * num

print(middle(2)) #> 1 2 3 4
