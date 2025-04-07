"""A list of available burgers.

Each burger is represented as a list: [ID, Name, Price]
"""
burger_list = [
    [1, "Mig Bac", 16],
    [2, "Cheese Burger", 10],
    [3, "Chicken Burger", 11],
    [4, "Quarter Pounder", 9],
]

# This list will hold all items the user adds to their cart
cart_items = []


def menu():
    """Display the main menu where the user chooses what they want to do."""
    while True:
        # Prompt user to choose an action
        user_input = input("Where would you like to go?\n"
                           "1: Order a burger\n"
                           "2: Cart\n"
                           "3: checkout\n"
                           "4: exit\n> ")

        # Call the corresponding function based on user input
        if user_input == "1":
            order()
            break

        elif user_input == "2":
            cart()
            break

        elif user_input == "3":
            checkout()
            break

        elif user_input == "4":
            end()

        else:
            print("That is not an option\nPlease select a number from 1-4")


def checkout():
    """
    Calculate and display the total amount for all items in the cart.

    Then end the program.
    """
    print("Checking out...")
    total = 0
    # Add up the prices of burgers and fries
    for item in cart_items:
        if isinstance(item, list):
            total += item[2]  # burger price
        elif item == "Fries":
            total += 3  # price for fries
    print(f"Total amount: ${total}")
    print("Thank you for your order!")
    end()
    return ""


def order():
    """
    Display the burger menu, allows user to select a burger.

    Optionally add fries, and decide if they want to order more.
    """
    while True:
        print("Here is our burger menu:")
        for burger in burger_list:
            print(f"{burger[0]}: {burger[1]} - ${burger[2]}")

        user_input = input("Please enter the number "
                           "of the burger you would like\n> ")

        # Match user input with burger options
        if user_input == "1":
            cart_items.append(burger_list[0])
            print("You have added a Mig Bac to your cart")
            fries()
            again()
            break
        elif user_input == "2":
            cart_items.append(burger_list[1])
            print("You have added a Cheese Burger to your cart")
            fries()
            again()
            break
        elif user_input == "3":
            cart_items.append(burger_list[2])
            print("You have added a Chicken Burger to your cart")
            fries()
            again()
            break
        elif user_input == "4":
            cart_items.append(burger_list[3])
            print("You have added a Quater Pounder to your cart")
            fries()
            again()
            break
        else:
            print("That is not an option please enter the number of the item")


def fries():
    """Asks users if they would like to add fries to their order."""
    while True:
        fries = input("Would you like fries with your burger? (Y/N)\n> ")
        if fries == "Y" or fries == "y":
            print("Alright fries have been added to cart")
            cart_items.append("Fries")
            break
        elif fries == "N" or fries == "n":
            print("Alright")
            break
        else:
            print("please enter 'Y' or 'N'")


def again():
    """Asks the user if they would like to order another burger."""
    while True:
        again = input("Would you like to order another burger? (Y/N)\n> ")
        if again == "Y" or again == "y":
            print("Alright")
            order()
        elif again == "N" or again == "n":
            print("Alright")
            menu()
        else:
            print("Please enter 'Y' or 'N'")


def cart_menu():
    """
    Allow users to either remove an item from the cart.

    Or go back to the main menu.
    """
    while True:
        choice = input("\n1: Remove an item\n2: Back to menu\n> ")

        if choice == "1":
            if not cart_items:
                print("Cart is empty.")
                return

            # Show all items with indexes for user to remove
            for i, item in enumerate(cart_items):
                name = item[1] if isinstance(item, list) else item
                print(f"{i + 1}: {name}")

            num = input("Enter item number to remove:\n> ")

            if num.isdigit():
                index = int(num) - 1
                if 0 <= index < len(cart_items):
                    cart_items.pop(index)
                    print("Item removed.")
                else:
                    print("Invalid number.")
            else:
                print("Enter a number.")

        elif choice == "2":
            menu()
            break

        else:
            print("Enter 1 or 2.")


def cart():
    """Display all items currently in the cart."""
    if not cart_items:
        print("Your cart is empty.")
    else:
        print("Your cart contains:")
        for item in cart_items:
            if isinstance(item, list):  # burgers
                print(f"- {item[1]}: ${item[2]}")
            else:  # fries
                print(f"- {item}")
    cart_menu()


def end():
    """End the program with a goodbye message."""
    print("See you next time.")
    exit()


# Start the program by calling the menu function
menu()
