## Today's Topics

- Classes
- Decorators

Here are some production applications to see things on a larger scale:
- https://github.com/Netflix/dispatch/tree/master/src/dispatch
- https://github.com/polarsource/polar/tree/main/server

## Decorators

### What's a decorator?

A decorator is a function that takes in another function as a callback and modifies or extends the behavior of the callback function.

---

### Decorators

Let's create a decorator that could be used for timing function calls.

```python
from datetime import datetime

# our decorator, which takes in a callback function
def timer(func):

    # define the wrapper function that we're going to return
    def wrapper():
        # get current time before function call
        before_time = datetime.now()

        # invoke the callback
        val = func()
        # log the return value of the function
        print(val)

        # get current time after function call
        after_time = datetime.now()

        # calculate total time
        total = after_time - before_time

        # return the total time
        return total

    # decorator returns the wrapper function object
    return wrapper
```

---

### Decorators

Using the `@decorator_name` syntax, we can shorten this:

```python
def my_function():
    return "hello"

my_function = timer(my_function)
```

To this:

```python=
@timer
def my_function():
    return "hello"
```

Decorating a function definition (with the `@decorator` syntax) does the same thing as reassigning the function name to the return value of the decorator.

---

### Passing arguments through a decorator

What if I want to wrap functions that take arguments... but I want to be flexible about what kind of arguments the function takes?

```python
from datetime import datetime

def timer(func):
    def wrapper(*args, **kwargs):
        before_time = datetime.now()
        val = func(*args, **kwargs)
        print(val)
        after_time = datetime.now()
        total = after_time - before_time
        return total

    return wrapper


@timer
def my_function_args(name):
    return f"hello {name}"

@timer
def my_sum(sum1, sum2):
    return sum1 + sum2
```

---

### Classes vs Dictionaries

---

In Python, the terms "dictionary" (often referred to using the type `dict`) and "object" can refer to different concepts, and understanding the distinction between them is important.

1. **Dictionary (`dict`):**

   - **Basic Definition:** A dictionary in Python is a built-in data type that stores data in key-value pairs.
   - **Mutable:** Dictionaries are mutable, meaning you can change, add, or remove key-value pairs after the dictionary has been created.
   - **Dynamic:** You can dynamically add new keys and values to a dictionary.
   - **Indexing:** Dictionaries are accessed via keys, not via index positions like lists.
   - **Syntax:** Defined with curly braces `{}`, with key-value pairs separated by colons. For example: `my_dict = {'key1': 'value1', 'key2': 'value2'}`.

2. **Object:**
   - **General Meaning:** In Python, everything is an object. This term is used broadly and refers to any instance of a class. Objects in Python are an encapsulation of variables (attributes) and functions (methods) into a single entity.
   - **Classes as Blueprints:** Objects are created from classes, which can be thought of as blueprints. A class defines attributes and methods, while an object is an instance of a class.
   - **Customization and Structure:** Objects are used for more structured data modeling. A class can have methods (functions that are defined within a class and can perform operations or actions using the object's attributes) and can enforce encapsulation and abstraction.

**Key Differences:**

- **Structure and Functionality:** Objects are more structured and can have their own methods and private data. Dictionaries are simple key-value stores without methods (apart from built-in dictionary methods).
- **Purpose:** Dictionaries are mainly used for storing and retrieving data via keys. Objects are used for creating structured data models, encapsulating data and behavior together.
- **Flexibility vs. Formality:** Dictionaries allow for a more flexible way of storing data; you can add any key-value pair at any time. Objects, defined by classes, have a more formal structure. You define what attributes and methods an object will have when you define its class.

In some contexts, especially when dealing with simple data structures, dictionaries and objects can serve similar purposes, such as storing data attributes. However, their usage, capabilities, and intentions are quite different, aligning with Python's diverse approaches to data representation and object-oriented programming.

---

### Creating Classes

To create a class we use the `class` keyword, and by convention, we capitalize the names of classes.

```python
# python example
class Icon:
    # more code to come
```

Python's constructor method is called `__init__()`.

```python
# python example
class Icon:
    def __init__(self, color, shape):
        self.color = color
        self.shape = shape
```

---

### Instances of classes

We create instances of a class by invoking the class as though it is a function (this invokes the class's `__init__()` method).

```python
# in python
my_new_icon = Icon("blue", "circle")
```

---

### Wait, what _is_ `self`?

`self` refers to the instance that a method was called on.

Whenever you invoke an instance method on a class instance, it is as though you are invoking the class's own method, and passing in the instance as an argument.

```python
some_icon = Icon("blue", "square")
# both below do the same thing
some_icon.my_method("other argument")
Icon.my_method(some_icon, "other argument")
```

---

### Instance variables and methods

You can set attributes on the instance with dot notation (`self.some_attribute = value`).

You can add instance methods to the class by defining functions and passing in `self`.

```python
class Icon:
    def __init__(self, color, shape):
        self.color = color
        self.shape = shape

    def my_method(self, word):
        print(f"hello {word}")
        return
```

---

### Class variables

Class variables are not attached to `self`. They are available for access on the class itself and across instances.

If we update a class variable on an instance, a shadow instance variable is created that hides the class variable of the same name.

```python
class Widget:
    price = "$5"
    def __init__(self, color):
        # instance variables
        self.color = color


my_widget = Widget("blue")
second_widget = Widget("chartreuse")
print(my_widget.price)  # "$5"
print(Widget.price)     # "$5"
my_widget.price = "$100"
print(second_widget.price) # "$5"
print(Widget.price)        # "$5"
Widget.price = "$50"
print(second_widget.price) # "$50"
print(my_widget.price)     # "$100"
```

---

### Class methods

We can use the `@classmethod` decorator to write class methods.

The first argument will refer to the class itself (conventionally called `cls`), rather than an individual instance.
They can modify class state but not instance state directly.

```python
# inside class
@classmethod
def widget_factory(cls, colors):
    widgets = [cls(color) for color in colors]
    print([widget.greet_widget() for widget in widgets])
    return widgets


print(Widget.widget_factory(["red",
"yellow", "beige"]))
```

---

### Static methods

Static methods don't take implicit arguments—they can't access the class or any instance of it.

- Defined using the @staticmethod decorator.
- Don’t require a reference to self.
- Can't access or modify class state.

```python
@staticmethod
def something_about_widgets():
    return "widgets are neat"
```

---

### Getters and setters

Getters & setters allow us to have methods that behave like properties.

They provide a convenient interface for implementing more complicated logic necessary for getting/setting a class property.

They can also be useful for protecting "private" values on your class.

---

### Getters

A getter allows you to define a method that behaves like a readable property. The `@property` decorator over a method creates a getter.

While the getter is a function, it is invoked as if it were a property.

```python
class Icon():
    def __init__(self, color, shape):
        self.color = color
        self.shape = shape

    # getter for ~secret~ password
    @property
    def my_password(self):
        return "somebody's secret password"

my_icon = Icon("blue", "square")
print(my_icon.color)

# call the getter method as if we were just
# reading a property
print(my_icon.my_password)
```

---

### Setters

A setter allows you to define a method that updates the getter "property". The decorator used to create a setter is `@<getter_method_name>.setter`.

You can have a standalone getter, but you must have a getter in order to have a setter. The setter method runs when you change the getter "property."

```python
class Icon():
    def __init__(self, color, shape, pswd):
        self.color = color
        self.shape = shape

        # set initial ~secret~ password
        # this calls the setter method!
        self.my_password = pswd

    # getter for ~secret~ password
    @property
    def my_password(self):
        return self._password

    # setter for ~secret~ password
    @my_password.setter
    def my_password(self, new_val):
        print("hashing password....")
        self._password =  str(new_val) + "12345" * 3

my_icon = Icon("blue", "square", "beepboop")
print(my_icon.my_password)

# call the setter method as if we were
# setting my_password as a regular property
my_icon.my_password = "new thing"
print(my_icon.my_password)
