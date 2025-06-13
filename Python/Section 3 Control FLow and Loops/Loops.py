
for i in range(1,11):
    print(i)

for i in range(1,21):
    if (i % 2 == 0):
        print(i)

for i in range(1,11):
    square = i ** 2
    print(square)

add = 0

for i in range(1,101):
    add+=i
    if(i == 100):
        print("Total is equal to ",add)

for i in range(1,11):
    print(f"5 * {i} = {5 * i}")

list1 = [2,4,6,8,10]
reversed_list = []

for i in range(len(list1)-1,-1,-1):
    reversed_list.append(list1[i])


print(f"original list = {list1}")
print(f"reversed list = {reversed_list}")

# word = input("Enter The Word:\n")
# count = 0
# vowels = ['a','e','i','o','u']

# for i in word:
#     if i.lower() in vowels:
#         count += 1
#
# print("count = ",count
#       )

list1 = [11,22,33,44,55]
for i,j in enumerate(list1):
    print(f"index = {i},element = {j}")

# number = int(input("Enter The Number"))
# factorial = 1
#
# if number < 0:
#     print("Factorial is not defined for Negative Numbers")
#
# elif number == 0:
#     print("Factorial is equal to 1")
#
# else:
#     for i in range(1,number+1):
#         factorial *= i
#         print(f"factorial = {factorial}")

is_prime = 1

# num = int(input("Enter The Number"))
# for i in range (2,int(num**0.5)+1):
#     if num % i == 0:
#         is_prime = 0
#         break
#
# if is_prime:
#     print("prime number")
# else:
#     print("Not a prime Number")


list1 = [1,10,2,11,22,44,3,2]
list2 = []

for  i  in list1:
    if i > 10:
        print(i)

number = 2345
sum = 0
for i in range(number):
    sum += number % 10
    number//= 10

print("sum of digits of number",sum

      )

# celsius = float(input("Enter The Temperature in Celsius"))
# fahrenheit = (celsius * 1.8)+32
#
# print("Fahrenheit = ",fahrenheit)


# count = 0
# word = input("Enter The String:\n")
# for i in word:
#     if i.isspace():
#         count+= 1
#
# print(count)

# t1 = 0
# t2 = 1
# t3 = t1+t2
#
# terms = int(input("Enter The Terms"))
#
# for i in range(terms):
#     print(t1)
#     t1 =  t2
#     t2 = t3
#     t3 = t1+t2

l1 = [1,2,3,4]
l2 = [3,4,5,6]

l1.extend(l2)


common = set(l1)
print(list(common))

count = 0
common1 = [11,22,33,44,55,66]
common2 = [11,22,33,44,55]
common = list(set(common1)&set(common2))
common.sort()
print("Common elements",common)

# rev = 0
# number = int(input("Enter The Number"))
# palindrome = number
# for i in range(len(str(number))):
#     if number!=0:
#         rev += number % 10
#         rev *= 10
#         number//=10
#
# rev//=10
# if (palindrome == rev):
#     print("The number is palindrome")
# else:
#     print("The Number is Not palindrome")
count  = 0
sentence = input("Enter The Sentence")
word_count = input("Enter The word to count")
for i in sentence:
    count = sentence.count(word_count)
    print(count)
    break