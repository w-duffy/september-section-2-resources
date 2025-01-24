# Python Classes Give You UNLIMITED POWER 😈

Classes are a combination of information and behavior. A blueprint that allows
you to make objects with predefined attributes.

```js
// simple js class
class Dog {
  constructor(name) {
    this.sound = 'woof'
    this.name = name
  }
}

const fido = new Dog("fido");
const rex = new Dog("rex");
console.log(myDog);
```

```py
# simple py class
class Dog:
    # doesn't have to be self, but is always self by convention
    def __init__(self):
        self.sound = 'woof'


my_dog = Dog()
print(my_dog)
print(my_dog.sound)
```

```py
# using methods
class Dog:
    def __init__(self):
        self.sound = 'woof'

    def make_sound(self):
        print(self.sound)

    def change_sound(self, sound):
        self.sound = sound


my_dog = Dog()
my_dog.make_sound()
# notice that we aren't passing in self
# python does this automatically
my_dog.change_sound('bark')
my_dog.make_sound()
```

## Dunder methods

Dunder methods (double underscore methods) like `__init__` and `__doc__`are special methods in
python, usually dealing with built in behaviors or properties.

```py
# setting initial state
class Dog:
    """
    This is just a description of the class.
    This helps other devs understand how to use your class
    It expects to receive the positional arguments
    (str:name, str:sound)
    """

    def __init__(self, name, sound):
        self.name = name
        self.sound = sound


dog_1 = Dog('Callie', 'woof')
print(dog_1.name, dog_1.sound)
print(dog_1.__doc__)
```

```py
# private variables
class Dog:
    def __init__(self, name, sound):
        """
        Use a leading underscore on instance variables
        that shouldn't be accessed when using the class.
        This isn't an actual python feature, its a convention.
        All instance variables should be private,
        except for any variables you explicitly want to be public
        """
        self._name = name
        self._sound = sound

    def get_name(self):
        return self._name

    def get_sound(self):
        return self._sound


dog_1 = Dog('Callie', 'woof')
print(dog_1.get_name(), dog_1.get_sound())
```

```py
# reserving memory
class Dog:
    # Not required, just a memory optimization
    # Python devs will often build a class, then fill in slots last
    __slots__ = ['_name', '_sound']

    def __init__(self, name, sound):
        self._name = name
        self._sound = sound

    def get_name(self):
        return self._name

    def get_sound(self):
        return self._sound


dog_1 = Dog('Callie', 'woof')
print(dog_1.get_name(), dog_1.get_sound())
```

```py
# Pretty printing: because
# <__main__.Dog object at 0x7f36545b5fd0>
# is ugly
class Dog:
    __slots__ = ['_name', '_sound']

    def __init__(self, name, sound):
        self._name = name
        self._sound = sound

    def get_name(self):
        return self._name

    def get_sound(self):
        return self._sound

    def __repr__(self):
        # Another fancy dunder method
        # python will use this whenever you try to print
        # an instance of this class
        return f'<Dog (name: {self._name}, sound: {self._sound})>'


dog_1 = Dog('Callie', 'woof')
print(dog_1)
```

## Builtin Class Decorators

These decorators allow us to convert class methods into properties

Makes code easier to use and more uniform

Without decorators, we must invoke each method

```py
# no decorators
class Dog:
    def __init__(self):
        self._sound = 'woof'

    def get_sound(self):
        return self._sound

    def change_sound(self, new_sound):
        self._sound = new_sound

    def del_sound(self):
        del self._sound


my_dog = Dog()
print(my_dog.get_sound())

my_dog.change_sound('bark')
print(my_dog.get_sound())

my_dog.del_sound()
print(my_dog.get_sound())
```

## `@property.method`

With decorators, we use each method as if it were a property

- Makes our class feel like a "normal" object

To do this, decorate your `getter` with `@property`

Then decorate your `setter` & `deleter`

- `@prop_name.setter`
- `@prop_name.deleter`

```py
# with decorators
class Dog:
    def __init__(self):
        self._sound = 'woof'

    @property
    def sound(self):
        return self._sound

    @sound.setter
    def sound(self, new_sound):
        self._sound = new_sound

    @sound.deleter
    def sound(self):
        del self._sound
        print('no more sound')


my_dog = Dog()
print(my_dog.sound)

my_dog.sound = 'bark'
print(my_dog.sound)

del my_dog.sound
print(my_dog.sound)
```
