
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

class Catalogue:
    # Order by colour / weight / ?
    def cat():
        print("This is where all the wares would be.")
        colours = ['black', 'white', 'grey',
                  'green', 'brown', 'orange', 'yellow',
                  'red', 'pink', 'purple', 'blue']
        weights = [0, 1, 2, 3, 4, 5, 6, 7]
        fibers = ['cotton', 'ribbon', 
                  'acrylic', 'chenille',
                  'wool', 'merino wool', 'alpaca wool']
        print("Available colours are: ", colours, "\n" \
        "Which colour would you like?")
        colour_choice = input()
        print("Available sizes are: ", weights, "\n" \
        "Which size would you like?")
        weight_choice = input()
        print("Available fibers are: ", fibers, "\n" \
        "Which type of fiber would you like?")
        fiber_choice = input()
        ware_choice = colour_choice, " ", fiber_choice, " yarn in size ", weight_choice
        return ware_choice


# END OF CATALOGUE CLASS

# ----------------------------------------------

# START OF MENU CLASS:

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
        Catalogue.cat()
        print()

    def buy(self):
        print("Do you know what you want or do you need to browse first? \n" \
        "Y - YES, I know what I want \n" \
        "N - NO, I would like to browse the catalogue \n" \
        "X - I changed my mind.")

        buy_choice = input()
        if buy_choice.upper() == "Y":
            print("Which colour yarn would you like? And which size?")
            order = input()
        elif buy_choice.upper() == "N":
            Catalogue.cat()
        else:
            print("That's quite alright.")

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

# ASKING TO PLAY AGAIN:
# NEEDED: way to loop back to shop menu

print("Would you like to revisit the shop (PLAY AGAIN)? \n" \
"YES / NO")
revisit = input()

if revisit.upper() == "YES":
    shop_loop == True
    # Then a loop option that works better than just "shop.menu()"
elif revisit.upper() == "NO":
    print("Off you go then.")
else:
    print("Come again?")

# END OF PROGRAM

# ----------------------------------------------