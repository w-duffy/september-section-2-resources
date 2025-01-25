# Create a function that takes in a tuple of strings. It should return a  tuple
# including only the strings that are greater than 8 letters in length.

# Write your function here.
#!!START SILENT
def big_words(tup):
  long_words_list = []
  for word in tup:
    if len(word) > 8:
      long_words_list.append(word)
  return tuple(long_words_list)

# alternate solution using list comprehension (wow,
# such beauty and concision; python truly is amazing)
def big_words(tup):
  return tuple([x for x in tup if len(x) > 8])
#!!END

print(big_words(('earth', 'jupiter', 'mars', 'neptune'))) #> ()
print(big_words(('wakanda', 'melbourne', 'london', 'france'))) #> ('melbourne',)
print(big_words(('app', 'academy', 'app academy', 'xylophone'))) #> ('app academy', 'xylophone')