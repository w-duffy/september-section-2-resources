# It's time to explore the *list* object and how to use it Follow the
# instructions in the code comments. Be sure to test your work by running your
# code!

# DO NOT EDIT - Starting with a simple lists of colors and numbers
colors = ["blue", "Green", "PURPLE", "blue-green", "sky blue"]
numbers = [2, 34, 8.5, -22.0, 33//4, 2**5]
print ('COLORS', colors)
print ('NUMBERS', numbers)

# 1. Print the total number of colors (length of the list)
#!!START SILENT
print(len(colors))
#!!END

# 2. Print the first color
#!!START SILENT
print(colors[0])
#!!END

# 3. Print the second and third colors
#!!START SILENT
print(colors[1:3])
#!!END

# 4. Print the last two colors
#!!START SILENT
print(colors[-2:])
#!!END

# 5. Print the smallest number in the numbers list
#!!START SILENT
print(min(numbers))
#!!END

# 6. Print the largest number in the numbers list
#!!START SILENT
print(max(numbers))

# 7. Sort the numbers
#!!START SILENT
numbers = sorted(numbers)
# Also acceptable: numbers.sort()
#!!END

# UNCOMMENT WHEN YOU WORK ON #7
#!!ADD
# print ('SORTED NUMBERS', numbers)
#!!END_ADD
#!!START SILENT
print ('SORTED NUMBERS', numbers)
#!!END

# 8. Sort the colors alphabetically ignoring case
#!!START SILENT
colors = sorted(colors, key=str.lower)
# Also acceptable: colors.sort(key=str.lower)
#!!END

# UNCOMMENT WHEN YOU WORK ON #8
#!!ADD
# print ('SORTED COLORS', colors)
#!!END_ADD
#!!START SILENT
print ('SORTED COLORS', colors)
#!!END