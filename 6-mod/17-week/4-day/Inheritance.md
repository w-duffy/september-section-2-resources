# Inheritance

Conceptually, class inheritance works the same way in Python as it did in JavaScript

- Parent/Child relationships
- Passing down methods
- Using `super` to access the parent

The difference lies in the syntax

In JS, to make a child from a parent, we use the `extends` keyword when creating the class.

The child class then calls super in its constructor, passing in any variables found in the parent constructor

```js
// js
class Animal {
  constructor(name, sound) {
    this.name = name;
    this.sound = sound;
  }

  speak() {
    return `${this.name} says ${this.sound}`;
  }
}

class Dog extends Animal {
  constructor(name) {
    super(name, 'woof'); //default sound
  }
}

const myDog = new Dog('callie');
console.log(myDog.speak());
```

In Python, there's no keyword to create a Parent/Child relationship. Instead, we simply pass the parent like an argument to the child class

```py
class Animal:
    pass


class Dog(Animal):
    pass
```

Python still uses super, but it works a little differently.

`super()` is a function that can access the methods of the parent class being passed to the child.

All of the methods available on the parent, including the "constructor" `__init__` method, can be called through `super()`

```py
super().method_name()
```

Since creating a child class requires using the parent's constructor arguments, child classes nearly always follow this format

```py
# py
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, 'woof')
```

But don't be fooled into thinking this is special syntax specific to `__init__()`!

Think of `super()` as nothing more than an object of the parent class. Anything on that parent object can be used through `super()`

However, you don't **_need_** to use super to call a parent method on a child instance. You only need it if you're calling a parent method **in the child class definition**

```py
class Parent:
    def test(self):
        print('I am a parent class')

    def big_method(self):
        print("This method originated from the parent")

    def medium_method(self):
        print('Did you get me to print?')


class Child(Parent):
    def test(self):
        print('I am a child class')
        super().test()

    def small_method(self):
        super().big_method()


child = Child()
child.test()
child.small_method()
child.medium_method()
```
