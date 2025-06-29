try:
    a = int(input("Enter The Number 1:\n"))
    b = int(input("Enter Number 2:\n"))
    c = input("Enter The Operator\n1.Addition\n2.Subtraction\n3.Multiplication\n4.division\n")
    match c:
        case "1":
            print(f"Addition = {a+b}")
        case "2":
            print(f"Subtraction = {a-b}")
        case "3":
            print(f"Multiplication = {a * b}")
        case "4":
            try:
                print(f"Division = {a/b}")
            except ZeroDivisionError:
                print("Can't divide by zero")
        case _:
            print("Invalid choice")
except ValueError as e:
    print("Only integers are allowed")
except TypeError as t:
    print("Cant add string and integers")
except Exception as ee:
    print(ee)