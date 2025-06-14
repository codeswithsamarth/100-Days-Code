# Now there is a one problem that for each object we want to write attribute similarly
from tkinter.font import names


class Item:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

        def calculate_total_price(self,x,y):
            return x * y

item1 = Item("Phone",100,5)

item2 = Item("Laptop",500,2)

print(item1.name,item1.price,item1.quantity)

print(item2.name,item2.price,item2.quantity)