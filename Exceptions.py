# try:
#     age = int(input("Age: "))
# except ValueError as ex:
#     print("You did not enter a valid age.")
#     print(ex)
#     print(type(ex))
# else:
#     print("No exceptions were thrown")
# print("Execution continues.")

# try:
#     file = open("Exeptions.py")
#     age = int(input("Age: "))
#     xfactor = 10 / age
# except ValueError:
#     print("You did not enter a valid age.")
# except ZeroDivisionError:
#     print("Age cannot be 0.")
# else:
#     print("No exceptions were thrown.")
# finally: 
#     file.close()

# try:
#     with open("Exeptions.py") as file:
#         print("File opened.")
#     age = int(input("Age: "))
#     xfactor = 10 / age
# except ValueError:
#     print("You did not enter a valid age.")
# except ZeroDivisionError:
#     print("Age cannot be 0.")
# else:
#     print("No exceptions were thrown.")
# # finlly clouse is not needed because of with

# def calculate_xfactor(age):
#     if age <= 0:
#         raise ValueError("Age cannot be 0 or less.")
#     return 10 / age

# try:
#     calculate_xfactor(-1)
# except ValueError as error:
#     print(error)

# SAME AS BEFORE LINE FROM 37 to 45

from timeit import timeit

code1 ="""
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age

try:
    calculate_xfactor(-1)
except ValueError as error:
    # print(error)
    pass
"""

code2 ="""
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10 / age

xfactor = calculate_xfactor(-1)
if xfactor == None:
    pass
"""
print("first code=", timeit(code1, number=10000))
print("second code=", timeit(code2, number=10000))