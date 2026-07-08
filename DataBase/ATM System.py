import string

lower = string.ascii_lowercase
upper = string.ascii_uppercase
symbols = string.punctuation
all_characters = lower + upper + symbols


ATM= int(input("Enter your ATM pin: "))


import sqlite3

# 1. الاتصال بقاعدة البيانات لقراءة الحساب
connection = sqlite3.connect("atm_system.db")
cursor = connection.cursor()

# 2. أمر SQL لجلب بيانات الـ pin والحساب الجاري والادخار
cursor.execute("SELECT pin, checking, savings FROM accounts")
account_data = cursor.fetchone()  # هذا الأمر يجلب الصف الأول على شكل Tuple

connection.close() # نغلق الاتصال بعد القراءة بسلام

# 3. توزيع البيانات المسترجعة على متغيراتك القديمة لكي يظل باقي الكود يعمل كما هو!
ATM_number = account_data[0]       # سيأخذ القيمة 1234 من القاعدة
checking_balance = account_data[1] # سيأخذ القيمة 10000.0 من القاعدة
savings_balance = account_data[2]  # سيأخذ القيمة 5000.0 من القاعدة

balance = checking_balance + savings_balance  # مجموع الحسابين
# Number of password attempts
max_attempts = 3
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
    

    if choice == 1:
        print("Your total balance is: ", balance)
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
        balance += deposit
        history.append(("Deposit", deposit))
        print("Your new balance is: ", balance)
        print("Checking Balance: ", checking_balance)
        print("Savings Balance: ", savings_balance)
        # أمر SQL لتحديث الأرصدة الجديدة في قاعدة البيانات
        connection = sqlite3.connect("atm_system.db")
        cursor = connection.cursor()
        cursor.execute("""
            UPDATE accounts 
            SET checking = ?, savings = ?
        """, (checking_balance, savings_balance))
        connection.commit() # حفظ التغيير نهائياً
        connection.close()
    elif choice == 3:
        balance_choice = int(input("Enter 1 for Checking or 2 for Savings: "))
        withdraw= int(input("Enter the amount to withdraw:"))
        
        if withdraw > balance:
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
                    success = True
            elif balance_choice == 2:
                if withdraw > savings_balance:
                    print("You don't have enough balance in your savings account.")
                else:
                    savings_balance -= withdraw
                    success = True
            else:
                print("Invalid choice. Please try again.")
                continue
            if success == True:
                balance -= withdraw
                total_withdraw += withdraw
                history.append(("Withdraw", withdraw))
                print("Your new balance is: ", balance)
                print("Checking Balance: ", checking_balance)
                print("Savings Balance: ", savings_balance)
            # أمر SQL لتحديث الأرصدة الجديدة في قاعدة البيانات
        connection = sqlite3.connect("atm_system.db")
        cursor = connection.cursor()
        cursor.execute("""
            UPDATE accounts 
            SET checking = ?, savings = ?
        """, (checking_balance, savings_balance))
        connection.commit() # حفظ التغيير نهائياً
        connection.close()
    elif choice == 4:
        print("Transaction History:")
        for transaction in history:
            print(transaction[0], ":", transaction[1])
    elif choice == 5:
        new_pin = int(input("Enter your new pin: "))
        ATM_number = new_pin
        ATM = new_pin

        # حفظ الرمز السري الجديد في قاعدة البيانات نهائياً!
        connection = sqlite3.connect("atm_system.db")
        cursor = connection.cursor()
        cursor.execute("UPDATE accounts SET pin = ?", (new_pin,))
        connection.commit()
        connection.close()

        print("Your pin has been changed successfully.")
    elif choice == 6:
        print("Thank you for using the ATM. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please try again.")                      




