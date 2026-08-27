def deposit(checking_balance, savings_balance):
    amount = get_safe_int("Enter the amount to deposit: ")

    if amount <= 0:
        print("Amount must be positive.")
        return checking_balance, savings_balance

    account_choice = get_safe_int("Choose account to deposit into (1 for Checking, 2 for Savings): ")
    if account_choice == 1:
        checking_balance += amount
    elif account_choice == 2:
        savings_balance += amount
    else:
        print("Invalid account choice.")
        return checking_balance, savings_balance
    print("Deposit completed successfully.")        
    return checking_balance, savings_balance

def withdraw(checking_balance, savings_balance, total_withdraw, daily_limit):
    amount = get_safe_int("Enter the amount to withdraw: ")  
    if amount <= 0:
        print("Amount must be positive.")
        return checking_balance, savings_balance, total_withdraw
    elif total_withdraw + amount > daily_limit:
        print("Daily withdrawal limit exceeded.")
        return checking_balance, savings_balance, total_withdraw
    elif amount %50 != 0:
        print("Amount must be a multiple of 50.")
        return checking_balance, savings_balance, total_withdraw
    account_choice = get_safe_int("Choose account to withdraw from (1 for Checking, 2 for Savings): ")
    if account_choice == 1:
        if amount > checking_balance:
            print("Insufficient funds in Checking account.")
            return checking_balance, savings_balance, total_withdraw
        else:
            checking_balance -= amount
            total_withdraw += amount
            return checking_balance, savings_balance, total_withdraw
    elif account_choice == 2:
        if amount > savings_balance:
            print("Insufficient funds in Savings account.")
            return checking_balance, savings_balance, total_withdraw
        else:
            savings_balance -= amount
            total_withdraw += amount
            return checking_balance, savings_balance, total_withdraw
    else:
        print("Invalid account choice.")
        return checking_balance, savings_balance, total_withdraw




    