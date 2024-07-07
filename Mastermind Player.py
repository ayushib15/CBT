import random

def generate_secret_number():
    return str(random.randint(1000, 9999))  # Generate a 4-digit random number

def get_guess():
    while True:
        guess = input("Enter your guess (4-digit number): ")
        if guess.isdigit() and len(guess) == 4:
            return guess
        else:
            print("Invalid input. Please enter a 4-digit number.")

def evaluate_guess(secret, guess):
    correct_digits = 0
    for i in range(4):
        if guess[i] == secret[i]:
            correct_digits += 1
    return correct_digits

def play_mastermind():
    print("Welcome to Mastermind!")

    player1 = input("Enter name for Player 1: ")
    player2 = input("Enter name for Player 2: ")

    secret_number = generate_secret_number()
    print(f"{player1}, set your secret number.")

    attempts = 0
    while True:
        guess = get_guess()
        attempts += 1

        if guess == secret_number:
            print(f"Congratulations, {player2}! You guessed the number {secret_number} in {attempts} attempts. You are crowned Mastermind!")
            break
        else:
            correct_digits = evaluate_guess(secret_number, guess)
            print(f"{player1} hints: {correct_digits} digit(s) are correct.")

    secret_number = generate_secret_number()
    print(f"\n{player2}, set your secret number.")

    attempts = 0
    while True:
        guess = get_guess()
        attempts += 1

        if guess == secret_number:
            print(f"Congratulations, {player1}! You guessed the number {secret_number} in {attempts} attempts. You are crowned Mastermind!")
            break
        else:
            correct_digits = evaluate_guess(secret_number, guess)
            print(f"{player2} hints: {correct_digits} digit(s) are correct.")

if __name__ == "__main__":
    play_mastermind()

