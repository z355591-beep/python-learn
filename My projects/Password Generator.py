import random
import string

def generate_password(length):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    all_characters = lower + upper + digits + symbols
    password = ""
    for i in range(length):
        password += random.choice(all_characters)
    return password

print("Welcome to the Password Generator!")

while True:
    try:
        length = int(input("Enter the desired password length: "))
        if length < 6 or length > 50:
            print("Password length should be between 6 and 50 characters. Please try again.")
            continue
        print(f"Generated password: {generate_password(length)}")
        break
    except ValueError:
        print("Please enter a valid number for the password length.") 


