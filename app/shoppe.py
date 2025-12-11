import menu, checkout

def enter_shop():
    shop = menu.Menu()
    pay = checkout.Checkout()
    shop_loop = True

    while shop_loop:
        shop.menu()
        menu_choice = input()

        if menu_choice.upper() == "B":
            item = shop.buy()
            if item:
                pay.add_item(item)
        elif menu_choice.upper() == "R":
            shop.ret_wares()
        elif menu_choice.upper() == "L":
            pay.basket()
            shop.charity()
            shop_loop = False
        elif menu_choice.upper() == "E":
            shop_loop = False
        else:
            print("Sorry, I didn't catch that.")