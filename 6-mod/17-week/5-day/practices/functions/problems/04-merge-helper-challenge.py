# Recall the merge sort algorithm:
    
# 1. Find midpoint to divide list in half
# 2. Call `merge_sort` recursively on the first half
# 3. Call `merge_sort` recursively on the second half
# 4. Merge the two sorted halves with `merge`

# Implement the `merge_sort` function with the `merge` helper function.

# Write your code here.
#!!ADD
def merge_sort(lst):
    # # Call merge somewhere in here
    pass

def merge(first_half, second_half):
    # # Merge logic goes here
    pass
#!!END_ADD
#!!START SILENT
# This is an out-of-place solution, see if you can do this in-place if you
# hadn't previously done so!

def merge_sort(list):
    if len(list) > 1:
        mid = len(list)//2
        lower_half = merge_sort(list[:mid])
        upper_half = merge_sort(list[mid:])
        return merge(lower_half, upper_half)
    return list

def merge(lower, upper):
    i = j = 0
    temp = []
    while i < len(lower) or j < len(upper):
        if i == len(lower):
            temp.append(upper[j])
            j+=1
        elif j == len(upper):
            temp.append(lower[i])
            i+=1
        elif lower[i] < upper[j]:
            temp.append(lower[i])
            i+=1
        else:
            temp.append(upper[j])
            j+=1
    return temp

#!!END

lst = [5, 2, 38, 91, 16, 427]

sorted_lst = merge_sort(lst)        # Out of place solution
print(sorted_lst)

merge_sort(lst)                     # In place solution
print(lst)