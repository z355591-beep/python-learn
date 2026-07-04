ATM= int(input("Enter your ATM pin: "))
ATM_number = 1234
max_attempts = 3
Balance = 5000
history = []
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
    print("5. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Your balance is: ", Balance)
    elif choice == 2:
        deposit= int(input("Enter the amount to deposit:"))
        Balance += deposit
        history.append(("Deposit", deposit))
        print("Your new balance is: ", Balance)
    elif choice == 3:
        withdraw= int(input("Enter the amount to withdraw:"))
       
        if withdraw > Balance:
            print("You don't have enough balance")
        
        elif total_withdraw + withdraw > daily_limit:
            print(f"You have exceeded your daily withdrawal limit of {daily_limit}.")
        else:          
            Balance -= withdraw
            total_withdraw += withdraw
            history.append(("Withdraw", withdraw))
            print("Your new balance is: ", Balance)
        
    elif choice == 4:
        print("Transaction History:")
        for transaction in history:
            print(transaction[0], ":", transaction[1])
    elif choice == 5:        
        print("Thank you for using the ATM. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")                      




