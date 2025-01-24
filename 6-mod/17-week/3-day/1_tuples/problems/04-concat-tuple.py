# Create a function that returns a concatenated tuple.


def concat_tuple(tup, le):
    return tup + le


print(
    concat_tuple((5, 8, 9, 2, 3, 1, 4, 2), (5, 8, 9, 2, 3, 1, 4, 2))
)  # > (5, 8, 9, 2, 3, 1, 4, 2, 5, 8, 9, 2, 3, 1, 4, 2)
print(concat_tuple((5, 8, 9), ("a", "b")))  # > (5, 8, 9, 'a', 'b')
print(concat_tuple(("a", "b", "c"), (8.0, 5.7, 9)))  # > ('a', 'b', 'c', 8.0, 5.7, 9)
