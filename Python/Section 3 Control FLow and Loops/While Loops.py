
i = 1
while(i<=5):
    print(i)
    i+=1


i = 2
while(i<=20):
    print(i)
    i+=2

sum = 0
i = 1
while(i<10):
    sum += i
    i+=1

print("sum = ",sum)

i = 10
while(i >= 1):
    print(i)
    i-=1;

name = "Samarth"
i = 0
while(i<len(name)):
    print(name[i])
    i+=1

num = 4
factorial = 1
while(num>1):
    factorial*=num
    num-=1
    print(factorial)

# sum = 0
# n = int(input("Enter The Number"))
# while(n!=0):
#     sum+=n%10
#     n//=10
#
# print("Sum = ",sum)

# sum = 0
# num = int(input("Enter The Number"))
# palindrome = num
#
# while(num!=0):
#     sum+=num%10
#     sum*=10
#     num//=10
#
# sum//=10
# if (sum == palindrome):
#     print("The Number is Palindrome")
# else:
#     print("The Number is Not palindrome")
#
# is_prime = 0
# n = int(input("Enter The Number"))
# i = 2
# while(i<=n//2):
#     if (n % i == 0):
#         is_prime = 0
#         break
#     i+=1
#     print(is_prime)

# t1 = 0
# t2 = 1
# t3 = t1+t2
#
# terms = int(input("Enter The Terms"))
# i = 0
# while(i<terms):
#     print(t1)
#     t1 = t2
#     t2 = t3
#     t3 = t1+t2
#     i+=1

# num = int(input("Enter The Number"))
# i = 1
# while (i<=10):
#     print(f"{num} X {i} = {num*i}")
#     i+=1
#
s = "Samarth"
vowels = 'aeiou'
i = 0
count = 0
while i < len(s):
    if s[i] in vowels:
        count += 1
    i+=1
print("Vowels = ",count)

# 153 1**3+5**3+3**3
n = int(input("Enter The Number"))
total = 0
temp = n
power = len(str(n))
while temp>0:
    digit = temp % 10
    total += digit ** power
    temp//=10

if (total == n):
    print("Number is Armstrong Number")
else:
    print("Number is Not Armstrong Number")



