# Given a list of items, create a set from the list. Note the differences with
# performing the same action in JavaScript.

list_of_items = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]

# set_of_items = set(list_of_items)

set_of_items = set()
set_of_items.update(list_of_items)

print(set_of_items)

# ! Not a dict
not_a_dict = {1, 1, 2, 2, 3, 3}
print(not_a_dict)  #! {1, 2, 3}
