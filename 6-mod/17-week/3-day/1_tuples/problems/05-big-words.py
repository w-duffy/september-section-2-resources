# Create a function that takes in a tuple of strings. It should return a  tuple
# including only the strings that are greater than 8 letters in length.


def big_words(tup):
    return tuple([el for el in tup if len(el) > 8])


print(big_words(("earth", "jupiter", "mars", "neptune")))  # > ()
print(big_words(("wakanda", "melbourne", "london", "france")))  # > ('melbourne',)
print(
    big_words(("app", "academy", "app academy", "xylophone"))
)  # > ('app academy', 'xylophone')
