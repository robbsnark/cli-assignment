import menu

def enter_shop():
    shop = menu.Menu()
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