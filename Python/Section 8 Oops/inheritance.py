#inheritance is a fundamental concept in c programming which involves creating classes subclasses or derived classess
# based on existence classes superclass or base class

class Vehicle:
    all = []
    def __init__(self,brand,model,year,fuel):
        self.brand = brand
        self.model = model
        self.year = year
        self.fuel = fuel
        Vehicle.all.append(self)

    def print_object(self):
        for keys,value in self.__dict__.items():
            print(keys,value)

    def start(self):
        print("The Vehicle is starting")

    def stop(self):
        print("The vehicle is Stopping")

class car(Vehicle):
    def __init__(self,brand,model,year,type,fuel):
        super().__init__(brand,model,year,fuel)
        self.type = type


class bike(Vehicle):
    def __init__(self,brand,year,model,fuel,number_of_wheels):
        super().__init__(brand,year,model,fuel)
        self.number_of_wheels = number_of_wheels

car1 = car("Tesla","Model_X",2024,"Suv","Electric")
bike1 = bike("Hero Honda",2025,"Splendor","Petrol",2)
