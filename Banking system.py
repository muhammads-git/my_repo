#banking system
balance = 50000
Loan_Amount = balance / 2   

def BankAccount():
    print("******Welcome to your Bank Account******* ")
    Account =print(f"Your Current balance is : {balance}")
BankAccount()

while True:
    Account_setting = int(input(f"For\n1: Deposit \n2: Withdraw \n3: Exit \n4: Loan\n"))

    if Account_setting == 1:
        deposit = int(input("How much you want to deposit: "))
        balance = balance + deposit
        print(f"You have successfully deposited Rs:{deposit} into your account:")
        print("Your account balance is :",balance)
  
    if Account_setting == 2:
        withdrawal = int(input("How much you want to withdraw:"))
        if withdrawal > balance:
            print("You have not enough money")
        else:
            balance_new = balance - withdrawal
            print(f"You have successfully withdrew Rs:{withdrawal} from your account")
            print(f"Your current account balance is {balance_new}")
    if Account_setting == 3:
        print("Exiting.....")
        break
    if Account_setting == 4:
        loan = int(input("How much loan would you take?\n"))
        if loan > Loan_Amount:
            print("According to your balance you cannot take this much loan:")
        else:
            print(f"The loan amount is added to your balance , Which will be cut in next deposit")
            balance += loan
            print("You balance is:", balance)
print("Thank you for trusting:")

        