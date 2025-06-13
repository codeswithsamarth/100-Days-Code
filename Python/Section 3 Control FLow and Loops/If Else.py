num = 12
if num % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")

age = int(input("Enter The Age:"))
if age > 0:
    if age > 18:
        print("You can vote")
    else:
        print("You can\'t vote")
else:
    print("Enter The valid age")

side1 = int(input("Enter Sides of triangle:"))
side2 = int(input("Enter Side 2 of Triangle:"))
side3 = int(input("Enter Side 3 of Triangles:"))

if(side1==side2 and  side2 == side3):
    print("Triangle is Equilateral")
elif(side1==side2 or side2 == side3):
    print("Triangle is isosceles")
else:
    print("Triangle is Scalene")

number = int(input("Enter The Number:"))
if number % 2 == 0:
    if number > 0:
        print("Number is Positive Even")
    else:
        print("Number is Negative Even")
else:
    if number > 0:
        print("Number is Positive Odd")
    else:
        print("Number is Negative Odd")