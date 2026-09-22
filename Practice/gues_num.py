import random 

def guess_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed = False
    while not guessed:
        user_guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1
        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            guessed = True
            print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")

print("Welcome to the Number Guessing Game!")

print("You have to guess a number between 1 and 100.")

input("Press Enter to start the game...")

