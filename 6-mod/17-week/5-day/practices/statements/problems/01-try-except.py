# In Python, error handling can be done using a `try`/`except` block. Implement
# `except` blocks to handle the exceptions that will be raised for the following
# `try` blocks:

# Example 1
try:
    str = 'hello'
    str[0] = 'm'
    print(str)
#!!START SILENT
except TypeError as e:
    print(e, "... because strings are immutable!")
#!!END
finally:
    print('I happen regardless of any exceptions.')

# Example 2
try:
    print(x)
#!!START SILENT
except NameError as e:
    print(e)
#!!END
finally:
    print('I happen regardless of any exceptions.')