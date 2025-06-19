class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(f"{self.name},{self.salary}")

class Manager(Employee):
    def __init__(self,name,salary,team_size):
        super().__init__(name,salary)
        self.team_size = team_size

m1 = Manager("Sanket",14000,22)
m1.show()