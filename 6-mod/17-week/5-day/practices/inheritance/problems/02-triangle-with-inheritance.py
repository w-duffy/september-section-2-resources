# Build off your RegularPolygon class and create another class called Triangle.
# The Triangle class should have functionality that calculates both the
# perimeter and the area of the triangle. The calculated values for both the
# perimeter and area should be assigned to respective instance properties on the
# Triangle class.

# The area of a triangle can be calculated with Heron's formula:
# √(s(s-a)(s-b)(s-c)), where s is the semi-perimeter of the triangle. The
# semi-perimeter is the perimeter divided by 2. The square root function sqrt()
# can be imported from the built-in math package.

# Write your class here.

#!!START SILENT
# import sqrt function
from math import sqrt

# class we implemented in the previous problem
class RegularPolygon:
    type = "Polygon"
    
    def __init__(self, num_sides, length):
        if num_sides < 3:
            raise Exception("A polygon must have at least 3 sides.")
        
        self.num_sides = num_sides
        self.length = length

    def identify_polygon(self):
        identifier_dict = {
            3: "Triangle",
            4: "Quadrilateral",
            5: "Pentagon",
            6: "Hexagon",
            7: "Heptagon",
            8: "Octagon",
            9: "Nonagon",
            10: "Decagon"
        }

        try:
            self.type = identifier_dict[self.num_sides]
        except KeyError:
            self.type = f"Polygon with {self.num_sides} sides"

    @classmethod
    def polygon_factory(cls, values):
        return [cls(num_sides, length) for num_sides, length in values]

    @staticmethod
    def get_perimeter(polygon):
        return polygon.num_sides * polygon.length

# triangle class
class Triangle(RegularPolygon):
    def __init__(self, num_sides, length):
        if num_sides != 3:
            raise Exception("A triangle must have exactly three sides")
            
        super().__init__(num_sides, length)
        self.perimeter = super().get_perimeter(self)
        self.area = self.get_area()

    def get_area(self):
        # calculate semi-perimeter
        s = self.perimeter/2

        # calculate area with Heron's formula
        return sqrt(s * (s - self.length) * (s - self.length) * (s - self.length))
#!!END

triangle_a = Triangle(3, 3)
print(triangle_a.perimeter) # 9
print(triangle_a.area) # 3.8971...

triangle_b = Triangle(3, 12)
print(triangle_b.perimeter) # 36
print(triangle_b.area) # 62.3538...

triangle_c = Triangle(4, 12)
print(triangle_c.perimeter) # Exception: A triangle must have exactly three sides