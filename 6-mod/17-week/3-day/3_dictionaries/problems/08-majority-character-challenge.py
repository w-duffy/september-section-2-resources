# Given a string, write a function that returns the character that is the
# majority of the string. If there is no majority character, return None. A
# majority is considered as having more than `n / 2` instances where `n` is the
# length of the string.


def majority_char(val):
    counter_obj = {}

    for char in val:
        if char in counter_obj:
            counter_obj[char] += 1
        else:
            counter_obj[char] = 1
        if counter_obj[char] > (len(val) / 2):
            return char

    # for char, num_appearances in counter_obj.items():
    #     if num_appearances > (len(val) / 2):
    #         return char

    return None


# def majority_char(s):
#     char_counts = {char: s.count(char) for char in set(s)}
#     return next(
#         (char for char, count in char_counts.items() if count > len(s) / 2), None
#     )


str = "all"
str2 = "welcome to the jungle"

print(majority_char(str))  # 'l'
print(majority_char(str2))  # None
