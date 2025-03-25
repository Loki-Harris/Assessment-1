# All of these lists are used to create the burger
order = []
meat = ["Beef", "Chicken", "Fish"]
cheese = ["Cheddar", "Swiss", "Grated"]
toppings = ["Lettuce", "Tomato", "Onion", "Egg", "Bacon",]
sauce = ["Tomato Sauce", "BBQ Sauce", "Mayonnaise", "Aioli"]
sides = ["Fries", "Hashbrown", "Salad", "Nothing"]
drink = ["Coca-Cola", "Pepsi", "Water"]

print("Welcome to the Burger Shop")

def menu():

    user_choice = input("What would you like to do?\n"
    "1: Create a burger\n2: Cart\n3: Checkout\n4: Exit\n> ")
    if user_choice == "1":
        create()
    elif user_choice == "2":
        cart()
    elif user_choice == "3":
        checkout()
    elif user_choice == "4":
        end()
    else:
        print("That is not a valid number")
        menu()


def create():
    print("Hello")

def cart():
    print("Hi")

def checkout():
    print("No")

def end():
    print("See you next time")
    exit()

menu()
