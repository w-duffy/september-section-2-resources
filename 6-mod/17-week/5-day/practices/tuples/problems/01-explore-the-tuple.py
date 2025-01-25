# It's time to explore the *tuple* object and how to use it.

# Follow the instructions in the code comments. Be sure to test your work by
# running your code!

# For the bonus, remember you can split a returned tuple to variables: `(a,b,c)
# = myfunc()`

# DO NOT EDIT
odds = 1,3,5,7,9
evens = 2,4,6,8

# Step 1: Print out the result of adding evens to odds
#!!START SILENT
print(odds+evens)
#!!END

# Step 2: Print out the result of multiplying odds by three
#!!START SILENT
print(odds*3)
#!!END

# Step 3A: Use print to find out if odds is less than evens
#!!START SILENT
print(odds < evens)
#!!END

# Step 3B: Print out your explanation of why 3A has that result
#!!START SILENT
print('First item in odds (1) is < first item in evens (2), so odds < evens.')
#!!END

# Step 4: Print out the average of the numbers in evens using one line of code
#!!START SILENT
print(sum(evens)/len(evens))
#!!END

# Step 5A: Write a function 'minmaxmean' that accepts an iterable and
#         returns the minimum value, the maximum value and the average (mean)
#!!START SILENT
def minmaxmean(iterable):
    return min(iterable), max(iterable), sum(iterable)/len(iterable)
#!!END

# Step 5B: Use print to confirm you function is working on evens and odds
#!!START SILENT
print(minmaxmean(evens))
print(minmaxmean(odds))
#!!END

# BONUS: Call your function with a new tuple of your own creation
#        And print the results in a pretty way
#!!START SILENT
(low,high,ave) = minmaxmean((22, 33, 44, 55, -7, 16, 123))
print('Average is {2} with range from {0} to {1}.'.format(low, high, ave))
#!!END