burger_list = [
    [1, "Mig Bac", 16], 
    [2, "Cheese Burger", 10], 
    [3, "Chicken Burger", 11],
    [4, "Quater Pounder", 9],
]

cart_items = []


def menu():
    """
    is the menu where users will chooses what they want to do.
    """

    while True:

        user_input = input("Where would you like to go?\n1: Order a burger\n"
        "2: Cart\n3: checkout\n4: exit\n> ")

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
    print("Hello")


def order():
    while True:
        print(burger_list)
        user_input = input("Please enter the number of the burger you would like\n> ")
        if user_input == "1":
            cart_items.append(burger_list[0])
            print("You have added a Mig Bac to your cart")
            fries()
            again()
            break
        elif user_input == "2":
            cart_items.append(burger_list[1])
            print("You have added a Cheese Burger to you cart")
            fries()
            again()
            break
        elif user_input == "3":
            cart_items.append(burger_list[2])
            print("You have added a Chicken Burger to you cart")
            fries()
            again()
            break
        elif user_input == "4":
            cart_items.append(burger_list[3])
            print("You have added a Quater Pounder to you cart")
            fries()
            again()
            break
        else:
            print("That is not an option")

def fries():    
    """
    This asks users if they would like fries with their burger
    """
    while True:
        fries = input("Would you like fries with your burger? (Y/N)\n> ")
        if fries == "Y" or fries == "y":
            print("Alright fries have been added to cart")
            cart_items.append("Fries")
            break
        elif fries == "N" or fries == "n":
            print("Alright")
            menu()
        else:
            print("please enter 'Y' or 'N'")

def again():
    """
    This is used to ask the user if they would like to order another burger
    """
    while True:
        again = input("Would you like to order another burger? (Y/N)\n> ")
        if again == "Y" or again == "y":
            print("Alright")
            order()
        elif again == "N" or again == "n":
            print("Alright")
            menu()
        else:
            ("Please enter 'Y' or 'N'")

def cart():
    print(cart_items)


def end():
    print("See you next time.")
    exit()

menu()