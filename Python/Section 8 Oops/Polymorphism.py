# polymorphism means many form examples in built in
"""
+ operator add two number also concatenate two strings
* operator multiply the number cause repetation if used in strings
"""
"""
Polymorphism allow object of different class to treated as objects of a common superclass
"""
class Vehicle:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print("Vehicle is starting")

    def stop(self):
        print("Vehicle is Stopping")

class motorcycle(Vehicle):
    def __init__(self,brand,model,year):
        super().__init__(brand,model,year)

class Car(Vehicle):
    def __init__(self,brand,model,year,number_of_doors):
        super().__init__(brand,model,year)

        self.number_of_doors = number_of_doors


vehicles = [
    Car("Ford", "Focus", 2008, 5),
    motorcycle("Honda","Scoppy",2010),
    ]

for vehicle in vehicles:
    if isinstance(vehicle,Vehicle):
        print(f"Inspecting {vehicle.brand} {vehicle.model} ({type(vehicle).__name__})")
        vehicle.start()
        vehicle.stop()
    else:
        raise Exception("No Vehicle Object Found")
# Loop Through List and Inspect them

# for vehicle in vehicles:
#     if isinstance(vehicle,Car):
#         print(f"Inspecting {vehicle.brand},{vehicle.model} ({type(vehicle).__name__})")
#         vehicle.start()
#         vehicle.stop()
#     elif isinstance(vehicle,motorcycle):
#         print(f"Inspecting {vehicle.brand},{vehicle.model} {type(vehicle).__name__}")
#         vehicle.start_bike()
#         vehicle.stop_bike()

#     else:
#         raise Exception("Invalid Object Object is not a valid vehicle")

