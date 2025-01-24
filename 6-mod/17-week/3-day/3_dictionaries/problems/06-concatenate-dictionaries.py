# Given a list, `lst` of dictionaries, write a function,
# `concatenate_dictionaries` that concatenates the contents of each dictionary
# into a single dictionary. If multiple dictionaries share the same key, use the
# value of the higher indexed dictionary in the list.

# #! Lvl 1 Thief
# def concatenate_dictionaries(lst):
#     new_dict = {}

#     for obj in lst:
#         for key in obj:
#             new_dict[key] = obj[key]

#     return new_dict

#! Lvl 50 Crook # Simplest solution here
def concatenate_dictionaries(lst):
    new_dict = {}

    for el in lst:
        new_dict.update(el)

    return new_dict


# #! Lvl 99 Boss
# def concatenate_dictionaries(lst):
#     new_dict = {}

#     for el in lst:
#         new_dict = {**new_dict, **el}

#     return new_dict


# #! Lvl 1000 Wizard Using Transfiguration Magic
# def concatenate_dictionaries(lst):
#     return {key_val_pair for obj in lst for key_val_pair in obj.items()}
#     # return {(key, value) for obj in lst for key, value in obj.items()}
#     # return {k: v for d in lst for k, v in d.items()}


# def concatenate_dictionaries(lst):
#     return dict(
#         (key, value)  # What to store in the dictionary
#         for obj in lst  # What to loop over
#         for key, value in obj.items()  # What to nested loop over
#     )


lst = [{"a": "this", "b": "is"}, {"c": "the", "d": "merged"}, {"d": "dictionary"}]

print(concatenate_dictionaries(lst))
"""
Prints: 
{
    'a': 'this',
    'b': 'is',
    'c': 'the',
    'd': 'dictionary'
}
"""
