# Given a list of `Cat` objects (dictionaries representing cats), write a
# function `cat_verify` that uses the `all()` built-in function to determine if
# all cats are the same breed. Then use `any()` to determine if any of them are
# up for adoption. Return the result as a tuple.

# The `breed` represents the cat's breed, and `adopted` represents whether the
# cat bas been adopted already or not.

cat_list = [
    {"name": "Lenny", "breed": "Ragdoll", "adopted": False},
    {"name": "Roger", "breed": "Siamese", "adopted": False},
    {"name": "Katya", "breed": "Persian", "adopted": True},
]

# map(() => , arr)
# arr.map(() =>)


# Write your code here.
def cat_verify(cats):
    # same_breed = all(
    #     [True if el["breed"] == cats[0]["breed"] else False for el in cats ]
    # )
    same_breed = all(map(lambda el: el["breed"] == cats[0]["breed"], cats))
    can_adopt = any([not el["adopted"] for el in cats])

    # return same_breed, can_adopt # ? Instructions say this...???
    return same_breed and can_adopt


print(cat_verify(cat_list))  # False
