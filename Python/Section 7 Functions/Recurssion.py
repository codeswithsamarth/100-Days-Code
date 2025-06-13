# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n * factorial(n-1)
#
# num = int(input("Enter The Number"))
#
# if num < 0:
#     print("Cant Find Factorial for Negative")
# else:
#     print("Factorial = ",factorial(num))

# def fibonacci(n):
#     if n == 0 or n == 1:
#         return n
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
#
# term = int(input("Enter The Term"))
#
# print("Fibonacci Series\n")
# i = 0
# while(i<term):
#     print(fibonacci(i))
#     i+=1
#
def power(base,expo):
    if expo == 0:
        return 1
    else:
        return base * power(base,expo-1)

num1 = int(input("Enter The Base"))
num2 = int(input("Enter The Power"))

print("Answer = ",power(num1,num2))