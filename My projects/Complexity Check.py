from english_words import get_english_words_set

english_words_dictionary = get_english_words_set(['web2'], lower=True)


def check_strength(password):
    
    if  password in english_words_dictionary:
        return "Weak(Password is a common English word)"

    
    if len(password) < 8:
        return "Weak"
    
    has_number = False
    has_uppercase = False
    has_symbol = False

    for char in password:
        if char.isdigit():
            has_number = True
        if char.isupper():
            has_uppercase = True
        if char in "!@#$%^&*()-+.,_=":
            has_symbol = True

    score = 0
    if has_number: score += 1
    if has_uppercase: score += 1
    if has_symbol: score += 1

    if score == 3:
        return "Strong"
    elif score == 2:
        return "Medium"
    else:
        return "Weak"


user_password = input("Enter your password: ")
strength = check_strength(user_password)

print(f"Your password strength is: {strength}")