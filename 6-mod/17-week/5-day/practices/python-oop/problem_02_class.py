# CLASS DECLARATION
#
# Declare a class named "FreeShoes" with the following features:
#
# * A constructor that takes two values, a name and a total number of shoes.
# * A method named "give_away" that reduces the number of available shoes
#   by one. Calling this method over and over should never result in a negative
#   number of available shoes.
# * A "__repr__" method that has the format
#     "<{name} ({available shoes})>"
#
# Test data at the bottom.

#!!START
class FreeShoes:
    def __init__(self, name, shoes):
        self.name = name
        self.shoes = shoes

    def give_away(self):
        self.shoes -= 1
        if self.shoes < 0:
            self.shoes = 0

    def __repr__(self):
        return f"<{self.name} ({self.shoes})>"
#!!END


# Test calls
shoes = FreeShoes("Academy shoes", 3)
print(shoes)  # > "<Academy shoes (3)>"

shoes.give_away()
print(shoes)  # > "<Academy shoes (2)>"

shoes.give_away()
shoes.give_away()
print(shoes)  # > "<Academy shoes (0)>"

shoes.give_away()
print(shoes)  # > "<Academy shoes (0)>" Cannot have # of copies < 0
