from catalogue import Catalogue
import json

# 'checkout.py' handles payment, balance and receipts
# That's pretty much it

class Checkout:
    def __init__(self, balance=100):
        self.wares = []
        self.balance = balance

        try:
            with open("receipts.json") as file:
                previous = json.load(file)
                print("You previously bought:")
                for item in previous:
                    print("•", item)
        except FileNotFoundError:
            pass


    def add_ware(self, ware):
        self.wares.append(ware)
        print(f"Added to basket: {ware}")


    def total(self):
        return sum(ware.price for ware in self.wares)


    def basket(self):
        print("Your basket contains:")
        for ware in self.wares:
            print("-", ware)
        print(
            "Total:", self.total(), "credits \n" \
            "Would you like to pay or continue browsing? \n" \
            "Y - YES, I'd like to pay \n" \
            "N - NO, I'd like to keep browsing"
        )
        checkout_choice = input()
        if checkout_choice.upper() == "Y":
            self.pay()
        elif checkout_choice.upper() == "N":
            print("Go ahead.")


    def pay(self):
        total = self.total()
        if self.balance >= total:
            self.balance -= total
            print("Thank you kindly. Your wallet still contains:", self.balance)

            with open('receipts.json', 'w') as file:
                json.dump([str(w) for w in self.wares], file)
            
            print("You bought: ")
            for ware in self.wares:
                print("•", ware)
            print("You spent:", total)

            self.wares.clear()
        else:
            print("It seems you don't have enough funds.")