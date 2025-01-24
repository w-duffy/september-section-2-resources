# Function Decoration and Introspection

## Decorators

A function that returns another function

Main purpose is to modify the behavior of a callback

We've been capable of doing this in JS, but haven't had much incentive to structure our code this way

```js
const js_decorator = (func_being_decorated) => {
  return (another_arg) => {
    another_arg += 'something happened';
    return func_being_decorated(another_arg);
  };
};

let my_func = (arg) => {
  // Pretend this function does something
  return arg;
};

my_func = js_decorator(my_func);

console.log(my_func('Pretend '));
```

Python's version would look like this

```py
# JavaScript-y way of using decorators
# Messy, hard to follow with complex functions
def my_func(arg):
    # Pretend this function does something
    return arg


def my_decorator(func_being_decorated):
    def wrapper(another_arg):
        another_arg += 'something happened again'
        return func_being_decorated(another_arg)
    return wrapper


my_func = my_decorator(my_func)

print(my_func('Pretend '))
```

This is used far more in Python than JS, so we have some nicer syntax to work with

`@decorator` is just syntactic sugar, but improves readability

```py
# Looks cleaner, you'll be seeing this a lot later
def my_decorator(func_being_decorated):
    def wrapper(another_arg):
        another_arg += 'something happened again'
        return func_being_decorated(another_arg)
    return wrapper


@my_decorator
def my_func(arg):
    # Pretend this function does something
    return arg


print(my_func('Pretend '))
```

One more breakdown to hopefully make it more clear

```py
@my_decorator
def my_func(arg):
    return arg

# is the same as saying

my_func = my_decorator(my_func)

# which is technically

my_func = wrapper_with_my_func_inside
```

When you invoke `my_func`, you're running `wrapper` from the decorator.

`wrapper` has `my_func` inside of it, so it runs `my_func`

## Introspection

The ability to look into a function's inner workings

Makes complex/nested functions easier to understand and work with

```py
@my_decorator
def my_func(arg):
    return arg

print(my_func)
print(dir(my_func))
print(my_func.__closure__)
print(my_func.__closure__[0].cell_contents)
```

### Viewing Closures

```py
def greeting_maker(hello_word):
    def name_input(name):
        return f'{hello_word}, {name}!'
    return name_input


hello_greeting = greeting_maker('hello')
print(hello_greeting.__closure__)  # notice you get back a tuple

# the first item in the tuple, in this case the only item
print(hello_greeting.__closure__[0])

# the value held in the closure
print(hello_greeting.__closure__[0].cell_contents)
```

### Viewing Decorators

```py
# basic decorators
def greeting_decorator(greeting_func):
    # 1. decorator function intakes a function to invoke
    # 2. wrapper function is defined
    def greeting_wrapper(name):
        # 3. code to run
        # 4. decorator functions argument is invoked
        print(f'{greeting_func()}, {name}!')
    # 5. wrapper function is returned
    return greeting_wrapper


def hello():
    return 'Hello'


print("default func:", hello)  # <function hello at 0x7fe04abf6af0>
print("default func is closure?:", hello.__closure__)  # None
hello = greeting_decorator(hello)
print("closure func:", hello)
# <function greeting_decorator.<locals>.greeting_wrapper at 0x7f186b2d9c10>
print("closure func closure:", hello.__closure__)
# (<cell at 0x7f186b2e1fd0: function object at 0x7f186b2d9af0>,)
print("closure func closure contents:",
      hello.__closure__[0].cell_contents)
# <function hello at 0x7f3125a26af0>


# syntactic sugar for howdy = greeting_decorator(howdy)
@greeting_decorator
def howdy():
    return 'Howdy'


print('howdy decorated:', howdy)

```

## Decorator Problems (40m)
