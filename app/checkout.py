from catalogue import Catalogue

class Checkout:
    def __init__(self):
        self.wares = []

    def add_ware(self, ware):
        self.wares.append(ware)

    def basket(self):
        print("Your basket contains:")
        for ware in self.wares:
            print("-", ware)
