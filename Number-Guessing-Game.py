from random import randint

correct_number = randint(1, 50)
max_attempts = 5
current_attempt = 0
is_correct = False

while current_attempt < max_attempts and not is_correct:
    guess = int(input("Enter your guess (between 1 and 50): "))
    current_attempt += 1

    if guess == correct_number:
        is_correct = True
        print(f"Congratulations! You've guessed the correct number {correct_number} in {current_attempt} attempts.")

    else:
        print(f"Wrong guess! You have {max_attempts - current_attempt} attempts left.")

if not is_correct:
    print(f"Sorry! You've used all your attempts. The correct number was {correct_number}.")

