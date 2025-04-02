burger_list = [
    ["Mig Bac", 15.99], 
    ["Cheese Burger", 10.99], 
    ["Chicken Burger", 10.99]
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
    print(burger_list)
    while True:
        found_burger = find_burger()
        print(found_burger)



def find_burger():
    while True:
        user_input = input("Please enter the name of the burger you would like \n> ").lower().strip()
        for burger in burger_list:
            if burger[0].strip().lower() == user_input:
                burger_found = burger
                return burger_found
            

        print("Burger not found")



def cart():
    print("Hor")


def end():
    print("See you next time.")
    exit()

menu()