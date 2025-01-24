# Write a function that returns `True` if a dictionary contains the specified
# key, and `False` otherwise.

# #? Python classes for data types
# dict()
# tuple()
# str()
# int()
# list()


# def has_key(dict, key):
#     # my_dict = dict(module="Python 3") #! TypeError: 'dict' object is not callable
#     return key in dict


def has_key(obj, key):
    # print(dir(obj))
    return key in obj


print(has_key({"a": 44, "b": 45, "c": 46}, "d"))
# False

print(has_key({"craves": True, "midnight": True, "snack": True}, "morning"))
# False

print(has_key({"pot": 1, "tot": 2, "not": 3}, "not"))
# True
