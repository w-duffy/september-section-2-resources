#  Remove Repeats

# Given two strings, write a function, remove_repeats that returns a set of the
# uncommon characters from both strings. Do NOT use the ^ operator.

#!!START
def remove_repeats(str1, str2):
    common_set = set(str1) & set(str2)
    result = set()
    for ch in set(str1 + str2):
        if ch not in common_set:
            result.add(ch)
    return result
#!!END


str1 = 'aloha'
str2 = 'bonjour'

print(remove_repeats(str1, str2))    # {'r', 'a', 'l', 'h', 'n', 'b', 'j', 'u'}
