
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

# ----------------------------------------------

# THOUGHTS:
# Give charity bin its own class ?
# Does the PLAY AGAIN bit need its own class ?

# TO-DO:
# Create inventory / Catalogue
# Implement buying + paying system
# Implement return + refund system
# 

# ----------------------------------------------

# START OF CATALOGUE CLASS:

class Catalogue():
    # Order by colour / weight / ?
    def cat(self):
        print("Here you can pick a COLOUR, SIZE and finally TYPE OF FIBER.")

        colours = ['black', 'white', 'grey',
                  'green', 'brown', 'orange', 'yellow',
                  'red', 'pink', 'purple', 'blue']
        weights = [0, 1, 2, 3, 4, 5, 6, 7]
        fibers = ['cotton', 'ribbon', 
                  'acrylic', 'chenille',
                  'wool', 'merino wool', 'alpaca wool']
        
        print("Available colours are: ", colours, "\n" \
        "What colour would you like?")
        colour_choice = input()
        print("Available sizes are: ", weights, "\n" \
        "Which size would you like?")
        weight_choice = input()
        print("Available fibers are: ", fibers, "\n" \
        "Which type of fiber would you like?")
        fiber_choice = input()

        ware_choice = (f"{colour_choice}, {fiber_choice}, {weight_choice}")
        return ware_choice


# END OF CATALOGUE CLASS

# ----------------------------------------------

# START OF MENU CLASS:

class Menu(Catalogue):
    def menu(self):
        print("Welcome to the YARN STORE. \n" \
            "We have all colours of YARN you'll ever need. \n" \
            "You're welcome to BROWSE our catalogue and BUY anything you like. \n" \
            "And don't forget to leave a little something in our charity bin.")
        print("What would you like to do? \n" \
            "B - BUY WARES \n" \
            "R - RETURN WARES \n" \
            "L - LEAVE SHOP")

    def buy(self):
        ware_choice = self.cat()
        print("So you want ", ware_choice + "? \n" \
            "Y - YES, that's right \n" \
            "N - NO, I changed my mind")
        confirm_order = input()
        if confirm_order.upper() == "Y":
            print("")
        elif confirm_order.upper() == "N":
            print("nvm")            

    def ret_wares(self):
        print("What would you like to return?")

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
        self.charity()

# END OF MENU CLASS

# ----------------------------------------------

# START OF PROGRAM:

def enter_shop():
    shop = Menu()
    shop_loop = True

    while shop_loop:
        shop.menu()
        menu_choice = input()

        if menu_choice.upper() == "B":
            shop.buy()
        elif menu_choice.upper() == "R":
            shop.ret_wares()
        elif menu_choice.upper() == "L":
            shop.leave()
        elif menu_choice.upper() == "E":
            shop_loop = False
        else:
            print("Sorry, I didn't catch that.")

# ASKING TO PLAY AGAIN:

while True:
    enter_shop()

    print("Would you like to revisit the shop (PLAY AGAIN)? \n" \
        "YES / NO")
    revisit = input()

    if revisit.upper() == "YES":
        continue
    elif revisit.upper() == "NO":
        print("Off you go then.")
        break
    else:
        print("Come again?")

# END OF PROGRAM

# ----------------------------------------------