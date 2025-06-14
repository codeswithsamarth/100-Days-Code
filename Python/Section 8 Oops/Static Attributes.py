# Static Attributes
"""Static Attributes is also called as class attribute that belong to class itself used to
   They are used for manipulate different structure like instantiating objects  from csv"""

class User:
    user_count = 0
    def __init__(self,user,email):
        self.user = user
        self.email = email
        User.user_count += 1

    def get_display(self):
        print(f"Username:{self.user},Email:{self.email}")


user1 = User("Samarth","samarthp2828@gmail.com")
user2 = User("Sanket","sanketp2727@outlook.com")

print(user1.user_count)