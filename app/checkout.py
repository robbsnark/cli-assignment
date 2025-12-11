from catalogue import Catalogue

class Checkout:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def basket(self):
        print("Your basket contains:")
        for item in self.items:
            print("-", item)
