# It's time to explore the *tuple* object and how to use it.

# Follow the instructions in the code comments. Be sure to test your work by
# running your code!

# For the bonus, remember you can split a returned tuple to variables: `(a,b,c)
# = myfunc()`

# DO NOT EDIT
odds = 1, 3, 5, 7, 9
evens = 2, 4, 6, 8

# Step 1: Print out the result of adding evens to odds
print(evens + odds)

# Step 2: Print out the result of multiplying odds by three
print(odds * 3)

# Step 3A: Use print to find out if odds is less than evens
print(odds < evens)

# Step 3B: Print out your explanation of why 3A has that result
print("Just checks for first item in each for the comparison")
print((3, 5, 7, 9) < (2, 4, 6, 8))  # That's why this prints False

# Step 4: Print out the average of the numbers in evens using one line of code
print(sum(evens) / len(evens))


# Step 5A: Write a function 'minmaxmean' that accepts an iterable and
#         returns the minimum value, the maximum value and the average (mean)
def min_max_mean(iterable):
    return min(iterable), max(iterable), sum(iterable) / len(iterable)


# Step 5B: Use print to confirm you function is working on evens and odds
print(min_max_mean(evens))
print(min_max_mean(odds))

# BONUS: Call your function with a new tuple of your own creation
#        And print the results in a pretty way
(min, max, avg) = min_max_mean(evens + odds + (25, 50, 75, 100))

print(f"Average: {avg}, Min: {min}, Max: {max}")
