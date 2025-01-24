# Write a function that takes in a name and returns an appropriate name tag for
# them from entries in a variable named `GUEST_LIST`. If the person's name does
# not exist in the guest list, make a name tag that says they're a guest.

GUEST_LIST = {
    "Kurt": "Germany",
    "Julia": "France",
    "Ito": "Japan",
    "Katherine": "England",
    "Sam": "Argentina",
}


def greeting(name):
    msg = "Hi! I'm "

    if name in GUEST_LIST:
        msg += name + f" from {GUEST_LIST[name]}"
    else:
        msg += "a guest"

    return msg + "."


# def greeting(name):
#     return (
#         f"Hi! I'm {name} from {GUEST_LIST[name]}."  # GUEST_LIST[name] ?
#         if name in GUEST_LIST  # `Hi! I'm ${name} from ${GUEST_LIST[name]}.` :
#         else "Hi I'm a guest."  # "Hi I'm a guest."
#     )


print(greeting("Kurt"))  # > "Hi! I'm Kurt from Germany."
print(greeting("Sam"))  # > "Hi! I'm Sam from Argentina."
print(greeting("Monty"))  # > "Hi! I'm a guest."
