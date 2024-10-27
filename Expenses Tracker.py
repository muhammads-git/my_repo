Expenses = []

#add expenses
def add_expenses():

    #collect data or expenses from user
    date = input("Enter the date :(DD/MM/YY) ")
    amount = int(input("Enter the amount : "))
    category = input("Enter the category: ")
    description = input("Enter the description: ")


    #create dictionary
    expense = {
        'date' : date,
        'amount' : amount,
        'category' : category,
        'description' : description,
    }

    #adding data to the list
    Expenses.append(expense)

def display_expenses():
    if not Expenses:
        print("No expenses recorded: ")
        return

    #iterate through all expenses in dictionary and print
    for i,expense in enumerate(Expenses , start=1):
        print(f"{i}. Date: {expense['date']} , Amount: {expense['amount']},"
        f"Category: {expense['category']}, Description: {expense['description']}")

# calculating total expenses
def Total_expenses():
    if not Expenses:
        print("No expenses recorded")

    Total = sum(expense['amount'] for expense in Expenses )
    print(f"total Expenses {Total}:")

def main():
    while True:
        print("Options")
        print("1: Add expenses:")
        print("2: Display expenses:")
        print("3: Total Expenses:")

        user_choice = input("Choose ..\n")

        if user_choice == '1':
            add_expenses()
        elif user_choice == '2':
            display_expenses()
        elif user_choice == '3':
            Total_expenses()
        elif user_choice == '4':
            print("BYE BYE:")
        else:
            print("Invalid choice , try again!")

         
    check_total = Total_expenses()
  
    if check_total <= 10000:
        print("Bhosdi ke kahan le ke jayga.")
    else:
        print("Uraaaa Uraaaa")

    #start the program....
if __name__ == "__main__":
    main()
     