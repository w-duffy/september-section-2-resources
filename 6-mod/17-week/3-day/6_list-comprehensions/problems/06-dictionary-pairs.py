# Create a function that takes in a list of  `key` and list of `value` argument
# that returns a dictionary of key/value pairs.


def dictionary_pairs(keys, values):
    return {keys[i].title(): values[i] for i in range(len(keys))}


print(
    dictionary_pairs(["name", "age", "food"], ["James", 24, "steak"])
)  # > {'Name': 'James', 'Age': 24, 'Food': 'steak'}
print(
    dictionary_pairs(["name", "age", "food"], ["Vivian", 21, "sushi"])
)  # > {'Name': 'Vivian', 'Age': 21, 'Food': 'sushi'}
print(
    dictionary_pairs(["name", "age", "food"], ["Alex", 6, "chocolate"])
)  # > {'Name': 'Alex', 'Age': 6, 'Food': 'chocolate'}
