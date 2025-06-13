name = "Harry"
print(name.startswith("Har"))
print(name.endswith("rry"))

name = "Samarth"
age = 23
print(f"My name is {name} and My Age is {age}")
introduction = "My Name is {} and My Age is {}".format(name,age)

person = {"name1":"Samarth","Age1":28}
for_intro = "My Name is {name1} and My Age is {Age1}".format_map(person)
print(for_intro)

name = "Harshit"
print(name.upper())
print(name.lower())
print(name.capitalize()) # Capital only First Letter of String
print("this is the python title examole".title())

namee = "ABC"
print(namee.isalpha())
print(namee.isalnum())

strings = "  Hello World  "
print(strings.lstrip())
print(strings.rstrip())

string1 = 'Sam Warld'
print(string1.find('S'))
print(string1.rfind('a'))

# name = input("Enter Your Name:")
# name1,name2  = name.split(" ")
# print(name1[0]+name2[0])

# Partition is function Which seperate
s = "Samarth\nApparao\nPatil"
print(s.splitlines())

s5 = "Hello"
print(s5.center(10,"\t"))

s15 = "150"
print(s15.zfill(12))

s5 = "Hello"
print(s5.center(10,"\n"))

sd = "HElLO"
print(sd.casefold())

qw = "Hello World"
print(qw.removeprefix("Hello "))

# Remove Suffix
qwe = "Srujan Sanket"
print(qwe.removesuffix("Sanket"))
