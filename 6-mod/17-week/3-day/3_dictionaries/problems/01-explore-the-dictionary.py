# It's time to explore the *dictionary* object and how to use it.

# Follow the instructions in the code comments.

# Be sure to test your work by running your code!

# There are two ways to declare dictionaries
# Create a dictionary and assign it to the d1 variable using the dict()
# constructor that has key/value pairs
#   key: "module", value: "Python 3"
#   key: "subject", value: "Dictionaries"
d1 = dict(module="Python 3", subject="Dictionaries")

# Create a dictionary and assign it to the d2 variable using the dictionary
# literal that has key/value pairs
#   key: "module", value: "Python 3"
#   key: "subject", value: "Dictionaries"
d2 = {"module": "Python 3", "subject": "Dictionaries"}


# Convert d1 to a list using the list() method. Then, print it. What gets
# put into the list?
d1_as_list = list(d1)

# print(d1_as_list)  # ['module', 'subject'] #! Keys only
# print(list(d1.values())) # ['Python 3', 'Dictionaries'] #! Values
# print(tuple(d1.values())) # ('Python 3', 'Dictionaries') #! Values
# print(list(d1.items()))  # Just like Object.entries()

# # ? DESTRUCTURE!!!! More like array destructuring than anything else
# first_kv_pair, second_kv_pair = list(d1.items())

# print(dir(d1))

# Unlike JavaScript, the keys in Python dictionaries can be any kind of
# value, not just strings or Symbols. Add a key to d1 that is the number
# one with the value "one". Then, add another key to d1 that is a string
# that contains the character 1 and give it the value of "one". Then,
# print the dictionary to see what's in there.

d1[1] = "one"
d1["1"] = "one as well"

print(d1)


# Now, check that the following keys are in d1 by printing out if they do exist.
#  "module"    should be True
#  "subject"   should be True
#  "age"       should be False
#  1           should be True
#  "1"         should be True
#  "one"       should be False
#  True        should be False #! BUT IT DOESN'T HAHAHAH CLASSIC

# if "subject" in d1:
#     print("Yes")
# else:
#     print("No")

# print("'module' in d1:", "module" in d1)
# print("'subject' in d1:", "subject" in d1)
# print("'age' in d1:", "age" in d1)
# print("1 in d1:", 1 in d1)
# print("'1' in d1:", "1" in d1)
# print("'one' in d1:", "one" in d1)
# print("True in d1:", True in d1)

# print(True == 1)
# print(True is 1)

# print(
#     {"module": "Python 3", "subject": "Dictionaries", 1: "one", "1": "one as well"}
#     == {"module": "Python 3", "subject": "Dictionaries", 1: "one", "1": "one as well"}
# )
# print(
#     {"module": "Python 3", "subject": "Dictionaries", 1: "one", "1": "one as well"}
#     is {"module": "Python 3", "subject": "Dictionaries", 1: "one", "1": "one as well"}
# )

# if 4:
#     print("True!")
# else:
#     print("False :(")

print(True == 4)
