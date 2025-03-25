# I am going to use time to have little pauses in some of the code to make it easier to read for the user
import time

# All of these lists are used to create the burger
order = [[]]
meat = ["Beef", "Chicken", "Fish", "None"]
cheese = ["Cheddar", "Swiss", "Grated", "None"]
toppings = ["Lettuce", "Tomato", "Onion", "Egg", "Bacon", "None"]
sauce = ["Tomato Sauce", "BBQ Sauce", "Mayonnaise", "Aioli", "None"]
sides = ["Fries", "Hashbrown", "Salad", "None"]
drink = ["Coca-Cola", "Pepsi", "Water", "None"]

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
    print("Hello")

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
