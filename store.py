


class Item:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price


    # def __str__(self):
    #     return f"Item: name: {self.name} price: {self.price}"


class Store:
    items: {str: Item}

    def __init__(self, name):
        print("Store Name: ", name)
        self.name = name

    def add_item(self, name: str, price: float):
        item = Item(name=name, price=price)
        self.items[name] = item

    def get_item(self, name: str):
        return self.items[name]

    def default(self, o):
        return o.__dict__



            # def __str__(self):
    #     if item in self.items:
    #         return  f"Store: Name-{self.name}: item: "
    #     return f"Store: name:{self.name} Items:{self.items}"
