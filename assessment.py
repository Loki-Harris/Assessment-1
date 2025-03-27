# I am going to use time to have little pauses in some of the code to make it easier to read for the user
import time

# All of these lists are used to create the burger
order = [] 
meat = ["Beef", "Chicken", "Fish", "None"]
cheese = ["Cheddar", "Swiss", "Grated", "None"]
toppings = ["Lettuce", "Tomato", "Onion", "Egg", "Bacon", "None"]
sauce = ["Tomato Sauce", "BBQ Sauce", "Mayonnaise", "Aioli", "None"]
sides = ["Fries", "Hashbrown", "Salad", "None"]
drink = ["Coca-Cola", "Pepsi", "Water", "None"]
burger = []

print("Welcome to the Burger Shop")

# Is the menu that the user will choose what to do
def menu():

    user_choice = input("What would you like to do?\n"
    "1: Create a burger\n2: Cart\n3: Checkout\n4: Exit\n> ")
    if user_choice == "1":
        create_burger()
    elif user_choice == "2":
        cart()
    elif user_choice == "3":
        checkout()
    elif user_choice == "4":
        end()
    else:
        print("That is not a valid number")
        menu()

# Will be how the user will create their burger with sides and drink
def create_burger():
    print(meat)
    user_choice_meat = input("We Will start with the meat please type the meat you would like\n>")
    print("Next is cheese")
    print(cheese)
    user_choice_cheese = input(">")
    print("Now are the toppings")
    add_toppings()
    print("Next are sides")
    print(sides)
    user_choice_sides = input(">")
    print("lastly what drink would you like")
    print(drink)
    user_choice_drink = input(">")
    burger.append(user_choice_meat)
    burger.append(user_choice_cheese)
    burger.append(user_choice_sides)
    burger.append(user_choice_drink)
    order.append(burger)
    menu()


def add_toppings():
        print(toppings)
        user_choice_toppings = input(">")
        repeater = True
        while repeater == True:
            user_choice = input("Would you like to add more toppings? Y/N\n>")
            if user_choice == "Y" or user_choice == "y":
                print("Alright what else would you like to add")
                burger.append(user_choice_toppings)
                print(toppings)
                user_choice_toppings = input(">")
            elif user_choice == "N" or user_choice == "n":
                print("Ok next")
                repeater = False
                burger.append(user_choice_toppings)
            else:
                print("That is not an option")
                add_toppings()

# Is how the user will check what they are ordering and if they want to remove anything from their order
def cart():
    print(order)
    user_input = input("Would you like to remove anything from your cart?\n> ")
    if user_input == "no" or "No":
        menu()
    elif user_input == "yes" or "Yes":
        print("I will do this later")
    else:
        print("That is not an option")
        cart()

# Is how the user will pay and order their food
def checkout():
    print("Not yet")

# Is used to exit the program
def end():
    print("See you next time")
    time.sleep(0.5)
    exit()

menu()
