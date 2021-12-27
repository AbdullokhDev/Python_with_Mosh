# Class: blueprint for creating new objects
# Object: instance of a class

# Class: Human
# Objects: Abdulloh, Muhammad, Abu Bakr, Umar, Usmon, Ali

# class Point:
#     def draw(self):
#         print("draw")
        
# point = Point()
# print(type(point))
# print(isinstance(point, Point))

# CONSTRUCTOR
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def draw(self):
        print(f"Point ({self.x}, {self.y})")
        
point = Point(1, 2)
point.draw()