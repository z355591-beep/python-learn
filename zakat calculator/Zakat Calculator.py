from datetime import datetime


def fixer(promt):
    while True:
        try:
            return float(input(promt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


user_name = input("Enter your name: ").strip()
while True:
    if user_name.replace(" ", "").isalpha():
        print("right name")
        break
    else:
        print("Invalid name. Please enter a valid name consisting of letters only.") 
        user_name = input("Enter your name: ").strip() 
amount = fixer("Enter the amount of money you have: ")
nisab = fixer("Enter the nisab threshold: ")
hawl = input("Have you held this amount for one lunar year? (yes/no): ").strip().lower()

if amount >= nisab and hawl == "yes":
    zakat = amount * 0.025
    print(f"Thank you for using the Zakat Calculator, {user_name}.")
    print(f"You are eligible to pay Zakat. The amount you need to pay is: {zakat:.2f}")

    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("zakat_records.txt", "a", encoding="utf-8") as file:
        file.write(
            f"name: {user_name} | "
            f"date: {date} | amount: {amount} |"
            f"nisab: {nisab:.2f}, zakat: {zakat:.2f}\n"
            )
    print("Your Zakat payment has been recorded.")    
else:
    print("You are not eligible to pay Zakat.")