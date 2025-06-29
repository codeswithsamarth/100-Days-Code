import re

email = input("Enter The Email:")

if re.search(r"[\w]+@[\w]+\.edu$",email):
    print("Valid")
else:
    print("Invalid")