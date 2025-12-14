from app.catalogue import Catalogue
import json

class Checkout:
    def __init__(self, balance=100):
        self.wares = []
        self.balance = balance

    def add_ware(self, ware):
        self.wares.append(ware)
        print(f"Added to basket: {ware}")

    def total(self):
        return sum(ware.price for ware in self.wares)

    def basket(self):
        print("Your basket contains:")
        for ware in self.wares:
            print("-", ware)
        print("Total:", self.total(), "credits \n" \
        "Would you like to pay or continue browsing? \n" \
        "Y - YES, I'd like to pay \n" \
        "N - NO, I'd like to keep browsing")
        checkout_choice = input()
        if checkout_choice == "Y".upper():
            self.pay()
        elif checkout_choice == "N".upper():
            print("Go ahead.")

    def pay(self):
        total = self.total()
        if self.balance >= total:
            self.balance -= total
            print("Thank you kindly. Your wallet still contains:", self.balance)
            self.wares.clear()
            with open('ware_choice.json', 'r') as ware_choice, open('receipts.json', 'r') as receipts:
                receipts_insert = json.load(ware_choice)
                destination = json.load(receipts)
                destination.append(receipts_insert)
            with open('receipts.json', 'w') as receipts:
                json.dump(receipts, destination)
        else:
            print("It seems you don't have enough funds.")