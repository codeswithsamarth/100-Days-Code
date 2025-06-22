# try:
#     user_input = input("Enter The Number")
#     number = int(user_input)
#     if number < 1 or number > 100:
#         print("Number is out of range")
#     else:
#         print(f"Number is valid {number}")
# except ValueError:
#     print("Letter are Not allowed Only number")
#
# try:
#     num1 = int(input("Enter The Number 1:\n"))
#     num2 = int(input("Enter The Nuber 2:\n"))
#     result = num1 / num2
#     print(f"Result = {result}")
# except ZeroDivisionError:
#     print('Denominator can\'t be zero')
# except ValueError:
#     print("Only Numbers are allowed")
from math import expm1
from unittest import expectedFailure

# fruits = ["apple",'banana','orange']
# try:
#     index = int(input("Enter The index"))
#     print(f"You selected index = {fruits[index]}")
# except IndexError:
#     print("Index out of range or invalid")
# except ValueError:
#     print("Value must be integer")
#
# person = {"Samarth":20,"Sanket":12}
# try:
#     key = input("Enter The key")
#     print(f"Value is {person[key]}")
# except KeyError:
#     print("Key are Invalid")
#
#
# try:
#     num1 = int(input("Enter the number 1"))
#     num2 = int(input("Enter the number 2"))
#     print(f"Adding result = {num1+num2}")
# except TypeError:
#     print("Cant add integer with string")
# except ValueError:
#     print("Only integers are allowed")

# try:
#     name = input("Enter Your name")
#     name.append("Samarth")
# except AttributeError:
#     print("You cant use append method in string")
#
# try:
#     temp = float(input("Enter the temperature"))
#     if temp < -100 or temp > 100:
#         raise Exception("Temperature is out of range")
#     else:
#         print(f"Temperature = {temp}")
#
# except Exception as e:
#     print('error = ',e)

i = 1
while(i < 5):
    try:
         a = int(input("Enter The Number 1"))
         b = int(input("Enter The Number 2"))
         print(f"sum = {a+b}")
         i+=1
    except Exception as e:
        print("Some Error occur =  ",e)
    finally:
        print("This is always executed")