# Create a function that returns a list of tuples that are sorted by the sum of
# the tuples. Hint: use the built-in range function. #! but why


def bubble_sum(tup_lst):
    return sorted(tup_lst, key=lambda el: sum(el))


print(
    bubble_sum([(3, 5), (1, 3), (6, 5), (2, 8)])
)  # > [(1, 3), (3, 5), (2, 8), (6, 5)]
print(
    bubble_sum([(2, 5), (2, 5), (7, 8), (2, 6)])
)  # > [(2, 5), (2, 5), (2, 6), (7, 8)]
print(
    bubble_sum([(5, 6), (1, 2), (3, 0), (2, 4)])
)  # > [(1, 2), (3, 0), (2, 4), (5, 6)]
print(
    bubble_sum([(5, 4), (1, 0), (2, 1), (4, 1)])
)  # > [(1, 0), (2, 1), (4, 1), (5, 4)]
