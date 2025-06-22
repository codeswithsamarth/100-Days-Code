class Employee:
    company = "Hp"
    def __init__(self,name,salary):
        self.salary = salary
        self.name = name


    @classmethod
    def print_company(cls):
        print(cls.company)

    @classmethod
    def change_company(cls,new_company):
        cls.company = new_company

e1 = Employee("Samarth",24545)

e1.print_company()
e1.change_company("Samarth")
e1.print_company()