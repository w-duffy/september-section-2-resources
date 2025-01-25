# Create a function that returns True if the first list can be nested inside the
# second. 

# list1 can be nested inside list2 if: 
# - list1's min is greater than list2's min
# - list1's max is less than list2's max 

# You may want to consider writing a couple of functions to organize your thoughts better.

# Write your code here.
#!!START SILENT
def list_max(lst):
  max = lst[0]
  for i in range(1, len(lst)):
    l = lst[i]
    if l > max:
      max = l
  return max

def list_min(lst):
  min = lst[0]
  for i in range(1, len(lst)):
    l = lst[i]
    if l < min:
      min = l
  return min

def can_nest(list1, list2):
  list1_min = list_min(list1)
  list1_max = list_max(list1)
  list2_min = list_min(list2)
  list2_max = list_max(list2)
  return list1_min > list2_min and list1_max < list2_max
#!!END

print(can_nest([1, 2, 3, 4], [0, 6]))  #> True
print(can_nest([3, 1], [4, 0]))        #> True
print(can_nest([9, 9, 8], [8, 9]))     #> False
print(can_nest([1, 2, 3, 4], [2, 3]))  #> False