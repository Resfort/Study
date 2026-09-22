import random 

def guess_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed = False