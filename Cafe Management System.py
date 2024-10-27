# Cafe management system!

Menu = {

        'Pizza' : 40,
        'Pasta' : 50,
        'Burger': 60,
        'Coffe' : 55,
        'Tea'  : 100,

}

#Greet
print("Welcome to python Restaurant: ")
print("Pizza: Rs40\n, Pasta: Rs50\n, Burger: Rs60\n, Coffe: Rs100\n Tea: Rs100")

while True:

    order_total = 0
    item_1 = input("Enter the name of the item you want to order: = ")

    if item_1 in Menu:
        order_total += Menu[item_1]
        print(f"Your {item_1} has been added to your order")
    else:
        print(f"The item {item_1} is not available")

    another_item = input("Do you want anything else (Yes/No)")

    if another_item == "Yes":
        item_2 = input("Enter the name of item: ")

        if item_2 in Menu:
            order_total += Menu[item_2]
            print(f"Your {item_2} has been successfully added to order :")

        else:
            print(f"Your order {item_2} is not in the menu today:")

    print(f"The total amount of the order is Rs{order_total}: ")
    payement = input("How would you like to pay ? (Card/Cash)")
    if payement == "Card":
        print("OK , Swipe Your card here! ")
    else:
        print(f"Give Rs{order_total}\n Thank you!  ")

