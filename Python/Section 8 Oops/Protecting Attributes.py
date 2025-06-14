class user:
    def __init__(self,username,email,password):
        self.username = username
        self.__email  = email
        self.password = password

    def access_emai(self):
        password = input("Enter Your Password")
        if password == self.password:
            return self.__email.lower()
        else:
            print("Wrong Password")

user1 = user("sanket","sanket123@gmail.com","123")
user2 = user("samarth","samarth123@gmail.com","431")

print(user2.access_emai())

# Types :- Protected _  Private :- __