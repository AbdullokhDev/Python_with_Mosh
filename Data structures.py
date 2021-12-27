# letters = ["a","b","c"]
# matrix = [[0,1],[2,3]]
# zeros = [0] * 5
# combined = letters + zeros
# numbers = list(range(20))
# char = list("Hello world")
# print(char)

# letters = ['a','b','c','d','e']
# letters[0] = 'A'
# print(letters)
# print(letters[0:3])
# print(letters[::2])

# LIST UNPACKING
# numbers = [1,2,3]
# first, second, third = numbers
# print(first)
# print(third)

# numbers = [1,2,3,4,5,6,7,8]
# first, second, *other = numbers
# print(first)
# print(other)

# it shows with its index
# letters = ['a','b','c','d']
# for letter in enumerate(letters):
#     print(letter)

# # ADD and REMOVE
# letters = ['a','b','c','d']
# # append funct is adding new object at the end of list while
# # insert you should specify number of index
# letters.append('e')
# letters.insert(0, '-')

# # pop func is remove by index while
# # remove function is removes only by itself
# # delete func is removes range of objects while
# # clear func is removes all of them
# letters.pop(0)
# letters.remove("b")
# del letters[0:3]
# letters.clear()
# print(letters)

# LAMBDA FUNCTION
# items = [
#     ('Product1', 10),
#     ('Prroduct2', 9),
#     ('Product3', 12)
#    ]

# items.sort(key=lambda item: item[1])
# print(items)

# items = [
#     ('Product1', 10),
#     ('Prroduct2', 9),
#     ('Product3', 12)
#     ]
# prices = []
# for item in items:
#     prices.append(item[1])
    
# print(prices)

# items = [
#     ("Product1", 10),
#     ("Prroduct2", 9),
#     ("Product3", 12),
#     ]
# prices = list(map(lambda item: item[1], items))
# print(prices)

# items = [
#     ("Product1", 10),
#     ("Product2", 8),
#     ("Prodcut3", 12),
#     ("Product4", 15),
#     ]

# # prices = list(map(lambda item: item[1], items))
# # list comprhensions is similar to map lambda and preffered using it
# prices = [item[1] for item in items]
# print(prices)

# deque importing
# from collections import deque
# queue = deque([])
# queue.append(1)
# queue.append(2)
# queue.append(3)
# queue.popleft()
# print(queue)
# if not queue:
#     print("empty")

# x = 10
# y = 11

# z = x
# x = y
# y = z

# print("x", x)
# print("y", y)

# x = 11
# y = 22

# x, y = y, x
# print("x", x)
# print("y", y)

# numbers = [1, 2, 3, 3, 4, 5, 6, 6, 6, 6, 7, 8, 9, 9]
# uniques = set(numbers)
# print(uniques)

# numbers = [1, 1, 2, 3, 4]
# first = set(numbers)
# second = {1, 5}

# print(first | second)
# print(first & second)
# print(first - second)
# print(first ^ second)

# point = {"x": 1, "y": 2}
# point = dict(x=1, y=2)
# print(point)

# values = []
# for x in range(5):
#     values.append(x * 2)
    
# values = {x * 2 for x in range(5)}
# print(values)

from sys import getsizeof

# values = (x * 2 for x in range(100000))
# print("gen:", getsizeof(values))

# values = [x * 2 for x in range(100000)]
# print("list:", getsizeof(values))

# unpacking operator *

# numbers = [1, 2, 3]
# print(numbers)
# print(*numbers)
# print(1, 2, 3)

# values = list(range(5))
# values = [*range(5), *"Hello"]
# print(values)

# first = {"x": 1}
# second = {"x": 10, "y": 2}
# combinedDic = {**first, **second, "z": 111}
# print(combinedDic)


from pprint import pprint
sentence = "This is a common interview question"

char_frequency = {}
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1
# pprint(char_frequency, width=1)

char_frequency_sorted = (sorted(
    char_frequency.items(), 
    key=lambda kv: kv[1], 
    reverse=True))
print(char_frequency_sorted[0])