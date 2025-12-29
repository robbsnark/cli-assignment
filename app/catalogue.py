from ware import Ware

# 'catalogue.py' holds the shop's stock and details about the items
# This is simply where the customer is sent to make their choices about what to buy

class Catalogue():
    def cat(self):
        print("Here you can pick a COLOUR, SIZE and finally TYPE OF FIBER.")

        colours = ['GREEN', 'BROWN', 'YELLOW',
                  'RED', 'PINK', 'BLUE']
        weights = [0, 1, 2, 3, 4, 5, 6, 7]
        fibers = ['COTTON', 'RIBBON', 'ACRYLIC', 
                  'CHENILLE', 'WOOL', 'MERINO WOOL']

        print("Available COLOURS are:")
        for colour in colours:
            print(colour)
        print("What COLOUR would you like?")
        colour_choice = input().upper()

        print(
            "Available SIZES are: ", weights, "\n" \
            "Which SIZE would you like?"
        )
        while True:
            try:
                weight_choice = int(input())
                if weight_choice not in weights:
                    print("Please pick a number between 0 and 7.")
                    continue
                break
            except ValueError:
                print("Please pick a number between 0 and 7.")

        print("Available FIBERS are:")
        for fiber in fibers:
            print(fiber)
        print("Which type of FIBER would you like?")
        fiber_choice = input().upper()

        return Ware(colour_choice, weight_choice, fiber_choice)