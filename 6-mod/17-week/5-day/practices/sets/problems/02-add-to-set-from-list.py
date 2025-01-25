# Given a set, `st`, and a list, `lst`, write a function, `add_to_set`, that
# merges the `st` to `lst` and returns the result.

# Write your code here.
#!!ADD
def add_to_set(st, lst):
    pass
#!!END_ADD
#!!START SILENT
# Using .update
def add_to_set(st, lst):
    st.update(lst)
    return st

# Manual
def add_to_set2(st, lst):
    lst_to_set = set(lst)
    return st | lst_to_set
#!!END

st = { 1, 2, 3, 4 }
lst = [12, 4, 42, 93, 2, 85]

print(add_to_set(st, lst))    # { 1, 2, 3, 4, 42, 12, 85, 93 }