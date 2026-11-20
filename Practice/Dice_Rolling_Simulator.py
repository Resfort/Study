import random

def roll_dice():
    throws = int(input("Enter the number of times to roll the dice: "))
    results = []
    for _ in range(throws):
        roll = random.randint(1, 6)
        results.append(roll)
    print(f"Results: {results}")
if __name__ == "__main__":
    roll_dice()