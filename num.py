import random

secret_number = random.randint(1, 100)
attempts = 0
max_attempts = 10

print("Welcome to the Number Guessing Game!")

while attempts < max_attempts:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
        break
else:
    print(f"Sorry, you've reached the maximum number of attempts. The correct number was {secret_number}. Game over!")
