# Implement a decorator function called `hello_world_decorator` that will be
# used to `print` statements. The decorator function should take another
# function argument as a callback, implement an inner wrapper function, and
# finally return the wrapper function object.

# Implement the inner wrapper function with the following:
# - A print statement of the string "Hello"
# - Calls the callback function
# - Another print statement after the callback containing the string "Goodnight"

# Finally, be sure to decorate the `world` function using the decorator syntax.


def hello_world_decorator(cb):
    def wrapper():
        print("Hello")
        cb()
        print("Goodnight")
        # return cb

    return wrapper


@hello_world_decorator
def world():
    print("World")


world()  # > Hello World Goodnight

what_is_dis = world()  # > Hello World Goodnight
# what_is_dis_now = what_is_dis()
# print(what_is_dis_now)
# print(world)
# print(what_is_dis)
# what_is_dis()
