# Write a function that returns `True` if a dictionary is empty, and `False`
# otherwise.

# Write your function here.
#!!START SILENT
def is_empty(d):
  return not d
#!!END

print(is_empty({}))        #> True
print(is_empty({"a": 1}))  #> False