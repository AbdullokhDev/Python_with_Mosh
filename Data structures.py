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

# ADD and REMOVE
letters = ['a','b','c','d']
# append funct is adding new object at the end of list while
# insert you should specify number of index
letters.append('e')
letters.insert(0, '-')

# pop func is remove by index while
# remove function is removes only by itself
# delete func is removes range of objects while
# clear func is removes all of them
letters.pop(0)
letters.remove("b")
del letters[0:3]
letters.clear()
print(letters)
