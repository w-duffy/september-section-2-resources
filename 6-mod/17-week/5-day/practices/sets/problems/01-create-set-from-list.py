# Given a list of items, create a set from the list. Note the differences with
# performing the same action in JavaScript.

# Write your code here.

#!!ADD
# # (Hint: Does declaring a new set require any keywords like `new`?)
#!!END_ADD

#!!START SILENT
lst = [1, 2, 3, 4, 1, 3, 5]
set_of_lst = set(lst)

# Alternatively, add list to empty set.
st = set()
st.update(lst)
#!!END