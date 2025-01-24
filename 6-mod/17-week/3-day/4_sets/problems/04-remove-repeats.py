# Given two strings, write a function, `remove_repeats` that returns a set of
# the uncommon characters from both strings. Do NOT use the `^` operator.

# # ! They say no. I say...why not???
# def remove_repeats(str1, str2):
#     return set(str1) ^ set(str2)

# # ! Technically not cheating...but totally is cheating
# def remove_repeats(str1, str2):
#     return set(str1).symmetric_difference(set(str2))


# def remove_repeats(str1, str2):
#     all_chars = {*str1, *str2}
#     combined_chars = set(str1) & set(str2)

#     return set([char for char in all_chars if char not in combined_chars])


def remove_repeats(str1, str2):
    st3 = (set(str1) - set(str2)) | (set(str2) - set(str1))
    return st3


str1 = "aloha"
str2 = "bonjour"

print(remove_repeats(str1, str2))  # {'r', 'a', 'l', 'h', 'n', 'b', 'j', 'u'}
