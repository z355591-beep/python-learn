def password_check(password):
    # Check password length
    if len(password) >= 12:
        return "Strong"
    elif len(password) >= 6 and len(password) < 12:
        return "medium"
    else:
        return "weak"

password = input("Enter your password: ")
print(f"Your password strength is: {password_check(password)}")


