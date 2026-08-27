import os
import sqlite3

# حساب المسار التلقائي للملف بغض النظر عن مكان تشغيل الطرفية
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "atm_system.db")

#حل مشكلة ValueError
def get_safe_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")




# اسم المستخدم والرقم السري
name = input("Enter your name: ")
ATM = get_safe_int("Enter your ATM pin: ")


# 1. الاتصال بقاعدة البيانات لقراءة الحساب
connection = sqlite3.connect(db_path)
cursor = connection.cursor()

# 2. أمر SQL لجلب بيانات الـ pin والحساب الجاري والادخار
cursor.execute("SELECT user_name, pin, checking, savings FROM accounts")
account_data = cursor.fetchone()  # هذا الأمر يجلب الصف الأول على شكل Tuple

connection.close() # نغلق الاتصال بعد القراءة بسلام

# 3. توزيع البيانات المسترجعة على متغيراتك القديمة لكي يظل باقي الكود يعمل كما هو!
user_name = account_data[0]  # سيأخذ القيمة 1234 من القاعدة
ATM_number = account_data[1]       # سيأخذ القيمة 1234 من القاعدة
checking_balance = account_data[2] # سيأخذ القيمة 10000.0 من القاعدة
savings_balance = account_data[3]  # سيأخذ القيمة 5000.0 من القاعدة

balance = checking_balance + savings_balance  # مجموع الحسابين
# Number of password attempts
max_attempts = 3 
history = []
# Daily withdrawal limit
daily_limit = 2000
total_withdraw = 0

# دالة الإيداع
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

# دالة السحب
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

while ATM != ATM_number and max_attempts > 0:
    print("Incorrect pin. Please try again.")
    ATM = get_safe_int("Enter your ATM pin: ")
    max_attempts -= 1       
    if max_attempts == 0:
        print("You have exceeded the maximum number of attempts. Please try again later.")
        exit()

while name != user_name and max_attempts > 0:
    print("Incorrect name. Please try again.")
    name = input("Enter your name: ")
    max_attempts -= 1       
    if max_attempts == 0:
        print("You have exceeded the maximum number of attempts. Please try again later.")
        exit()

while ATM == ATM_number:
    print("Welcome to the ATM!")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. View History")
    print("5. Change Pin")
    print("6. Change Name")
    print("7. Exit")

    choice = get_safe_int("Enter your choice: ")
    
    #عرض الرصيد
    if choice == 1:
        print("Your total balance is: ", balance)
        print("Checking Balance: ", checking_balance)
        print("Savings Balance: ", savings_balance)
    #إداع الاموال
    elif choice == 2:
        old_balance = checking_balance + savings_balance
        checking_balance, savings_balance = deposit(checking_balance, savings_balance)
        balance = checking_balance + savings_balance
        history.append(("Deposit", balance - old_balance))
        print("Your new balance is: ", balance)
        print("Checking Balance: ", checking_balance)
        print("Savings Balance: ", savings_balance)
        # أمر SQL لتحديث الأرصدة الجديدة في قاعدة البيانات
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        cursor.execute("""
            UPDATE accounts 
            SET checking = ?, savings = ?
        """, (checking_balance, savings_balance))
        connection.commit() # حفظ التغيير نهائياً
        connection.close()
    
    # سحب الأموال
    elif choice == 3:
        old_balance = checking_balance + savings_balance
        checking_balance, savings_balance, total_withdraw = withdraw(checking_balance, savings_balance, total_withdraw, daily_limit)
        balance = checking_balance + savings_balance
        history.append(("Withdraw", old_balance - balance))
        if history[-1][1] > 0:  # إذا تم السحب بنجاح
            print("Withdrawal completed successfully.")
        else:
            print("Withdrawal failed.")    
        print("Your new balance is: ", balance)
        print("Checking Balance: ", checking_balance)
        print("Savings Balance: ", savings_balance)
            # أمر SQL لتحديث الأرصدة الجديدة في قاعدة البيانات
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        cursor.execute("""
            UPDATE accounts 
            SET checking = ?, savings = ?
        """, (checking_balance, savings_balance))
        connection.commit() # حفظ التغيير نهائياً
        connection.close()
    elif choice == 4: # عرض تاريخ العمليات
        print("Transaction History:")
        for transaction in history:
            print(transaction[0], ":", transaction[1])
    elif choice == 5: # تغيير الرمز السري
        new_pin = get_safe_int("Enter your new pin: ")
        ATM_number = new_pin
        ATM = new_pin

        # حفظ الرمز السري الجديد في قاعدة البيانات نهائياً!
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        cursor.execute("UPDATE accounts SET pin = ?", (new_pin,))
        connection.commit()
        connection.close()

        print("Your pin has been changed successfully.")
    elif choice == 6: # تغيير الاسم
        new_name = input("Enter your new name: ")
        user_name = new_name
        name = new_name
        # حفظ الاسم الجديد في قاعدة البيانات نهائياً!
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        cursor.execute("UPDATE accounts SET user_name = ?", (new_name,))
        connection.commit()
        connection.close()
        print("Your name has been changed successfully.")
    elif choice == 7: # الخروج من النظام
        print("Exiting the ATM. Goodbye!")
        print("Thank you for using the ATM. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please try again.")                      




