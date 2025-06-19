import csv
class Item:
    all = []
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        return f"Item('{self.name},{self.price},{self.quantity}')"

    @classmethod
    def instantiate_from_csv(cls):
        with open('item.csv','r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
            for item in items:
                Item(
                    name=item.get('name'),
                    price = int(item.get('price')),
                    quantity= int(item.get('quantity')),
                )

Item.instantiate_from_csv()
print(Item.all)