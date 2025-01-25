# It's time to explore the *range* object and how to use it with loops.

# Follow the instructions in the code comments. Be sure to test your work by
# running your code!

print('THREE CASES FOR RANGE')
print('A) End Value')

# STEP 1: Change the zero in the range to 10
#         Notice how "10" is not included in the output
#!!ADD
for i in range(0):
    print(i)
#!!END_ADD
#!!START SILENT
for i in range(10):
    print(i)
#!!END

print('B) Start & End Values')

# STEP 2: Code a `for` loop to print numbers 5 through 9
#!!START SILENT
for i in range(5,10):
    print(i)
#!!END

print('C) Only Even Values')

# STEP 3: Print 0, 2, 4, 6 and 8 using a for loop
#         Hint - range can take a 3rd parameter for the step distance
#!!START SILENT
for i in range(0,10,2):
    print(i)
#!!END
