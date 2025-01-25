# In Python, lambda functions work as anonymous functions that evaluates to a
# single expression. You could say it's a little more petite than its JavaScript
# counterpart.

# Write a function `string_multi_print` that accepts a string, `str`, and
# returns a lambda that prints `str` `i` times.

# Write your code here.
#!!ADD
def string_multi_print(str):
    pass
#!!END_ADD
#!!START SILENT
def string_multi_print(str):        # Prints 1 concatenated string
    return lambda i : print(str * i)

def string_mutli_print_2(str):      # Prints `str` on a new line `i` times
    return lambda i : print((str + "\n") * i)
#!!END

string_multi_print('hello ')(2)  # Prints "hello hello "
string_multi_print('wahoo ')(3)  # Prints "wahoo wahoo wahoo "