class user:
    def __init__(self,username,email,password):
        self.username = username
        self.__email  = email
        self.password = password

    @property
    def email(self):
        return self.__email


    @email.setter
    def email(self,email):
        if '@' in email:
            password = input("Enter The Password:\n")
            if password == self.password:
             self.__email = email
            else:
                print("Wrong Password")
        else:
            print("Invalid Email Format It should contain @ symbol")

user1 = user("sanket","sanket123@gmail.com","123")
user2 = user("samarth","samarth123@gmail.com","431")

user1.email = "sanketpatil123gmail.com"
print(user1.email)