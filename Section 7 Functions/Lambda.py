# lambda is a anonymous function which has no name

square = lambda x: x **2
print(square(2))

avg = lambda a,b,c:(a+b+c)/3
print((avg(30,27,28)))

even = lambda n: "Even" if n%2 == 0 else "odd"
print(even(4))

leap = lambda year: "Leap Year" if year % 4 == 0 and year % 100!=0 or year % 400 == 0 else "Not a Leap Year"
print(leap(2024))

palindrome = lambda x: "Palindrome" if  x == x[::-1] else "Not A Palindrome"
print(palindrome("CIVIC"))

