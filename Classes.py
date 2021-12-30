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

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
        
#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y

# point = Point(1, 2)
# other = Point(1, 2)
# print(point == other)

# class TagCloud:
#     def __init___(self):
#         self.tag = {}
    
#     def add(self, tag):
#         self.tags[tag] = self.tags.get(tag, 0) + 1
        
#     def __getitem___(self, tag):
#         return self.tags.get(tag.lower(), 0)
    
#     def __setitem___(self, tag, count):
#         self.tags[tag.lower()] = count
        
#     def __len__(self):
#         return len(self.tags)
    
#     def __iter__(self):
#         return iter(self.tags)

# cloud = TagCloud()
# cloud["python"] = 10
# len(cloud)
# cloud.add("python")
# cloud.add("python")
# cloud.add("python")
# print(cloud.tags)

# class Product:
#     def __init__(self, price):
#         self.set_price(price)
        
#     def get_price(self):
#         return self.__price
    
#     def set_price(self, value):
#         if value < 0:
#             raise ValueError("Price cannot be negative")
#         self.__price = value

# product = Product(-50)



# # INHERITANCE
# class Animal:
#     def __init__(self):
#         print("Animal constructor")
#         self.age = 1
    
#     def eat(self):
#         print("eat")

# # this is method overriding from base class which is animal
# class  Mammal(Animal):
#     def __init__(self):
#         super().__init__()
#         print("Mammal constructor")
#         self.weight = 2
        
#     def walk(self):
#         print("walk")
         
# class  Fish(Animal):
#     def swim(self):
#         print("swim")       

# m = Mammal()
# f = Fish()
# m.eat()
# print(f.age)
# print(m.age)
# print(m.weight)

# class Flyer:
#     def fly(self):
#         pass
    
# class Swimmer:
#     def swim(self):
#         pass
    
# class FlyingFish(Flyer, Swimmer):
#     pass

# ABSTRACT BASE CLASSES
# from abc import ABC, abstractmethod

# class InvalidOperationError(Exception):
#     pass

# class Stream(ABC):
#     def __init__(self):
#         self.opened = False
        
#     def open(self):
#         if self.opened:
#             raise InvalidOperationError("Stream is already opened")
#         self.opened = True
        
#     def close(self):
#         if not self.opened:
#             raise InvalidOperationError("Stream is already closed")
#         self.opened = False
    
#     @abstractmethod
#     def read(self):
#         pass

# class FileStream(Stream):
#     def read(self):
#         print("Reading data from a file")

# class NetworkStream(Stream):
#     def read(self):
#         print("Reading data from a network")

# class MemoryStream(Stream):
#     def read(self):
#         print("Reading data from a memory stream.")

# stream = MemoryStream(
# stream.open()

# from abc import ABC, abstractmethod

# # class UIControl(ABC):
# #     @abstractmethod
# #     def draw(self):
# #         pass
    
# class TextBox:
#     def draw(self):
#         print("Text box")
    
# class DropDownList:
#     def draw(self):
#         print("Drop down list")

# def draw(controls):
#     for control in controls:
#         control.draw()

# ddl = DropDownList()
# tb = TextBox()
# #print(isinstance(ddl, UIControl))
# #draw(ddl)
# #draw(tb)
# draw([ddl, tb])

# class Text(str):
#     def duplicate(self):
#         return self + self
    
# #text = Text("Python")
# #print(text.lower())


# class TrackableList(list):
#     def append(self, object):
#         print("Append called")
#         super().append(object)

# list = TrackableList()
# list.append("1")

from collections import namedtuple
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
        
#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y
  
Point = namedtuple("Point", ["x", "y"])
p1 = Point(1, 2)
p2 = Point(1, 2)
print(p1 == p2)




































