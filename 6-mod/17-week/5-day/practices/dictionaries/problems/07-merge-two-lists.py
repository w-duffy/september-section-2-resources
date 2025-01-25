# Given two lists, `lst1` and `lst2`, write a function `merge_lists` that merges
# them into a dictionary where the `lst1` represents a list of the keys and
# `lst2` represents a list of the values. Assume the lists are of the same
# length.

# Write your code here.
#!!START SILENT
def merge_lists(lst1, lst2):
    merged_dict = {}
    ind = 0
    while ind < len(lst1):
        merged_dict[lst1[ind]] = lst2[ind]
        ind += 1
    return merged_dict
#!!END

lst1 = ['a', 'b']
lst2 = [1, 2]
merged_dict = merge_lists(lst1, lst2)
print(merged_dict)      # { 'a': 1, 'b': 2 }