# def greet():
#     print("Hello world")
#     print("Welcome to programming world")
    
    
# greet()

# parameters inside brackets
# def greet2(first_name, last_name):
#     print(f"Hello {first_name} {last_name}")
#     print("Welcome")
    
# # arguments
# greet2("Mosh", "Hamedani")
# greet2("John", "Smith")

# two types of function 1-Perform a task 2-Return a value

# def get_greeting(name):
#     return f"Hi {name}"


# message = get_greeting("Abdullokh")
# print(message)

# def increment(number, by):
#     return number + by

# result = increment(2, 5)
# print(result)

# # or we can use like that
# print(increment(number=3, by=4))


# def auto_increment(number, by = 1):
#     return number + by


# print(auto_increment(4))
    

# def multiply(*numbers):
#     print(numbers)
    
# multiply(3,5,6,7)
    
    
# def calculate(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#     return total

# print(calculate(3,4,5,6))
    
    
# def save_user(**user):
#     print(user)

# save_user(id=1, name="Abdullokh", age=22)
    

# def save_user_with_one_argument(**user):
#     print(user["name"])
    
# save_user_with_one_argument(id=1, name="Mosh", age=44)
    
# debugging
# def calculate(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#     return total

# print("start")
# print(calculate(3,4,5,6))

# 1 aprroach
# def fizz_buzz(input):
#     if input % 3 == 0:
#         result = "Fizz"
#     else:
#         result = "Buzz"
#     return result
# print(fizz_buzz(3))

# 2 approach
def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    return input
print(fizz_buzz(7))
    
    
    
    
    
    
    
    
    