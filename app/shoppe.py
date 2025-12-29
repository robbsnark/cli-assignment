import menu, checkout

# PROGRAM START --------------------------------------
# 'shoppe.py' contains the workings of the main menu
# This is where the program starts and where the user is usually sent after an action

def enter_shop():
    pay = checkout.Checkout()
    shop = menu.Menu(pay)
    shop_loop = True

    while shop_loop:
        shop.menu()
        menu_choice = input()

        if menu_choice.upper() == "B":
            shop.buy()
        elif menu_choice.upper() == "V":
            shop.view_basket()
        elif menu_choice.upper() == "L":
            pay.basket()
            shop_loop = False
        else:
            print("Sorry, I didn't catch that.")

# -----------------------------------------------