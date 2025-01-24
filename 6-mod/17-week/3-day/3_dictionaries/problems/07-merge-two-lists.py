# Given two lists, `lst1` and `lst2`, write a function `merge_lists` that merges
# them into a dictionary where the `lst1` represents a list of the keys and
# `lst2` represents a list of the values. Assume the lists are of the same
# length.


def merge_lists(lst1, lst2):
    return {lst1[i]: lst2[i] for i in range(len(lst1))}
    # return dict(zip(lst1, lst2))
    # return list(zip(lst1, lst2))
    # return tuple(zip(lst1, lst2))


lst1 = ["a", "b"]
lst2 = [1, 2]
tup1 = ("a", "b")
tup2 = (1, 2)
merged_dict = merge_lists(lst1, lst2)
print(merged_dict)  # { 'a': 1, 'b': 2 }

merged_dict = merge_lists(tup1, tup2)
print(merged_dict)  # { 'a': 1, 'b': 2 }
