# Given a list of `Cat` objects (dictionaries representing cats), write a
# function `cat_verify` that uses the `all()` built-in function to determine if
# all cats are the same breed. Then use `any()` to determine if any of them are
# up for adoption. Return the result as a tuple.

# The `breed` represents the cat's breed, and `adopted` represents whether the
# cat bas been adopted already or not.

cat_list = [
    {
        "name": "Lenny",
        "breed": "Ragdoll",
        "adopted": False
    },
    {
        "name": "Roger",
        "breed": "Siamese",
        "adopted": False
    },
    {
        "name": "Katya",
        "breed": "Persian",
        "adopted": True
    }
]

# Write your code here.
#!!ADD
def cat_verify(cats):
    pass
#!!END_ADD
#!!START SILENT
def cat_verify(cats):
    # Same breed
    cat_breed = all(map(lambda cat: cat['breed'] == cats[0]['breed'], cats))
    
    # Up for adoption
    up_for_adoption = any(map(lambda cat: cat['adopted'] == False, cats))

    # Return result as tuple
    return (cat_breed, up_for_adoption)
#!!END

print(cat_verify(cat_list))    # False