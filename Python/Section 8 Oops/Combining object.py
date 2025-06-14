class dog:
    def __init__(self,name,breed,owner):
        self.name = name
        self.breed =  breed
        self.owner = owner
    def bark(self):
        print("Whoof Whoof ")


class owner:
    def __init__(self,name,address,contact_no):
        self.name = name
        self.address = address
        self.mobile_number = contact_no

owner1 = owner("Samarth","Solapur","9839932472")
dog1 = dog("REO","Pomeranian",owner1)

owner2 = owner("Sanket","Solapur","93489243434")
dog2 = dog("Princy","Pomeranian",owner2)

print(f"{dog1.owner.name}")
print(f"{dog2.owner.name}")