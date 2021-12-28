# Class: blueprint for creating new objects
# Object: instance of a class

# Class: Human
# Objects: Abdulloh, Muhammad, Abu Bakr, Umar, Usmon, Ali

# Class: Car
# Instance: 2017 Honda Civic
# Attributes: weight, color would be an attribute of that instance of that class

# class Point:
#     def draw(self):
#         print("draw")
        
# point = Point()
# print(type(point))
# print(isinstance(point, Point))

# CONSTRUCTOR
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
        
#     def __str__(self):
#         return f"({self.x}, {self.y})"
    
#     def draw(self):
#         print(f"Point ({self.x}, {self.y})")
        
# point = Point(1, 2)
# print(str(point))
# point.draw()

# another = Point(3, 4)
# another.draw()

# All Humans have two eyes, two ears, so these are attributes we'll define
# at the class level, and they are shared among all intances

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __gt__(self, other):
        return self.x == other.x and self.y == other.y

point = Point(1, 2)
other = Point(1, 2)
print(point > other)








































