# Implement a decorator function called chain_decorator that will be used to
# chain function calls. The decorator function should take another function
# argument as a callback, implement two inner wrapper functions, and finally
# return the wrapper function object in each respective wrapper function.

# Implement the inner wrapper function with the following:
# - Takes a variable number of positional and keyword arguments
# - Initializes a variable that calls the callback function with arguments
#   passed to the wrapper
# - Returns the variable multiplied by itself.

# Implement another inner wrapper function with the following:
# - Takes a variable number of positional and keyword arguments
# - Initializes a variable that calls the callback function with arguments
#   passed to the wrapper
# - Returns the variable multiplied by 3

# Finally, be sure to decorate num function using the decorator syntax.

# ? True decorator chaining


def first_decorator(cb):
    print("Line 24")

    def wrapper(*args, **kwargs):
        print("Line 27")
        val = cb(*args, **kwargs)

        print("returning from first_decorator")
        return val * val

    return wrapper


def second_decorator(cb):
    print("Line 37")

    def wrapper(*args, **kwargs):
        print("Line 40")
        val = cb(*args, **kwargs)
        return val * 3

    return wrapper


# num = first_decorator(second_decorator(num))
@first_decorator
@second_decorator
def num(a, b):
    print("Line 51")
    return a + b


# Print order #! 37, 24, 27, 40, 51

# print(num(5, 2))  # > 441
# print(num(8, 2))  # > 900
# print(num(4, 9))  # > 1521


# #! Awkward a/A approach
# def chain_decorator(cb):
#     def _inner_decorator(cb):
#         def _inner_wrapper(*args, **kwargs):
#             val = cb(*args, **kwargs)
#             print("THIS IS FINAL VAL", val * val)
#             return val * val

#         return _inner_wrapper

#     @_inner_decorator
#     def wrapper(*args, **kwargs):
#         val = cb(*args, **kwargs)
#         print("THIS IS SECOND VAL", val * 3)
#         return val * 3

#     return wrapper


# @chain_decorator # num = chain_decorator(num)
# def num(a, b):
#     print("THIS IS FIRST VAL", a + b)
#     return a + b


# print(num(5, 2))  # > 441
# print(num(8, 2))  # > 900
# print(num(4, 9))  # > 1521


def way_better_function(a, b):
    val = (a + b) * 3
    return val * val


print(way_better_function(5, 2))  # > 441
print(way_better_function(8, 2))  # > 900
print(way_better_function(4, 9))  # > 1521
