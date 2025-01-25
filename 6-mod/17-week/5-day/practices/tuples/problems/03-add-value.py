# Create a function that takes in a tuple, `tup` and a value, `val`. The
# function should return a tuple with the given value added to the end of the
# tuple.

# Write your function here.
#!!START SILENT
def add_value(tup, val):
  lst = list(tup)
  lst.append(val)
  return tuple(lst)
#!!END

print(add_value((1,2,3,4), 5)) #> (1, 2, 3, 4, 5)
print(add_value(("a", "b", "c"), "d")) #> ('a', 'b', 'c', 'd')
print(add_value((8, 9, "d", 6), "a")) #> (8, 9, 'd', 6, 'a')