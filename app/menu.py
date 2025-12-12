import catalogue, checkout
import json

class Menu(catalogue.Catalogue):
    def menu(self):
        print("Welcome to the YARN STORE. \n" \
            "We have all colours and kinds of YARN you'll ever need. \n" \
            "You're welcome to BROWSE our catalogue and BUY anything you like. \n" \
            "And don't forget to leave a little something in our charity bin.")
        print("What would you like to do? \n" \
            "B - BUY WARES \n" \
            "V - VIEW BASKET \n" \
            "L - LEAVE SHOP")

    def buy(self):
        while True:
            ware_choice = self.cat()

            print("So you want", ware_choice + "? \n" \
                "Y - YES, that's right \n" \
                "N - NO, I changed my mind")
            
            confirm_order = input()
            if confirm_order.upper() == "Y":
                print("Selection confirmed.")
                with open('ware_choice.json', 'w') as file:
                    json.dump(ware_choice, file)
                return ware_choice
            
            elif confirm_order.upper() == "N":
                print("That's quite alright. Pick again.")
                continue
            else:
                print("Say again?")
                continue
            

    def view_basket(self):
        with open('ware_choice.json', 'r') as file:
            view_basket = json.load(file)
        print("Your basket contains: ", view_basket)


    def charity(self):
        print("Hey, hold on! Wouldn't you like to spare a little something for our charity tin? \n" \
        "YES / NO")
        donate = input()

        if donate.upper() == "YES":
            print("How much would you like to donate?")
            donate_sum = input()
            # something like:
            # (int)donate_sum += charity_bin
        elif donate.upper() == "NO":
            print("Hmph, alright...")
        else:
            print("Say again?")
            self.charity()

    def leave(self):
        print("Leave chosen")
        # pay = checkout.Checkout()
        # pay.basket()
        self.view_basket()
        self.charity()