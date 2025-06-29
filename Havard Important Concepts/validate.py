import re

email = input("Enter Your Email:").strip()
# if '@' in email:
#     print("Valid")
# else:
#     print("Invalid")

# if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$",email):
#     print("Valid")
# else:
#     print("Invalid")

if re.search(r"[\w]+@[\w]+\.edu",email):
    print("Valid")
else:
    print("Invalid")