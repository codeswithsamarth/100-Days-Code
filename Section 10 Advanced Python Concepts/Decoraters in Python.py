# decorator extend behaviour of function
# This takes func itt creates new function inside its body return the extended function

import time

def time_calculator(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"Time Taken to execute is {end-start:.4f} seconds")

    return wrapper

def decorator(func):
    def wrapper():
        print("I am Going to Execute The Function")
        func()
        print("I have executed this Function")
    return wrapper

@decorator
def say_hello():
    print("Hello!")

say_hello()

def authentication(func):
    def wrapper():
        print("Authenticating!")
        saved_username = "Samarthp2727"
        saved_password = "Samarthp2727"
        username = input("Enter The Name:\n")
        password = input("Enter The Password:\n")

        if username == saved_username and  password == saved_password:

            func(username)
            print("Authentication completed")
        else:
            print("User Not Found!")
    return wrapper

@time_calculator
@authentication
def user(username):
    print(f"Hello Welcome {username}!")

user()