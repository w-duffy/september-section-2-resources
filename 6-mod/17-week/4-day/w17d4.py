# ## Classes
from pydantic import BaseModel

class Animal(BaseModel):
    sound: str
    name: str


class WorldlyEntity:
    def __init__(self, name, sound):
        self.sound = sound
        self.name = name

#     def animal_method(self):
#         print(self)
#         return "not none"

# class User(db.Model):
#     username = db.Column(db.String())


class Animal:
    def __init__(self, name, sound, password):
        self.sound = sound
        self.name = name
        self._hashedPassword = password

    def animal_method(self):
        print(self)

    @property
    def password(self):
        is_user = True # logic to see if it's a user
        if is_user is False:
            return "too bad you can't GET it 🙂"
        else:
            return self._hashedPassword


    @password.setter
    def password(self, password):
        print("Running setter hash algorithms")
        self._hashedPassword = password


woofer = Animal("woofer", "woof", "goodpass")

print("before: ", woofer.password)
woofer.password = "new pass"
print("after: ", woofer.password)




# woofer.password = "new pass"


# print(woofer.password)








# woofer.name = "NOT WOOFER"
# woofer.animal_name = "NOT WOOFER"
# print("\n", woofer.animal_name)

# def hello_world():
#     print("Hello world!")

# def goodbye():
#     print("goodbye")

def wrapper_func(login_a_user):
    def validate_user():
        print("did I run?")
        ## validation logic
        try:
            pass # validation logic
            login_a_user()
        except: # ValidationError(e)
            return "you're a hacker"
        finally:
            pass # @redirect home

        print("did I also run?")
    return validate_user

@wrapper_func
def log_in():
    print("hey I'm an easy func")

@wrapper_func
def some_other():
    print("all the time?")

# easy_func()

# some_variable = wrapper_func(hello_world)
# another_variable = wrapper_func(goodbye)

# some_variable()

# another_variable()



# fido = Dog("fido")
# print(fido.name, fido.sound, fido.hello)


# # class AnimalMixin:
# #     # utitlity methods
# #     pass

# # ## Inheritance
# # class Dog(Animal, AnimalMixin):
# #     pass

# # class Cat(Animal, AnimalMixin):
# #     pass


# # """
# # multi
# # line
# # """


# # ## Getters and Setters
# # class User:
# #     """
# #     This is for creating a user class
# #     Attributes:
# #         name (str): name of the user
# #         age (int): age of the user
# #         password (str): password of the user
# #     """
# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age
# #         self._password = "12345"

# #     @property
# #     def password(self):
# #         return self._password

# #     @password.setter
# #     def password(self, new_password):
# #         # Some hashing logic here
# #         self._password = new_password

# #     def greet(self):
# #         """Method that prints hello and the user's name"""
# #         return f"Hello {self.name}!"

# #     def __repr__(self):
# #         print("did i run?")
# #         return f"DEFINED HERE: User(name={self.name}, age={self.age}, password={self.password})"

# # demo = User("Demo", 50)
# # # print(demo)
# # demo.greet()

# # help(User)

# # print(demo.password)

# ################################################################################
# ## Build a class to prevent Will from having to always add line breaks on prints


# print("hi", "hello", "world", sep="\n\n------\n\n", end="\n\n")

class WillPrint:
    """This is wills custom printer"""
    def __init__(self, sep, end):
        self.sep = sep
        self.end = end

    def custom_print(self, *printable):
        print(*printable, sep=self.sep, end=self.end)

    # def __call__(self, *printable):
    #     print(*printable, sep=self.sep, end=self.end)


# wprint = WillPrint("\n\n~~~~~~\n\n", "\n\n").custom_print

# some_var = "hi"
# nums = [1,2,3]
# spot = {"id": 1, "name": "disney world"}

# wprint(f"some_var: {some_var}", f"nums: {nums}", f"spot details: {spot}")


# # wprint = WillPrint("\n\n~~~~~~\n\n", "\n\n")
# # zprint = WillPrint("\n\n----I love this utility----\n\n", "\n\n")
# # zprint.custom_print("hi", "hello", "world")
# # print(vars(wprint))

# # wprint.custom_print("hi", "hello", "world")
