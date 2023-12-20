import math

# A program which allows the user to add, remove and checkout with items that they purchase
# This program is a simplified version to pet-store and will include functions

# List of items

menu = [
    "Purina One Cat Salmon - Whole Grain               ",
    "Iams Senior 7+ Cat Food With Ocean Fish           ",
    "Iams Adult 1+ Cat Food With Fresh Chicken         ",
    "Felix As Good As It Looks Cat Food Mixed Selection",
    "Felix Doubley Delicious Cat Food Meaty Selection  ",
    "Winalot Wet Dog Food Pouches Meaty Chunks In Jelly",
    "Bakers Whirlers Double Flavour Twisted Treats     ",
    "Chicken And Country Vegetable Dry Dog Food        ",
]

prices = [7.99, 5.99, 3.99, 7.00, 4.00, 3.99, 4.00, 6.99]

# Display the menu and the cart until the user checks out
print("\nWelcome to Pawesome Warehouse \n\nWhat would you like to do?\n")

done = False
while not done:
    print(
        "1. Add an item to your cart \n2. Remove an item from your cart \n3. View your cart \n4. Checkout"
    )
    choice = input(
        "\nPlease enter the number of the option that you would like to choose: "
    )
    break
    done = True


# Class to include all data and functions of the shopping cart
class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item, price):
            if item in self.items: 
                self.items[item] += price 
            