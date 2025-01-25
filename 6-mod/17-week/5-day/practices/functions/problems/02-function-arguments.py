# In Python, default and keyword arguments are allowed, similar to JavaScript.
# Write a function that accepts at least 2 arguments, with at least one that has
# a default value. Try moving the position of the positional and default
# arguments' declaration and see what happens!

# Write your code here.

#!!START SILENT
# Trying to declare functions with default arguments in various positions.
def sample_function_1(input1 = 'Hello World', input2, input3):  # ERROR
    print(input1 + input2 + input3)

def sample_function_2(input1, input2 = 'Hello World', input3):   # ERROR
    print(input1 + input2 + input3)

def sample_function_3(input1, input2, input3 = 'Hello World'):  # NO ERROR
    print(input1 + input2 + input3)

# Defaulted arguments should go last in both function declaration and usage.
#!!END

#!!ADD
sample_function(input = "asdf", "a", "b")      # ERROR
sample_function("asdf", input = "a", "b")      # ERROR
sample_function("asdf", "a", input = "b")      # VALID
#!!END_ADD

#!!START SILENT
sample_function_1(input = "asdf", "a", "b")      # ERROR
sample_function_2("asdf", input = "a", "b")      # ERROR
sample_function_3("asdf", "a", input = "b")      # VALID
#!!END