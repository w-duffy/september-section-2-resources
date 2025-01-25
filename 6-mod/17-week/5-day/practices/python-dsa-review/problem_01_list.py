#  Insertion Sort

# Create a function named insertion_sort that uses the insertion sort algorithm
# to sort the list.


#!!START
def insertion_sort(lst):
    for i in range(1, len(lst)):
        ele = lst[i]
        j = i-1
        while lst[j] > ele and j >= 0:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = ele
    return lst
#!!END

print(insertion_sort([55, 21, 5, 3, 6, 95])) #> [3, 5, 6, 21, 55, 95]
print(insertion_sort([4, 1, 0, 3, 8, 9])) #> [0, 1, 3, 4, 8, 9]
print(insertion_sort([1, 4, 3, 0, 3, 0, 2, 8])) #> [0, 0, 1, 2, 3, 3, 4, 8]
