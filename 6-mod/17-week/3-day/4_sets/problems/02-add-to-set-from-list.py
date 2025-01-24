# Given a set, `st`, and a list, `lst`, write a function, `add_to_set`, that
# merges the `st` to `lst` and returns the result.


# def add_to_set(st, lst):
#     st.update(lst)
#     return st

# ? Union
def add_to_set(st, lst):
    return st | set(lst)


st = {1, 2, 3, 4}
lst = [12, 4, 42, 93, 2, 85]

print(add_to_set(st, lst))  # { 1, 2, 3, 4, 42, 12, 85, 93 }
