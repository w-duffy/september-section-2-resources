# It's time to explore the *dictionary* object and how to use it.

# Follow the instructions in the code comments. 

# Be sure to test your work by running your code!

# There are two ways to declare dictionaries
# Create a dictionary and assign it to the d1 variable using the dict()
# constructor that has key/value pairs
#   key: "module", value: "Python 3"
#   key: "subject", value: "Dictionaries"
#!!ADD
d1 = # Your declaration here
#!!END_ADD
#!!START SILENT
d1 = dict(module="Python 3", subject="Dictionaries")
#!!END

# Create a dictionary and assign it to the d2 variable using the dictionary
# literal that has key/value pairs
#   key: "module", value: "Python 3"
#   key: "subject", value: "Dictionaries"
#!!ADD
d2 = # Your declaration here
#!!END_ADD
#!!START SILENT
d2 = {"module": "Python 3", "subject": "Dictionaries"}
#!!END

# Unlike JavaScript, the keys in Python dictionaries can be any kind of
# value, not just strings or Symbols. Add a key to d1 that is the number
# one with the value "one". Then, add another key to d1 that is a string
# that contains the character 1 and give it the value of "one". Then,
# print the dictionary to see what's in there.
#!!START SILENT
d1[1] = "one"
d1["1"] = "one"
print(d1)
#!!END

# Convert d1 to a list using the list() method. Then, print it. What gets
# put into the list?
#!!ADD
d1_as_list = # Your conversion here
#!!END_ADD
#!!START SILENT
d1_as_list = list(d1)
print(d1_as_list)
#!!END


# Now, check that the following keys are in d1 by printing out if they do exist.
#!!START SILENT
# The first one is there for you.
#!!END
#  "module"    should be True
#  "subject"   should be True
#  "age"       should be False
#  1           should be True
#  "1"         should be True
#  "one"       should be False
#  True        should be False
#!!START SILENT
print(f"'module' in d1? {'module' in d1}")
#!!END