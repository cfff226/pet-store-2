import math

# A program which allows the user to add, remove and checkout with items that they purchase
# This program is a simplified version to pet-store and will include functions

print("\nWelcome to Pawesome Warehouse \n\nWhat would you like to do?\n")

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
def add_item(shopping_cart, shopping_quant):
    print(
        "----------------------------------------------------------------------------------\n\t\t\t\t\tMENU\n"
    )
    for i in range(len(menu)):
        print(str(i + 1) + ". " + menu[i], "\t\t\t", "£", (prices[i]), "\n")
    print(
        "\n----------------------------------------------------------------------------------\n"
    )

    try:
        item = int(
            input(
                "\nPlease input the number of the item that you would like to add to your cart: "
            )
        )
    except ValueError:
        print("You have entered an incorrect value")
        add_item(shopping_cart, shopping_quant)

    while True:
        try:
            quant = int(
                input("\nPlease input the quantity of the item you wish to purchase: ")
            )
            break
        except ValueError:
            print("\n\nYou've entered an incorrect value")
            continue

    if menu[item - 1] in shopping_cart:
        print("repeated order")
        idx = shopping_cart.index(menu[item - 1])
        shopping_quant[idx] += quant

    else:
        print("\n\n\t\tNew selection\n")
        shopping_cart.append(menu[item - 1])
        shopping_quant.append(quant)
        print("\nThis item has been added to your cart successfully\n")


# View shopping cart
def view_cart(shopping_cart, shopping_quant, price_total):
    if shopping_cart == []:
        print(
            "\n\n\t\tYour cart is currently empty\n\n"
        )
    else:
        for i in range(len(shopping_cart)):
            idx = menu.index(shopping_cart[i])
            unit_price = prices[idx]
            unit_price = unit_price * shopping_quant[i]
            price_total.append(unit_price)
            total = sum(price_total)

            print(
                f"\nItem {i + 1}: {shopping_cart[i]} Quantity: {shopping_quant[i]}        \
                        Price: £{unit_price}\n\n-------------------------------------------------------------------------------------------------------------------\n"
            )
        print(f"\n\nYour cart total is £{total}\n\n")
        price_total.clear()


# Remove item from cart
def remove_item(shopping_cart, shopping_quant, item_to_remove):
    try:
        remove_item_input = int(
            input("\nPlease input the number of the item you wish to remove: ")
        )
        print("\nYou selected: ", shopping_cart[remove_item_input - 1])
    except ValueError:
        print("\n\n\t\tYou have entered an incorrect value")
        remove_item(shopping_cart, shopping_quant, item_to_remove)
    except IndexError:
        print("\n\n\t\tThis item does not exist in your cart")
        remove_item(shopping_cart, shopping_quant, item_to_remove)

    while True:
        try:
            quant = int(
                input("\nPlease input the quantity of the item you wish to remove: ")
            )
            break
        except ValueError:
            print("\n\n\t\tYou have entered an incorrect value")
            continue

    if shopping_cart[remove_item_input - 1] in shopping_cart:
        idx = shopping_cart.index(shopping_cart[remove_item_input - 1])
        item_to_remove = shopping_cart[remove_item_input - 1]
        shopping_quant[idx] = shopping_quant[idx] - quant

        if item_to_remove in shopping_cart and shopping_quant[idx] == 0:
            shopping_cart.remove(shopping_cart[remove_item_input - 1])
            shopping_quant[idx] = 1

    print("\n\n\t\tYour changes to the shopping cart have been successful")


def main():
    shopping_cart = []
    shopping_quant = []
    price_total = []
    item_to_remove = ""

    while True:
        # Display the menu and the cart until the user checks out
        print("\n\t\tMenu:\n")
        print(
            "\n\n1. Add an item to your cart \n2. View your cart \n3. Remove an item from your cart \n4. Checkout"
        )
        choice = input(
            "\nPlease enter the number of the option that you would like to choose: "
        )
        if choice == "1":
            add_item(shopping_cart, shopping_quant)
        elif choice == "2":
            view_cart(shopping_cart, shopping_quant, price_total)
        elif choice == "3":
            remove_item(shopping_cart, shopping_quant, item_to_remove)
        elif choice == "4":
            print(
                "\n\n\t\t-------------------- Thank you for shopping at Pawsome Warehouse --------------------\n\n"
            )
            break
        else:
            continue


main()
