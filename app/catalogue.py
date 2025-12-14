from ware import Ware

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

        print("Available SIZES are: ", weights, "\n" \
        "Which SIZE would you like?")
        weight_choice = input()

        print("Available FIBERS are:")
        for fiber in fibers:
            print(fiber)
        ("Which type of FIBER would you like?")
        fiber_choice = input().upper()

        return Ware(colour_choice, weight_choice, fiber_choice)