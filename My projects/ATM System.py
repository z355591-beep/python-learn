ATM= int(input("Enter your ATM pin: "))
#ATM Password is 1234
ATM_number = 1234
# Number of password attempts
max_attempts = 3
checking_balance = 10000
savings_balance = 5000
Balance = checking_balance + savings_balance
history = []
# Daily withdrawal limit
daily_limit = 2000
total_withdraw = 0

while ATM != ATM_number and max_attempts > 0:
    print("Incorrect pin. Please try again.")
    ATM = int(input("Enter your ATM pin: "))
    max_attempts -= 1

if max_attempts == 0:
    print("You have exceeded the maximum number of attempts. Please try again later.")

while ATM == ATM_number:
    print("Welcome to the ATM!")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. View History")
    print("5. Change Pin")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
#
    if choice == 1:
        print("Your total balance is: ", Balance)
        print("Checking Balance: ", checking_balance)
        print("Savings Balance: ", savings_balance)
    elif choice == 2:
        deposit= int(input("Enter the amount to deposit:"))
        balance_choice = int(input("Enter 1 for Checking or 2 for Savings: "))
        if balance_choice == 1:
            checking_balance += deposit
        elif balance_choice == 2:
            savings_balance += deposit
        else:
            print("Invalid choice. Please try again.")
            continue
        Balance += deposit
        history.append(("Deposit", deposit))
        print("Your new balance is: ", Balance)
        print("Checking Balance: ", checking_balance)
        print("Savings Balance: ", savings_balance)
    elif choice == 3:
        balance_choice = int(input("Enter 1 for Checking or 2 for Savings: "))
        withdraw= int(input("Enter the amount to withdraw:"))
        
        if withdraw > Balance:
            print("You don't have enough balance")
        
        elif total_withdraw + withdraw > daily_limit:
            print(f"You have exceeded your daily withdrawal limit of {daily_limit}.")
        elif withdraw % 50 != 0:
            print("Please enter an amount in multiples of 50.")    
        else:          
            if balance_choice == 1:
                if withdraw > checking_balance:
                    print("You don't have enough balance in your checking account.")
                else:
                    checking_balance -= withdraw
            elif balance_choice == 2:
                if withdraw > savings_balance:
                    print("You don't have enough balance in your savings account.")
                else:
                    savings_balance -= withdraw
            Balance -= withdraw
            total_withdraw += withdraw
            history.append(("Withdraw", withdraw))
            print("Your new balance is: ", Balance)
            print("Checking Balance: ", checking_balance)
            print("Savings Balance: ", savings_balance)
    elif choice == 4:
        print("Transaction History:")
        for transaction in history:
            print(transaction[0], ":", transaction[1])
    elif choice == 5:
        new_pin = int(input("Enter your new pin: "))
        ATM_number = new_pin
        ATM = new_pin
        print("Your pin has been changed successfully.")
    elif choice == 6:
        print("Thank you for using the ATM. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please try again.")                      




