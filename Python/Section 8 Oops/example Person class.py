class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello My Name is {self.name} and My Age is {self.age}")

person1 = Person("Samarth",17)
person2 = Person("Sanket",16)

person1.greet()
person2.greet()