# It's Python Time!

https://www.pythoncheatsheet.org/cheatsheet/basics

Python Introduction

- Booleans
- Strings
- Numbers

## Booleans

```js
//JS
true && false;
true || false;
true && !false;
```

```py
#Py
True and False
True or False
True and not False
```

```js
//falsy values for js
false;
0 - 0;
0n;
'', '', ``;
null;
undefined;
NaN;
```

```py
#falsy values for py
None
False
0
0.0
''
[]
()
{}
set()
range(0)
```

Truthy and Falsy values (Boolean type coercion) differ in JS and Python. One common gotcha is empty
collections (reference types) are truthy in JS and falsy in Python.

## Strings

Strings are basically the same in python and JavaScript, but the methods
assosiated with strings are different.

```js
//JS
'hello'.length; //5
'hello'[4]; //o
'hello'.slice(0, 2); //he
'hello' + ' ' + 'world';
let word1 = 'hello';
let word2 = 'world';
let sentence = `${word1} ${word2}!`;
```

```py
#Py
len('hello') #5
# negative indexing is a thing
'hello'[4] or 'hello'[-1] #o
# built in range functionality is a thing
'hello'[0:2] # he
'hello' + ' ' + 'world'
'hello ' * 3
word_1 = 'hello'
word_2 = 'world'
format_sentence = '{0} {1}!'.format(word1, word2)
fstring_sentence = f'{word1} {word2}!' #fstring, newest syntax introduced in python 3.6
questions = 20
num_correct = 10
score = f'You got {num_correct/questions:%}'
score = f'You got {num_correct/questions:.0%}'
```

[format spec](https://docs.python.org/3/library/string.html#formatspec)

## Numbers

int -- whole numbers, both positive and negative
float -- numbers with a decimal point

integer division -- whole number division

```py
#Py
print(20 / 6) # 3.33333
print(20 // 6) # 3 integer division
```

++ and -- do not exist in python

## Assigning and Manipulating Variables

no variable declaration keywords `variable = 0`

chaining declarations is possible `count = max = min = 0`

value and type of a variable can be reassinged at any time

NaN doesn't exist! Python throws an exception (error) when math operations are
attempted on types that dont support those operations.

## None Type

pythons version of null

## is vs == (identity vs equality / reference vs value)

```py
print (2 == '2')    # => False
print (2 is '2')    # => False
print ("2" == '2')    # => True
print ("2" is '2')    # => True
print (2 == 2.0)    # => True
print (2 is 2.0)    # => False
obj1 = {'hello': 'world'}
obj2 = {'hello': 'world'}
print(obj1 == obj2) # => True
print(obj1 is obj2) # => False
```

## If statements

If statements in python are made up of the following

- the `if` keyword
- an expression that evaluates to True or False (a condition) `a == b`
- a colon `:`
- an indented block to execute if the condition evaluates to True

```py
name = 'Tony'
if name == 'Tony':
  print('Hello Tony')
elif name == 'Peter':
  print('Hello Peter')
else:
  print('Hello')
```

## Loops

### While

```py
count = 0
while count < 5:
  print(count)
  count += 1
  #break exits the loop
  #pass continues the current iteration
  #continue moves on to the next iteration immediately
```

### For

```py
# standard for loop
word = 'hello'
for letter in word:
  print(letter)
# if you need an index
for i in range(len(word)):
  print({i: word[i]})
```

## Error Handling

```py
# simple error catching
a = 321
try:
    print(len(a))
except:
    print('Silently handle error here')
    # Optionally include a correction to the issue
    a = str(a)
    print(len(a))
```

```py
#catching named errors
a = 100
# b = "5"
# b = 0
# b = 5
try:
    print(a / b)
except ZeroDivisionError:
    pass
except (TypeError, NameError) as e:
    print("ERROR!", e)
finally:
    print("Finally...")
```

## Functions

- Naming convention is snake_case
- declaration is basically the same as JS with `function` replaced by `def` and
  `{}` replaced by `:` and an indented block.

```py
def i_am_a_function():
  print('fun fun function')
i_am_a_function()
```

---

### Function Parameters and Arguments

The biggest difference between JS and Python functions is in parameters and
arguments. JS has exclusively positional arguments. Python has positional
arguments and keyword arguments.

You should order parameters and arguments in this order.

1. positional arguments
2. \*args
3. keyword arguments with default values
4. \*\*kwargs

```py
# positional: a positional argument, works the same way as JS
# (*)args: any extra arguments that don't have a positional parameter. Type is a Tuple. Similar to rest parameter in js
# default: keyword argument with default value
# (**)kwargs: any arguments with a key=value pairing. Type is a Dictionary.
def parameters(positional, *args, default='default', **kwargs):
  print(positional, args, default, kwargs)
parameters('hello', 1,2,3,4, test='test', world='earth')
# It is considered best practice to use positional arguments for parameters without default values and keyword arguments for parameters with default values
def default_value(a, b='b'):
  print(a, b)
default_value('a')
default_value('a', 'c')
default_value('a', b='d')
```

---

### Anonymous Function

Lambda functions are not as flexible as arrow functions in JS. While arrow
functions can be treated mostly like a normal function, a lambda function is
intended to be a simple one liner. It is meant to do a single task. Great where
it is able to used, but not a replacement for normal functions.

```js
const yell = (input) => input.toUpperCase();
console.log(yell('hello'));
```

```py
yell = lambda input: input.upper()
print(yell('hello'))
```

---

## Structured Data

---

### Sequences

Each item in a sequence is assigned an index which determines the order of the
sequence. Zero indexed.

- strings
- lists
- tuples
- ranges

---

### Collections

Instead of indexes, collections use hashable values.
A hashable value is something which never changes during its lifetime. All
immutable data types are hashable no mutable data types are hashable.

- dictionaries
- sets

---

### Iterables

They are your collections and sequences

---

## Data Types

---

### List

Very similar to JS arrays, lists are used to store a sequence of item. Typically
lists are homogeneous (of one type) by convention, but the data types itself
does not require that.

Lists are mutable.

Lists are instantiated using `[]`

---

### Range

Ranges are an immutable list of numbers.

Ranges are declared using one to three parameters

- start: (optional -- default value = 0) first number in the sequence
- stop: (required) -- next number past the last number in the sequence
- step (optional -- default value = 1) - the difference between each number in
  the sequence.

---

### Tuple

Very similar to Lists, the biggest difference is that tuples are immutable.

Tuples are instantiated using `()`

---

### Dictionary

A mappable collection where a hashable value is used as a key to reference a
value. Very similar to JS objects.

Dictionaries are instantiated using `{key:value}`

---

### Set

A set is an unordered collection of unique hashable values.

Sets are instantiated using set(), `{value, value}`

---

## Lists

```py
my_empty_list = []
print(my_empty_list) #> []
nums = [1,2,3,4]
print(nums)        #> [1,2,3,4]
print(nums[0])     #> 1
print(nums[3])     #> 4
print(nums[-1])    #> 4
print(nums[1:2])   #> [2]
print(nums[::2])   #> [1, 3]
print(nums[20])    #> IndexError: list index out of range
print(len(nums))   #> 4
print('total', sum(nums))   #> 10
print('max', max(nums))     #> 4
print('min', min(nums))     #> 1
print('avg', sum(nums) / len(nums)) #> 2.5
print('reverse', sorted(nums, reverse=True)) #> [4,3,2,1]
nums.append(5)
print(nums) #> [1,2,3,4,5]
nums.remove(4)
print(nums) #> [1,2,3,5]
del nums[0]
print(nums) #> [2,3,5]
del nums[:]
print(nums) #> []
other_nums = [5,6,7,8]
# *: splat operator, unpacks data from the collection, similar to spread operator
print([*nums, *other_nums]) #> [1,2,3,4,5,6,7,8]
```

some common list methods:

- append: adds an element to the end of the lists
- remove: remove the first item with the specified value
- copy: returns a copy of the list
- insert: adds an element at the specified position
- pop: removed an element at the specified position
- sort: sorts the list

other useful list methods:

- count: return the number of times x appears in the list
- reverse: reverse the elements of the list in place
- extend: extend the list by appending all the items from the iterable
- clear: remove all items from the list

## List Comprehensions

```py
[expression (optional if -> else) for element in iterable (optional if expression)]

nums = [1,2,3,4,5]
doubled = [x*2 for x in nums]
even_doubled = [x*2 for x in nums if x % 2 == 0]
even_double_odd_zero = [x*2 if x % 2 == 0 else 0 for x in nums if x != 1]

print(doubled)
print(even_doubled)
print(even_double_odd_zero)

def is_prime(num):
  for i in range(2, num):
    if num%i == 0:
      return False
  return True

res = [x for x in range(25) if x > 1 and is_prime(x)]

print(res)
```
