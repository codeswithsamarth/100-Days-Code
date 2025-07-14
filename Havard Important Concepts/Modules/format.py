import re

email = input("Enter The Email:")

if re.search(r"^[A-za-z_]+@gmail+\.com$",email):
    print("Valid email")
else:
    print("Invalid Email")