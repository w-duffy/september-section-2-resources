# It's time to put your knowledge of lists, tuples and dictionaries together. In
# this exercise, you will complete the basic statistics calculations for
# - Minimum
# - Maximum
# - Mean
# - Median
# - Mode

# Follow the instructions in the code comments. Be sure to test your work by
# running your code!

# You will likely need to look at the Python documentation to complete this
# activity. https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
# (Search 'dictionary', go to 'Built-in Types', scroll down to 'Mapping Types -
# dict'.)

# After Step 1, you should see this in the terminal:
# - ('min', 'max', 'mean', 'median', 'mode')
# - (1, 9, 5.0, None, None)
# - (12, 99, 43.666666666666664, None, None)

# In Step 2, the expected median values are 5 and 35.5. Median is the middle
# element. When the list has an odd length it's as easy as taking the value at
# the middle index on the sorted list. When the length is even, it's the average
# of the two numbers closest to the middle.

# In Step 3, the expected mode values are 1 and 23. Mode is the element which is
# most repeated.

# BONUS A is really whatever you want to do. It is recommended that you add
# fringe cases (e.g. a list of a single number like zero or all numbers are the
# same).

# BONUS B is to revisit the mode function and return nothing if more than one
# number is repeated the most number of times (like sample1). When successful,
# this would result in (1, 9, 5.0, 5, None) for the first call to analyze.

# STEP 1: Complete analyze function to return 5 values:
#    - minimum
#    - maximum
#    - mean (a.k.a. average)
#    - median (center point)
#    - mode (most repeated)
def analyze(nums):
    return (min(nums), max(nums), sum(nums) / len(nums), median(nums), mode(nums))


# STEP 2: Complete median function to return center number
#         WITHOUT using built-in function
def median(nums):
    sorted_nums = sorted(nums)
    mid = len(nums) // 2

    if len(nums) % 2 == 1:
        return sorted_nums[mid]

    else:
        return (sorted_nums[mid] + sorted_nums[mid - 1]) / 2


# STEP 3: Complete mode function to return most-repeated number
#         WITHOUT using built-in function
# BONUS B: Catch special case where more than one value repeats the most
def mode(nums):
    tracker = {}

    for num in nums:
        if num in tracker:
            tracker[num] += 1
        else:
            tracker[num] = 1

    counted_sorted = sorted(tracker.items(), key=lambda el: el[1])

    # ? Bonus B
    prev_last, last = counted_sorted[-2:]
    if prev_last[1] == last[1]:
        return

    return last[0]


# DO NOT EDIT - sample data for checking your work
sample1 = 1, 2, 3, 4, 5, 6, 7, 8, 9
sample2 = [37, 45, 23, 65, 75, 34, 23, 23, 23, 65, 12, 99]

print(("min", "max", "mean", "median", "mode"))
print(analyze(sample1))
print(analyze(sample2))

# BONUS A: Print more samples as you see fit
