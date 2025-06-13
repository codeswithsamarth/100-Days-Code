# map applies function to each item in iterable

# map(function,iterable)

nums = [3,2,6,7,8,9,11,8]
even = list(filter(lambda x: x % 2 == 0,nums))
print(even)

double = list(map(lambda x: x*2,nums))
print(double)

square = list(map(lambda x: x ** 2,range(5)))
print(square)

l = [2,7,11,22,99,111]
num_str = list(map(lambda x: str(x),l))
print(num_str)

name = ["samarth","sanket","harshit"]
capital = list(map(lambda x: x.upper(),name))
print(capital)

l1 = [1,2,3,4]
l2 = [4,5,6,7]
add = list(map(lambda x,y: x+y,l1,l2))
print(add)

# filter :- no change to items

nums = [1,-1,-11,-99,99.88,-00,-991]
positive = list(map(lambda x: x if x >0 else None,nums))
print(positive)

# name = []
# i = 0
# while (i < 5):
#     names = (input("Enter The Name:\n"))
#     name.append(names)
#     i+=1
#
# start_a = list(filter(lambda x:x if x.startswith("A") else None,name))
# print(start_a)

a = [2,3,4,6,6,9,8,12,10,15]
divisible_by_2 = list(filter(lambda x: x if x % 2 == 0 else None,a))
print(divisible_by_2)

imp = [1,2.0,3.0,3,4.8,9,00,9.0]
floats = list(filter(lambda x: x if isinstance(x,float) else None,imp))
print(floats)

strs = ["Samarth","Patil","Sanket"]
str_ex = list(map(lambda x: x+"!",strs))
print(*str_ex)

a = [2,4,6]
b = [4,6,7]
greater = list(map(lambda x,y: x if x >y else y,a,b))
print(greater)