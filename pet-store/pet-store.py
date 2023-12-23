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
def add_item(shopping_cart, shopping_quant):
    for i in range(len(menu)):
        print(str(i + 1) + ". " + menu[i], prices[i])

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
        print(idx)
        shopping_quant[idx] += quant
    else:
        print("new selection")
        shopping_cart.append(menu[item - 1])
        shopping_quant.append(quant)

        print("\nThis item has been added to your cart successfully\n")


# View shopping cart
def view_cart(shopping_cart, shopping_quant, itemised_quant, price_total, final_total):
    for i in range(len(shopping_cart)):
        idx = menu.index(shopping_cart[i])
        unit_price = prices[idx]
        itemised_quant = shopping_quant[idx] * unit_price
        print(itemised_quant)
        price_total.append(itemised_quant)
        print(price_total)
        print(
            f"\nItem: {shopping_cart[i]} Quantity: {shopping_quant[i]}        \
                      Price: £{unit_price}\n\n---------------------------------------------------------------------------------------------------------------\n"
        )

    final_total = sum(price_total)
    print(f"Your shopping cart total is £{final_total}\n\n")


# Remove item from cart
def remove_item(shopping_cart, shopping_quant):
    try:
        remove_item_input = int(
            input("\nPlease input the number of the item you wish to remove: ")
        )
        print("\nYou selected: ", shopping_cart[remove_item_input - 1])
    except ValueError:
        print("You have entered an incorrect value")
        remove_item(shopping_cart, shopping_quant)
    except IndexError:
        print("This item does not exist in your cart")
        remove_item(shopping_cart, shopping_quant)

    while True:
        try:
            quant = int(
                input("\nPlease input the quantity of the item you wish to remove: ")
            )
            break
        except ValueError:
            print("You have entered an incorrect value")
            continue

    if shopping_cart[remove_item_input - 1] in shopping_cart:
        idx = shopping_cart.index(shopping_cart[remove_item_input - 1])
        shopping_quant[idx] = shopping_quant[idx] - quant
        if shopping_cart[remove_item_input -1] in shopping_cart and shopping_quant[idx] == 0:
            shopping_cart.pop(idx)

           
    
  











def main():
    shopping_cart = []
    shopping_quant = []
    price_total = []
    itemised_quant = 0
    final_total = 0

    print("\nWelcome to Pawesome Warehouse \n\nWhat would you like to do?\n")

    while True:
        # Display the menu and the cart until the user checks out

        print(
            "1. Add an item to your cart \n2. View your cart \n3. Remove an item from your cart \n4. Checkout"
        )
        choice = input(
            "\nPlease enter the number of the option that you would like to choose: "
        )
        if choice == "1":
            add_item(shopping_cart, shopping_quant)
        elif choice == "2":
            view_cart(shopping_cart, shopping_quant, itemised_quant, price_total, final_total)
        elif choice == "3":
            remove_item(shopping_cart, shopping_quant)
        # elif choice == "4":
        # print("Thank you for shopping at Pawesome Warehouse")
        # else:
        # continue


main()
