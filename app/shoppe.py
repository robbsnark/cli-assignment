import menu, checkout

def enter_shop():
    shop = menu.Menu()
    pay = checkout.Checkout()
    shop_loop = True

    while shop_loop:
        shop.menu()
        menu_choice = input()

        if menu_choice.upper() == "B":
            ware = shop.buy()
            if ware:
                pay.add_ware(ware)
        elif menu_choice.upper() == "V":
            # pay.basket()
            shop.view_basket()
        elif menu_choice.upper() == "L":
            pay.basket()
            shop.charity()
            shop_loop = False
        elif menu_choice.upper() == "E":
            shop_loop = False
        else:
            print("Sorry, I didn't catch that.")