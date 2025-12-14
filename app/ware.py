
class Ware:
    def __init__(self, colour, weight, fiber):
        self.colour = colour
        self.weight = int(weight)
        self.fiber = fiber
        self.price = self.calculate_price()

    def calculate_price(self):
        fiber_prices = {
            'ACRYLIC': 5,
            'COTTON': 5,
            'WOOL': 10,
            'CHENILLE': 15,
            'RIBBON': 15,
            'MERINO WOOL': 20
        }

        if 0 <= self.weight <= 2:
            weight_price = 0
        elif 3 <= self.weight <= 5:
            weight_price = 5
        elif 6 <= self.weight <= 7:
            weight_price = 10
        else:
            print("Please pick a weight between 0 and 7.")

        fiber_price = fiber_prices[self.fiber]
        total_price = fiber_price + weight_price

        return total_price
    

    def __str__(self):
        return f"{self.colour} {self.fiber} YARN in SIZE {self.weight}"
    