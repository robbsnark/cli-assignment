
# throwing ideas around

# stock / library
# option thing 0: look at "menu" of things available
# option thing 1: put one in basket
# option thing 2: buy the thing
# option thing 3: return the thing

# option thing x: donate to charity

# calculation: how much did the store bring in
#               how much did the charity bring in

# you can return and fiddle with the store cash but not charity cash

class Menu:
    def menu(self):
        print("Welcome to the YARN STORE. \n" \
        "We have all colours of YARN you'll ever need. \n" \
        "You're welcome to BROWSE our catalogue and BUY anything you like. \n" \
        "And don't forget to leave a little something in our charity bin.")
        print("What would you like to do? \n" \
        "A - BROWSE CATALOGUE \n" \
        "B - BUY WARES \n" \
        "C - RETURN WARES \n" \
        "D - LEAVE SHOP")

    def browse(self):
        print("Browse chosen")

    def buy(self):
        print("Buy chosen")

    def ret_wares(self):
        print("Return wares chosen")
        print("What would you like to return?")

    def charity(self):
        print("Hey, hold on! Wouldn't you like to spare a little something for our charity tin? \n" \
        "YES / NO")
        donate = input()
        if donate.upper() == "YES":
            print("How much would you like to donate?")
            donate_sum = input()
        elif donate.upper() == "NO":
            print("Hmph, alright...")
        else:
            print("Say again?")
            self.charity()

    def leave(self):
        print("Leave chosen")
        self.charity()

# END OF MENU CLASS

# FILLER TEXT TO SEE IF THE REPO SYNC WORKS

# START OF PROGRAM:

shop = Menu()
shop_loop = True

while shop_loop == True:
    shop.menu()
    menu_choice = input()

    if menu_choice.upper() == "A":
        shop.browse()
    elif menu_choice.upper() == "B":
        shop.buy()
    elif menu_choice.upper() == "C":
        shop.ret_wares()
    elif menu_choice.upper() == "D":
        shop.leave()
    elif menu_choice.upper() == "E":
        shop_loop = False
    else:
        print("Sorry, I didn't catch that.")

class Catalogue:
    def cat():
        print("This is where all the wares would be.")