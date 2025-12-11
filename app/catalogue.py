class Catalogue():
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