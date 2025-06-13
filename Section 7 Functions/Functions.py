# def calculator():
#     num1 = int(input("Enter The Number 1:\n"))
#     num2 = int(input("Enter The Number 2:\n"))
#     operator = int(input("Enter The choice 1.Addition 2.Subtraction 3.Multiplication 4.Division\n"))
#     match operator:
#         case 1:
#             print("Addition = ",num1+num2)
#         case 2:
#             print("Subtraction = ",num1-num2)
#         case 3:
#             print("Multiplication = ",num1*num2)
#         case 4:
#             if (num2 == 0):
#                 print("Cant Divide by Zero Math Error!")
#             else:
#                 print("Division = ",num1/num2)
#         case _:
#             print("Enter The Valid Option ")
#
# calculator()

students = {}
def add_student():
    roll = int(input("Enter The Roll No:\n"))
    if roll in students:
        print("Student Already Exists")
    else:
        name = input("Enter The Name:\n")
        students[roll] = name
        print("Student added successfully")

def search_student():
    roll = (input("Enter The Roll No"))
    if roll in students:
        print(f"Student Found in List {students[roll]}")
    else:
        print("Student Not Found in List")

def delete_student():
    roll = (input("Enter The Roll No"))
    if roll in students:
        del students[roll]
        print("Students Deleted")
    else:
        print("Student Not Found")

def show_all():
    if not students:
        print("No Students Available")
    else:
        print("All Students")
        for roll,name in students.items():
            print(f"Roll No = {roll} Student = {name}")

def student_system():
    while True:
        print("Student Management System")
        print("1.Add Student\n2.Search student\n3.Delete Student\n4.Show all Student\n5.Exit")
        choice = (input("Enter Your Choice:"))
        if choice == "1":
            add_student()
        elif choice == "2":
            search_student()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            show_all()
        elif choice == "5":
            print("Thanks For visiting student Management System")
        else:
            print("Enter The valid choice")

student_system()