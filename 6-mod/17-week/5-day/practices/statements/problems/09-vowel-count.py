# Create a function called `vowel_count` that takes in a string and returns a
# count of how many vowels are in the string.

# Write your solution here.

#!!START SILENT
def vowel_count(string):
  count = 0
  vowel = "aeiouAEIOU"
  for i in string:
    if i in vowel:
      count += 1
  return count
#!!END

print(vowel_count("App Academy"))         #> 4
print(vowel_count("Coding Expert"))       #> 4
print(vowel_count("Supreme"))             #> 3
print(vowel_count("Chamber of Secrets"))  #> 5