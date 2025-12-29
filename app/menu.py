import catalogue, checkout

# 'menu.py' expands on the individual workings of the menu options
# These are pretty much step 2 after picking something in the main menu
# Here lies the 'buy' function, which is especially important for the program to work

class Menu(catalogue.Catalogue):
    def __init__(self, checkout):
        self.checkout = checkout

    def menu(self):
        print(
            "Welcome to the YARN STORE. \n" \
            "We have all colours and kinds of YARN you'll ever need. \n" \
            "You're welcome to BROWSE our catalogue and BUY anything you like. \n" \
            "And don't forget to leave a little something in our charity bin."
        )
        print(
            "What would you like to do? \n" \
            "B - BUY WARES \n" \
            "V - VIEW BASKET \n" \
            "L - LEAVE SHOP"
        )

# THE 'BUY' FUNCTION
# A while loop (built similarly to the menu in shoppe.py) responsible for saving the user's order selection
# When the user confirms their order, it's sent to the shopping basket and saved to a file

    def buy(self):
        while True:
            ware_choice = self.cat()

            print(
                "So you want", ware_choice, "? \n" \
                "Y - YES, that's right \n" \
                "N - NO, I changed my mind"
            )
            
            confirm_order = input()
            if confirm_order.upper() == "Y":
                print("Selection confirmed.")
                self.checkout.add_ware(ware_choice)

                with open('basket_history.json', 'a') as file:
                    file.write(str(ware_choice) + "\n")
                return
            
            elif confirm_order.upper() == "N":
                print("That's quite alright. Pick again.")
                continue
            else:
                print("Say again?")
                continue
            

    def view_basket(self):
        print("Your basket currently contains:")
        if not self.checkout.wares:
            print("Your basket is currently empty.")
        for ware in self.checkout.wares:
            print("•", ware)