import catalogue, checkout
import json

# 'menu.py' exands on the individual workings of the menu options
# These are pretty much step 2 after picking something in the main menu
# Here lies the 'buy' function, which is especially important for the program to work

class Menu(catalogue.Catalogue):
    basket = []

    def menu(self):
        print("Welcome to the YARN STORE. \n" \
            "We have all colours and kinds of YARN you'll ever need. \n" \
            "You're welcome to BROWSE our catalogue and BUY anything you like. \n" \
            "And don't forget to leave a little something in our charity bin.")
        print("What would you like to do? \n" \
            "B - BUY WARES \n" \
            "V - VIEW BASKET \n" \
            "L - LEAVE SHOP")

# THE 'BUY' FUNCTION
# A while loop (built similarly to the menu in shoppe.py) responsible for saving the user's order selection
# When the user confirms their order, it's sent to the shopping basket

    def buy(self):
        while True:
            ware_choice = self.cat()

            print("So you want", ware_choice, "? \n" \
                "Y - YES, that's right \n" \
                "N - NO, I changed my mind")
            
            confirm_order = input()
            if confirm_order.upper() == "Y":
                print("Selection confirmed.")
                self.basket.append(str(ware_choice))
                with open('basket_history.json', 'w') as file:
                    json.dump(str(ware_choice), file)
                return ware_choice
            elif confirm_order.upper() == "N":
                print("That's quite alright. Pick again.")
                continue
            else:
                print("Say again?")
                continue
            

    def view_basket(self):
        print("Your basket currently contains:")
        for b in self.basket:
            print("•", self.basket)


    def charity(self):
        print("Have a nice day ♥")
        # charity_loop = True
        # while charity_loop:
        #     print("Hey, hold on! Wouldn't you like to spare a little something for our charity tin? \n" \
        #     "YES / NO")
        #     donate = input()

        #     if donate.upper() == "YES":
        #         print("How much would you like to donate?")
        #         donate_sum = input()
        #         # something like:
        #         # (int)donate_sum += charity_bin
        #     elif donate.upper() == "NO":
        #         print("Hmph, alright...")
        #         charity_loop = False
        #     else:
        #         print("Say again?")

    def leave(self):
        print("Leave chosen")
        checkout.basket()
        # self.charity()