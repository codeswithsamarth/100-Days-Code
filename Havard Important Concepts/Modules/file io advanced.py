import csv
# names = []
# for _ in range(3):
#     name = input("Enter The Name")
#     names.append(name)
#
# for name in sorted(names):
#     print(f"Hello {name}")

# with open('name.txt','r') as file:
#     for line in file:
#         print("Hello",line.rstrip())

# for content in contents:
#     print(content.rstrip())

# names = []
# with open("names.txt") as file:
#     for line in file:
#         names.append(line.rstrip())
#
# for name in sorted(names):
#     print(f"Hello,{name}")

students = []
with open('names.csv') as file:
    reader = csv.reader(file)
    for row,header in reader:
        students.append({"name":row,"city":header})
for student in sorted(students,key=lambda student:student):
    print(f"{student['name']} is in {student['city']}")

