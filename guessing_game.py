import random

print("================================")
print("      NUMBER GUESSING GAME")
print("================================")

number = random.randint(1, 100)
attempts = 0

print("\nI have selected a number between 1 and 100.")
print("Try to guess it!")

while True:

    try:
        guess = int(input("\nEnter your guess: "))

        attempts += 1

        if guess < number:
            print("Too low! Try again.")

        elif guess > number:
            print("Too high! Try again.")

        else:
            print("\nCongratulations!")
            print("You guessed the correct number.")
            print("The number was:", number)
            print("Attempts:", attempts)
            break

    except ValueError:
        print("Please enter a valid whole number.")
