a = -6
print(abs(a))

values = [True,False,True,False,False]
print(any(values))
print(all(values))

number = 10
print(bin(number))

value = -0
print(bool(value))

# ascii to letter = byte if single bytearray if arrayy

byte = bytes(65)
print((byte))

def my_fun():
    pass
print(callable(my_fun()))

num = 97
print(chr(num))

# compile functions compile source code

code = compile("x = 10*10","sam.py","exec")
exec(code)
print(x)

number = complex(2,3)
print(number)

# dir prints the list of attribute of an object
print(dir([]))

number,number2 = divmod(2,7)
print(number,number2)

# enumerate is used to return index and value
my_list = ["Samarth","Sanket","Hashit"]
for i,name in enumerate(my_list):
    print(i)

x = 5
result = eval('x+2')
print(result)

print(hash('hello'))

help(str)

print(hex(233))

print(id('hello'))

print(isinstance(5,int))

print(len('hello'))

print(max([1,2,3]))