# Write a function that takes in a name and returns an appropriate name tag for
# them from entries in a variable named `GUEST_LIST`. If the person's name does
# not exist in the guest list, make a name tag that says they're a guest.

GUEST_LIST = {
  "Kurt": "Germany",
  "Julia": "France",
  "Ito": "Japan",
  "Katherine": "England",
  "Sam": "Argentina"
}

# Write your function here.
#!!START SILENT
def greeting(name):
  if name not in GUEST_LIST:
    return "Hi! I'm a guest."
  return f"Hi! I'm {name} from {GUEST_LIST[name]}."
#!!END

print(greeting("Kurt"))   #> "Hi! I'm Kurt from Germany."
print(greeting("Sam"))    #> "Hi! I'm Sam from Argentina."
print(greeting("Monty"))  #> "Hi! I'm a guest."
