# In this problem, you'll explore the difference between a dictionary in Python
# and a plain-old JavaScript object. Try declaring a dictionary representing a
# cat using the same notation as you would in JavaScript, with the properties
# for `name`, `breed`, and `age`.

# Did you run into any errors executing your code? Try adding or removing
# quotations around the keys in your dictionary and see what effect that may
# have.

# Write your code here.
#!!START SILENT
# Fails
cat1 = {
    name: "Henry",
    breed: "Russian Blue",
    age: 7
}

# Successful creation
cat1 = {
    "name": "Henry",
    "breed": "Russian Blue",
    "age": 7
}

# In the first dictionary, Python interprets `name`, `breed`, and `age` as
# variables. Since they haven't been declared, it isn't a valid key.
#!!END
