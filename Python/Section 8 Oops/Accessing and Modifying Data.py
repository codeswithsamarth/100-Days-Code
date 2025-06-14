class user:
    def __init__(self,username,email,password):
        self.username = username
        self.email  = email
        self.password = password

    def say_hi_to_user(self,user):
        print(f"Sending Message to {user.username}: Hi {user.username} it's {self.username}")

user1 = user("sanket","sanket@123","123")
user2 = user("samarth","samarth@123","431")

user1.say_hi_to_user(user2)

user1.email = "sanketp1234@gmail.com"
print(user1.email)