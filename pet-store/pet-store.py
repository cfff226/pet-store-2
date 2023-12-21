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


# Add item to cart
def add_item(shopping_cart):
    for i in range(len(menu)):
        print(str(i + 1) + ". " + menu[i], prices[i])

    try:
        item = int(
            input(
                "\nPlease input the number of the item that you would like to add to your cart: "
            )
        )
        shopping_cart.append(menu[item - 1])
        print(shopping_cart)
    
        print(menu[item -1])
        if menu[item -1] in shopping_cart:
            print("this item is in your cart")

    except ValueError:
        print("You have entered an incorrect value")
        add_item(shopping_cart)















def main():
    shopping_cart = []
    shopping_quant = []
    price_total = []

    while True:
        # Display the menu and the cart until the user checks out
        print("\nWelcome to Pawesome Warehouse \n\nWhat would you like to do?\n")

        print(
            "1. Add an item to your cart \n2. Remove an item from your cart \n3. View your cart \n4. Checkout"
        )
        choice = input(
            "\nPlease enter the number of the option that you would like to choose: "
        )
        if choice == "1":
            add_item(shopping_cart)
        # elif choice == "2":
        #     view_cart(shopping_cart)
        # elif choice == "3":
        #     remove_item(shopping_cart)
        # elif choice == "4":
        # print("Thank you for shopping at Pawesome Warehouse")
        # else:
        # continue


main()
