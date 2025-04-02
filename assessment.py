burgers = ["Mig Bac", "Cheese Burger", "Chicken Burger"]



def menu():
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
            print("That is not an option")


def checkout():
    print("Hello")
    
def order():
    print(burgers)


def cart():
    print("Hor")

def end():
    print("See you next time.")
    exit()

menu()