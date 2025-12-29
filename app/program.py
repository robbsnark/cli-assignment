import shoppe

# 'program.py' runs the program and asks afterwards if the user wants to play again

while True:
    shoppe.enter_shop()

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