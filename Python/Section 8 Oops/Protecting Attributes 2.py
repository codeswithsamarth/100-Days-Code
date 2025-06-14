class user:
    def __init__(self,username,email,password):
        self.username = username
        self._email  = email
        self.password = password


    def change_email(self,password,email):
        if '@' in email:
            if password == self.password:
             self._email = email
        else:
            print("Wrong Password")

user1 = user("sanket","sanket123@gmail.com","123")
user2 = user("samarth","samarth123@gmail.com","431")

user1.change_email("123","sanketp123gmail.com")
print(user1._email)